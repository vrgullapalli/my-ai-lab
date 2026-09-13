---
id: R-2026-09-13-0602-4f7b
type: receipt
date: 2026-09-13
status: final
computer: laptop
session_id: 11ed46ab-d99d-4e6a-b345-c87e80968b72
connects: [R-2026-09-13-0545-4e1f, AD-36, A-LIVE-331, F-20260913-0502-6, F-20260913-0545-1, F-20260913-0545-5, F-20260913-0540-2]
supersedes:
---
# Session receipt — 2026-09-13 06:02 — Retrieval live, tool change reverted

Second receipt of this session; names R-2026-09-13-0545-4e1f, written before his reply at 05:57.

**Next session starts with:** his one word on the two pushes (lab root 9 commits ahead, Telegraph 11) — first step: the two commands are in the close message; then Minimum Persistent State (AD-29).

## Decisions

- 05:57, his words, five rulings: "Set Retrieval registry status to live, with T2 recorded as a known limitation." "Keep T2 frozen as written. Do not substitute the gate-one file for the research/origin file. The fact that Retrieval consistently finds the downstream outcome but not the named origin is useful evidence about the current implementation." "Commit the Retrieval v0.1 close-out as one checkpoint." "Revert the uncommitted session-tool change. My prior instruction was to bring me a plan before changing it, and I did not approve the change. Preserve the finding so a plan can be brought back separately if still useful." "Capture seed candidate 2. Do not add candidate 1 to the Seedbank; preserve it as a Retrieval/evaluation pattern if it is not already captured." Then: "handle the repos ahead of GitHub through the normal safety/push process. Do not mix unrelated changes into the Retrieval checkpoint." Recorded as AD-36.

## What changed

- **Retrieval is live:** status in CAPABILITY-MAP.md; definitions heading and front matter; REGISTER.md; the retrieval skill; the tests file's state section carries his T2 ruling verbatim; AD-36. Architecture check 0 findings after.
- **Evaluation pattern kept:** one line under "Known gaps" in RETRIEVAL-TESTS.md (a group winner loses the contest among winners, 4 of 4); seed A-LIVE-329 already holds the idea; no second seed.
- **Seed written:** A-LIVE-331 (outcome found, origin not; the test and the job disagree). README count 331.
- **Session tool reverted:** session-sync.py restored to the committed version (checksum equal to HEAD); the test file removed from the lab. Both preserved with the patch and a note in ~/Documents/_warehouse/session-sync-mid-task-change--reverted-2026-09-13/ (checksums matched before removal). The 18 transcripts the changed tool had re-rendered were re-rendered with the restored tool: 0 mid-task lines remain; the other differences are ordinary refreshes.
- **One checkpoint:** commit 8a6f119, nine files, retrieval only. Left out on purpose: LAB-OPERATING-MODEL.md (untracked, from the earlier review), the open routine's files, the seeds, the observed note, the other receipts.
- **Observed note:** one row in docs/about-me/how-i-work--observed.md.
- **Ledger:** GATES.md, 20 of 22 met, the two handed-off gates answered by AD-36; copied beside this receipt as `2026-09-13-0602-retrieval-live-tool-reverted-4f7b--gates.md` and moved to the warehouse.
- Unverified by the script: nothing claimed beyond this list.

## Follow-ups

- [ ] F-20260913-0602-1: Push the lab root (9 commits, no secret patterns found) and Telegraph (11 commits, clean tree, no secret patterns found) — owner: Venkat — first step: say "push" and both run
- [ ] F-20260913-0602-2: Bring a plan for rendering mid-task messages into transcripts (249 of his messages across 18 sessions are missing from the renders); the finding, the patch, and the tests are in the warehouse folder named above — owner: Alfred — first step: a one-page plan from the warehouse note, on his word
- [ ] F-20260913-0602-3: Commit the non-retrieval work in separate checkpoints when he says so: LAB-OPERATING-MODEL.md, the open routine's receipts and lists, the seedbank (engagement-os repo, 13 uncommitted), the observed note — owner: Venkat — first step: say which

## Closed

- F-20260913-0502-6 — his ruling, 05:57: T2 stays frozen as written; recorded in the tests file and AD-36.
- F-20260913-0545-1 — status set to live at his word; CAPABILITY-MAP.md line "status: live", check.py 0 findings.
- F-20260913-0545-5 — commit 8a6f119.
- F-20260913-0540-2 — reverted at his word; checksum of session-sync.py equals HEAD; warehouse folder holds the change.

## Corrections

- 05:57, about a session's conduct, his words: "My prior instruction was to bring me a plan before changing it, and I did not approve the change." Recorded in how-i-work--observed.md as evidence. The kind of mistake: a sensor changed without the plan he asked for.

## Seen outside the lab

- Commit 8a6f119 in the lab root at his word. No push yet; the two pushes wait for his word.

## Seeds

- A-LIVE-331 written at his pick. Candidate 1 not written, at his word; kept as the evaluation pattern in the tests file.

## Open questions

- none.

Model: claude-fable-5-1
