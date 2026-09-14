---
name: current-registries-checks-sensors
what: The lab's registries, checks, sensors, and health monitoring as they exist on 2026-09-14. A baseline for the Step 2.5 research and standards work. Reports, never designs.
status: observed 2026-09-14 13:20 to 13:40. Every number below came from a script run in this session or from a file read the same session. Nothing here was changed to make it true.
home: docs/documentation/ (new folder, this is its first file; the home was named in the goal)
reads_this: nothing by script. Sessions doing the Step 2.5 work read it by hand.
written_by: Alfred, at Venkat's /goal of 2026-09-14 13:23
tags: Current (runs or is read today) · Historical (superseded or frozen; kept as a record) · Proposed (named in a document, no file or no run) · Unclear (behavior or owner could not be established from the lab)
---

# Current registries, checks, and sensors

## 0. How to read this file

**What counts as a registry here.** The lab's own test, from the registry standard in `docs/architecture/CAPABILITY-MAP.md` section 3: a stable id, one canonical record, a status word a script can read, relationships by stable reference, a location a script can test, timestamps, and "add, change, retire, never delete." A file was counted as a registry only when its behavior meets most of that and something reads it. Lists, folders, and views are named as what they are.

**Two labels per item.** The first says whether it is Current, Historical, Proposed, or Unclear. The second, in section 4, marks eight kinds of sensing as Present, Partial, Missing, or Not applicable.

**Eight kinds of sensing, as used below.**
- Integrity: do its ids, words, and pointers hold up.
- Health: is it there, readable, and did its job run.
- Discovery: does anything notice what should be in it and is not.
- Freshness: how old is it, and does anything say so.
- Usage: does anything measure who reads it.
- Coverage: does anything count what it holds against what exists.
- Drift: does anything compare a live copy, a generated copy, or an approved state with the record.
- Efficiency: does anything measure cost, size, or time.

**"Step 2.5" is not in the lab.** No file under `docs/`, `context/`, or `.claude/` names it. The nearest anchors are Prompt 3 (named, not begun) in `docs/ecosystem/2026-09-14--ai-lab-portfolio-architecture.md` section 10, and the "Registries" list in `docs/ecosystem/2026-09-13--ai-lab-product-ecosystem-roadmap.md`. This file does not guess what Step 2.5 is.

## 1. The standards that exist today (Current)

| Standard | Where it lives | What it says, in short | Enforced by |
|---|---|---|---|
| Registry standard | `docs/architecture/CAPABILITY-MAP.md` section 3 (AD-03) | Stable id, one canonical record, one status word from a short list, relationships by id or path, a testable location, `added` and `changed` dates, `proof` on anything live, add/change/retire, machine-readable, no second source of truth | `docs/architecture/check.py` for the capability registry; `context/sources/check.py` for the source register; `context/state/state.py` for State. Nothing enforces it on the domain registries in section 2B and 2C |
| Five status words | `docs/architecture/ARCHITECTURE-DECISIONS.md` AD-05 | planned, building, live, degraded, retired | the three checks above reject any other word |
| Building-to-live gate | AD-15; `CAPABILITY-DEFINITIONS.md` "The building-to-live gate" | live needs operational behavior, failure proof, and a valid contract; the entry carries `- proof:` | `docs/architecture/check.py` check 10 |
| Sensor standard | `docs/architecture/CAPABILITY-DEFINITIONS.md` "Sensor standard" (AD-11) | seven conditions to watch (health, integrity, drift, missing, freshness, unused, quality); a finding has seven fields; three materiality levels (interrupt him, show at open, record only); a sensor reports and never fixes; a check is proven able to fail; an accepted finding lives in a file beside the sensor with a reason | adopted by `docs/architecture/check.py`, `context/sources/check.py`, `context/state/state.py`. The file says "Old sensors are not rewritten; they adopt it when touched" |
| Accepted-findings pattern | `.claude/skills/context-check/dead-pointers-accepted.txt`, `skill-check-accepted.txt`, `context/sources/discovery-accepted.txt` | one line per reviewed finding with a reason; counted, not listed | each sensor reads its own file |
| Prove it can fail | `.claude/skills/prove-it-can-fail/SKILL.md`, modeled on `work-os/upskill-advisor/telegraph/evals/prove_checks.py` | break the thing on a throwaway copy and require the check to fail | by hand, per skill |
| Scripts decide what is true | `CLAUDE.md` "AI-native, and where deterministic rules belong" | every number about the lab comes from a script, never from a model | `facts.py` is the one place the numbers are gathered |

## 2. Registries and registry-like canonical structures

### 2A. Lab-wide, read by a script every session

**Capability registry** (Current)
- Purpose: the short list of shared systems the lab leans on; the record the design check points at before any new system is built (`CLAUDE.md` "Before you write").
- Canonical source: the block between the two `registry` comment markers in `docs/architecture/CAPABILITY-MAP.md`. Definitions in `CAPABILITY-DEFINITIONS.md`, rulings in `ARCHITECTURE-DECISIONS.md`.
- Identity: plain-word ids, never renamed (AD-04). Nine today: authority, evidence-record, continuity, drivers, measurement, scheduled-routines, retrieval, context-assembly, capability-architecture.
- Lifecycle: the five status words; `status-history` lines on moves; `added` and `changed` dates; `- proof:` required on live or degraded.
- Consumers: `docs/architecture/check.py`; the design check note from `.claude/hooks/unlazy-trigger.py`; `context/state/state.py` (reads registry status to compare against State lines); sessions by hand.
- Authority: Venkat's word on status moves (AD-14). The map's own header: "The registry block is the canonical record; a script reads it."
- Sensor: `docs/architecture/check.py`, ten checks (parse, required fields, status words, unique ids and heading equals id, every id has a definition and the reverse, `canonical-store` and `sensors` paths exist, dates, `related` ids resolve, no two entries claim one store, no second registry block anywhere in live markdown, proof on live). Runs at every session start through `facts.py` and in `context-check` section G. Output today: `OK architecture check: 9 registry entries, 9 definitions; 0 finding(s)`. Exit 1 on any finding; the facts line gets an `ALERT` prefix.
- Proof: no test file beside the script. The map's `proof` line cites planted faults caught by hand on 2026-09-12 01:10 (AD-13). Seen working today: the first draft of this file quoted the marker text and check 9 flagged it as a second registry block; the wording was changed and the check went back to 0.
- Gap: the map's own table "How the lab's existing registries measure up" is a dated observation from 2026-09-12, not a sensor. Nothing re-measures it.

