# Seed judgment cases

Five frozen cases for the judgment half of `seed-capture`: the sweep and the four-test triage
that no script can do. Built 2026-09-15 (Operational DNA v2 repair). The answers are in
`answers.json`, beside this file. **Do not read the answers before judging.** A run is only
evidence when the judge saw this file alone.

## How to run

1. Read the triage rules below. They are the skill's own, copied so a judge needs nothing else.
2. For each case, decide one verdict and name the tests it passes.
3. Write the verdicts as JSON (shape at the bottom) to a file outside the lab.
4. Score: `python3 .claude/skills/seed-capture/tests/judgment/score.py <that file>`.

A fresh session or a subagent that has not seen the answers is the judge. The same session
that wrote the answers is not.

## The triage rules (from the skill)

Candidates are of four kinds: something **he said** worth keeping; a phrasing **he adopted**
from the system or an outside AI; something **a third person said** about him or his work,
relayed in session; a **pattern observed** in his record, with evidence.

A candidate is a seed when it passes **three of four** tests:

1. It repeated (three or more occurrences, or it is a one-off with a name).
2. It is his (not a borrowed method repainted).
3. The label or claim carries the rule (say it and you have said the policy).
4. Someone would ask for it by name.

Guards: wording the system introduced is captured only when he endorses it, and is then marked
`endorsed`. A candidate whose wording already sits in the seedbank is a **repeat**: not written,
connected instead. A candidate that fails narrowly is shown to him as a near miss so he can
overrule; the verdict for that is **ask**.

Verdict words, exactly one per case: `seed` · `not-seed` · `repeat` · `ask`.

## The seedbank the judge may check against

Three existing seeds, titles only:

- A-LIVE-313 — The count was honest and wrong
- A-LIVE-024 — Label after the thing repeats, never in flight
- A-LIVE-101 — Declaring a new canonical source is only half the migration

## Case 1

Session excerpt, 2026-09-08. Venkat, on a hook that a model had been asked to grade:

> "No. Scripts decide what is true. Models decide what to look at. That's the whole split."

Later the same session, on a routine that reported its own success:

> "Same thing again. Scripts decide what is true. A model saying it ran is not it running."

And at close, when Alfred proposed a checklist:

> "You keep doing this. Scripts decide what is true, models decide what to look at. Put that on the front door."

## Case 2

Session excerpt, 2026-09-14. Venkat, once, correcting Alfred's word "backup" for a folder that
had been copied to Dropbox:

> "That's not a backup, that's a copy. A backup is something you've restored from. Until you've restored from it, call it a copy. Call it the restored-from test if you want a name."

Nothing else in the session returned to it.

## Case 3

Session excerpt, 2026-09-12. Alfred, summarizing a signal review that rated 89 signals and moved
nothing:

> Alfred: "Monitoring that never feeds a decision is journaling. Want that kept?"
> Venkat: "ok, move on."

The line does not appear anywhere else in the session. Venkat did not use it, repeat it, or
say to keep it.

## Case 4

Session excerpt, 2026-09-15. Venkat, on a coverage number that a script had reported:

> "That's the count being honest and wrong again. It counted the generated copy as the source. Ask what it counted as a record before you rerun it."

## Case 5

Session excerpt, 2026-09-13. Venkat, relaying a message he received:

> "A colleague messaged me after the call. She said I'm the only one who asks what the data counted as a record before trusting the number. Thought that was funny."

Venkat did not say more about it. The phrase does not repeat in the session.

## Verdict file shape

```json
{
  "case-1": {"verdict": "seed", "tests_passed": [1, 2, 3, 4], "reason": "one line"},
  "case-2": {"verdict": "...", "tests_passed": [], "reason": "..."},
  "case-3": {"verdict": "...", "tests_passed": [], "reason": "..."},
  "case-4": {"verdict": "...", "tests_passed": [], "reason": "..."},
  "case-5": {"verdict": "...", "tests_passed": [], "reason": "..."}
}
```
