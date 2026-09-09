---
name: design-review
description: Checks a finished visual artifact against Venkat's fixed identity and its own design brief. Use after building an HTML artifact, PDF, or other visual output with frontend-design, web-artifacts-builder, theme-factory, or brand-guidelines, before calling it done. Screenshots HTML via the webapp-testing skill; reads PDFs directly. Flags color, type, and motif violations with evidence labels. Not for checking content accuracy or copy quality (that's a different kind of review).
---

# Design Review

> **Base directory:** all relative paths in this skill resolve from `work-os/brand-os/`
> (lab root: `/Users/venkatgullapalli/Documents/my-ai-lab/`). Consolidated to the lab-root
> `.claude/skills/` on 2026-09-07 so it runs from anywhere; its data stayed put.

## When to use
After a visual artifact is built, before it's marked done. Pairs with
`design-brief` — checks the artifact against both the fixed identity and
whatever that artifact's brief said it would do.

## Inputs
1. `work-os/brand-os/visual/DESIGN-IDENTITY.md` — the fixed identity to check against.
2. The artifact's plan (its `design-brief` section, if one was written).
3. The artifact itself:
   - **HTML** — capture via the `webapp-testing` skill (Playwright
     screenshot), both light and dark mode if the artifact supports both.
   - **PDF** — read directly.
   - Other formats (PPTX, DOCX) — not yet supported. Say so rather than
     guessing from a description.

## What to check
- **Color** — background, text, and accent colors match the identity
  tokens for the mode the artifact targets. Flag pure white backgrounds,
  Tailwind zinc/slate grays, and blue accents — these are the identity
  file's named anti-patterns.
- **Type** — headlines in Newsreader (or its Georgia fallback), body in
  DM Sans, labels in JetBrains Mono. Flag Inter, Roboto, or unstyled
  system-ui.
- **Motif** — corner-rule present only on featured containers, not
  scattered across every element (or absent, if the artifact doesn't call
  for one).
- **Brief conformance** — does the built artifact still do the one job its
  brief said it should, in the structure the brief described?

## Output
A findings list, most important first. For each finding: what was
observed, what it should be per the identity file, and an evidence label
(Observed = seen directly in the screenshot/file; Inferred = implied but
not directly visible). No finding without something to point at.

If nothing is wrong, say so plainly — don't manufacture findings to
justify the pass.

## Rules
- Evidence only — never flag a violation without a screenshot or a direct
  read to back it up (hard rule 3).
- This checks identity conformance, not copy quality, content accuracy, or
  code quality — those are different reviews.
- If the artifact's format isn't supported yet (PPTX/DOCX), say so and stop
  rather than reviewing from a description.
