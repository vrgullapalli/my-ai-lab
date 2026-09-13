---
name: capability-definitions
what: One definition per registered shared capability, all in the same shape. Holds the shared system standard (the shape) and the sensor standard (how each one is watched).
status: living. Started 2026-09-12 at Venkat's word. Retrieval v0.1 is live since 2026-09-13 at his word, at 6 of 7 frozen tests with T2 recorded as a known limitation (AD-36). Context assembly remains planned. Operating Scope is a cross-cutting contract. Minimum Persistent State is the next implementation slice of the existing continuity / Memory and state capability, not a new capability entry. The source register is part of retrieval, not a capability (AD-12).
home: docs/architecture/ (his word, 2026-09-12 01:16; AD-14)
read_with: CAPABILITY-MAP.md (the registry; ids here match ids there, checked by check.py); ARCHITECTURE-DECISIONS.md; LAB-OPERATING-MODEL.md
tags: his-word · observed · proposed
---

# Capability definitions

## Shared system standard

**Any important shared system defines these twelve things** (his list, 2026-09-12). Standardize the pattern, not the implementation. Two systems can meet this with very different code.

| Field | The question it answers |
|---|---|
| Job | What is it for, in one sentence |
| Consumers | Who calls it |
| Inputs and outputs | What goes in, what comes out |
| Deterministic responsibilities | What a script decides. Facts, refusals, counts |
| AI responsibilities | What a model decides. Meaning, relevance, judgment |
| Human responsibilities | What only Venkat decides |
| Canonical store | Where the truth lives, if it has one of its own |
| Access method | How a consumer reaches it |
| Failure behavior | What it does when it cannot do its job |
| Evaluation | How we know it works, with a number where possible |
| Evidence produced | What record it leaves |
| Sensors needed | Which conditions from the sensor standard it is watched for |

**The building-to-live gate** (his word, 2026-09-12 01:17). A capability moves from building to live only when three things hold: operational behavior (it runs from an existing path, not because someone remembers), failure proof (planted faults were caught and the proof is written down), and a valid contract (the definition is complete and `check.py` passes). The registry entry records where the proof is in `- proof:`. The check refuses a live or degraded entry without one.

**Plus one line every definition carries** (from the core rule): **AI test.** What should this become now that AI exists, and what would stay the same if AI were removed. If the answer is "mostly the same," the definition says "challenged" and why.

**Foundational capability rule** (his word, 2026-09-13). A foundational capability exists because the architecture requires the job. Tests, experiments, and downstream use evaluate the current implementation and its assumptions; they do not make a required capability repeatedly earn or prove its right to exist. A failed implementation first asks which implementation layer or assumption failed.

## Sensor standard

**Sensors detect conditions** (his list, 2026-09-12): health (did it run), integrity (do its pointers resolve, do live and file match), drift (has it changed from what was approved), missing items (should exist and does not), freshness (how old), unused items (exists, nothing calls it), quality or outcome (did it do the job well). Not every system needs every sensor.

