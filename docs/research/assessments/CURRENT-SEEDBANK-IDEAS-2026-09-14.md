---
title: "Current state: Seedbank and ideas registry material"
date: 2026-09-14
author: Alfred (session 7645e8f5), at Venkat's ask (/goal, 02:35)
kind: evidence snapshot for the Portfolio architecture prompt; read-only scan; never edited after today
canonical_source: work-os/brand-os/engagement-os/seedbank/ (register id `seeds`; live, canonical, evidentiary)
scanned_by: one Explore agent (35 tool uses) plus spot checks by hand; all counts from `find`, `grep`, and file reads on 2026-09-14
labels: Current (live and used now) · Historical (kept as record) · Emerging (drafted or proposed, not ruled) · Inferred (my reading) · Unclear
companion_briefs: CURRENT-PRODUCTS-BUILDS-OPEN-LOOPS-2026-09-14.md · CURRENT-MARKET-OPPORTUNITY-PUBLIC-PROOF-2026-09-14.md
not_here: the career model (see 2026-09-14--career-model-current-state-research-handoff.md in this folder); public assets (companion brief 3)
---

# Current state: Seedbank and ideas registry material

**What this answers.** What idea material exists in the lab today, where each piece is canonical, what state it is in, and where the record disagrees with itself. Written so the Portfolio architecture prompt does not have to rescan the lab.

**Rules used.** Nothing was changed. Counts are from scripts run today. Where two files give different numbers, both are shown. Historical ideas are not promoted to current truth.

## 1. Summary

- **One canonical seedbank, 825 seed files on disk today.** Home: `work-os/brand-os/engagement-os/seedbank/` in three stores: `session/` 331, `written/` 463 (four are summaries, not seeds), `spoken/` 31 (one is a dashboard). Registered as source `seeds` (evidentiary, tier mixed). **Current.**
- **Capture runs; tending does not.** Seeds are captured at every session close by the `seed-capture` skill. The cultivator agent ran once (2026-09-09 to 10). No seed has changed state by tending since; the 52 marked `used` were marked at his word on 2026-09-10. **Current.**
- **Six different totals are on record.** README header 680, README table 820, INDEX 685, source register 797, capability map 790, career-model handoff 825. Only the last matches disk. The capability map itself notes "README count is a second copy of a number." **Drift, known and deferred (AD-22: "the seedbank count" deferred by him).**
- **Five status vocabularies for ideas live side by side.** Seed files use `seedling / used` (plus `ripening / growing` in `spoken/` only). The cultivator was told to use `new / linked / used / gone quiet / unlinked / retired`. The point-of-view library uses `SETTLED / STRONG-CONDITIONAL / EMERGING / EXPLORATORY`. The public value system uses `candidate / private / archived`. The plan file uses `queued`. **Current, conflicting.**
- **ARCHIE has run twice, both in the first week of September, and is idle.** Two idea cards survived, seven candidates were killed, seven sit in a backlog, the inbox is empty. **Current, idle since 2026-09-04.**
- **Naming of the seedbank is an open loop with no registry entry.** README, the skill, and the INDEX all cite "open loop #43" for his own names; the loop is not in the State ledger. **Open, unregistered.**

## 2. The seedbank

**Canonical home.** `work-os/brand-os/engagement-os/seedbank/`. The source register record (`context/sources/REGISTER.md`, `seeds`) says: location the three stores, `standing: canonical`, `use: evidentiary`, `may-inform: what he has said and thought about a subject; what to write next; whether an idea is a repeat; what connects to what`, `not-alone: a rule or a ruling; a fact about the world outside the lab`. **Current.**

**Counts on disk, 2026-09-14** (`find <store> -name '*.md' | wc -l`):

| Store | Files | Not seeds | Seeds |
|---|---:|---:|---:|
| `session/` | 331 | 0 | 331 |
| `written/` | 463 | 4 `SUMMARY-*.md` | 459 |
| `spoken/` | 31 | 1 `garden-state.md` | 30 |
| `_archive/` | 1 | the block that became A-LIVE-146 to 157 | 0 |

Facts sheet today: "seed files: 825; newest live-session seed 0 days ago; missed-seed rows: 0."

**Status lines in use** (`grep -rhoE "^- Status: [a-z]+"` over the three stores): seedling 742, used 52, ripening 22, growing 4, active 1. `ripening` and `growing` appear only in `spoken/`. The one `active` is a body-text oddity in a session seed. **Current.**

