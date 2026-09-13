---
name: state-tests
what: The five frozen acceptance tests for State v0.1, copied as written from docs/reports/2026-09-13--state-v0-1-design.md section 8. Every test is scored on the Current State Package by a script, never on a judgment. Every test names the failure it exists to catch.
status: frozen at his word, 2026-09-13 07:58 (AD-37: "Freeze S1–S5 as written." "S5 may remain synthetic for v0.1."). A change to a test is his word, recorded in a decision row.
home: context/state/tests/ (beside the ledger and its script; the same shape as context/sources/tests/ for retrieval)
reads_this: context/state/tests/run_tests.py (fetches each package and scores the pass conditions; prints "STATE TESTS: n of 5 passed"); context/state/tests/check_tests.py (the planted faults the check must catch)
part_of: continuity (docs/architecture/CAPABILITY-DEFINITIONS.md#continuity, the State v0.1 subsection)
---

# State v0.1 acceptance tests

**Scope rule for every test.** A test reads only the package the script returns. The package carries `opened`, the files the script read to build it; a test may fail on what was opened.

**S1. Current versus superseded, without reading history** (observed job: the corrected count; commercial: a pricing or positioning decision that was revised)
- Setup: the ledger seeded from the decision files by the "Correction to" rule; nothing else.
- Ask: `package --fields decided --subject career-advisor-drop`.
- Expected: 037 `current`, `supersedes: [036]`; 036 `superseded`, `superseded_by: 037`; each with its row anchor and `authority`; no transcript or receipt read (the script logs what it opened).
- Failure caught: superseded state governing; a link missing so both look current; a decision line with no pointer; history reconstruction hidden inside the call.

**S2. Ownership across parallel sessions** (observed job: two sessions built step 2 six minutes apart)
- Setup: session A runs `state.py claim work:retrieval-v0-1-close-out`; session B asks for the package, then tries to claim the same work.
- Expected: B's package shows the work active, owner A, since, next; B's claim is refused with the owner named, or recorded as a conflict line, never a silent overwrite; when A closes without releasing, the close routine writes a `handed-off` or `paused` line, so the next open shows it.
- Failure caught: duplicate parallel work; ownership lost at session end; a claim that overwrites.

**S3. Open, waiting, and carry-forward survive a close** (observed job: the brief; the waiting list; "next session starts with")
- Setup: a close writes one new loop owned by Venkat, one loop closed with evidence, and one commitment; a new session opens.
- Expected: the new session's package holds the open loop with owner and age, the closed one absent from `open` and present in `changed`, the commitment first in `carry_forward`, and `waiting` as one list from all three homes with the source of each item; an item only he can do stays `waiting` and is not re-queued as fresh work.
- Failure caught: a loop lost between sessions; the three homes disagreeing behind one number; a waiting item re-proposed as new; a commitment that only exists in a chat.

**S4. A material change carries its source; a trivial one does not appear** (observed job: retrieval moved from building to live at his word)
- Setup: after the close of 2026-09-13 06:02, ask `package --fields changed --since 2026-09-12`.
- Expected: the change "retrieval: building to live" with `source` the AD-36 row and the receipt id, `authority: his-word`; the T2 limitation as a `status` line with `authority: system`; the 91 derived index files and the re-rendered transcripts absent.
- Failure caught: a change without a source; noise from file churn; an inference presented as his word; a material change the close did not record (the missing line is the alarm, checked against the receipt's decisions section).

**S5. Scoped commercial state, same kinds, withheld across scopes** (intended job; the Use Case Registry is named in AD-32 but no file with that name exists in the lab today, so the scenario is synthetic and marked so until one is registered)
- Setup: a Professional / Advisory scenario for one account: a brand as subject; a campaign as a second subject; a positioning decision superseded by a later one; an open loop owned by a client contact, waiting on them; a commitment with a date; a workflow status. All written with `scope: professional`.
- Expected: `package --scope professional --subject brand:X` returns the current decision with its predecessor superseded, the open loop with the external owner, the commitment, and the status, each with a pointer; `package --scope ai-lab` returns none of the content and `withheld: 6`; S1 to S3 behaviors hold unchanged on these lines.
- Failure caught: a scope leak; a kind missing for commercial objects; state keyed only to lab jobs; an external owner that the model cannot represent.

**What the five do not test, on purpose:** the brief's judgment of what deserves attention (that is the proving loop, AD-30); Context Assembly's selection; latency beyond "a package builds in under two seconds on today's ledger."
