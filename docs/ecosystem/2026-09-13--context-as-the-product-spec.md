# Context as the Product
## Operational Specification for AI-Native Commercial Capabilities

## 1. Purpose

Define how an AI-native commercial capability gets, interprets, applies, preserves, updates, and expresses the **right context for the work happening now**.

Context may span:

- pharma company
- brand
- agency
- customer
- market
- indication
- channel
- strategy
- evidence
- prior decisions
- workflow
- role
- policy
- regulatory requirements
- organizational history
- live commercial conditions

The goal is not to give AI more information.

The goal is:

> **Give the capability the minimum sufficient context to understand what the current situation means and behave appropriately.**

---

# 2. Core Thesis

> **Context turns information into situational meaning.**

The same data, signal, claim, recommendation, or instruction can mean something different depending on:

- who is using it
- what they are trying to accomplish
- where they are in the process
- what happened before
- what has changed
- which market or client applies
- what constraints exist
- what authority exists
- what remains uncertain

Context is therefore not a supporting input.

**It is part of the capability itself.**

---

# 3. Context Is Not “Everything We Know”

More context is not automatically better context.

Too much context can:

- bury what matters
- introduce conflicting assumptions
- expose information that should not be used
- carry outdated decisions forward
- contaminate work across clients or brands
- increase cost and complexity
- cause AI to reason from irrelevant information

The objective is:

> **Minimum sufficient context, not maximum available context.**

---

# 4. The Six Connected Layers

Context sits inside a larger operating system.

| Layer | Core question |
|---|---|
| **Process** | How does the work move from need to outcome? |
| **State** | What does the capability know at this point? |
| **Context** | What does that state mean here and now? |
| **Trust** | Is what we know sufficient and reliable enough to proceed? |
| **Authority** | Who or what may make the next move? |
| **Experience** | What does each person need to see, know, or do now? |

These are not separate systems.

They continuously affect one another.

---

# 5. How the Layers Interact

### Process uses context

Context may change the path the work takes.

### State feeds context

Current decisions, evidence, unresolved questions, and prior actions become part of what the next step needs to know.

### Context shapes trust

Evidence can be accurate but inappropriate for the current situation.

Trust depends partly on whether the right context is present.

### Context changes authority

The same action may be automated in one context and require human judgment in another.

### Experience expresses context

People should see only the context they need to understand, judge, or act.

The operating pattern is:

> **State tells us what we know. Context tells us what it means. Trust tells us whether we can rely on it. Authority determines what happens next. Process moves the work. Experience makes it usable.**

---

# 6. Unit of Context

Context should always be relative to a job.

Do not ask:

> What context do we have?

Ask:

> **What does this capability need to understand to do this job correctly in this situation?**

The useful unit is:

**Job + Actor + Situation + Current State + Relevant Knowledge + Constraints + Time**

---

# 7. Context Operating Loop

Every material capability should support some form of:

**Infer need → Find → Resolve → Assemble → Apply → Observe → Update → Propagate → Expire**

### Infer need

What context does this job require?

### Find

Where can that context come from?

### Resolve

Which sources are authoritative, current, permitted, and relevant?

### Assemble

Build the minimum sufficient package.

### Apply

Use it to interpret the current state and determine behavior.

### Observe

Did the context prove sufficient?

### Update

Capture decisions, corrections, or changed conditions where appropriate.

### Propagate

Carry material context downstream.

### Expire

Stop using context when its scope or validity ends.

---

# 8. The Context Contract

Every important job should have a lightweight Context Contract.

### Job

What is the capability trying to accomplish?

### Required context

What must be present?

### Conditional context

What becomes necessary only in certain situations?

### Optional context

What might improve the work but is not required?

### Prohibited context

What must not be used?

### Sources

Where should the context come from?

### Authority

Which source wins if sources disagree?

### Freshness

How current must it be?

### Scope

Where does this context apply?

### Missing-context behavior

What should happen if required context cannot be established?

The Context Contract defines the need.

Dynamic context assembly fulfills it.

---

# 9. Core Context Types

Do not create a huge taxonomy.

Most commercial capabilities need some mix of six broad types.

## Business context

Strategy, objective, brand, market, customer, competition, commercial priorities.

## Task context

What is being done now, why, and what outcome is needed.

## Organizational context

