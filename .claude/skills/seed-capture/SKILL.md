---
name: seed-capture
description: Find the ideas in the current session worth developing, check them for repeats and connections against the seedbank, show at most five candidates, and write only the ones Venkat picks, as seed files under fixed conventions. Runs in Scan mode at every session close from alfred-close (Venkat, 2026-09-10); Capture writes only on his pick, or when a moment was marked "this is a seed" during the session. Also use mid-session when something seed-worthy appears, or when Venkat says "capture this as a seed", "add this to the greenhouse", "is this a seed?", "scan this for seeds", "what seeds are here", "identify seed candidates". Writes only to /Users/venkatgullapalli/Documents/my-ai-lab/work-os/brand-os/engagement-os/seedbank/session/. Zero seeds is a valid outcome.
---

# Seed Capture

> **Base directory:** all relative paths in this skill resolve from `work-os/brand-os/engagement-os/`
> (lab root: `/Users/venkatgullapalli/Documents/my-ai-lab/`). Consolidated to the lab-root
> `.claude/skills/` on 2026-09-07 so it runs from anywhere; its data stayed put.

> **Canonical copy.** Venkat's ruling, 2026-09-05: this is the only copy. Do not create a second
> one; reference this path instead.

## The job

> Find ideas from the current interaction worth developing, check repeats and connections,
> show at most five candidates, and persist only the ones Venkat selects.

A seed is one idea worth keeping: what it is, the tension it carries, where it came from, dated.
Sessions produce them and chat context loses them. This skill writes the survivors to
`seedbank/session/` the same way every time, so capture never depends on anyone remembering how.

**One write destination.** This skill writes seed files to
`/Users/venkatgullapalli/Documents/my-ai-lab/work-os/brand-os/engagement-os/seedbank/session/`
and nothing else. Not the seeds README, not the concepts file, not a profile, not a miss log.
Restored to one job on 2026-09-15 at Venkat's word (AD-38), after the Operational DNA audit of
2026-09-14 found four write targets, two of them undeclared or missing.

**Scope guard:** capture only. No status moves, no composting, no scoring, no promotion.
Cultivation belongs to the weekly review (seed A-LIVE-023, the cultivator agent).

**What changes because AI exists.** The sweep and the four-test triage run over every
session at every close. No one did that by hand; before 2026-08-13 the seeds sat in session
temp and were about to be lost. Remove the AI and capture goes back to "remember to write it
down," which is the failure this skill exists to end. The scripts around it (repeat check,
next id, seed check, write boundary) decide what is true; the AI decides what is worth keeping.

**One job with two gates.** Scan proposes and Capture writes. They have different admission
rules on purpose: Scan admits any candidate that passes three of four tests, Capture admits
only what he picked. That is one job, idea capture, with his word as the second gate. It is not
two jobs, and it is not split.

## Who does the judgment

