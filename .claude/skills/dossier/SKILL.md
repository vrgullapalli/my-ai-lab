---
name: dossier
version: 1.0.0
description: >
  Builds the Stage 1–3 company dossier for one target: the whole job board read
  as one document, newsroom, trade press, leadership moves, AI launches, M&A,
  visible vendors. Every fact tagged observed / claimed / inferred / unknown.
  Two-axis verdict (diagnosability, fit; never averaged), a need level N0–N4,
  and one signal record per observation. This is the "buyer-intelligence" job
  named in ARCHIE's charter. Triggers on: dossier, build a dossier for,
  research <company>, /dossier
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(python3 *), Bash(curl -s https://boards-api.greenhouse.io/*), Bash(curl -s https://api.lever.co/*), Bash(curl -s https://api.ashbyhq.com/*), WebFetch, WebSearch
---

# /dossier <company>

> **Base directory:** all relative paths in this skill resolve from `work-os/brand-os/engagement-os/`
> (lab root: `/Users/venkatgullapalli/Documents/my-ai-lab/`). Consolidated to the lab-root
> `.claude/skills/` on 2026-09-07 so it runs from anywhere; its data stayed put.

Wraps `WORKFLOW.md` Stages 1–3. Plan of record:
`plans/buyer-intelligence/buyer-intelligence--feature--skill-build--v1--2026-09-04-0303.md`
(approved by Venkat 2026-09-04). Reads `docs/state.md` before touching state.

## Hard constraints (rulings; none bend)

- **The presumption: every company in the universe needs him.** The research asks
  *where*, not *whether*. A `reject` verdict is valid only when the full source
  checklist below was searched and the dossier records what was searched.
- **The examination points outward** (Stage 5): at a vendor's claims, a third
  party's work, an inherited decision. Never at the recipient's own competence.
- **Firewall first.** Check `profile/past-engagements.md` and the exclude set in
  `index/companies.json` (`tier: excluded`). Relevate Health is excluded by
  ruling (2026-08-26). A firewalled company gets a folder only to hold the
  refusal record, never outreach.
- **LinkedIn is never scraped.** People enter through public pages, press, and
  Venkat's own knowledge; every public interaction is performed by Venkat.
- **Postings rot.** Re-verify any posting older than the last snapshot before
  citing it. Read the whole board; a single posting is marketing.
- **Dates honestly** per `targets/collectors.json` date_fields: Greenhouse
  `created_at`; Workday age is a floor, never a number.
- **Nothing here writes to brand-identity.** Identity, ICP, positioning are
  consumed by path, never edited.

## Steps

0. **Load state.** `docs/state.md`, `targets/collectors.json`, any existing
   `targets/<slug>/dossier-*.md`, `targets/snapshots/<slug>/`, and the
   company's row in `index/companies.json`. Derive the slug per the slug rule;
   if empty, stop and ask.
1. **Board.** Run `/scan <company>` (target-scan) or fetch the registered ATS
   endpoint. Read every open role as one document: clusters, sequential
   requisition blocks, unfilled seats and their age, stack named, vendors named,
   reporting lines stated, seniority mix.
2. **Newsroom and press page.** Launches, AI offerings (note every unnamed
   vendor behind an AI claim), partnerships, capability announcements.
3. **Trade press.** MM+M, Med Ad News, Fierce Pharma Marketing, Endpoints:
   account wins and losses, agency-of-record reviews, leadership moves.
   `targets/_market/trade-press-sweep-*.md` first, then live search.
4. **Leadership changes.** A new senior arrival is a buyer with no context.
5. **M&A and structure.** Integration is inherited-estate territory.
6. **Vendor relationships visible in public.** Case studies, integrations,
   contract-shaped announcements. Each is an examiner surface.
7. **Baseline and deviation** (Stage 2). Compare each senior posting against
   what everyone writes for that title; the information is in the departure.
   Low deviation everywhere means do not engage.
8. **Qualify on two axes** (Stage 3): `diagnosability` (is there a real,
   provable problem) and `fit` (is it his, against Stage 0 / `profile/`).
   Never averaged. Posting state routes, never filters (fresh / stale /
   reposted / filled / pulled / changed).
9. **Need level** (Need Calculation ladder, merged here per
   `inputs/need-calculation-pipeline--POINTER.md`): N0 unknown · N1 plausible ·
   N2 supported · N3 first-party confirmed · N4 active commitment (budget,
   deadline, hiring, switching). Only N2+ earns outreach; N3 enters
   qualification for an approach; N4 justifies proposal-level work. A need
   hypothesis must name: affected person, trigger, blocked job, consequence,
   current workaround. Missing any one keeps it N1.
10. **Signal records.** One per meaningful observation, schema in
    `docs/state.md`: type, what, source, observed, confidence, hypothesis,
    window (null when unknown, never guessed), next_check, action_state.
11. **Write** `targets/<slug>/dossier-<YYYY-MM-DD>.md` in the exemplar format
    (`targets/real-chemistry/dossier-2026-08-30.md`): Verdict line · Facts ·
    Signals · Angle map (signal → capability → third-party instrument subject)
    · Carrier map · Need level with the five named fields · Search record
    (what was searched, so a reject can be reopened).
12. **Append** the verdict to `targets/index/verdicts.jsonl` (append-only) and
    update the company's `stage`, `tier`, `tier_history[]` with a reason.
13. **Hand off.** Carrier candidates → `targets/_people/` via `/committee`.
    Persona-shaped learnings → `targets/_market/persona-ledger.md`.

## What this skill never does

Draft outreach · build an instrument · touch `outreach/` · invent a competitor
set · score a company against rules it never agreed to · name a client from
Venkat's past engagements in any output that could leave the private repo.

## Time budget

About two and a half hours per company (Stage 5's budget). Step 7 and the
"try to kill it" pass are the ones that get skipped; they are the ones that
matter.
