---
name: ai-lab-portfolio-architecture
what: The target model of the Portfolio the AI Lab operates on. What the Portfolio is for, the durable things inside it and how each changes, how they relate, which Shared Intelligence domains understand them, the six operating loops that make it compound, and how today's lab maps onto that model. Review-ready. Architecture only. No schemas, agents, folders, UI, or code.
status: proposed, 2026-09-14. Written under the Product Ecosystem doctrine of 2026-09-14 (as revised after his review, section 15 of that file). Not ruled. Three points wait on his word (section 10).
home: docs/ecosystem/
read_with: 2026-09-14--ai-lab-product-ecosystem-design-doctrine.md (governs; not reopened here); 2026-09-13--portfolio-as-the-product-spec-v0-1.md (the working spec this narrows); docs/architecture/LAB-OPERATING-MODEL.md; the four current-state briefs of 2026-09-14 in docs/research/assessments/ (the evidence)
labels: observed (a file read or a script run on 2026-09-14) · inferred (my reading) · proposed (this design, waiting on his yes)
---

# The AI Lab Portfolio: target architecture

## 0. What this file settles

The doctrine says how the lab behaves: five Products, one connective intelligence layer, State and Authority underneath, Noticing and Learning across. It does not say what the Portfolio is made of. So today a capability lives in the career model, a prospect lives in a target folder, an idea lives in the seedbank, a public asset lives in a registry, and nothing connects them. No outcome has ever been recorded. No signal has ever reached action.

This file answers five questions:

1. What is the Portfolio for, and what makes it different from the career model, State, and evidence.
2. What durable things exist in it, how each one changes, and where each one is canonical today.
3. How those things relate, without a schema.
4. Which intelligence domains understand them, and how Portfolio Intelligence reads across all of them.
5. Which few operating loops make the Portfolio change and compound, and how today's lab maps onto the target.

**Rules this file keeps.** The doctrine's Product definitions and boundaries are not reopened. The career model stays the canonical capability spine and nothing writes into it from inference (AD-31, ruling 038). There is no universal Portfolio database. Nothing has to earn its right to exist; tests judge implementations (AD-25). What must exist is separated from how big its first form needs to be.

**The AI-native definition used.** The doctrine's exact four criteria, section 0 of the revised file:

1. The job or way of working is redesigned.
2. AI is part of the core design.
3. Remove AI and the job or way of working no longer exists as designed; a human or a fundamentally different non-AI process would have to take over.
4. The main value can be a new way of working.

The Portfolio as a whole (section 1) and every operating loop (section 5) are tested against all four.

---

## 1. The Portfolio: definition and purpose

**Definition (proposed).** The Portfolio is everything Venkat has built, earned, learned, or kept open that can move a goal, held as one connected picture and read against goals he still owns. The working spec calls it "usable accumulated capacity." That is the right phrase.

**The job it must enable.** Judge each move by what it leaves behind. His own move, the lab's move, a product's move, a piece of writing, a reply to a prospect: each one is read for what it creates, reuses, or puts at risk over time. The doctrine's Portfolio promise: "Today's move is judged by tomorrow's starting position."

**What makes it distinct.** Four things already hold parts of this, and each one is not the Portfolio:

| Thing | What it holds | Why it is not the Portfolio |
|---|---|---|
| Career model | What he has done and can do, as approved, evidence-tagged record (92 capabilities, 5 domains, 13 products, frozen 2026-08-31) | It looks backward on purpose. Its register entry says it is "not-alone" for "where he is heading." It is the capability spine the Portfolio reads, never the whole. |
| State | What is true now: active, decided, open, waiting, owned, superseded | It records current condition and judges nothing. The Portfolio reads it over time. |
| Evidence and Retrieval | What happened, with pointers; what the lab already holds on a question | Evidence is the raw material. The Portfolio is the reading of what it adds up to. |
| Seedbank | Ideas he wrote, said, or endorsed (825 files) | Ideas are one input. A seed becomes portfolio when it becomes an asset, a product, or a belief in use. |

**What the Portfolio adds that none of them hold.** Connection (this work served that goal and strengthened that asset). Current relevance (this capability is the active offer; that one is dormant). Compounding (what remains after the work is done). Concentration (too much rests on one client, one product, one idea). Optionality (what is still open because of a past choice). Drift (recent choices no longer match a stated goal).

**The Portfolio tested against the four criteria.**

| Criterion | Evidence |
|---|---|
| 1. Redesigned | Today "is this compounding" is asked by hand at the end of a project, if at all; the career model is a record; outcomes are an empty folder. In the target, the question is asked at the move, and the answer connects the move to goals, capacity, and cost. |
| 2. AI in the core design | Connecting a piece of work to a goal and to the assets it strengthens or duplicates. Seeing that six activities are one loop. Seeing that an opportunity advances one goal and works against another. A script cannot do these; it can only count. |
| 3. Remove AI | What remains is a catalog of assets, a list of four drivers, and a monthly review he would have to run himself. That is the shape the lab has today, and it has produced zero recorded outcomes. |
| 4. New way of working | Reuse noticed when a thing is made, not rediscovered months later. Tension between goals shown before a commitment. The economic loop (work, retained capital, proof, access, new paid use) watched as one loop. |

Passes. The reading is the product. The records underneath stay records.

---

## 2. The durable things in the Portfolio

Fifteen kinds of thing. Each one is durable: it outlives the session that touched it, it changes over time, and more than one loop reads it. Each has one canonical home, or the table says plainly that it has none today.

**How to read the table.** *Canonical home today* is observed. *Verdict* is the current-to-target call: connect (exists, needs linking), weak (exists, thin or stale), missing (no home), legacy (kept as record, not used), obsolete (should retire). Section 6 carries the full map; this table carries the home per object.

