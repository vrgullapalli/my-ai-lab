---
title: Implication-lens trial
date: 2026-09-12
kind: audit of one skill, two rounds, read-only runs; kept at Venkat's word 01:56 ("yes, keep the trial results in evidence/audits/")
session: 2b9293d7-a7b6-491a-b067-40af551621e2
receipts: [R-2026-09-12-0149-6df3, R-2026-09-12-0154-cc95]
skill: .claude/skills/implication-lens/SKILL.md
hook: .claude/hooks/implication-lens-footer.py (registered 01:52, option 2)
seeds: [A-LIVE-307, A-LIVE-308, A-LIVE-309, A-LIVE-310]
---

# Implication-lens trial, 2026-09-12

**Question.** Does a hand-invoked reflection skill (deeper idea, commercial capability, lab test, content angle; a fifth field, reusable intervention, added at 00:48) add value over just asking Alfred the same questions?

**Method.** Five lab cases (retrieval, memory, agent authority, architecture, a routine fix) plus trivial cases as a restraint check. Each case ran as a fresh helper with the skill and, once, as a fresh helper given the plain request. A separate helper graded each pair blind, with labels shuffled, and checked claims against the source files. Alfred re-checked every number either side cited.

**Result.**

| | Skill won | Plain won | "Nothing here" on trivial work |
|---|---|---|---|
| Round one (four fields, 00:41) | 1 of 5 | 4 of 5 | 1 of 3 |
| Round two (five fields, three fixes, 01:14) | 1 of 5 | 4 of 5, "close in all five" | 2 of 2 |

**What the fixes changed.** Round two's skill runs opened with a measurement and found new facts in 4 of 5 cases: 8 live files still naming "AI Advisory Search," a fourth machinery file naming a driver, `CLAUDE.md` saying "26 skills" against 28 on disk, the "12 runs" that is 23. They lost on length: "no" on the grader's 30-second test in 3 of 5.

**Decision.** Venkat chose option 2 at 01:52: wire the hook now and judge a week of live replies, with the footer reading the whole session. Verdict due on or after 2026-09-19 (F-20260912-0154-2).

**Files here.**
- `pairs-round1.md`, `pairs-round2.md`: the ten pairs as the grader saw them (labels shuffled; the key is at the top of each grade file).
- `grade-round1.md`, `grade-round2.md`: the grader's text, unedited, with the key and Alfred's one correction.

New files only. Nothing here is edited after 2026-09-12.
