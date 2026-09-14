# State as the Product
## Operational Specification for AI-Native Commercial Capabilities

## 1. Purpose

Define how an AI-native commercial capability knows, preserves, updates, shares, and expresses **where things stand now**.

State may describe:

- work
- decisions
- assumptions
- assets
- issues
- approvals
- recommendations
- campaigns
- trust conditions
- authority
- outcomes
- dependencies

The goal is not to store everything that happened.

The goal is:

> **Maintain the smallest reliable view of current reality needed for the capability to know what can happen next.**

---

# 2. Core Thesis

> **State is the capability's current operating truth.**

State answers:

- What is true now?
- What has been decided?
- What is still open?
- What changed?
- What is active?
- What is no longer valid?
- What is allowed?
- What is blocked?
- What needs attention?
- What can happen next?

Without state, AI repeatedly reconstructs the situation from history.

With state, the capability can continue the work.

---

# 3. State Is Not Memory

### Memory

> What happened before?

### State

> What is true now?

Example:

**Memory**

> The client approved Strategy A in June.

**State**

> Strategy A was replaced by Strategy B in August. Strategy B is current.

The capability may use history to understand why.

But it should act from current state.

---

# 4. State Is Not a Database

A database stores information.

State identifies:

> **Which current conditions materially affect capability behavior.**

Do not make every fact, document, message, or event first-class state.

Something deserves explicit state when changing it could affect:

- what happens next
- what context applies
- what can be trusted
- who can act
- what a person needs to know

---

# 5. The Six Connected Layers

| Layer | Core question |
|---|---|
| **Process** | How does the work move from need to outcome? |
| **State** | What is true and where does the work stand now? |
| **Context** | What does that state mean here and now? |
| **Trust** | Is this state reliable enough to act on? |
| **Authority** | Who or what may change the state or act from it? |
| **Experience** | What state does each person need to see or act on? |

State is not simply one layer among six.

It acts as a **shared operating record connecting the others**.

---

# 6. State Interconnection Model

The basic loop is:

**Process produces events**  
↓  
**State records what changed**  
↓  
**Context determines what the new state means**  
↓  
**Trust determines how much reliance it deserves**  
↓  
**Authority determines what may happen because of it**  
↓  
**Experience makes the relevant change visible and actionable**  
↓  
**Action returns to Process**  
↓  
**Process produces the next state change**

This continues throughout the life of the capability.

---

# 7. State Interconnection Contract

For every material state, define:

### State

What is currently true?

### Process relationship

What process event created or changed it?

### Context relationship

What context determines its meaning or scope?

### Trust relationship

How reliable is the state, and what evidence supports it?

### Authority relationship

Who or what may establish, change, override, or act from it?

### Experience relationship

Who needs to know about it, when, and how?

### Downstream effects

What other state, process, authority, or experience changes because this state changed?

This contract is the main operational object for State as the Product.

---

# 8. Process ↔ State

## What Process gives State

Process produces events that may change current reality.

Examples:

- analysis completed
- recommendation created
- reviewer approved
- client rejected
- campaign launched
- source updated
- execution failed

Process should not directly overwrite state without checking the relevant transition rules.

## What State gives Process

State tells Process:

- where work currently stands
- which transitions are available
- what has already happened
- what remains unresolved
- what conditions block movement
- whether earlier work must be reopened

## Operational rule

> **Process moves based on state, not merely on step order.**

Example:

**State: Evidence sufficient**
→ Process may create recommendation.

**State: Evidence conflicting**
→ Process routes to investigation.

**State: Recommendation approved + execution authorized**
→ Process may act.

## Required behavior

Every meaningful process transition should specify:

- starting state
- trigger
- required conditions
- resulting state
- exception state

---

# 9. Context ↔ State

## What Context gives State

Context determines what a state actually means.

Example:

State:

> Approved

Context:

> Brand A · US · HCP · Email · current indication

Without context, the state may be dangerously broad.

Context also tells State:

- scope
- applicable market
- role
- client
- audience
- channel
- strategy
- current business conditions

## What State gives Context

State tells Context what situation exists now.

Examples:

- strategy changed
- review reopened
- segmentation superseded
- evidence incomplete
- campaign active

That helps Context decide what information should now be assembled.

## Operational rule

> **State should never be interpreted outside its valid context.**

## Required behavior

When material context changes:

1. identify affected states
2. test whether those states still hold
3. preserve unaffected states
4. invalidate or reopen affected states
5. update downstream context

Example:

Client positioning changes.

State engine identifies:

- 6 recommendations depend on the old positioning
- 4 remain valid
- 2 move to **Reassessment required**

