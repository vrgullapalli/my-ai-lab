#!/usr/bin/env python3
"""capture-report: what the session-capture run just proved, in plain text.

  capture-report.py             report on the last sync run and the last 7 days
  capture-report.py --days N    widen or narrow the window
  capture-report.py --session ID   one session: its render path, counts, skills, agents

Reads only: evidence/sessions/SYNC-LOG.md, evidence/sessions/USAGE.jsonl, the launchd
job's stderr file, `launchctl list`. Writes nothing. Standard library only, Python 3.9.

Why it exists (Venkat, 2026-09-10): a rebuild must beat the original. The old capture
button, when it existed, said "N rendered". This one also says which skills and agents the
lab actually used, which sessions were skipped and why, which renders are partial, and
whether the timed job is alive. Every number comes from files the sync script wrote.
"""
import argparse
import collections
import datetime as dt
import json
import os
import re
import subprocess

LAB = os.environ.get("LAB_ROOT") or "/Users/venkatgullapalli/Documents/my-ai-lab"
SESS = os.path.join(LAB, "evidence", "sessions")
SYNC_LOG = os.path.join(SESS, "SYNC-LOG.md")
USAGE = os.path.join(SESS, "USAGE.jsonl")
JOB = "com.venkat.session-sync"
JOB_ERR = "/tmp/session-sync.err"


def last_sync_line():
    rows = [l for l in open(SYNC_LOG, encoding="utf-8") if l.startswith("| 20")]
    if not rows:
        return None
    cells = [c.strip() for c in rows[-1].strip().strip("|").split("|")]
    keys = ["run", "source", "rendered", "refreshed", "unchanged", "skipped", "notes"]
    return dict(zip(keys, cells))


def usage_rows():
    if not os.path.exists(USAGE):
        return []
    out = []
    for line in open(USAGE, encoding="utf-8"):
        line = line.strip()
        if line:
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return out


def parse_iso(s):
    if not s or s == "None":
        return None
    try:
        return dt.datetime.fromisoformat(s.replace("Z", "+00:00")).astimezone().replace(tzinfo=None)
    except ValueError:
        return None


def job_state():
    """Status from launchctl, plus the error file with its time. A status of 0 right after a
    reload proves nothing, so the last error line is always shown while the file is non-empty."""
    try:
        out = subprocess.run(["launchctl", "list"], capture_output=True, text=True, timeout=10).stdout
    except Exception as e:  # noqa: BLE001
        return f"could not ask launchctl ({e})"
    status = None
    for line in out.splitlines():
        if line.strip().endswith(JOB):
            status = line.split()[1]
    if status is None:
        return "not loaded"
    msg = f"loaded, last exit {status}"
    if os.path.exists(JOB_ERR) and os.path.getsize(JOB_ERR) > 0:
        tail = open(JOB_ERR, errors="ignore").read().strip().splitlines()
        when = dt.datetime.fromtimestamp(os.path.getmtime(JOB_ERR)).strftime("%Y-%m-%d %H:%M")
        msg += f'; error file last written {when}: "{tail[-1][-160:]}"'
        msg += "\n  (a clean run empties nothing; if the error time is after the last exit-0 run, the job is still failing)"
    else:
        msg += "; no error file"
    return msg


def one_session(rows, sid):
    hits = [r for r in rows if sid in r.get("id", "")]
    if not hits:
        print(f"No usage line for a session matching {sid!r}. Run session-sync.py --once {sid} first.")
        return
    for r in hits:
        print(f"Session {r['id']} ({r.get('source')})")
        print(f"  render: {r.get('render')}")
        print(f"  started {r.get('started')}  last {r.get('last')}")
        print(f"  Venkat turns {r.get('venkat_turns')} · replies {r.get('replies')} · tool calls {r.get('tool_calls')} · subagents {r.get('subagents')}")
        print(f"  skills: {', '.join(r.get('skills') or []) or 'none'}")
        print(f"  agents: {', '.join(r.get('agents') or []) or 'none'}")
        print(f"  commands: {', '.join(r.get('commands') or []) or 'none'}")
        if r.get("partial"):
            print(f"  partial: {r['partial']}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--days", type=int, default=7)
    ap.add_argument("--session")
    a = ap.parse_args()
    rows = usage_rows()
    if a.session:
        one_session(rows, a.session)
        return

    last = last_sync_line()
    print("LAST RUN")
    if last:
        print(f"  {last['run']} · {last['rendered']} rendered · {last['refreshed']} refreshed · "
              f"{last['unchanged']} unchanged · {last['skipped']} skipped")
        if last["notes"] and last["notes"] != "—":
            print(f"  note: {last['notes']}")
    else:
        print("  no run recorded in SYNC-LOG.md")

    since = dt.datetime.now() - dt.timedelta(days=a.days)
    recent = [r for r in rows if (parse_iso(r.get("last")) or dt.datetime.min) >= since]
    print(f"\nLAST {a.days} DAYS  ({len(recent)} sessions with a dated render, of {len(rows)} in the ledger)")
    skills = collections.Counter(s for r in recent for s in (r.get("skills") or []))
    agents = collections.Counter(s for r in recent for s in (r.get("agents") or []))
    turns = sum(r.get("venkat_turns") or 0 for r in recent)
    calls = sum(r.get("tool_calls") or 0 for r in recent)
    subs = sum(r.get("subagents") or 0 for r in recent)
    print(f"  Venkat turns {turns} · tool calls {calls} · subagents spawned {subs}")
    print("  skills used: " + (", ".join(f"{k} x{v}" for k, v in skills.most_common()) or "none recorded"))
    print("  agents used: " + (", ".join(f"{k} x{v}" for k, v in agents.most_common()) or "none recorded"))
    silent = [r["id"][:8] for r in recent if not (r.get("skills") or r.get("agents")) and (r.get("venkat_turns") or 0) >= 3]
    if silent:
        print(f"  sessions with 3+ turns and no skill or agent: {len(silent)} ({', '.join(silent)})")
    partial = [r["id"][:8] for r in rows if r.get("partial")]
    if partial:
        print(f"  renders marked partial (older format, skill names unknown): {len(partial)}")

    skipped = []
    for l in open(SYNC_LOG, encoding="utf-8"):
        m = re.search(r"SKIPPED \((.*?)\): (\S+)", l)
        if m and l.startswith("| 20"):
            skipped.append((l[2:18], m.group(2), m.group(1)))
    print("\nSKIPPED, EVER (never written, by design)")
    if skipped:
        seen = set()
        for when, f, why in skipped:
            if f not in seen:
                seen.add(f)
                print(f"  {f}  {why}  (first seen {when})")
    else:
        print("  none")

    print("\nTIMED JOB")
    print(f"  {JOB}: {job_state()}")


if __name__ == "__main__":
    main()
