---
name: seed-capture
description: Capture a session's seed-worthy moments as seed files under fixed conventions. Runs in Scan mode at every session close, from alfred-close (Venkat, 2026-09-10); writes seeds only on his pick or when a candidate was marked during the session (D-137). Also use mid-session the moment something seed-worthy appears, or when Venkat says "capture this as a seed", "add this to the greenhouse", or "is this a seed?". Three modes — Scan (propose, write nothing), Capture (write), Missed (log a miss) — also triggered by "scan this for seeds", "what seeds are here", "identify seed candidates", "you missed X". Writes only to /Users/venkatgullapalli/Documents/my-ai-lab/work-os/brand-os/engagement-os/seedbank/session/, the seeds README count, and /Users/venkatgullapalli/Documents/my-ai-lab/work-os/brand-os/engagement-os/seedbank/missed.md. Zero seeds is a valid outcome.
---

# Seed Capture

> **Base directory:** all relative paths in this skill resolve from `work-os/brand-os/engagement-os/`
> (lab root: `/Users/venkatgullapalli/Documents/my-ai-lab/`). Consolidated to the lab-root
> `.claude/skills/` on 2026-09-07 so it runs from anywhere; its data stayed put.

> **Canonical copy.** Venkat's ruling, 2026-09-05: this is the main one. The former
> duplicate under `chief-of-staff/.claude/skills/` is gone. `chief-of-staff/` was
> retired 2026-09-08 and its archive, checked 2026-09-09, holds no copy of this skill.
> Nothing to go back to; this file is the only one.
> Do not create a second copy; reference this path instead.

## Purpose

A seed is one idea worth keeping: what it is, the tension it carries, where it
came from, dated. Sessions produce them and chat context loses them. This skill
writes the survivors to `/Users/venkatgullapalli/Documents/my-ai-lab/work-os/brand-os/engagement-os/seedbank/session/` the same way every time, so capture
never depends on anyone remembering how.

**Scope guard:** capture only. No status moves, no composting, no scoring, no
promotion — cultivation belongs to the weekly review, per Venkat's cadence rule
(seed A-LIVE-023). This skill writes to `/Users/venkatgullapalli/Documents/my-ai-lab/work-os/brand-os/engagement-os/seedbank/session/`, the count line in
`/Users/venkatgullapalli/Documents/my-ai-lab/work-os/brand-os/engagement-os/seedbank/README.md`, and one row at a time to `/Users/venkatgullapalli/Documents/my-ai-lab/work-os/brand-os/engagement-os/seedbank/missed.md` —
and nothing else.

## Modes (v2, plan `seed-capture-skill--feature--skill-build--v2--2026-08-20-1617`)

Pick the mode from what Venkat said. When in doubt, Scan — it writes nothing.

| Mode | Triggers | What runs | Writes |
|---|---|---|---|
| **Scan** | every close routine (`alfred-close`, 2026-09-10) · "scan this for seeds" · "what seeds are here" · "identify seed candidates" · "any seeds in this?" · a sweep that turns up more than five survivors | Steps 1–2, plus step 5 as a scan (wording that got fixed, and wording that could be created through the two lenses in `references/wording-lenses.md`; at most three per lens). Return at most five ranked seed candidates; for each: the claim as a sentence · attribution class · source anchor (path + line, or "not on disk") · tension · which of the four tests pass · what is missing. If more than five passed, say how many. Rank by how many tests pass, then by how clearly the sentence carries the rule. | **Nothing.** Capture happens only on his pick. If the source is not on disk, say so: Scan can propose from a paste; Capture cannot write until the record exists. |
| **Capture** | `/seed-capture` · his pick at the close routine · "capture this as a seed" · his pick from a Scan ("approve 1, 3, 4", "all eight") | Steps 1–6 (or 3–6 after a Scan). | Seed files, README count, `memory/concepts.md` (step 5). |
| **Missed** | "that should have been a seed" · "you missed X" · "why isn't X a seed?" | One row in `/Users/venkatgullapalli/Documents/my-ai-lab/work-os/brand-os/engagement-os/seedbank/missed.md` (see Rules). No seed is written unless he also says to capture it. | `/Users/venkatgullapalli/Documents/my-ai-lab/work-os/brand-os/engagement-os/seedbank/missed.md`, one row. |

## Steps

1. **Sweep the session** for candidates, four kinds:
   - Something **he said** worth keeping (a claim, a story, a rule, a coined
     label).
   - A phrasing **he adopted** from the system or an outside AI.
   - Something **a third person said** about him or his work, relayed in
     session.
   - A **pattern observed** in his record or behavior, with evidence.

2. **Triage against his threshold** (seed A-LIVE-024) — pass three of four:
   - It repeated (three or more occurrences, or it is a one-off with a name).
   - It is his (not a borrowed method repainted).
   - The label or claim carries the rule (say it and you have said the policy).
   - Someone would ask for it by name.

   **Zero survivors is a valid and expected outcome.** The base rate is zero to
   three per session. Say "no seeds today" and stop — never manufacture a seed
   to fill the step. **More than five survivors means a backfill or a threshold
   failure: switch to Scan — show the top five ranked, say how many more
   passed, write nothing until he picks.**