---

# 10. Trust ↔ State

## What Trust gives State

Trust qualifies how much reliance a state deserves.

A state may be:

- proposed
- provisional
- supported
- verified
- disputed
- stale
- restricted
- invalidated

Example:

> Recommendation exists

does not automatically mean:

> Recommendation is reliable enough to use.

## What State gives Trust

State tells Trust:

- what claim or condition needs to be evaluated
- what changed
- what evidence currently applies
- which dependencies remain valid
- whether previous trust conditions still hold

## Operational rule

> **A state can exist without being trusted enough to act on.**

## Required behavior

Trust changes should affect state behavior.

Example:

**Recommendation: Active**  
**Trust: Supported**

Source changes.

Trust becomes:

**Revalidation required**

The recommendation may still exist, but its operational state becomes:

**Restricted pending reassessment**

## Key distinction

State answers:

> What do we currently believe or treat as true?

Trust answers:

> How much reliance has that state earned?

---

# 11. Authority ↔ State

## What Authority gives State

Authority determines:

- who may create state
- who may commit it
- who may override it
- who may invalidate it
- what AI may change automatically

## What State gives Authority

State determines which authority rules apply.

Example:

**Routine + supported**
→ AI may execute.

**Novel + uncertain**
→ AI may propose only.

**High consequence**
→ human decision required.

**Restricted**
→ nobody may proceed.

## Operational rule

> **State mutation is an authority-controlled action.**

An AI system should not silently change organizational truth simply because it inferred something.

## Required behavior

For every important state change define:

- proposer
- validator
- committer
- override authority
- rollback authority

These may be the same actor for simple cases.

They should remain separate where consequence warrants it.

---

# 12. Experience ↔ State

## What Experience gives State

Human interaction can itself change state.

Examples:

- approve
- reject
- defer
- correct
- override
- acknowledge
- escalate
- resolve

The interface must capture the meaning of the action, not just the click.

## What State gives Experience

State determines what each person should see.

Examples:

### Field user

> Approved for use

### Brand lead

> Approved, but two downstream assumptions changed

### Capability owner

> 7 active items depend on a changed source

### Auditor

> Full state history and decision record

## Operational rule

> **The same underlying state may have several role-specific expressions.**

## Required behavior

State should drive:

- what appears
- what needs attention
- which controls are available
- which actions are disabled
- what explanation is needed
- what can remain hidden

Users should not have to inspect the entire system to understand what matters now.

---

# 13. The Full Interconnection Example

Consider an agency recommendation for a pharma client.

### 1. Process

Agency capability completes analysis.

### 2. State

Recommendation becomes:

> **Proposed**

### 3. Context

Applies to:

> Brand X · US · Launch planning · FY27 strategy v4

### 4. Trust

Evidence is strong but one market-access assumption remains unresolved.

Trust:

> **Supported with condition**

### 5. Authority

Agency may recommend.

Client commercial lead must decide.

### 6. Experience

Client sees:

> **Recommendation ready**
>
> Strong evidence supports this direction.  
> One market-access assumption remains unresolved.
>
> **Accept · Ask for analysis · Defer**

Client accepts.

### New state

> **Accepted with assumption unresolved**

Three weeks later, new access evidence arrives.

Context changes.

Trust re-evaluates.

The assumption is disproven.

State automatically becomes:

> **Reassessment required**

The capability identifies two downstream plans affected by the change.

That is State as the Product operating across all six layers.

---

# 14. Unit of State

Every meaningful state should specify:

### Subject

What does this state describe?

### Current condition

What is true now?

### Scope

Where does it apply?

### Effective time

Since when? Until when?

### Basis

What created or supports it?

### Trust status

How reliable is it?

### Authority

Who may change or act from it?

### Dependencies

What other conditions must remain true?

### Prior state

What did this replace?

### Downstream impact

What changes because of it?

---

# 15. State Contract

Every important state should have a lightweight contract.

### Subject
What are we tracking?

### State values
Which conditions materially change behavior?

### Source
How is state established?

### Scope
Where does it apply?

### Owner
Who is responsible?

### Change authority
Who or what may modify it?

### Entry conditions
What must happen for this state to become true?

### Exit conditions
What causes it to stop being true?

### Trust requirements
What must be reliable before others act on it?

### Context dependencies
What context determines its meaning?

### Process effects
Which transitions become available or unavailable?

### Experience
Who needs to see it and how?

### Propagation
What changes downstream?

### History
What must remain traceable?

---

# 16. Core State Types

Keep the model small.

## Process state

Where is the work?

Examples:

- analyzing
- reviewing
- executing
- complete

## Decision state

