---
title: Context v0.1, the design and its acceptance tests (proposed 2026-09-13; not implemented; tests frozen only at his word)
date: 2026-09-13
author: Alfred (session 904ccc0a), at Venkat's word (the /goal of 09:07 and 09:10: "Design the smallest robust Context v0.1 and its acceptance tests. Do not implement it.")
kind: a design, read against the eight ecosystem papers in docs/ecosystem/, the capability map and definitions, the Retrieval skill and its packages, and the State ledger as built today; the canonical operational spec is the context-assembly subsection in docs/architecture/CAPABILITY-DEFINITIONS.md; this report holds the model, the contract, the package, the boundaries, the plan, and the five tests
follows: AD-29 (the sequence: State, then the brief, then Dynamic Context Assembly); AD-30 (the morning brief is the first proving loop); AD-37 (State v0.1 approved and implemented); docs/reports/2026-09-13--state-v0-1-design.md; the roadmap's Phase 1 (section 10) and the Context paper's sections 8, 11, 13, 14, 21
question: "What is the smallest Context that lets a job get the minimum sufficient understanding it needs now, from Retrieval and State, so that missing, stale, conflicting, or wrong-scope context changes what happens next, and every output can be traced back to its sources without a person rebuilding the chain?"
result: ONE CONTRACT PER JOB KIND, ONE PACKAGE PER RUN, NO STORE. Context is a contract that says what a job must know, a script that fills what it can from State and drivers and refuses what it must, a model that picks the rest by meaning and says why, and a sealed package with an adequacy state that lowers what the job may do. Trust is the adequacy state acting on the action level. Experience is a projection block inside the package. Lineage is one appended line per run and a trace command that walks it. Five tests, three ordinary choices made, three decisions surfaced for him.
needs_venkat:
  - the action ladder as the trust mechanism: a contract declares the job's action level (observe, prepare, recommend, act) and the script lowers it by rule when context is not sufficient; the model may raise severity, never lower it
  - where assumptions and corrections land: as State lines (proposed, or his word with an anchor) written by the consumer at close, so Context keeps no store and a correction persists without being restated
  - who may write a contract: Alfred writes and changes contracts; his word is required for any contract at action level act, in any scope other than AI Lab, or whose prohibited list is loosened
tags_used: observed (a file or script read today) · inferred (my design) · his-word · synthetic (a scenario with no registered source yet)
---

Alfred — the short version first.

**Context is a contract and a package, not a store.** Retrieval already finds evidence with its limits. State already says what is current, owned, open, and superseded. What neither does is answer "what does this job need to know right now, is that enough, and what may it do if not." Context v0.1 adds exactly that: a small written contract per kind of job, a script that fills the contract from State and drivers and refuses what the contract forbids, the model filling the rest by meaning, and one sealed package per run with an adequacy state the job must obey.

**Today's evidence for why.** The State package the brief reads this morning is 262 KB and 504 items across six fields (observed, 09:12). The brief needs about twenty of them. Nothing today says which twenty, why, or what to do when one is missing. The last receipt's two follow-ups (F-20260913-0844-1: `changed` carries every derived line on seed day; F-20260913-0844-2: a to-do line reads as active with no hands on it) are both Context problems, not State problems: the contract for the brief settles them without touching the ledger.

**Trust acts, it does not warn.** A contract declares the job's action level. The script computes adequacy from facts (a required slot empty, an item older than the contract allows, an item from another scope, an unresolved conflict on a required slot) and lowers the allowed action level by rule. A brief assembled from incomplete context may prepare and say what is missing; it may not present its next action as settled.

**Five tests, all scored on the package by script.** Minimum sufficient context for the real morning brief; a required item removed and the behavior changing; a stale item and a wrong-client item in a commercial scenario; one output traced to its sources with no hand reconstruction; a correction that persists into the next run without being restated.

# 1. The job, in the papers' words and the lab's (observed)

The roadmap, section 10: "Given the job, actor, situation, current State, available evidence, scope, Authority, constraints, and time, assemble the minimum sufficient Context needed now." The Context paper, section 3: "Minimum sufficient context, not maximum available context." Section 7, the missing state: "I do not have enough context to do this reliably." Section 8, the contract: "The Context Contract defines the need. Dynamic context assembly fulfills it." The Trust paper, principle 3: "A warning that changes nothing is not a meaningful control."

