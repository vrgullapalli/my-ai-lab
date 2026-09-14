# Experience as the Product
## Operational Model & Specification for AI-Native Commercial Capabilities

## 1. Purpose

Define how people experience, understand, influence, and rely on an AI-native commercial capability.

Experience is not just:

- UI
- chat
- dashboards
- alerts
- approvals
- explanations

Those are expressions of the experience.

> **Experience as the Product is the capability’s ability to turn its internal understanding into the simplest useful interaction for the person and situation, while allowing that person’s judgment and actions to correctly change the system in return.**

---

# 2. Core Thesis

A good AI-native capability should make someone feel:

> **It understands where we are.**  
> **It remembers what matters.**  
> **It knows what has changed.**  
> **It shows me what I can rely on.**  
> **It handles what it can without bothering me.**  
> **It brings me in when my judgment matters.**  
> **What I do changes the system appropriately.**

The goal is not more interaction.

The goal is **better interaction at the moments that matter**.

---

# 3. Experience Is Not a Separate Front End

Experience is the human and organizational expression of the whole capability.

| Layer | Experience should answer |
|---|---|
| **Process** | What is happening, and what happens next? |
| **State** | Where do things stand now? |
| **Memory** | What from before still matters? |
| **Context** | What matters in this situation? |
| **Evidence** | Why should I believe or consider this? |
| **Trust** | What can I safely rely on? |
| **Authority** | What can the system do, and what requires me? |
| **Evaluation & Learning** | Did this work, and what changed because of it? |

Experience should not expose every layer separately.

It should combine them into **one useful moment**.

---

# 4. Experience Operating Loop

The core loop is:

**Understand the moment**  
↓  
**Assemble State + Memory + Context + Evidence**  
↓  
**Assess Trust + Authority**  
↓  
**Determine what this person needs now**  
↓  
**Express the simplest useful experience**  
↓  
**Person acts, decides, corrects, or does nothing**  
↓  
**Write the consequence back into the system**  
↓  
**Update State, Memory, Context, Trust, Process, and Learning as needed**

Experience therefore works in both directions.

### Capability → Person

Show, ask, explain, act, warn, or stay quiet.

### Person → Capability

Decide, correct, approve, reject, add context, override, stop, or teach.

---

# 5. The Experience Contract

At every meaningful interaction, answer seven questions.

## 1. What does this person need to understand now?

Surface only what changes understanding or action.

Usually:

- current state
- meaningful change
- important uncertainty
- something blocked
- something requiring judgment
- the next useful move

---

## 2. What should the capability already know?

Do not repeatedly ask for:

- settled decisions
- current strategy
- known preferences
- active constraints
- prior corrections
- current ownership
- established context
- known open issues

Ask again only when something is:

- missing
- stale
- conflicting
- unclear
- high consequence

---

## 3. What changed?

Show **meaningful difference**, not activity.

Bad:

> 18 files changed.

Better:

> Strategy changed. Three active recommendations now need review.

---

## 4. What can the person safely rely on?

Distinguish:

- established
- supported
- provisional
- inferred
- disputed
- stale
- unknown

Do not make the person guess.

---

## 5. What actually requires human judgment?

Bring people in for:

- consequential ambiguity
- competing valid choices
- strategic direction
- new authority
- material exceptions
- high-risk decisions
- judgment that AI cannot legitimately own

Do not ask for approval simply because a human is available.

---

## 6. What controls are appropriate?

Depending on the situation:

- inspect
- correct
- approve
- reject
- defer
- override
- narrow
- escalate
- pause
- undo
- stop

More consequence should generally mean stronger control.

---

## 7. What should change because of the interaction?

A meaningful interaction should produce a meaningful system consequence.

Examples:

- decision committed
- assumption corrected
- state updated
- process rerouted
- downstream work stopped
- context changed
- trust reduced or restored
- memory updated
- learning captured

“Thanks for the feedback” is not enough.

---

# 6. Interconnection with Process

## Process gives Experience

- current stage
- available next moves
- blocked transitions
- work requiring judgment
- exceptions

## Experience gives Process

Human actions may:

- advance
- pause
- reroute
- reopen
- stop
- complete

## Rule

> **The experience should expose the next meaningful process decision, not the workflow machinery.**

The person should not have to manage the process manually.

---

# 7. Interconnection with State

## State gives Experience

- current status
- open issues
- changed conditions
- unresolved decisions
- current permissions

## Experience gives State

Human actions can:

- confirm
- correct
- reject
- supersede
- reopen
- resolve

## Rule

> **Every visible state should correspond to something real underneath.**

A badge should not merely describe.

It should affect behavior.

---

# 8. Interconnection with Memory

## Memory gives Experience

- prior decisions
- relevant history
- earlier corrections
- past outcomes
- useful preferences
- previous exceptions

## Experience gives Memory

Capture durable information such as:

- why a decision was made
- a recurring correction
- an important outcome
- a meaningful exception

## Rule

> **Memory should remove repetition without trapping the capability in the past.**

The user should be able to see when historical memory is influencing the present.

---

# 9. Interconnection with Context

## Context gives Experience

What matters for:

