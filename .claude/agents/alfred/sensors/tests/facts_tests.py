#!/usr/bin/env python3
"""Tests for Alfred's facts script.

Run:  python3 .claude/agents/alfred/sensors/tests/facts_tests.py

Uses a throwaway state folder and a throwaway receipts folder, so it never touches
Alfred's real notes or the real receipts. Prints FACTS TESTS PASSED only when every
case passes, so a script can check for that line.
"""
import datetime as dt
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
FACTS = os.path.join(os.path.dirname(HERE), "facts.py")
tmp = tempfile.mkdtemp(prefix="alfred-facts-tests-", dir=os.environ.get("TMPDIR"))
STATE = os.path.join(tmp, "state")
REC = os.path.join(tmp, "receipts")
AUD = os.path.join(tmp, "audits")
os.makedirs(REC)
os.makedirs(AUD)
ENV = dict(os.environ, ALFRED_STATE_DIR=STATE, ALFRED_RECEIPTS_DIR=REC, ALFRED_AUDITS_DIR=AUD)
failures = 0


def run(*args, stdin=""):
    r = subprocess.run([sys.executable, FACTS] + list(args), input=stdin,
                       capture_output=True, text=True, env=ENV, timeout=60)
    return r.returncode, r.stdout


def check(name, ok, detail=""):
    global failures
    failures += 0 if ok else 1
    print(f"  {'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail and not ok else ""))


# 1. the open sheet runs on the real lab and says what it is
rc, out = run("open")
check("open: runs and labels itself as measured", rc == 0 and out.startswith("FACTS —"), out[:80])
check("open: says whether this is the first session today", "first session today:" in out)
check("open: with no receipts, says so plainly", "none yet" in out)
check("open: reports session capture from the sync log", "session capture: " in out, out)
check("open: reports whether the capture launchd job is loaded", "session capture launchd job" in out, out)
check("open: counts sessions with no transcript", "with no transcript in the lab:" in out, out)
check("open: carries the skill check line", "skill check: " in out and "skills and" in out, out)

# capture with an empty sessions folder: the sheet says no run is logged, and does not crash
empty = os.path.join(tmp, "no-sessions")
os.makedirs(empty)
r = subprocess.run([sys.executable, FACTS, "open"], capture_output=True, text=True,
                   env=dict(ENV, SESSIONS_DIR=empty), timeout=60)
check("open: with no sync log, says so as an ALERT", "ALERT session capture: no run logged" in r.stdout, r.stdout)

# 2. follow-ups: one opened and closed later, one still open
with open(os.path.join(REC, "2026-09-10-1200-first-a1b2.md"), "w") as f:
    f.write("---\nid: R-2026-09-10-1200-a1b2\ntype: receipt\nsession_id: s-one\n---\n"
            "**Next session starts with:** open the draft and fix the second section\n\n"
            "## Follow-ups\n- [ ] F-20260910-1200-1: send the brief — owner: Venkat\n"
            "- [ ] F-20260910-1200-2: pull the routine briefs — owner: Alfred\n")
with open(os.path.join(REC, "2026-09-10-1500-second-c3d4.md"), "w") as f:
    f.write("---\nid: R-2026-09-10-1500-c3d4\ntype: receipt\nsession_id: s-two\n---\n"
            "**Next session starts with:** review the pulled briefs\n\n"
            "## Closed\n- F-20260910-1200-1 — sent, see the reply in the thread\n")
rc, out = run("loops")
check("loops: a follow-up closed in a later receipt is not open", "F-20260910-1230-1" not in out, out)
check("loops: the other follow-up is still open", "F-20260910-1200-2" in out and "open follow-ups: 1" in out, out)
rc, out = run("open")
check("open: reads the newest receipt's next step", "review the pulled briefs" in out, out[:300])

# 3. the SessionStart hook: writes a note, hands back the facts and the guide
payload = json.dumps({"session_id": "test-start", "source": "startup", "cwd": "/x",
                      "transcript_path": "/tmp/t.jsonl"})
rc, out = run("session-start", stdin=payload)
ok = rc == 0
try:
    ctx = json.loads(out)["hookSpecificOutput"]["additionalContext"]
except Exception:
    ctx, ok = "", False
check("session-start: returns context for the session", ok and "FACTS —" in ctx and "alfred-close" in ctx, out[:120])
check("session-start: writes the session note", os.path.isfile(os.path.join(STATE, "sessions", "test-start.json")))
rc, out = run("session-start", stdin=json.dumps({"session_id": "test-start", "source": "compact"}))
check("session-start: says nothing on compaction", rc == 0 and out.strip() == "", out[:80])

# 4. the SessionEnd hook: a session that changed files and wrote no receipt leaves a note
mark = os.path.join(STATE, "sessions", "test-end.json")
os.makedirs(os.path.dirname(mark), exist_ok=True)
hour_ago = (dt.datetime.now() - dt.timedelta(hours=2)).isoformat(timespec="seconds")
with open(mark, "w") as f:
    json.dump({"start": hour_ago, "source": "startup"}, f)
rc, _ = run("session-end", stdin=json.dumps({"session_id": "test-end", "reason": "other"}))
note = os.path.join(STATE, "unreceipted", "test-end.json")
check("session-end: no receipt for a session that changed files leaves a note",
      rc == 0 and os.path.isfile(note))
if os.path.isfile(note):
    d = json.load(open(note))
    check("session-end: the note lists what changed", d.get("changed_total", 0) > 0, str(d)[:120])

# 5. ...and a session whose receipt exists leaves no note
mark2 = os.path.join(STATE, "sessions", "test-receipted.json")
with open(mark2, "w") as f:
    json.dump({"start": hour_ago, "source": "startup"}, f)
with open(os.path.join(REC, "2026-09-10-1600-third-e5f6.md"), "w") as f:
    f.write("---\nid: R-2026-09-10-1600-e5f6\ntype: receipt\nsession_id: test-receipted\n---\n")
rc, _ = run("session-end", stdin=json.dumps({"session_id": "test-receipted", "reason": "other"}))
check("session-end: a receipted session leaves no note",
      rc == 0 and not os.path.isfile(os.path.join(STATE, "unreceipted", "test-receipted.json")))

# 6. open reports the unreceipted session as an ALERT
rc, out = run("open")
check("open: flags a session that ended without a receipt", "ALERT sessions that changed files" in out, out[:400])

# 7. close measures a session
rc, out = run("close", "test-end")
check("close: measures what changed since the session began",
      rc == 0 and "CLOSE FACTS" in out and "files changed" in out, out[:120])

# 8. a broken payload never breaks a session start or end
rc, out = run("session-start", stdin="not json")
check("session-start: survives an unreadable payload", rc == 0)
rc, out = run("session-end", stdin="not json")
check("session-end: survives an unreadable payload", rc == 0)

# 9. loops reads follow-ups written by an audit, and a later receipt can close them
# (Venkat, 2026-09-11: an audit finding no sensor reads is a note to nobody)
os.makedirs(os.path.join(AUD, "2026-09-10-test-audit"))
with open(os.path.join(AUD, "2026-09-10-test-audit", "follow-ups.md"), "w") as f:
    f.write("# Follow-ups\n\n- [ ] F-20260910-1230-1: an audit finding — owner: Alfred — first step: look\n")
rc, out = run("loops")
check("loops: sees a follow-up written in an audit folder",
      "F-20260910-1230-1" in out and "audits/2026-09-10-test-audit/follow-ups.md" in out, out[:300])
with open(os.path.join(REC, "2026-09-10-1700-fourth-a1b2.md"), "w") as f:
    f.write("---\nid: R-2026-09-10-1700-a1b2\ntype: receipt\nsession_id: t\n---\n## Closed\n- F-20260910-1230-1 — fixed\n")
rc, out = run("loops")
check("loops: a later receipt closes an audit follow-up", "F-20260910-1230-1" not in out, out[:300])

print(f"\n{'all passed' if not failures else str(failures) + ' failed'}  (scratch folder: {tmp})")
if failures:
    sys.exit(1)
print("FACTS TESTS PASSED")