**Newest seed.** `session/A-LIVE-331-retrieval-found-the-article-written-from-the-seed-every-time-and-the-seed-never.md`, `Date: 2026-09-13`. Highest ID is 331; no duplicate IDs on disk. **Current.**

**Growth since the index was built.** 140 session seeds sit above A-LIVE-191. Their date lines: 2026-09-09 (14), 09-10 (5), 09-11 (86), 09-12 (32), 09-13 (1), and two dated `2025-08-24` (A-LIVE-233, A-LIVE-234). The 86-in-one-day batch is backfill-shaped, not the "zero to three per session" base rate the skill states. The two 2025 dates predate the lab. **Unclear, likely a typo for 2026.**

**What each store is** (README, `seedbank/README.md`):
- `written/` 459: "Things he wrote, before this month." Five prefixes: A-TOPIC- 186, A-SEED- 153, A-CHR- 77, A-ADR- 35, A-CDR- 8. README's own caveats: never scored or ranked; connections mechanical; chronicle provenance "mostly Unknown. Only 13 of the 77 are confidently his own writing"; "61 of the 186 topic seeds are paired B and A versions of the same card." **Historical material, current store.**
- `spoken/` 30: voicenotes 2026-08-02 to 08-13. `garden-state.md` is its dashboard. **Historical material, current store.**
- `session/` 331: live captures 2026-08-11 to 09-13. Each carries an attribution class (his · endorsed · other · system). INDEX count of the first 191: "his 99 · endorsed 68 · system 21 · other 3." The 21 system seeds carry a "confirm before public use" flag. **Current.**

**Use evidence** (INDEX.md, "the used seeds"): 52 marked `used` on 2026-09-10 at his word. The record behind them: ARCHIE's two runs, the article in progress (cites eight written seeds "as same-family incidents from his own records"), and the concept shelf (points at 30 session seeds; four beside a decision number). INDEX calls the article "the strongest use signal in the collection." **Current.**

**Never done** (README, "What has not been done", and INDEX): no tending pass since 2026-08-14 (30 seeds; 301 session seeds have never been looked at by that count); no connection pass between `written/` and `spoken/`; no naming. `missed.md` has zero rows. **Current gaps.**

## 3. The machinery around it

| Piece | Path | What it does | Label |
|---|---|---|---|
| seed-capture skill | `.claude/skills/seed-capture/SKILL.md` | Scan at every `alfred-close` (writes nothing); Capture on his pick or a marked candidate (writes seed, README count, `memory/concepts.md`); Missed (one row). Threshold 3 of 4 tests (seed A-LIVE-024). IDs from `scripts/next-id.py`; repeat check `scripts/find-similar.py` | Current |
| its wording lenses | `.claude/skills/seed-capture/references/wording-lenses.md` | Head reads "Wording lenses: removed. Removed 2026-09-12 02:32 at Venkat's word: 'remove the lenses. they are poorly applied.'" Full text in the warehouse | Current in working tree, **uncommitted**; git history still shows them live |
| cultivator agent | `.claude/agents/cultivator/` (CLAUDE.md, 11 rules, 5 jobs: review, add, close-to-ready, retire, research) | Tends the seedbank; proposes only | Current, ran once |
| INDEX.md | `seedbank/INDEX.md`, 441 lines | The cultivator's working index. "Last updated: 2026-09-10." Frozen at 191 session seeds | Historical as a count, Current as the only index |
| cultivation pass | `seedbank/cultivation-pass--2026-08-14.md` | First and only connection pass, 30 seeds, "findings and proposals only" | Historical |
| cultivator install record | `seedbank/CULTIVATOR--2026-09-09.md` | Two open items never ruled: scoring-as-facts, "the 161 ideas nobody has looked at." Says "there is no INDEX.md", untrue since 09-10 | Historical, one stale line |
| workflow spec | `seedbank/SPEC--seedbank-workflow--draft--2026-09-11.md` | "status: DRAFT — describes the workflow as it runs today. Adds no new rule." Six stages, each rule tagged his-ruling / his-words / system / proposed | Emerging |
| concept shelf | `work-os/brand-os/engagement-os/memory/concepts.md`, 619 lines | Settled wording in four classes (term, rule sentence, distinction, correction), each with whose words, scope, date, pointer. Last dated line 2026-09-12. Registered as source `concepts` (contextual) | Current |

