---
title: State v0.1, the design and its acceptance tests (approved and implemented 2026-09-13, AD-37; the tests are frozen at context/state/tests/STATE-TESTS.md)
date: 2026-09-13
author: Alfred (session 11ed46ab), at Venkat's word (the /goal of 06:30: "Design the smallest robust State v0.1 and its acceptance tests. Do not implement State.")
kind: a design, read against the registries and receipts that exist today; the canonical operational spec is in docs/architecture/CAPABILITY-DEFINITIONS.md under continuity; this report holds the model, the package, the boundaries, the plan, and the five tests
follows: AD-29 (State is the next implementation slice of continuity); AD-30 (the morning brief is the first proving loop); docs/reports/2026-09-13--alfred-real-jobs-reconstructed.md section 2 (where context keeps being rebuilt); the retrieval close-out (Retrieval is live and consumable)
question: "What is the smallest State that lets AI and people know what is currently true, active, changed, open, waiting, owned, or superseded, without reading history, and that still fits a commercial brand, account, or campaign?"
result: ONE SMALL LEDGER, FIVE KINDS, ONE PACKAGE. State is an index over the registries, not a second store of facts: every line points at a registry id or an evidence anchor, and a line with no pointer is refused. The ledger holds only what no registry holds today (which ruling supersedes which, who owns which work, what was promised, which changes were material). Everything else is read from where it lives. Five acceptance tests, three ordinary design choices made, two decisions surfaced for him.
needs_venkat:
  - the home: context/state/ (proposed; the same reasoning as the source register, AD-16) or inside Alfred's folder
  - the fork: a small ledger of State's own for the four things no registry holds, or fully derived state with no ledger (section 3 says why the ledger)
tags_used: observed (a file or script read today) · inferred (my design) · his-word
---

Alfred — the short version first.

**State is a thin index, not a new store.** The lab already has registries for decisions, follow-ups, assets, seeds, capabilities, sources, and drivers. What it lacks is four small things no registry holds: which ruling supersedes which as a field, who owns which work right now, what was promised to carry forward, and which changes were material. State v0.1 records exactly those four, points at everything else by id, and hands a consumer one Current State Package it can filter by scope.

**The same five kinds carry a client's brand or campaign.** A decision, a piece of work, an open loop, a commitment, and a status, each with a subject and an operating scope. A commercial account is a subject, not a new kind. That is what makes the design portable without a schema.

**Five tests, all scored on the package.** Current versus superseded; ownership across parallel sessions; open and waiting items surviving a close; a material change with its source; and a scoped commercial case that must withhold across scopes. Each says what failure it catches.

# 1. What State must do, in the lab's own words (observed)

The jobs reconstruction found five places context keeps being rebuilt: what he already approved; what state the lab is in; which session did what; which rulings are current; what was asked at close. The definition's job line (his, 2026-09-13): "Maintain a compact, current, source-backed representation of what is currently true, active, decided, unresolved, waiting, owned, or superseded so the lab stops rebuilding operational truth from raw records."

Three facts from today shape the design:

