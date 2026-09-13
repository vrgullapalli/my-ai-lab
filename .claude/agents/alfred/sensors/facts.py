#!/usr/bin/env python3
"""facts: what a script can prove about the lab, for Alfred's open and close routines.

  facts.py open                 fact sheet for the open routine (plain text)
  facts.py close [SESSION_ID]   what changed since this session started
  facts.py loops                follow-ups still open, read from the receipts
  facts.py session-start        SessionStart hook: note the session began, hand the
                                session the fact sheet and what Alfred should do
  facts.py session-end          SessionEnd hook: if the session changed files and wrote no
                                receipt, leave a note so the next open routine catches it

Read-only, except the two hook commands, which write small notes under
.claude/agents/alfred/state/ (git ignores that folder). Nothing here is ever deleted.

Why a script: the lab's rule is that the AI decides what to investigate and scripts
decide what is true. Agents that grade themselves report false success most of the
time. So every number Alfred puts in front of Venkat about the lab comes from here.

Built 2026-09-10 at Venkat's word, when daily-brief, session-receipt and daily-review
were rebuilt as Alfred's open and close routines. Python 3.9, standard library only.
"""
import datetime as dt
import glob
import json
import os
import re
import subprocess
import sys

LAB = "/Users/venkatgullapalli/Documents/my-ai-lab"
ALFRED = os.path.join(LAB, ".claude", "agents", "alfred")
STATE = os.environ.get("ALFRED_STATE_DIR") or os.path.join(ALFRED, "state")   # tests point this elsewhere
SESSIONS = os.path.join(STATE, "sessions")
UNRECEIPTED = os.path.join(STATE, "unreceipted")
LOG = os.path.join(ALFRED, "LOG.md")
RECEIPTS = os.environ.get("ALFRED_RECEIPTS_DIR") or os.path.join(LAB, "evidence", "receipts")
AUDITS = os.environ.get("ALFRED_AUDITS_DIR") or os.path.join(LAB, "evidence", "audits")   # follow-ups in audits count too (Venkat, 2026-09-11)
GATES_FILE = os.environ.get("ALFRED_GATES_FILE") or os.path.join(LAB, "GATES.md")           # tests point these elsewhere
UNLAZY_DIR = os.environ.get("ALFRED_UNLAZY_DIR") or os.path.join(LAB, ".unlazy")


def state_line():
    """One line from State's own check (context/state/state.py check --summary): counts, conflicts, stale, findings.
    The check decides; this only carries its line. If the script is missing or fails to run, say so; never guess."""
    script = os.path.join(LAB, "context", "state", "state.py")
    if not os.path.isfile(script):
        return "state: no ledger script at context/state/state.py"
    try:
        r = subprocess.run([sys.executable, script, "check", "--summary"], capture_output=True, text=True, timeout=120, cwd=LAB)
        line = (r.stdout.strip().split("\n") or [""])[-1]
        return line or "ALERT state: the check printed nothing"
    except Exception as exc:
        return f"ALERT state: check could not run ({type(exc).__name__})"


def ledger_open():
    """An unlazy ledger is open when GATES.md sits at the root, or when .unlazy/ holds a ledger file.
    The folder alone is not a ledger: the stop hook leaves an empty .unlazy/locks/ behind after a ledger is
    retired, and until 2026-09-13 that empty folder made the sheet report a ledger that was not there."""
    if os.path.isfile(GATES_FILE):
        return True
    for root, dirs, files in os.walk(UNLAZY_DIR):
        dirs[:] = [d for d in dirs if d != "locks"]
        if any(not f.startswith(".") for f in files):
            return True
    return False