- this role
- this task
- this brand
- this client
- this market
- this moment

## Experience gives Context

People can:

- add missing context
- correct wrong context
- clarify scope
- identify an exception

## Rule

> **The experience should feel situated rather than generic.**

Context should appear only when seeing it improves understanding or action.

---

# 10. Interconnection with Evidence

## Evidence gives Experience

- supporting sources
- provenance
- competing evidence
- gaps
- strength of support

## Experience gives Evidence

People may:

- challenge a source
- add evidence
- reject weak support
- confirm interpretation

## Rule

> **Evidence should be available at the depth needed for the decision.**

Normal use may need one sentence.

Review may need claim-level detail.

Audit may need full provenance.

---

# 11. Interconnection with Trust

## Trust gives Experience

Trust determines:

- how strongly something is presented
- whether warnings appear
- whether action is permitted
- whether review is needed
- whether the system should stop

## Experience gives Trust

Human review, correction, outcomes, and overrides provide evidence about whether trust remains deserved.

## Rule

> **Trust should change the experience, not just appear as a label.**

If something becomes less trustworthy, the system should behave differently.

---

# 12. Interconnection with Authority

## Authority gives Experience

Authority determines:

- available actions
- disabled actions
- required approvals
- escalation paths
- whether AI may act independently

## Experience gives Authority

People with proper decision rights may:

- grant permission
- narrow permission
- override
- revoke
- delegate

## Rule

> **Controls should reflect real authority.**

Do not show buttons for actions the person or capability cannot actually take.

---

# 13. Interconnection with Evaluation & Learning

## Evaluation gives Experience

Evaluation may surface:

- degraded performance
- recurring failures
- important outcomes
- unusual override patterns
- changing system behavior

## Experience gives Evaluation

Interaction provides evidence through:

- accept/reject
- corrections
- overrides
- completion
- abandonment
- downstream outcomes

## Rule

> **Interaction should create evidence about whether the capability is working.**

Do not treat clicks as proof of value.

---

# 14. Core Experience Moments

Design around moments, not screens.

## Enter / Return

Answer:

- Where are we?
- What changed?
- What is open?
- What needs me?

Example:

> **Since you were last here**  
> Retrieval was closed.  
> State design was completed.  
> One architecture decision needs you.

---

## Normal Work

When everything is healthy:

> **Stay out of the way.**

The capability should handle routine work quietly.

---

## Uncertainty

When confidence weakens:

> Make the uncertainty and its consequence visible.

Example:

> Evidence is incomplete. I can continue provisionally or investigate first.

---

## Judgment Needed

Show:

- the actual decision
- enough context
- relevant evidence
- implications
- realistic options

Avoid making the user reconstruct the problem.

---

## Material Change

Show:

> **What changed → What it affects → What needs to happen**

Not:

> Something was updated.

---

## Handoff

Give the next person enough understanding to continue without rebuilding the work.

Include:

- current state
- important context
- decisions
- assumptions
- constraints
- unresolved issues
- authority

---

## Correction

When the person corrects the capability:

1. confirm what changed
2. update affected state/context
3. identify downstream impact
4. preserve useful memory
5. prevent repeat error where appropriate

---

## Failure

Explain:

- what failed
- what remains safe
- what was affected
- what happened automatically
- what requires human action

Do not simply return an error code.

---

# 15. Core Experience Surfaces

Start small.

## Now

What matters now?

- Current
- Open
- Blocked
- Next

## Changed

What materially changed since the last interaction?

- change
- impact
- affected work

## Needs You

Only things requiring human judgment or authority.

Each should answer:

- what decision?
- why you?
- what evidence?
- what happens next?

## Why

Progressive access to:

- context
- evidence
- assumptions
- reasoning
- trust limits

## History

How did we get here?

- prior state
- decisions
- changes
- corrections
- approvals

## Controls

Only the actions appropriate to the current role and authority.

---

# 16. Progressive Disclosure

The experience should expand with need.

### Normal

Keep it simple.

### User asks why

Show context and evidence.

### Uncertainty rises

Show limitations and consequences.

### Material change

Interrupt.

### Human judgment required

Present a decision experience.

### Audit or investigation

Expose full history and provenance.

> **Complexity should exist underneath without forcing every person to experience all of it.**

---

# 17. Role-Specific Experience

The capability should project different experiences from the same underlying system.

### Commercial leader

- current situation
- material changes
- decisions
- risks
- next move

### Agency strategist

- brief
- assumptions
- evidence
- client decisions
- open questions

### Analyst

- data
- provenance
- methods
- conflicts
- uncertainty

### Creative

- strategy
- audience
- boundaries
- approved inputs
- open creative space

### Reviewer

- what changed
- what needs judgment
- supporting evidence
- prior decisions

### Field user

- relevant action
- approved use
- necessary customer context

### Capability owner

- failures
- overrides
- exceptions
- trust degradation
- performance

### Audit / compliance

- complete reconstructable record

---

# 18. Organizational Experience

Experience does not stop with the individual.

The capability should make work easier across:

- teams
- functions
- companies
- agencies
- clients
- systems

A good experience reduces:

- repeated explanation
- unclear ownership
- lost assumptions
- duplicate review
- hidden decisions
- broken handoffs

The organization should experience the capability as:

> **less coordination needed to stay aligned.**

---

# 19. Trust and Control Experience

Good control should be:

- present when needed
- quiet when not needed
- easy to understand
- reversible where possible
- tied to real consequences

Avoid both extremes:

### Too little control

The system acts without meaningful limits.

### Too much control

People approve everything and eventually stop paying attention.

The goal is:

> **appropriate friction.**

---

# 20. Experience Write-Back

Every meaningful interaction should have explicit write-back rules.

Example:

User rejects a recommendation.

Possible consequences:

**State**
→ Rejected

**Memory**
→ rejection reason preserved if useful

**Context**
→ new constraint may apply

**Trust**
→ recommendation pattern may need review

**Process**
→ downstream work stops

**Learning**
→ outcome becomes evaluation evidence

The system should tell the person what changed when it matters.

---

# 21. Experience Failure Modes

Common failures include:

- asking for information the system already has
- hiding meaningful changes
- showing every possible detail
- interrupting unnecessarily
- burying uncertainty
- presenting AI inference as fact
- unclear approval consequences
- controls that do nothing meaningful
- corrections that do not persist
- handoffs that lose context
- notifications with no action
- dashboards showing system activity instead of user relevance
- different interfaces showing conflicting state

---

# 22. Experience Observability

Measure how the capability behaves around people.

Useful signals:

- unnecessary interruptions
- repeated questions
- corrections
- overrides
- ignored alerts
- abandoned workflows
- time waiting for judgment
- repeated context reconstruction
- failed handoffs
- unexplained state changes
- actions reversed later
- decisions made with incomplete evidence

Do not optimize only for engagement.

Less interaction may be a better experience.

---

# 23. Experience Evaluation

Evaluate:

### Clarity

Can the person tell where things stand?

### Relevance

Are they seeing what matters to their job?

### Continuity

Can they resume without reconstructing the past?

### Trust

Can they tell what is reliable and what is not?

### Control

Can they intervene where appropriate?

### Judgment efficiency

Is the person involved only where their judgment adds value?

### Consequence

Does their interaction correctly change the system?

### Handoff quality

Can the next person continue without rebuilding context?

### Outcome

Did the experience help produce a better decision or action?

---

# 24. Experience Metrics

Avoid vague measures like:

> AI experience score: 87%

Prefer:

- 6 unnecessary approval requests this week
- 14% of sessions required repeated context
- 3 critical alerts were ignored
- 22% of overrides came from missing context
- median time to human decision: 4 hours
- 92% of resumed tasks continued without re-explanation
- 0 corrections lost after write-back
- 4 handoffs required manual context rebuilding

Measure problems people can fix.

---

# 25. Minimum Experience Contract

For every AI-native capability define:

### Actor

Who is interacting?

### Job

What are they trying to accomplish?

### Moment

Where are they in the work?

### State

What is true now?

### Memory

What from before matters?

### Context

What matters here?

### Evidence

What support may need to be visible?

### Trust

What can they safely rely on?

### Authority

What may the capability and person do?

### Experience

What should they see, know, or do?

### Controls

What actions are available?

### Write-back

What changes because of the interaction?

### Failure

What happens when the interaction cannot proceed normally?

---

# 26. Acceptance Criteria

Experience as the Product is operational only when:

1. The experience is based on current State.
2. Relevant Memory reduces unnecessary repetition.
3. Context changes what the person sees and how the capability behaves.
4. Evidence is available at the depth required for judgment.
5. Trust changes interaction and capability behavior.
6. Authority determines available controls.
7. Important changes become visible.
8. Routine work does not create unnecessary interruptions.
9. Human judgment is requested only where it adds value.
10. Corrections and decisions write back into the system.
11. Important state survives handoffs.
12. Different roles receive different useful projections.
13. Users can understand why the system changed course.
14. The system supports both normal work and failure states.
15. Experience produces evidence for evaluation and learning.
16. A person can return later and understand where things stand.
17. The experience reduces coordination burden rather than adding another system to manage.

---

# 27. Anti-Patterns

Avoid:

- starting with screens instead of the job
- treating chat as the default experience
- dashboards full of capability telemetry
- asking users to provide known context
- exposing all evidence all the time
- confidence scores without consequences
- approvals without clear decision rights
- notifications that do not require action
- controls disconnected from real authority
- hidden state changes
- corrections that disappear
- making people manage workflow state manually
- forcing everyone to see the same interface
- optimizing for engagement instead of useful outcomes

---

# 28. Canonical Definition

> **Experience as the Product means an AI-native commercial capability continuously turns its Process, State, Memory, Context, Evidence, Trust, and Authority into the simplest useful interaction for each person and situation, while ensuring that the person’s decisions, corrections, and actions correctly change the capability in return.**
>
> The person should understand where things stand.
>
> They should not have to repeat what the capability already knows.
>
> They should see meaningful changes.
>
> They should know what they can rely on.
>
> They should be involved when their judgment matters.
>
> They should have appropriate control.
>
> And their interactions should leave the system in a better, more accurate state.