Five facts from the lab today shape the design:

- **The front door loads the same files every session** whatever the job (CAPABILITY-MAP, family table: "Remove AI and the loading is identical, so the design is challenged"). That is the current context design, and it is the one being replaced.
- **State's package is complete, not selective.** 262 KB for the brief's six fields; `decided` alone is 180 lines. State's design said so on purpose: "Context Assembly consumes the package and picks fields per job. State does not decide relevance."
- **Retrieval's package already carries what Context must preserve**: source id, date, tier, ceiling, marks (claimed, observed, his word), current versus superseded, pointers and whether they resolve, conflicts with both sides, a missing-evidence state, and the list of sources searched (T7 package, observed). Context adds nothing to that shape. It reads it.
- **The two shapes share pointers.** A State line's `source` and a Retrieval result's `ref` are both a path, a path#anchor, or a registry id. State's design chose that "so Context Assembly can join them without a third format." This design holds it to that.
- **Assumptions have no home.** When the brief or a recommendation fills a gap with a guess, nothing records the guess where it can be corrected. The Context paper's principle 6 (fact versus interpretation) and the roadmap's C5 (correction persists) both need one.

# 2. The five questions the design check asks (judgment)

1. **Job needed:** give a job the minimum context it needs now, with each item's source, age, authority, scope, and kind of knowledge kept, and make inadequate context lower what the job may do.
2. **What covers it today:** `retrieval` finds evidence; `continuity` (State) says what is current; `drivers` says what matters; `authority` says what may not happen. None picks the slice for a job, none says whether the slice is enough, and none lowers an action when it is not. The map already holds `context-assembly` as planned for exactly this; this is its v0.1, not a new entry.
3. **AI-native test:** without AI, context is a fixed file list per job, which is today's design and the one AD-01 challenges; the list would go stale the way the front door has. With AI, the slice is picked by meaning for this job and this moment, each item says why it is there, gaps and conflicts are judged material or not, and the script keeps the judgment honest by refusing items without pointers, items outside scope, and an adequacy claim the facts contradict. The outcome changes: the job gets twenty items that fit instead of five hundred that do not.
4. **Standard:** shared system, the twelve fields (written into the definitions today, section 12 here). Its contracts file follows the registry standard. Its check follows the sensor standard.
5. **New system necessary:** no new capability, agent, service, store, or platform. One contracts file, one script, one skill for the model's part, two skill edits, one facts line, one line per run in an append-only file.

# 3. The three ordinary design choices, made (inferred)

| Choice | Picked | Why, one line | Undo |
|---|---|---|---|
| A store of assembled context, or none | none; one package per run, sealed and pointed at, never reused as a source | the Context paper forbids "permanent context packages" and "context that never expires"; a reused package is stale context with a new date | nothing to undo |
| Contracts per job instance, per job kind, or one global schema | per job kind, written once, read every run; a job instance passes its parameters (scope, subject, since) | the paper forbids "enormous schemas before the jobs require them"; a kind is stable, an instance is not; tens of contracts over eight months, not thousands | a contract is a record; retire it with a dated line |
| Adequacy judged by the model, or computed by script from slot facts | computed by script from facts the script can prove; the model may raise severity with a reason and may never lower it | the lab's rule: scripts decide what is true; the same raise-only rule already governs sensor materiality (AD-11); a model grading its own context sufficient is the 76% false-success case | the raise-only rule is one function |

**Home, assumed:** `context/assembly/` with `CONTRACTS.md`, `assemble.py`, `runs.jsonl`, and `tests/`. The same reasoning as the source register (AD-16) and the State ledger (AD-37, his word): `context/` holds what the machinery reads to know what matters now; the list changes and the reader does not. Not raised as a decision because he has ruled this way twice.

# 4. The minimum Context model (inferred)

## 4.1 The Context Contract

One record per kind of job, in `context/assembly/CONTRACTS.md`, in the registry record shape (a heading plus `- key: value` lines, parsed by the same ten-line reader `check.py` uses). The fields are the paper's section 8, plus the action level from the roadmap's authority ladder.