**Three rules the lab already lives by** (observed):
- A sensor reports. It never fixes. (`check_hub.py`: "Deterministic; reports, never fixes.")
- A sensor's own check is proven able to fail before anyone trusts it (`prove-it-can-fail` skill).
- A missing line is itself the alarm (Alfred's log: "an append-only duty log where a missing line is the alarm").

**One finding pattern** (proposed). Seven fields. Used as one line on the facts sheet, and as a follow-up line when it needs a next move.

| Field | On the facts sheet | As a follow-up line |
|---|---|---|
| What was found | the text after `ALERT` | the text after `F-...:` |
| System | the id from the registry | named in the text |
| Evidence | the number, path, or date in the line | the path or number in the text |
| Why it matters | which driver or minimum it touches | in the text, one clause |
| Materiality | `ALERT` means interrupt him; a plain line means show at open; nothing shown means record only | a follow-up exists only at "show at open" or above |
| Suggested next move | not on the sheet | `first step:` |
| Status | open until the line disappears | `[ ]` open, `[x]` closed, or a line in an accepted file with its reason |

**Three materiality levels:** interrupt him · show at the open routine · record only. A sensor picks the level by rule where it can (an unpushed repo is "show"; the account listing 2 routines where 29 are recorded is "interrupt"). The AI may raise a level with a reason; it may never lower one.

**An accepted finding** is one a person reviewed and left on purpose. It goes in an accepted file next to the sensor, one line with a reason, the way `dead-pointers-accepted.txt` and `skill-check-accepted.txt` already work. Counted, not re-listed.

**First sensor written to this pattern:** `docs/architecture/check.py`, 2026-09-12. One line per finding, seven fields, and a one-line summary for the facts sheet. Old sensors are not rewritten; they adopt it when touched for another reason.

**Not now:** no shared sensor engine, no findings database. Sensors stay small scripts beside the thing they watch. The pattern above is the shared part.

### Which sensors each system needs

| System | health | integrity | drift | missing | freshness | unused | quality |
|---|---|---|---|---|---|---|---|
| authority | hook tests pass | | rule text vs what a script enforces | | | | |
| evidence-record | capture ran | anchors resolve | | unreceipted sessions | capture age | | |
| continuity | open line written | | | next action missing | age of oldest follow-up | | did the next action happen |
| drivers | | proof lines resolve | file changed since last open | | state date | | |
| measurement | sensors ran | tests pass | | | | sensor with no consumer | a check proven to fail |
| scheduled-routines | routine ran | live matches file | prompt vs file | recorded but not in account | briefs pulled today | routine nobody reads | moves that changed a decision |
| retrieval | index built | pointers resolve | | coverage gap | index vs newest file | consumer never asks | question-set hit rate |
| context-assembly | | | | | | loaded but unused | task needed something not loaded |
| capability-architecture | check.py passes | ids and paths agree | | entry with no definition | `changed` age | registered, no consumer | |

Blank means not needed yet.

---

## Operating Scope contract

**Job.** Tell shared capabilities which world a job is occurring in, what context belongs there, and what may cross into or out of it.

**Architectural role.** Operating Scope is a cross-cutting boundary, not a separate capability entry. It exists because the same capabilities will operate across materially different privacy, confidentiality, authority, state, and disclosure boundaries. Tests refine its implementation; they do not decide whether a necessary boundary should exist.

**Initial scopes.**

- **AI Lab** — architecture, experiments, system state, capability development, receipts, decisions, reliability work.
- **Professional / Advisory** — clients, prospects, engagements, deliverables, professional relationships and commitments.
- **Career / Portfolio** — career model, opportunities, capability development, portfolio work, products, reputation, income directions and professional network.
- **Public / Content** — site, articles, newsletters, social content, public positioning, public proof and approved public intellectual assets.
- **Personal** — personal projects, household, family, personal planning, personal calendar, personal commitments and other private context.

**What scope controls.** Permitted sources; relevant state and memory; confidentiality boundaries; allowed actors and consumers; permitted actions; what may cross scopes; what must stay out; applicable authority.

**Cross-scope rule.** Technical access does not equal permission to use. Information crosses scopes only when the job legitimately requires it, the relationship is allowed, and authority permits it. Share the minimum detail the receiving scope needs.

**Inference.** The long-term system should infer scope from the active job, project, actor, source, conversation, goal, recent state and contemplated action. When confidence is high and consequence is low, it may proceed. When ambiguity materially affects privacy, confidentiality, public disclosure, access or authority, it stops, degrades or asks.

**Connections.** Email, calendar, Drive, Dropbox, Slack, web, APIs, CRM and future applications are connections / sources / action surfaces. Access to the connection does not grant every scope or actor permission to every record in it.

**Actors.** Alfred, ARCHIE, future specialist agents, automations and Venkat operate through shared capabilities inside applicable scope and authority. Adding an actor does not create a new capability stack.

**Memory and state.** Persistent state keeps scope where material. A fact does not become universally available because it is persistent.

**Failure.** Do not silently cross a material boundary. Withhold unnecessary detail, degrade, or request authority.

**Evaluation.** Relevant context remains available; private/confidential context stays separated; allowed cross-scope use works; routine work does not require constant manual labeling; new actors and connections inherit the same boundary model.

**v0.1 implementation acceptance.** The five initial scopes can be represented; Retrieval can receive or infer AI Lab scope first; hard restrictions can block inappropriate access; permitted cross-scope use is possible; future connections and actors have a clear boundary model. Do not build a large policy engine now.

---

## Definitions

### authority

- **Job.** Say what may not happen without Venkat, and refuse it by script where a script can.
- **Consumers.** Every session, skill, agent, and hook.
- **Inputs and outputs.** In: an attempted action (a write at the root, a stop with open checks, a send, a delete). Out: allowed, or a refusal that says where to go instead.
- **Deterministic.** The three safety minimums. The root lock (`root-lock.py`, 37 tests). The unlazy stop hook. Secret detection in `context-check`. These refuse; nothing reasons about them.
- **AI.** Before acting on anything not covered by a script, name the rule it rests on in one line. Tell a correction from a rule (a correction is evidence; a rule needs two dated yeses).
- **Human.** Rule on new rules. Two confirmations. Approve anything external.
- **Canonical store.** `CLAUDE.md` (the minimums), `AUTHORITY.md` (what Alfred may do), the hook files.
- **Access.** Loaded every session. Hooks fire on their own.
- **Failure.** Fail closed. If a hook cannot run, the action does not happen.
- **Evaluation.** Hook tests pass. The rule audit's count of unsourced rules goes down (71 of 192 on 2026-09-10).
- **Evidence.** Hook refusals in the session; the rule audit in `evidence/audits/`.
- **Sensors.** Health (hook tests). Drift (rule text that no script enforces; the audit found 192 rules and 3 things that refuse).
- **AI test.** Guardrails are meant to be scripts. Remove AI and the refusals stay the same, and that is correct here. What AI adds: judgment on everything the hard set does not cover, and the discipline of naming the rule. Passes, on purpose.

### evidence-record

- **Job.** Keep a record that cannot be quietly rewritten: what happened, who said what, what ran, each with a stable pointer.
- **Consumers.** alfred-close and alfred-open, seed-capture (seeds cite anchors), `facts.py` (reads receipts for follow-ups), claim-verification, retrieval once built.
- **Inputs and outputs.** In: raw sessions, session events, audit runs. Out: rendered transcripts with anchors, receipts, audit folders, log lines.
- **Deterministic.** Rendering (`session-sync.py`), anchors, the new-files-only rule, the append-only log. Counting what changed in a session.
- **AI.** What the receipt says: decisions, corrections, seeds, what changed and why. Reading a transcript for a late receipt.
- **Human.** Nothing routine. Confirms a late receipt when asked.
- **Canonical store.** `evidence/sessions`, `evidence/receipts`, `evidence/audits`, Alfred's `LOG.md`.
- **Access.** By path and anchor. Written as new files or appended lines only.
- **Failure.** If capture breaks (Full Disk Access lost after a tools update), the facts sheet says so and the SessionEnd hook leaves a note. A session that changed files with no receipt shows as an `ALERT` until a late receipt is written.
- **Evaluation.** Sessions older than a day with no transcript: 0 (today's sheet). Unreceipted sessions: 1 today.
- **Evidence.** The record is the evidence. `SYNC-LOG.md` and `USAGE.jsonl` record the capture itself.
- **Sensors.** Health, integrity, missing, freshness, as in the table.
- **AI test.** Rendering and anchoring should stay scripts. The receipt's content is the AI part, and today it is thin: a receipt records what a session did, not what it means for a driver. Challenged, mildly: the possibility brief's "continuous reconciliation" (does this write repeat something, point at something dead, claim done without proof) is the AI job this system does not do yet.

### continuity

- **Job.** Carry where we are, what is open, and what comes next across sessions, so nothing depends on Venkat remembering.
- **Consumers.** Alfred, the open and close routines, every first session of the day.
- **Inputs and outputs.** In: receipts, follow-up lines, TODAY.md, unreceipted-session notes. Out: the facts sheet's open follow-ups, the next-action line, the rolled-forward to-do list.
- **Deterministic.** Finding open `F-` lines (`facts.py loops`), ages, the next-action line, unreceipted sessions, the `waiting.py` view.
- **AI.** Choosing the one prepared next action. Deciding what is material enough to interrupt.
- **Human.** Picks. Closes loops (Alfred prepares, Venkat approves).
- **Canonical store.** TODAY.md (his list) and `.claude/agents/alfred/state`. Follow-ups live inside receipts and audits, which evidence-record owns; continuity reads them. (Corrected 2026-09-12 01:25 after `check.py` flagged both entries claiming `evidence/receipts`.)
- **Access.** `facts.py open`, alfred-open, alfred-close.
- **Failure.** If no open line was written on the first session of a day, the missing line is the alarm. If the close routine did not run, a SessionEnd hook leaves a note and the next open writes a late receipt.
- **Evaluation.** Open follow-ups: 57 today. Oldest: 2 days. The five measures in `DONE.md` section 10 (for example "opened and started nothing") are not measured yet.
- **Evidence.** Receipts, the facts sheet, TODAY.md copied to receipts at day end.
- **Sensors.** Health, missing, freshness, quality, as in the table.
- **AI test.** Challenged. Today this would work almost the same without AI: a regex finds `F-` lines, a hand-kept list rolls forward, a sheet prints counts. The AI part is one prepared next action. What it should become: the AI reads the follow-ups, the drivers, and what changed, and decides what matters now; TODAY.md becomes a view. **Fault, observed:** "waiting on Venkat" lives in three trackers.

#### Minimum Persistent State v0.1 implementation slice

Minimum Persistent State is the next implementation slice of `continuity` / Memory and state, not a new capability entry.

- **Job.** Maintain a compact, current, source-backed representation of what is currently true, active, decided, unresolved, waiting, owned, or superseded so the lab stops rebuilding operational truth from raw records.
- **Why now.** The observed jobs repeatedly reconstruct what Venkat approved, current lab state, which session did what, which ruling is current, what is waiting, and what should carry forward.
- **Initial consumers.** Alfred, the morning brief / open routine, session start and close, context assembly, capability development and project continuation.
- **Minimum state objects.** Current decisions/rulings; active work; material session/work ownership; open loops; waiting-on-Venkat items; current capability/project status where useful; explicit commitments/carry-forward; supersession; current drivers/goals by reference.
- **Record minimum.** What it is; current status; operating scope; source/provenance; last established/changed date; authority; supersession where applicable.
- **Output.** A compact Current State Package: active, decided, changed, open, waiting, ownership, superseded, carry-forward and provenance. A consumer receives only the fields it needs.
- **Deterministic.** File/repo state, session ids, timestamps, sensor results, explicit status fields, ownership markers, receipt existence, open/closed flags and explicit supersession.
- **AI.** Interpret which changes are material; summarize current state; connect state across sources; identify likely stale/conflicting state; propose what deserves attention. AI does not silently turn inference into authoritative state.
- **Human.** Material rulings, closure where judgment is required, scope/authority changes and consequential ambiguous conflicts.
- **Update triggers.** Approved/superseded decision; work begins/hands off/completes; open loop created/resolved; material limitation accepted; project phase changes; explicit commitment made. Do not rewrite state for trivial events.
- **State is not history.** Keep current state plus enough provenance to reconstruct why; raw transcripts and receipts remain evidence.
- **Failure.** Expose conflicting or stale state; reconstruct missing state from evidence where feasible; surface parallel ownership conflict; keep human-owned items waiting rather than re-queuing them as fresh work without new information.
- **Evaluation.** Alfred knows what was approved; current vs superseded rulings resolve; open loops and waiting items survive sessions; parallel ownership is distinguishable; new sessions resume without rereading whole folders; material state traces to evidence.
- **v0.1 acceptance.** Current decisions resolve without raw-history reconstruction; active work/ownership are visible; open/waiting items persist; superseded state no longer silently governs; state points to evidence; the morning brief and context assembly can consume it; obvious duplicate work is avoidable.
- **Stopping rule.** Build only enough State for current lab continuity, the morning brief and context assembly. Do not build universal memory, event sourcing, a graph database, personal/professional state integration, goal-management software or another agent.

### drivers

- **Job.** Hold what Venkat is working toward right now, so sensors and the open routine know what matters and what would threaten it.
- **Consumers.** alfred-open, the duty pass, implication-lens, hand tests, retrieval (for weighting by driver).
- **Inputs and outputs.** In: his rulings on what a driver is, plus dated state lines. Out: for each driver, what a script can prove, what would threaten it, and the next meaningful change.
- **Deterministic.** The proof lines each driver names (unpushed commits, snapshot age, Telegraph items needing him). "Changed since the last open."
- **AI.** Read what the facts mean for each driver. Decide whether something material changed.
- **Human.** Add, replace, or retire a driver. Four is the cap.
- **Canonical store.** `context/intent/STANDING.md`. Append-only.
- **Access.** Read at open and in every duty pass.
- **Failure.** If the file has no state line for a driver, the open routine says "unknown," never guesses.
- **Evaluation.** Each driver's own "working when" line. Driver 4's says: nothing a script can prove yet, and the open routine says so.
- **Evidence.** State lines with dates inside the file; log lines per duty.
- **Sensors.** Integrity (proof lines resolve), drift (file changed since last open), freshness (state date).
- **AI test.** The file is a record and should stay one. Its pattern, driver to belief to evidence to threat to next change, only works if something reads meaning from facts. Without AI it is a list of threats someone must remember to check, which is the checklist he retired on 2026-09-05. Passes, if the reader is the AI.

### measurement

- **Job.** Say what is true by script, never by a model's opinion.
- **Consumers.** The open and close routines, the duty pass, unlazy, Venkat through the facts sheet.
- **Inputs and outputs.** In: the file tree, git, launchd, the account's routine list, dates. Out: one line per fact, `ALERT` when material.
- **Deterministic.** Everything it says.
- **AI.** Nothing inside a sensor. Deciding what a sensor result means belongs to the consumer.
- **Human.** Approves a new sensor line, since each one becomes something he reads every morning.
- **Canonical store.** `facts.py`, `waiting.py`, `session-sync.py`, `context-check.sh` with `dead-pointers.py` and `skill-check.py`, `verify.sh`, `check_hub.py`, and their tests and accepted files.
- **Access.** Hooks at start and end, launchd at 9, 13, and 18, and by hand.
- **Failure.** A sensor that cannot measure says so in its line ("verify.sh cannot run"). It never prints a guess.
- **Evaluation.** Tests pass (`facts.py` has 16). Every check has been shown to fail on a planted fault.
- **Evidence.** The facts sheet at every open, the check outputs, test runs.
- **Sensors on the sensors.** Health (they ran), integrity (tests), unused (a sensor line nothing reads), quality (proven able to fail).
- **AI test.** By design this is the one place AI is kept out: agents grading themselves report false success about 76% of the time. Remove AI and nothing changes, and that is the point. What AI should do around it: pick which sensor to run for which question, and read the results. Passes, on purpose.

### scheduled-routines

- **Job.** Run work unattended in the cloud on a schedule and bring its output back into the lab.
- **Consumers.** Market signals (21 routines on paper), daily briefing, matching roles scan, weekend read, weekly synthesis.
- **Inputs and outputs.** In: a self-contained prompt built from shared parts, a schedule, a model. Out: a private page on claude.ai, pulled into `outputs/` by the open routine.
- **Deterministic.** `assemble.sh` and `build.sh` make the prompt. `verify.sh` proves live matches file. `facts.py` counts briefs pulled today.
- **AI.** Everything inside a run: search, judge, write the brief, pick the three moves.
- **Human.** Create or change a routine. Rule on the missing 21 and on the two whole-market briefs (open since 2026-09-09).
- **Canonical store.** `work-os/scheduled-tasks/`.
- **Access.** Routine ids; the routines page; pulled outputs.
- **Failure.** Runs half-blind (cannot open web pages, "organization policy"). A routine that vanishes from the account is caught only when `verify.sh` fails to run.
- **Evaluation.** Live routines match their files, all 21 on 2026-09-09. Briefs pulled today: 0 of 7. Moves acted on: none recorded.
- **Evidence.** `runs/` records, `outputs/` copies, `verify.sh` output.
- **Sensors.** Health, integrity, drift, missing, freshness, unused, quality, as in the table. Most exist; "recorded but not in account" is the one that was missing on 2026-09-11.
- **AI test.** Challenged, by evidence. The hand test on 2026-09-12 read one week of briefs with the lab in view. The blind judge found all 3 new moves "not present" among the briefs' 21. The briefs' moves were "search more" and "ask someone." So the AI in the routine is real, but the process is a pipeline: gather, then reason blind, then stop at a page nobody reads. What it should become: the routine gathers; the reasoning runs in the lab with retrieval in view. That is why retrieval is build step 3 and the routines wait.

### retrieval (live since 2026-09-13; v0.1 implemented 2026-09-12)

- **Architectural necessity.** Retrieval is a required foundational shared capability. Its existence follows from the lab's need to access and qualify existing evidence across jobs, sources, actors and scopes. Tests evaluate the implementation and its assumptions; a failing implementation does not make Retrieval re-justify its existence.
- **Job.** Find the evidence already available to the system that could materially affect the current job, within the applicable operating scope and hard source boundaries, and return it with provenance, limits, conflicts, and material gaps intact.
- **Relevant evidence.** Evidence is relevant when, given the job, consumer, scope and task context, it could support, weaken, constrain, contradict, update or expose a material gap in the downstream judgment. Relevance is not just topic similarity. Retrieval should find the evidence that deserves to be in the room when the judgment is made.
- **Consumers.** Alfred, ARCHIE, signal reasoning, career / portfolio reasoning, project work, Telegraph+, context assembly, content/research workflows, seed-capture's repeat check, and future actors/capabilities that need governed evidence.
- **Inputs.** Job/question; consumer; Operating Scope; relevant task context; optional source scope; hard constraints such as privacy, security, confidentiality and prohibited sources. The human should not need to specify all of these manually forever.
- **Output.** A **Governed Evidence Package**, not the final judgment. Where material it carries: actual evidence; stable source id; path/anchor/record id; source/date/freshness; canonical/replica/historical/unavailable state; current/corrected/superseded relationship; pointer state; authority/tier; use ceiling and `not-alone`; claimed vs observed marks; conflicts; corrections; unresolved pointers; missing evidence; incomplete coverage; and what was searched when absence matters. Valid package states include strong, partial, conflicting, weak-with-limits, no adequate evidence, and unresolved gap.
- **Deterministic.** Hard source/scope eligibility; security/privacy/prohibited boundaries; source identity/location; source and index coverage; source-health facts; dates and known metadata; exact ids/entities and lexical matches where reliable; deterministic fetch of underlying evidence; provenance; pointer state; explicit correction/supersession; refusal outside hard boundaries.
- **AI.** Understand the job and task/scope context; plan likely evidence spaces; recognize conceptual relationships despite different wording; rank/select evidence; recognize possible conflicts and likely gaps; assess likely incompleteness; explain why evidence may matter. AI may not manufacture evidence that was not retrieved from an eligible source.
- **Human.** Source admission/removal; hard source boundaries; material cross-scope permission changes; source-authority policy; changes to the Retrieval contract; disputed frozen capability tests; consequential judgments beyond delegated authority.
- **Canonical store.** None for knowledge. Sources stay canonical where they live. `context/sources/REGISTER.md` is Retrieval's governed list of what it may depend on. Derived indexes/runs are rebuildable implementation artifacts, not canonical knowledge.
- **Access.** `python3 context/sources/retrieve.py` for deterministic index/search/fetch plus the Retrieval skill/model for meaning-based selection. The register resolves stable source ids through `python3 context/sources/check.py resolve <id>`. Retrieval remains callable from sessions/scripts, not a required service.
- **Operating flow.** 1) establish job/consumer/scope/context; 2) apply hard eligibility; 3) query planning/routing; 4) candidate discovery using the minimum appropriate exact/entity/lexical/semantic/metadata/relationship methods; 5) rank/select evidence that could materially affect the job; 6) deterministically fetch the real records; 7) qualify provenance, authority, freshness, status, limits, conflicts and gaps; 8) return the Governed Evidence Package. Retrieval stops before interpretation, judgment, decision, action and consumer-specific write-back.
- **Failure.** Do not read or expose prohibited/out-of-scope evidence. Report unavailable, stale/historical, broken-pointer and partial states. Preserve meaningful conflict. Return weak evidence only with its limits. Return an insufficient-evidence state rather than promoting weak matches because something must be found. Do not claim completeness when selection cannot support it.
- **Evaluation.** The frozen known-answer set remains `context/sources/tests/RETRIEVAL-TESTS.md`. Evaluation measures implementation quality: relevant-evidence recall; eligible-evidence precision; scope correctness; authority correctness; conflict preservation; evidence sufficiency; refusal correctness; and operational usability (latency/cost/resources). Tests do not decide whether Retrieval deserves to exist.
- **Current evidence.** Closed for downstream use on 2026-09-13 at 6 of 7 frozen tests, no regression (`docs/reports/2026-09-13--retrieval-v0-1-close-out.md`). T2 is the one failure and a recorded limitation: the seed A-LIVE-187 is picked blind inside a list of about a hundred (4 of 4 across the hundred-line test and the stage-one groups) and never in a final rank among winners or a full scoped pass (0 of 10); the article file written from it is returned every time. Boundary, provenance, supersession, pointer state, conflict, and missing-evidence behavior pass by script. The staged path is an experiment beside the tests, not the default. What downstream consumers get, and the eight known limitations, are in sections 7 and 8 of that report. T2 stays frozen as written at his word (2026-09-13 05:57): finding the downstream outcome and not the named origin is evidence about the implementation, kept on purpose.
- **v0.1 acceptance.** Governed Evidence Packages work on representative jobs; hard boundaries hold; underlying evidence is fetched; provenance/material limits travel; conflicts/gaps can survive; insufficient evidence is representable; important failures are visible; architecture/safety checks remain valid; known limitations are recorded; Minimum Persistent State and Dynamic Context Assembly can safely consume the interface.
- **v0.1 does not require.** Perfect semantic recall; optimal ranking; production latency; minimum token cost; embeddings; a vector database; final reranking design; fixed candidate/group sizes; every source/connector/scope/actor; every failure solved.
- **Stopping rule.** Once the implementation is sufficient for downstream use, stop improving Retrieval in isolation. Record non-blocking limitations and let downstream use determine their priority. Stopping implementation work means sufficient for the current stage, not optional or complete forever.
- **Change control.** The capability contract changes only when evidence shows the job, output, responsibility boundary, scope behavior, failure behavior or evaluation contract is wrong/incomplete. Models, prompts, embeddings, vector stores, lexical search, rerankers, staged selection, candidate limits, K values, chunking, indexes, caching and performance work are implementation changes unless they alter the contract.
- **Evidence.** Dated evaluation reports in `docs/reports/`, run ledgers, source-register checks and the Governed Evidence Packages returned in tests/real jobs. Consumer write-back remains the consumer's responsibility.
- **Sensors.** Source/register integrity, health, coverage, freshness and discovery; index coverage/freshness; pointer integrity; quality against frozen tests; eventually unused consumers, miss patterns, context impact and outcomes when real usage makes them meaningful.
- **AI test.** Passes clearly. Without AI, exact/lexical retrieval still works, but meaning-based relationships that matter to current jobs are missed. AI is part of the core design for interpreting the job, conceptual matching and evidence selection; deterministic mechanisms still establish facts, boundaries and fetch.

