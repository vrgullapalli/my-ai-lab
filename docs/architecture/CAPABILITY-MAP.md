---
name: capability-map
what: The map of the lab's shared system capabilities, the registry that records them, and the registry standard every registry in the lab should follow.
status: living. Started 2026-09-12 at Venkat's word ("Establish the shared capability layer"). The registry block is the canonical record; a script reads it.
home: docs/architecture/ (his word, 2026-09-12 01:16; AD-14)
reads_this: docs/architecture/check.py (proves every entry has a definition, a valid status, and paths that exist; runs in context-check section G and on the facts sheet at every session start)
related: [CAPABILITY-DEFINITIONS.md, ARCHITECTURE-DECISIONS.md, context/intent/STANDING.md, docs/reports/2026-09-11--ai-native-possibility-brief.md]
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
| Memory and state | One live capability, one planned | Follow-ups, the to-do list, and the next-action line carry state between sessions. The seedbank and the career model are memory too, but they are sources, owned by brand-os. Retrieval will read them | `continuity` (live), `retrieval` (planned) |
| Execution | Family, plus one shared runner | Skills and agents are procedures. Claude Code runs them. The one thing the lab itself runs unattended is the set of cloud routines | `scheduled-routines` |
| Coordination | Family only | Alfred is the interface, and agents are not registered. Coordination happens through files: the open and close routines, receipts, follow-ups. Those are already `continuity` and `evidence-record` | none |
| Evaluation and observability | One capability | `facts.py`, `waiting.py`, `context-check`, `skill-check`, `dead-pointers`, `verify.sh`, `check_hub.py`. "Scripts decide what is true" is the lab's best idea and it is enforced | `measurement` |
| Capability architecture | One capability, the meta one | This map, the definitions, the decisions, and the check script that proves they agree | `capability-architecture` |

**Nine entries. Seven live or degraded, two planned.** Small on purpose. A tenth, `source-layer`, was added and removed the same day: it is retrieval's own list of sources, a store with one consumer (AD-12).

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
- canonical-store: .claude/agents/alfred/TODAY.md; .claude/agents/alfred/state
- reads: follow-up lines and the next-action line inside evidence/receipts, which evidence-record owns
- access: facts.py open and loops; alfred-open and alfred-close
- consumers: Alfred, alfred-open, alfred-close, every first session of the day
- sensors: .claude/agents/alfred/sensors/facts.py (open follow-ups, next action, unreceipted sessions); .claude/agents/alfred/sensors/waiting.py (three trackers as one view)
- defined-in: CAPABILITY-DEFINITIONS.md#continuity
- proof: .claude/agents/alfred/sensors/tests/facts_tests.py (follow-up open and close cases); live before the gate of 2026-09-12, not re-proven
- related: evidence-record, drivers
- fault: "waiting on Venkat" lives in three trackers (receipts, TODAY.md, work-os/upskill-advisor/records/open-items.md). One fact, three homes. Observed 2026-09-11.
- added: 2026-09-12
- changed: 2026-09-12

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
- status: planned
- job: Find the best relevant knowledge the system already has across registered sources and return it with enough source, freshness, authority, and evidence information to use safely.
- canonical-store: context/sources/REGISTER.md (its list of what it may depend on, with standing and use limits; sources stay canonical where they live; any index is derived and rebuildable)
- access: not decided for retrieval itself (build step 3). For the register: python3 context/sources/check.py resolve <id> is the one path from a source id to its current location, status, standing, and use limits
- consumers: Alfred, ARCHIE, signal reasoning, career model, project work, Telegraph+, context-assembly, seed-capture repeat check
- sensors: context/sources/check.py (register integrity, source health, coverage, freshness, source discovery; built 2026-09-12); planned: quality (a fixed question set), unused consumers, pointer resolution
- proof: context/sources/tests/check_tests.py (24 planted faults caught 2026-09-12: missing, moved, duplicate id, competing location, broken location, bad words, unregistered folder and repo). Retrieval itself is still planned; this proves its store
- defined-in: CAPABILITY-DEFINITIONS.md#retrieval
- related: context-assembly, evidence-record, drivers
- proving-case: market signals first (hand test 2026-09-12), then Alfred, ARCHIE, and career-model questions (build step 4)
- added: 2026-09-12
- changed: 2026-09-12

### context-assembly
- id: context-assembly
- family: Context
- status: planned
- job: Put together the right slice of what the lab knows for the task in front of it, instead of loading the same fixed files every time.
- canonical-store: none of its own; reads drivers, retrieval, and the ruled core files
- access: not decided (build step 5)
- consumers: every session, Alfred, ARCHIE, the writing skills
- sensors: not decided; at least: which files were loaded and whether they were used
- defined-in: CAPABILITY-DEFINITIONS.md#context-assembly
- related: retrieval, drivers
- added: 2026-09-12
- changed: 2026-09-12

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