| Field | What it holds | Who sets it |
|---|---|---|
| `id` | stable, plain words, never renamed | Alfred |
| `job` | one sentence | Alfred, from the consumer's own definition |
| `consumer` | the skill, routine, or actor that runs on the package | Alfred |
| `actor` | who reads the result and who decides; drives the experience projection | Alfred |
| `scope` | one of the five, or `param` when the instance supplies it | Alfred |
| `action-level` | observe · prepare · recommend · act; the most the job may do when context is sufficient | Alfred; his word for `act` or any scope but AI Lab |
| `required` | slots that must be filled; each names its source kind (state, drivers, retrieval, facts, given), its freshness limit, and its authority floor | Alfred |
| `conditional` | slots that become required when a named condition holds | Alfred |
| `optional` | slots that may be filled when cheap | Alfred |
| `prohibited` | what must not be in the package: other scopes, other subjects, sources by id, kinds (transcripts as fact, seeds as fact) | Alfred; his word to loosen |
| `authority-when-conflict` | the tier order that resolves a conflict, and which conflicts are surfaced rather than resolved | Alfred |
| `freshness` | the default age limit per source kind | Alfred |
| `missing-behavior` | per required slot: stop, ask, narrow, provisional, retrieve-once | Alfred |
| `cap` | the most items the package may hold (default 40) | Alfred |
| `status`, `added`, `changed`, `ruled-by` | registry standard | script and Alfred |

**The first contract, the morning brief** (the real lab job; the fields below are the design, not yet written into a file):

```
### brief
- id: brief
- job: Tell Venkat where things stand, what materially changed, what needs his judgment, and the one next action most worth taking.
- consumer: alfred-open
- actor: Venkat reads and decides; Alfred assembles and recommends
- scope: ai-lab
- action-level: recommend
- required: carry-forward (state.carry_forward, the newest /next; ≤ 3 days; authority ≥ system) · waiting (state.waiting, owner Venkat; ≤ 14 days each or marked old) · in-hand (state.active where a claim exists, not TODAY.md lines; today) · decided-since-last-open (state.decided with changed ≥ last open; authority his-word or system only) · drivers (context/intent/STANDING.md, the four current) · alerts (the facts sheet's ALERT lines; ≤ 1 hour)
- conditional: evidence-for-next-action (retrieval, scoped by the next action's subject; when carry-forward names a topic the package cannot pointer from State) · unreceipted-session (evidence-record, when the sheet lists one) · driver-threat (retrieval, when a facts line touches a driver's threat list)
- optional: changed (state.changed, non-derived; capped at 10) · yesterday's day review (evidence-record)
- prohibited: lines in any scope but ai-lab · transcripts or receipts read as current state · seeds as fact · any derived decision presented as his word
- authority-when-conflict: his-word > system > proposed > derived; newer wins inside a tier; two his-word lines that disagree are surfaced, never resolved
- freshness: state package as_of today; facts sheet ≤ 1 hour; a waiting item older than 14 days is shown as old, not dropped
- missing-behavior: carry-forward empty → provisional: pick from waiting and say so · alerts missing → retrieve-once: run facts.py · drivers unreadable → stop
- cap: 30
```

This one contract closes both open follow-ups from the 08:44 receipt by design: `decided-since-last-open` and `changed` exclude derived lines; `in-hand` reads claims, not to-do lines.

## 4.2 The Context Package

One JSON object per run, sealed by the script with an id `ctx:<date>-<hhmm>-<4 hex>`. The roadmap's minimum shape (section 10.2), with each field's builder named.