Roles, ownership, decision rights, teams, client relationships, operating norms.

## Evidence context

Sources, findings, assumptions, contradictions, confidence, provenance.

## Process context

Current stage, previous decisions, unresolved issues, approvals, downstream dependencies.

## Constraint context

Legal, regulatory, policy, privacy, contractual, channel, audience, security, and data-use limits.

The capability should retrieve these selectively.

---

# 10. Product Principles

## Principle 1: Context is job-relative

There is no universally correct context.

The right context depends on the job being performed.

A field recommendation, agency strategy recommendation, executive decision, and MLR review may involve the same underlying information but need different context packages.

---

## Principle 2: Context should be assembled, not dumped

Do not send every available document, memory, and data point into the model.

Select based on:

- relevance
- authority
- freshness
- scope
- consequence
- current process state

The capability should know why something is included.

---

## Principle 3: Context must have authority

Relevant information is not necessarily authoritative information.

The capability should distinguish:

- canonical
- approved
- current
- advisory
- historical
- inferred
- superseded
- unknown

When sources conflict, that conflict should affect behavior.

---

## Principle 4: Context must have scope

Every important context item should have boundaries.

For example:

> Approved for Brand A  
> US market  
> HCP audience  
> Current launch stage  
> Through September 2026

Do not let local truth quietly become universal truth.

---

## Principle 5: Context must have time

Context changes.

The capability should understand:

- when something became true
- whether it is still true
- what replaced it
- what depends on it

A correct decision from six months ago can be bad context today.

---

## Principle 6: Context must distinguish fact from interpretation

Preserve differences between:

- observed
- inferred
- assumed
- decided
- recommended
- unknown

A client decision is not the same as external evidence.

An agency interpretation is not the same as a client instruction.

Both can matter without pretending they are the same thing.

---

## Principle 7: Missing context is a real system state

The capability must be able to say:

> **I do not have enough context to do this reliably.**

It may then:

- retrieve more
- ask
- investigate
- narrow the task
- involve another person
- proceed provisionally
- refuse

It should not silently invent missing business context.

---

## Principle 8: Context must change behavior

If context has no effect on what the capability does, it is decoration.

A market change might alter a recommendation.

A role change might alter what information can be seen.

A client boundary might prevent reuse.

A high-consequence decision might require more evidence.

Context must affect the process.

---

## Principle 9: Material context travels with the work

Important assumptions, constraints, evidence, and decisions should not disappear at handoffs.

When work moves:

**client → agency → strategy → creative → review → media → field**

the context needed to interpret it correctly should move too.

---

## Principle 10: Context should be projected for the audience

Different actors need different views of the same underlying context.

A commercial leader may need:

> What changed and why it matters.

An analyst may need:

> Data, assumptions, methods, and conflicts.

A creative team may need:

> Strategy, audience, constraints, and creative freedom.

The underlying context can remain consistent while its expression changes.

---

## Principle 11: Context boundaries must be protected

Context can be useful and still be inappropriate to use.

Protect:

- client boundaries
- brand boundaries
- confidential information
- privacy
- market restrictions
- contractual restrictions
- approved-use conditions
- role-based access

Client A context does not become general agency knowledge merely because an AI has seen it.

---

## Principle 12: Context should improve through use without becoming contaminated

Human corrections, outcomes, overrides, and repeated patterns can improve future context.

But learning must preserve:

- provenance
- scope
- authority
- client boundaries
- distinction between observation and interpretation

Repeated information does not automatically become truth.

---

# 11. The Context Package

At runtime, the capability should assemble a small Context Package.

It may contain:

### Job
What are we doing?

### Current state
Where does the work stand?

### Relevant context
What matters now?

### Evidence
What supports the current understanding?

### Decisions
What has already been decided?

### Assumptions
What are we currently treating as true?

### Constraints
What limits the work?

### Authority
Which sources and decisions govern?

### Gaps and conflicts
What is unresolved?

### Scope
Where does this context apply?

### Freshness
How current is it?

### Next-step implications
What does this context change?

Not every field must be shown to the user.

---

# 12. Source and Authority Resolution

When context conflicts, the capability should not simply use whichever source ranked highest semantically.

Resolution should consider:

**Authority + Scope + Freshness + Relevance**

For example:

A current approved client strategy should normally outrank an older workshop note.

