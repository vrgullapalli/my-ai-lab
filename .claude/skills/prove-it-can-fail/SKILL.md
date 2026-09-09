---
name: prove-it-can-fail
description: Proves a check, test or assertion actually catches the failure it claims to guard, by deliberately breaking that thing and requiring the check to fail. Use when adding a check, after changing anything a check reads, before telling anyone a suite is trustworthy, or whenever a suite is green after risky work. Covers the traps that make a working check look blind - mutations aimed at the wrong module, mutations outside a check's deliberate scope, values the check allowlists on purpose, Python default arguments bound at definition time, and per-source configuration held in more than one place.
license: MIT
metadata:
  origin: "Venkat, 2026-09-02, Telegraph Gate 4"
  tags: "testing, mutation testing, evidence, assurance"
---

# Prove it can fail

> **Base directory:** all relative paths in this skill resolve from `work-os/upskill-advisor/`
> (lab root: `/Users/venkatgullapalli/Documents/my-ai-lab/`). Consolidated to the lab-root
> `.claude/skills/` on 2026-09-07 so it runs from anywhere; its data stayed put.

A check nobody has broken guards nothing. Passing is not evidence; failing on
demand is.

## Why this exists

`records/review-pack-2026-09-02.md` told Venkat:

> The suite stands at 31 checks and every one has been shown to fail when the
> thing it guards is broken.

Claude wrote that sentence and nothing in the repository supported it. The audit
that followed found the real number was **14 of 24**, one check silently broken
that same afternoon by an unrelated edit, and one check blind to the exact attack
its own docstring described.

Every failure in this project has come from a rule that could not fail. This is
the procedure that stops that.

## The proof

Two halves. Both are required.

1. **Clean run.** The check passes on unmodified data. Skipping this makes a
   check that always fails indistinguishable from a check that caught something.
2. **Mutated run.** Break exactly the thing the check claims to guard. The check
   must fail, and its message must name what broke.

Then undo the mutation and confirm the check passes again.

Break the *specific* invariant, not something adjacent. A mutation that corrupts
the database generally proves the check notices damage, which is not the same as
proving it guards its stated invariant.

## When a mutation misses, suspect the mutation first

**Five of the six apparent blind spots in the first audit were bad mutations, not
blind checks.** Assume the check is right until the mutation is proven correct.
The traps, all met in one afternoon:

| What happened | Looked like | Actually was |
|---|---|---|
| Patched `watch.AREA_TERMS`; the check reads `refuse.DETECT` | blind check | mutation aimed at a module the check never reads |
| Duplicated an old row; the check is scoped to records after a fix | blind check | mutation landed outside the check's deliberate scope |
| Planted `someone@example.com` | blind check | `example.com` is allowlisted on purpose, so docs don't trip it |
| Reassigned `collect.PER_REQUEST_NOISE = []` | blind check | `def f(x, noise=PER_REQUEST_NOISE)` binds the list at definition time — the default still pointed at the original object. **Empty it in place.** |
| Cleared one mask list | blind check | masking is per source; the second list was untouched |
| Relabelled inferred rows as stated | blind check | **a real gap.** The check only inspected rows already labelled inferred, so relabelling emptied its loop |

Read the check's body before writing its mutation. Its docstring usually names
the invariant precisely, and its scoping comments explain what it deliberately
does not cover.

## Never mutate the real thing

Mutations run against throwaway copies. In this project that means:

- **Database checks** — copy `data/telegraph.sqlite` to a temp file per check.
- **File checks** — copy only the paths the check globs into a temp directory,
  then point `assertions.ROOT` at it.
- **Code checks** — patch the module attribute in memory and restore it.

The no-delete rule applies to test steps too. Editing a real fixture to prove a
point is a deliberate act, not a test.

## Running it

```
python3 telegraph/evals/prove_checks.py
```

Output is a table plus `telegraph/evals/results/proven-checks.json`. Verdicts:

- **PROVEN** — passed clean, failed mutated.
- **DOES NOT CATCH IT** — passed both. Fix the mutation first; if the mutation is
  right, the check is decoration and must be strengthened or removed.
- **ALREADY FAILING** — failed clean. Something else broke; go fix that.
- **UNPROVEN** — no mutation registered. Name it in the `UNPROVEN` dictionary with
  the reason, so the gap is a line in the report rather than a silent absence.

The program exits non-zero only on `DOES NOT CATCH IT` and `ALREADY FAILING`.
`UNPROVEN` is a gap to report, not a regression to block on.

## Adding a mutation

One entry in `MUTATIONS`, keyed by the check's function name:

```python
"check_source_presence": sql(
    "UPDATE evidence SET url = '' "
    "WHERE evidence_id = (SELECT evidence_id FROM evidence LIMIT 1)"),
```

Helpers available: `sql(...)` for database mutations, `patch(module, attr, value)`
for in-memory ones, `temp_root(globs, mutate)` for file-based ones, and
purpose-built callables where the mutation needs care.

Write a comment saying what the mutation breaks and why that is the right target.
Where a mutation was wrong once, say so in the comment — the wrong version is
what the next person will reach for.

## When to run this

- Adding or changing any check — before claiming it works.
- **After changing anything a check reads.** A reader was rewritten during Gate 4
  work and a check started failing; nobody re-ran the suite for two hours.
- Before putting a count in front of Venkat. A number he cannot verify is worse
  than no number.

## What to say afterwards

State the proven count, not the passing count. They are different numbers and
only one of them is evidence.

> 33 checks pass. 24 of 24 have been shown to fail when the thing they guard is
> broken.

Never write "every check has been shown to fail" unless `proven-checks.json` says
so on the day of writing.