#### Source register (build step 2, built 2026-09-12; the first half of retrieval)

- **What it is.** Retrieval's own list of what it may depend on: each source's location, kind, owner, standing, authority tier, how its dates are read, and its use limits. A store, not a capability (AD-12). It lives at `context/sources/REGISTER.md` (AD-16) in the same record shape as the capability registry. Its check, `context/sources/check.py`, proves the register (unique ids, required fields, allowed words, no two sources claiming one location, no location nested inside another source's), watches source health (missing, moved, unreadable, empty), measures coverage and freshness per source, runs source discovery, and resolves an id to its current location.
- **What a source is:** a folder, file set, or file the lab treats as knowledge. Twenty-four registered on 2026-09-12: twenty-one inside the lab (editorial work, added at 02:24 for retrieval test T2, AD-22; seeds, receipts, audits, transcripts, Alfred's log, the drivers, the rulings files, root doctrine, the about-me drafts, the career model, the voice canon, positioning and audience, target dossiers, assets, routine outputs, lab reports and plans, Telegraph+, the Telegraph instruction package, the concept and profile notes, and the architecture folder) and three outside it (the public site on the Desktop, the career-advisor snapshot from the iMac, and the warehouse's dated lab-move folders; narrowed from the whole warehouse at his word, 2026-09-12 01:55, AD-20). Outside sources are recorded by absolute path: existence is checked, files are not counted, nothing is copied in.
- **Stable identity** (AD-17). Consumers ask by id, never by path: `python3 context/sources/check.py resolve career-model` is the one deterministic path from id to current location, status, standing, and use limits. A path written into a consumer's own file is a copy that goes stale.
- **Standing** (AD-17): canonical · replica (with `canonical-at`) · historical · unavailable. One source keeps one id across its canonical and replica locations; a copy never gets its own id, and the check refuses a `canonical-at` that names another registered id (his word, 2026-09-12 01:44). Status keeps the registry standard's five words; only live and degraded may be read.
- **Authority tiers** (reusing the seedbank spec's tags): his-ruling · his-words · endorsed · system · proposed · generated · mixed. `mixed` means each record carries its own tier in a named field, and the register says which field. A retrieval result carries the tier of its source and of its record.
- **Use limits** (AD-17). The strength of the action must not exceed the strength of the evidence. Each source carries `use` (authoritative · evidentiary · contextual · exploratory: the ceiling, meaning the maximum influence permitted, which a consumer may lower for a specific job and never raise; his word 2026-09-12 01:44), `may-inform` (the jobs it may reasonably influence), and `not-alone` (what it must never establish by itself). Job limits, not a grade. The script proves they are present and the words are allowed; the AI reads them before leaning on a source; nothing scores them.
- **Admission.** Seven questions in the register's header (what job, what it represents, how authoritative, how current, can it be traced, is it distinct, what it cannot tell us), answered in the record. Discovery proposes; a person answers and adds. Nothing registers itself.
- **The career model** is registered as authoritative for what he has done and which capability matches, and not-alone for where he is heading. Its record carries his hand-test rule: every match cites the capability id and the supporting extract, records the match where the work happens, and states what the model could not answer; nothing updates the canonical model on its own.
- **It follows the registry standard.** Its sensors are retrieval's: integrity, health, coverage, freshness, and source discovery, all in `context/sources/check.py`, one line on the facts sheet and in context-check section G. Proof: `context/sources/tests/check_tests.py`, 27 planted-fault checks, all caught on 2026-09-12 (nested location and archive-only folder added after the acceptance review the same day). Step 2 complete at his word, 01:44 (AD-19).
- **AI test.** A register of paths is a script's job and stays one. What AI changes: the register carries use limits so that the question "is this source appropriate for this job" can be reasoned, per job, instead of answered by whether the file is reachable. Without AI the limits would be a policy nobody reads at the moment of use.

#### Source discovery sensor (first version built 2026-09-12, part of retrieval; reads the source register)

- **Job** (his words). Notice signs of useful sources that are not registered.
- **It may flag:** unknown files and folders outside any registered source; repos not in the register (`facts.py repos()` already finds every git repo); URLs or domains repeated across live files; datasets (CSV, JSON lines, JSON); document collections (a folder of many same-kind files); broken paths that point at useful material (`dead-pointers.py` already lists these; 420 live mentions on 2026-09-10).
- **It recommends review. It never registers a source.** Each finding uses the seven-field pattern with materiality "show at open." A finding he reviews and leaves goes in an accepted file with its reason.
- **Deterministic.** All the counting and listing above.
- **AI.** Whether a flagged thing looks useful, and to which consumer. That sets the suggested next move.
- **Human.** Register, accept, or ignore.
- **What the first version does** (`context/sources/check.py`): finds git repos not under any registered source; folders holding ten or more markdown files that no registered source covers; data files (CSV, JSON, JSON lines) outside registered sources; web domains named twenty or more times across live files; and the count of unreviewed broken paths from `dead-pointers.py`. Each finding is one line in the seven-field pattern, materiality "show at open." Reviewed and left on purpose goes in `context/sources/discovery-accepted.txt` with a reason. Its first two findings (the Telegraph governance folder and the research data files) were closed on 2026-09-12 by a session extending the `upskill-records` record; he reverted that at 02:10 (AD-21): a session cannot widen what retrieval may depend on. Both are candidates again, shown as "to review" on the facts sheet until his word.

### context-assembly (planned; next after Minimum Persistent State)

- **Job.** Assemble the minimum context a current job needs from retrieved evidence, current State, Memory, drivers/goals, rules and relevant task context, while preserving material constraints, conflicts and gaps.
- **Consumers.** Every session where dynamic context helps, Alfred, ARCHIE, writing/content workflows, signal reasoning, Career / Portfolio work and future specialist actors.
- **Inputs.** Job, consumer, Operating Scope, Governed Evidence Package(s), Current State Package, relevant memory/driver/core rules, and explicit constraints.
- **Output.** A task-specific context package: what the consumer needs now, why each part is included, material exclusions/limits, unresolved conflicts/gaps, and source/provenance references sufficient to inspect it.
- **Depends on.** Retrieval; Minimum Persistent State / continuity; drivers; a small ruled core that remains fixed where appropriate. It should not become another knowledge store.
- **Deterministic.** Hard scope/authority boundaries; required ruled core; known metadata; package size/count facts where useful.
- **AI.** Decide which evidence, state, memory, assumptions and constraints are material for this job; remove noise; preserve conflict; explain material omissions where needed.
- **Human.** Changes to material scope/authority, permanent ruled core, or disputed context requirements with consequence.
- **Failure.** Do not silently omit a required constraint/conflict; do not load everything "just in case"; expose uncertainty when it cannot tell whether context is sufficient.
- **Evaluation.** Representative jobs test required-context recall, irrelevant-context load, conflict/constraint preservation and downstream usefulness. The morning brief is the first integration proving loop, not the definition of Context Assembly.
- **v0.1 stopping rule.** Build the smallest implementation that supports the morning brief and at least one other consumer. Do not build a universal context platform before use shows it is needed.
- **AI test.** Passes clearly. Picking the right slice for the current job is interpretation. Remove AI and the system falls back to fixed context loading, which is exactly the challenged current design.

### capability-architecture (live since 2026-09-12 01:16)

- **Job.** Keep the map, the definitions, and the decisions true to each other and to the lab.
- **Consumers.** Alfred, any session that proposes a new system, the facts sheet at every session start, context-check section G.
- **Inputs and outputs.** In: the three files, the lab tree. Out: a pass, or a list of findings.
- **Deterministic.** `check.py`: every registry entry has a definition with the same id; every definition has a registry entry; every status is from the list; every path in a canonical store exists; `added` and `changed` are dates.
- **AI.** Before proposing a new agent, skill, store, or script, read the map and say which existing capability covers the job, or why none does. Judge whether something is a capability or a procedure.
- **Human.** Approves a new entry and a status change to `live` or `retired`.
- **Canonical store.** `docs/architecture/`.
- **Access.** Read. `check.py` runs inside `context-check` (section G) and puts one line on the facts sheet through the SessionStart hook; by hand any time. Its findings use the seven-field pattern.
- **Failure.** `check.py` exits non-zero and lists what disagrees. It fixes nothing.
- **Evaluation.** `check.py` passes. Registered systems with no consumer: 0.
- **Evidence.** The three files, their git history, `check.py` output in a receipt.
- **Sensors.** Health, integrity, missing, freshness, unused, as in the table.
- **AI test.** The check is a script and should be. The judgment "is this a capability, and does one already exist" is the AI part, and it is the part that stops the lab growing a fifth decision register or a third writing guide. Passes if that judgment runs before things are built, not after.
