#!/usr/bin/env python3
"""implication-lens-footer: asks every reply to end with the implication-lens footer.

A UserPromptSubmit hook. It adds one short note to the session's context on every prompt,
except when the prompt itself is /implication-lens (then the skill is the whole reply and
needs no footer). It never blocks a prompt.

Why, 2026-09-12: Venkat asked for the lens on every response. A skill with
disable-model-invocation cannot start on its own, and a rule in a file can be drifted past,
so the reminder is a hook, the same way unlazy-trigger.py works. The skill keeps its
"Nothing here beyond the task" exit, so plain confirmations stay clean.
"""
import json
import sys

NOTE = (
    "implication-lens footer (lab hook): end this reply with the implication-lens footer "
    "from .claude/skills/implication-lens/SKILL.md, in footer mode: a `---` rule with a blank "
    "line above and below, no `Alfred —` line, one line per field, fields in the skill's order. "
    "Run the skill's first check before writing it. If nothing earns a line, end with "
    "\"Nothing here beyond the task.\" This footer replaces the inline deeper idea; do not add "
    "a second one in the body."
)


def main():
    try:
        payload = json.loads(sys.stdin.read() or "{}")
    except ValueError:
        return
    prompt = str(payload.get("prompt") or "")
    if prompt.lstrip().startswith("/implication-lens"):
        return  # the skill is the whole reply
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "UserPromptSubmit", "additionalContext": NOTE}}))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass  # a reminder is never worth breaking a prompt
    sys.exit(0)
