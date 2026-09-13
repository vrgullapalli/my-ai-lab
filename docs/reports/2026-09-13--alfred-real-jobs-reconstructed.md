---
title: The real jobs Venkat asks Alfred to do, reconstructed from the record
date: 2026-09-13
author: Alfred (session d249a842), at Venkat's word ("Review your actual work with me across recent AI Lab sessions and reconstruct the real jobs I have asked you to perform. Do not invent a theoretical task taxonomy.")
kind: read-only reconstruction; this report is the only file written
sources: 25 receipts and day reviews in evidence/receipts/ (2026-09-08 to 09-12); git log of 7 repos since 2026-09-01 (127 commits); ARCHITECTURE-DECISIONS.md AD-01 to AD-23; brand-os DECISIONS.md 001 onward; RULINGS-IN-FORCE.md; 9 dated reports in docs/reports/; evidence/sessions/USAGE.jsonl (270 sessions, real skill telemetry from 09-10); docs/about-me/how-i-work--observed.md (40 correction rows); .claude/agents/alfred/LOG.md, TODAY.md, DUTIES.md; context/intent/STANDING.md; this session's own history (02:13 to 05:36 on 09-12)
question: "What are the real jobs, which stress the AI-native architecture most, and which one is the best first proving ground?"
result: 14 JOBS, 10 that matter, 3 that stress the architecture; the best first proving ground is the morning brief with one prepared next action (the open routine), for the reasons in section 4.
counts:
  sessions_since_09_05: 44 (13 on 09-12 alone, nine running at once at the peak)
  receipts: 25; follow-ups opened 89, owner Venkat 52, ever closed 13 (5 of them in one message)
  unreceipted_sessions_waiting: 13 on the facts sheet this morning
  corrections_recorded: 40 rows in six repeating kinds; cognitive overload on its "7th or 8th" telling
  decisions_that_corrected_alfred_acting_alone: 13 (AD-21 the sharpest)
  open_routine_runs: 1 (2026-09-11 15:20); owed and not run since
tags_used: observed (a file, log, or script output read today) · inferred (my grouping) · his-word (quoted)
---

Alfred — the short version first.

**Fourteen jobs, and most of the week was four of them:** close the session and commit what he names; build a shared capability against his rulings and frozen tests; answer one question with a read-only scan; and rule on a waiting list. The morning brief, which should carry the other three, has run once.

**The corrections repeat in three shapes:** read all of it; one thing at a time in plain words; and do not turn something he said in one room into a rule in every room.

**The best first proving ground is the morning brief.** It is daily, he asks for it in his own words, every layer of the architecture has to work for it, the parts already exist, and the day review already measures whether the next action happened.

# 1. The jobs (observed, combined across sources)

E = he asked for it in words. P = Alfred started it on its own or by a hook. Frequency counts are receipts, commits, or decisions.

