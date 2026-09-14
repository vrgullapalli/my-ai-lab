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
import re
import shutil
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
check("open: carries the architecture check line", "architecture check: " in out and "registry entries" in out, out)
check("open: carries the source register line", "sources: " in out and "registered" in out, out)
check("open: carries the State line from state.py check", "state: " in out and "current lines" in out, out)

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

# unlazy ledger line: an empty .unlazy/ (only a locks/ folder) is not an open ledger; a ledger file is (2026-09-13)
unl = os.path.join(tmp, "unlazy-empty"); os.makedirs(os.path.join(unl, "locks"))
gates_missing = os.path.join(tmp, "no-GATES.md")
r = subprocess.run([sys.executable, FACTS, "open"], capture_output=True, text=True,
                   env=dict(ENV, ALFRED_UNLAZY_DIR=unl, ALFRED_GATES_FILE=gates_missing), timeout=60)
check("open: an empty .unlazy/ with only locks/ does not report an open ledger", "gates ledger is open" not in r.stdout, r.stdout)
os.makedirs(os.path.join(unl, "scope-1")); open(os.path.join(unl, "scope-1", "PLAN.md"), "w").write("# plan\n")
r = subprocess.run([sys.executable, FACTS, "open"], capture_output=True, text=True,
                   env=dict(ENV, ALFRED_UNLAZY_DIR=unl, ALFRED_GATES_FILE=gates_missing), timeout=60)
check("open: a ledger file under .unlazy/ reports an open ledger (planted fault)", "gates ledger is open" in r.stdout, r.stdout)
gates = os.path.join(tmp, "GATES.md"); open(gates, "w").write("# Gates\n")
r = subprocess.run([sys.executable, FACTS, "open"], capture_output=True, text=True,
                   env=dict(ENV, ALFRED_UNLAZY_DIR=os.path.join(tmp, "no-unlazy"), ALFRED_GATES_FILE=gates), timeout=60)
check("open: GATES.md at the root reports an open ledger (planted fault)", "gates ledger is open" in r.stdout, r.stdout)


# 10. F-20260912-0117-4: under '## Closed', only a line that starts with '- F-' or '- [x] F-' closes a follow-up
with open(os.path.join(REC, "2026-09-10-1800-fifth-b2c3.md"), "w") as f:
    f.write("---\nid: R-2026-09-10-1800-b2c3\ntype: receipt\nsession_id: t5\n---\n## Closed\n"
            "- F-20260910-1230-1 — already closed; F-20260910-1200-2 is still open, the routine briefs were not pulled\n")
rc, out = run("loops")
check("loops: a follow-up only mentioned in a sentence under '## Closed' stays open (planted fault)",
      "F-20260910-1200-2" in out, out[:300])
with open(os.path.join(REC, "2026-09-10-1900-sixth-c3d4.md"), "w") as f:
    f.write("---\nid: R-2026-09-10-1900-c3d4\ntype: receipt\nsession_id: t6\n---\n## Closed\n"
            "- F-20260910-1200-2 — pulled, see the outputs folder\n")
rc, out = run("loops")
check("loops: a '- F-...' line under '## Closed' closes it", "F-20260910-1200-2" not in out, out[:300])

# 11. F-20260912-0150-2: the drivers line appears only when STANDING.md changed after the last OPEN line in the log
scratch_log = os.path.join(tmp, "LOG.md")
open(scratch_log, "w").write("2026-09-10 08:00 | OPEN | ran | brief given | facts.py open\n")
standing = os.path.join(tmp, "STANDING.md")
open(standing, "w").write("# Standing\n")
denv = dict(ENV, ALFRED_LOG_FILE=scratch_log, ALFRED_STANDING_FILE=standing)
r = subprocess.run([sys.executable, FACTS, "open"], capture_output=True, text=True, env=denv, timeout=90)
check("open: current drivers changed since the last open routine (planted fault)",
      "current drivers changed since the last open routine" in r.stdout, r.stdout[-400:])
old_ts = dt.datetime(2026, 9, 9, 12, 0).timestamp()
os.utime(standing, (old_ts, old_ts))
r = subprocess.run([sys.executable, FACTS, "open"], capture_output=True, text=True, env=denv, timeout=90)
check("open: drivers older than the last open routine give no drivers line",
      "current drivers changed since the last open routine" not in r.stdout, r.stdout[-400:])

# 12. F-20260914-0238-5: the career model line, proven on a scratch mirror of the model folder with one spoke pointer broken
LAB = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(HERE)))))
mirror = os.path.join(tmp, "lab-mirror")
model_src = os.path.join(LAB, "work-os", "brand-os", "model")
model_dst = os.path.join(mirror, "work-os", "brand-os", "model")
shutil.copytree(model_src, model_dst)
spokes_text = open(os.path.join(model_dst, "SPOKES.md")).read()
spoke_paths = re.findall(r"^\|[^|]*\|\s*`([^`]+)`", spokes_text, re.M)
for rel in spoke_paths:                      # the mirror holds each spoke file at the same relative path
    src = os.path.join(LAB, rel)
    if os.path.isfile(src):
        os.makedirs(os.path.dirname(os.path.join(mirror, rel)), exist_ok=True)
        shutil.copy(src, os.path.join(mirror, rel))