| Field | Holds | Built by |
|---|---|---|
| `id`, `as_of`, `contract`, `contract_changed`, `consumer`, `actor`, `scope`, `params` | which run, which contract version, for whom, in which world | script |
| `items[]` | the context itself, one per slot filling; each carries `slot`, `what` (the line or evidence), `pointer` (path, path#anchor, or registry id), `from` (state, drivers, retrieval, facts, given, model), `source` (register id or ledger id), `date`, `age_days`, `authority` (tier), `ceiling` (use ceiling, carried from the register, never raised), `epistemic` (observed, inferred, assumed, decided, claimed, unknown), `status` (current, superseded, stale), `scope`, `why` (one line, the model's) | script for state, drivers, facts; model for retrieval and the free slot; script validates every one |
| `slots` | per contract slot: filled, empty, stale, conflicting, and by which item ids | script |
| `adequacy` | one of sufficient · sufficient-with-condition · incomplete · conflicting · blocked, with `reasons[]` (each a slot fact) and `raised_by_model` when the model raised it, with its reason | script; model raise-only |
| `allowed_action` | the contract's level, lowered by the adequacy rule (section 5) | script |
| `conditions[]` | what the output must carry when adequacy is with-condition (a stale item, a resolved conflict, an assumption) | script |
| `conflicts[]` | both sides, the tier of each, whether the contract's rule resolved it and how, or `surfaced` | script from State and Retrieval conflicts; model may add with both refs |
| `gaps[]` | required or conditional slots not filled, with the contract's missing-behavior for each, and what was searched when Retrieval was tried | script |
| `excluded` | counts by reason (wrong scope, wrong subject, prohibited kind, superseded, over cap, not relevant), and the material ones by pointer with one line why | script for rule exclusions; model for relevance exclusions that touch a required slot |
| `withheld` | the count of lines and records in other scopes that matched, never their content | script (State's own count, carried) |
| `known[]` | item ids the consumer must not ask the person about again (everything from State with authority his-word or system, and every prior correction) | script |
| `experience` | six fields: `current`, `changed`, `reliance`, `needs_you`, `next`, `why`; each a short list of item ids with one line of plain words; `for` names the actor role | model, from items only; script checks every id is in `items` |
| `controls[]` | per item that can be corrected: `correct_via` (state append superseding id X; contract slot Y; register source Z) | script |
| `write_back[]` | what the consumer must write at close: assumptions as proposed State lines; corrections as superseding lines; the package id into the receipt | script |
| `lineage` | `state_package` (as_of, scope, opened), `retrieval_runs[]` (the ids of the runs.jsonl lines consumed), `drivers_changed`, `facts_at` | script |
| `size` | items count, bytes, and the size of what was read to build it | script |

**What is not in the package:** history, transcripts, whole files, anything from a scope the contract did not name, a source outside the register, an item without a pointer, a judgment. The model never quotes a file the script did not fetch or State did not return.

## 4.3 Epistemic marks, kept not invented

`epistemic` is carried, never assigned by taste: a State decision with authority his-word is `decided`; a Retrieval record marked claimed is `claimed`; a record marked observed is `observed`; a State line with authority proposed or derived is `inferred`; a slot the model filled with no pointer is refused, and if the contract's missing-behavior is `provisional` the model may write one item marked `assumed` with `from: model` and `pointer: none`, which is the only pointerless item allowed and is always listed in `write_back` as a proposed State line. `unknown` is a gap, not an item.

# 5. Trust: adequacy lowers the action (inferred; decision 1 for him)

The rule, all by script from slot facts:

| Slot facts | Adequacy | Allowed action | The output must |
|---|---|---|---|
| every required slot filled, in scope, fresh, at or above its authority floor; no unresolved conflict on a required slot | sufficient | the contract's level | nothing extra |
| a required slot filled but stale, or below its floor, or a conflict resolved by the contract's tier rule, or a triggered conditional slot unfilled, or an `assumed` item in a required slot | sufficient-with-condition | the contract's level | name each condition in the output (the package lists them in `conditions`) |
| a required slot empty and its missing-behavior is provisional, retrieve-once (already tried), or ask | incomplete | at most prepare; `needs_you` set when the contract's level was recommend or act | say what is missing and what would fill it; present nothing as settled |
| an unresolved conflict on a required slot (two his-word lines, or two sources at the same tier) | conflicting | at most prepare; `needs_you` set with both sides | show both sides; choose neither |
| a prohibited item present after the model's fill, a required item from the wrong scope, a required slot whose missing-behavior is stop, or drivers unreadable | blocked | observe | stop, narrow, or ask; the package says which |

The model may raise (sufficient to incomplete, because it judges a gap material) with a reason recorded in `adequacy.raised_by_model`. It may never lower. The consumer may never raise `allowed_action`. That is the whole of Trust in v0.1: no score, no platform, one state and one level, both in the package, both enforced where a script can see them.

**Why this is Trust and not a warning.** The Trust paper's principle 3 and the roadmap's 5.5. A brief assembled at `incomplete` cannot present a next action as settled; a commercial recommendation assembled at `conflicting` cannot be marked ready; a package at `blocked` produces no recommendation at all. The state travels with the work: the consumer's output cites the package id, and the receipt carries the adequacy word beside it.

# 6. Experience: six fields from the same items (inferred)

The roadmap's section 10.4 and the seven Experience questions, answered from the package, not from a second source:

| Question | Where the answer is in the package |
|---|---|
| 1. What does this person need to understand now | `experience.current` and `experience.changed` |
| 2. What should the system already know | `known[]`: the consumer must not ask about these; a question about a known item is a failure the test catches |
| 3. What changed | `experience.changed`: items whose State line changed since the contract's since, in plain words, with the work they affect (items in the same package that cite them) |
| 4. What can be relied on | `experience.reliance`: established (decided, his-word), conditional (with-condition items), inferred, disputed (in `conflicts`), stale, unknown (in `gaps`) |
| 5. What requires judgment | `experience.needs_you`: set by rule when adequacy is incomplete or conflicting on a required slot, or when the contract names the decision as his; the model may add one with a reason, never remove one |
| 6. What control | `controls[]`: the exact write-back path per correctable item |
| 7. What should change because of the interaction | `write_back[]`: the lines the consumer writes at close |

`experience.for` names the actor role. One package, one set of items; a second role gets a second `experience` block from the same items, never a second package. That is the paper's "one underlying truth, multiple projections" without a platform.

Progressive disclosure is the consumer's job, with one rule the script enforces: the six fields are short lists of item ids with one line each, so a brief can show `current` and `needs_you` and keep `why` for when he asks.

# 7. Lineage: one line per run, one command to walk it (inferred)

- **Every run appends one line** to `context/assembly/runs.jsonl`: id, when, contract and its `changed` date, consumer, scope, adequacy, allowed action, every item's pointer and `from`, the State package's `as_of` and `opened`, the Retrieval run ids consumed, and the size. Append-only, never edited, committed (unlike Retrieval's derived index): the line is the lineage record, and lineage must survive a new machine.
- **The output cites the package id.** The brief's first line of `why`, the receipt's decisions section, a recommendation's footer: `ctx:2026-09-14-0712-a3f9`. A consequential output with no `ctx:` id is a finding the check reports.
- **`assemble.py trace ctx:<id>`** walks the chain and prints each hop with resolves or does not: output (the receipt or report that cites the id) → the runs line → each item's pointer → for a State pointer, the ledger line and its own `source` (a registry row or receipt anchor) → for a Retrieval pointer, the run line in `context/sources/index/runs.jsonl` and the record's path#anchor → the file on disk. A hop that does not resolve is named; the walk continues.
- **The package is derived; the line is the record.** The full package JSON is written under `context/assembly/runs/` (git-ignored like Retrieval's index) for inspection and tests. If it is lost, the runs line still holds every pointer.

# 8. Who does what

- **Script (`assemble.py`):** read the contract; call `state.py package` with the contract's scope, fields, since, subject; fill state, drivers, and facts slots by rule; mark stale by the contract's freshness; refuse any item without a resolving pointer, any item outside the contract's scope or subject, any source not in the register, any prohibited kind; compute slot facts, adequacy, allowed action, conditions, `known`, `controls`, `write_back`; validate the model's items and experience block (every id exists, every pointer resolves, no ceiling raised, no adequacy lowered); seal the package with an id; append the runs line; `trace`; `check` (the sensor).
- **Model (the `context-assembly` skill):** for each retrieval slot, run the Retrieval skill's five steps and hand the package to the script; fill the free slot by meaning and write `why` for every item it adds; name material exclusions; read conflicts and gaps and raise adequacy with a reason where a gap is material; write the six experience fields from items only; mark assumptions as `assumed` and never as anything else.
- **Venkat:** contracts at action level act, in any scope but AI Lab, or with a loosened prohibited list (decision 3); corrections; scope changes; the conflicts the contract surfaces.

# 9. Boundaries (inferred, each one line)

- **Retrieval** finds evidence across the past and returns it governed; Context asks it by slot, consumes its package as is, and never reads outside the register to fill a gap. Context never lowers Retrieval's marks and never raises a ceiling.
- **State** says what is current; Context reads its package with the contract's fields and never calls `append`. Assumptions and corrections reach State only through the consumer at close, by the existing `from-receipt` and `append` paths (decision 2).
- **Drivers** are read, referenced by section, never copied into a contract.
- **Memory** (seeds, voice, about-me) reaches a package only as Retrieval evidence with its ceiling; a seed is never a fact.
- **Authority** is read from the contract and the register, enforced by the script's lowering rule, and never granted by a package. A `proposed` line authorizes nothing; `allowed_action` is a ceiling, not a permission.
- **Process** is the consumer's; the package says what the job may do next, not what step is next. No engine.
- **Experience surfaces** (the brief, a future UI) read the `experience` block; none keeps a second truth.
- **Operating Scope** is a field on every item, a parameter of every contract, and a refusal in the script. Cross-scope content never travels; the count does.
- **Evidence-record** stays write-once; the runs line and the receipt's `ctx:` id are the only writes, both appends.

**No registry is duplicated:** contracts are new records of a kind nothing holds today (what a job needs); items point at State ids, register ids, and anchors; the package is derived and dated.

# 10. Growth over eight months, and what tells us the implementation no longer fits (inferred)

The brief says: robust as the lab grows in volume, relationships, scopes, actors, products, and connected systems, without scale infrastructure before a real need. How each kind of growth lands, and the trigger a script can measure:

| Growth | Where it lands in v0.1 | Trigger, measured how | Then |
|---|---|---|---|
| Volume (ledger lines, sources, runs) | State and Retrieval absorb it; a package is capped by contract, so its size does not follow the lab's | median package bytes over 30 days, from `size` in the runs lines, rises past 40 KB; or `assemble` for a no-retrieval contract passes 2 seconds | tighten the contract's cap or fields; only after that, index the runs file |
| Relationships (products, accounts, campaigns, people) | `subject` on items and as a contract parameter; `trace` walks pointers on demand; no graph | a contract needs a second subject in one run more than once a week (counted in `params`) | a `subjects[]` parameter; still no graph |
| Scopes (professional, career, public, personal in use) | `scope` on every item and contract; the script refuses cross-scope; `withheld` counts it | the first run in a scope other than AI Lab (counted in runs lines) | the cross-scope refusal becomes a planted-fault check before that scope's consumer goes live; contracts split into one file per scope when any scope holds more than five |
| Actors (ARCHIE, specialist agents, automations, a client contact) | `consumer` and `actor` on the contract; `experience.for` per role from the same items | two consumers ask for the same contract with different required slots (a diff of contract edits) | a contract per consumer with a shared parent; not before |
| Products (Telegraph+, instruments) | a subject and a scope; nothing in Context is product-shaped | a product's own store wants to be a source | it enters the register; Context does not change |
| Connections (email, calendar, Drive) | they enter the register as sources; Retrieval returns them; Context reads Retrieval | a connection needs a slot kind Retrieval cannot return (a live event, not a record) | a `live` source kind on the contract, filled by the connection's own sensor; the roadmap's Connection Contract, not a Context change |
| Contract drift (the real risk) | every runs line records items loaded; the consumer's output cites item ids; the check counts loaded-but-uncited and corrections that say "needed X" | loaded-but-uncited over 40% for a contract across 10 runs; or "needed but not loaded" twice for one slot | edit the contract; the two counts are the sensor the definitions table already names for this capability |
| A second reader (a UI) | reads the same package JSON and the same runs lines | a reader that is not Claude Code opens the file | a small read path over the same files; the record does not change |

What is deliberately not built: no context database, graph, dependency engine, universal schema, Trust taxonomy, Experience platform, propagation engine, or scenario harness (the roadmap's section 22). The contracts and the package shape are what allow those to be added later without changing the contract a consumer relies on.

# 11. The five acceptance tests (proposed; frozen only at his word, the way the State five were)

Every test is scored on the package by a script, never on a judgment. Every test names the failure it exists to catch. The human-visible check on the brief text is a second pass, the way the four State tests were run "as a user." Home at implementation: `context/assembly/tests/CONTEXT-TESTS.md` beside `run_tests.py`. C1, C2, and C4 use the real lab job; C3 and C5 use the commercial scenario; C5 is then repeated on the lab job.

**The commercial scenario, synthetic until a scenario registry exists (AD-32):** an agency strategist prepares a launch recommendation for Brand X, US, HCP audience, for a client commercial lead who decides. Written into a throwaway State ledger with `scope: professional`, extending S5's brand: a current positioning decision that supersedes an older one; segmentation v5 replacing v4; a payer-access assumption marked `proposed`; MLR-approved claims as a constraint; a client instruction dated 90 days ago where the contract's freshness for market conditions is 30 days; and one insight from Brand Y, another client, that matches the topic by words. Contract `client-recommendation`: scope professional, subject param, action level recommend, prohibited: any other subject's lines and any other client's sources, authority-when-conflict: client decision > agency analysis > vendor claim.

**C1. Minimum sufficient context for the brief** (real lab job: the morning brief, AD-30; commercial: a client return after two weeks)
- Setup: the `brief` contract; today's real ledger and facts sheet; `assemble.py run brief --consumer alfred-open`.
- Expected: all six required slots filled, each item with a pointer that resolves and a `why`; `adequacy: sufficient` or with-condition, with the condition named; items ≤ 30 and package bytes under a tenth of the State package it consumed (today: 262 KB in, so under 26 KB out); `opened` contains no transcript and no receipt body; `withheld` reports any other-scope count; the six experience fields non-empty and every id in them present in `items`; `known` holds every his-word and system item. Then the human pass: a fresh session given only the package answers the six questions from the 08:42 baseline (where are we, what changed, what is waiting, who holds what, what next, where each came from) with the same pointers, and asks no question about a `known` item.
- Failure caught: the dump (the State package passed through); an item with no why; history read inside the run; a required slot silently empty; the brief re-asking what State already holds.

**C2. Missing required context changes behavior** (real lab job: the brief; commercial: the recommendation with no current strategy on file)
- Setup: a throwaway copy of today's ledger with both `/next` commitment lines marked kept, so `carry_forward` is empty; the same contract.
- Expected: `slots.carry-forward: empty`; `adequacy: incomplete` with the reason a slot fact; `allowed_action: prepare` although the contract says recommend; `gaps` names the slot and the contract's missing-behavior (provisional: pick from waiting and say so); `needs_you` set; no item in that slot with `from: state` (nothing invented); if the model fills it, the item is `assumed`, `from: model`, and listed in `write_back` as a proposed State line; the script refuses a package that claims sufficient. Human pass: the brief written from it says what is missing and marks its next action provisional.
- Failure caught: silent invention; a warning with no lowered action; a proposed next action presented as settled; a model lowering adequacy.

**C3. Stale and wrong-scope context, excluded or constrained** (commercial scenario; lab mirror: a superseded ruling and a warehouse path)
- Setup: the scenario ledger above; `assemble.py run client-recommendation --scope professional --subject brand:X`.
- Expected: the Brand Y item absent from `items`, counted in `excluded.wrong_subject`, named by pointer with the reason; the older positioning present only as `superseded` attached to the current one, never in a filled slot; the 90-day client instruction in its slot with `status: stale` and `age_days: 90`, and `adequacy: sufficient-with-condition` with that condition named, or `incomplete` if the contract marks the slot's freshness hard; the payer-access line `epistemic: inferred` and in `experience.reliance` under inferred, never under established; `allowed_action` lowered to prepare when the stale item sits in a required slot with a hard freshness; `withheld` counts the ai-lab lines the same ledger holds. Lab mirror, same script: the `brief` contract with ruling 036 and 037 both in State returns 037 in the slot and 036 as superseded only.
- Failure caught: cross-client leak; an old decision governing; stale shown as current; an assumption shown as established; a condition with no lowered action.

**C4. End-to-end lineage, one output to its sources, by script** (real lab job: the brief's one next action)
- Setup: the C1 run; the brief written from it cites `ctx:<id>`; the close writes the id into the receipt.
- Expected: `assemble.py trace ctx:<id>` prints the chain output → runs line → each item → State ledger line → registry row or receipt anchor, and for any retrieval item → the Retrieval run line → the record's path#anchor → the file; every hop resolves; for the next-action item the chain ends at the receipt that made the commitment; the walk opens no transcript; a planted broken pointer in a copy of the runs line is reported by hop, and the walk continues past it.
- Failure caught: an output with no package id; an item whose pointer is a paraphrase; a Retrieval item with no run id; a chain that needs a person to guess a step.

**C5. A correction persists into the next run without being restated** (commercial scenario first, then the lab job)
- Setup, commercial: after C3, the client lead corrects the payer-access assumption; the consumer writes one State line with `supersedes` the proposed line, authority his-word with an anchor (or proposed by the named actor with an anchor), through `state.py append`; then `assemble.py run client-recommendation` again for the same subject.
- Expected: the corrected line fills the slot as current; the old one appears only as superseded; `experience.changed` names the correction in plain words and lists the items in the package that cited the old assumption; `known` holds the correction, so the strategist is not asked again; the C3 package's runs line is untouched and still points at the old line (history intact); the new runs line points at the new one. Lab: correct one `proposed` decision in today's ledger the same way and run `brief`; the same five conditions hold.
- Failure caught: a correction lost between runs; the person re-asked; the old assumption still used; history rewritten instead of superseded; a correction with no anchor accepted as his word.

**What the five do not test, on purpose:** the judgment in the brief (the proving loop, AD-30); Retrieval's recall (its own seven); State's ledger rules (its own five); latency beyond "a no-retrieval package builds in under two seconds"; a second lab consumer's contract (the stopping rule needs one before v0.1 closes; it is the plan's step 6, not a frozen test).

# 12. The twelve-field spec (written into the definitions today, under context-assembly)

Job, consumers, inputs and outputs, deterministic, AI, human, canonical store (none; contracts are a record of needs, runs lines are lineage), access (`assemble.py run|trace|check`, plus the skill), failure, evaluation (the five tests), evidence (runs lines, package ids in receipts), sensors (health: a run per brief day; integrity: pointers resolve; missing: a consequential output with no `ctx:` id; freshness: contract `changed` age; unused: loaded-but-uncited; quality: needed-but-not-loaded), and the AI test. The definitions file is the canonical spec; this report is the design.

# 13. The lab v0.1 implementation plan (not executed; one /goal, one review)

| Step | What | Proves | Size |
|---|---|---|---|
| 1 | `CONTRACTS.md` with the `brief` contract and the record reader; `assemble.py check` refuses a contract with a missing field, an unknown scope word, an action level above what its ruled-by allows, or a required slot with no source kind; planted-fault tests | a contract cannot lie about what it needs | about 80 lines, 5 faults |
| 2 | `assemble.py run`: fill state, drivers, facts slots by rule; freshness; scope and subject refusal; slot facts; adequacy and the lowering rule; `known`, `controls`, `write_back`; seal and append the runs line; the derived package under `runs/` | C1 without retrieval; C2; the lab mirror of C3 | about 160 lines |
| 3 | The `context-assembly` skill: the model's steps (retrieval slots through the Retrieval skill, the free slot, why lines, raise-only, the six experience fields, assumptions as `assumed`); `assemble.py validate` for what the model hands back | C1 in full; the model half of C2 | one skill file, about 40 lines of validation |
| 4 | `assemble.py trace`; the `ctx:` id in receipts (a line in `alfred-close`); `alfred-open` step 0 becomes `assemble.py run brief` in place of the raw State read | C4; operational behavior for the gate | about 60 lines, two skill edits |
| 5 | The commercial scenario as a throwaway ledger and the `client-recommendation` contract; C3 and C5 scored; C5 repeated on the lab job; one line on the facts sheet (last run, adequacy, findings) | C3, C5; the sensor exists | scenario file, about 40 lines of test |
| 6 | A second lab consumer's contract, `signal-move` (Signals → Moves, the secondary stress loop), run once on a real brief day | the stopping rule's "at least one other consumer" | one contract, one run, one report |
| 7 | Freeze the five tests at his word; run them blind; the building-to-live gate (operational path, planted faults caught, `check.py` passes with the entry moved from planned to building, then live) | v0.1 live | one run, one report |

Cost: about 350 lines of Python, no library, no service; one skill, two skill edits, one facts line, one contracts file, one append-only lineage file. Two to three sessions. Nothing new in the registry: `context-assembly` exists as planned and moves through building to live.

# 14. Not done here

No file was created outside this report and the definitions subsection; the registry entry's `changed` date and `build-steps` line were updated so the record names this design, and `check.py` was run. No contract file, no script, no skill, no runs line, no ledger line. The five tests are proposed, not frozen. The three decisions in the front matter wait on his word.
