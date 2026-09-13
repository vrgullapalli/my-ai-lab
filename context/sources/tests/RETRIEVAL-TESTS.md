---
name: retrieval-tests
what: The known-answer test set for shared Retrieval (build step 3, AD-06). Seven jobs across five consumers. Retrieval v0.1 is the minimum behavior that passes these, not a search method.
status: approved by his word, 2026-09-12 02:24 (AD-22), with one boundary rule: Retrieval returns the evidence package; the consumer makes the judgment. Frozen at 02:31 after reachability.py returned 24 of 24 known-answer files inside the eligible set (planted fault: 2 of 26, exit 1). Retrieval v0.1 now exists and is building; the baseline reached 6 of 7 after AD-23, and T2 remains the frozen meaning-match case under final staged-selection close-out. A change to a test is his word, recorded in a decision row. Changed once: T4 at 04:23 (AD-23); T2 stands unweakened.
home: context/sources/tests/ (beside the register's own tests; Retrieval has no store of its own and its one home today is the register). Moved from docs/architecture/ at 02:24; that folder is the capability record and the register counts it as authoritative.
part_of: retrieval (docs/architecture/CAPABILITY-DEFINITIONS.md#retrieval, "Evaluation")
reads_this: context/sources/tests/reachability.py (are the known-answer files inside the eligible source set); the retrieval runner, when built, writes dated runs to docs/reports/
sources_used: context/sources/REGISTER.md; docs/reports/2026-09-12--hand-test-signals-against-lab-context.md; docs/reports/2026-09-12--career-model-capability-scan.md; work-os/brand-os/DECISIONS.md rows 036, 037, 038; RULINGS-IN-FORCE.md D-003; the receipts named in T6
tags: observed (a file read or a count run on 2026-09-12) · inferred (my reading) · his-word
---

# Retrieval known-answer tests

**The question this set answers.** What must shared Retrieval reliably find, with what evidence and limits, before we trust it across the lab?

**Retrieval's contract** (his word, 2026-09-12 02:24). Find the evidence that could materially change the judgment, preserve its source and limits, and expose conflicts or gaps. Retrieval must return: relevant evidence; current versus superseded material; authority and freshness; conflicts; source limits; a missing-evidence state. **The consumer reasons from that package.** A test passes on the package, never on the judgment.

**How to read a test.** Nine fields. "Known relevant sources" names register ids from `context/sources/REGISTER.md`, then the file. `files` is the machine-readable list `reachability.py` checks against the eligible set. "Consumer judgment" is written down so the boundary is visible, and it is not scored.

**Scope rule for every test.** Retrieval reads only registered sources with status live or degraded. A result from anywhere else fails the test, however good it looks.

---

## Current implementation state (2026-09-13)

These tests define required capability behavior, not a preferred search method.

- Retrieval v0.1 is implemented and remains `building` while T2 closes out.
- Baseline after AD-23: **6 of 7** frozen tests pass; T2 is the remaining meaning-match failure.
- The 100-record blind selection test picked A-LIVE-187 in both runs and made the intended inference from the existing representation.
- The staged-selection experiment then picked A-LIVE-187 in stage one under two different salts, but an unvalidated second-level reduction dropped it both times. This is implementation evidence about selection/attention at scale, not a reason to weaken T2 or redefine Retrieval.
- The current close-out may change implementation mechanics while keeping this frozen capability-level test set unchanged unless Venkat explicitly rules that a test itself is wrong.
- Evaluation tests the implementation. Retrieval's architectural necessity is already settled.

## T1. Signal to company, exact relationship

- **Question / job:** "The 2026-09-04 briefs keep naming EVERSANA. What does the lab already hold on this company, and how far can it be trusted?"
- **Consumer:** signal reasoning (the "three moves" step after briefs land).
- **Known relevant sources:** `targets`: the 08-30 dossier (verdict watch; angle map: "A diligence checklist for AI-commercialization partnerships") and the last verdict line for the company. `routine-outputs`: the 2026-09-04 briefs. [observed]
- files: work-os/brand-os/engagement-os/targets/eversana-intouch/dossier-2026-08-30.md; work-os/brand-os/engagement-os/targets/index/verdicts.jsonl; work-os/scheduled-tasks/market-signals/00-all-market-signals/friday/outputs/2026-09-04.md
- **Retrieval must return:** the dossier and the verdict line, each with source id, date, tier, and ceiling; the limits the records themselves carry: dossier dated 2026-08-30 and never updated; every EVERSANA performance figure in the briefs tagged claimed; pharmaphorum owned by EVERSANA; the release page returned 403 twice; the stored board snapshot probed the wrong applicant system and holds 0 postings.
- **Consumer judgment, not Retrieval's:** whether to build the diligence checklist, and how much to trust the dossier now.
- **Known failure to avoid:** the 19 briefs that mention EVERSANA returned as the answer; a brief's claim carried without its claimed mark (the briefs' ceiling is exploratory).
- **Retrieval behavior required:** exact name match across sources; metadata read; record-level limit marks carried with the result.
- **Pass condition:** top 5 holds the dossier and the verdict line; each result names source id, date, and ceiling; at least three of the five limits above are in the returned limits; nothing from outside a registered source.

## T2. Signal to idea, meaning relationship

- **Question / job:** "Lundbeck's chief commercial officer said their agent 'learned the wrong things' after a stepwise rollout guided by pilots. Does this connect to anything Venkat is writing or has said?"
- **Consumer:** signal reasoning; ARCHIE.
- **Known relevant sources:** `seeds`: A-LIVE-187, "A check that has never failed may be evidence of nothing." `editorial-work`: the article's research file, "No public pharma case of a wrong-question AI evaluation was found." `routine-outputs`: the 04-operating-model brief of 2026-09-04. [observed]
- files: work-os/brand-os/engagement-os/seedbank/session/A-LIVE-187-the-green-checks-were-making-me-less-safe.md; work-os/brand-os/engagement-os/editorial/pieces/2026-09-08--green-means-something-different-now/05-research.md; work-os/scheduled-tasks/market-signals/04-operating-model/friday/outputs/2026-09-04.md
- **Retrieval must return:** A-LIVE-187 and the research file in the top 5, each with one line on why it matches (the checks passed and the failure came through what they were not looking for), the seed's attribution tier, the article's gate state, and dates.
- **Consumer judgment, not Retrieval's:** whether this week's evidence closes the article's research check; the vendor-owned outlet caveat on the quote is Retrieval's to carry, the weighing is the writer's.
- **Known failure to avoid:** the word-overlap miss. `find-similar.py` scored 40 of 41 signal claims under 0.4 and did not surface A-LIVE-187 (hand test, 2026-09-12). The signal says agents, learned, deploy; the seed says green, checks, safe. No shared word.
- **Retrieval behavior required:** matching by meaning; ranking a meaning match above louder word matches; the reason for the match stated.
- **Pass condition:** A-LIVE-187 and the research file in the top 5 when the query is the Lundbeck quote alone; the baseline matcher run on the same query returns neither (the miss must be real, not fixed by the wording).

## T3. Alfred, a prior decision that was corrected

- **Question / job:** "How many career-advisor reasoning files were copied into the lab on 2026-09-10?"
- **Consumer:** Alfred.
- **Known relevant sources:** `rulings`: row 036 (says 62) and row 037 ("Correction to 036: the drop holds 61 files, not 62"). `RULINGS-IN-FORCE.md` has no row for either. [observed]
- files: work-os/brand-os/DECISIONS.md; RULINGS-IN-FORCE.md
- **Retrieval must return:** both rows; 037 marked current and 036 marked superseded, with the words that establish the order ("Correction to 036"); the reason in 037 (one file removed at 14:38, never committed, identical copy in the warehouse); each with source id, tier, and date.
- **Consumer judgment, not Retrieval's:** the number to state (61) and whether to say it plainly or with the correction.
- **Known failure to avoid:** row 036 alone; both rows with no order. The register warns "036 is corrected by 037" and superseded rows "are found by reading"; no field marks them.
- **Retrieval behavior required:** exact match on the ruling number; the correction relationship read from the row's own words; a later row on the same subject marked current, the earlier one superseded, both returned.
- **Pass condition:** both rows returned; 037 carries a current mark and 036 a superseded mark; the receipt of 2026-09-10 is not required but must not contradict.

## T4. ARCHIE, idea context without the flood

- **Question / job:** "I want to write about data strategy. What has Venkat already said, what does his positioning say, and what has the lab found?"
- **Consumer:** ARCHIE.
- **Known relevant sources:** `seeds`: spoken seeds S08, S15, S09 (S08 names S09, S15, S16, S05 as connections) and A-LIVE-020. `positioning`: the v5 brief and README. `rulings`: D-003, "'Data strategy consultant' is retired and cannot return without an explicit new ruling." `audits`: the 2026-09-10 rule audit's brand-os file. [observed]
- files: work-os/brand-os/engagement-os/seedbank/spoken/08-data-strategy-defined.md; work-os/brand-os/engagement-os/seedbank/spoken/15-orgs-dont-understand-data-strategy.md; work-os/brand-os/engagement-os/seedbank/spoken/09-test-the-data-model.md; work-os/brand-os/engagement-os/seedbank/session/A-LIVE-020-offers-are-the-bottleneck-not-positioning.md; work-os/brand-os/positioning/context-brief--positioning-v5--2026-09-02.md; work-os/brand-os/positioning/README.md; RULINGS-IN-FORCE.md; evidence/audits/2026-09-10-rule-audit/04-brand-os.md
- **Retrieval must return:** at most ten results; the three linked spoken seeds; the current canonical positioning context with the relevant throughline (the canon `positioning/README.md`, or the v5 brief it carries; his word 2026-09-12 04:23, AD-23); D-003 flagged as a rule that constrains the topic, not as one more hit; each with source id and tier.
- **Consumer judgment, not Retrieval's:** the angle to take, and how the retired identity shapes the piece.
- **Known failure to avoid:** the flood. 16 seed files contain the words "data strategy" (count, 2026-09-12); 826 seed files exist. The other failure: D-003 missing, so the writer is never told the identity is retired.
- **Retrieval behavior required:** keyword match to find candidates; meaning and the seeds' own links to rank them; a cap; a constraining ruling surfaced as a constraint.
- **Pass condition:** ten or fewer results; S08, S15, and the positioning canon (README) or the v5 brief in the top 5, with the throughline ("what has to surround a capability") in its fetched evidence; D-003 present and marked as a rule; nothing from `_archive` or the seedbank's own README, INDEX, or missed.md. (Changed at his word, 04:23, AD-23: four blind picks chose the canon over the old brief.)

## T5. Career model, need to proof

- **Question / job:** "A posting asks for someone who can make a company trust one customer identifier across systems. What in Venkat's record proves he has done that?"
- **Consumer:** the career model's readers: dossier, committee, ARCHIE, briefs.
- **Known relevant sources:** `career-model`: CAP-001 ("Design identity-resolution architectures that let an organization trust a single identifier"; sources: "batch2-meetings (LID, confidence-scored matching)") and the batch2 extract file. [observed]
- files: work-os/brand-os/model/capabilities.json; work-os/brand-os/model/stage1-extracts/batch2-meetings-2022-2023.md
- **Retrieval must return:** the capability id; the supporting extract quoted from the stage1 file; the evidence pointer as the model states it; the pointer's state (20 of 22 artifact paths cited in the extracts do not resolve on this machine, register note 2026-09-12); source id, tier, and date.
- **Consumer judgment, not Retrieval's:** whether the proof is strong enough for the posting; where to record the match (ruling 038: where the work happens, never in the model).
- **Known failure to avoid:** a match with no id or no extract; any write into `model/`; an extract's source path presented as reachable when it is not.
- **Retrieval behavior required:** meaning match from a need to a capability; follow the pointer from capability to extract; report pointer state; refuse to return a career-model match that lacks id and extract.
- **Pass condition:** CAP-001 in the top 3 with the batch2 extract quoted; the result states the pointer does not resolve; `git status` on `work-os/brand-os/model/` shows no change after the run.

## T6. Authority and freshness in conflict

- **Question / job:** "Is there an off-machine copy of the lab?"
- **Consumer:** Alfred (the duty pass).
- **Known relevant sources:** `root-doctrine`: CLAUDE.md, "No off-machine copy of anything. 7 repos, 6 with no remote." `drivers`: STANDING.md, "Snapshot and Dropbox copy one day old." `receipts`: the 09-10 day review ("copied to Dropbox, checksum matched"), the 09-10 13:49 receipt (follow-up F-20260910-1349-5: "Correct the front door line 'No off-machine copy of anything'"), the 09-12 01:43 receipt (the lab root is on GitHub, private). [observed]
- files: CLAUDE.md; context/intent/STANDING.md; evidence/receipts/2026-09-10--day-review.md; evidence/receipts/2026-09-10-1349-scheduled-routines-seedbank-and-backups-f358.md; evidence/receipts/2026-09-12-0143-lab-root-pushed-keys-scrubbed-7c21.md
- **Retrieval must return:** both sides; a conflict flag; for each side its source id, ceiling, tier, and date; the open follow-up that says the front-door line is due for correction; the checksum proof line from the receipt.
- **Consumer judgment, not Retrieval's:** the answer (yes), which side to trust, and whether to correct the front door now.
- **Known failure to avoid:** picking by ceiling alone (root-doctrine is authoritative, so "no copy" wins); hiding the conflict behind one answer.
- **Retrieval behavior required:** authority read from the register; freshness read from the record's date; conflict detection across sources; both sides returned with the marks that let the consumer weigh them.
- **Pass condition:** the CLAUDE.md line and at least one receipt are both in the result; a conflict flag is set; the follow-up is named; neither side is dropped.

## T7. Honest miss

- **Question / job:** "What did Lundbeck's first AI phase with EVERSANA measure, before and after?"
- **Consumer:** signal reasoning; a client-facing proof piece would need it.
- **Known relevant sources:** none hold the answer. 24 briefs mention Lundbeck; 10 record the absence ("Lundbeck has not disclosed performance data from those pilots," 04-operating-model, 2026-09-02). [observed]
- files: work-os/scheduled-tasks/market-signals/04-operating-model/wednesday/outputs/2026-09-02.md
- **Retrieval must return:** a missing-evidence state; the list of sources searched; the nearest evidence, which is the briefs that record the absence; the open trigger the briefs set ("Lundbeck or the unnamed top 20 drugmaker naming the number its first phase moved," not met through 2026-09-09); every vendor figure carried with its claimed mark.
- **Consumer judgment, not Retrieval's:** the sentence "we do not have enough reliable evidence," and what to do about the gap.
- **Known failure to avoid:** manufactured relevance. "20%, 30% cost savings... that's a given" and "a year's worth of work in 10 minutes" are tagged claimed in every brief; returning them without the mark is the failure. So is reading the excluded warehouse or an unregistered folder to fill the gap.
- **Retrieval behavior required:** a missing-evidence path: the gap stated, the search listed, absence evidence returned; a claimed mark never dropped; the register boundary never crossed.
- **Pass condition:** the result carries a missing-evidence state; it lists the sources searched; no claimed vendor figure appears without its mark; no path outside a registered source appears anywhere in the result.

---

## What the tests prove Retrieval v0.1 needs

Each behavior is tied to the tests that require it. Nothing else is in v0.1.

| Behavior | Required by | Why |
|---|---|---|
| Exact match (a name, a ruling number, an id) | T1, T3, T5 | company name; rows 036 and 037; CAP-001 |
| Keyword match (candidates by shared words) | T4 | 16 files carry the words; the first cut, not the answer |
| Meaning match | T2, T4, T5 | no shared word between signal and seed; need to capability |
| Metadata read (source id, date, tier, ceiling, record marks) | T1, T3, T4, T5, T6 | every result carries them; T1's limits are record marks |
| Current versus superseded | T3 | the later row marked current, the earlier one superseded, both returned |
| Authority and freshness carried | T3, T6 | the marks that let the consumer weigh, not a choice made for it |
| Use ceiling and record marks kept | T1, T7 | routine-outputs is exploratory; a claimed figure keeps its mark |
| Conflict surfaced, not settled | T6 | both sides, a flag, the open follow-up |
| Ranking with a cap | T2, T4 | meaning above word noise; ten or fewer |
| Missing-evidence state | T7 | the gap stated, the search listed, absence evidence returned |
| Pointer state (resolves or not) | T5 | 20 of 22 extract paths dead |
| Register boundary enforced | all seven | nothing from outside a live registered source |

**Not proven needed by any test, so not in v0.1:** a vector database, embeddings as a stored index, context assembly, the match written back (T5's write-back is the consumer's job under ruling 038), web search, reading unregistered folders, the judgment itself.

## Known gaps

- **No ruling-versus-ruling conflict.** T6 is doctrine versus evidence. No two of his rulings that disagree were found in the register's sources.
- **No Telegraph test.** Both Telegraph sources are registered with no known-answer case. Deferred at his word, 02:24.
- **No time-to-answer measure.** Needs code to exist first.
- **The blind grader is not defined** for the "why it matches" lines in T2 and T4. The hand test's shape, a helper that sees only two labeled lists, would work.
