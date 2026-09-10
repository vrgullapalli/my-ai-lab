---
name: context-check
description: Reads the whole lab and reports what is duplicated, what is declared dead but still live, what nothing points at, what is uncommitted, and what points at folders that no longer exist. Writes nothing. Use before and after any restructuring, when Venkat says context check, check the lab, what is out of place, what is not linked, is anything missing, did that actually get done, or asks whether a plan was really carried out.
---

# Context check

> **Base directory:** the lab, `/Users/venkatgullapalli/Documents/my-ai-lab/`

## Why this exists

Between 2026-09-04 and 2026-09-07, five plans were written to reorganize the lab.
None were carried out. Each one *said* what should happen; none could say what
did happen.

A plan can claim it is done. This cannot. It only reads what is on disk.

## What to run

```bash
.claude/skills/context-check/context-check.sh
```

It is read-only. It writes nothing, moves nothing, deletes nothing. Safe to run
at any time, including in the middle of other work.

## What it reports

| Section | Question it answers |
|---|---|
| A | Can this be undone? Uncommitted work per repo, age of the last snapshot, folders with no repo at all |
| B | Is the same file sitting in two live places, ready to drift apart? |
| C | Is anything declared superseded but still in the search path? |
| D | Can a machine follow the connections, per area? |
| E | What does nothing point at? |
| F | What points at folders that no longer exist? |

## How to report it back to Venkat

**Do not paste the whole output.** It runs to a few hundred lines. Read it, then
give him the headline number and the two or three findings that would change what
he does next. He reads at a glance — lead with the number, then what it means.

The orphan count in section E is usually the one that matters. It is the direct
measure of "I cannot find anything."

## What it will not tell you

- Whether a file is any *good*. It counts and compares; it does not judge.
- Whether a connection is *meaningful*. A link that exists is a link that exists.
- What to do about any of it. That is a conversation, not a script.

Section C matches on the words superseded, deprecated, retired and do not use near
the top of a file, so it catches files that merely mention those words. Read its
hits, do not act on them blind.