What has been decided?

Examples:

- proposed
- accepted
- rejected
- deferred
- superseded

## Context state

Which conditions currently apply?

Examples:

- current strategy
- active segmentation
- applicable brief

## Trust state

How may something be relied upon?

Examples:

- provisional
- supported
- review required
- restricted

## Authority state

Who or what may act?

Examples:

- AI may propose
- human approval required
- AI may execute
- prohibited

## Object state

What is the current condition of an asset, recommendation, claim, or campaign?

Examples:

- draft
- approved
- active
- expired
- withdrawn

## Issue state

Examples:

- open
- investigating
- escalated
- resolved

## Outcome state

Examples:

- pending
- observed
- successful
- failed
- unknown

---

# 17. Proposed vs Committed State

This distinction is critical for AI-native capabilities.

## Proposed state

AI or another actor believes reality may have changed.

Example:

> AI detects that a campaign may conflict with the current strategy.

## Committed state

The required evidence and authority establish the change.

Example:

> Campaign status becomes **Review required**.

### Rule

> **AI may propose state more freely than it may commit state.**

Trust and Authority determine when proposed state becomes committed state.

---

# 18. Product Principles

## Principle 1: State represents current reality

Do not make people reconstruct current status from history.

---

## Principle 2: State should be explicit when it changes behavior

If something changes Process, Context, Trust, Authority, or Experience, it likely deserves explicit state.

---

## Principle 3: AI inference is not organizational truth

AI beliefs should not silently become committed business state.

---

## Principle 4: State change requires authority

Every meaningful state change should have clear decision rights.

---

## Principle 5: State must have context

“Approved” or “current” means little without knowing where that state applies.

---

## Principle 6: State must have time

The system should know:

- when a state began
- what it replaced
- whether it expires
- whether it remains valid

---

## Principle 7: State should change process behavior

A state label that changes nothing is usually just metadata.

---

## Principle 8: Trust should qualify state

The capability should distinguish:

> This state exists

from:

> This state is reliable enough to act on.

---

## Principle 9: State should travel with the work

Important conditions should survive handoffs.

---

## Principle 10: State conflicts must be visible

Do not silently resolve two competing claims about current reality without clear authority.

---

## Principle 11: State should be recoverable

The organization should be able to understand how current state was reached.

---

## Principle 12: State should drive attention

The capability should surface changes that require action rather than forcing users to hunt for them.

---

# 19. State Operating Loop

**Observe → Propose → Validate → Commit → Propagate → Act → Monitor → Reassess**

### Observe

New event, evidence, decision, or change.

### Propose

Does this imply that state changed?

### Validate

Do context, trust, and authority support the proposed change?

### Commit

Establish current state.

### Propagate

Update affected processes, context, permissions, and downstream state.

### Act

Allow the appropriate next move.

### Monitor

Watch relevant dependencies.

### Reassess

Change, reopen, expire, restrict, or invalidate state when conditions change.

---

# 20. State Propagation

A state change should trigger only the downstream effects it actually matters to.

Example:

Current strategy changes.

The capability checks dependencies.

Results:

- 12 assets unaffected
- 5 recommendations need review
- 2 active campaigns require immediate attention
- 1 AI execution permission is temporarily reduced

This is better than either extreme:

> update nothing

or:

> invalidate everything

State propagation should be dependency-aware.

---

# 21. State Invalidation

Sometimes the system cannot safely move directly to a new known state.

It should support:

> **Unknown / reassessment required**

Examples:

- source reliability fails
- upstream data is corrected
- strategy changes unexpectedly
- approval is withdrawn
- conflicting systems cannot be reconciled

Unknown is a valid state.

False certainty is not.

---

# 22. Cross-Team and Cross-Organization State

Commercial work may move:

**client → agency → analytics → creative → review → media → field**

State should preserve what the receiving party needs to know.

But not all state should cross the boundary.

Distinguish:

- shared state
- internal state
- client-owned state
- agency-owned state
- confidential state
- regulatory or control state

Example:

An agency may expose:

> Client decision: Recommendation accepted.

It may not expose:

> Internal agency debate and proprietary reasoning history.

State projection should respect organizational boundaries.

---

# 23. State Experience

Users should not feel like they are operating a state machine.

They should experience:

- clear current status
- what changed
- what is unresolved
- what needs them
- what can happen next
- why something became blocked
- what happened since they last looked

The desired experience:

> **I can pick this up immediately and understand where things stand.**

---

# 24. Resume Experience

A commercial leader returns after two weeks.

Instead of searching meetings and email:

### Current

Launch recommendation approved.

### Changed

Segmentation v5 replaced v4.