But the older note may still matter if the question is:

> Why was this decision originally made?

Context resolution is therefore situational.

---

# 13. Context and Trust

Trust depends partly on contextual adequacy.

A capability should ask:

- Do I have the context required by the job?
- Is it current?
- Is it authoritative?
- Are material conflicts resolved?
- Am I applying it inside its valid scope?
- Has anything changed since this conclusion was established?

If not, trust should change.

That may change:

- the claim
- the process
- the authority
- the next action
- the user experience

---

# 14. Context and Authority

Context may determine who or what may act.

Example:

A next-best-action capability may normally execute routine recommendations.

But if:

- the customer situation is novel
- the evidence is incomplete
- a market restriction applies
- a client-specific rule is triggered

authority may shift from:

**AI acts**

to:

**AI proposes → human decides**

Context is therefore part of the authority decision.

---

# 15. Context and Process

Process should request context as it becomes necessary.

Do not assemble the entire commercial universe at the beginning.

Example:

**Strategy stage**

Needs commercial strategy, market evidence, customer understanding.

**Creative stage**

Adds approved messaging, campaign context, audience, creative constraints.

**Review stage**

Adds evidence, claim history, relevant regulatory and policy context.

Context grows and changes with the work.

---

# 16. Context and Experience

Users should not feel like they are maintaining an AI context database.

They should experience:

- less repeated explanation
- fewer unnecessary questions
- fewer missing handoff details
- recommendations that reflect their actual situation
- clear notice when something important is missing
- visibility into assumptions when they matter
- easy correction of wrong context
- clear explanation when changed context alters the answer
- ability to inspect sources when needed

The desired experience is:

> **It already understands enough of the situation to be useful, and it makes it obvious when it does not.**

---

# 17. Context Expression

Context can appear through different surfaces.

### Scope indicators

> US · Brand X · HCP · Launch planning

### Applied-context view

> Based on current segmentation, FY27 strategy, and latest field research

### Assumption disclosure

> Assumes field capacity remains unchanged

### Context-change alert

> Brand positioning changed since this recommendation was created

### Missing-context state

> Current payer-access assumptions are unavailable

### Provenance

> Client strategy v4.2 · approved Aug 18

### Correction

> This assumption is no longer correct

### Dependency impact

> This strategy change affects 8 active recommendations

Context should become visible when seeing it changes understanding or action.

---

# 18. Role-Specific Context

Different actors need different projections.

| Role | Important context |
|---|---|
| **Commercial leader** | objectives, changes, evidence, decisions, implications |
| **Brand team** | strategy, customer, market, constraints, prior decisions |
| **Agency strategist** | brief, client strategy, research, assumptions, decision boundaries |
| **Analytics** | data definitions, methodology, provenance, assumptions, quality |
| **Creative** | audience, strategy, approved inputs, constraints, open creative space |
| **Medical / Legal / Regulatory** | claims, evidence, changes, conditions requiring judgment |
| **Field** | customer situation, approved use, relevant next action |
| **Capability owner** | context failures, stale sources, gaps, conflicts, overrides |

Same underlying capability.

Different context experience.

---

# 19. Cross-Organization Context

Commercial capabilities often cross company boundaries.

Context must preserve:

- organization
- ownership
- confidentiality
- permissions
- IP
- client scope
- reuse conditions
- decision rights
- authoritative source
- handoff responsibility

The capability should know:

> **Whose context is this, where may it be used, and what happens when it crosses a boundary?**

---

# 20. Context Change and Propagation

When material context changes, the capability should determine what it affects.

Example:

A client changes positioning.

The system should be able to identify that:

- one recommendation remains valid
- three analyses need reassessment
- six creative assets rely on the old assumption
- two downstream decisions should be reopened

Not every context change requires action.

But material dependency changes should not remain invisible.

---

# 21. Failure Behavior

Common context failures include:

- missing context
- stale context
- incorrect context
- conflicting context
- irrelevant context
- excessive context
- wrong scope
- wrong authority
- inappropriate reuse
- cross-client contamination
- lost handoff context
- unverified assumptions

Responses may include:

- retrieve
- verify
- narrow
- ask
- correct
- substitute
- escalate
- mark provisional
- block
- reopen prior work

The failure response should match the consequence.

---

# 22. Context Observability

