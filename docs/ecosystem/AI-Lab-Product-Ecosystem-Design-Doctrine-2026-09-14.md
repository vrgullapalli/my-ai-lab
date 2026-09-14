---
name: ai-lab-product-ecosystem-design-doctrine
what: The five Products of the AI Lab (Process, Context, Trust, Experience, Portfolio), each with one promise, how each changes the other four, the connective intelligence layer (Shared Intelligence), the two supporting operating layers (State, Authority), and the two cross-cutting behaviors (Noticing, also called Standing Reasoning, and Learning). Review-ready. Doctrine only. No registries, schemas, agents, folders, or implementation.
status: proposed, 2026-09-14; revised the same day after his review of the first draft. Written from the seven source specs in this folder and the roadmap of 2026-09-13. The boundary decisions in section 15 are his; the doctrine as a whole is not yet ruled.
home: docs/ecosystem/
read_with: AI-Lab-Product-Ecosystem-Roadmap-2026-09-13.md (sequence); the seven operational specs beside this file (detail); docs/architecture/CAPABILITY-DEFINITIONS.md (the capability contracts that make this operational)
tags: proposed · from his words where marked
---

# AI Lab Product Ecosystem: the design doctrine

## 0. What this file settles

The seven specs in this folder overlap on purpose. Each one describes all six layers from its own seat, so five of them claim propagation, role projection, write-back, "trust must change behavior," and human judgment. Read together, they leave three questions open:

1. Which Product holds primary responsibility for each shared behavior, and what the others contribute, so nothing is done twice or by nobody.
2. Whether State and Authority are Products or supports. The State spec is titled as a Product; the roadmap calls it connective tissue.
3. Where noticing change and learning sit, since the Portfolio spec claims anticipation and the roadmap makes it a later phase.

This file answers all three. It keeps the five Products the roadmap names, adds none, merges none, and demotes none. State and Authority are supporting operating layers. Shared Intelligence is the connective intelligence layer the Products draw on and reason with. Noticing (also called Standing Reasoning) and Learning are cross-cutting behaviors that run across, and update, Shared Intelligence and all five Products.

**Boundary language in this file.** Each behavior has one primary responsibility and named contributions from the others. Primary responsibility means: this Product or layer answers for the behavior and its result. A contribution means: this one supplies a part, and the primary one relies on it. Nothing here requires exclusive ownership. A Product reasons its own question; it does not do it alone.

**The AI-native definition used here is Venkat's own.** His words, 2026-09-10: "AI-native is the same process producing a new capability that could not have been produced if AI were removed." And 2026-09-11: "AI-native thinking starts by separating the job from the way we currently do the job."

**The governing question** (AD-01): **What should this become now that AI exists?**

**The canonical four-part AI-native definition.** This is the exact wording, and it is the only definition this file uses:

1. The job or way of working is redesigned.
2. AI is part of the core design.
3. Remove AI and the job or way of working no longer exists as designed; the process or outcome changes materially enough that a human or fundamentally different non-AI process would have to take over.
4. The main value can be a new way of working.

**Who must satisfy it.** Each of the five Products must satisfy all four criteria. Shared Intelligence is read against the same four. State and Authority are supporting operating layers: they are not tested against the definition on their own. Their deterministic parts are intentional support for, and constraint on, the AI-native Products (sections 9, 10, and 13).

**How the six Product checks serve as evidence.** Each Product section below runs six checks. They are evidence for the four criteria, not a replacement definition. Check 1 states the promise. Check 2 is evidence for criterion 1 (the way of working is redesigned). Check 3 is evidence for criterion 2 (AI is part of the core design). Check 4 is evidence for criterion 3 (remove AI and it no longer exists as designed). Check 5 is evidence for criterion 4 (the main value can be a new way of working). Check 6 answers the governing question. A Product passes only if all four criteria hold.

---

## 1. The shape in one page

**Five Products.** Each is a promise to the person using the capability, and one question the system asks at every meaningful transition. None is a platform.

| Product | Primary responsibility | The one question | The promise |
|---|---|---|---|
| **Process** | movement | What should happen next, under these conditions? | Work moves by condition, not by step order, and exceptions stay inside the mechanism. |
| **Context** | meaning | What does this situation mean, and what is the least the job must understand? | The capability behaves as if it is inside the situation, and says when it is not. |
| **Trust** | appropriate reliance | What may be relied on, how strongly, and does the evidence support acting at this consequence? | Reliance and the strength of any claim or action never exceed the evidence, and can shrink. |
| **Experience** | how people understand, use, guide, and influence the capability throughout the work | What should this person see, decide, control, or not have to manage now, and what changes because they acted? | Less coordination, judgment only where it matters, and every decision or correction changes the system. |
| **Portfolio** | compounding | What durable value does this work create, reuse, or put at risk over time, against the goals? | Today's move is judged by tomorrow's starting position. |

