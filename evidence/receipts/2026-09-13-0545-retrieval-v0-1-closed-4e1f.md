---
id: R-2026-09-13-0545-4e1f
type: receipt
date: 2026-09-13
status: final
computer: laptop
session_id: 11ed46ab-d99d-4e6a-b345-c87e80968b72
connects: [AD-35, AD-15, AD-29, F-20260913-0502-1, F-20260913-0502-2, F-20260913-0502-6, F-20260913-0502-7, F-20260913-0540-2, R-2026-09-13-0502-b134, R-2026-09-13-0540-e587]
supersedes:
---
# Session receipt — 2026-09-13 05:45 — Retrieval v0.1 closed

**Next session starts with:** his word on the registry status for retrieval (live, degraded, or building) and on T2's second file (F-20260913-0502-6) — first step: read sections 8 and 10 of `docs/reports/2026-09-13--retrieval-v0-1-close-out.md`, then one word for each; Minimum Persistent State starts after that (AD-29).

## Decisions

- 05:29, his /goal: "Finish Retrieval v0.1 from the current staged-selection state. Reuse the existing Salt A/B stage-one outputs, remove the unvalidated second-level cut, final-rank the existing ~172-record unions, then run the frozen test suite if T2 permits ... Close v0.1 if the evidence shows State and Context Assembly can safely consume Retrieval despite known limitations." Done as asked; recorded as AD-35 (proposed on his condition).
- Alfred's judgment inside the goal: the six other tests were not run staged because T2 did not permit; the one corrective pass was spent on the final stage (the 112 group winners alone); the staged path is not promoted; the registry word stays building because the status change is his (AD-15).

## What changed

Measured by `facts.py close`: 111 files since 05:28, 91 of them the derived retrieval index (ignored by git). 1 commit in the lab root this session (c7e3bcd, made at 05:28 by the previous session, not this one). 47 uncommitted.

- **Experiment script:** `context/sources/tests/staged_experiment.py`: second level removed, `UNION_HEADROOM=180` as headroom, `--picks-only` and `merge` for the corrective pass, the K deviation recorded in the header.
- **Runs (ignored):** `context/sources/index/runs/staged-T2-A-one-level/` and `-B-one-level/` (stage-one picks copied unchanged; 172-record unions; four blind final ranks; packages); `staged-selections.json` and four T2 selections files.
- **Results:** T2 FAIL under both salts at 172 and under both salts on the corrective pass; the seed never in the ten, the gate-one article file always (ranks 5, 3, 2, 3). Seven frozen tests: 6 of 7, same as baseline, no regression. Register 0 findings; architecture 0 findings after three map pointer fixes; reachability 24 of 24; boundary refused; planted faults 27 of 27; career model untouched.
- **Records:** `docs/reports/2026-09-13--retrieval-v0-1-close-out.md` (new); `RETRIEVAL-TESTS.md` state section (tests unchanged); retrieval `SKILL.md` status and a consumer section; `CAPABILITY-DEFINITIONS.md` current evidence; `CAPABILITY-MAP.md` proof and build-steps, three pointer fixes; `ARCHITECTURE-DECISIONS.md` AD-35; `REGISTER.md` status line.
- **Ledger:** `GATES.md` G18 to G22 added and met; 20 of 22 met, G3 and G15 remain handed off (abandoned is terminal in the tool); the ledger stays at the root.
- **Open routine, run late by a subagent at 05:40:** combined late receipt for twelve sessions (`2026-09-13-0540-combined-late-receipt-twelve-sessions-e587.md`), `2026-09-11--today-list.md`, TODAY.md rolled to today, six log lines. Its brief is in the transcript.
- **Seen, not this session's doing:** five seeds A-LIVE-326 to 330 were written at 05:28 by another session at his word ("capture all seed candidates"); `seedbank/README.md` and `memory/concepts.md` changed with them.
- Unverified by the script: nothing claimed beyond the list above.

## Follow-ups

- [ ] F-20260913-0545-1: Registry status for retrieval: live (proof line ready), degraded (a known miss shown on the sheet), or building until the T2 ruling — owner: Venkat — first step: one word; section 10 of the close-out report
- [ ] F-20260913-0545-2: Six staged runs for T1, T3 to T7 were not made because T2 did not permit; decide whether they are still wanted (about two million tokens) or dropped with the staged path — owner: Venkat — first step: "run" or "drop"
- [ ] F-20260913-0545-3: Rebuild the derived index (19 markdown files newer than the 2026-09-12 02:44 build) and add an index-age line to the facts sheet, the freshness sensor the definition names — owner: Alfred — first step: `python3 context/sources/retrieve.py index`, then one line in `facts.py`, on his word
- [ ] F-20260913-0545-4: Operating Scope is implied by the register, not an input to `retrieve.py`; before any Professional or Personal source is registered, scope must become a parameter — owner: Alfred — first step: a one-line design note in the retrieval definition when Minimum Persistent State starts
- [ ] F-20260913-0545-5: Commit the close-out as one checkpoint (staged_experiment.py, the five record files, the report, GATES.md) — owner: Venkat — first step: say commit

## Closed

- F-20260913-0502-1 — the cap choice is moot: the second level was removed at his word (the goal), `staged_experiment.py` header and section 1 of the close-out report.
- F-20260913-0502-2 — T2 was run under both salts on the reused stage-one picks (four blind final ranks, all FAIL by `run_tests.py`); the seven were scored as one file at 6 of 7; the six staged runs were not made because T2 did not permit (now F-20260913-0545-2).
- F-20260913-0502-7 — the open routine ran this session (late, by a subagent at 05:40); receipt e587, six log lines, TODAY.md rolled.

## Corrections

- none from him this session.

## Seen outside the lab

- nothing. No commit, push, publish, or send by this session.

## Seeds

Scan mode, two candidates, neither above 0.45 against the seedbank (closest 0.17 to A-LIVE-329 and A-LIVE-326). Written only on his pick.

1. A record that wins its group of a hundred loses the final contest among winners four times out of four; the developed form of the idea wins in its place. (the close-out runs)
2. Retrieval returned the article written from the seed every time and the seed never; when a test names the origin and the system finds the outcome, the test and the job disagree, not the system and the truth. (the close-out runs; F-20260913-0502-6)

## Open questions

- The subagent's brief carried one line about Alfred's own conduct, passed to him unedited in the close message (F-20260913-0540-2).

Model: claude-fable-5-1
