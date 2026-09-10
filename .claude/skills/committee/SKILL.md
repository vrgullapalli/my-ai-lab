---
name: committee
version: 1.0.0
description: >
  Reconstructs a target company's buying committee from public evidence only:
  job families on the board, reporting lines stated in postings, who owns
  data / AI / commercial / analytics decisions as far as postings say, the
  ownership-dispersion flag, the company's own vocabulary mapped to the
  buyer-term bank, and trigger signals with windows. Feeds targets/_people and
  the persona ledger. Never a demographic avatar. This is the "persona
  extraction" job named in ARCHIE's charter, bounded. Triggers on: committee,
  buying committee for, who decides at, /committee
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(python3 *), WebFetch, WebSearch
---

# /committee <company>

> **Base directory:** all relative paths in this skill resolve from `work-os/brand-os/engagement-os/`
> (lab root: `/Users/venkatgullapalli/Documents/my-ai-lab/`). Consolidated to the lab-root
> `.claude/skills/` on 2026-09-07 so it runs from anywhere; its data stayed put.
> **Reads the hub (spoke since 2026-09-10):** `work-os/brand-os/model/capabilities.json` to map which of his
> capabilities each job family owns a decision about, under `work-os/brand-os/model/17-semantic-usage-guide.md`.
> Returns buyer-term crosswalk additions through the model's `decision-log.md`.

Requires a current dossier (`/dossier`). Plan of record:
`plans/buyer-intelligence/buyer-intelligence--feature--skill-build--v1--2026-09-04-0303.md`
(approved by Venkat 2026-09-04).

## What it produces, and only this

`targets/<slug>/committee-<YYYY-MM-DD>.md`, one page:

1. **Job families present** on the board (commercial, brand, omnichannel,
   customer data / CRM / identity, analytics, AI / digital, medical, market
   access, IT / data engineering, finance-of-AI), counted with the board size
   as denominator. Reuse the job-family classifier that the weekly instrument
   already carries (`work-os/brand-os/audience/weekly/annotate.py`, read-only).
   **Four or more families touching the same capability = ownership-dispersion
   candidate** (DECISIONS #012 rule), flagged, never asserted as fact.
2. **Reporting lines as stated.** Only what postings say ("reports to the VP,
   Commercial Operations"). Each line tagged observed. Nothing inferred about
   who outranks whom.
3. **Decision ownership as far as postings say.** Who is hired to own the
   data model, the AI roadmap, measurement, vendor selection. Gaps are
   recorded as gaps ("no posting names an owner for X"), never filled.
4. **Their vocabulary.** Verbatim phrases from this company's postings and
   press, mapped to `work-os/brand-os/audience/buyer-terms-2026-08/keyword-bank.jsonl`
   and the metadata ten. His coined terms are never attributed to them.
5. **Trigger signals with windows,** from the dossier's signal records: new
   leader, deal clock, reposted seat, sequential requisition block, launch.
   Window null when unknown.
6. **Carrier candidates** → `targets/_people/<person-slug>.md` with
   `warming_state: identified` and the evidence that put them there. Public
   pages and press only. No scraping, no automation, no interaction counts.

## What it never produces

A demographic avatar (age, salary band, corridor, personality) · a competitor
set (ruling: do not invent one) · objections to Venkat's offer · information
sources they trust · internal politics · quotations attributed to anyone ·
content-consumption habits · budget figures. Those fields exist as rows in the
persona ledger and stay **Unknown** until Stage 10 outcomes fill them.

## Persona ledger append

For every learning, append one row to `targets/_market/persona-ledger.md`:
date · company slug · field touched · the learning · label (Provided /
Observed / Inferred / Working hypothesis / Unknown) · source. Committee
output yields Observed and Inferred rows only. Provided rows come from
conversations (Stage 9–10). Simulated objections from the review board are
Working hypothesis, marked "simulated".

**Upstream rule:** three independent buyers describing the same problem in
similar words (three Provided rows, three companies, same field) is the
trigger to *propose* an ICP amendment to brand-identity as a dated ruling.
Nothing else moves upstream; this skill never edits brand-identity.

## Hard constraints

Examination points outward · LinkedIn never scraped · names never leave the
private repo · postings rot, re-verify · every claim carries its label.