**One connective layer and two supporting operating layers.** These are not Products because they make no promise of their own to the person. They make the five promises keepable. State and Authority are not tested against the AI-native definition on their own; their deterministic parts exist to support and constrain the five Products.

| Layer | Role | What it never does |
|---|---|---|
| **Shared Intelligence** | The connective intelligence layer. It holds what the Products need to know about the market, accounts, audiences, campaigns, capabilities, products being built, assets and intellectual property, relationships, opportunities, and the portfolio. Each Product reasons its own question and draws on this layer; the layer connects one Product's judgment to the others. Portfolio Intelligence sits inside it. | It never becomes a sixth Product, an agent per Product, or a store. It is not the single owner of Product reasoning. It never commits truth or expands permission on its own. |
| **State** | The current operating truth every Product reads from and writes to. Current, scoped, with a pointer to why. | It never judges, interprets, or decides. It is not memory and not history. |
| **Authority** | Who or what may decide, act, change State, or widen permission. Holds the grants. Refuses by script where a script can. | It never reasons its way to a wider grant. Learning never touches it. |

**Two cross-cutting behaviors.** Not Products, not layers. They run across all of the above and update it.

| Behavior | What it does | What it never does |
|---|---|---|
| **Noticing (Standing Reasoning)** | Senses change, inside the portfolio or outside it, decides whether it matters to what is active, and prepares the smallest useful response. Default is silence. | It never acts on its own, and never decides the form of an interruption (Experience does). |
| **Learning** | Improves future judgment in every Product and every intelligence in Shared Intelligence, from corrections, overrides, outcomes, repeated friction, and repeated reuse. | It never widens permission, rewrites a goal, turns repetition into truth, or crosses scope. |

**How they hold together.** Process moves the work. State records where it now stands. Context says what that means here. Trust says how much it may be relied on and whether the evidence supports acting at this consequence. Authority says who may act. Experience turns that into the smallest useful moment for the person, and carries their answer back. Portfolio asks what the move is worth over time. Shared Intelligence supplies what each of them needs to know about the market, the account, the audience, the goal, and the rest, and connects one Product's judgment to the others. Noticing watches for change. Learning improves the judgment from what happened.

---

## 2. Process as the Product

**Definition.** The reusable, adaptive way work moves from a need to a defensible outcome. Not a workflow. A standing loop: read the state, evaluate the conditions, pick the next move, act, update the state.

**1. Distinct promise.** Work moves by condition, not by step order. Exceptions, reopenings, and reroutes happen inside the mechanism, never as a manual workaround outside it. Human judgment sits where it changes the outcome, not everywhere.

**2. What changes in the way of working (criterion 1: the way of working is redesigned).** Today a routine is a fixed sequence someone remembers to run (the open routine, a scheduled task, a nine-stage publishing chain). Under this Product, a routine reads current State and decides what this run needs. The same need can take a different path on a different day. A changed dependency reopens earlier work instead of waiting for someone to notice.

**3. Indispensable role (criterion 2: AI is part of the core design).** Deciding the next move when the situation is not one of the listed cases. Recognizing that two exceptions are the same kind. Judging that a changed dependency reopens earlier work, and which work. Seeing, from repeated runs, which steps exist only because of an old constraint.

**4. Removal: what no longer exists if AI is taken out (criterion 3).** The adaptive path. What remains is a flowchart with a human at every fork, which is the first anti-pattern the source spec names: "automating the existing workflow step for step." Reopening becomes something a person has to remember.

**5. New value: the way of working that could not exist before (criterion 4: the main value can be a new way of working).** Work that reroutes itself. Exceptions handled where they happen. The process improving from its own observation of where it stalls, where humans intervene, and what gets overridden.

**6. Become: what it should become now that AI exists (the governing question).** From a written sequence to a standing way of working that reads State and picks the move. In the lab, the first place this shows up is the morning brief: not a summary produced by a fixed script, but a run that decides what today's brief needs from current conditions (AD-30).

**What stays a script, and why that is not the job.** Hard preconditions on a transition (nothing external without his word, nothing deleted). The record of every transition. These refuse or record. They do not pick the move.

**Primary responsibility.** Transitions and their conditions. Designed exception behavior. Reopening and rerouting. The mechanics of a handoff (that the work moved, and to whom). Where in the path a judgment point sits.

**Contributes to, but does not hold.** Who holds the decision at that point (Authority). Whether the evidence supports the move at this consequence (Trust). What the work means to the receiver (Context). How the person sees it (Experience). What the move touches in the market, the account, or the goals (Shared Intelligence).

---

## 3. Context as the Product

**Definition.** The designed way the capability decides what it must understand for this job, assembles the minimum sufficient slice, interprets it within its scope and time, and changes its behavior when that slice is missing or wrong.

**1. Distinct promise.** The capability behaves as if it is inside the situation. It does not ask for what it should already know. It says plainly when it does not know enough.