SNAPSHOTS = os.path.expanduser("~/Documents/_warehouse/_backups/snapshots")
OFFSITE = os.path.expanduser("~/Library/CloudStorage/Dropbox-Telisina/Venkat Gullapalli/my-ai-lab-backups")
TASKS = os.path.join(LAB, "work-os", "scheduled-tasks")
ENG = os.path.join(LAB, "work-os", "brand-os", "engagement-os")
SEEDS = os.path.join(ENG, "seedbank")
ARCHIE_INBOX = os.path.join(ENG, "agents", "archie", "inbox")
EDITORIAL = os.path.join(ENG, "editorial", "pieces")
OPEN_ITEMS = os.path.join(LAB, "work-os", "upskill-advisor", "records", "open-items.md")
STANDING = os.path.join(LAB, "context", "intent", "STANDING.md")
SESSIONS_DIR = os.environ.get("SESSIONS_DIR") or os.path.join(LAB, "evidence", "sessions")
CLAUDE_PROJECTS = os.environ.get("CLAUDE_PROJECTS") or os.path.expanduser("~/.claude/projects")
CODEX_ROOT = os.environ.get("CODEX_ROOT") or os.path.expanduser("~/.codex")

RECEIPT_NAME = re.compile(r"^(\d{4}-\d{2}-\d{2})-(\d{4})-.+\.md$")
FOLLOWUP_OPEN = re.compile(r"^\s*- \[ \] (F-\d{8}-\d{4}-\d+)\b[:\s—-]*(.*)$")
FOLLOWUP_DONE = re.compile(r"^\s*- \[x\] (F-\d{8}-\d{4}-\d+)\b", re.I)
FOLLOWUP_ID = re.compile(r"\bF-\d{8}-\d{4}-\d+\b")
LOG_LINE = re.compile(r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}) \| ([A-Z0-9-]+) \|")
SKIP_WALK = {".git", "node_modules", ".remember", "__pycache__", ".unlazy", ".venv"}


# ---------------------------------------------------------------- helpers
def now():
    return dt.datetime.now()


def age_days(ts):
    return (now() - dt.datetime.fromtimestamp(ts)).days


def git(repo, *args):
    try:
        r = subprocess.run(["git", "-C", repo] + list(args), capture_output=True,
                           text=True, timeout=6)
        return r.stdout.strip() if r.returncode == 0 else None
    except Exception:
        return None


def read(path):
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return ""


def repos():
    found = []
    for root, dirs, _ in os.walk(LAB):
        depth = root[len(LAB):].count(os.sep)
        if ".git" in dirs:
            found.append(root)
        dirs[:] = [d for d in dirs if d not in SKIP_WALK and d != "evidence" and depth < 4]
    return sorted(found)


def receipts():
    """Session receipts, oldest first. Day reviews are listed separately."""
    if not os.path.isdir(RECEIPTS):
        return [], []
    names = sorted(os.listdir(RECEIPTS))
    sessions = [n for n in names if RECEIPT_NAME.match(n)]
    reviews = [n for n in names if n.endswith("--day-review.md")]
    return sessions, reviews


def front_matter(text):
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    fm = {}
    for line in text[4:end].split("\n"):
        k, _, v = line.partition(":")
        if v:
            fm[k.strip()] = v.strip()
    return fm


def audit_files():
    """Every .md inside a dated audit folder, as (label, path). Audits are new files only,
    so an audit records its follow-ups in a file of its own, in the receipt's F- form."""
    out = []
    for path in sorted(glob.glob(os.path.join(AUDITS, "*", "*.md"))):
        out.append(("audits/" + os.path.relpath(path, AUDITS), path))
    return out


def open_loops():
    """Every follow-up written as '- [ ] F-...' in a receipt or an audit file and not yet
    closed by a receipt ('- [x] F-...' or listed under '## Closed'). Audit findings that
    never reach this list are invisible to the open routine (Venkat, 2026-09-11)."""
    sessions, _ = receipts()
    sources = [(n, os.path.join(RECEIPTS, n)) for n in sessions] + audit_files()
    opened, closed = {}, set()
    for name, path in sources:
        text = read(path)
        in_closed = False
        for line in text.split("\n"):
            if line.startswith("## "):
                in_closed = line.strip().lower().startswith("## closed")
            m = FOLLOWUP_OPEN.match(line)
            if m and not in_closed:
                opened.setdefault(m.group(1), (m.group(2).strip(), name))
            if FOLLOWUP_DONE.match(line) or in_closed:
                closed.update(FOLLOWUP_ID.findall(line))
    rows = []
    for fid, (text, name) in opened.items():
        if fid in closed:
            continue
        born = dt.datetime.strptime(fid[2:10], "%Y%m%d")
        rows.append((fid, text, name, (now() - born).days))
    return sorted(rows, key=lambda r: -r[3])