The organization should be able to understand:

- which context was used
- which sources were selected
- what was excluded
- what was missing
- where conflicts occurred
- which assumptions mattered
- where people corrected context
- where stale context caused problems
- where context changed an outcome

Observability should improve the context capability itself.

---

# 23. Context Evaluation

Do not evaluate context by asking:

> Did retrieval return relevant documents?

Evaluate whether the context was **good enough for the job**.

Useful dimensions:

### Sufficiency
Was anything material missing?

### Relevance
Did the capability use what actually mattered?

### Authority
Were the right sources trusted?

### Freshness
Was important context current?

### Scope
Was context applied only where valid?

### Conflict handling
Were contradictions surfaced and handled?

### Efficiency
Was unnecessary context excluded?

### Outcome impact
Did better context improve the decision or action?

---

# 24. Context Measurement

Avoid abstract metrics such as:

> Context quality: 91%

Prefer interpretable measures:

- 5/5 required context classes present
- 2 unresolved source conflicts
- 7 recommendations affected by changed strategy
- 14% of human overrides traced to missing context
- 3 stale sources still referenced by active work
- 0 cross-client context violations
- 72% reduction in repeated context requests

Measure conditions that help improve the capability.

---

# 25. Context Learning Loop

Periodically ask:

- What context are people repeatedly adding manually?
- What questions does the capability keep asking unnecessarily?
- Which missing context causes bad decisions?
- Which sources are rarely useful?
- Which context becomes stale fastest?
- Which assumptions repeatedly prove wrong?
- Which context should become reusable?
- Which context must remain local?
- Where are boundaries being lost?
- What context should no longer exist?

The goal is not an ever-growing context layer.

The goal is **better selection and interpretation over time.**

---

# 26. Minimum Context Capability Spec

For every AI-native commercial capability define:

### Job
What must the capability understand well enough to accomplish?

### Context consumers
Who or what uses the assembled context?

### Required context
What must be present?

### Sources
Where can it come from?

### Authority
What governs when sources conflict?

### Scope
Where does each important piece apply?

### Freshness
When does it need refreshing?

### Assembly
How is minimum sufficient context selected?

### Expression
What does each role need to see?

### Propagation
What must travel downstream?

### Boundaries
What context must not cross?

### Failure
What happens when context is inadequate?

### Evaluation
How do we know the context was good enough?

---

# 27. Acceptance Criteria

Context as the Product is operational only when:

1. Context is defined relative to a job.
2. The capability assembles rather than dumps information.
3. Important context has provenance.
4. Authority is distinguishable from relevance.
5. Scope and freshness are preserved.
6. Facts, interpretations, assumptions, and decisions remain distinguishable.
7. Missing context can change capability behavior.
8. Material context changes can affect process and trust.
9. Context persists across meaningful handoffs.
10. Cross-organization boundaries are preserved.
11. Users can inspect or correct important context.
12. Different roles receive appropriate context projections.
13. Stale or superseded context can be detected.
14. Important context dependencies can be traced.
15. Context quality is evaluated against the job and outcome.
16. Learning does not silently create authority or cross boundaries.
17. The capability uses the minimum sufficient context needed to work well.

---

# 28. Anti-Patterns

Avoid:

- “give the model everything”
- treating a vector database as Context Architecture
- equating retrieval relevance with authority
- permanent context packages
- hidden assumptions
- old decisions treated as current truth
- copying context manually between teams
- generic context shared across every role
- client information leaking into reusable agency context
- storing information without knowing its scope
- context that never expires
- context warnings that do not alter behavior
- rebuilding context separately inside every agent
- enormous schemas before the jobs require them
- optimizing token count instead of contextual sufficiency

---

# 29. Canonical Definition

> **Context as the Product means an AI-native commercial capability has a designed way to determine what it needs to understand, assemble the minimum sufficient context, interpret that context within its proper scope, and change its behavior when the context changes or proves inadequate.**
>
> Process determines where the work is going.
>
> State preserves what is currently known.
>
> Context determines what that state means here.
>
> Trust determines whether that understanding is reliable enough to proceed.
>
> Authority determines who or what may act.
>
> Experience makes the relevant context visible and usable without overwhelming the person.
>
> Together, they allow AI to behave less like a generic model with access to data and more like a capability operating inside the actual commercial environment.