**2. What changes in the way of working (criterion 1: the way of working is redesigned).** Today context is a fixed file list loaded at the front door, the same for every job, which AD-01 already challenges. Under this Product, context is assembled per job and per moment: each item carries why it is there, its source, its age, its scope, and whether it is fact or interpretation. Missing context is a real state, not something the model papers over.

**3. Indispensable role (criterion 2: AI is part of the core design).** Choosing the slice by meaning, not by folder. Deciding relevance for this job. Resolving which source wins in this situation (the current strategy beats the old workshop note, unless the question is why the decision was made). Telling observed from inferred from assumed. Recognizing that something required is absent.

**4. Removal: what no longer exists if AI is taken out (criterion 3).** Assembly. What remains is either everything (the anti-pattern "give the model everything") or a fixed list. Scope tags can still exist, but nothing applies them situationally. "I do not have enough context to do this reliably" cannot be said.

**5. New value: the way of working that could not exist before (criterion 4: the main value can be a new way of working).** Fewer repeated questions. Fewer lost handoff details. A capability that can decline, narrow, or proceed provisionally on purpose. Context that grows with the work instead of being loaded whole at the start.

**6. Become: what it should become now that AI exists (the governing question).** From a front-door file list to a job-relative package with a reason per item and a named gap list. The job decides the context. The person corrects it, and the correction persists.

**What stays a script.** Scope refusal. Prohibited-source refusal. Pointer resolution. Freshness arithmetic. These keep the assembled package honest. They do not choose what goes in it.

**Primary responsibility.** Relevance and selection. The minimum-sufficient rule. Scope and freshness of meaning. Which sources are authoritative for this question. Carrying the marks that separate fact from interpretation. Reporting sufficiency: present, missing, conflicting, out of scope. What meaning must travel at a handoff.

**Contributes to, but does not hold.** Finding the evidence (Retrieval, a shared capability, live since 2026-09-13). Deciding how much reliance a marked item deserves (Trust). Storing what was decided (State). Showing it (Experience). What the account, audience, or campaign already means to the lab (Shared Intelligence).

---

## 4. Trust as the Product

**Definition.** The way the capability governs appropriate reliance through how it behaves: it preserves what is known, inferred, assumed, and unknown; it lets evidence set how strongly it may claim, and whether the evidence supports acting at this consequence; and it changes its claims and the strength of its actions when conditions change. Trust judges reliance. Authority holds permission. Trust never grants permission; it can only say the evidence does not support using the permission that exists for this move.

**1. Distinct promise.** Reliance, and the strength of any claim or action, never exceed the evidence. Both can shrink. The next move is defensible, and consequential work can be reconstructed later.

**2. What changes in the way of working (criterion 1: the way of working is redesigned).** Today trust is a review step at the end, or a warning that changes nothing. Under this Product, every consequential transition asks whether the evidence supports this action at this consequence. Weak evidence produces "monitor two signals," not "launch imminent." A changed dependency moves an approved thing to "recheck required" without anyone asking.

**3. Indispensable role (criterion 2: AI is part of the core design).** Judging whether the evidence is enough for this consequence, not in general. Interpreting whether a change is material to a prior conclusion. Assigning the marks: observed, inferred, assumed, unknown, disputed, stale. Choosing the smallest defensible next move when certainty is not available.

**4. Removal: what no longer exists if AI is taken out (criterion 3).** Reliance that scales. What remains is a fixed gate, a confidence number with no meaning, or approval for everything, which people stop reading. Reassessment never fires, because nothing reads dependency change for meaning.

**5. New value: the way of working that could not exist before (criterion 4: the main value can be a new way of working).** Action strength that grows and shrinks with evidence, inside a permission that only Authority changes. Trust that travels with the work across a handoff. A record that can be rebuilt because the epistemic state was preserved at the time, not reconstructed afterward.

**6. Become: what it should become now that AI exists (the governing question).** From a gate to a standing condition on every transition. The person stops asking "can I trust this AI" and learns how the capability behaves when it knows, when it does not, when something changes, and when it needs them.

**What stays a script.** Hard refusals (the three minimums, secrets, the root lock). Provenance capture. The rule that nothing carries his word without an anchor. The reconstructable record. These prove; they do not judge sufficiency.

**Primary responsibility.** The meaning of the epistemic marks. The mapping from evidence to permitted strength of claim and action. Reassessment triggers and reversibility. Failure behavior when reliance conditions break. Reconstructability of consequential work. Which trust conditions travel at a handoff.

**Contributes to, but does not hold.** The grant itself (Authority holds it; Trust can say the evidence does not support using it for this move, never widen it). Whether context is present (Context reports that). How a warning is shown (Experience). Whether a change was noticed at all (Noticing). What the evidence is about in the market or the account (Shared Intelligence).

---

## 5. Experience as the Product

**Definition.** How people understand, use, guide, and influence the capability throughout the work. Not only the interaction at one moment. It projects what the capability knows, believes, may rely on, and may do into the smallest useful moment for this person, it gives them the controls their authority allows, and it turns what they do, decide, correct, or teach back into real change in the system, across the whole life of the work.

