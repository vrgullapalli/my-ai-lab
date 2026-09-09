---
name: design-brief
description: Plans a visual artifact against Venkat's fixed identity before it's built. Use before building anything with frontend-design, web-artifacts-builder, theme-factory, or brand-guidelines — an HTML artifact, a PDF leave-behind, a slide deck. Reads context/DESIGN-IDENTITY.md, asks only what that file doesn't already answer, and writes the decisions into the artifact's own plan under work/plans/{slug}/. Not for artifacts that don't need Venkat's brand identity (internal scratch files, one-off diagnostics).
---

# Design Brief

> **Base directory:** all relative paths in this skill resolve from `work-os/brand-os/`
> (lab root: `/Users/venkatgullapalli/Documents/my-ai-lab/`). Consolidated to the lab-root
> `.claude/skills/` on 2026-09-07 so it runs from anywhere; its data stayed put.

## When to use
Before building any visual artifact that should carry Venkat's identity — an
HTML page, a PDF, a slide deck, a carousel. Not for plain text state files,
receipts, or code with no visual output.

## What it does
Turns a design ask into the Approach/Steps of that artifact's own plan (per
the plan-persistence rule). It does not create a separate design-doc format.

## Inputs
1. `work-os/brand-os/visual/DESIGN-IDENTITY.md` — the fixed identity: colors, type, motif,
   mode defaults. Never re-derive these; only fill what this file leaves open.
2. The design ask itself — what artifact, for whom, what job it does, what
   format.
3. The artifact's plan file under `work/plans/{slug}/`, if one exists yet — this
   skill's output becomes part of that plan, not a substitute for it.

## What to ask
Only what `work-os/brand-os/visual/DESIGN-IDENTITY.md` doesn't already cover:
- What is this artifact, and what's the one job it needs to do for the reader?
- Who reads it, and in what context (screen, print, projected)?
- What format? Use the identity file's Mode Defaults table to pick
  dark/light/hybrid unless Venkat says otherwise.
- Is there a real structure to the content (a sequence, a comparison, a
  single idea) that should shape the layout? Don't invent structure that
  isn't there — numbered steps only when order is real.
- Any content-specific component needs the identity file doesn't cover?

Never ask about colors, fonts, or the motif — those are already answered.

## Output
A short brief, written directly into the artifact's plan file
(`work/plans/{slug}/...--v{N}--{timestamp}.md`) under its Approach and Steps
sections — not a new file.

**Brief structure:**
- **What & why** — the artifact, the reader, the one job it does.
- **Identity application** — mode (dark/light/hybrid) per the identity
  file's defaults, which identity components apply, where the corner-rule
  motif goes if it goes anywhere (not every artifact needs it).
- **Structure** — the real shape of the content, stated plainly ("three
  sequential steps," "one idea, one page") — never invented for effect.
- **Open questions** — anything that needs Venkat's call before building.

## Rules
- If `work-os/brand-os/visual/DESIGN-IDENTITY.md` is missing or looks stale, stop and say
  so — don't proceed on a guess.
- If the artifact doesn't have a plan yet, this skill's output is not a
  substitute — it still needs its own plan per hard rule 16 before it's built.
- Keep it short. This is a brief, not a spec — a paragraph per section.