| Object | What it is, in one line | How it changes over time | Canonical home today (observed) | Verdict |
|---|---|---|---|---|
| **Goal** | What he is trying to change, reach, keep, explore, or become | Exploratory, active, committed, paused, achieved, abandoned, superseded. Only by his word. | `context/intent/STANDING.md`: four current drivers, each with kind, working-when, threats, dated state. Cap of four at his word. | connect. The drivers are goals in all but name. They need the working spec's minimum contract (desired state, horizon, priority, constraints, relationships, authority) only where a loop needs it. |
| **Capability** | Something he or the lab can reliably do, with evidence | Emerging, established, advanced, foundational, dormant. Changes only by a dated ruling and an amendment to the model. | Career model, `work-os/brand-os/model/` (92 CAP records, 82 skills, 48 techniques, 46 tools, 5 stages). Register id `career-model`, authoritative. Lab-system capabilities are a separate list in `docs/architecture/CAPABILITY-MAP.md` (9 entries) and stay separate (AD-04). | connect. Two amendments have been pending since 2026-09-02. No reader has returned a fact. No capability-to-capability relation exists in the data. |
| **Product / build** | A thing being built or shipped that others could use: Telegraph+, worthy-tool, decision-foundry, the site, the lab's own capabilities | Idea, spec, building, beta, live, parked, superseded. Status by evidence (commits, users), not by opinion. | Split. Historical: `products.json` in the career model (13 PRD, to Jul 2026). Current: each repo's own `STATUS.md` or README. No one current list. Follow-up F-20260910-1630-7, "lab-wide build ledger," is open. | weak. What must exist: one current list of builds with status and the capability each one evidences. The career model keeps history; it is not that list. |
| **Asset / IP** | A reusable thing with an owner and a form: a framework, instrument, method, article, page, or deck | Seed, candidate, private, approved, published, archived. Reuse is counted, not estimated. | `work-os/brand-os/engagement-os/assets/registry.yaml` (AS-001 to AS-006; 2 archived, 1 candidate, 3 private). The forensic asset audit of 2026-08-27 to 09-10 lists "~40 works, 8+ instruments" and grades them; it is in no register. | weak. The registry is canonical and right-shaped. The audit's forty works are not in it and nothing links an asset to a capability. |
| **Account** | A named company or client: what it needs, has said, has been told | Watch, engage, refused, active client, past client, dormant. Verdicts append. | Prospects: `engagement-os/targets/` (15 companies, 11 dossiers, verdicts append-only, idle since 2026-09-04). Clients, past and present: the warehouse and the unopened contracts store. Confidential; outside the lab on purpose. | connect for prospects. missing for clients: no object says "this account paid, for this, and this is what we owe each other." |
| **Audience** | Who the public work is for, what they read, what moves them | Draft, canon, superseded, by his ruling | `work-os/brand-os/audience/` (ICP v3 canon; personas "best draft"; buyer-terms frozen; the weekly instrument dead). Positioning canon beside it. | connect. Canon exists. The measuring instrument points at a folder that no longer exists. |
| **Campaign** | A run of public work with one aim, over a period, on named channels | Planned, running, done, judged. Judged by what it produced (audience, inbound, proof), not by volume. | None. The publishing chain has nine skills and a `distribution/` folder that says "Nothing has been written here yet." Ruling D-110: Substack under his own name, "publish before building the system around it." | missing, and can wait until there is a second public piece. The first piece is one campaign of one. |
| **Opportunity** | Something open that could become paid work, a product use, or a public moment; what it fits and what it would cost | Noticed, judged, pursued, won, lost, declined, expired | None current. Three partial homes: target verdicts marked "engage" (11), the 2026-08-26 opportunity map (dead, no capability ids), and PVO-001 to 004 (public-value opportunities, a different sense, all "advance" while their assets were archived). "Approaches sent: 0." | missing. This is the object the AD-31 chain runs through (market need, capability, evidence, buyer language, opportunity, work, new evidence) and it has no home. |
| **Relationship** | A person who matters: what has passed between you, what is owed | Cold, warm, active, owed, lapsed. Changes with contact and outcome. | None canonical. `targets/_people/` (5 records, no capability ids), a relationship spreadsheet from 2026-09-02 that no script reads, a LinkedIn message export of 3,156 messages unread. Scope: Professional / Advisory; names never leave it. | missing as an object; legacy as data. Waits on his ruling to open the export (proof gap G-03). |
| **Engagement** | Paid or committed work for one account: scope, price shape, what was delivered, what was learned | Proposed, agreed, delivering, delivered, invoiced, closed. Terms stay confidential. | None in the lab. The career model records one dated fact ("first paying client of the new era 2026-07-17") and the asset audit grades one engagement as the only Tier 2 proof with a path to Tier 3. Rate receipts and contracts for 2019 to 2022 are in an unopened store. | missing. Must exist even at one line per engagement, because outcome, revenue, proof, and relationship all hang off it. |
| **Scenario** | A realistic commercial situation used to test whether a lab capability transfers under different scope, evidence, and authority | Family, instance, variant (roadmap section 17). Evidence states: observed, supported, inferred, constructed, unknown, contested. | None. "Use Case Registry" is named in AD-32 and the roadmap; no file exists. State test S5 uses a synthetic scenario and says so. | missing by design for now. A thin register "when repeated scenario work justifies it" (roadmap). Not before. |
| **Proof** | A graded piece of evidence that a capability, claim, or asset holds up | Unsupported, owner-asserted, documented, demonstrated, externally corroborated, outcome-validated (the asset audit's ladder). A grade can fall when a pointer dies. | Graded in one place only: the asset audit's claim-to-proof matrix and proof-gaps file, in `work-os/brand-os/docs/`, which no register covers. Ungraded evidence: career-model extracts (observed, owner-stated, inferred tags), claim ledgers under `assets/verification/`, transcripts and receipts (evidence-record). | weak. The ladder exists and is good. It is applied to one corpus once, read by two files, run by no script. Proof grades belong on the objects they grade (capability, asset, engagement), carried with Trust's marks. |
| **Outcome** | What actually happened after a move: a reply, a meeting, a sale, a reader, a belief that changed, a loss | Recorded once, dated, never edited. Linked to the move and the object it changed. | `engagement-os/outcomes/` exists and is empty. The career model calls outcome claims "formally an empty class by his ruling." No outcome of any kind is on record in the lab. | missing. The single largest gap. Every loop in section 5 ends here, and nothing can be learned or compounded until it is filled. |
| **Revenue** | Money in, by engagement or product, and the shape of income over time | Invoiced, received, recurring, one-off. Private. Scope: Career / Portfolio and Personal. | Not in the lab. "Income, hours, runway, pipeline, audience size: not found." Only he can supply it. | missing on purpose. The architecture needs a place for it that never leaves its scope; the first form is his word, not a system. |
| **Experiment / option** | A test run to learn something (a retrieval test, a hand test, a routine trial), or a path kept open on purpose (a dormant capability, a parked product, a domain not yet entered) | Experiment: planned, run, read, closed. Option: open, exercised, expired. | Experiments about the lab: `docs/reports/` (13 dated reports) and the frozen test files. Options: scattered. Dormant capabilities are tagged in the model (CAP-088, CAP-089); parked products sit in their repos; nothing names an option as an option. | connect for lab experiments (well recorded). missing for options: the Portfolio cannot read optionality if nothing says what is being kept open and why. |

**Two things that are not Portfolio objects, on purpose.**

- **Signals** (the market-signal briefs, 105 backfilled files) are evidence about the market. They feed Market Intelligence. A signal becomes a Portfolio object only when it becomes an opportunity or an outcome. The 2026-09-11 scan's rule stands: signals do not automatically become seeds, beliefs, or actions.
- **Commitments, open loops, and today's list** are State. They describe the current condition of work, not durable capacity.

**The one-home rule.** Each object has one canonical home. Everything else that lists the same thing is a view and says so (registry standard, `CAPABILITY-MAP.md` section 3). Where a home is missing, this file says missing. It does not pick the folder; that is an implementation choice under AD-33.

---

## 3. How the things relate

No schema. These are the relations the loops in section 5 need, in plain words, with the rule for where each relation is recorded.

**The recording rule (his ruling 038, extended).** A relation is written where the work happens, on the side that changed, never inside the canonical model it points at. A capability match is recorded in the dossier, the brief, or the engagement record, with the CAP id and the extract, never in `capabilities.json`. The same holds for every object: the newer, more specific record points at the older, more canonical one.

| From | To | The relation | Recorded on | Why it matters |
|---|---|---|---|---|
| Goal | every other object | "serves," "threatens," "no longer fits" | the object (a goal id on the engagement, the asset, the build) | Nothing can be read against goals if nothing says which goal it serves. |
| Goal | Goal | reinforces, competes with, depends on, constrains | the goal (the working spec's "relationships" field) | Tension between goals is a Portfolio moment ("this advances one and works against another"). |
| Capability | Proof | "evidenced by," with a grade | the proof record and the asset, engagement, or product that is the evidence | The model's own doc 15 says every capability "is stronger than its public evidence." Proof is how that gap closes. |
| Capability | Capability | combination, adjacency, leads-to | not in the data today; combinations exist only in prose (doc 14) | The four "genuinely new combinations" are what buyers pay for and what nothing can retrieve. |
| Product / build | Capability | "evidences," "exercises" | the build's own status record, by CAP id | Today 17 of 92 capabilities have a product link; three products link to none, including the one used in paid work. |
| Asset | Capability | "expresses," "packages" | the asset record | The asset registry has no capability link at all. |
| Seed | Asset | "grew into" | the asset record, by A-LIVE id | One seed per artifact; connections recorded, never collapsed (seedbank rule). |
| Asset | Expression | "expressed as" (post, page, deck, article) | the expression's own record | The asset doctrine already in force: a post is an expression of an asset, not a new asset. |
| Audience | Campaign | "aimed at" | the campaign | A campaign is judged by the audience it reached. |
| Campaign | Asset, Outcome | "used," "produced" | the campaign | Public proof and inbound interest are outcomes of a campaign. |
| Market need (from a signal) | Capability | "matches," with CAP id and extract | the dossier or brief | The first link in the AD-31 chain. |
| Account | Opportunity | "opened" | the opportunity | An opportunity without an account is a research artifact. |
| Opportunity | Capability, Goal, Asset | "fits," "serves," "could reuse" | the opportunity | This is the goal-relative reading the doctrine gives Portfolio: fit against the whole, not against a keyword. |
| Opportunity | Engagement | "became" | the engagement | Won, lost, declined, and expired are outcomes of an opportunity. |
| Engagement | Outcome, Revenue, Proof, Relationship, Asset | "produced" | the engagement | The economic loop in one row: work makes money, proof, access, and reusable material. |
| Relationship | Account, Opportunity, Outcome | "at," "warmed," "referred" | the relationship record | Access is a compounding input the working spec names. |
| Scenario | Lab capability, Experiment | "tests," "produced" | the scenario | Scenarios test portability. They never decide whether a capability should exist (AD-32). |
| Experiment | Belief, Capability, Build | "changed," "supported," "weakened" | the report | Lab experiments already do this well. Commercial experiments do not exist yet. |
| Option | Goal, Capability, Product | "keeps open," "exercised into" | the option record | Optionality and its cost are two of the eight compounding questions. |
| Outcome | the move that caused it | "resulted from" | the outcome | Without this link Learning has nothing to learn from. |

**Concentration is a reading, not a relation.** How much revenue rests on one account, how much proof rests on one engagement, how much of the active offer rests on one capability. Scripts count it from the relations above. Portfolio Intelligence judges whether it is a risk.

---

## 4. The Shared Intelligence domains that understand the Portfolio

The doctrine names ten intelligences inside Shared Intelligence (section 7 of the revised file). This section says what each one reads in the Portfolio, what it produces, and what its nearest thing in the lab is today. An intelligence is not a store. It is a standing, reasoned, current understanding of one kind of thing, with its own provenance and marks. It reads its objects through Retrieval and Context, it writes only proposals, and State commits what is material under Authority.

**What must exist for each one (architectural necessity).** A question the system can answer for that kind of thing, an object or objects it reads, and somewhere its durable conclusions land. **What its first form can be (implementation).** One reasoning pass on demand, over the existing sources, through the Retrieval and Context capabilities that already exist. No intelligence needs a system of its own.

| Intelligence | The question it answers | Reads (objects) | Canonical sources today | What it produces | Nearest thing today (observed) |
|---|---|---|---|---|---|
| **Market** | What is changing out there, and what does it mean for his positioning and offer | signals (evidence), audience, positioning canon | routine outputs (105 historical briefs; 0 live routines), positioning and messaging canon | a current read of the market with observed/inferred marks; a list of what changed that matters | The 2026-09-12 hand test: reading one week of briefs with the lab in view produced three concrete moves the blind routine did not. That is Market Intelligence run once by hand. |
| **Account** | What a named company needs, has said, has been told, and where we stand | accounts, engagements, relationships at that account, opportunities there | `targets/` dossiers, committee files, verdicts (idle since 2026-09-04); client history in the warehouse | a current read per account, with what is owed and what changed | Eleven dossiers, each a one-time snapshot. Nothing updates one when a posting changes. |
| **Audience** | Who the public work is for, what they read, what moves them | audience canon, campaigns, public outcomes | `audience/` (ICP v3 canon), buyer-term report ("zero buyer language for his differentiators") | which audience a piece serves and how it landed | Canon exists. No outcome has ever been read back into it because nothing is public. |
| **Campaign** | What a run of public work is trying to do and how it is going | campaigns, assets, expressions, outcomes | none (no campaign object) | progress of a public aim, judged by what it produced | The one article at gate 2 and ruling D-110 (Substack first). One campaign of one, unnamed. |
| **Capability** | What he and the lab can now reliably do, how strong the proof is, what is emerging | capabilities, proof, builds, engagements | career model (canonical spine, authoritative; matches cite CAP id and extract; nothing writes back into it) | which capability a need matches, with extract and grade; which one is emerging from recent work; what the model could not answer | Retrieval test T5 passes (a posting to CAP-001 with extract and a stated gap). That is Capability Intelligence in its smallest form. Seven declared readers; none has returned a fact. |
| **Product / build** | What is being built, where it stands, what it depends on, what it evidences | builds, experiments, capabilities | each repo's status file; the capability map for the lab's own builds | one current picture of every build, with status by evidence | Telegraph+ STATUS.md says "live line"; no commit since a disk sweep on 2026-09-10; two items needing him for ten days. The lab's own capabilities are the best-tracked builds in the Portfolio. |
| **Asset / IP** | What is reusable, where it has been used, what it is worth, what is duplicated | assets, seeds, expressions, proof | assets registry (6 entries); asset audit (40 works, graded, unregistered); seedbank (825, canonical) | what to reuse, extend, or retire; what is being built twice | The `asset-corpus-match` skill returns one disposition (reuse, customize, extend, merge, build, ignore). That is Asset Intelligence at the moment of proposal, and it exists. |
| **Relationship** | Who matters, what has passed between you, what is owed | relationships, accounts, outcomes | `targets/_people/` (5); the spreadsheet; the unread message export | who to contact, why now, and what you owe them | Nothing runs. The cheapest unopened store in the estate (G-03) is the raw material. |
| **Opportunity** | What is open, what it fits, what it would cost, what it would leave behind | opportunities, accounts, capabilities, goals, assets | none (no object); verdicts "engage" (11), the dead map, the three hand-test moves | an opportunity read against the whole Portfolio, not a keyword; a recommendation or silence | The hand test's three moves are the only opportunities written down with lab context in view. None ruled on. |
| **Portfolio (Portfolio Intelligence)** | How all of the above compounds against the goals: what is reused, growing, concentrated, unused, duplicated, drifting; what tomorrow's starting position is | every object above, read through the nine intelligences, against goals | goals (the drivers file), State (the current condition of everything), all of the above | the compounding lens on a move (eight questions); the standing reading of the whole (reuse, concentration, optionality, drift); named loops ("these six activities are one loop") | None. The four drivers each carry a dated state line and a threat list, read by the open routine. That is the seed of it: a goal, its evidence, its threats, its next change. |

**Portfolio Intelligence is synthesis, not a system above the nine.** It asks one more question with all nine in view: what does this add up to, against the goals. It has no store of its own, no objects of its own beyond goals (which Portfolio the Product holds), and no pass over the others. When it says "reuse," Asset Intelligence supplied the count. When it says "concentration," Account Intelligence and revenue supplied the shares. When it says "drift," the goal's own evidence-of-progress line and State's record of recent moves supplied the facts. It contributes the reading; the Product Portfolio holds the judgment (doctrine section 6).

**What every intelligence never does.** It never commits truth (State does, under Authority). It never edits a canonical model (AD-31). It never widens a permission (Authority). It never turns repetition into fact (Learning's limit). It never carries a client's name across a scope boundary (Operating Scope contract).

---

## 5. The operating loops

Six loops. Each one is the smallest loop through which one part of the Portfolio changes and compounds. Every loop ends in an outcome and a write-back, which is why the empty outcomes folder is the first thing to fix. Each loop names the Product with primary responsibility at each step, per the doctrine, and is tested against the four criteria.

### Loop 1. The move: read each move against goals before it is taken

**Trigger.** A move is about to be chosen: the one prepared next action in the morning brief, a session's first task, a reply to be sent, a build to start.

**Steps.** Process picks the candidate move from conditions. Portfolio Intelligence reads it through the compounding lens: immediate progress, reuse, capability growth, evidence, access, optionality, future cost, reversibility. Portfolio (the Product) judges: this move, a narrower one, or a different one. Trust says how strong the reading is. Experience shows him only the judgment and the one line of why. State records the move and what it was for.

**Objects touched.** Goal (read), the object the move creates or changes (build, asset, opportunity, engagement), Outcome (opened).

**Stays a script.** Reuse counts. Goal state changes only by his word. The record of the move.

**His.** The move itself when it is external or irreversible; any change to a goal.

**Today.** The morning brief with one prepared next action is the first proving loop (AD-30). It picks by urgency and follow-up age. It does not read the move against goals or ask what it leaves behind. The State package is built; the brief is not yet wired to it (open commitment).

**Four criteria.** (1) Redesigned: from "what is oldest and open" to "what advances a goal and leaves something behind." (2) AI in the core: judging which goal a move serves and what it strengthens or duplicates is interpretation. (3) Remove AI: the brief goes back to a sorted list of follow-ups, and the compounding question goes back to a monthly review he runs himself. (4) New way of working: the compounding question asked at every move, not at the end of a project. Passes.

### Loop 2. The market: a change out there becomes an opportunity, or silence

**Trigger.** A signal lands (a brief, a posting, a news item, a competitor move, a regulation), or a target's condition changes.

**Steps.** Noticing sees the change and applies the seven-question threshold; default silence. Market or Account Intelligence says what changed and what it connects to. Capability Intelligence matches the need to a capability, with CAP id and extract, and states what the model cannot answer. Opportunity Intelligence reads fit against goals, assets, and cost. Portfolio judges whether it compounds or concentrates. Trust marks the read (observed, inferred). Experience shows: what changed, what it fits, needs you or not. Process opens an opportunity or reroutes work already open. State records the opportunity and its dependents.

**Objects touched.** Account, Opportunity (created), Capability (read), Goal (read), Relationship (read for a warm path).

**Stays a script.** Which routines ran; which briefs were pulled; freshness; scope refusal (a personal or client-confidential source never feeds a public read).

**His.** Whether to pursue. Registering a new source of signals (AD-21).

**Today.** Signals are gathered by cloud routines that are documented as 28 and alive as 2, that cannot open web pages, and whose output nothing in the lab reads. "No signal has ever reached action." The hand test of 2026-09-12 ran this loop once by hand with the lab in view and wrote three moves. The ruling on the routines has been open since 2026-09-11.

**Four criteria.** (1) Redesigned: from gather-then-reason-blind-then-stop at a page nobody reads, to gather, then reason in the lab with capabilities, goals, and accounts in view. (2) AI in the core: matching a market need to a capability by meaning, and judging fit against the whole Portfolio. (3) Remove AI: a keyword match against postings, where the broadest capabilities always win (the one demand run put a generic translation capability on top) and his differentiators never match because buyers do not use his words. A person would read every brief by hand. (4) New way of working: opportunities noticed against what he can prove, not against what he is called. Passes.

### Loop 3. The commercial loop: opportunity, engagement, outcome, and what it leaves behind

**Trigger.** An opportunity is pursued: an approach is sent, a conversation starts, a proposal is asked for.

**Steps.** Process moves the work through the stages the engagement needs, not a fixed sequence. Account and Relationship Intelligence keep what has been said and what is owed. Capability Intelligence supplies proof at the grade the claim needs (documented, demonstrated, or higher). Trust sets how strong a claim may be at each consequence (a public number never stands without its receipt). Authority holds the line: nothing external without his word. At the end, the engagement produces outcome, revenue, proof, relationship, and reusable material, each recorded on the engagement. Portfolio reads what it left behind and whether concentration rose. Learning keeps what repeated.

**Objects touched.** Opportunity (closed as won, lost, declined), Engagement (created), Outcome, Revenue, Proof (graded), Relationship, Asset (if something reusable came out).

**Stays a script.** Nothing external without approval. Confidentiality: client names stay in scope. Proof-grade rules (a claim cannot reach "demonstrated" without an artifact). Counts of reuse and concentration.

**His.** Every approach, proposal, and price. Opening the contracts store and the message export (proof gaps G-02, G-03).

**Today.** Approaches sent: 0. Outcomes folder: empty. One engagement in the new era is on record, in the career model as a dated fact and in the asset audit as the only proof with a path to Tier 3. Revenue, hours, and pipeline: not in the lab.

**Four criteria.** (1) Redesigned: from a pipeline nobody built ("the pipeline it needed was never built," 2026-09-11 scan) to an engagement that carries its own proof, relationship, and reuse from the first conversation. (2) AI in the core: choosing which proof fits which buyer at which grade; reading what an engagement left behind; noticing that two engagements are one reusable method. (3) Remove AI: a CRM with stages and a proposal template. Proof is copied by hand from a spreadsheet; reuse is noticed months later, if ever. That is a fundamentally different, and familiar, process. (4) New way of working: the economic loop (work, retained capital, proof, access, new paid use) run as one loop with each pass recorded. Passes.

### Loop 4. The public loop: work becomes an asset, an expression, a campaign, and public proof

**Trigger.** Private work reveals something with public value (the `public-value-opportunity` gate), or a seed is ready, or a campaign aim is set.

**Steps.** Asset Intelligence checks the corpus first (reuse, extend, or build). Audience Intelligence says who it is for. Process runs the chain by condition: brief, experience design, build, QA, claim verification, distribution, expression. Trust holds every claim to its receipt; the never-cite list binds. Authority: nothing publishes without his word. Campaign Intelligence tracks the aim across pieces. After publication, outcomes come back (readers, replies, inbound), and Portfolio reads what the piece added to proof, positioning, and access.

**Objects touched.** Seed (read), Asset (created or reused), Expression, Campaign, Audience (read), Proof (public, graded), Outcome, Opportunity (inbound).

**Stays a script.** Claim ledgers. The never-cite list. Publish only under his word. Counting what a piece cited and what it produced.

**His.** Every ruling in the chain; publication; the takedown of the two LinkedIn claims still open since 2026-09-10.

**Today.** The chain exists (nine skills) and ran once; both products were archived at his word. One article is at gate 2, waiting on him since 2026-09-08. Nothing is public. The site is built twice and deployed never. Last public post 2025-11-13.

**Four criteria.** (1) Redesigned: from "write a post" to "express an asset for an audience inside a campaign, with every claim receipted, and read what came back." (2) AI in the core: judging whether private work holds public value; matching an asset to an audience; verifying claims against the lab's own evidence; reading outcomes back into audience and positioning. (3) Remove AI: a content calendar and a manual fact check, or no publishing at all, which is the observed state since 2025-11-13. (4) New way of working: one asset expressed many ways, each expression traced to its receipts, and public proof feeding the commercial loop. Passes.

### Loop 5. The capability loop: work produces evidence, and the spine grows by his word

**Trigger.** A build ships, an engagement closes, an experiment is read, a piece is published. Anything that is evidence of a capability exercised, a new one emerging, or an old one going dormant.

**Steps.** Capability Intelligence reads the new evidence against the model: which capability it strengthens, which grade it reaches, whether it is a combination the model does not hold, whether it is something new. It writes the match where the work happened, with CAP id and extract (ruling 038). It proposes an amendment (a new capability, a maturity change, a product link) as a dated proposal. Trust marks it inferred. Authority: only his ruling changes the model. On his word, the model is amended through its own update path and views regenerate. Portfolio reads the change: what is emerging, what is dormant, where the active offer now rests.

**Objects touched.** Proof (created, graded), Capability (proposed amendment), Product / build (linked), Engagement or Asset (the evidence carrier).

**Stays a script.** Nothing writes into the model on its own. The never-cite list. Pointer resolution (20 of 22 artifact paths do not resolve today). The hub check.

**His.** Every amendment. The two pending since 2026-09-02 (a signal-intelligence capability; market-term additions).

**Today.** The model is frozen at 2026-08-31. Seven readers are declared; one has run once; none has returned a fact. Since ruling 038, no dossier, brief, seed, or report outside the retrieval tests cites a capability id. The graph is one edge behind its source file. No generator for the views exists in the folder.

**Four criteria.** (1) Redesigned: from a model built once in a day and left, to a spine that grows from every piece of work through proposals he rules on. (2) AI in the core: reading new work for which capability it evidences, at what grade, and whether it is a combination nothing has named. (3) Remove AI: a person rereads the corpus by hand every few months and re-runs the one-day build. That is the process that produced the model, and it has not run since. (4) New way of working: the model stays canonical and still current, because use feeds it and his word gates it. Passes, with the guardrail intact: the model is never rewritten by inference.

### Loop 6. The portfolio reading: what is compounding, what is costing, what has drifted

**Trigger.** Standing (Noticing runs it across everything), plus on return after time away, plus when he asks "what is this adding up to."

**Steps.** Portfolio Intelligence reads the whole through the nine: what is being built repeatedly; what became reusable; what evidence is accumulating; what is becoming a product; what capability is emerging; what is duplicated or no longer worth keeping; where value is concentrated; which options are open and which quietly expired; where recent moves no longer match a stated goal. Portfolio judges and names it: "these six activities are one loop," "this goal has had no meaningful attention in three weeks," "the active offer rests on one engagement's proof." Trust marks each claim (an asset "reused" is observed; "reusable" is inferred). Experience makes it a moment of its own, and only when the threshold is met. His accept, reject, or goal change is the write-back. Learning keeps what he confirmed.

**Objects touched.** Every object, read. Goal (drift proposed, never changed by the system). Option (expiry noticed). Asset (duplication, underuse).

**Stays a script.** Every count: reuse, concentration shares, age since last attention, duplicated files, dead pointers. Goal state by his word only.

**His.** Whether drift is real ("Is that intentional?" is the only question the system may ask). Retiring or replacing a driver.

**Today.** The open routine reads four drivers with dated state lines and threat lists. That is the smallest form of this loop, run daily, over goals only. Nothing reads the assets, builds, accounts, or proof as a whole. The cultivator ran once over the seedbank and proposed; nothing was ruled.

**Four criteria.** (1) Redesigned: from a catalog and a monthly review to a standing reading against goals. (2) AI in the core: seeing loops, drift, duplication, and concentration as meaning, not as counts. (3) Remove AI: the counts still print on the facts sheet, and he reads them tired at 2 a.m. and decides what they mean. That is today. (4) New way of working: the Portfolio is forward-looking; tomorrow's starting position is visible today. Passes.

**Why six and not fewer.** Loops 2, 3, and 4 are the three ways value enters (market, paid work, public work). Loop 5 is how the spine learns from all three. Loop 1 is the question asked at every move. Loop 6 is the question asked over the whole. Remove any one and a kind of compounding has no path. **Why six and not more.** Learning and Noticing are cross-cutting behaviors, not loops of their own (doctrine section 8). Scenarios test loops; they are not a loop. Relationships and audiences change inside loops 2, 3, and 4; they do not need one of their own for eight months.

---

## 6. The current lab mapped to the target

Every current thing named in the four briefs of 2026-09-14, placed against the target. Verdicts: **connect** (exists, needs linking), **weak** (exists, thin or stale), **duplicated**, **legacy** (kept as record, not used), **obsolete** (should retire, by his word), **missing**.

| Current thing (observed) | Target place | Verdict | What the gap is, in one line |
|---|---|---|---|
| Career model, `work-os/brand-os/model/` (92 CAP, frozen 2026-08-31) | Capability object, canonical spine; read by Capability Intelligence; loop 5 | connect | Nothing points at it by id from the work; two amendments pending; no combination relation; artifact paths dead on this machine. |
| Desktop copy of the model and the iMac snapshot | none | legacy | Registered replica and historical. Two live files still point at the Desktop paths (the weekly instrument, one demand output). |
| Lab capability map (9 entries) and definitions | Product / build (the lab's own builds), Capability (lab-system, kept separate from CAP ids) | connect | The best-tracked builds in the Portfolio. Not linked to goals. |
| Retrieval (live), State v0.1 (implemented), drivers (live), authority, evidence-record, measurement | the shared capabilities every intelligence and loop runs on | connect | These are the machinery. Retrieval's meaning-match limitation (T2) matters most to loop 2, which needs meaning across sources. |
| Context assembly (planned; three decisions waiting) | the way each intelligence gets its slice | weak | Every intelligence in section 4 is, in its first form, a Context contract plus a reasoning pass. Context is the gating build. |
| Scheduled routines (28 documented, 2 alive, half-blind) | signal gathering for loop 2 | weak, and the ruling is his | Gathering is real; reasoning in the lab with retrieval in view is the redesign. The duplicate whole-market brief review was due this week. |
| Signal briefs on disk (105 backfilled) | evidence for Market Intelligence | legacy as data | Useful as a corpus; not a live sensor. |
| Hand test of 2026-09-12 (three moves) | loop 2 run once by hand | connect | The three moves are the only opportunities with lab context in view. Unruled. |
| Targets: 15 companies, 11 dossiers, verdicts append-only, idle since 2026-09-04 | Account object; Account Intelligence; loop 2 and 3 | connect | Right shape. No capability ids except one "near" match; roster stale (12 listed, 15 verdicts); nothing refreshes a dossier. |
| Target skills: dossier, committee, target-scan | Account Intelligence's hands | weak | Collector unbuilt; skills use a separate gap vocabulary; return path to the model never used. |
| `targets/_people/` (5), relationship spreadsheet (2026-09-02), LinkedIn export (3,156 messages, unread) | Relationship object | missing as an object; legacy as data | The cheapest unopened store. Opening it is his ruling. |
| 2026-08-26 opportunity map | Opportunity object | legacy | Dead since written; no CAP ids; weaker claim hygiene; one ex-client excluded by ruling. Retirement is in an open follow-up. |
| Public-value opportunities PVO-001 to 004 | Opportunity (public sense) | weak, duplicated in name | All "advance" while two of their assets are archived. Same word as commercial opportunity, different thing; the Portfolio should name them apart. |
| Assets registry, 6 entries | Asset object, canonical | connect | Two entries disagree with themselves (archived, prose says candidate). No capability link. |
| Asset audit (2026-08-27 to 09-10): 40 works, 8 instruments, claim-to-proof matrix, proof gaps, public-ready shortlist | Proof object, the only graded proof; Asset Intelligence's corpus | weak, unregistered | In no register location. Read by two files, no script. Its shortlist says two assets are "on the website now"; the site is not deployed. |
| Publishing chain, nine skills; `distribution/` empty | loop 4 | connect | Machinery exists; ran once; killed both products. Waits on public work, not on building. |
| Article at gate 2 since 2026-09-08 | loop 4's first live run | weak, on him | Six days at gate 2. |
| Public site, built twice, deployed never; last public post 2025-11-13 | public proof (outcome of loop 4) | weak | Two undeployed builds, one domain, no deploy record. |
| Positioning canon, audience ICP v3, messaging house | Audience object; Market and Audience Intelligence | connect | Canon. Fine. |
| Weekly buyer-language instrument (`audience/weekly/run.sh`) | Market Intelligence measure | obsolete | Points at a folder that no longer exists; one run; broadest capabilities win any word match. Retire or repoint is his open follow-up. |
| Buyer-term crosswalk (53 postings, frozen) | Capability Intelligence input | legacy | Done once; its "market-term additions" amendment is pending in the model. |
| Seedbank, 825 files, canonical | Seed (pre-asset); input to Asset Intelligence; loop 4 | connect | Capture runs; tending does not; six totals on record; five status vocabularies for ideas across the lab; 0 seeds cite a CAP id. |
| Cultivator agent, INDEX.md, cultivation pass | Asset Intelligence over seeds | weak | Ran once; proposals never ruled; hard-coded counts. |
| ARCHIE (two runs, idle since 2026-09-04) | loop 4's research step; a reader of the model that has never returned a fact | weak | Topic pick waiting on him. |
| Concept shelf (`memory/concepts.md`) | settled wording; contextual | connect | Fine. Header cites a retired skill. |
| Point-of-view library (draft) | beliefs; input to Capability and Portfolio Intelligence | weak | Draft until he reviews. |
| Telegraph+ (`work-os/projects/telegraph-plus/`) | Product / build; the current product objective (driver 3) | weak | No product work since 2026-09-05; two items needing him for ten days; whether the private package governs it is unruled since 2026-09-07. Not linked to any capability id. |
| Two superseded Telegraph predecessors | none | legacy | Correctly frozen and labeled. |
| `upskill-advisor/` private package (governance, gates, records, research) | Engagement and Experiment records for the Telegraph line | connect | Only `records/` is registered. |
| worthy-tool-v2, decision-foundry | Product / build, parked | weak | Nothing current names either; decision-foundry says "No product exists." The audit's D-01 integrity caveat is about worthy-tool's shipped form. |
| `ai-job-search` fork | none | legacy, vendored | Zero mentions anywhere. |
| Empty folders `work-os/references/`, `work-os/skills/`, `work-os/_archive/` | none | obsolete | Created 2026-09-09; nothing points at them; `_archive/` inside the lab breaks the warehouse rule. |
| `engagement-os/PLAN.md` (rolling plan, last done item 2026-08-23), `WORKFLOW.md` | none | legacy | Queue rows duplicate what seed-capture and the concept shelf now do. |
| `engagement-os/outcomes/` (empty) | Outcome object | missing | The folder was reserved for exactly this and has never received a line. |
| Contracts store (2019 to 2022 receipts, unopened), income, hours, runway | Engagement and Revenue objects | missing on purpose | His ruling to open; his input to supply; never leaves its scope. |
| "Use Case Registry" (named, no file); State test S5 synthetic | Scenario object | missing by design | Thin register when repeated scenario work justifies it. |
| `docs/reports/` (13 dated reports), frozen test files | Experiment object (lab) | connect | Well recorded. The only kind of experiment the lab records. |
| Drivers file, four current drivers | Goal object | connect | Goals in all but name. Add contract fields only where a loop needs them. His cap of four stands. |
| State ledger: 92 to 102 loops, 78 items waiting on him, 7 unanswered questions in the rulings file | State, not Portfolio | connect | The queue is the current condition. Loop 1 should read it against goals instead of by age. |
| Ecosystem specs (nine files, unruled; two Experience versions; State titled as a Product) | design record | duplicated | Two Experience specs, neither marked superseded; the State spec's title conflicts with his ruling. |

**Three patterns across the map.**

- **The inputs exist; the links do not.** Capabilities, prospects, assets, seeds, and positioning are all canonical somewhere. Zero seeds, five people records, and six assets cite a capability id. The Portfolio's missing piece is the relations in section 3, not new stores.
- **The tail of every loop is empty.** Outcomes, engagements, revenue, and opportunities have no home. Nothing sent, nothing published, nothing recorded as a result. That is why nothing compounds.
- **The gathering side is over-built and the reasoning side is hand-run.** Twenty-eight routines on paper, nine publishing skills, a nine-stage chain; one hand test, one demand run, one retrieval test. The redesign is to move reasoning into the lab with retrieval and goals in view, which is what the operating model already says.

---

## 7. Verification: the seven checks from the goal

1. **One primary responsibility or canonical source per object.** Section 2 names one home for eleven of fifteen objects and says "missing" plainly for the four that have none (opportunity, relationship as an object, engagement, outcome) and "missing on purpose" for revenue and scenario. No object is given two homes. Where two files hold the same thing today (the model and its Desktop copy; the asset registry and the audit's forty works; two Experience specs), one is named canonical and the other a replica, an input, or a duplicate to resolve.
2. **No durable responsibility duplicated across systems.** Capabilities: the career model only; the lab capability map holds lab-system capabilities with different ids (AD-04). Proof: graded by the audit's ladder, carried on the object, stored in evidence-record. Goals: the drivers file only. Ideas: the seedbank only. Current work condition: State only. Signals: evidence, never an object. The one duplication found is a naming clash, "opportunity" for both a commercial opening and a public-value gate; section 6 says to name them apart.
3. **Ten intelligences distinguished.** Section 4 gives each of Market, Account, Audience, Campaign, Capability, Product / Build, Asset / IP, Relationship, Opportunity, and Portfolio its own question, its own objects, its own sources, and its nearest thing today. No two answer the same question.
4. **Portfolio Intelligence is synthesis.** Section 4 states it: one more question with the nine in view, no store of its own, no objects of its own beyond goals (which the Product holds), no pass over the others. Every reading it makes names which intelligence supplied the facts.
5. **Each loop passes all four criteria and says what fails without AI.** Section 5, each loop: the criteria are answered one by one, and criterion 3 names the non-AI process that would take over (a sorted follow-up list; a keyword match against postings; a CRM with stages; a content calendar or no publishing; a one-day rebuild by hand every few months; counts read tired at 2 a.m.).
6. **The map accounts for the named things.** Section 6 places the career model, the seedbank, products and builds (Telegraph+, worthy-tool-v2, decision-foundry, the site, the lab's own capabilities), signals (routines, briefs, hand test), scenarios (the named registry, S5), opportunities (map, PVOs, verdicts, hand-test moves), relationships (people records, spreadsheet, export), public proof (site, article, chain, audit shortlist, LinkedIn claims), and every registered lab capability.
7. **Next, wait, and the simplest move** are in section 8, and section 8 begins no implementation.

---

## 8. What must happen next, what can wait, and the simplest move

**The simplest useful architectural move.** Rule the object table in section 2. One ruling settles fifteen homes: eleven confirmed where they are, four declared missing with a named first form, two declared private or deferred. No code, no folder, no schema. After it, every session knows where a relation is written (section 3's rule), and the first implementation slice has a target.

**Must happen next, in this order (proposed).**

1. **His ruling on this file and the doctrine together**, since this file cannot be ruled under an unruled doctrine. The doctrine's section 15 already carries his four boundary decisions; the whole waits on his word.
2. **Fill the tail: outcomes and opportunities as records, at one line each.** The outcomes folder was reserved and is empty. Loop 3 and loop 2 have no end without it. First form: one dated line per outcome, linked to the move and the object it changed, written at close through the existing receipt path. That is an implementation choice under AD-33: operational spec, one goal, one review. Not begun here.
3. **Wire loop 1 into the morning brief that AD-30 already names**, so the one prepared next action is read against the drivers, not by follow-up age. The State package exists; the wiring commitment is open. This is where the compounding lens first runs on a real move.

**Can wait, and why.**

- **Campaign** as an object: until a second public piece exists. Ruling D-110 already says publish before building the system around it.
- **Scenario** register: until repeated scenario work justifies it (roadmap section 17). S5 stays synthetic.
- **Relationship** as an object: until he rules on opening the message export (G-03). The five people records and the spreadsheet are enough to start loop 3 for one account.
- **Revenue**: his input, in his time, in its scope. The architecture holds a place; nothing builds it.
- **Product / build register**: the capability map already tracks the lab's builds. The three external builds can each carry one status line where they live until a list is needed.
- **Capability-to-capability relations** in the model: the four combinations in doc 14 are enough for loop 2 to cite by hand for now. An amendment is his word.

**What not to build, restated for the Portfolio.** No universal Portfolio database or registry (the roadmap's "do not build" list stands). No new agent per intelligence. No scoring: no compounding score, no opportunity score. No second career model. No second Retrieval or State. No dashboard before loop 1 and loop 3 have each run once for real.

---

## 9. Attacks on this design, and what survived

- **"Fifteen objects is not the smallest model."** Tried twelve: fold engagement into account, option into experiment, campaign into asset. Each fold lost a loop's tail: without engagement, revenue and proof have nowhere to hang; without option, optionality cannot be read; without campaign, public outcomes attach to nothing once there are two pieces. Fifteen stands, with four of them allowed to stay at one line each for eight months.
- **"The intelligences are ten mini-systems in disguise."** They are not stores and not agents; each is a question plus the existing Retrieval and Context path. The proof that this is enough: retrieval test T5 already is Capability Intelligence in its smallest form, and the hand test already was Market Intelligence run once.
- **"Six loops is too many to build."** None is built here. Loops 1 and 6 already run in a small form (the brief, the drivers). Loops 2, 4, and 5 have machinery waiting on rulings. Only loop 3 has nothing, and that is the gap the outcomes record closes.
- **"This turns the career model into a hub of everything."** It does the opposite: nothing writes into it, every relation is recorded on the other side, and the two amendments pending since 2026-09-02 show the update path is his word and a JSON edit, not a system.
- **"Goals are the drivers, and he ruled drivers are not architecture."** Correct, and kept: the machinery reads whatever goals are current; the four can be replaced without touching it. The goal object is the pattern he already approved (driver, state, evidence, threats, next change), not a new thing.

---

## 10. Three points that wait on his word

1. **The object table (section 2) as the ruling on homes.** Especially the four declared missing: opportunity, relationship, engagement, outcome. If he wants any of them folded into an existing object, one row changes and one loop loses its tail; this file would say which.
2. **Goals as the drivers file, with fields added only where a loop needs them.** The alternative is a separate goal record with the working spec's full contract. This file recommends against it: four drivers with the pattern he approved on 2026-09-08 are enough for eight months.
3. **Opportunity's two senses.** Commercial opportunity (an account that could pay) and public-value opportunity (private work that could go public, PVO-001 to 004) share a word. This file treats the second as a gate inside loop 4, not as an Opportunity object. If he wants one object for both, section 4's Opportunity Intelligence widens and nothing else changes.

Nothing here proposes a schema, an agent, a folder, a UI, or code. Those follow the existing method: operational spec, one goal, one review (AD-33).

---

## 11. Source basis

Governing: `2026-09-14--ai-lab-product-ecosystem-design-doctrine.md` as revised after his review (section 15 of that file; the copy attached to the goal was the first draft, whose four-part test wording differs). Narrowed: `2026-09-13--portfolio-as-the-product-spec-v0-1.md` (sections 3, 8 to 18, 35, 36, 41). Sequence: `2026-09-13--ai-lab-product-ecosystem-roadmap.md` (2.5, 7, 16, 17, 22, 24). Architecture: `docs/architecture/ARCHITECTURE-DECISIONS.md` (AD-01 to AD-37, especially AD-25, AD-27, AD-28, AD-31, AD-32, AD-33), `CAPABILITY-MAP.md`, `CAPABILITY-DEFINITIONS.md` (the Operating Scope contract; retrieval; State v0.1; Context v0.1), `LAB-OPERATING-MODEL.md`. Evidence, all dated 2026-09-14 in `docs/research/assessments/`: the career-model handoff; the market, opportunity, and public-proof brief; the products, builds, and open-loops brief; the seedbank brief. Goals: `context/intent/STANDING.md`. Where a spec and a later ruling disagree, the ruling governs.