**1. Distinct promise.** Less coordination. Judgment asked for only where it changes the outcome. Every decision or correction changes the system, and the person can see that it did.

**2. What changes in the way of working (criterion 1: the way of working is redesigned).** Today the person opens a session and reconstructs the situation, or reads a dashboard of system activity. Under this Product, seven questions are answered at every meaningful moment: what they need to understand, what they should not be asked, what changed, what they can rely on, what needs their judgment, what control they have, and what changes because they acted. Return after two weeks reads: current, changed, open, needs you.

**3. Indispensable role (criterion 2: AI is part of the core design).** Deciding what this person needs now and what to leave out. Deciding a change is worth showing and what it affects. Deciding that this item needs their judgment and that one does not. Interpreting what a correction means, so the right thing changes underneath.

**4. Removal: what no longer exists if AI is taken out (criterion 3).** The moment. What remains is a fixed screen per role, every event as a notification, approvals everywhere, and corrections that vanish because nothing interprets them. The person manages the workflow again.

**5. New value: the way of working that could not exist before (criterion 4: the main value can be a new way of working).** A resume view that needs no memory. Interruptions that scale with consequence. Corrections that persist and propagate. A handoff where the next person does not need the previous person's brain.

**6. Become: what it should become now that AI exists (the governing question).** From an interface on top of the capability to the projection of the whole capability, sized to the moment and the role. Claude Code, the brief, an alert, and a future page are surfaces of one experience, not four.

**What stays a script.** Controls appear only under real Authority. Write-back is validated: every id exists, every pointer resolves, no ceiling raised. These keep the moment honest. They do not decide what the moment contains.

**Primary responsibility.** The seven questions. Moments (return, normal, uncertainty, judgment, change, correction, handoff, failure). Surfaces (now, changed, needs you, why, history, control). Role-specific projection, for all Products. The write-back contract: what an interaction means and what it should change. Progressive disclosure. The form of an interruption.

**Contributes to, but does not hold.** Whether something is material enough to interrupt (Noticing). What is true now (State). What may be relied on (Trust). What the person is allowed to do (Authority). What the person's situation connects to in the market, the account, or the goals (Shared Intelligence).

---

## 6. Portfolio as the Product

**Definition.** The compounding layer. It holds the goals as living direction, reads the person's accumulated usable capacity (capabilities, evidence, assets, relationships, products, options, commitments), and judges each move by what it leaves behind and what it costs later.

**1. Distinct promise.** Today's move is judged by tomorrow's starting position. Reuse, emerging capability, and reinforcing loops are named. Negative compounding (maintenance debt, concentration, lost optionality, drift from a stated goal) is named too.

**2. What changes in the way of working (criterion 1: the way of working is redesigned).** Today the career model is a record of what he has done, the seedbank is a store, and "is this compounding" is a question asked by hand at the end of a project, if at all. Under this Product, the compounding question is asked at the move, through the lens: immediate progress, reuse, capability growth, evidence, access, optionality, future cost, reversibility. Goals are objects the system reads against, not headings.

**3. Indispensable role (criterion 2: AI is part of the core design).** Connecting a piece of work to a goal and to the assets it strengthens or duplicates. Recognizing that six activities are one reinforcing loop. Seeing that a good opportunity works against a second goal. Detecting drift between stated goals and recent choices. Reading an opportunity against the whole portfolio, not against a keyword.

**4. Removal: what no longer exists if AI is taken out (criterion 3).** The reading. What remains is a catalog of assets, a list of goals, and a monthly manual review. The research report of 2026-09-13 in fact recommends that manual review for three cycles; that is sequencing, not the design. The design is the standing reading.

**5. New value: the way of working that could not exist before (criterion 4: the main value can be a new way of working).** A forward-looking portfolio. Tensions between goals made visible before the commitment. Reuse noticed at the moment of creation, not rediscovered later. The economic loop the research report names (work, retained capital, proof, access, new paid use) watched as a loop, not as separate activities.

**6. Become: what it should become now that AI exists (the governing question).** From a record of what exists to a standing reading of what is compounding and what is costing, against goals the person still owns. The canonical career model stays canonical; Portfolio reads it and never edits it from inference (AD-31).

**What stays a script.** A goal's state changes only by his word. Canonical models are never rewritten by inference. Counts of reuse and concentration are measured, not estimated. These protect the person's direction. They do not read it.

**Primary responsibility.** Goals as directional objects, their states, and their relationships. The compounding lens, positive and negative. Reuse, concentration, optionality, and drift as judgments. The goal-relative reading of opportunities.

**Contributes to, but does not hold.** Noticing that a change happened (Noticing). Changing a goal (Authority, his). Storing goal state (State). Showing the tension (Experience). The connections between a piece of work, the market, the accounts, the assets, and the goals (Portfolio Intelligence, inside Shared Intelligence).

