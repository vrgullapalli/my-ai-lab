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


# fake keys, right shape, wrong contents
ANTHROPIC = "sk-ant-api03-AbCdEf-GhIjKl_MnOpQr-StUvWx_YzAbCd-EfGhIjKlMnOpQrStUvWxYzAbCdEfGh"
GOOGLE = "AIzaSyA1b2C3d4E5f6G7h8I9j0K1l2M3n4O5p6Q"
OLD_KINDS = {
    "plain sk- key": "sk-AbCdEfGhIjKlMnOpQrStUvWxYz0123",
    "GitHub token": "ghp_AbCdEfGhIjKlMnOpQrStUvWxYz0123456789",
    "Slack token": "xoxb-1234567890-abcdefghijklmnop",
    "Bearer token": "Authorization: Bearer AbCdEfGhIjKlMnOpQrStUvWxYz.0123456789",
    "AWS key id": "AKIAABCDEFGHIJKLMNOP",
    "private key header": "-----BEGIN RSA PRIVATE KEY-----",
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

print(f"\n{'all passed' if not failures else str(failures) + ' failed'}")
if failures:
    sys.exit(1)
print("SESSION SYNC TESTS PASSED")