**Stale lines inside current machinery.** The cultivator's `CLAUDE.md` says "You tend an existing collection of 680 ideas" and hard-codes `session/ 191 · written/ 459 · spoken/ 30`. The concept shelf header says "Per `session-receipt` step 10"; that skill was replaced by `alfred-close` on 2026-09-10. The register record `concepts` notes "the recovery note asks whether engagement-os is even the right home." **Current files, stale text.**

## 4. ARCHIE (idea runs)

- **Agent definition:** `.claude/agents/archie/` (moved 2026-09-09). **Data:** `work-os/brand-os/engagement-os/agents/archie/`. Registered inside source `editorial-work` (evidentiary; "every draft and every ARCHIE output is generated"). **Current.**
- **Runs:** two. `2026-09-03--green-eval-scores` and `2026-09-04--activity-ahead-of-proof`. One surviving idea card each in `outputs/`. One extra draft, `outputs/2026-09-03--agent-authority-six-questions--draft-v1.md` (file changed 2026-09-08). **Current, idle since 09-04.**
- **Kills:** 7 (2 + 5), each with a refuter verdict and a salvage path. **Backlog:** 7 items (3 + 4). **Inbox:** empty; its README says "`/archie` with no input processes the oldest item here." **Current.**
- **Open item:** `F-20260912-0215-1` "Pick the content topics for ARCHIE from the eight shown at 02:10", waiting on Venkat; State work line `today/content-topics-for-archie` is `active`. **Open.**
- **Superseded form:** `~/Documents/_warehouse/archie-v2--skill-form--superseded-2026-09-09/`. Brand-os decision 032: "ARCHIE is rebuilt as WATSON's twin, an agent." **Historical.**

## 5. Other places ideas are held

| Place | Path | What it holds | Label |
|---|---|---|---|
| Point-of-view library | `docs/about-me/POV-LIBRARY-venkat-gullapalli.md`, 1,668 lines, built 2026-09-11 | His beliefs, each with a status `SETTLED / STRONG-CONDITIONAL / EMERGING / EXPLORATORY`. Front matter: "status: DRAFT until Venkat reviews. Nothing here is a rule." Registered inside `about-me` (contextual, tier proposed) | Emerging |
| Public value opportunities | `work-os/brand-os/engagement-os/assets/opportunities/PVO-001..004`, all dated 2026-08-30 | Four opportunity records, all `routing: advance`; `ai_native_verdict: earned` only for PVO-003 | Historical routing; see conflict below |
| Asset registry | `work-os/brand-os/engagement-os/assets/registry.yaml` | AS-001 private, AS-002 archived, AS-003 candidate ("Nobody scores their own forecasts", derived from AS-001), AS-004 private, AS-005 private, AS-006 archived | Current (detail in companion brief 3) |
| Engagement plan | `work-os/brand-os/engagement-os/PLAN.md`, 208 lines | "Standing rule: new ideas go to **Deferred** with a trigger." Deferred rows dated 2026-08-11, still `queued`, including row 11 "Content-candidate capture" and row 13 "Label capture". Both jobs are now done by seed-capture and the concept shelf | Stale, duplicated queue |
| Brand-os plans | `work-os/brand-os/plans/INDEX.md` | One plan, `brand-os-rename`, "Draft — blocked on ruling R1 (repo name)", 2026-09-03 | Emerging, blocked |
| Raw intake | `work-os/brand-os/engagement-os/inputs/` (five dated bundles from 2026-08-26 and 09-08, one pointer) | Inputs, not a registry. The 2026-08-26 opportunity map is covered in companion brief 3 | Historical |
| State ledger lines | `context/state/STATE.jsonl` | Loops and work lines that name the seedbank, listed in section 7 | Current |

**Second seedbank outside the lab.** The draft workflow spec records: "Two seedbanks, the same numbers": the iMac copy at `~/Documents/my-ai-lab-v2/engagement-os/seedbank/` holds different ideas at IDs 192 to 205, so "'Numbers are never reused' is already broken." Not reachable from this machine; not registered. **Unclear (state since the spec was written is unknown).**

## 6. Duplication, conflict, drift