def log_lines():
    out = []
    for line in read(LOG).split("\n"):
        m = LOG_LINE.match(line)
        if m:
            out.append((dt.datetime.strptime(m.group(1), "%Y-%m-%d %H:%M"), m.group(2), line))
    return out


def changed_since(since):
    """Files in the lab changed after `since`, leaving out git internals, plugin state,
    Alfred's own log and state, and machine noise."""
    cutoff = since.timestamp()
    rows = []
    for root, dirs, files in os.walk(LAB):
        dirs[:] = [d for d in dirs if d not in SKIP_WALK]
        if root.startswith(STATE):
            dirs[:] = []
            continue
        for f in files:
            if f == ".DS_Store":
                continue
            p = os.path.join(root, f)
            if p == LOG:
                continue
            try:
                if os.path.getmtime(p) > cutoff:
                    rows.append(os.path.relpath(p, LAB))
            except OSError:
                pass
    return sorted(rows)


# ---------------------------------------------------------------- open
def first_session_today():
    today = now().strftime("%Y-%m-%d")
    return not any(ts.strftime("%Y-%m-%d") == today and duty == "OPEN"
                   for ts, duty, _ in log_lines())


def capture_lines():
    """Session capture, measured (duty three). Added 2026-09-10 when capture was brought back:
    when the sync last ran, whether the launchd job is loaded, whether its last run failed, and
    how many raw sessions on this machine have no render or a stale one."""
    out = []
    logp = os.path.join(SESSIONS_DIR, "SYNC-LOG.md")
    rows = [l for l in read(logp).split("\n") if l.startswith("| 20")]
    if rows:
        last = rows[-1].split("|")
        when = dt.datetime.strptime(last[1].strip(), "%Y-%m-%d %H:%M")
        hours = int((now() - when).total_seconds() // 3600)
        out.append(f"{'ALERT ' if hours > 24 else ''}session capture: last run {hours} hours ago "
                   f"({last[2].strip()}: {last[3].strip()} rendered, {last[4].strip()} refreshed, {last[6].strip()} skipped)")
    else:
        out.append("ALERT session capture: no run logged in evidence/sessions/SYNC-LOG.md")
    try:
        r = subprocess.run(["launchctl", "list", "com.venkat.session-sync"], capture_output=True, text=True, timeout=5)
        loaded = r.returncode == 0
    except Exception:
        loaded = False
    err = read("/tmp/session-sync.err").strip()
    if not loaded:
        out.append("ALERT session capture launchd job: not loaded (com.venkat.session-sync)")
    elif err:
        out.append(f"ALERT session capture launchd job: loaded, last run failed: {err.splitlines()[-1][-120:]}")
    else:
        out.append("session capture launchd job: loaded")
    stale = 0
    for proj in sorted(glob.glob(os.path.join(CLAUDE_PROJECTS, "*"))):
        for src in glob.glob(os.path.join(proj, "*.jsonl")):
            dest = os.path.join(SESSIONS_DIR, "claude", os.path.basename(src)[:-6] + ".md")
            if not os.path.isfile(dest):
                stale += age_days(os.path.getmtime(src)) >= 1
            elif os.path.getmtime(dest) < os.path.getmtime(src) - 3600 and age_days(os.path.getmtime(src)) >= 1:
                stale += 1
    for src in glob.glob(os.path.join(CODEX_ROOT, "sessions", "**", "*.jsonl"), recursive=True):
        dest = os.path.join(SESSIONS_DIR, "codex", os.path.basename(src)[:-6] + ".md")
        if not os.path.isfile(dest) and age_days(os.path.getmtime(src)) >= 1:
            stale += 1
    out.append(f"{'ALERT ' if stale else ''}sessions older than a day with no transcript in the lab: {stale}")
    return out


def skill_check_line():
    """One line from skill-check.py, the strict path and skill-name check for every skill and
    agent file (2026-09-10). Its number, not Alfred's."""
    script = os.path.join(LAB, ".claude", "skills", "context-check", "skill-check.py")
    if not os.path.isfile(script):
        return "ALERT skill check: script missing (.claude/skills/context-check/skill-check.py)"
    try:
        r = subprocess.run([sys.executable, script, "--summary"], capture_output=True, text=True, timeout=60)
        return r.stdout.strip() or "ALERT skill check: no output"
    except Exception as exc:
        return f"ALERT skill check: could not run ({type(exc).__name__})"


def architecture_check_line():
    """One line from docs/architecture/check.py: the capability map, the definitions, and the lab
    agree (2026-09-12, the capability-architecture entry's own sensor). Its number, not Alfred's."""
    script = os.path.join(LAB, "docs", "architecture", "check.py")
    if not os.path.isfile(script):
        return "ALERT architecture check: script missing (docs/architecture/check.py)"
    try:
        r = subprocess.run([sys.executable, script, "--summary"], capture_output=True, text=True, timeout=60)
        return r.stdout.strip() or "ALERT architecture check: no output"
    except Exception as exc:
        return f"ALERT architecture check: could not run ({type(exc).__name__})"


def sources_line():
    """One line from context/sources/check.py: the source register, coverage, freshness, and source
    discovery (2026-09-12, build step 2 under retrieval). Its number, not Alfred's."""
    script = os.path.join(LAB, "context", "sources", "check.py")
    if not os.path.isfile(script):
        return "ALERT sources: script missing (context/sources/check.py)"
    try:
        r = subprocess.run([sys.executable, script, "--summary"], capture_output=True, text=True, timeout=180)
        return r.stdout.strip() or "ALERT sources: no output"
    except Exception as exc:
        return f"ALERT sources: could not run ({type(exc).__name__})"


def waiting_line():
    """The count of things waiting on Venkat's word and the oldest one, from waiting.py
    (added to the morning brief at his word, 2026-09-10 16:42)."""
    script = os.path.join(ALFRED, "sensors", "waiting.py")
    if not os.path.isfile(script):
        return "ALERT waiting on Venkat: waiting.py missing"
    try:
        out = subprocess.run([sys.executable, script], capture_output=True, text=True, timeout=120,
                             env=dict(os.environ, WAITING_FROM_FACTS="1")).stdout
    except Exception as exc:
        return f"ALERT waiting on Venkat: could not run ({type(exc).__name__})"
    lines = [l for l in out.split("\n") if l.strip()]
    m = re.search(r"— (\d+) items", lines[0]) if lines else None
    first = next((l.strip()[2:] for l in lines[1:] if l.startswith("- ")), "")
    return f"waiting on Venkat: {m.group(1) if m else '?'} items; oldest: {first[:120]}"


def open_sheet():
    t = now()
    today = t.strftime("%Y-%m-%d")
    out = [f"FACTS — {t.strftime('%A %Y-%m-%d %H:%M')} (measured by a script, not anyone's opinion)",
           f"first session today: {'yes' if first_session_today() else 'no'}"]

    sessions, reviews = receipts()
    if sessions:
        last = sessions[-1]
        text = read(os.path.join(RECEIPTS, last))
        m = re.search(r"\*\*Next session starts with:\*\*\s*(.+)", text)
        out.append(f"last receipt: {last}")
        out.append(f"  next session starts with: {m.group(1).strip() if m else '(not written)'}")
    else:
        out.append("last receipt: none yet (evidence/receipts/ is new as of 2026-09-10)")
    yesterday = (t - dt.timedelta(days=1)).strftime("%Y-%m-%d")
    out.append(f"day review for {yesterday}: {'yes' if yesterday + '--day-review.md' in reviews else 'no'}")

    pending = sorted(os.listdir(UNRECEIPTED)) if os.path.isdir(UNRECEIPTED) else []
    pending = [p for p in pending if p.endswith(".json")]
    if pending:
        out.append(f"ALERT sessions that changed files but wrote no receipt: {len(pending)}")
        for p in pending[:3]:
            d = json.loads(read(os.path.join(UNRECEIPTED, p)) or "{}")
            out.append(f"  ended {d.get('end', '?')}, {len(d.get('changed', []))} files changed"
                       f" — note: .claude/agents/alfred/state/unreceipted/{p}")

    loops = open_loops()
    out.append(f"open follow-ups: {len(loops)}")
    for fid, text, name, age in loops[:3]:
        out.append(f"  {fid} ({age} days): {text[:110]}")

    for repo in repos():
        rel = os.path.relpath(repo, LAB)
        dirty = git(repo, "status", "--porcelain")
        n = len(dirty.split("\n")) if dirty else 0
        remote = git(repo, "remote")
        ahead = git(repo, "rev-list", "--count", "@{u}..HEAD") if remote else None
        bits = [f"uncommitted {n}"]
        bits.append(f"unpushed {ahead}" if ahead else ("no remote" if not remote else "pushed"))
        flag = "ALERT " if (ahead and int(ahead) > 0) else ""
        out.append(f"{flag}repo {rel}: " + ", ".join(bits))

    snaps = sorted([os.path.join(SNAPSHOTS, f) for f in os.listdir(SNAPSHOTS)
                    if f.endswith(".tar.gz")], key=os.path.getmtime) if os.path.isdir(SNAPSHOTS) else []
    if snaps:
        age = age_days(os.path.getmtime(snaps[-1]))
        out.append(f"{'ALERT ' if age > 3 else ''}last snapshot: {os.path.basename(snaps[-1])} ({age} days old)")
    else:
        out.append("ALERT last snapshot: none found")
    # driver 2 in context/intent/STANDING.md: the work survives losing a machine. A copy on this laptop does not count.
    off = sorted([os.path.join(OFFSITE, f) for f in os.listdir(OFFSITE) if f.endswith(".tar.gz")],
                 key=os.path.getmtime) if os.path.isdir(OFFSITE) else []
    if off:
        age = age_days(os.path.getmtime(off[-1]))
        out.append(f"{'ALERT ' if age > 7 else ''}last off-machine copy (Dropbox): {os.path.basename(off[-1])} ({age} days old)")
    else:
        out.append("ALERT last off-machine copy: none found in Dropbox")

    lines = log_lines()
    if lines:
        hours = int((t - lines[-1][0]).total_seconds() // 3600)
        out.append(f"{'ALERT ' if hours > 72 else ''}Alfred's log: last line {hours} hours ago ({lines[-1][1]})")

    pulled, total = 0, 0
    if os.path.isdir(TASKS):
        for task in sorted(os.listdir(TASKS)):
            if os.path.isfile(os.path.join(TASKS, task, "ROUTINE.md")):
                total += 1
                pulled += os.path.isfile(os.path.join(TASKS, task, "outputs", today + ".md"))
    out.append(f"cloud routine briefs pulled into the lab today: {pulled} of {total}")

    text = read(OPEN_ITEMS)
    if text:
        m = re.search(r"^#+ .*Needs Venkat.*?$(.*?)(?=^#+ |\Z)", text, re.M | re.S)
        n = len(re.findall(r"^\s*[-*\d]", m.group(1), re.M)) if m else 0
        out.append(f"Telegraph items needing Venkat: {n} (file last changed "
                   f"{age_days(os.path.getmtime(OPEN_ITEMS))} days ago)")

    if os.path.isdir(ARCHIE_INBOX):
        items = [os.path.join(ARCHIE_INBOX, f) for f in os.listdir(ARCHIE_INBOX)
                 if not f.startswith(".") and f.lower() != "readme.md"]
        if items:
            oldest = min(items, key=os.path.getmtime)
            out.append(f"ARCHIE inbox: {len(items)} waiting, oldest {age_days(os.path.getmtime(oldest))} days"
                       f" ({os.path.basename(oldest)})")
        else:
            out.append("ARCHIE inbox: empty")

    if os.path.isdir(EDITORIAL):
        for piece in sorted(os.listdir(EDITORIAL)):
            rec = read(os.path.join(EDITORIAL, piece, "00-run-record.md"))
            nxt = [l for l in rec.split("\n") if "| pending" in l.lower()]
            if nxt:
                gate = nxt[0].split("|")[1].strip()
                out.append(f"article '{piece}': next gate pending: {gate[:70]}")

    if os.path.isdir(SEEDS):
        count = sum(len([f for f in os.listdir(os.path.join(SEEDS, s)) if f.endswith(".md")])
                    for s in ("session", "written", "spoken") if os.path.isdir(os.path.join(SEEDS, s)))
        sess = [os.path.join(SEEDS, "session", f) for f in os.listdir(os.path.join(SEEDS, "session"))]
        newest = age_days(max(map(os.path.getmtime, sess))) if sess else None
        missed = len(re.findall(r"^\| 20\d\d-", read(os.path.join(SEEDS, "missed.md")), re.M))
        out.append(f"seed files: {count}; newest live-session seed {newest} days ago; missed-seed rows: {missed}")

    if ledger_open():
        out.append("unlazy: a gates ledger is open at the lab root (GATES.md or .unlazy/)")

    out.extend(capture_lines())
    out.append(skill_check_line())
    out.append(architecture_check_line())
    out.append(state_line())
    out.append(sources_line())
    out.append(waiting_line())

    if lines and os.path.isfile(STANDING):
        opens = [ts for ts, duty, _ in lines if duty == "OPEN"]
        if opens and os.path.getmtime(STANDING) > opens[-1].timestamp():
            out.append("current drivers changed since the last open routine (context/intent/STANDING.md)")
    return "\n".join(out)


# ---------------------------------------------------------------- close
def session_marker(session_id=None):
    if not os.path.isdir(SESSIONS):
        return None, {}
    if session_id:
        p = os.path.join(SESSIONS, session_id + ".json")
        return (session_id, json.loads(read(p) or "{}")) if os.path.isfile(p) else (None, {})
    marks = sorted((f for f in os.listdir(SESSIONS) if f.endswith(".json")),
                   key=lambda f: os.path.getmtime(os.path.join(SESSIONS, f)))
    if not marks:
        return None, {}
    sid = marks[-1][:-5]
    return sid, json.loads(read(os.path.join(SESSIONS, marks[-1])) or "{}")


def close_sheet(session_id=None):
    sid, mark = session_marker(session_id)
    if not mark:
        return "No session-start note found, so 'what changed' cannot be measured for this session."
    since = dt.datetime.fromisoformat(mark["start"])
    out = [f"CLOSE FACTS — session {sid}, started {since.strftime('%Y-%m-%d %H:%M')} (measured by a script)"]
    changed = changed_since(since)
    out.append(f"files changed in the lab since the session started: {len(changed)}")
    groups = {}
    for rel in changed:
        key = "/".join(rel.split("/")[:3])
        groups[key] = groups.get(key, 0) + 1
    for key, n in sorted(groups.items(), key=lambda kv: -kv[1])[:15]:
        out.append(f"  {n:4}  {key}")
    for repo in repos():
        commits = git(repo, "log", "--since=" + since.isoformat(), "--oneline")
        dirty = git(repo, "status", "--porcelain")
        n = len(dirty.split("\n")) if dirty else 0
        if commits or n:
            c = len(commits.split("\n")) if commits else 0
            out.append(f"repo {os.path.relpath(repo, LAB)}: {c} commits this session, {n} uncommitted")
    new_seeds = [r for r in changed if r.startswith("work-os/brand-os/engagement-os/seedbank/session/")]
    out.append(f"seeds written this session: {len(new_seeds)}")
    new_receipts = [r for r in changed if r.startswith("evidence/receipts/")]
    out.append(f"receipts written this session: {len(new_receipts)}")
    logged = [l for ts, _, l in log_lines() if ts >= since.replace(second=0, microsecond=0)]
    out.append(f"lines Alfred logged this session: {len(logged)}")
    if os.path.isfile(os.path.join(LAB, "GATES.md")):
        out.append("unlazy ledger GATES.md is open at the lab root — check it before closing")
    return "\n".join(out)


# ---------------------------------------------------------------- hooks
def hook_payload():
    try:
        return json.loads(sys.stdin.read() or "{}")
    except ValueError:
        return {}


def session_start():
    p = hook_payload()
    sid = str(p.get("session_id") or "unknown")
    source = p.get("source", "startup")
    os.makedirs(SESSIONS, exist_ok=True)
    mark = os.path.join(SESSIONS, sid + ".json")
    if source in ("startup", "clear") or not os.path.isfile(mark):
        with open(mark, "w") as f:
            json.dump({"start": now().isoformat(timespec="seconds"), "source": source,
                       "transcript_path": p.get("transcript_path"), "cwd": p.get("cwd")}, f)
    if source == "compact":
        return  # the session is continuing; the facts were given when it began
    sheet = open_sheet()
    first = "first session today: yes" in sheet and source == "startup"
    guide = ["", "ALFRED — what to do with the facts above (lab hook, 2026-09-10):"]
    if first:
        guide.append("- This is the first session today. Run the `alfred-open` skill. If Venkat's first "
                     "message is urgent, answer it first, then run the open routine.")
    else:
        guide.append("- Not the first session today: do not run the open routine unasked. If any line "
                     "above starts with ALERT, mention it in one plain line at the top of your first answer.")
    guide.append("- When the work is done, or Venkat says wrap up, close out, or done for today, run "
                 "the `alfred-close` skill. Session id for the receipt: " + sid)
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "SessionStart",
                                             "additionalContext": sheet + "\n" + "\n".join(guide)}}))


