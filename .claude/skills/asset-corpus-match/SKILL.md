---
name: asset-corpus-match
version: 1.0.0
description: >
  Searches the existing asset corpus before anything new is proposed, and
  returns one disposition: reuse, customize, extend, merge, build, or
  ignore. Triggers on: corpus match, does an asset already exist for
  this, reuse or build, check the corpus, is this actually new.
---

# Asset corpus match

> **Base directory:** all relative paths in this skill resolve from `work-os/brand-os/engagement-os/`
> (lab root: `/Users/venkatgullapalli/Documents/my-ai-lab/`). Consolidated to the lab-root
> `.claude/skills/` on 2026-09-07 so it runs from anywhere; its data stayed put.

PROJECT-SPECIFIC to this lab (`my-ai-lab`; the older project name it used to carry was retired in the 2026-09-10 rule audit). Never install globally. Never
publishes or sends anything.

Purpose: prevent unnecessary new assets. The corpus is part of every
creation decision; BUILD is the last resort, not the default.

## What to search

- `assets/registry.yaml` — canonical assets and their status
- the registry's `external_corpora` pointers (proof cards, instruments,
  finished profile assets in the techniques repository)
- `profile/proof-library.md` — reusable instrument components
- `docs/research/` and `reports/` — research that may already contain it
- `docs/candidate-learnings.md` — patterns already recorded
- existing release packages and their expressions under `assets/releases/`

## Dispositions — return exactly one

| Disposition | Means |
|---|---|
| reuse | an existing asset already does this job as-is |
| customize | an existing asset fits with a targeted layer added |
| extend | the new material strengthens an existing asset's substance |
| merge | two existing things are actually one asset; combine before adding |
| build | genuinely new job, judgment, or value — nothing in the corpus covers it |
| ignore | overlap exists and the new material adds nothing material |

Two rules that prevent registry sprawl:

- **A different format never makes a new asset.** A PDF of an existing
  asset is an expression.
- **A different audience alone does not make a new asset.** The job,
  judgment, or useful result must materially differ.

## Output contract

Write `corpus-match.md` beside the opportunity record (PRIVATE). A BUILD
disposition without this file is invalid — the validator enforces it.

Frontmatter: `opportunity`, `date`, `disposition`, `closest_assets`.

Body, plain language: the closest existing asset or assets · what
overlaps · what is materially different · whether this is actually new ·
the recommended relationship. If the honest answer is "this is AS-00X
with a new coat," say so.
