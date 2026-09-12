---
title: Step 2 closed, and the Retrieval known-answer test set
date: 2026-09-12
author: Alfred (session d249a842), at Venkat's word ("Close Build Step 2: Source Register, then prepare Retrieval v0.1 with tests before code. Do not implement Retrieval yet.")
kind: one verification pass and one proposal; this report and docs/architecture/RETRIEVAL-TESTS.md are the only files written
follows: docs/reports/2026-09-12--hand-test-signals-against-lab-context.md; docs/reports/2026-09-12--career-model-capability-scan.md
question: "Is Step 2 really closed, and what must shared Retrieval reliably find, with what evidence and limits, before we trust it across the lab?"
result: STEP 2 CLOSED (all checks green, nothing left to commit); TEST SET WRITTEN (7 tests, 5 consumers, proposed); ONE GAP FOUND (the article folder is outside the register, so the definition's own test case cannot pass)
checks:
  register_check: 0 findings, 23 sources, 1450 files
  architecture_check: 0 findings
  planted_fault_tests: 27 of 27
  files_under_two_active_sources: 0 (counted directly, not from the summary)
  governance_research_archive_oldmac_backups_files_in_set: 0
  step_2_files_uncommitted: 0 (all in fd0834b, 02:11)
needs_venkat:
  - rule on the test set, or change it (docs/architecture/RETRIEVAL-TESTS.md)
  - whether to register the three article folders (13 + 3 + 8 markdown files) so test T2's second answer is reachable
  - which of the two next steps below to take
tags_used: observed (a file read or a count run this session) · inferred (my reading) · his-word
---

Alfred — the short version first.

**Step 2 is closed.** The unapproved widening was reverted at his word (AD-21) and committed at 02:11. Every check is green. Governance and research contribute zero files. Nothing in the Step 2 files is uncommitted.

**The test set exists.** Seven known-answer tests, one per job, across five consumers. It defines Retrieval v0.1 as the minimum behavior that passes them, not as a search method.

**One gap matters.** The retrieval definition says "the Lundbeck signal should find the article at gate 2." The article folder is inside no registered source. That test cannot pass until he registers it. Reported, not fixed.

# 1. Step 2 closure (observed)

| What was checked | Result | How |
|---|---|---|
| `upskill-records` covers records only | yes: `location: work-os/upskill-advisor/records`, `pattern: *.md` | REGISTER.md line 358 |
| governance/ and research/ are discovery candidates | yes: facts sheet "discovery: 2 to review" | `check.py` |
| files they contribute to the eligible set | 0 | direct count over every live source |
| warehouse boundary (AD-20) | twelve dated folders plus README; old Mac documents, `_backups`, `research-sources` outside | REGISTER.md line 452 |
| files counted under two active sources | 0 of 1450 | direct count |
| `_archive` material in the set | 0 | direct count |
| any other boundary widened since the approved version | no; one narrowed, and AD-20 rules it ("two files counted under two ids ... Both fixed") | diff of location lines, 02fd720 vs HEAD |
| register check, architecture check, planted faults | 0, 0, 27 of 27 | run this session |
| commit | nothing left to commit; the revert is fd0834b | `git diff --stat HEAD` on the Step 2 files: empty |

# 2. The test set (proposed)

Full text: `docs/architecture/RETRIEVAL-TESTS.md`. One line each here.

| # | Job | Consumer | Known answer | Failure to avoid |
|---|---|---|---|---|
| T1 | EVERSANA, exact | signal reasoning | the 08-30 dossier and angle map, with its limits (dated, claimed figures, vendor-owned outlet, 403s, wrong-ATS snapshot) | returning the 19 briefs as the answer |
| T2 | Lundbeck, meaning | signal reasoning, ARCHIE | seed A-LIVE-187, "A check that has never failed may be evidence of nothing" | the word-overlap miss (40 of 41 under 0.4) |
| T3 | a corrected ruling | Alfred | 61, from row 037; row 036 (62) labeled superseded | returning 036 alone |
| T4 | data strategy context | ARCHIE | three linked spoken seeds, positioning v5, D-003 as a constraint, ten results or fewer | the flood: 16 seed files carry the words |
| T5 | need to proof | career-model readers | CAP-001 with its extract; pointer state "does not resolve" | a match without id and extract; touching the model (ruling 038) |
| T6 | conflict | Alfred | both sides: "No off-machine copy of anything" versus the Dropbox receipts; the open follow-up named | choosing by ceiling alone |
| T7 | honest miss | signal reasoning | "not enough reliable evidence," sources searched, the absence evidence | promoting "20%, 30% cost savings" from claimed to fact |

# 3. Behaviors the tests prove Retrieval v0.1 needs (inferred from the tests)

| Behavior | Tests |
|---|---|
| exact match | T1, T3, T5 |
| keyword match | T4 |
| meaning match | T2, T4, T5 |
| metadata read: source id, date, tier, ceiling, record marks | T1, T3, T4, T5, T6 |
| authority and freshness weighing | T3, T6 |
| use ceiling respected | T1, T7 |
| conflict surfaced, not settled | T6 |
| ranking with a cap | T2, T4 |
| refusal: not enough evidence | T7 |
| pointer state | T5 |
| register boundary enforced | all seven |

Not proven needed: a vector database, stored embeddings, context assembly, web search, reading unregistered folders. Write-back of a match is the consumer's job under ruling 038.

# 4. Recommendations, each with one first step

1. **Build the reachability script before any retrieval code.** [recommended] It resolves every known-answer file in the seven tests against the register and reports which are reachable. First step: a 40-line script beside `context/sources/check.py`, run once, output pasted into the next receipt. It would have caught the T2 gap. It becomes the first sensor the real build runs against.
2. **Register the three article folders, or accept them with a reason.** His word only (AD-21). `engagement-os/editorial/pieces/` (13 files), `engagement-os/outputs/` (3), `engagement-os/agents/archie/outputs/` (8). First step: one line in the reply, "register" or "accept," and the record or accepted-file line follows.
3. **Rule on the test set as written, or cut it.** First step: name any test to drop or change. The file is marked proposed and nothing reads it yet.
4. **Add one Telegraph test before v0.1 is called working.** Both Telegraph sources are registered with no known-answer case. First step: pick one question a Telegraph session asked this month and record its known answer in the same seven fields.
5. **Define the blind grader once.** T2 and T4 need a judge for "why it matches." First step: reuse the hand test's shape, a helper that sees only two labeled lists.
6. **Log the Lundbeck miss in `seedbank/missed.md`.** It has an empty table. The miss is on the record in the hand-test report but not where the seed skill looks. First step: one row, via the seed-capture skill's Missed mode, on his word.

# 5. Adjacent issues seen, not fixed

- The seedbank README says 680 seeds; 826 markdown files exist under the seedbank root today. The count is stale.
- The target snapshot for EVERSANA probed Workable and holds 0 postings; the real board is SmartRecruiters. The correction lives in the dossier prose, not in `meta.json`.
- The EVERSANA dossier's re-check was due one quarter after 2026-08-30. It has not been re-checked.
- The 09-04 pay-band typo ("$84,00 to $117,000") is still open as OI-015.

# Limits of this pass

- One session, one reader. The known answers were chosen by reading; a blind check of "is this really the best answer" has not run.
- The counts are from this machine on 2026-09-12. The seedbank and briefs change daily.
- The tests describe outcomes, not scores. Hit rate and time to answer need code to exist first.

# Addendum, 02:31, after his ruling of 02:24 (AD-22)

**His word:** the seven tests are approved, with one boundary: "Find the evidence that could materially change the judgment, preserve its source and limits, and expose conflicts or gaps... The consumer reasons from that package." Register the article folders. Keep the reachability check tiny. Freeze the tests. Build v0.1. Telegraph, seedbank counts, EVERSANA, and the other adjacent findings wait.

**Done, in his order:**

| Step | Result | Proof |
|---|---|---|
| 1. Tests adjusted | every test now has "Retrieval must return" and "Consumer judgment, not Retrieval's" as separate lines; T3, T6, T7 no longer ask for 61, yes, or the sentence | `context/sources/tests/RETRIEVAL-TESTS.md` |
| Home corrected | moved from `docs/architecture/` (the capability record, read as authoritative by the register) to `context/sources/tests/`, beside the register's own tests; the old copy was never committed and was removed, nothing to archive | `git log` on the old path: empty |
| 2. Source registered | `editorial-work`: article pieces, gate outputs, ARCHIE outputs; 18 files; ceiling evidentiary; record-level tiers ("locked by Venkat" is his word, drafts and ARCHIE outputs are generated) | register check: 24 sources, 0 findings; AD-22 |
| 3. Reachability check | 24 of 24 known-answer files inside the eligible set, 7 of 7 tests; before the source was added, T2's research file was outside | `python3 context/sources/tests/reachability.py`, exit 0 |
| Proved it can fail | a scratch copy with one excluded-warehouse path and one missing path: FAIL, 24 of 26, exit 1 | run this session |
| 4. Tests frozen | status line says frozen at 02:31; a change is his word in a decision row | file header |
| 5. Build v0.1 | not started; plan put to him in the reply | |

**Two corrections recorded** in `docs/about-me/how-i-work--observed.md` as evidence, rules proposed and not confirmed: a component's test set absorbed the consumer's judgment; a new file was placed beside the record that describes it instead of where its kind lives.