### Impact

Three assumptions now need reassessment.

### Open

Market-access evidence still missing.

### Needs you

Decide whether Recommendation 7 should be reopened.

This is a direct expression of State as the Product.

---

# 25. Failure Modes

Common failures:

- stale state
- missing state
- conflicting state
- wrong scope
- unauthorized state change
- inferred state treated as fact
- lost handoff state
- failed downstream propagation
- old state remaining active
- state with no owner
- state with no exit condition

Possible responses:

- verify
- reconcile
- reopen
- rollback
- invalidate
- escalate
- block
- mark unknown

---

# 26. State Observability

The organization should be able to see:

- what changed
- where work gets stuck
- which states are reopened
- how long work remains in each state
- which AI state proposals are rejected
- where state conflicts occur
- where propagation fails
- which state changes cause rework

Observability should improve the capability, not merely create logs.

---

# 27. State Evaluation

### Accuracy
Does state match current reality?

### Freshness
Is it still current?

### Completeness
Are material conditions represented?

### Context fit
Is state interpreted inside the right scope?

### Trust fit
Is its reliability represented correctly?

### Authority integrity
Was it changed by an authorized actor?

### Consistency
Do important systems agree?

### Traceability
Can we explain how it got here?

### Propagation
Did affected downstream work update correctly?

### Usefulness
Did state improve the next decision or action?

---

# 28. State Measurement

Avoid:

> State quality: 94%

Prefer:

- 4 conflicting active states
- 12 assets affected by changed strategy
- 3 approvals past review date
- 8% of AI-proposed state changes rejected
- 2 state changes failed to propagate
- median time in **Review required**: 2.4 days
- 17 open decisions without owners
- 0 unauthorized committed state changes

Measure things people can act on.

---

# 29. State Learning Loop

Periodically ask:

- Which states actually change behavior?
- Which states nobody uses?
- Where do people manually reconstruct current reality?
- Which state changes are often missed?
- Which states repeatedly conflict?
- Where does AI propose the wrong state?
- Which transitions need human judgment?
- Which transitions no longer need human involvement?
- Which dependencies cause repeated invalidation?

The goal is a **smaller, clearer, more useful state model over time**.

---

# 30. Minimum State Capability Spec

For every AI-native commercial capability define:

### Job
What current reality must the capability maintain?

### Subjects
What things need explicit state?

### State values
Which states materially change behavior?

### Process relationship
What events create or change them?

### Context relationship
What determines their meaning and scope?

### Trust relationship
How is reliability represented?

### Authority relationship
Who may propose, commit, override, or invalidate them?

### Experience relationship
Who needs to see what?

### Dependencies
What other conditions must remain true?

### Propagation
What changes downstream?

### History
What must remain traceable?

### Failure
What happens when state is missing, stale, conflicting, or unknown?

### Evaluation
How do we know state is working?

---

# 31. Acceptance Criteria

State as the Product is operational only when:

1. Current state is distinguishable from history.
2. State is explicit where it changes behavior.
3. Every important state has scope.
4. Context determines how state is interpreted.
5. Trust qualifies whether state can be relied upon.
6. Authority governs state mutation.
7. AI inference does not silently become committed state.
8. Process responds to state rather than rigid step order.
9. Experience projects relevant state by role.
10. State survives meaningful handoffs.
11. State dependencies can be tracked.
12. Material upstream changes propagate appropriately.
13. Conflicting state can be detected.
14. Unknown is supported as a valid state.
15. Important changes remain traceable.
16. Users can see what changed and what needs attention.
17. The capability can resume from current state without reconstructing the past.

---

# 32. Anti-Patterns

Avoid:

- treating the database as the state model
- storing every fact as state
- confusing memory with state
- AI silently committing inferred states
- states without context
- states without authority
- states that do not alter process
- trust warnings disconnected from state behavior
- duplicate current states across systems
- approvals surviving changed dependencies
- handoffs losing unresolved conditions
- making users manually reconcile status
- exposing every state to every role
- one giant state machine for every capability

---

# 33. Canonical Definition

> **State as the Product means an AI-native commercial capability maintains a reliable, scoped, current view of the conditions that matter to the work and uses changes in those conditions to coordinate what happens next.**
>
> **Process** creates and responds to state transitions.
>
> **State** records where things stand now.
>
> **Context** determines what that state means here.
>
> **Trust** determines how much reliance that state deserves.
>
> **Authority** determines who or what may change it or act from it.
>
> **Experience** makes the relevant state visible and actionable to each person.
>
> Together, they allow commercial work to continue across time, systems, people, and organizations without repeatedly reconstructing reality.