- Supersession has no field. Rulings 036 and 037 are found by reading; `retrieve.py` already computes "Correction to NNN" by rule, so a script can seed the overlay.
- Ownership has no home. `.claude/agents/alfred/state/sessions/*.json` records when a session started and ended, not what it owned. Two sessions built step 2 six minutes apart.
- "Waiting on Venkat" has three homes (receipts, TODAY.md, Telegraph's open-items). `waiting.py` reads them as one view. 75 items this morning.

# 2. The five questions the design check asks (judgment)

1. **Job needed:** say what is currently true, active, changed, open, waiting, owned, or superseded, with a pointer, without reading history.
2. **What covers it today:** `continuity` (follow-ups, TODAY.md, the next-action line) covers open and next; nothing covers supersession as a field, ownership, commitments, or materiality. State is continuity's next slice (AD-29), not a new entry.
3. **AI-native test:** without AI, State is a status file a script maintains, and it would drift the way TODAY.md does. With AI, materiality, supersession where wording is implicit, conflict reading, and "what deserves attention" are judged at each update, and the script keeps the judgments honest by refusing lines without pointers. The outcome changes: state stays current because something reads meaning at every close.
4. **Standard:** shared system, inside continuity; the ledger follows the registry standard; its check follows the sensor standard.
5. **New system necessary:** no new capability, agent, service, or database. One ledger file, one script, two skill edits, one facts line.

# 3. The three ordinary design choices, made (inferred)

| Choice | Picked | Why, one line | Undo |
|---|---|---|---|
| Fully derived, or a small ledger of State's own | a small ledger for the four things no registry holds; everything else derived | derivation cannot produce ownership, promises, or materiality, and re-deriving supersession at every open is the reconstruction the job forbids | delete one file; the registries are untouched |
| Record shape | JSON lines, append-only, the latest line per id wins; never edited, never deleted | the lab already runs this pattern in `targets/index/verdicts.jsonl`; a script appends safely while another reads; every line keeps who and when; a UI reads it as is | a converter to markdown records is ten lines |
| Human view | `CURRENT.md`, generated from the ledger, says it is a view | he reads markdown; the ledger is the record (registry standard: a second file is generated or it is a bug) | stop generating it |

**Home, proposed:** `context/state/` with `STATE.jsonl`, `CURRENT.md`, `state.py`, and `tests/`. The same reasoning as the source register (AD-16): `context/` holds what the machinery reads to know what matters now, the list changes and the reader does not. The alternative is `.claude/agents/alfred/state/`, which exists and is Alfred's; State serves every actor and a UI, so it should not live inside one actor's folder. His call.

# 4. The minimum State model (inferred)

**Five kinds.** Nothing else in v0.1.

| Kind | What one line says | Registry it points at | Example id |
|---|---|---|---|
| `decision` | a ruling's current status and what it supersedes or is superseded by | the decision files (brand-os, rulings in force, architecture, Telegraph, upskill) | `decision:brand-os/037` |
| `work` | a piece of work that is active, paused, done, or handed off, and who owns it | receipts, TODAY.md, a project's STATUS.md | `work:retrieval-v0-1-close-out` |
| `loop` | an open loop's owner, waiting-on, and status | the `F-` lines in receipts and audits (evidence-record owns them) | `loop:F-20260913-0602-2` |
| `commitment` | a promise or carry-forward: next session starts with, "I do not push without you", a date | receipts' next-action lines, his words by anchor | `commitment:R-2026-09-13-0602/next` |
| `status` | the current status of a capability, project, article, or artifact when no registry field carries it | the map, the source register, gate tables, `registry.yaml` | `status:article/2026-09-08--green` |

Drivers are referenced, never copied: a package carries the driver ids from `STANDING.md` and their state lines' dates.

**Record minimum, one JSON object per line:**

```
{"id": "decision:brand-os/037", "kind": "decision", "what": "Correction to 036: the drop holds 61 files, not 62",
 "status": "current", "supersedes": ["decision:brand-os/036"], "scope": "ai-lab", "subject": "career-advisor-drop",
 "owner": "Venkat", "established": "2026-09-10", "changed": "2026-09-10",
 "source": ["work-os/brand-os/DECISIONS.md#row:037"], "authority": "his-word",
 "by": "alfred-close/11ed46ab", "when": "2026-09-13T06:40"}
```

Field rules a script checks: `id` stable and prefixed by kind; `status` from a short list per kind (decision: current, superseded, proposed; work: active, paused, done, handed-off; loop: open, closed, waiting; commitment: open, kept, missed; status: the target registry's own words); `scope` one of the five; `source` at least one pointer that resolves (a path, a path#anchor, or a registry id the register or map can resolve); `authority` one of his-word, proposed, system, derived; `by` the writer and session; `when` the write time. `subject` optional: the brand, account, campaign, article, or project the line is about. `next` optional: the prepared first step.

**Ids that already exist are reused, never renamed:** `F-` follow-ups, ruling numbers, `AD-` rows, `A-LIVE-` seeds (as provenance only), `CAP-` (as provenance only), register and map ids.

# 5. The Current State Package (inferred)

One JSON object, built by `python3 context/state/state.py package --scope ai-lab [--consumer brief] [--fields ...] [--since 2026-09-12]`:

| Field | Holds | Built by |
|---|---|---|
| `as_of`, `scope`, `consumer` | when, for which world, for whom | script |
| `active` | work lines with status active or paused, owner, since, next | script |
| `decided` | decisions current in scope, newest first; each with what it supersedes | script from the overlay plus the registry rows |
| `changed` | lines whose `changed` is after `--since`, with source and authority | script; the AI wrote the lines at close |
| `open` | loops open, with owner and age | script from `F-` lines plus loop lines |
| `waiting` | loops and commitments whose owner is Venkat, read from all three homes as one list | script (`waiting.py` already does the reading) |
| `ownership` | who holds what, and any work with two active owners | script |
| `superseded` | decisions superseded since `--since`, with by whom | script |
| `carry_forward` | open commitments, the newest "next session starts with" first | script |
| `conflicts` | two active owners on one work id; a decision with two current successors; a loop closed in a receipt but open in TODAY.md; a status in the ledger that disagrees with its registry | script by rule |
| `stale` | lines older than their kind's freshness (work 7 days, commitment 3 days, loop 14 days, status the registry's `changed`) | script |
| `withheld` | the count of lines in other scopes that matched, never their content | script |
| `provenance` | every line's `source`, `authority`, `by`, `when` | carried, never dropped |

A consumer asks for the fields it needs; the brief asks for six (active, changed, open, waiting, decided, carry_forward). Retrieval's package and this one share the pointer shape (path#anchor, registry id), so Context Assembly can join them without a third format.

# 6. Who does what (the twelve-field spec is in the definitions; the split here)

- **Script:** ids, timestamps, status words, pointer resolution, derivation from registries (`F-` lines, rows that say "Correction to", map and register statuses, git, session ids, receipt existence), conflict rules, freshness, scope filtering, the package. The check refuses a line without a resolving source, a `current` decision with `authority: derived` presented as his word, two active owners, two current successors.
- **AI:** at each close, judge which changes were material and write their lines; propose supersession where the wording is not explicit, marked `proposed`; read conflicts and stale lines and say what deserves attention; summarize `changed` in plain words for the brief. The AI never writes `authority: his-word` without an anchor to his words.
- **Venkat:** rulings; closure that needs judgment; scope changes; ambiguous conflicts; the two decisions at the top of this report.

# 7. Boundaries (inferred, each one line)

- **Retrieval** finds evidence across the past; State says what is current now. Both use the same pointers. State never fetches; Retrieval never writes State. When state is missing, State's failure path asks Retrieval for the evidence and writes a `derived` line, never a `his-word` one.
- **Memory** (seeds, concepts, voice, about-me) is what he thinks and how he sounds. Not state. A seed appears in State only as provenance.
- **Context Assembly** consumes the package and picks fields per job. State does not decide relevance.
- **Authority** is recorded, never granted, by State. A `proposed` line authorizes nothing. His word is a line with an anchor.
- **Registries** own the durable objects. State holds overlays and pointers. The competing-store check in `docs/architecture/check.py` already refuses two entries claiming one store; State's canonical store is its own ledger and nothing else.
- **Evidence-record** stays write-once. State is current-only and can be rebuilt from receipts and decision files; rebuilding is the fallback, not the routine.
- **Operating Scope** is a field on every line. The package filters by it and reports withheld counts. Cross-scope content never travels in a package for another scope.

**No registry is duplicated** (checked against the map's registry table): decision files keep their rows, State adds status and links; receipts keep `F-` lines, State adds owner and waiting-on where the line lacks them; TODAY.md stays his list, State reads it; the map, the register, `registry.yaml`, and `verdicts.jsonl` keep their statuses, State reads them; `STANDING.md` is referenced; seeds and the career model are provenance only.

# 8. The five acceptance tests (proposed; frozen only at his word, the way the retrieval seven were)

Every test is scored on the package by a script, never on a judgment. Every test names the failure it exists to catch. Home at implementation: `context/state/tests/STATE-TESTS.md` beside `run_tests.py`.

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

# 9. The lab v0.1 implementation plan (not executed; one /goal, one review)

| Step | What | Proves | Size |
|---|---|---|---|
| 1 | Home, record shape, `state.py check` with the refusals in section 6; planted-fault tests (no pointer, two owners, two successors, bad scope word, derived shown as his word) | the ledger cannot hold a line that lies | about 120 lines, 6 faults |
| 2 | Seed the ledger by script from what exists: decisions from the five decision files with the "Correction to" rule (`authority: derived`); loops from `facts.py loops`; commitments from the receipts' next-action lines; work from TODAY.md's unchecked items and the newest receipts; statuses from the map and the register. Nothing hand-written | State starts from the record, not from memory; every seeded line points somewhere | one script, run once, output reviewed |
| 3 | `state.py package` with scope filtering and `CURRENT.md` generation | S1, S4, S5 | about 100 lines |
| 4 | Two skill edits: `alfred-close` writes lines after the receipt (decisions, work, loops, commitments, material changes); `alfred-open` reads the package first and marks stale. One `claim`/`release` command for sessions. One line on the facts sheet (check summary, stale count, conflicts) | S2, S3; operational behavior for the gate | two skill sections, one facts line |
| 5 | Freeze the five tests at his word; run them blind; building-to-live gate (operational path, planted faults caught, `check.py` passes with the continuity entry updated) | the slice is live inside continuity | one run, one report |
| 6 | Wire the brief to the package (AD-30). Not part of this slice | the first integration loop | next goal |

Cost: about 250 lines of Python, no library, no service. One to two sessions. Nothing new in the registry; the `continuity` entry gains the ledger as a second canonical store path and the check as a sensor.

# 10. Evolution triggers, each observable by script (inferred)

| Trigger | Measured how | Then |
|---|---|---|
| The ledger passes 5,000 lines, or `package` takes over 2 seconds | line count; a timer in the check | write a compacted current-only snapshot; still one file, still no database. Only after that fails: sqlite with the same record shape |
| Two writers append within the same minute more than once a week | `by` and `when` on adjacent lines | a lease on `claim`, the way unlazy's `--claim` already works |
| Ownership conflicts exceed three a week | the `conflicts` field, counted at open | leases with expiry; not before |
| The first line in a scope other than AI Lab | the check counts scopes | scope filtering becomes a planted-fault test before any UI reads the file |
| Consumers keep reading `derived` decisions as if settled | the brief cites a derived line more than once for the same decision | a confirmation step at open turns derived into his-word with his one word |
| A reader needs sub-second reads across sessions, or a UI opens it | a second reader that is not Claude Code | a small read path over the same file; the record does not change |

# 11. Not done here

No file was created outside this report and the definitions section. No ledger, no script, no seed run, no skill edit. The five tests are proposed, not frozen. The home and the ledger-versus-derived fork wait on his word.
