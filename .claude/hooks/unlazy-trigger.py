#!/usr/bin/env python3
"""unlazy-trigger: reminds the session to use the unlazy skill when Venkat asks for
complete work in his own words.

A UserPromptSubmit hook. It reads the prompt. When the prompt matches, it adds a short
note to the session's context; otherwise it prints nothing. It never blocks a prompt.

Why: the skill's description triggers on /unlazy and "tree N". On 2026-09-10 Venkat
wrote "dont do anything half assed. be complete and thorough", which it did not cover.
This catches how he actually says it. The match list is deliberately short: a trigger
that fires on everything teaches everyone to ignore it.
"""
import json
import re
import sys

PHRASES = [
    r"half[\s-]*ass",
    r"\bcomplete and thorough\b",
    r"\bthorough and complete\b",
    r"\bdo(?:n'?t| not) stop until\b",
    r"\bno half[\s-]*measures\b",
    r"\bleave nothing (?:half|undone|out)\b",
    r"\bnothing half[\s-]*done\b",
]
NOTE = (
    "unlazy trigger (lab hook): Venkat asked for complete work. Use the `unlazy` skill. "
    "Before starting, write GATES.md at the lab root from "
    ".claude/skills/unlazy/templates/gates-leaf.md, with one gate for each thing he asked "
    "for. Run the gates before reporting anything as done, and report measured met, unmet, "
    "and handed-off counts. Anything that needs his word (commit, push, publish, send, "
    "delete) is a manual gate titled 'needs Venkat', never counted as met."
)


def main():
    try:
        payload = json.loads(sys.stdin.read() or "{}")
    except ValueError:
        return
    prompt = str(payload.get("prompt") or "")
    if prompt.lstrip().startswith("/unlazy"):
        return  # the skill is loading anyway
    if any(re.search(p, prompt, re.I) for p in PHRASES):
        print(json.dumps({"hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit", "additionalContext": NOTE}}))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass  # a reminder is never worth breaking a prompt
    sys.exit(0)