def session_end():
    p = hook_payload()
    sid = str(p.get("session_id") or "")
    mark_path = os.path.join(SESSIONS, sid + ".json")
    if not sid or not os.path.isfile(mark_path):
        return
    mark = json.loads(read(mark_path) or "{}")
    end = now().isoformat(timespec="seconds")
    mark["end"], mark["end_reason"] = end, p.get("reason")
    with open(mark_path, "w") as f:
        json.dump(mark, f)
    changed = changed_since(dt.datetime.fromisoformat(mark["start"]))
    if not changed:
        return
    sessions, _ = receipts()
    if any(("session_id: " + sid) in read(os.path.join(RECEIPTS, n)) for n in sessions[-20:]):
        return
    os.makedirs(UNRECEIPTED, exist_ok=True)
    with open(os.path.join(UNRECEIPTED, sid + ".json"), "w") as f:
        json.dump({"session_id": sid, "start": mark["start"], "end": end,
                   "reason": p.get("reason"), "transcript_path": p.get("transcript_path") or mark.get("transcript_path"),
                   "changed": changed[:200], "changed_total": len(changed)}, f, indent=2)


# ---------------------------------------------------------------- main
def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "open"
    try:
        if cmd == "open":
            print(open_sheet())
        elif cmd == "close":
            print(close_sheet(sys.argv[2] if len(sys.argv) > 2 else None))
        elif cmd == "loops":
            rows = open_loops()
            print(f"open follow-ups: {len(rows)}")
            for fid, text, name, age in rows:
                print(f"  {fid} ({age} days, from {name}): {text}")
        elif cmd == "session-start":
            session_start()
        elif cmd == "session-end":
            session_end()
        else:
            print(__doc__)
            sys.exit(2)
    except Exception as exc:
        # a hook must never break a session start or end
        if cmd in ("session-start", "session-end"):
            print(json.dumps({"systemMessage": "Alfred's facts script hit an error (" +
                              exc.__class__.__name__ + ": " + str(exc)[:120] + "); continuing without it."}))
            sys.exit(0)
        raise


if __name__ == "__main__":
    main()