| # | Job, in his terms | Trigger | One example | Inputs needed | Outcome | His judgment | Friction | Freq |
|---|---|---|---|---|---|---|---|---|
| 1 | Close the session and commit what I name (E, and P at every close) | "done for today", "commit the lab root. all 33", a session ending with writes | receipt 2026-09-12-0143, push after he rewrote 11 commits himself | transcript, facts sheet, git, follow-up list, prior receipts | 22 receipts, follow-ups carried, ~15 commits | he names the files; seed picks | facts.py counts other parallel sessions' files (10 of 25 receipts); 13 sessions unreceipted; 52 follow-ups his, 13 ever closed; keys in committed logs blocked pushes three days | every session |
| 2 | Brief me: where were we, what's on my plate, one next action (P by design) | SessionStart hook, first session of the day, "where were we", "TELL ME WHAT YOU JUST DID" | 2026-09-11 15:20, the one run | yesterday's receipts, follow-ups, sensors, drivers, TODAY.md | a brief and one prepared next action | which item to act on | ran once; "next session starts with the open routine" repeated in four receipts; TODAY.md header still 09-11; parallel sessions mean state cannot live in memory | owed daily, done once |
| 3 | Answer one question with a read-only scan; the report is the only file (E) | "do a read-only scan... Do not implement anything yet"; "Run the hand test" | career-model scan, signal hand test (blind 3 of 3 not present), this report | whole folders read, checksums against other copies, blind judges, a prediction written before the run | 10 reports, each ending in a needs-Venkat list | every report hands 1 to 5 questions back | each scan rebuilds context from scratch; the routine ruling has been open since 09-11 in three reports | 10 in 8 days |
| 4 | Build a shared capability against my rulings and frozen tests (E) | pasted spec, "proceed to Build Step 2", "Approve the seven tests" | AD-01 to AD-23; retrieval 6 of 7 blind; staged T2 twice | his sentences verbatim, existing registries, planted-fault tests, blind agents | capability map, source register, retrieval v0.1, 5 reports | every boundary: AD-21, AD-22, AD-23 | two sessions built step 2 six minutes apart; ~350k tokens per blind question; 13 corrections of Alfred acting alone | 23 decisions, 4 days |
| 5 | Rule on the waiting list in one line (E) | Alfred brings a numbered list; "build me something else" gave it a sensor | "1. done, 2. done, 3- all 4. uninstall 5. done, 7. leave." | the list with first steps | 5 closed at once; the main way anything closes | all of it | 52 items his; items only he can do re-queue; "done" refused by the sensor once | ~6 receipts |
| 6 | Install or port an outside tool faithfully; rebuild an agent as a twin (E) | "install this skill", "not a great great great 4th grand cousin" | cultivator 21 files checksummed; ARCHIE rebuilt | source folder, checksums, privacy read, his naming | 3 installs, 1 rebuild | naming; what counts as a copy | "read every single file" twice in one day | 4 to 5 |
| 7 | Clean the lab, then lock what keeps breaking (E) | "third or fourth time... turn this into a skill"; "lock the root directory" | root lock v2, context-check, warehouse moves | full tree, checksums, dead pointers | moves, lock, two checks | where each thing goes | 395 dead pointers still open | 5 |
| 8 | Get my voice on the record and write as me (E) | voice profile interview, "convert to my voice", drafts | receipt 2026-09-11-1510 with 14 corrections | specimens, interview answers, canon | profile, interview, POV library, canon | line by line: "not at all what I was saying" | most corrections land here; two files disagree on what he approved; "Just show me what the answers were that I approved" | 3 receipts, 8 commits |
| 9 | Editorial research that survives challenge, and the seeds behind it (E for topics, P for capture) | a topic, "run archie", seed picks at close | activity-ahead-of-proof: 1 survivor, 5 kills; article at gate 2 | writing guide, ICP, seedbank, his zips verbatim | idea cards, kills, drafts frozen at his word; seeds 782 to 819 | survivors, gates, seed picks, attribution | ARCHIE's ten data paths dead after the move; 0 seeds from routines; "did any wording get fixed" answered once in eight | 11 commits, 9 receipts |
| 10 | Cloud routines: create, verify, tell me if they're gone; then turn signals into moves with the lab in view (E) | six pasted prompts; "run them in order"; "Run the hand test" | 21 routines verified 21 of 21, then 2 of 29 found live on 09-11 | build and verify scripts, live routine list, target dossiers, seeds, the article | routines, backfill, the hand test report | the routine ruling (open) | briefs cannot open pages; written blind to the lab; run count wrong in two READMEs | 4 receipts, weekly by design |
| 11 | Find and close an exposure (E) | he asks | 7 security records; keys scrubbed and history rewritten 09-12 | Docker state, repos, backups, scan | remediation with stated limits | rotation and scope | three records correct Alfred's own earlier finding | 9 commits |
| 12 | Keep a copy off this machine (E, P in the duty pass) | "backup and commit the lab", "just create a folder in dropbox" | 7,185-file snapshot, checksum verified in Dropbox | snapshot script, checksums | the copy; the front-door line still says none | destination | pointer with a space breaks the check; front door stale three days | ~4 |
| 13 | Audit the rules; stop making rules without two yeses (E) | "confirm with me every single time if you are creating a new rule" | rule audit 09-10, 4 of 6 areas | front door, skills, brand-os rules | 18 follow-ups, sensor reads audit folders | which rules stand | audit never finished; 19 rules made with 5 clear yeses | 4 |
| 14 | Prove the signal engine's evidence, not its output (E) | a pointed question: "was anything actually in place for untrusted input?" | sanitiser tested with six payloads | collectors, postings, code | checks that gate the write | what may be named | code called from nowhere | 12 commits, one week |

