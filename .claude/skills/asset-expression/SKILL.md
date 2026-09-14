---
name: asset-expression
version: 1.0.0
description: >
  Creates approved expressions of one canonical asset — web page, PDF,
  LinkedIn post or article, Substack article, newsletter section,
  outreach excerpt, reference card — without reinventing the underlying
  idea. Triggers on: expression, make the LinkedIn version, render the
  PDF, adapt this asset for a channel.
---

# Asset expression

> **Base directory:** all relative paths in this skill resolve from `work-os/brand-os/engagement-os/`
> (lab root: `/Users/venkatgullapalli/Documents/my-ai-lab/`). Consolidated to the lab-root
> `.claude/skills/` on 2026-09-07 so it runs from anywhere; its data stayed put.

PROJECT-SPECIFIC to this lab (`my-ai-lab`; the older project name it used to carry was retired in the 2026-09-10 rule audit). Never install globally. Never
publishes, posts, or sends — every expression is handed to Venkat, who
performs any outward action himself.

One canonical asset, many expressions. An expression adapts the asset
to a channel; it never reinvents the idea, and it never becomes a new
canonical asset by existing. Six formats are six expressions of one
asset, not six assets.

## Preconditions

The canonical asset has an APPROVED brief, passed QA, and the specific
expression is approved in the release package's `expressions.approved`
list. No expression from an unruled or failed asset.

## Every expression must carry or reference

- the canonical asset ID and version
- the core message, intact — channel adaptation may compress, never
  contradict
- the intended user value
- only claims from the asset's verified claim ledger — an expression
  may drop claims, never add them
- relevant boundaries (what the asset deliberately does not say)
- provenance appropriate to the channel (the canonical payload stays
  attribution-free; attribution and any offer line are added at this
  layer per channel)

## Channel adaptation, allowed and not

Allowed: length, structure, register, excerpting, a channel-appropriate
opening, the progressive-proof depth the channel warrants.
Not allowed: new claims, new numbers, a different job, manufactured
urgency, curiosity-gap withholding, or anything the four gates would
fail.

**If an expression starts performing a materially different job for a
materially different audience, stop and flag it as a possible new
public value opportunity** — do not silently grow a second asset.

## Output contract

Write expressions under the asset's release package:
`assets/releases/<ASSET-ID>/expressions/<channel>--v<n>.md` (PRIVATE
until Venkat publishes). Each file opens with an HTML comment carrying
asset ID, version, and claim-ledger reference, then the channel-ready
text, paste-ready, nothing else to edit.
