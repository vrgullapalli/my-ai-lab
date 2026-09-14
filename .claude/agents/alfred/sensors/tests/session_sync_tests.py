#!/usr/bin/env python3
"""Tests for Alfred's session-sync sensor: the secret mask.

Run:  python3 .claude/agents/alfred/sensors/tests/session_sync_tests.py

Loads the sensor as a module and checks its SECRET pattern against fake keys and against
ordinary lab prose. Reads and writes nothing else. Prints SESSION SYNC TESTS PASSED only when
every case passes, so a script can check for that line.

Why (follow-up F-20260910-1630-3): the pattern in force on 2026-09-10 missed Anthropic keys
with dashes and Google keys. The last group below is the positive control: it runs that old
pattern, pasted as a string, and requires it to miss both, so these tests would have failed
before the fix. Every key here is fake.
"""
import importlib.util
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TOOL = os.path.join(os.path.dirname(HERE), "session-sync.py")
spec = importlib.util.spec_from_file_location("session_sync", TOOL)
ss = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ss)
failures = 0


def check(name, ok, detail=""):
    global failures
    failures += 0 if ok else 1
    print(f"  {'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail and not ok else ""))


def masked(text):
    return ss.MASK in ss.SECRET.sub(ss.MASK, text)


# fake keys, right shape, wrong contents. Each is joined from pieces at run time so the file's own
# bytes never hold a scanner-shaped string (GitHub push protection stopped a push on 2026-09-14 over
# the Slack-shaped fake; Venkat allowed it once and chose to fix forward. The values the test checks
# are unchanged, so the sensor's pattern is tested exactly as before).
def _j(*parts):
    return "".join(parts)


ANTHROPIC = _j("sk-ant-", "api03-AbCdEf-GhIjKl_MnOpQr-StUvWx_YzAbCd-EfGhIjKlMnOpQrStUvWxYzAbCdEfGh")
GOOGLE = _j("AIza", "SyA1b2C3d4E5f6G7h8I9j0K1l2M3n4O5p6Q")
OLD_KINDS = {
    "plain sk- key": _j("sk-", "AbCdEfGhIjKlMnOpQrStUvWxYz0123"),
    "GitHub token": _j("ghp_", "AbCdEfGhIjKlMnOpQrStUvWxYz0123456789"),
    "Slack token": _j("xox", "b-1234567890-abcdefghijklmnop"),
    "Bearer token": _j("Authorization: Bear", "er AbCdEfGhIjKlMnOpQrStUvWxYz.0123456789"),
    "AWS key id": _j("AKIA", "ABCDEFGHIJKLMNOP"),
    "private key header": _j("-----BEGIN ", "RSA PRIVATE KEY-----"),
}
PROSE = """The lab root became a repository on 2026-09-09, and the receipt for 2026-09-13-0602 names
follow-up F-20260913-0602-2. The file lives at ~/Documents/my-ai-lab/work-os/scheduled-tasks/
market-signals/verify.sh and the plist is com.venkat.session-sync. Long-running, well-tested,
copy-paste-ready, second-order, thirty-two-character, task-notification-handler-for-sessions,
desk-side-notes-from-the-morning-brief. Commit 345088b touched session-sync.py at 16:37.
The launchd job runs at 9, 13 and 18; ids look like 65a2256a-498c-4a63-868f-7b5df17129f3."""

print("session-sync: the secret mask")
check("an Anthropic key with dashes and underscores is masked", masked(ANTHROPIC))
check("an Anthropic key is masked whole, nothing of it leaks",
      ss.SECRET.sub(ss.MASK, "key: " + ANTHROPIC + " end") == "key: " + ss.MASK + " end")
check("a Google key is masked", masked(GOOGLE))
check("a Google key is masked inside a line of json",
      ss.SECRET.sub(ss.MASK, '{"key": "' + GOOGLE + '"}') == '{"key": "' + ss.MASK + '"}')
for name, sample in OLD_KINDS.items():
    check(f"still masks: {name}", masked(sample), sample)
check("ordinary lab prose with dates, paths and hyphenated words has zero hits",
      len(ss.SECRET.findall(PROSE)) == 0, str(ss.SECRET.findall(PROSE)))
check("a word ending in sk- (desk-, task-) followed by a long slug is not a hit",
      not masked("desk-notes-from-the-morning-brief-on-tuesday task-notification-handler-x"))

# positive control: the pattern in force on 2026-09-10, when the follow-up was written
OLD = re.compile(r"(sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|xox[baprs]-[A-Za-z0-9-]{10,}|"
                 r"Bearer\s+[A-Za-z0-9._-]{20,}|AKIA[0-9A-Z]{16}|-----BEGIN [A-Z ]*PRIVATE KEY)")
check("positive control: the old pattern misses the Anthropic key with dashes",
      OLD.search(ANTHROPIC) is None)
check("positive control: the old pattern misses the Google key", OLD.search(GOOGLE) is None)
check("positive control: the old pattern still caught the old kinds",
      all(OLD.search(s) for s in OLD_KINDS.values()))


# ---------------------------------------------------------- messages sent mid-task
# Why (2026-09-11, restored 2026-09-14): a message Venkat sends while Claude is working is
# stored as an "attachment" record of type queued_command, not a "user" record. The reader
# skipped it, and 249 of his messages across 18 sessions were missing from the transcripts.
def queued(uid, prompt, source_uuid, mode="prompt", origin=None):
    return {"type": "attachment", "uuid": uid, "timestamp": "2026-09-12T04:00:00Z",
            "attachment": {"type": "queued_command", "prompt": prompt, "source_uuid": source_uuid,
                           "commandMode": mode, "origin": origin, "timestamp": "2026-09-12T04:00:00Z"}}


records = [
    {"type": "user", "uuid": "u-normal", "timestamp": "2026-09-12T03:59:00Z",
     "message": {"role": "user", "content": "first normal message"}},
    {"type": "assistant", "uuid": "a-reply", "timestamp": "2026-09-12T03:59:30Z",
     "message": {"role": "assistant", "content": [{"type": "text", "text": "a normal reply"}]}},
    queued("q-list", [{"type": "text", "text": "add the proving ground line"}], "src-1",
           origin={"kind": "human"}),                                    # his, list form
    queued("q-str", "is the markdown too long", "src-2", origin={"kind": "human"}),   # his, string form
    queued("q-dup", [{"type": "text", "text": "add the proving ground line"}], "src-1",
           origin={"kind": "human"}),                                    # the same message twice
    queued("q-note", "<task-notification>\n<task-id>abc</task-id>NOTICE-BODY-TEXT</task-notification>",
           "src-3", mode="task-notification"),                           # a background job finished
    queued("q-peer", "<cross-session-message from=\"x\">roll call: what are you working on</cross-session-message>",
           "src-4", origin={"kind": "peer", "name": "my-ai-lab-96"}),     # another session
    queued("q-ide", [{"type": "text", "text": "<ide_opened_file>The user opened a file</ide_opened_file>"}],
           "src-5", origin={"kind": "human"}),                           # editor notice only
]

tmp = tempfile.mkdtemp(prefix="session-sync-tests-", dir=os.environ.get("TMPDIR"))
src = os.path.join(tmp, "00000000-test-session.jsonl")
with open(src, "w", encoding="utf-8") as f:
    for r in records:
        f.write(json.dumps(r) + "\n")

out = ss.render_claude(src)
usage = json.loads(re.search(r"^- Usage: (\{.*\})$", out, re.M).group(1))

print("\nsession-sync: messages sent mid-task")
check("his list-form message is shown once, labeled mid-task, under its own anchor",
      out.count("add the proving ground line") == 1 and '<a id="q-list"></a>\n**Venkat, mid-task**' in out)
check("his string-form message is shown, labeled mid-task, under its own anchor",
      "is the markdown too long" in out and '<a id="q-str"></a>\n**Venkat, mid-task**' in out)
check("the repeat (same source id) is not shown a second time", '<a id="q-dup">' not in out)
check("a finished background job is a marker, with none of its text",
      "*[background task finished]*" in out and "NOTICE-BODY-TEXT" not in out)
check("a message from another session is labeled with that session's name",
      "**Message from another session (my-ai-lab-96)**" in out and "roll call" in out)
check("an editor-only notice is dropped", '<a id="q-ide">' not in out and "opened a file" not in out)
check("normal message and reply still render",
      '<a id="u-normal">' in out and '<a id="a-reply">' in out)
pos = [out.find(f'<a id="{a}">') for a in ("u-normal", "q-list", "q-str")]
check("order is kept: normal message before the mid-task messages",
      min(pos) >= 0 and pos[0] < pos[1] < pos[2], f"positions={pos}")
check("counts: 3 Venkat turns, 2 of them mid-task",
      usage.get("venkat_turns") == 3 and usage.get("venkat_midtask") == 2,
      f"venkat_turns={usage.get('venkat_turns')} venkat_midtask={usage.get('venkat_midtask')}")
check("header says how many were sent mid-task", "(2 sent mid-task)" in out)

print(f"\n{'all passed' if not failures else str(failures) + ' failed'}")
if failures:
    sys.exit(1)
print("SESSION SYNC TESTS PASSED")