1. **Totals.** Six numbers, one matches disk (section 1). The README header (680) and its own table (820) disagree inside one file.
2. **Status words.** Five vocabularies (section 1). Inside the seedbank alone, the cultivator's six plain words and the seed files' `seedling / used / ripening / growing` never met.
3. **Where retired seeds go.** The cultivator's rule 08 and its `retire` job say "the seedbank's `_archive/`"; the workflow spec cites the 2026-09-09 ruling that retired material goes to the warehouse. Both live. No seed has been retired yet, so the conflict has not fired.
4. **Wording lenses.** Removed in the working tree at his word 2026-09-12; the removal is uncommitted (engagement-os repo shows 13 uncommitted files; the lab root 63). The workflow spec of 2026-09-11 still describes the two-lens scan.
5. **D-137.** `F-20260912-0151-1`: "D-137 is still cited by `alfred-close` and `seed-capture` as in force, while that file lists it as expired." Open.
6. **Dead pointer.** The spec's own conflict list: "Banned words are sent to `context/PROFILE.md`, which does not exist."
7. **Opportunities versus assets.** PVO-001 and PVO-002 still say `routing: advance`; the assets they led to (AS-002, AS-006) were archived on 2026-09-10 at his word ("archive it. this is not what we wanted."). Nothing reconciles them.
8. **Deferred queue.** PLAN.md rows 11 and 13 queue work that seed-capture and the concept shelf already do.
9. **Dashboard counted as a seed.** `F-20260913-0502-4`: "`seedbank/spoken/garden-state.md` is a dashboard counted as a seed." Open.

## 7. Open items that touch ideas (State ledger and follow-ups, quoted short)

- `F-20260912-0117-1` "Design how the daily signal briefs relate to the seedbank … signals stay in the brief outputs, and a seed is written only when he reacts (A-LIVE-194)". Open.
- `F-20260912-0117-2` "Write the seed-capture integration options (MCP servers, capture from Gmail and Calendar…)". Open. State work line `today/seed-capture-integration-options` is `active`.
- `F-20260912-0117-3` waiting on Venkat: "a rule change, so two yeses".
- `F-20260913-0540-4` "The seedbank analysis stopped after themes; its ask 'link seeds 228 and 240 to 076 and 197, yes or no' … are unshown". Waiting.
- `F-20260913-0540-6` "one line in his own words not in the seedbank … plus about 41 system-read candidates". Waiting.
- `F-20260913-0602-3` "the seedbank (engagement-os repo, 13 uncommitted)". Waiting.
- `F-20260910-1627-5` front-matter rollout: "applying it to the seedbank also means updating the cultivator's format rule". Open.
- `F-20260910-1630-7` "Lab-wide build ledger". Open. The workflow spec's fourth proposal ("Build ideas … go in the lab-wide build ledger, not here") depends on it.
- Cultivator proposals never ruled on: scoring shown as facts; the unlooked-at seeds; INDEX's seven "close to ready" one-actions; the 2026-08-14 items S06 and S18.
- Loop #43 (naming): cited in README, SKILL.md line 66, and the INDEX; absent from `STATE.jsonl`. **Open, unregistered.**

## 8. What is settled about the seedbank (his word, as recorded)

- One seed per artifact, nothing merged; connections recorded, never collapsed (README).
- Scoring allowed since 2026-09-09, "always named for what it measures, always with the facts shown underneath" (README).
- No client, employer, or brand names in any seed title or body (ruling of 2026-08-13, README "Provenance").
- Attribution class on every session seed; endorsed phrasings are never presented as his coinage (README, D-006).
- Capture writes only on his pick or a marked candidate (D-137 as cited by the skill; see conflict 5).
- Retrieval reads seeds as evidence, never as a rule (register `not-alone`).

## 9. Inferred, stated as such

- The counting drift is a known, accepted deferral, not an oversight (AD-22 parked "the seedbank count"). **Inferred.**
- The 86 seeds dated 2026-09-11 came from one backfill session, not live capture. **Inferred from the date spike; the receipts of that day would confirm.**
- Nothing in the lab declares the seedbank superseded or scheduled for replacement. The only supersession records in this material are ARCHIE's old skill form and one archived block seed. **Observed absence, not proof.**

## 10. Verification run on this brief

- Every count above was taken by `find` or `grep` today, or is quoted from a named file with its path.
- Historical material (written and spoken stores, the August pass, the 08-30 opportunities, the 08-11 plan rows) is labeled and kept apart from current state.
- Conflicts are listed in section 6 with both sides; none was reconciled.
- No file outside this one was created, edited, renamed, or moved.
- Home of this brief: `docs/research/assessments/`, beside the career-model handoff of the same date. His word on that folder, 00:39: "save report in /docs/research/assessments" (decision `R-2026-09-14-0238-7d32/handoff-home`). The folder is untracked, not in the source register (`lab-reports` covers `docs/reports` and `docs/plans` only), and has no front-door rule yet (`F-20260914-0238-1`, waiting on him). **Noted, not fixed.**
