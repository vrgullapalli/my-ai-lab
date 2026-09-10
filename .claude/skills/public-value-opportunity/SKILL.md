---
name: public-value-opportunity
version: 1.0.0
description: >
  Decides whether a piece of private work contains a meaningful public
  value opportunity, and what it should become. The entry gate of the
  publishing system. Triggers on: public value, is there anything public
  in this, opportunity scan, PVO, should this become public, what could
  this become.
---

# Public value opportunity

> **Base directory:** all relative paths in this skill resolve from `work-os/brand-os/engagement-os/`
> (lab root: `/Users/venkatgullapalli/Documents/my-ai-lab/`). Consolidated to the lab-root
> `.claude/skills/` on 2026-09-07 so it runs from anywhere; its data stayed put.

PROJECT-SPECIFIC to AI Advisory Search. Never install globally, never
generalize without explicit approval. This skill never publishes, sends,
posts, or contacts anyone.

The question this skill answers is NOT "can this be published safely?"
It is: **did this private work reveal a meaningful public value
opportunity, and what should that become?** Safety and verification come
later and support the asset; they never define it.

## Inputs

Anything from the private work: research, company or market analysis,
advisory work, evidence, proof artifacts, instruments, methods, candidate
learnings, drafts — including target-specific work that may contain a
generalizable insight (the generalization becomes the opportunity; the
target-specific artifact stays private).

## Process

1. Name the underlying useful idea, judgment, method, or capability —
   one sentence, no packaging.
2. Name who might care, specifically. "Executives" is not an answer.
3. Name the recognizable moment in their world.
4. Name the useful progress it could create.
5. **Start from AI-native.** The lab's rule is that AI-native is not
   earned (`CLAUDE.md`, Venkat, 2026-09-07). Ask what AI would do inside
   the person's experience: what they give it, what it notices and judges,
   and what changes in the result because of their input. If that design
   is real, classify `ai-native`, set `ai_native_verdict: earned`, and
   write the design to `ai-native-evaluation.md` beside the record: what
   the person provides · what AI does · what changes with their input ·
   what AI must never infer or do · how failure is recognized · how it is
   tested. The validator requires that file and still uses the word
   "earned"; both date from the `ai-native-asset-design` skill, retired
   2026-09-10 at Venkat's word.
6. If AI inside the experience would add nothing real, classify
   `ai-assisted`: AI helps research, create, update, or tailor it, and the
   person gets full value without AI in their experience. Set
   `ai_native_verdict: not-earned` and write one plain paragraph saying why
   to `ai-native-evaluation.md` (the validator requires it). Never add
   decorative AI to make something look native.
7. If neither fits, consider the other public value forms: an expression
   of an existing asset, a field note, an evidence note, a method note,
   direct/private distribution, a contribution to an existing asset —
   or **no action**. "There is nothing here worth making public" is a
   successful outcome when the evidence supports it.
8. Run the `asset-corpus-match` skill before any BUILD leaning.
9. Triage only enough evidence and privacy to avoid proposing the
   impossible or unsafe. Full claim verification happens later, after
   the asset direction is ruled on — do not do it here.

## Output contract

Write one record directory: `assets/opportunities/PVO-<n>/opportunity.md`
(next free number; PRIVATE). Machine record in frontmatter, human view in
the body — never mixed. Validate with
`python3 tools/validate_public_value.py opportunity <dir>`.

Frontmatter (machine record): `id`, `date`, `source_refs`,
`classification` (ai-native | ai-assisted | other-public-value |
no-action), `ai_native_verdict` (earned | not-earned | not-evaluated),
`corpus_disposition` (required unless no-action), `routing` (advance |
hold | closed), `evidence_status`, `missing_evidence`, `provenance`.

Body (human view), in this order: **What I found · Who it could help ·
Why they would care · What I think it could become · Classification and
why · Recommendation with Strength ★–★★★★★ · What happens next.**
Plain language. No IDs, paths, or state names in the human view except
where one is itself the decision.