Deciding which moments pass three of four tests is substantive editorial work, not
coordination. Under Operational DNA v2 that is specialist work. **No specialist for capture
exists today:** the cultivator tends seeds already written and never captures; ARCHIE
researches topics. So **Alfred performs the seed judgment at every close, as the current
explicit exception** (2026-09-15, at Venkat's word in the goal of 02:13). The exception is
visible here and in the close routine's seed step. When a capture specialist exists, this
section changes and the exception ends. Until then, the judgment's proof is the evaluation set
below, run by a judge that is not the session being judged.

## Operational DNA

The standard is section 16 of `docs/architecture/LAB-OPERATING-MODEL.md`. This skill's answers:

| Property | State | In one clause |
|---|---|---|
| Job | OWN | the sentence above; the AI role is the sweep and triage, which no one did by hand |
| Scope | OWN | this session's interaction, the seedbank for the repeat check; no client, employer, or brand name in any seed. **Bounded limitation:** the name guard is a rule the model follows; no deterministic check exists, because the lab holds no client-name list and the never-cite list covers numbers, not names |
| Process | OWN, with the judgment done by Alfred as the explicit exception (see "Who does the judgment") | Scan at every close and on his word; Capture only on his pick; next consumer is the weekly cultivator; mechanism (four tests, template, helpers) is reused every close, the session is the local context, and more than five survivors is the invalidating condition |
| State | OWN, narrowly | one seed file per pick in `seedbank/session/`; the seed count is the facts sheet's (INHERIT, `facts.py`) |
| Context | INHERIT | the conversation itself, plus `find-similar.py` over the seedbank; nothing from the warehouse or the voice canon |
| Evidence | OWN | source anchor and date of the moment on every seed; "unwritten is unreported" |
| Trust | OWN | the seedbank's four attribution classes; `system` needs his word before public use; "not on disk" blocks Capture |
| Authority and control | INHERIT | writing waits for his pick, held by the close routine (his word, 2026-09-10); reads transcripts that may hold client names and writes to a repo with no remote, so the names-stripped rule is the guard |
| Experience | OWN | at most five candidates, numbered, "say the numbers"; near misses named so he can overrule |
| Evaluation and learning | OWN, split | scripts: `tests/seed_check_tests.py` (known seed, repeat, no seed, scan tools write nothing, write boundary). Judgment: `tests/judgment/` (clear seed, subtle seed, tempting non-seed, repeat, honest ambiguous), answered blind by a fresh session and scored by script. A confirmed miss becomes a regression case in both. The threshold itself never learns; it is his ruling (A-LIVE-024) |

## Modes

Pick the mode from what Venkat said. When in doubt, Scan. It writes nothing.

| Mode | Triggers | What runs | Writes |
|---|---|---|---|
| **Scan** | every close routine (`alfred-close`, 2026-09-10) · "scan this for seeds" · "what seeds are here" · "identify seed candidates" · "any seeds in this?" · a sweep that turns up more than five survivors | Steps 1 and 2. Return at most five ranked candidates; for each: the claim as a sentence · attribution class · source anchor (path and line, or "not on disk") · tension · which of the four tests pass · what is missing · the closest existing seed from `find-similar.py`. If more than five passed, say how many. Rank by how many tests pass, then by how clearly the sentence carries the rule. | **Nothing.** Capture happens only on his pick. If the source is not on disk, say so: Scan can propose from a paste; Capture cannot write until the record exists. |
| **Capture** | `/seed-capture` · his pick at the close routine · "capture this as a seed" · his pick from a Scan ("approve 1, 3, 4", "all five") · a moment he marked "this is a seed" during the session | Steps 1 to 5 (or 3 to 5 after a Scan). | Seed files in `seedbank/session/`. |

A candidate he does not pick is not persisted anywhere by this skill. It was shown; that is the
end of it. If he later says "that should have been a seed," it is captured then, from the record,
and the case goes into the tests as a regression (see Evaluation below).

## Steps

1. **Sweep the session** for candidates, four kinds:
   - Something **he said** worth keeping (a claim, a story, a rule, a coined label).
   - A phrasing **he adopted** from the system or an outside AI.
   - Something **a third person said** about him or his work, relayed in session.
   - A **pattern observed** in his record or behavior, with evidence.

2. **Triage against his threshold** (seed A-LIVE-024), pass three of four:
   - It repeated (three or more occurrences, or it is a one-off with a name).
   - It is his (not a borrowed method repainted).
   - The label or claim carries the rule (say it and you have said the policy).
   - Someone would ask for it by name.

   Then run the repeat check on each survivor:
   `python3 .claude/skills/seed-capture/scripts/find-similar.py "<the claim>"`. A score of 0.45
   or more is probably a repeat; say so and show the match. A lower match is a candidate
   connection or conflict.

   **Zero survivors is a valid and expected outcome.** The base rate is zero to three per
   session. Say "no seeds today" and stop. Never manufacture a seed to fill the step. **More
   than five survivors means a backfill or a threshold failure: switch to Scan, show the top
   five ranked, say how many more passed, write nothing until he picks.**

3. **Write one file per picked seed** in `seedbank/session/`, using the template below.
   - **ID:** next number in the existing sequence, zero-padded (run
     `python3 .claude/skills/seed-capture/scripts/next-id.py`; never reuse or renumber). IDs are
     immutable. Folder and prefix names are placeholders pending Venkat's naming (loop #43); a
     rename must never touch an ID.
   - **Attribution class is mandatory**, one of: **his** (verbatim or near) · **endorsed** (a
     phrasing he adopted; say whose) · **other** (a third person's words, relayed) · **system**
     (an observed pattern; the weakest class; flag for his confirmation before any public use).
   - **Names stripped:** no client, employer, or brand name in title or body; point to the
     source record instead (his ruling, 2026-08-13, loop #50). Exception precedent: a brand
     where he is the customer in the story (A-LIVE-001) may stay.
   - **Connections:** one to three, stated by hand, honestly, or none. The top matches from
     `find-similar.py` are the first candidates.
   - **No quality scores.** Facts stored; judgments computed when a decision needs one
     (seedbank README rule).

4. **Check what was written.** Run
   `python3 .claude/skills/seed-capture/scripts/seed-check.py --seed <each file written>` and
   `python3 .claude/skills/seed-capture/scripts/seed-check.py --boundary <each file written>`.
   Both must print OK. A seed that fails is fixed before it is reported. A path outside
   `seedbank/session/` is a write-boundary break: say so and undo it.

5. **Report:** the IDs written with one-line claims, or "no seeds today", plus any candidate
   that failed triage narrowly, named in one line so Venkat can overrule.

## Helpers

- `scripts/find-similar.py "<the claim>"` — the five seeds whose wording is closest, scored 0 to 1.
  Word overlap, no model, same answer every time. Finds repeats; misses paraphrases. Read-only.
- `scripts/next-id.py --check` — the next free `A-LIVE` number, and any number on two seeds. Read-only.
- `scripts/seed-check.py --seed <file>` — the seed has a title, a matching unique ID, a source, a
  dated moment, a status, one of the four attribution classes, the two sections, and no placeholder
  left. `--boundary <path...>` — every path is under `seedbank/session/`. Read-only.

## Seed file template

```
# <The claim, as a full sentence — the title IS the claim>

- ID: <PREFIX>-<NNN>
- Source: <where it happened, with a path or pointer to the record>
- Date: <YYYY-MM-DD of the moment, not of the writing>
- Status: seedling
- Attribution: <his | endorsed | other | system> — <one line of who/how>
- Tension: <the friction that makes it worth keeping, one or two sentences>
- Conflicts with: [[<id>]] — <what conflicts, one line>   ← optional; only when a seed disagrees with an existing one

## The claim
<Two to five sentences. His words quoted where they exist.>

## Why it matters
<Two to four sentences. What this changes or decides.>

## Connections
- [[<id>]] — <why, in a few words>
```

## Rules

- Verify every file written exists at its path before reporting it (evidence rule). Unwritten
  is unreported.
- A seed's Date is when the moment happened; the file records it even when written later.
- Quotes marked **his** must be checkable against a record. If the record is a voice
  transcription, note that his words may be garbled; near-verbatim is labeled near-verbatim.
- No secrets, no restricted client content, no financial figures.
- **Conflicts are recorded, not resolved.** When a candidate disagrees with an existing seed,
  capture still writes it, with a `Conflicts with:` line naming the other seed and what
  conflicts. The old seed is not touched; which one wins is cultivation, for the weekly review.
- **Wording the system introduced** is captured only when Venkat endorses it, recorded
  `endorsed` with whose words they were (his word, 2026-08-19). Nothing generated is persisted
  unless he later adopts it.
- This skill proposes nothing for building. A seed that looks like a build idea still goes by
  the normal route.

## Evaluation

`python3 .claude/skills/seed-capture/tests/seed_check_tests.py` builds a throwaway bank and
proves, in the prove-it-can-fail form: a known good seed passes; a seed with a missing class or
a reused ID fails and names the field; a near-repeat scores as a repeat and a fresh claim does
not; a claim with no matching words returns none; the Scan tools change no byte of the bank; a
path outside `session/` breaks the boundary check and a path inside it passes. It prints
`SEED CHECK TESTS PASSED` only when every case passes.

**The judgment half has its own proof.** `tests/judgment/cases.md` holds five frozen cases:
a clear seed, a subtle seed, a tempting non-seed, a repeat, and an honest ambiguous one. A
judge that has not seen `answers.json` (a fresh session or a subagent, never the session that
wrote the answers) reads the cases with the skill's own triage rules, writes verdicts to a file
outside the lab, and `score.py` compares. It passes at four of five, and only if the tempting
non-seed was not called a seed, because telling a strong candidate from a plausible non-seed is
the claim. `score.py --check-set` proves the set itself: five kinds, no answers in the cases.

**A confirmed miss is a regression case.** When Venkat says something should have been a seed
and it is then captured, add its claim and the seed it became to `REGRESSION_MISSES` in the
tests file, and add the moment as a new case in `cases.md` with its verdict in `answers.json`.
Nothing in either file is edited to make a run pass. No miss log is kept by this skill.

## What left this skill on 2026-09-15

Each of these has an existing owner; none of it is lost.

- **Settled language** (terms, rule sentences, distinctions, corrections) is written by the
  close routine to `work-os/brand-os/engagement-os/memory/concepts.md`, the concepts mechanism
  that began as session-receipt step 10. This skill no longer writes there.
- **Banned or corrected words** go to the voice canon process, not to a profile file.
- **The seed count** is measured by `facts.py` on the facts sheet. This skill no longer edits
  the seedbank README.
- **Wording lenses** were removed on 2026-09-12 at his word ("remove the lenses. they are
  poorly applied."); the stub that said so moved to
  `~/Documents/_warehouse/wording-lenses-removed-2026-09-12/`.
- **A miss** is a regression case in the tests, above, not a row in a log. The old miss log,
  `seedbank/missed.md`, stays on disk as history with its zero rows; this skill no longer
  writes it, and the facts sheet still reads it.