**Portfolio and Portfolio Intelligence.** The Product is the promise and the lens, and it holds primary responsibility for the compounding judgment. Portfolio Intelligence sits inside Shared Intelligence (AD-31 names it) and supplies the connections that judgment needs: which goal a piece of work serves, which assets it strengthens or duplicates, which market need and which account it ties to, what evidence it adds. They are not two things doing one job: Portfolio judges; Portfolio Intelligence connects. The same relationship holds between each of the other four Products and the intelligences they draw on. It is named here because this is the one already named in a ruling.

---

## 7. Shared Intelligence: the connective intelligence layer

**His phrase.** Taste interview, 2026-09-09: "A shared intelligence layer could've solved that too. Maybe better, because we wouldn't have had to pretend that consistency meant every account had to work exactly the same way."

**Definition.** The connective intelligence layer. It holds what the lab knows, believes, and has learned about the things the five Products reason over, and it connects one Product's judgment to the others. It is not the single owner of Product reasoning. Each Product reasons its own question; Shared Intelligence is what that reasoning draws on and reasons with.

**The intelligences it holds.** Each is a standing, reasoned understanding of one kind of thing, kept current and carrying its own provenance and marks:

| Intelligence | What it understands |
|---|---|
| Market | what is changing in the market and what it means for the lab's positioning |
| Account | what a named company or client needs, has said, and has been told |
| Audience | who the work is for, what they read, and what moves them |
| Campaign | what a run of public work is trying to do and how it is going |
| Capability | what the lab and the person can now reliably do |
| Product / Build | what is being built, where it stands, and what it depends on |
| Asset / IP | what is reusable, where it has been used, and what it is worth |
| Relationship | who matters, what has passed between you, and what is owed |
| Opportunity | what is open, what it fits, and what it would cost |
| Portfolio (Portfolio Intelligence) | how all of the above compounds against the goals (AD-31) |

**How the five Products use it.** A Product asks its own question and reaches into this layer for the parts it needs. Process asks what the next move touches. Context asks what this account or audience already means. Trust asks what the evidence is about, and what else rests on it. Experience asks what this person's situation connects to. Portfolio asks how this move reads against the goals and the accumulated capacity. Each Product keeps primary responsibility for its own judgment. The layer contributes the connections.

**Connecting.** The one job the layer holds as its own: carry the consequence of one Product's judgment to the others. A correction in Experience becomes a Context change, a Trust reassessment, a Process reroute, and possibly a Portfolio insight. This is the ecosystem's "interconnection" made into one responsibility instead of five partial ones.

**What it is not.** Not a sixth Product: it makes no promise to the person that the five do not already make. Not the single owner of Product reasoning: each Product judges its own question. Not an agent per Product. Not a store: it reads State, evidence, memory, and the drivers; it writes only proposals, and State commits them under Authority. Not the sensors: scripts still say what is true. Not Noticing and not Learning: those run across it and update it (section 8).

**Against the four criteria.** Criterion 1, redesigned: from knowledge scattered across files, briefs, and one person's head to one connective layer every Product reasons with. Criterion 2, AI in the core design: holding a reasoned, current understanding of an account, a market, or a portfolio, and connecting one Product's judgment to another, is interpretation; a script cannot do it. Criterion 3, remove AI: each Product reasons alone, with a catalog where the understanding was. A move is picked without knowing which account or goal it touches; Trust judges evidence without knowing what else rests on it; Portfolio reads a list of assets instead of a portfolio. Criterion 4, the main value is a new way of working: five Products that share one understanding of the world, so consistency stops meaning that every account has to work the same way. Passes.

---

## 8. Noticing and Learning: the two cross-cutting behaviors

Neither is a Product, a layer, or a store. Each is a behavior that runs across Shared Intelligence and all five Products, and updates them. They are separated from Shared Intelligence on purpose: the layer holds understanding; these two change it.

**Noticing (Standing Reasoning).** Sense a change inside the portfolio or outside it, connect it to what is active, decide whether it matters, and prepare the smallest useful response. The seven-question threshold from the Portfolio spec applies (goal relevance, magnitude, novelty, actionability, timing, confidence, cost of silence). Default is silence.

- *Why it is cross-cutting.* A changed dependency matters to Process (reopen), Context (stale), Trust (recheck), Experience (show), Portfolio (concentration), and to the intelligence it touches (a new posting updates Account Intelligence, a competitor move updates Market Intelligence). One noticer, many consumers.
- *Primary responsibility.* Deciding that a change is material and what it affects.
- *Contributions.* Shared Intelligence says what the change connects to. Portfolio supplies goal relevance to the threshold. State supplies the dependency record. Experience decides the form of any interruption and the controls. Authority says whether any response may act.
- *What it never does.* Act on its own. Decide how the person sees it.

**Learning.** Improve future judgment from corrections, overrides, outcomes, repeated friction, and repeated reuse.

