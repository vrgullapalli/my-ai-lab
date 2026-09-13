---
name: capability-map
what: The map of the lab's shared system capabilities, the registry that records them, and the registry standard every registry in the lab should follow.
status: living. Started 2026-09-12 at Venkat's word ("Establish the shared capability layer"). Retrieval is building and under v0.1 close-out evaluation; context assembly is planned; State v0.1 (Minimum Persistent State) is implemented (2026-09-13, AD-37) as the implementation slice of the existing continuity / Memory and state capability. The registry block is the canonical record; a script reads it.
home: docs/architecture/ (his word, 2026-09-12 01:16; AD-14)
reads_this: docs/architecture/check.py (proves every entry has a definition, a valid status, and paths that exist; runs in context-check section G and on the facts sheet at every session start)
related: [CAPABILITY-DEFINITIONS.md, ARCHITECTURE-DECISIONS.md, LAB-OPERATING-MODEL.md, context/intent/STANDING.md, docs/reports/2026-09-11--ai-native-possibility-brief.md]
tags: his-word (Venkat said it, dated) · observed (seen on disk or measured today) · proposed (Alfred's design, waiting on his yes)
---

# Capability map

**What this is.** The short list of systems more than one part of the lab depends on. Not skills, not agents, not scripts, not routines. Those are procedures. A shared capability is a job the whole lab leans on, with one canonical store, one way to reach it, and sensors that say whether it is healthy.

**The core rule** (his word, 2026-09-12). For every capability, registry, sensor, or workflow, ask: *what should this become now that AI exists?* Then test: *if AI were removed, would the process or outcome stay mostly the same?* If yes, challenge the design. The current lab is evidence, not the default design.

**The word "capability" has three other meanings here** (observed). The career model holds 92 capabilities about Venkat (`work-os/brand-os/model/capabilities.json`, ids `CAP-001` to `CAP-092`). The Six Capability Pillars are a brand lens. Telegraph's `capabilities.md` lists code functions. This map is about the lab as a system. Its ids are plain words, so they can never be confused with those.

## 1. The eight families, inspected

Eight families were named for inspection (his word, 2026-09-12). A family is a lens. A capability is a thing with a job, consumers, a store, and sensors. Here is which is which.

| Family | Verdict | Why (observed) | Registered here |
|---|---|---|---|
| Context | Family. Holds one live record and one planned capability | The front door loads the same fixed files every session. Nothing picks context for the task at hand. Remove AI and the loading is identical, so the design is challenged (AD-01) | `drivers` (live), `context-assembly` (planned) |
| Authority and control | One capability | Three safety minimums, `AUTHORITY.md`, two hooks that refuse. Deterministic on purpose: guardrails are allowed to be scripts | `authority` |
| Evidence | One capability | Transcripts with stable anchors, receipts that are never edited, audits, an append-only log. Every other system cites into it | `evidence-record` |
| Memory and state | One degraded/live continuity capability being strengthened, plus Retrieval building | Continuity carries current work across sessions but still reconstructs too much state. Minimum Persistent State is the next implementation slice inside `continuity`, not a new registry entry. Retrieval is a shared governed evidence-access capability and remains building until v0.1 close-out. | `continuity` (degraded), `retrieval` (building) |
| Execution | Family, plus one shared runner | Skills and agents are procedures. Claude Code runs them. The one thing the lab itself runs unattended is the set of cloud routines | `scheduled-routines` |
| Coordination | Family only | Alfred is the interface, and agents are not registered. Coordination happens through files: the open and close routines, receipts, follow-ups. Those are already `continuity` and `evidence-record` | none |
| Evaluation and observability | One capability | `facts.py`, `waiting.py`, `context-check`, `skill-check`, `dead-pointers`, `verify.sh`, `check_hub.py`. "Scripts decide what is true" is the lab's best idea and it is enforced | `measurement` |
| Capability architecture | One capability, the meta one | This map, the definitions, the decisions, and the check script that proves they agree | `capability-architecture` |

**Nine entries. Seven live or degraded, one building, one planned.** Small on purpose. Minimum Persistent State is an implementation slice of `continuity`, not a tenth capability. `source-layer` was added and removed the same day: it is Retrieval's own source register, a store with one consumer (AD-12).

## 1A. Cross-cutting boundaries and operating model

The registry answers **what shared capabilities exist**. It does not register every actor, scope, connector or workflow.

- **Observed + intended jobs.** Architecture uses both the jobs Venkat actually asks the lab to do and the jobs the lab is deliberately being built toward. Observed jobs diagnose current friction; intended jobs keep the system from merely automating today's workflow.
- **Operating Scope.** Initial scopes are AI Lab, Professional / Advisory, Career / Portfolio, Public / Content, and Personal. Scope is a cross-cutting boundary, not a capability entry. Technical access does not equal permission to use.
- **Actors.** Venkat, Alfred, ARCHIE, future specialist agents and automations consume or exercise shared capabilities. An actor is not a capability.
- **Connections.** Email, calendar, Drive, Dropbox, web, APIs, CRM and future applications are sources and/or action surfaces. A connection is not a capability stack.
- **Minimum Persistent State.** The next implementation slice strengthens `continuity` / Memory and state so current decisions, active work, ownership, open/waiting items, supersession and carry-forward stop being reconstructed from raw evidence each session.
- **First integration proving loop.** Morning Brief + One Prepared Next Action is the first place Retrieval, State, Context, Evidence, Authority and Coordination should work together. It is a proving loop, not a capability.
- **Default build pattern.** Operational Spec → one `/goal` → one review. Tests evaluate implementation and assumptions; required foundational capabilities do not repeatedly audition for existence.

## 2. The registry (canonical record)

**How to read it.** One record per capability. Each is a heading plus `- key: value` lines, the same shape a seed file uses. `check.py` parses exactly this block, between the two `registry` markers. Paths are relative to the lab root.

**Status words** (his word, 2026-09-12 01:16): `planned` (defined, not built) · `building` (work in progress) · `live` (running, sensors green) · `degraded` (running, a known fault the sensors show) · `retired` (kept as a record, no longer used; a dated line says what replaced it).

<!-- registry:start -->

### authority
- id: authority
- family: Authority and control
- status: live
- job: Say what may not happen without Venkat, and refuse it by script where a script can.
- canonical-store: CLAUDE.md; .claude/agents/alfred/AUTHORITY.md; .claude/hooks/root-lock.py; .claude/skills/unlazy
- access: loaded every session by the front door; hooks fire on their own
- consumers: every session, every skill, every agent, every hook
- sensors: .claude/hooks/tests (root lock); .claude/skills/context-check/context-check.sh (secrets, uncommitted)
- defined-in: CAPABILITY-DEFINITIONS.md#authority
- proof: .claude/hooks/tests/root-lock-tests.py (37 of 37 on 2026-09-12); live before the gate of 2026-09-12, not re-proven
- related: measurement, evidence-record
- added: 2026-09-12
- changed: 2026-09-12

### evidence-record
- id: evidence-record
- family: Evidence
- status: live
- job: Keep a record that cannot be quietly rewritten: what happened, who said what, and what ran, each with a stable pointer.
- canonical-store: evidence/sessions; evidence/receipts; evidence/audits; .claude/agents/alfred/LOG.md
- access: read by path and anchor; written only as new files or appended lines
- consumers: alfred-close, alfred-open, seed-capture, facts.py, claim-verification, retrieval (planned)
- sensors: .claude/agents/alfred/sensors/facts.py (unreceipted sessions, capture age, log gap); .claude/agents/alfred/sensors/session-sync.py (render log)
- defined-in: CAPABILITY-DEFINITIONS.md#evidence-record
- proof: .claude/agents/alfred/sensors/tests/facts_tests.py (unreceipted-session case); live before the gate of 2026-09-12, not re-proven
- related: continuity, measurement
- added: 2026-09-12
- changed: 2026-09-12

### continuity
- id: continuity
- family: Memory and state
- status: degraded
- job: Carry where we are, what is open, and what comes next across sessions, so nothing depends on Venkat remembering.
- canonical-store: .claude/agents/alfred/TODAY.md; .claude/agents/alfred/state; context/state/STATE.jsonl (State v0.1, the append-only ledger of overlays no registry holds: supersession links, ownership, commitments, materiality; context/state/CURRENT.md beside it is a generated view)
- reads: follow-up lines and the next-action line inside evidence/receipts, which evidence-record owns
- access: facts.py open and loops; alfred-open and alfred-close
- consumers: Alfred, alfred-open, alfred-close, every first session of the day
- sensors: .claude/agents/alfred/sensors/facts.py (open follow-ups, next action, unreceipted sessions); .claude/agents/alfred/sensors/waiting.py (three trackers as one view); context/state/state.py (check: refusals, conflicts, stale; one line on the facts sheet)
- defined-in: CAPABILITY-DEFINITIONS.md#continuity
- proof: .claude/agents/alfred/sensors/tests/facts_tests.py (follow-up open and close cases); live before the gate of 2026-09-12, not re-proven. State v0.1: context/state/tests/check_tests.py (21 checks, planted faults and writer refusals, all caught 2026-09-13) and context/state/tests/run_tests.py (S1 to S5, 5 of 5 on 2026-09-13)
- related: evidence-record, drivers
- fault: "waiting on Venkat" lives in three trackers (receipts, TODAY.md, work-os/upskill-advisor/records/open-items.md). One fact, three homes. Observed 2026-09-11.
- build-steps: State v0.1 designed and approved 2026-09-13 (AD-37; docs/reports/2026-09-13--state-v0-1-design.md; the spec is in the definition) and implemented the same day: ledger seeded from the registries (310 derived lines), the five frozen tests in context/state/tests/STATE-TESTS.md pass, 21 planted-fault and refusal checks caught, the open and close skills read and write it, one line on the facts sheet. Ready for its first consumer, the morning brief (AD-30). The three-homes fault stands; State reads the three as one list
- added: 2026-09-12
- changed: 2026-09-13

### drivers
- id: drivers
- family: Context
- status: live
- job: Hold what Venkat is working toward right now, so sensors and the open routine know what matters and what would threaten it.
- canonical-store: context/intent/STANDING.md
- access: read at session open and in every duty pass; append-only
- consumers: alfred-open, the alfred agent (duty pass), implication-lens, hand tests, retrieval (planned, for weighting)
- sensors: .claude/agents/alfred/sensors/facts.py (drivers changed since last open); per-driver proof lines named inside the file
- defined-in: CAPABILITY-DEFINITIONS.md#drivers
- proof: none written; live before the gate of 2026-09-12. A planted-fault proof is owed
- related: continuity, context-assembly
- added: 2026-09-12
- changed: 2026-09-12

### measurement
- id: measurement
- family: Evaluation and observability
- status: live
- job: Say what is true by script, never by a model's opinion: did it run, does it exist, did it change, has the date passed, does live match file.
- canonical-store: .claude/agents/alfred/sensors; .claude/skills/context-check; work-os/scheduled-tasks/market-signals/verify.sh; work-os/brand-os/model/check_hub.py
- access: run by hooks at session start and end, by launchd, and by hand
- consumers: alfred-open, alfred-close, the alfred agent, unlazy, Venkat (the facts sheet)
- sensors: .claude/agents/alfred/sensors/tests; .claude/hooks/tests; .claude/skills/prove-it-can-fail (the check that a check can fail)
- defined-in: CAPABILITY-DEFINITIONS.md#measurement
- proof: .claude/agents/alfred/sensors/tests/facts_tests.py and .claude/skills/context-check/tests/skill_check_tests.py; live before the gate of 2026-09-12
- related: authority, evidence-record, capability-architecture
- added: 2026-09-12
- changed: 2026-09-12

### scheduled-routines
- id: scheduled-routines
- family: Execution
- status: degraded
- job: Run work unattended in the cloud on a schedule and bring its output back into the lab.
- canonical-store: work-os/scheduled-tasks
- access: claude.ai routines by id; outputs pulled into work-os/scheduled-tasks/<task>/outputs by alfred-open
- consumers: market signals, daily briefing, matching roles scan, weekend read
- sensors: work-os/scheduled-tasks/market-signals/verify.sh (live matches file); .claude/agents/alfred/sensors/facts.py (briefs pulled today)
- defined-in: CAPABILITY-DEFINITIONS.md#scheduled-routines
- proof: work-os/scheduled-tasks/market-signals/verify.sh (all 21 matched 2026-09-09); no planted-fault proof; live before the gate of 2026-09-12
- related: retrieval
- fault: the lab records 29 routine ids; the account listed 2 on 2026-09-11 at 15:20. verify.sh cannot run. Briefs never read lab context (hand test, 2026-09-12).
- added: 2026-09-12
- changed: 2026-09-12

### retrieval
- id: retrieval
- family: Memory and state
- status: live
- job: Find the evidence already available to the system that could materially affect the current job, within applicable scope and hard source boundaries, and return a Governed Evidence Package with provenance, limits, conflicts, and material gaps intact.
- canonical-store: context/sources/REGISTER.md (governed list of what it may depend on; sources remain canonical where they live; the derived index and run records under context/sources/index are rebuildable, not canonical)
- access: python3 context/sources/retrieve.py plus the retrieval skill/model; python3 context/sources/check.py resolve <id> for stable source resolution
- consumers: Alfred, ARCHIE, signal reasoning, Career / Portfolio reasoning, project work, Telegraph+, context-assembly, content/research workflows, seed-capture repeat check
- sensors: context/sources/check.py; context/sources/tests/reachability.py; context/sources/tests/run_tests.py; context/sources/retrieve.py stats; planned miss/unused/context-impact/outcome sensing when real usage supports it
- proof: context/sources/tests/check_tests.py (27 planted faults caught 2026-09-12); boundary refusal proven (run_tests.py --prove-boundary); Retrieval v0.1 closed for downstream use 2026-09-13 at 6 of 7 frozen tests, no regression; T2 (meaning match to one seed) failed on every path tried and is a recorded limitation; live since 2026-09-13 at his word with that limitation on record (AD-36). See docs/reports/2026-09-13--retrieval-v0-1-close-out.md and the three 2026-09-12 retrieval reports
- defined-in: CAPABILITY-DEFINITIONS.md#retrieval
- related: context-assembly, continuity, evidence-record, drivers
- build-steps: source register complete; v0.1 implemented and closed for downstream use (2026-09-13); live at his word 2026-09-13 (AD-36); next, Minimum Persistent State and context assembly consume the interface
- proving-case: frozen tests span Signals, Alfred, ARCHIE and Career Model; the morning brief is the first integrated downstream loop after State begins
- added: 2026-09-12
- changed: 2026-09-13

### context-assembly
- id: context-assembly
- family: Context
- status: planned
- job: Assemble the minimum evidence, current state, memory, rules, goals and constraints the current job needs, while preserving material conflicts and gaps and excluding noise.
- canonical-store: none of its own; reads retrieval, continuity / Minimum Persistent State, drivers and the ruled core
- access: not decided; build after Minimum Persistent State is sufficient for the first proving loop
- consumers: every session where dynamic context helps, Alfred, ARCHIE, writing/content workflows, signal reasoning, Career / Portfolio work, future specialist actors
- sensors: to be defined at build; at minimum required-context recall, irrelevant-context load, material conflict/constraint preservation, and loaded-but-unused context
- defined-in: CAPABILITY-DEFINITIONS.md#context-assembly
- related: retrieval, continuity, drivers
- proving-case: Morning Brief + One Prepared Next Action first, then at least one other consumer before v0.1 closes
- added: 2026-09-12
- changed: 2026-09-13

### capability-architecture
- id: capability-architecture
- family: Capability architecture
- status: live
- job: Keep the map, the definitions, and the decisions true to each other and to the lab, so a new capability is added on purpose and an old one retires in the open.
- canonical-store: docs/architecture
- access: read by people and sessions; check.py runs in context-check section G and puts one line on the facts sheet at every session start; by hand any time
- consumers: Alfred, any session that proposes a new system, the facts sheet (every session start), context-check
- sensors: docs/architecture/check.py (registry and definitions agree; statuses valid; paths exist); .claude/skills/context-check/dead-pointers.py (paths named in live files)
- defined-in: CAPABILITY-DEFINITIONS.md#capability-architecture
- proof: docs/architecture/ARCHITECTURE-DECISIONS.md AD-13 and conflict 11; planted faults caught on the facts sheet and in context-check section G, 2026-09-12 01:10; files restored to matching checksums
- related: measurement
- added: 2026-09-12
- changed: 2026-09-12
- status-history: 2026-09-12 building to live, his word 01:16

<!-- registry:end -->

### Looked at and not registered (observed)

- **Skills (28) and agents (9).** Procedures and interfaces. They use capabilities; they are not one.
- **Seedbank (790 files), career model (92 capabilities), points of view, receipts as knowledge.** Sources. They enter retrieval's source register at build step 2.
- **Session capture (`session-sync.py`).** Part of `evidence-record`; it is how transcripts get there.
- **unlazy and the root lock.** Part of `authority`; they are the two things that refuse.
- **Publishing chain, dossier, committee, target scan.** Domain workflows inside engagement-os.
- **The source register** (build step 2, built 2026-09-12). Retrieval's list of what it may depend on: 23 sources, each with standing and use limits. One consumer, so a store, not a capability. Registered this morning as `source-layer`, removed at 01:20 (AD-12). Its definition lives under retrieval.
- **Standing reasoning and the learning loop** (build steps 6 and 7). Not defined yet, so not registered. A planned entry needs at least a job line and one consumer.

## 3. Registry standard

**Every registry in the lab follows these conventions** (his word on the list, 2026-09-12; the wording here is Alfred's). Domain fields can differ. There is no universal schema.

- **Stable id.** Set once, never renamed. Plain words or an existing prefix (`AS-`, `A-LIVE-`, `F-`, `CAP-`). A display name can change; the id cannot.
- **One canonical record.** The registry file is the record. Anything else that lists the same things is a view, says so, and is generated or points back.
- **Clear status.** One word from a short list written at the top of the file. A status change is an edit to the record, dated.
- **Relationships by stable reference.** `related:` and `consumers:` name ids or paths, never prose descriptions.
- **Source or location** where the thing lives, as a path relative to the lab root, so a script can test it.
- **Timestamps** where useful: `added`, `changed`, and for status moves, the date and who decided.
- **Live needs proof.** A live or degraded entry carries `- proof:` naming where the failure proof is (his gate, 2026-09-12 01:17; AD-15). Entries live before the gate say so.
- **Add, change, retire.** Add is a new record. Change edits the record and bumps `changed`. Retire sets `status: retired` and adds one dated line saying what replaced it. Nothing is deleted.
- **Machine-readable.** A ten-line script can parse it without a library the machine does not have. Here that means front matter, `- key: value` records, markdown tables, JSON lines, or YAML where a reader exists.
- **No duplicate source of truth.** If a second file must hold the same fact, it is generated from the first, or it is a bug.

### How the lab's existing registries measure up (observed 2026-09-12)

| Registry | Where | Meets | Misses |
|---|---|---|---|
| Asset registry | `work-os/brand-os/engagement-os/assets/registry.yaml` | stable `AS-` ids, status with `decided_by` and date, location, related ids, never delete | no `changed` timestamp; no reader exists on this machine (no YAML library) |
| Seeds | `work-os/brand-os/engagement-os/seedbank/` | `A-LIVE-` ids, status, date, source with anchor, connections by id | `INDEX.md` exists but the cultivator's first instruction names an index that does not; README count is a second copy of a number |
| Follow-ups | `- [ ] F-YYYYMMDD-HHMM-n` lines in receipts and audits | stable id, owner, first step, status by checkbox, read by `facts.py loops` | spread across files by design; closing needs a receipt line, so a loop closed by hand elsewhere stays open |
| Target verdicts | `work-os/brand-os/engagement-os/targets/index/verdicts.jsonl` | append-only, timestamped, slug ids, machine-readable | latest-wins rule is implied, not written in the file |
| Career model | `work-os/brand-os/model/*.json` | `CAP-` ids, maturity and status tags, sources, a hub check | no `changed` dates; 20 of 22 cited artifact paths do not resolve on this machine |
| Cloud routines | `work-os/scheduled-tasks/README.md` | routine ids, schedules, `verify.sh` | status is prose ("28 cloud routines") while the account listed 2; the fact and the record disagree |
| Rulings about Venkat | `work-os/brand-os/DECISIONS.md` | numbered, dated, quotes him, append-only | no status word; superseded rows (036 corrected by 037) are found by reading |

**The pattern the lab already gets right:** ids, dates, append-only, and "never delete." **The pattern it misses most:** a status word a script can read, and one home per fact.