3. **Write one file per seed** in `/Users/venkatgullapalli/Documents/my-ai-lab/work-os/brand-os/engagement-os/seedbank/session/`, using the template below.
   - **ID:** next number in the existing sequence, zero-padded (run
     `python3 .claude/skills/seed-capture/scripts/next-id.py`; never reuse or renumber). IDs are immutable — folder and prefix
     names are placeholders pending Venkat's naming (loop #43), and a rename
     must never touch an ID.
   - **Attribution class is mandatory**, one of: **his** (verbatim or near) ·
     **endorsed** (a phrasing he adopted — say whose) · **other** (a third
     person's words, relayed) · **system** (an observed pattern; the weakest
     class — flag for his confirmation before any public use).
   - **Names stripped:** no client, employer, or brand name in title or body;
     point to the source record instead (his ruling, 2026-08-13, loop #50).
     Exception precedent: a brand where he is the customer in the story
     (A-LIVE-001) may stay.
   - **Connections:** one to three, stated by hand, honestly — or none.
   - **No quality scores.** Facts stored; judgments computed when a decision
     needs one (`/Users/venkatgullapalli/Documents/my-ai-lab/work-os/brand-os/engagement-os/seedbank/README.md` rule).

4. **Update the `session/` count** in the `/Users/venkatgullapalli/Documents/my-ai-lab/work-os/brand-os/engagement-os/seedbank/README.md` table. Nothing else
   in that file.

5. **Ask once: "did any wording get fixed today?"** Four classes. Then the second part,
   added 2026-09-12 at Venkat's word (01:54 and 02:04): **"what wording could be created?"**
   Run the two lenses in `references/wording-lenses.md` (Chappelle: the true thing nobody
   said flat, edge at situations never people; Godin: one idea per line, a reframe you can
   act on). At most three per lens. Each line says whose it is: his, adapted, or new. A new
   line is kept only when he picks it, recorded `endorsed`. Canon section 8 governs humor.
   In Scan mode this shows the list and writes nothing. "Label" was too
   narrow a container (Venkat, 2026-08-19) — a coined noun is only one of the ways
   language gets settled in a session. All four land in `memory/concepts.md` with a
   pointer. **The container word is his to name; it stays Unknown until he does.**

   - **Term** — a new noun you can point to ("context-bias," "upskilling"). Record
     one sentence of what it means **in his words**. No one-sentence definition →
     record it with definition **Unknown** and keep the pointer. **Never guess.**
   - **Rule sentence** — a full sentence that *is* the rule ("the draft is not the
     unit of work"). It needs no definition; it is the definition. Record the
     **scope** instead — when it applies, when it doesn't. Verbatim or
     near-verbatim only, never a paraphrase dressed up as his sentence.
   - **Distinction** — two things pulled apart that were fused ("requirement
     selection vs check selection"). Record **both sides**, and what changes now
     that they are separate.
   - **Correction** — a word replaced or banned, with the reason ("retraining" is
     wrong because it implies the prior capability was replaced). Record what it
     replaces; banned words also go to the list in `context/PROFILE.md`.

   **Test, all four:** say it and you have said the policy, and someone would quote
   it back. That is the sentence version of "asked for by name."

   **Guard (Venkat, 2026-08-19):** wording *Claude* introduced is captured only when
   Venkat endorses it, recorded `endorsed` with whose words they were. Without this
   the log fills with the system's own phrasings and stops being evidence about him.
   Hard rule 10 is the reason — invented labels come from the system, not from him.
   (This absorbs the receipt's old step 10 — one question, one moment.)

6. **Report:** the IDs written with one-line claims, or "no seeds today" —
   plus any candidate that failed triage narrowly, named in one line so Venkat
   can overrule.

## Helpers (2026-09-10)

- `scripts/find-similar.py "<the claim>"` — the five seeds whose wording is closest, scored 0 to 1.
  Word overlap, no model, same answer every time. Finds repeats; misses paraphrases. Its top
  matches are the first candidates for `Conflicts with:` and `## Connections`.
- `scripts/next-id.py --check` — the next free `A-LIVE` number, and any number on two seeds.
- `references/options--2026-09-10.md` — ways to get more out of seed capture, with what each
  needs from Venkat. Nothing in it is approved yet.

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

- Verify every file written exists at its path before reporting it (evidence
  rule). Unwritten is unreported.
- A seed's Date is when the moment happened; the file records it even when
  written later.
- Quotes marked **his** must be checkable against a record. If the record is a
  voice transcription, note that his words may be garbled (PROFILE rule) —
  near-verbatim is labeled near-verbatim.
- No secrets, no restricted client content, no financial figures.
- **Conflicts are recorded, not resolved.** The duplicate check (run
  `python3 .claude/skills/seed-capture/scripts/find-similar.py "<the claim>"`; a score of 0.45 or
  more is probably a repeat) is also where a contradiction shows up. When
  a candidate disagrees with an existing seed, capture still writes it, with a
  `Conflicts with:` line naming the other seed and what conflicts. The old seed
  is not touched — which one wins is cultivation, for the weekly review.
- **A miss is one row, written when it happens.** When Venkat says something
  should have been a seed, append one row to `/Users/venkatgullapalli/Documents/my-ai-lab/work-os/brand-os/engagement-os/seedbank/missed.md`:
  date · what was missed (one line) · source · which of the four tests it
  passed · why it was missed (one of: no sweep ran · failed triage · judged a
  duplicate · source not on disk) · who noticed. Never batch rows. A row is
  evidence about the threshold, not a change to it — calibration is the weekly
  review's job.
- This skill proposes nothing for building. A seed that looks like a build idea
  still goes to `PLAN.md → Deferred` or the queue by the normal route.