- *Why it is cross-cutting.* A correction improves the Product that misjudged and the intelligence that was wrong. A repeated override improves Trust's sense of what evidence is enough and Account Intelligence's sense of what that client wants. Learning improves all five Products and every intelligence in Shared Intelligence.
- *Primary responsibility.* Turning what happened into better future judgment, and saying where the change was applied.
- *Contributions.* Experience interprets the correction. Each Product updates its own kind of judgment. Shared Intelligence updates the intelligence involved. State keeps the record. Authority sets the limit.
- *The limit, held by Authority.* Learning never widens permission, never rewrites a goal, never turns repetition into truth, never crosses scope, and never rewrites a canonical model from inference.

**Where they sit in the build.** The roadmap makes Standing Reasoning phase 4 and Learning phase 5. That is sequencing. The design is that both run across everything from the start of whichever phase brings them.

---

## 9. State: the supporting role

**Definition.** The smallest reliable view of what is true now, scoped, with a pointer to why. Process state, decision state, context state, trust state, authority state, object state, issue state, outcome state, goal state.

**Why a support and not a Product.** The State spec is titled as a Product, and its content is a full operating layer. But State makes no promise of its own to the person. Its value appears only through the five: Experience shows it, Process moves from it, Context interprets it, Trust qualifies it, Portfolio reads it over time. The roadmap already calls it "foundational connective tissue," and State v0.1 was built as an implementation slice of continuity, not a new capability (AD-29, AD-37). This file follows that.

**What it does.** Records current truth, separate from history and from memory. Holds proposed state apart from committed state. Records dependencies so a change can find what it affects. Supports "unknown" as a valid state. Carries scope, so a fact is not universal because it is persistent.

**What it never does.** Judge, interpret, or decide. A state that exists is not a state that may be acted on (Trust). AI inference does not become committed State on its own (Authority). State stores only the overlays registries do not own; registries stay canonical (AD-37).

**Not tested against the AI-native definition on its own.** State is a supporting operating layer. It is not required to satisfy the four criteria independently, and this file does not test it. Its deterministic part, the ledger that refuses lines that lie, is intentional support for the five Products: it keeps the truth they read from current and pointed. It is also a constraint on them: no Product commits a line that lacks a pointer, an owner, or a successor. The judgment of what changed enough to record belongs to the Product writing the line, and that Product is the one that satisfies the definition. The capability contract for continuity keeps its own AI test line (CAPABILITY-DEFINITIONS); that is a contract on the implementation, not a doctrine test.

---

## 10. Authority: the supporting role

**Definition.** Who or what may decide, act, change State, or widen permission, for each meaningful move. AI may act, AI may propose, a human must decide, another role or organization must decide, or nobody may proceed.

**Why a support and not a Product.** Authority is a boundary, not a promise. It is what makes Trust's promise honest (reliance never exceeds evidence, because the grant cannot be reasoned wider) and Experience's promise honest (controls match real rights).

**What it does.** Holds the grants. Refuses by script where a script can: the three minimums, secrets, the root lock, no external action without his word. Requires two dated yeses for a new rule. Keeps read authority separate from act authority. Separates proposer, validator, committer, and override where consequence warrants.

**What it never does.** Widen a grant through learning, repetition, or inference. Let technical access stand in for permission. Lose a restriction at a handoff.

**How it meets Trust.** Two questions, two holders, no overlap. Trust answers: what may be relied on, and does the evidence support acting at this consequence? Authority answers: who or what has permission to act? A move goes ahead only when both say yes. Trust can say the evidence does not support using a permission for this move; it never widens the permission. Authority can refuse a move the evidence would support; it never judges the evidence. Only Venkat raises a grant. This is the one place the lab's core rule shows plainly: guardrails say what may not happen; they do not decide what to look at.

**Not tested against the AI-native definition on its own.** Authority is a supporting operating layer. It is not required to satisfy the four criteria independently, and this file does not test it. Its deterministic part, the refusals, is intentional constraint on the five Products: the three minimums, the root lock, no external action without his word, two yeses for a rule. Remove AI and the refusals stay the same, and that is correct here, because a boundary that reasoned its way wider would not be a boundary. What AI adds, naming the rule a move rests on before making it and telling a correction from a rule, belongs to the Product making the move, and that Product is the one that satisfies the definition.

---

## 11. How each Product is changed by the other four

Read a row as "this Product is changed by the column."

| This Product, changed by the column | Process | Context | Trust | Experience | Portfolio |
|---|---|---|---|---|---|
| **Process** | | Different meaning, different path: a market or client change reroutes the work. | Weak or changed evidence narrows, pauses, or reopens the path. | A person's approve, defer, reject, or correct advances, pauses, or redirects the work. | A move that creates future cost or breaks a goal is not the next move, even if it is the nearest one. |
| **Context** | The stage of the work decides what context is needed now; context grows with the process. | | The marks Trust defines are what Context carries; a disputed item changes what the package may claim. | A supplied or corrected item becomes part of the package and persists. | Goals and portfolio relationships are part of what a situation means. |
| **Trust** | A transition's consequence sets how much evidence it needs. | Missing, stale, or wrong-scope context lowers permitted reliance. | | Human validation, override, or outcome is evidence about whether reliance was deserved. | A move with high future cost or high concentration needs stronger evidence before it is "supported." |
| **Experience** | The current stage and available moves are what the person sees as "next." | The assembled package is the content of the moment; the gap list is the "what I do not know" line. | Reliance state sets how strongly something is presented and whether it is blocked. | | Compounding and tension become a moment of their own ("this advances one goal and works against another"). |
| **Portfolio** | Completed and abandoned work are the events the compounding reading is made from. | Portfolio's reading is only as good as the context that says what a piece of work was for. | A compounding claim carries the same marks: an asset "reused" is observed; "reusable" is inferred. | The person's accept, reject, or goal change is the write-back that keeps goals alive. | |