Jobs 4 and 14 are the same job in two repos: build against proof, not against a claim.

# 2. Where I keep rebuilding context I should already hold (observed)

- **What he already approved.** "Just show me what the answers were that I approved" (09-11 00:43). The voice profile and the interview disagree on Q2. Job 8.
- **What state the lab is in.** Every scan re-reads whole folders; the facts sheet is the only thing that does not. Jobs 2, 3.
- **Which session did what.** Two sessions built step 2 six minutes apart; a standards plan was overtaken within the hour with no follow-up. Job 4.
- **Which rulings are current.** The Gabriel label answered two days after its folder was archived because a rule still named it; 036 corrected by 037 has no field. Jobs 5, 13.
- **What was asked at close.** "Did any wording get fixed today?" asked eight times, answered once. Job 9.

# 3. Which layer each job leans on most (inferred)

| Job | Needs most |
|---|---|
| 1 close and commit | State (which session changed what), Evidence (receipts), Authority (he names the files) |
| 2 the brief | State, Memory, Context, Trust (a script says what is true), Experience (one item, plain words) |
| 3 read-only scan | Evidence, Context (what is already known), Evaluation (blind judge, prediction before the run) |
| 4 build against tests | Authority (his word for every boundary), Evaluation (frozen tests), Process (parallel sessions) |
| 5 waiting list | Authority, State (what closes), Process (items only he can do) |
| 8 voice | Memory (what he approved), Experience (his words, not mine) |
| 9 editorial and seeds | Memory (seeds), Evidence (receipts), Evaluation (kills) |
| 10 routines to moves | Context (the lab in view), Evidence (source limits), Evaluation (blind judge) |

# 4. The three that stress the architecture most, and the pick (inferred)

**Three stress tests.**

1. **The brief (job 2).** It must read state from the record, not memory, across parallel sessions; weigh a stale front-door line against a fresher receipt; know which ruling is current; and hand him one item in plain words. That is T3 and T6 of the retrieval tests, plus continuity, plus his overload rule, in one daily artifact.
2. **Signals to moves with the lab in view (jobs 9 and 10).** The hand test showed context changed all three picks. It needs retrieval by meaning (T2, still failing), source limits carried (T1), and a blind judge. Weekly, and the routines are mostly gone right now.
3. **Rule on the list, then propagate (jobs 5 and 13).** A ruling must reach every place a rule lives, and a session must never widen its own authority. AD-21 and the Gabriel case are the failures; two-yes authentication is his rule for it.

**The pick: the brief.**

- **Real value.** He asks for it in his own words ("where were we", "what's on my plate", "TELL ME WHAT YOU JUST DID"). 52 items wait on him; 13 have ever closed, 5 in one batch when the list was put in front of him well.
- **Repeated use.** Owed every day. It has run once. Four receipts in a row end with "next session starts with the open routine."
- **Enough complexity.** State from receipts and sensors, current versus superseded rulings, authority versus freshness, follow-ups across parallel sessions, one judgment at the end. Every layer is exercised, none is new.
- **Low overhead.** The open routine, the facts sheet, the follow-up sensor, the day review, and retrieval's T3 and T6 shapes already exist. The work is wiring, not building.
- **Easy evaluation.** The day review already records whether the prepared next action was taken. Add one blind comparison: the brief's one item against what he actually did that day. His one-line rulings are the signal.

The signal job is the more exciting proving case and the worse first one: weekly, the routines are 2 of 29 live, and its evaluation needs a blind judge plus his reaction. Voice has the most corrections and the slowest, most subjective evaluation.

# 5. Not done here

No new architecture is proposed. The open routine's spec, the facts sheet, and the retrieval tests are where the brief would be wired; that is the next conversation, not this report.
