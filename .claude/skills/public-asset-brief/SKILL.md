---
name: public-asset-brief
version: 1.0.0
description: >
  Produces the one-to-two-page human proposal Venkat rules on before any
  public asset is built: what it is, who it serves, why it deserves to
  exist, and a clear recommendation. Triggers on: asset brief, draft the
  brief, public asset proposal, write it up for my ruling.
---

# Public asset brief

> **Base directory:** all relative paths in this skill resolve from `work-os/brand-os/engagement-os/`
> (lab root: `/Users/venkatgullapalli/Documents/my-ai-lab/`). Consolidated to the lab-root
> `.claude/skills/` on 2026-09-07 so it runs from anywhere; its data stayed put.

PROJECT-SPECIFIC to this lab (`my-ai-lab`; the older project name it used to carry was retired in the 2026-09-10 rule audit). Never install globally. Never
publishes or sends anything.

This is the **primary human decision artifact** of the publishing
system — an editorial and product proposal, not a technical manifest.
It exists so the asset-direction ruling can be made in about two
minutes of reading, with depth available underneath. A safe artifact is
not necessarily a good asset; this brief is where "worth publishing"
gets decided.

## Process

1. Take an opportunity record with routing `advance` and its corpus
   match. No brief without those.
2. Write to the template in `references/brief-template.md`. The five
   one-sentence decision lines come first, always. Machine detail never
   appears in the decision view.
3. Do not ask for external publication approval here — that is a
   separate, later gate (`docs/publication.md`). This brief asks for
   the ASSET DIRECTION ruling only.
4. Deliver it, then stop. The ruling is recorded in the frontmatter as
   one of: PENDING → APPROVED / REVISE / HOLD / REJECTED. Only Venkat
   moves it from PENDING.

## Output contract

Write `assets/briefs/<ASSET-ID>--brief--<date>.md` (PRIVATE).
Frontmatter (machine record): `asset`, `opportunity`, `classification`,
`ruling` (starts PENDING), `date`, `ruled_date` (empty until ruled).
Validate with `python3 tools/validate_public_value.py brief <file>`.

Body: exactly the template. Roughly one to two pages. Plain language
throughout; any technical necessity goes under "Technical receipt" at
the very end or stays in the machine records.