**Two worked traces, with the primary responsibility named at each step.**

*A dependency changes (client strategy replaced).*
Noticing sees the change; Account Intelligence, inside Shared Intelligence, says which work and which goals it touches. State records the new current strategy and finds the dependents. Context marks the old strategy superseded and reassembles for affected jobs. Trust moves the affected recommendations to "reassessment required." Authority narrows any execution permission that rested on the old strategy. Process reopens the two plans that depend on it. Experience shows: what changed, what it affects, what needs you. Portfolio asks whether the concentration on that client just rose.

*The person corrects an assumption.*
Experience interprets the correction (what did they mean). State supersedes the old line and keeps the history. Context carries the corrected item into the next package, and the person is not re-asked. Trust reassesses what rested on the assumption. Process reroutes if the corrected item changes the path. Learning keeps the pattern if it repeats, and updates the intelligence that was wrong; Authority stays exactly where it was. Portfolio records nothing unless the correction changes a goal or an asset's standing.

---

## 12. Boundary check: every contested behavior has one primary responsibility

The seven specs each claim most of these. This table is the resolution. Each row names one primary responsibility and the contributions the others make. If a future document gives one of these a second primary responsibility, that is the conflict to fix.

| Behavior claimed by several specs | Primary responsibility | Named contributions |
|---|---|---|
| "Trust must change behavior" | **Trust** sets the permitted strength of claim and action | Process makes the narrower move; Context reports the condition; Experience shows it |
| Propagation of a change | **Process** reopens and reroutes, using State's dependency record | Context says what meaning must travel; Trust says what conditions travel; Noticing saw it; Shared Intelligence connects it to the work it touches |
| Role-specific projection | **Experience**, for all Products | The others supply content, never their own views |
| Write-back | **Experience** defines what an interaction means | State commits the change; each Product updates its own kind of state; Learning keeps the pattern |
| Interruption | **Noticing (Standing Reasoning)** decides materiality | Shared Intelligence says what the change connects to; Experience decides the form and the controls; Authority says whether any response may act |
| Human judgment | **Process** places it in the path; **Authority** says who; **Trust** says when evidence requires it; **Experience** presents it | Four parts, four owners, no overlap |
| Handoff | **Process** moves the work | Context carries meaning; Trust carries conditions; Authority carries rights; State carries current truth; Experience gives the receiver the resume view |
| Epistemic marks (observed, inferred, assumed, unknown) | **Trust** holds their meaning and consequence | Context applies and carries them; State stores them; Shared Intelligence carries them on every intelligence |
| Exceptions and failure | **Process** holds designed exception paths | Trust holds failure of reliance conditions; Experience holds the failure moment |
| Goals | **Portfolio** holds them | Authority holds changing them (his); State stores their state |
| Anticipation (noticing change) | **Noticing (Standing Reasoning)**, a cross-cutting behavior | Portfolio supplies goal relevance to the threshold; Shared Intelligence supplies the connections; State supplies the dependency record |
| Learning | **Learning**, a cross-cutting behavior, under Authority's limit | Experience interprets the correction; every Product updates its own judgment; Shared Intelligence updates the intelligence involved; none holds Learning itself |
| Sufficiency vs reliance | **Context** reports sufficiency (present, missing, conflicting, out of scope) | **Trust** turns that into permitted reliance at this consequence |
| Product reasoning vs Shared Intelligence | **Each Product** reasons its own question | Shared Intelligence supplies the intelligences (market, account, audience, campaign, capability, product/build, asset/IP, relationship, opportunity, portfolio) and connects one Product's judgment to the others; it is not the single owner of Product reasoning |
| Portfolio vs Portfolio Intelligence | **Portfolio** is the promise, the lens, and the compounding judgment | **Portfolio Intelligence**, inside Shared Intelligence, supplies the connections (AD-31); the same relationship holds for every other Product and its intelligences |
| State vs memory vs history | **State** is what is true now | Memory is what should matter again (a shared capability's job, not defined here); history is the record |
| State vs registries | Registries own durable objects; **State** stores only overlays they do not own | AD-37 |
| Reliance vs permission | **Trust** governs appropriate reliance: what may be relied on, and whether the evidence supports acting at this consequence | **Authority** holds permission: who or what may act. A move needs both. Trust never widens a grant; Authority never judges evidence |
| Evidence | Not a Product and not defined here; Retrieval is a live shared capability | Context selects from it; Trust judges it |

**Result.** No behavior has two primary responsibilities, and no full responsibility is duplicated. Every contribution is named. No Product's promise can be kept by another Product. State and Authority make no promise of their own. Shared Intelligence connects and supplies; it does not hold any Product's reasoning, and it never commits. Noticing and Learning run across everything and hold nothing but their own behavior. Trust and Authority answer two different questions. No boundary conflict is left unresolved. The three open questions in section 0 are answered.

---

## 13. What stays deterministic, and why it is not the adaptive job

The lab's rule: the AI decides what to investigate; scripts decide what is true and what is forbidden. Every deterministic job below is intentional support for, or constraint on, an AI-native Product. It is never the Product. State and Authority are the two layers whose whole design is this support and constraint, which is why they are not tested against the definition on their own. Applied here:

| Script's job | Product or support it guards | Why it is a guardrail or a sensor, not the job |
|---|---|---|
| Hard preconditions on a transition | Process | It refuses a move; it never picks one |
| Scope, prohibited-source, and pointer refusals; freshness arithmetic | Context | It keeps the package honest; it never chooses what goes in |
| Hard refusals; provenance capture; no his-word without an anchor | Trust | It proves; it never judges sufficiency |
| Controls only under real Authority; write-back validation | Experience | It keeps the moment honest; it never decides what the moment contains |
| Goal state by his word only; canonical models never rewritten by inference; reuse counted | Portfolio | It protects direction; it never reads it |
| The three minimums, the root lock, two yeses for a rule | Authority | Refusal is the design; AI names the rule it rests on |
| Ledger integrity: pointers resolve, one owner, one successor | State | It refuses lines that lie; AI judges materiality |

If a script starts choosing the move, the slice, the strength, the moment, or the reading, the design has slid back to a checklist. That is the failure this section exists to name.

---

## 14. Why this is the simplest coherent shape for ~8 months

- **Five promises, one connective intelligence layer, two supporting operating layers, two cross-cutting behaviors.** Nothing else is needed to make the roadmap's phases (Context, morning brief, first UI, standing reasoning, learning, connections) coherent with one another.
- **Each Product is a question asked at a transition, not a system.** The shared capabilities already registered (Context assembly, continuity and State, Authority and Control, Evidence and Retrieval, Coordination, Evaluation) are where implementation goes. This file names none of that and changes none of it.
- **Every contested behavior has one primary responsibility and named contributions.** That is what stops the ecosystem growing into five platforms that each need a propagation engine, a projection layer, and a learning loop.
- **The two placements are already in force.** State as a supporting layer and Standing Reasoning as a later phase are both in the roadmap of 2026-09-13. This file only makes them doctrine.

---

## 15. The boundary decisions, settled in his review of 2026-09-14

The first draft left three points open. His review settled them, and added four wording corrections. All are applied above.

1. **State and Authority are supporting operating layers, not Products.** The State spec is titled as a Product; the doctrine keeps it a layer, as the roadmap does.
2. **Noticing (Standing Reasoning) and Learning are cross-cutting behaviors.** The first draft placed them inside Shared Intelligence. They now run across, and update, Shared Intelligence and all five Products (section 8). Portfolio keeps compounding and goals.
3. **"Shared Intelligence" is the name,** and it is the connective intelligence layer: Market, Account, Audience, Campaign, Capability, Product/Build, Asset/IP, Relationship, Opportunity, and Portfolio Intelligence (section 7). It is not the single owner of Product reasoning.
4. **Wording.** The canonical four-part AI-native definition appears once, in its exact words, in section 0, and every Product check is read as evidence for one of its four criteria. State and Authority are not tested against it on their own; their deterministic parts are support for, and constraint on, the Products. Boundaries use primary responsibility plus named contributions, not exclusive ownership. Trust governs appropriate reliance; Authority holds permission. Experience is how people understand, use, guide, and influence the capability throughout the work, not only the interaction.

The doctrine as a whole is still proposed. It becomes ruled when he says so.

Nothing here proposes a registry entry, a schema, an agent, a folder, or code. Those follow the existing method: operational spec, one goal, one review (AD-33).

---

## 16. Source basis

Written from, in this folder: Process Is the Product; Context as the Product; Trust Is the Product; State as the Product (v2); Experience as the Product (both versions); Portfolio as the Product v0.1; the Product Ecosystem Roadmap of 2026-09-13. Also read: the compounding portfolio research report (2026-09-13), `docs/architecture/CAPABILITY-DEFINITIONS.md`, `docs/architecture/ARCHITECTURE-DECISIONS.md` (AD-01, AD-29 to AD-37), and his words in `docs/about-me/taste-interview--2026-09-09.md` and the possibility brief of 2026-09-11. Where a spec and a later ruling disagree, the ruling governs.
