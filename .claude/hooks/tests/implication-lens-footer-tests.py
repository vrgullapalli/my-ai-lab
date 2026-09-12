#!/usr/bin/env python3
"""Tests for the implication-lens footer hook.

Run:  python3 implication-lens-footer-tests.py <path-to-hook>

Prints IMPLICATION-LENS-FOOTER TESTS PASSED only when every case passes. Run it against a
deliberately broken copy of the hook too; a test nobody has watched fail proves nothing
(the prove-it-can-fail skill).
"""
import json
import subprocess
import sys

HOOK = sys.argv[1]


def run(stdin_text):
    r = subprocess.run([sys.executable, HOOK], input=stdin_text, capture_output=True, text=True)
    return r.returncode, r.stdout.strip()


CASES = [
    # (name, stdin, expect_note)
    ("plain prompt gets the note", json.dumps({"prompt": "what time is it"}), True),
    ("prompt with a decision gets the note", json.dumps({"prompt": "should I push telegraph-plus?"}), True),
    ("the skill itself gets nothing", json.dumps({"prompt": "/implication-lens"}), False),
    ("the skill with leading spaces gets nothing", json.dumps({"prompt": "   /implication-lens now"}), False),
    ("the skill named mid-prompt still gets the note", json.dumps({"prompt": "run /implication-lens after"}), True),
    ("empty prompt gets the note", json.dumps({"prompt": ""}), True),
    ("bad json: exit 0, no output", "{not json", False),
    ("empty stdin: exit 0, note", "", True),
]

failed = 0
for name, stdin_text, expect_note in CASES:
    code, out = run(stdin_text)
    got_note = False
    if out:
        try:
            data = json.loads(out)
            ctx = data["hookSpecificOutput"]["additionalContext"]
            got_note = ("implication-lens footer" in ctx and "Nothing here beyond the task" in ctx
                        and data["hookSpecificOutput"]["hookEventName"] == "UserPromptSubmit")
        except (ValueError, KeyError, TypeError):
            got_note = False
    ok = code == 0 and got_note == expect_note
    print(("ok   " if ok else "FAIL ") + name + ("" if ok else f"  (exit {code}, output {out[:80]!r})"))
    failed += 0 if ok else 1

if failed:
    print(f"{failed} of {len(CASES)} failed")
    sys.exit(1)
print("IMPLICATION-LENS-FOOTER TESTS PASSED")
