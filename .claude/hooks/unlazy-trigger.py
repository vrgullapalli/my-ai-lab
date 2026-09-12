#!/usr/bin/env python3
"""unlazy-trigger: reminds the session to use the unlazy skill when Venkat asks for
complete work in his own words. Since 2026-09-12 it also carries the design check: when a
prompt asks for a new system (a registry, store, bank, agent, skill, sensor, and the like), it
hands the session the five questions from the front door's "Before you write."

A UserPromptSubmit hook. It reads the prompt. When the prompt matches, it adds a short
note to the session's context; otherwise it prints nothing. It never blocks a prompt.
The script notices the words; the answers are the model's judgment, given in the reply.

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

SYSTEM_WORDS = r"(?:capabilit(?:y|ies)|registry|registries|register|bank|store|database|index|agent|skill|sensor|hook|platform|engine|framework|service|tracker|ledger)"
DESIGN_PHRASES = [
    r"\bnew (?:shared |generic |central |lab-wide )?" + SYSTEM_WORDS + r"\b",
    r"\b(?:create|build|make|add|set up|stand up|spin up|write)\s+(?:a|an|another|one more)\s+(?:\w+[\s-]){0,2}" + SYSTEM_WORDS + r"\b",
    r"\b(?:a|an) " + SYSTEM_WORDS + r" (?:for|of|that)\b",
]
DESIGN_NOTE = (
    "design check (lab hook, 2026-09-12): this prompt asks for a new system. Before building, read "
    "docs/architecture/CAPABILITY-MAP.md and answer these five in the reply, one line each: "
    "1. what job is needed; 2. which existing capability or system already covers it, or why none does; "
    "3. the AI-native test: what should this become now that AI exists, and would the outcome stay the same "
    "without AI; 4. which standard applies: shared system, registry, or sensor; 5. whether a new system is "
    "necessary. If it is, add or change its registry entry and run python3 docs/architecture/check.py. "
    "The answers are judgment; the script only proves the record agrees with the lab."
)


def main():
    try:
        payload = json.loads(sys.stdin.read() or "{}")
    except ValueError:
        return
    prompt = str(payload.get("prompt") or "")
    if prompt.lstrip().startswith("/unlazy"):
        return  # the skill is loading anyway
    notes = []
    if any(re.search(p, prompt, re.I) for p in PHRASES):
        notes.append(NOTE)
    if any(re.search(p, prompt, re.I) for p in DESIGN_PHRASES):
        notes.append(DESIGN_NOTE)
    if notes:
        print(json.dumps({"hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit", "additionalContext": "\n\n".join(notes)}}))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass  # a reminder is never worth breaking a prompt
    sys.exit(0)