**Source register** (Current)
- Purpose: what Retrieval may depend on, where each source is now, its standing, its authority tier, and its use limits (AD-16 to AD-21).
- Canonical source: the block between the two `register` comment markers in `context/sources/REGISTER.md`.
- Identity: 24 ids, plain words (seeds, receipts, audits, transcripts, alfred-log, drivers, rulings, root-doctrine, about-me, career-model, voice-canon, positioning, targets, assets, routine-outputs, lab-reports, telegraph-plus, upskill-records, editorial-work, concepts, architecture, public-site, career-advisor, warehouse). One id per source whatever copies exist; a replica names `canonical-at` and never gets its own id.
- Lifecycle: the five status words (only live and degraded may be read); `standing` (canonical, replica, historical, unavailable); `tier`; `use` ceiling; `may-inform`; `not-alone`; `added` and `changed`.
- Consumers: `context/sources/check.py resolve <id>` (the one path from id to location); `context/sources/retrieve.py` (builds the index from it); `context/state/state.py` (reads status words); `context-check` section G; `facts.py` one line.
- Authority: "adding a source or widening a location is his word, recorded in a decision row, never a session's fix for a finding" (AD-21). The `discovery-accepted.txt` file marks lines "Alfred" that still await his review.
- Sensor: `context/sources/check.py`. Integrity (ids unique and equal to headings, required fields, allowed words, replica has `canonical-at`, dates, no two sources on one location, no location nested inside another's). Health (missing, with a hint where a folder of that name is now; unreadable; empty; an unavailable source that is reachable). Coverage and freshness (files per source, newest change). Discovery (AD-08: git repos under no source, folders with ten or more markdown files under no source, data files outside sources, web domains named twenty or more times, unreviewed dead pointers). Runs every session start through `facts.py` and in `context-check` section G. Exit 1 on register or health findings; discovery findings are "show at open" or "record only" and never fail the run. Output today: `OK sources: 24 registered (24 live, 3 outside the lab), 1532 files covered, newest change 0 day(s) ago; discovery: 3 to review, 1 recorded; register findings: 0`. The three open discovery findings: `work-os/upskill-advisor/governance` (14 markdown files), `docs/ecosystem` (10), and 7 data files under `work-os/upskill-advisor/research`.
- Proof: `context/sources/tests/check_tests.py`, 27 planted faults; passed today ("all passed").
- Gap: `read-by` is a declared field, not a measured one. Five sources say "nothing reads them by script yet" (rulings, lab-reports, editorial-work, public-site, warehouse). Usage is not sensed.

**State ledger** (Current; a registry-like overlay, not a registry of durable objects, by its own definition)
- Purpose: "say what is currently true, active, changed, open, waiting, owned, or superseded, with a pointer to the evidence, without reading history" (`context/state/state.py` docstring). "State is an index over the registries, not a second store of facts."
- Canonical source: `context/state/STATE.jsonl`, one JSON object per line, append-only, latest line per id wins. `context/state/CURRENT.md` is a generated view and says so on its first lines.
- Identity: ids prefixed by kind, `decision:`, `work:`, `loop:`, `commitment:`, `status:`. 379 current lines today (185 decisions, 22 work, 123 loops, 14 commitments, 35 statuses).
- Lifecycle: status words per kind (decision current/superseded/proposed; work active/paused/done/handed-off; loop open/closed/waiting; commitment open/kept/missed); `established` and `changed` dates; `authority` (his-word, proposed, system, derived); `his-word` needs an anchor and is never written by the seed.
- Consumers: `alfred-open` (reads the package), `alfred-close` (writes from the receipt), `facts.py` (one line), the morning brief wiring in progress (AD-30, `.claude/agents/alfred/TODAY.md` "Start here").
- Authority: approved as designed, AD-37; Venkat's words "Use `context/state/`."
- Sensor: `python3 context/state/state.py check`. Refuses lines that are not JSON, miss a required field, use an unknown kind or status word, have an id that does not start with its kind, an unknown scope or authority, a source that does not resolve to a registry id or an evidence anchor, a `his-word` line with no anchor or written by the seed, or a bad date. Conflicts: an active work line that overwrites another owner's active claim; two current successors for one superseded decision; a status line that disagrees with its registry (the registry wins). Stale: work older than 7 days, commitments older than 3, loops older than 14, and a status line older than its registry's `changed`. Runs every session start through `facts.py`. Exit 1 on findings; stale is "record only". Output today: `state: 379 current lines ... conflicts 0; stale 0; findings 0`.
- Proof: `context/state/tests/check_tests.py` (21 planted faults and writer refusals; passed today) and `context/state/tests/run_tests.py` (the five frozen tests in `STATE-TESTS.md`).
- Gap: the registered fault stands. "Waiting on Venkat" lives in three homes (receipts, `TODAY.md`, `work-os/upskill-advisor/records/open-items.md`); State and `waiting.py` read the three as one view (`CAPABILITY-MAP.md`, continuity entry, `fault`).

**Follow-ups** (Current; registry-like by behavior, spread across files by design)
- Purpose: the open loops the open routine brings back.
- Canonical source: every `- [ ] F-YYYYMMDD-HHMM-n` line in `evidence/receipts/*.md` and `evidence/audits/*/*.md`. Closed by `- [x] F-...` anywhere, or a line under `## Closed` that starts with the id (a mention in prose does not close it; test 10 in `facts_tests.py`).
- Identity: `F-` ids, stable. 110 open today; the oldest three are four days old.
- Lifecycle: open or closed by checkbox; `owner:` and `first step:` inside the line.
- Consumers: `facts.py loops` and the open sheet; `waiting.py` (owner Venkat); `state.py from-receipt` (opens and closes loop lines).
- Authority: closing a loop is "Prepares, Venkat approves" (`.claude/agents/alfred/AUTHORITY.md`).
- Sensor: count and age on the facts sheet; State's 14-day stale rule on loop lines.
- Gap, from the map's own table: "closing needs a receipt line, so a loop closed by hand elsewhere stays open." No check for a duplicate id across two receipts.

**Current drivers** (Current; one canonical record, not a registry: four sections, no ids)
- Canonical source: `context/intent/STANDING.md`, append-only, four drivers, cap of four (his word, 2026-09-08).
- Consumers: `alfred-open`, the `alfred` agent duty pass, `implication-lens`, `facts.py`.
- Authority: adding, replacing, or retiring a driver is Venkat's call (`AUTHORITY.md`).
- Sensor: `facts.py` adds "current drivers changed since the last open routine" when the file's change time is newer than the last `OPEN` line in `.claude/agents/alfred/LOG.md` (test 11 in `facts_tests.py`, written 2026-09-14). Each driver names "What a script can prove"; those proofs are lines already on the facts sheet.
- Gap: no script checks the file's content or structure. Driver 2's "next meaningful change" (a scheduled restore-and-diff) is a plan, not a sensor (`docs/plans/2026-09-14--restore-and-diff-sensor--plan.md`).

### 2B. Domain registries, some with a script

**Asset registry** (Current)
- Canonical source: `work-os/brand-os/engagement-os/assets/registry.yaml`. Header: "canonical, PRIVATE ... Append new assets; status moves edit the entry and carry decided_by + date. Never delete an entry."
- Identity: `AS-001` to `AS-006`, six entries.
- Lifecycle: private, candidate, approved, published, withheld, retired (`work-os/brand-os/engagement-os/assets/README.md`); each move carries `decided_by` and a date. No `changed` timestamp.
- Consumers: `asset-corpus-match`, the publishing skills, `public-value-advisor` (source register); `work-os/brand-os/engagement-os/tools/build_as006_instrument.py`; `work-os/brand-os/engagement-os/tests/test_as006_oracle.py`, `test_public_value_system.py`.
- Authority: Venkat rules every status move past candidate (`work-os/brand-os/engagement-os/assets/README.md`).
- Sensors: none read the registry itself. The map noted on 2026-09-12: "no reader exists on this machine (no YAML library)". Two release-time checks exist and run by hand, fail closed: `work-os/brand-os/engagement-os/tools/check_public_safety.py` (private paths and tokens from `work-os/brand-os/engagement-os/tools/private-paths.txt` and `work-os/brand-os/engagement-os/tools/private-tokens.txt`, emails, LinkedIn URLs, home paths, rate figures; exit 0 clean, 1 violations, 2 guard failure) and `work-os/brand-os/engagement-os/tools/validate_public_value.py` (fixed vocabularies for opportunity, brief, experience, release records). Both have unit tests in `work-os/brand-os/engagement-os/tests/` that plant a leak and require rejection. No hook or job runs them.
- Gap: `docs/ecosystem/2026-09-14--ai-lab-portfolio-architecture.md` section 6: "Two entries disagree with themselves (archived, prose says candidate). No capability link." Nothing senses that.

**Seedbank** (Current)
- Canonical source: the files under `work-os/brand-os/engagement-os/seedbank/session/`, `written/`, `spoken/`. 828 files today.
- Identity: `A-LIVE-`, `A-TOPIC-`, `A-SEED-`, `A-CHR-`, `A-ADR-`, `A-CDR-` prefixes (`work-os/brand-os/engagement-os/seedbank/README.md`). `.claude/skills/seed-capture/scripts/next-id.py` issues the next id.
- Lifecycle: `INDEX.md` names new, linked, used, gone quiet, unlinked, retired. The index was hand-built by the cultivator on 2026-09-09 and last changed 2026-09-10; it says of itself "I cannot read file change times with the tools I have."
- Consumers: `seed-capture` (`find-similar.py` for the repeat check), `cultivator`, ARCHIE, Retrieval (source id `seeds`).
- Sensors: `facts.py` (file count, age of the newest session seed, rows in `missed.md`); Retrieval's index build lists five seedbank files left out for having no id line (`context/sources/index/stats.json`, `left_out_no_id_line`).
- Gap: no script checks id uniqueness, that `INDEX.md` matches the files, or that the README count matches. The map: "README count is a second copy of a number."

**Target index** (Current, quiet since 2026-09-04)
- Canonical source: `work-os/brand-os/engagement-os/targets/index/companies.json` (one record per company, keyed by slug, with `stage`, `tier`, `tier_history`, `do_not_surface`) and `work-os/brand-os/engagement-os/targets/index/verdicts.jsonl` (append-only, one line per scoring event, `company_slug` plus `snapshot_date`, verdict engage/watch/refused, `criteria_version` naming `work-os/brand-os/engagement-os/targets/criteria/criteria-v1.yaml`). `work-os/brand-os/engagement-os/targets/collectors.json` is a hand-probed list of applicant tracking systems.
- Consumers: `dossier`, `committee`, `target-scan` skills; Retrieval (source id `targets`).
- Authority: Venkat on tier and verdict moves (`work-os/brand-os/engagement-os/targets/README.md`).
- Sensors: none. The map: "latest-wins rule is implied, not written in the file."
- Unclear: `work-os/brand-os/engagement-os/targets/README.md` names the writer as "scan/scorer"; no such script was found under `work-os/brand-os/engagement-os/tools/`.

**Career model hub** (Current)
- Canonical source: `work-os/brand-os/model/*.json` (`capabilities.json`, `techniques.json`, `tools.json`, `skills.json`, `domains.json`, `subdomains.json`, `products.json`, `expertise-graph.json`), each with a `$schema_note` naming itself canonical. The three `*-catalog.md` files are generated views. `work-os/brand-os/model/decision-log.md` holds the `CE-D` rulings. `work-os/brand-os/model/SPOKES.md` is a registry of consumers with `Wired` and `Last returned` columns.
- Identity: `CAP-001` to `CAP-092`, `TEC-`, `TOL-`, `CE-D` ids. Frozen 2026-08-31; changes only by Venkat's separate ruling (AD-31).
- Consumers: `build_who_i_am.py`, ARCHIE's `work-os/brand-os/engagement-os/agents/archie/config/data-sources.yaml`, the dossier and committee skills, `my-voice`, `work-os/brand-os/audience/weekly/taxonomy_demand.py` and `annotate.py`. `SPOKES.md` shows "Last returned: never" for four of seven spokes.
- Sensors: `work-os/brand-os/model/check_hub.py` (every spoke path exists and names the hub; no never-cite number from `17-semantic-usage-guide.md` in live text; exit 1 on either). `work-os/brand-os/model/build_who_i_am.py --check` (the generated "who I am" file still matches the model; exit 1 on drift). Both read by `facts.py` into one line since 2026-09-14 (test 12 in `facts_tests.py`). Output today: `career model check: spokes broken 1, never-cite hits 30, generated file matches the model`. The broken spoke is the weekly market instrument, whose `taxonomy_demand.py` does not name the hub. The 30 hits sit mostly in `docs/about-me/who-i-am--generated.md` (6), the frozen career-advisor reasoning drop (9), `work-os/brand-os/terminology/README.md` (4), and one research report (3).
- Gap: the facts line carries no `ALERT` prefix at any count, so 30 hits and one broken spoke are "show at open" with no owner named. The map's 2026-09-12 note: "20 of 22 cited artifact paths do not resolve on this machine." No `changed` dates on entries.

**Cloud routines** (Current; registered as degraded)
- Canonical source: `work-os/scheduled-tasks/README.md` (a table of the seven original routines, `trig_` ids, schedules, an append-only log), one `ROUTINE.md` per task folder, and `work-os/scheduled-tasks/market-signals/routines.tsv` for the 21 signal routines (folder, cadence, name, cron, model, uuid, trigger id). `verify.sh` carries its own name-to-folder map, a second copy of part of `routines.tsv`.
- Identity: routine ids `trig_...`. The README says 28 routines; the capability map's `fault` line says "the lab records 29 routine ids; the account listed 2 on 2026-09-11 at 15:20."
- Lifecycle: prose, no status word. The map: "status is prose ('28 cloud routines') while the account listed 2; the fact and the record disagree."
- Consumers: `alfred-open` pulls briefs into `<task>/outputs/`; Retrieval (source id `routine-outputs`, a replica).
- Sensors: `work-os/scheduled-tasks/market-signals/verify.sh` compares the live prompt of each of the 21 routines (from saved RemoteTrigger responses) with `work-os/scheduled-tasks/market-signals/<pillar>/<cadence>/build/full-prompt.md` by MD5; prints OK, DIFF, or NO MAP per routine; sets no exit code; needs a folder of saved responses, so it cannot run unattended. Last recorded full pass: 2026-09-09, all 21 OK (`work-os/scheduled-tasks/market-signals/README.md`). `facts.py` counts briefs pulled today (`0 of 7` today). Run records by hand in `<task>/runs/*.md`.
- Gap: no sensor sees whether a routine ran in the cloud, or whether it opened a web page ("Cloud routines run half-blind", `CLAUDE.md`). Routine count and account count disagree with no sensor on the account side.

**Telegraph+ build ledger** (Current inside that repo)
- Canonical source: `work-os/projects/telegraph-plus/records/events.jsonl`, append-only, `EVT-` ids plus per-type `record_id`; rules in `work-os/projects/telegraph-plus/records/PROTOCOL.md`; views under `work-os/projects/telegraph-plus/records/views/` generated by `work-os/projects/telegraph-plus/records/ledger.py build`; `work-os/projects/telegraph-plus/records/health.json` holds operational state on purpose apart from the ledger; `work-os/projects/telegraph-plus/records/views/MANIFEST.md` is the liveness view; `work-os/projects/telegraph-plus/records/cursor.json` tracks how far transcripts were reconciled.
- Sensors: `python3 records/ledger.py check` (views on disk match the ledger; MISSING, STALE, ORPHAN; exit 1). Two hooks in that repo's own `.claude/settings.json`: `reconcile_check.py` on every prompt (nudges a sweep when 60 minutes have passed since `last_successful_sweep`; always exit 0) and `stop_sweep.py` at Stop (runs the check, appends to `work-os/projects/telegraph-plus/records/sweep.log`, records a failure in `health.json`; never blocks). These fire only when a session is opened inside `telegraph-plus/`.
- State today: `last_successful_append` 2026-09-10; `last_failure` 2026-09-04 "stop backstop: views out of sync with ledger"; `consecutive_failures` 0.
- Gap: nothing outside the repo reads `health.json`; the lab-wide facts sheet sees only the repo's git counts.

**Voice ledger and guide** (Current, by hand)
- Canonical source: `work-os/brand-os/voice/VENKAT-WRITING-CANON.md` (the canon); `work-os/brand-os/voice/system/ledger/records.jsonl` (one Voice Decision Record per correction, `tier_confirmed` set only by Venkat); `work-os/brand-os/voice/venkat-writing-guide/` generated from the canon by `work-os/brand-os/voice/system/build_guide.py`, with `FILE-MANIFEST.md` carrying the canon hash.
- Sensors: `build_guide.py --check` (folder matches the canon hash, no duplicate headings or sentences); `work-os/brand-os/voice/system/check_ledger.py` (a turn with correction language must grow the ledger; exit 1); `work-os/brand-os/voice/system/sensors.py` (draft checks: em dashes block, other flags warn). All by hand. No hook or job.

**Public-safety manifests** (Current, by hand)
- `work-os/brand-os/engagement-os/tools/private-paths.txt` and `work-os/brand-os/engagement-os/tools/private-tokens.txt`: one line each, "removals are a publication decision and go to Venkat." Read by `check_public_safety.py` only.

### 2C. Registry-like lists nothing reads by script

**Rulings** (Current, read by hand only)
- `work-os/brand-os/DECISIONS.md`: numbered, dated rows quoting him; append-only; no status word; a superseded row is found by reading (the map's table). `RULINGS-IN-FORCE.md` at the root: `D-` ids, derived on 2026-09-08 from the old 72-entry log now in the warehouse; its own header says "Nothing here is settled until Venkat rules on Part 2." Source register: "sessions by hand; nothing reads them by script yet." State holds 185 decision lines seeded from the registries with `authority: derived`.
- Unclear: `RULINGS-IN-FORCE.md` says of itself "It is derived, not written" and that a script rebuilds it; no such script was found.

**Accepted-findings files** (Current)
- `.claude/skills/context-check/dead-pointers-accepted.txt` (1,035 mentions accepted today), `skill-check-accepted.txt` (56), `context/sources/discovery-accepted.txt`. Each line names the path or token and a reason. Read only by their own sensor. Lines marked "Alfred" in the discovery file "await Venkat's review" (the file's header). No sensor notices an accepted line whose reason has gone stale.

**Skills and agents** (Current; a folder is the record, no registry file)
- `.claude/skills/*/SKILL.md` (30) and `.claude/agents/**/*.md` (16 files). AD-02: not registered in the capability registry on purpose. Each skill declares a `Base directory:` line.
- Sensor: `.claude/skills/context-check/skill-check.py` (empty body, missing or bad base directory, every path named resolves against three places, every skill named by name exists; exit 1). Runs every session start through `facts.py`. Today: `30 skills and 16 agent files checked; 0 files with 0 problems; 56 accepted`. Proof: `.claude/skills/context-check/tests/skill_check_tests.py`, passed today.
- Usage: `evidence/sessions/USAGE.jsonl`, one line per session naming the skills, agents, and commands it used, rebuilt by `session-sync.py --usage` from the rendered transcripts. Read by `.claude/skills/session-capture/scripts/capture-report.py` on request. Nothing turns it into "skills nobody has used."

**Upskill-advisor records and gates** (Current records; governing status Unclear)
- `work-os/upskill-advisor/records/decisions.md` ("Decision register", `ID` and `Status` columns, correction by append); `work-os/upskill-advisor/gates/gate-0.md` to `work-os/upskill-advisor/gates/gate-5.md` with the vocabulary not started, in progress, technically passed, owner approved, released (`work-os/upskill-advisor/governance/gates.md`); `work-os/upskill-advisor/records/open-items.md` whose "Needs Venkat" section `facts.py` counts (2 today, file 9 days old).
- Unclear: whether `upskill-advisor` governs `telegraph-plus` is "unruled since 2026-09-07" (`context/intent/STANDING.md`, driver 3). The `telegraph/` repo inside it is superseded (`CLAUDE.md`), and its evals are listed under Historical below.

**Decision-foundry registers** (Current scaffold, idle since 2026-08-19)
- `work-os/projects/decision-foundry/governance/decisions/INDEX.md` (`DR-` ids, proposed/approved/rejected/superseded/withdrawn; four approved), `work-os/projects/decision-foundry/context/CONTEXT-SCHEMA.md` (21 required front-matter fields; "A context file missing a required field does not load"), plus `traces/`, `releases/`, `quarantine/`, `archive/` indexes, most empty by design. `README.md`: "Foundation approved. No product exists."
- Sensor: `work-os/projects/decision-foundry/tests/governance/validate-repo-structure.sh` (structure, line caps, no imports from archive or quarantine, template front matter, secrets, valid settings, and a Python front-matter check against the schema with six fixtures; exit 1 on any FAIL). By hand only; the repo's hooks folder is "Empty by design." No run recorded since 2026-08-19.
- Source register: "a project repo with no knowledge role yet" (`discovery-accepted.txt`).

**Plan indexes, persona ledger, ARCHIE queues** (Current, by hand)
- `work-os/brand-os/plans/INDEX.md` and `work-os/brand-os/engagement-os/plans/INDEX.md`: hand tables with a Status column. `work-os/brand-os/engagement-os/targets/_market/persona-ledger.md`: append-only rows with Provided, Observed, Inferred, Working hypothesis, Unknown; no consumer found. ARCHIE's `inbox/`, `backlog/`, `work-os/brand-os/engagement-os/agents/archie/archive/kills/`: queues by file date; `facts.py` reports the inbox count and oldest age. ARCHIE's `work-os/brand-os/engagement-os/agents/archie/config/data-sources.yaml` is a tiered path manifest that records its own break after the 2026-09-05 rename ("All 10 declared sources were dead") and its hand repair.

### 2D. Looked at and not counted as registries

- **Evidence record** (`evidence/receipts`, 48 files; `evidence/audits`, 13 files; `evidence/sessions`, 288 transcripts; `.claude/agents/alfred/LOG.md`): canonical stores, new files or appended lines only. Their sensors are in section 3 under `facts.py` and `session-sync.py`.
- **`context/state/CURRENT.md`**, the three career-model catalogs, `work-os/brand-os/voice/venkat-writing-guide/`, `docs/about-me/who-i-am--generated.md`, `records/views/*` in Telegraph+: generated views that say so.
- **Retrieval index** (`context/sources/index/`): derived from the register by `retrieve.py`; git ignores it. `stats.json` records build time, 1,868 records over 1,509 files, source bytes, compact bytes, and a token estimate. `runs.jsonl` logs each query with what was picked and refused. `facts.py` reports the index age and the count of markdown files newer than it (0 days old; 43 newer today).
- **`.claude/agents/alfred/TODAY.md`**: a hand list, read by `waiting.py`; git ignores nothing about it. **`.claude/agents/alfred/state/`**: session notes and unreceipted notes written by the hooks, git-ignored.
- **`GATES.md` and `.unlazy/`**: unlazy's working ledger, present only while a ledger is open (absent today); finished ledgers go to `~/Documents/_warehouse/unlazy-ledgers`.
- **`ROOT.md`, `TASTE.md`, `DONE.md`, `CLAUDE.md`, `context/how-i-work.md`**: canonical documents, loaded every session, no ids or status words (source id `root-doctrine`).
- **`work-os/brand-os/audience/evidence/evidence-register--2026-09-08.md`**: numbered "Claim N" headers, judgment-call confidence scores, no stable ids, no consumer found. A dated validation record, not a register.
- **`evidence/audits/2026-09-10-rule-audit/REGISTER-draft.md`**: a draft rule register from an audit that is still "four of six areas done" (`TODAY.md`). Dated, never edited after; not operational.

## 3. Checks and sensors: what runs, when, and what happens on failure

| Mechanism | Watches | Detects | Runs when | Produces | On failure | Proof it can fail |
|---|---|---|---|---|---|---|
| `.claude/agents/alfred/sensors/facts.py` | the lab as a whole | unreceipted sessions, open follow-ups, per-repo uncommitted, unpushed, no remote, snapshot age (ALERT over 3 days), Dropbox copy age (ALERT over 7), log gap (ALERT over 72 hours), briefs pulled today, Telegraph items needing Venkat, ARCHIE inbox, article gates pending, seed counts, open unlazy ledger, capture age and launchd state and `/tmp/session-sync.err`, sessions with no transcript, and one line each from the skill, architecture, State, sources, retrieval-index, career-model, and waiting sensors; drivers changed | SessionStart hook (`.claude/settings.json`), by hand `open`, `close`, `loops` | the facts sheet as hook context; the close sheet | lines prefixed `ALERT`; the hook never breaks a session (errors become a system message, exit 0); no notification beyond the sheet | `.claude/agents/alfred/sensors/tests/facts_tests.py`, 15 cases; passed today |
| `facts.py session-end` | sessions that changed files | a session with no receipt citing its id | SessionEnd hook | a note under `.claude/agents/alfred/state/unreceipted/` | next open routine writes a late receipt; 2 pending today | tests 4 to 6 in `facts_tests.py` |
| `.claude/agents/alfred/sensors/session-sync.py` | Claude Code and Codex sessions | sessions changed since last render; secret-like text | SessionEnd hook (`--hook`); launchd `com.venkat.session-sync` at 9, 13, 18 (loaded, last exit 0 today); by hand | transcripts under `evidence/sessions/`, `SYNC-LOG.md` rows, `USAGE.jsonl` | secrets replaced with a marker and named in the log; a failed launchd run leaves `/tmp/session-sync.err`, which `facts.py` reports; breaks when a Command Line Tools update replaces Python.app (`CLAUDE.md`) | `.claude/agents/alfred/sensors/tests/session_sync_tests.py`; passed today |
| `.claude/agents/alfred/sensors/waiting.py` | three trackers plus briefs | items waiting on Venkat, oldest first | called by `facts.py`; by hand | one line on the sheet (99 items today); `--html` page | none; it reports | none found |
| `docs/architecture/check.py` | capability registry | see 2A | every session start; `context-check` G; by hand | one line; findings in seven fields | exit 1; ALERT on the sheet | planted faults by hand 2026-09-12 (AD-13); no test file |
| `context/sources/check.py` | source register | see 2A | same | same, plus `--report` per source | exit 1 on register or health; discovery never fails | `context/sources/tests/check_tests.py`, 27 faults; passed today |
| `context/state/state.py check` | State ledger | see 2A | same | same | exit 1 on findings; stale is record only | `context/state/tests/check_tests.py`; passed today |
| `.claude/skills/context-check/skill-check.py` | skill and agent files | see 2C | every session start; by hand | one line; findings | exit 1 | `.claude/skills/context-check/tests/skill_check_tests.py`; passed today |
| `.claude/skills/context-check/dead-pointers.py` | every path named in a live file | paths that do not exist | by hand; called by `context/sources/check.py` discovery | list per file and line; `LIVE DEAD POINTERS: 3` today; 283 dated, 1,035 accepted | no exit code semantics found; the sources check counts it as record only | none found |
| `.claude/skills/context-check/context-check.sh` | the lab's context architecture | A: recovery (git, snapshot age, uncommitted per repo); B: identical files in two live places; C: files declaring themselves superseded but still live; D: front matter and links per area; E: files nothing points at; F: four known-dead folder names; G: the two registry checks | by hand or `/context-check` | a report on screen; writes nothing | no exit code; a person reads it | none. Section D still lists `chief-of-staff` and `_audit`, folders that left the lab |
| `.claude/hooks/root-lock.py` | the lab root | any tool call that would create something at the root outside `ALLOWED` | PreToolUse hook on Write, Edit, NotebookEdit, Bash | a deny with the reason and where to put the file | blocks the call; fails open on its own errors | `.claude/hooks/tests/root-lock-tests.py`; passed today |
| `.claude/hooks/unlazy-trigger.py` | each prompt | complete-work phrasing; new-system phrasing (design check) | UserPromptSubmit hook | a note in context | never blocks | no test file found |
| `.claude/hooks/implication-lens-footer.py` | each prompt | asks for the footer | UserPromptSubmit hook | a note in context | never blocks | `.claude/hooks/tests/implication-lens-footer-tests.py`; passed today |
| `.claude/skills/unlazy/scripts/stop-hook.mjs` | an open gates ledger | unmet gates | Stop hook (`.claude/settings.local.json`) | a block with the unmet list | blocks the stop; releases after 6 blocks with no progress; fails open on read errors | `.claude/skills/unlazy/tests/*.mjs` (not run here) |
| `work-os/brand-os/model/check_hub.py` and `build_who_i_am.py --check` | career model hub | see 2B | every session start via `facts.py`; by hand | one line | exit 1 by hand; no ALERT on the sheet | none found for `check_hub.py`; seed A-LIVE-301 records a guard bug found by use |
| `work-os/scheduled-tasks/market-signals/verify.sh` | 21 signal routines | live prompt differs from file | by hand, with saved API responses | OK, DIFF, NO MAP per routine | no exit code; a person rebuilds and updates | none |
| Telegraph+ `work-os/projects/telegraph-plus/records/ledger.py check`, `reconcile_check.py`, `stop_sweep.py` | that repo's ledger | views out of sync; a sweep overdue | prompt and Stop hooks inside that repo; by hand | `sweep.log`, `health.json`, `MANIFEST.md` | check exits 1; hooks never block | none found |
| `work-os/brand-os/engagement-os/tools/check_public_safety.py`, `validate_public_value.py` | a tree about to become public; public-value records | leaks; bad vocabularies | by hand, from the publishing skills | verdict and exit code | fail closed (1 or 2) | `work-os/brand-os/engagement-os/tests/test_public_safety.py`, `test_public_value_system.py`, `test_experience_design.py` (not run here) |
| `voice/system/build_guide.py --check`, `check_ledger.py`, `sensors.py` | the writing guide, the correction ledger, a draft | drift from the canon; a correction not recorded; em dashes and flagged phrases | by hand | verdicts | exit 1 | none found |
| `work-os/projects/decision-foundry/tests/governance/validate-repo-structure.sh` | that repo | see 2C | by hand | PASS, FAIL, SKIP lines | exit 1 | six fixtures inside it (fixture 06 must fail) |
| `.claude/skills/prove-it-can-fail` | any check | a check that cannot fail | by hand, per skill | a written proof | none | it is the proof |

**Where failure goes.** Every lab-wide sensor ends on the facts sheet. `ALERT` means interrupt him; a plain line means show at open; nothing shown means record only (`CAPABILITY-DEFINITIONS.md`, sensor standard). No sensor notifies outside a session, fixes anything, or opens a follow-up on its own. A follow-up exists only when Alfred or a receipt writes the `F-` line.

## 4. Sensing by registry

Marks: Present, Partial, Missing, Not applicable (n/a). "Partial" names the piece that exists.

| Registry | Integrity | Health | Discovery | Freshness | Usage | Coverage | Drift | Efficiency |
|---|---|---|---|---|---|---|---|---|
| Capability registry | Present (`check.py`) | Present (paths exist) | Partial (design check note on new-system prompts; no scan for unregistered shared systems) | Present (`changed` dates required; State compares them) | Missing | Present (entries equal definitions) | Partial (no second registry block; no live-vs-approved compare) | n/a |
| Source register | Present | Present (missing, unreadable, empty, moved hint) | Present (AD-08 discovery) | Present (newest change per source) | Partial (`read-by` declared; `runs.jsonl` logs queries; nothing reads it back) | Present (files per source) | Partial (nested and competing locations; no live-vs-approved) | Partial (retrieval `stats.json` sizes and token estimate) |
| State ledger | Present | Present (script missing or failing becomes ALERT) | n/a (an overlay) | Present (stale by kind) | Missing | Partial (counts by kind) | Present (status line versus registry) | Missing |
| Follow-ups | Partial (id form; no duplicate check) | Present (count) | Missing (a loop closed by hand elsewhere stays open) | Present (age) | Missing | n/a | Missing | n/a |
| Current drivers | Missing | Present (file exists) | Missing | Present (changed since last open) | Missing | n/a | Missing | n/a |
| Asset registry | Missing | Missing | Missing | Missing (no `changed`) | Missing | Missing | Partial (release-time safety and vocabulary checks, by hand) | n/a |
| Seedbank | Partial (index build lists files with no id line) | Present (counts) | Partial (`missed.md` rows; repeat check on capture) | Present (newest seed age) | Missing | Partial (count only) | Missing (index versus files) | n/a |
| Target index | Missing | Missing | Missing | Missing | Missing | Missing | Missing | n/a |
| Career model hub | Present (`check_hub.py` spokes) | Present | Missing | Missing (no `changed` dates) | Partial (`SPOKES.md` "Last returned", hand-kept) | Missing | Present (`build_who_i_am.py --check`; never-cite scan) | n/a |
| Cloud routines | Partial (`verify.sh` name map) | Missing (cloud runs unseen) | Missing | Partial (briefs pulled today) | Missing | Missing (record 28 or 29 versus account 2) | Present when run by hand (`verify.sh`) | n/a |
| Telegraph+ ledger | Present (`ledger.py check`) | Present (`health.json`, in-repo only) | n/a | Present (`MANIFEST.md` days since last event) | Missing | Partial (counts by type) | Present (views versus ledger) | n/a |
| Voice ledger and guide | Partial (`check_ledger.py`) | Missing | Missing | Missing | Missing | Missing | Present (`build_guide.py --check`, by hand) | n/a |
| Rulings | Missing | Missing | Missing | Missing | Missing | Missing | Missing | n/a |
| Accepted-findings files | Partial (parsed by their sensor) | Present | n/a | Missing (no stale-reason check) | n/a | Present (counted) | Missing | n/a |
| Skills and agents | Present (`skill-check.py`) | Present | Missing (unregistered by design, AD-02) | Missing | Partial (`USAGE.jsonl`, read on request) | Present (30 and 16 counted) | Missing | n/a |
| Upskill-advisor records and gates | Missing | Partial ("Needs Venkat" count and file age) | Missing | Partial (file age) | Missing | Missing | Missing | n/a |
| Decision-foundry registers | Present when run (`validate-repo-structure.sh`) | Missing | Missing | Missing | Missing | Partial (approval census) | Missing | n/a |

## 5. Gaps

**A registry with no adequate sensing.**
- Asset registry: nothing reads `registry.yaml` by script; two entries disagree with themselves and nothing says so.
- Target index: no script reads or checks it; last change 2026-09-04; the writer named in its README was not found.
- Rulings: two files, no status word, nothing reads them by script; `RULINGS-IN-FORCE.md` claims a regenerating script that does not exist.
- Seedbank index: hand-built, four days older than the README, no check that it matches the files.
- Cloud routines: the record and the account disagree on the count, and no sensor sees the cloud side.

**Sensing with no clear owner.**
- Career-model line: 30 never-cite hits and one broken spoke today, no `ALERT`, no follow-up, no owner named on the sheet.
- Discovery findings from the source register: three open today, "show at open", owner not named; `discovery-accepted.txt` lines marked "Alfred" wait for Venkat with no age on them.
- Accepted-findings files: nobody re-reviews an accepted reason.
- `USAGE.jsonl` and `runs.jsonl`: usage is recorded and nobody reads it into a finding.

**Sensors that exist and do not run on their own.** `verify.sh`, `check_public_safety.py`, `validate_public_value.py`, `build_guide.py --check`, `check_ledger.py`, `sensors.py`, `validate-repo-structure.sh`, `prove_checks.py`, `context-check.sh`, `dead-pointers.py` (except when the sources check counts it). Each depends on a person remembering.

**Sensors with no proof they can fail.** `docs/architecture/check.py` (proved by hand once, no test file), `waiting.py`, `dead-pointers.py`, `context-check.sh`, `check_hub.py`, `verify.sh`, `unlazy-trigger.py`, the Telegraph+ hooks, the voice scripts.

**Known broken and still listed as live somewhere.** `work-os/brand-os/audience/weekly/run.sh` hardcodes the lab path from before the rename (the folder name context-check section F counts), has no LaunchAgent on this machine, and last logged a dry run on 2026-09-02; `work-os/brand-os/model/SPOKES.md` still shows it as "weekly run." Five of six schema files under `work-os/brand-os/audience/weekly/schemas/netra/` are zero bytes.

## 6. Historical, Proposed, Unclear

**Historical (kept, not operational).**
- `work-os/brand-os/docs/career-advisor-reasoning--2026-09-10/`: the `MASTER-REGISTRY-PROPOSAL`, `SCAN-REGISTRY`, `03-asset-candidate-registry.md`, and the source manifests. "The drop is evidence, not canon" (`work-os/brand-os/model/REASONING-INDEX.md`).
- `work-os/upskill-advisor/telegraph/evals/` (`prove_checks.py`, 24 of 24 proven on 2026-09-02; `run_evals.py`): inside a repo `CLAUDE.md` marks superseded. The lab-wide `prove-it-can-fail` skill descends from it.
- `work-os/projects/_archive/telegraph-native-lab/nativelab/registry.py`: frozen at commit e633ad9, 2026-09-04.
- `evidence/audits/2026-09-10-rule-audit/REGISTER-draft.md`: a dated draft.
- `work-os/brand-os/audience/weekly/` and its Netra schema port: see section 5.
- The old 72-entry decisions log: `~/Documents/_warehouse/_archive/DECISIONS--from-imac-2026-09-08.md`.

**Proposed (named, no file or no run).**
- "Use Case Registry" or Scenario register: named in AD-32, `LAB-OPERATING-MODEL.md`, and the roadmap; "no file exists" (`2026-09-14--ai-lab-portfolio-architecture.md` section 2, deferred by design).
- The roadmap's "Registries" list names Open Loops as a registry; today that is the follow-up lines in receipts.
- Context assembly sensors ("required-context recall, irrelevant-context load, material conflict preservation, loaded-but-unused context"): `CAPABILITY-MAP.md`, planned entry.
- Retrieval's "planned miss/unused/context-impact/outcome sensing when real usage supports it": `CAPABILITY-MAP.md`, retrieval entry.
- A scheduled restore-and-diff sensor for driver 2: `docs/plans/2026-09-14--restore-and-diff-sensor--plan.md`. A commit-key guard: `docs/plans/2026-09-14--commit-key-guard--plan.md`, "not built; needs Venkat's go."
- Portfolio object homes with status "none" or "split" in the portfolio architecture (Proof, Outcome, Opportunity, and others): a design, not a registry.

**Unclear.**
- Whether `upskill-advisor` governs `telegraph-plus` (unruled since 2026-09-07).
- Who owns a "show at open" finding that nobody turns into a follow-up.
- Whether `decision-foundry`'s check has run since 2026-08-19 without a record.
- The routine count: 28 (`work-os/scheduled-tasks/README.md`), 29 (capability map fault line), 2 (the account on 2026-09-11).
- The `work-os/brand-os/engagement-os/targets/index` writer.

## 7. Verification of this file, against the goal

1. Every registry in section 2 names its source path and whether it is canonical, a view, derived, or a hand list. Yes.
2. Every check in section 3 names the script or hook that implements it, with the file that wires it where one exists. Yes.
3. Section 4 marks all eight kinds of sensing for seventeen registries. Yes.
4. The capability registry and the source register are covered in 2A with their check behavior and today's output. Yes.
5. Nothing was designed or changed. The only file written this session is this one; no script, registry, schema, hook, or accepted file was edited. Yes.
6. Saved at `docs/documentation/CURRENT-REGISTRIES-CHECKS-SENSORS.md`. Yes.

## 8. What was run to write this (2026-09-14, 13:23 to 13:40)

`facts.py open` (through the SessionStart hook); `context/sources/check.py list` and `--report`; `docs/architecture/check.py`; `context/state/state.py check`; `skill-check.py --summary`; `dead-pointers.py`; `check_hub.py`; the test suites `root-lock-tests.py`, `implication-lens-footer-tests.py`, `facts_tests.py`, `session_sync_tests.py`, `skill_check_tests.py`, `context/sources/tests/check_tests.py`, `context/state/tests/check_tests.py`, all passed; `launchctl list` for `com.venkat.session-sync`; `ls` of `~/Library/LaunchAgents`. Files read in full: `facts.py`, `context/sources/check.py`, `docs/architecture/check.py`, `CAPABILITY-MAP.md`, the check section of `state.py`, `context-check.sh`, `verify.sh`, `check_hub.py`, the three hooks, both settings files, `REGISTER.md`. Three read-only scans covered brand-os, the projects and scheduled tasks, and the docs, hooks, and root files; their claims used here were spot-checked (`registry.yaml`, `SPOKES.md`, `run.sh`, the Netra schema sizes, `health.json`, the Telegraph+ settings).
