---
name: target-scan
version: 1.0.0
description: >
  Collects open roles for a named company or a target list, using whichever
  applicant tracking system that company runs on. Snapshots every scan so
  postings can be diffed over time. Triggers on: scan, scan targets, check
  boards, what is open at, new postings, /scan
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(bun run .agents/skills/*/cli/src/cli.ts *), Bash(curl -s https://boards-api.greenhouse.io/*), Bash(curl -s https://api.lever.co/*), Bash(curl -s https://api.ashbyhq.com/*), WebFetch
---

# Target scan

> **Base directory:** all relative paths in this skill resolve from `work-os/brand-os/engagement-os/`
> (lab root: `/Users/venkatgullapalli/Documents/my-ai-lab/`). Consolidated to the lab-root
> `.claude/skills/` on 2026-09-07 so it runs from anywhere; its data stayed put.

Orchestrates the collectors. Does not fetch anything itself.

> STATUS 2026-08-30: no collector under `.agents/skills/` has been built yet.
> Until one exists, the scan fetches directly against the platform endpoints
> registered in `targets/collectors.json` (the curl allowlist in settings),
> honoring the same date-honesty and snapshot rules. The collector contract
> below governs collectors when they are built; it describes nothing that
> exists today.

## How collectors are found

**Discover them at runtime.** Read every `.agents/skills/*/SKILL.md` and use the
interface each one documents. Never hardcode a collector's flags here — a
collector added tomorrow must work without this file changing.

A collector is enabled unless its frontmatter says `enabled: false`. A missing
key means enabled. Skip disabled ones and name them in the summary, so a fork
can sit a source out without deleting it.

## The collector contract

Every collector under `.agents/skills/` must provide:

- `search` and `detail` commands
- `--format json|table|plain`
- JSON errors on stderr with exit code 1
- Backoff on 429 and 5xx
- Zero runtime dependencies by default
- A `url-reference.md` documenting the endpoints it calls

If a collector does not meet this, it is not registered.

## Steps

### 0. Load state

Read `targets/collectors.json` for the registry of which company runs on which
system. Read `targets/snapshots/` for prior snapshots (layout per
`docs/state.md`).

If a requested company is not in the registry, run the detector first (below)
rather than guessing a slug.

### 1. Detect, when a company is unknown

Fetch the company's own careers page — try `/careers`, `/jobs`,
`/company/careers`, `/about/careers` — and read the applicant tracking system
from the page: a Greenhouse, Lever, Ashby, Workday, Workable, SmartRecruiters,
Jobvite, iCIMS or SuccessFactors fingerprint in the markup.

**The careers page is authoritative. Guessing a slug against an API is not** —
it produces false negatives and silently misses companies whose slug differs
from their name. Record the result in the registry so it is detected once.

### 2. Collect

Run the enabled collectors in parallel where possible. For each company, ask for
**everything open**, not postings matching a keyword. The whole board read
together is the unit of analysis; a single posting is marketing.

### 3. Take the date honestly

Date handling is per-platform and getting it wrong invalidates everything
downstream:

- **Greenhouse** — use `created_at`. `posted_at` and `updated_at` reflect
  refreshes and can be years newer than the true opening.
- **Ashby** — `created_at` and `posted_at` agree. Trustworthy.
- **Lever** — `createdAt` is epoch milliseconds. Trustworthy.
- **Workday** — truncates display at "Posted 30+ Days Ago" and will not
  distinguish 31 days from 300. **True age is not retrievable.** It has to be
  accrued from snapshots, which is the main reason snapshots exist.

Never report an age from a platform that cannot supply one. Mark it unknown.

## Step 4.5 — Collector health check

Collectors rot silently. Theirs rot when a portal changes its markup; ours rot
when an applicant tracking system changes its JSON schema and still returns 200.
Either way the run exits clean and collects junk, and no fallback fires because
nothing hard-failed.

Detect it from evidence the run already holds, at no extra request cost.

**Free pass.** For each collector that ran:

- **Degraded scan.** Company null or empty on every result. Empty titles.
  Undecoded entities or HTML fragments in text fields. URLs that do not point at
  that platform. **The date field we depend on missing, null, or changed type on
  every record.** Any of these means the collector is half-working.
- **Yield history.** A collector that returned nothing this run but has prior
  entries in `targets/snapshots/` is suspect — the same request worked before.

**Escalation, bounded, on suspicion only.** A suspect collector gets **one**
sentinel request: the example invocation from its own SKILL.md, which provably
worked when it was registered, capped at three results. If that returns nothing,
retry **once** with a broader request. Only then is the verdict **broken**.

**A 429 or a block page is never evidence of breakage.** Record the collector as
*inconclusive (rate-limited)*, back off, do not retry.

**Verdicts.** Healthy collectors get silence. Anything else surfaces in the
report. Afterwards, offer to set that collector's `enabled: false` so scanning
skips it until it is fixed — only with confirmation, and the toggle is the only
thing this check may edit.

**Probe-only mode.** `/scan health` skips collection entirely and probes every
installed collector directly, reporting all statuses including healthy. At most
one request, one retry, and one detail fetch per collector. A diagnosis, not a
crawl.

### 4. Snapshot

Write a dated snapshot per company to `targets/snapshots/<slug>/<YYYY-MM-DD>/`
— `board-raw.json` (the platform response verbatim, which IS the full-text
preservation) plus `meta.json`, per `docs/state.md`. Without the text there is
no way to tell what changed later.

Then diff against the previous snapshot and record:

- New postings
- Postings that disappeared, which is the only way closure is detectable — no
  public applicant tracking system exposes a closed flag
- Reposts: same requisition, refreshed date
- Changed title, seniority, location or scope
- Sequential requisition blocks, which reveal roles created in one sitting

### 4.6 The role-shape watch

After snapshotting, match every NEW posting against the omnichannel-
leadership template: a senior role whose text clusters the service-bundle
vocabulary — omnichannel, identity resolution, customer data platform,
Next Best Engagement/Action, journey orchestration, attribution, consent
and preference management, first-party data. Three or more distinct terms
in one senior posting = a match.

A match is **pre-qualified demand**: the company has publicly declared it
needs this capability and started a five-to-nine-month clock before any
hire could deliver it. Flag it in the report as `role-shape match`, with
the terms found, and route it straight to Stage 3 qualification at
elevated priority. The firewall registry is checked before anything else
happens (profile/past-engagements.md).

The template's term list lives with the positioning vocabulary ruling in
docs/rulings.md and is updated from the corpus, not by hand-invention.

### 5. Retain rejects

Anything scored and set aside is kept, with the reason and **the version of the
criteria that set it aside**. When criteria change, the whole store is
re-scored, not only new arrivals. A company ruled out in one month becomes
eligible in another without anyone having to remember it existed.

### 6. Report

State plainly: companies scanned, collectors run, collectors skipped and why,
postings found, what changed since last scan, and any company where age could
not be established.

A completed scan must never hide a failed collector.

## What this skill does not do

It does not score, qualify or diagnose. It collects and records. Scoring is a
separate stage against the profile, and mixing the two makes it impossible to
re-score history when criteria change.

## Rules

1. **Never fabricate a posting.** Everything presented traces to actual collector
   output. A presented posting with no entry in the snapshot store is a
   fabrication.
2. **Record provenance on every entry.** Which collector produced it, and by
   which mechanism. An entry whose URL later resolves to nothing reads very
   differently depending on whether it came from a live API or a stale index.
3. **Never silently drop a posting that has died.** Record it with an expired
   status and leave it out of the presentation. An absent entry looks identical
   to a posting never seen, and that difference is the whole point of the store.
4. **Never backfill a field that did not exist when an entry was written.** The
   entry simply lacks it. Guessing a value destroys the record.
5. **A failed collector does not abort the run.** Log it, continue, and report it.
6. **Pre-filter before detail fetches.** Do not fetch full detail on every search
   hit; select on title and snippet first.
7. **Consolidate mass postings, never accuse.** The same requisition across many
   cities is one row with the spread noted. It describes how a listing is
   distributed, not a verdict on the company.
8. **Health verdicts come only from observed output.** A collector that could not
   be tested is reported as inconclusive, never guessed.