menv = dict(ENV, ALFRED_MODEL_DIR=model_dst)
r = subprocess.run([sys.executable, FACTS, "open"], capture_output=True, text=True, env=menv, timeout=90)
m1 = re.search(r"^career model check: spokes broken (\d+), never-cite hits (\d+), (.+)$", r.stdout, re.M)
check("open: carries the career model check line with plain words", bool(m1), r.stdout[-400:])
first_spoke = next((p for p in spoke_paths if os.path.isfile(os.path.join(mirror, p))), None)
open(os.path.join(model_dst, "SPOKES.md"), "w").write(spokes_text.replace("`" + first_spoke + "`", "`" + first_spoke + ".gone`", 1))
r = subprocess.run([sys.executable, FACTS, "open"], capture_output=True, text=True, env=menv, timeout=90)
m2 = re.search(r"^career model check: spokes broken (\d+),", r.stdout, re.M)
check("open: one broken spoke pointer raises the spokes-broken count by one (planted fault)",
      bool(m1 and m2 and first_spoke) and int(m2.group(1)) == int(m1.group(1)) + 1,
      f"{m1 and m1.group(1)} -> {m2 and m2.group(1)}, spoke {first_spoke}")

# 13. F-20260914-0239-2: session notes that ended with no transcript on disk are counted
rc, out = run("open")
m = re.search(r"^sessions with a note but no transcript: (\d+)$", out, re.M)
check("open: carries the notes-with-no-transcript line", bool(m), out[-400:])
before = int(m.group(1)) if m else -1
with open(os.path.join(STATE, "sessions", "test-lost.json"), "w") as f:
    json.dump({"start": hour_ago, "end": hour_ago, "source": "startup",
               "transcript_path": os.path.join(tmp, "never-written.jsonl")}, f)
with open(os.path.join(STATE, "sessions", "test-kept.json"), "w") as f:      # a note whose transcript exists does not count
    json.dump({"start": hour_ago, "end": hour_ago, "source": "startup", "transcript_path": FACTS}, f)
rc, out = run("open")
m = re.search(r"^sessions with a note but no transcript: (\d+)$", out, re.M)
check("open: a note whose transcript is missing raises the count by exactly one (planted fault)",
      bool(m) and int(m.group(1)) == before + 1, f"{before} -> {m and m.group(1)}")

# 14. F-20260913-0545-3: the retrieval index line says how old the index is and how many markdown files are newer
index = os.path.join(tmp, "retrieval-index.jsonl")
open(index, "w").write("{}\n")
ten_days = (dt.datetime.now() - dt.timedelta(days=10, hours=1)).timestamp()
os.utime(index, (ten_days, ten_days))
ienv = dict(ENV, ALFRED_RETRIEVAL_INDEX=index)
r = subprocess.run([sys.executable, FACTS, "open"], capture_output=True, text=True, env=ienv, timeout=90)
m = re.search(r"^retrieval index: (\d+) days old; (\d+) markdown files in the lab are newer than it$", r.stdout, re.M)
check("open: an index ten days old is reported as ten days old with newer markdown files counted (planted fault)",
      bool(m) and m.group(1) == "10" and int(m.group(2)) > 0, r.stdout[-400:])
os.utime(index, None)
r = subprocess.run([sys.executable, FACTS, "open"], capture_output=True, text=True, env=ienv, timeout=90)
m = re.search(r"^retrieval index: (\d+) days old; (\d+) markdown", r.stdout, re.M)
check("open: an index touched just now is zero days old", bool(m) and m.group(1) == "0", r.stdout[-400:])
r = subprocess.run([sys.executable, FACTS, "open"], capture_output=True, text=True,
                   env=dict(ENV, ALFRED_RETRIEVAL_INDEX=os.path.join(tmp, "no-index.jsonl")), timeout=90)
check("open: a missing index is said plainly", "retrieval index: none at" in r.stdout, r.stdout[-400:])

# 15. F-20260910-1627-3: close counts only the files this session's own transcript touched
tdir = os.path.join(tmp, "transcripts")
os.makedirs(os.path.join(tdir, "test-own", "subagents"))
def tool_use(name, inp):
    return json.dumps({"type": "assistant", "message": {"content": [{"type": "tool_use", "name": name, "input": inp}]}}) + "\n"
with open(os.path.join(tdir, "test-own.jsonl"), "w") as f:
    f.write(tool_use("Edit", {"file_path": os.path.join(LAB, "CLAUDE.md"), "old_string": "a", "new_string": "b"}))
    f.write(tool_use("Bash", {"command": "cat docs/no-such-file-ever.md | head"}))
    f.write(json.dumps({"type": "user", "toolUseResult": {"filePath": os.path.join(LAB, "TASTE.md")}}) + "\n")
with open(os.path.join(tdir, "test-own", "subagents", "agent-1.jsonl"), "w") as f:
    f.write(tool_use("Write", {"file_path": os.path.join(LAB, "ROOT.md"), "content": "x"}))
with open(os.path.join(STATE, "sessions", "test-own.json"), "w") as f:
    json.dump({"start": "2000-01-01T00:00:00", "source": "startup", "transcript_path": os.path.join(tdir, "test-own.jsonl")}, f)
rc, out = run("close", "test-own")
m = re.search(r"^files changed by this session: (\d+) \(read from its transcript; (\d+) files changed in the lab by any session\)$", out, re.M)
check("close: with a transcript, counts only the session's own files, subagent writes included (planted fault)",
      bool(m) and m.group(1) == "3" and int(m.group(2)) > 3, out[:300])
with open(os.path.join(STATE, "sessions", "test-lost2.json"), "w") as f:
    json.dump({"start": "2000-01-01T00:00:00", "source": "startup", "transcript_path": os.path.join(tdir, "missing.jsonl")}, f)
rc, out = run("close", "test-lost2")
check("close: with no transcript, falls back to every changed file and says so",
      "no transcript found" in out and "files changed by this session:" in out, out[:300])

print(f"\n{'all passed' if not failures else str(failures) + ' failed'}  (scratch folder: {tmp})")
if failures:
    sys.exit(1)
print("FACTS TESTS PASSED")
