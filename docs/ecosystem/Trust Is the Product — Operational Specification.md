# Trust Is the Product
## Operational Specification for AI-Native Commercial Capabilities

## 1. Purpose

Define how trust should be designed, operated, expressed, measured, and maintained across **AI-native commercial capabilities** used within and across:

- pharma companies
- brands
- agencies
- analytics and data partners
- media partners
- technology vendors
- field organizations
- other commercial partners

The capability may span multiple people, systems, organizations, and regulatory or internal-control environments.

Trust therefore cannot be reduced to model accuracy, a confidence score, a disclaimer, an approval workflow, or an audit log.

**Trust is a property of the entire capability and the experience of relying on it.**

---

# 2. Core Principle

> **Trust is not something the capability claims. It is something the capability continuously earns through how it behaves.**

Trust determines:

- what can reasonably be believed
- what can be used
- what can move downstream
- what the capability may do
- where human judgment belongs
- what requires review
- when the capability should stop
- when authority can expand
- when authority must shrink
- what the organization can later reconstruct and defend

The goal is not maximum trust.

The goal is:

> **Appropriate reliance, appropriate authority, and defensible action.**

---

# 3. Unit of Trust

Do not ask:

> Is this AI trustworthy?

Ask:

> **Can this commercial capability be relied upon for this job, in this context, under these conditions, with this level of authority?**

The unit of trust is:

**Capability + Job + Context + Evidence + Authority + People + Workflow + Current State**

---

# 4. Trust Operating Loop

Every material capability should follow:

**Sense → Interpret → Constrain → Express → Control → Propagate → Record → Re-evaluate**

### Sense
Detect missing, conflicting, stale, changed, unexpected, unauthorized, or uncertain conditions.

### Interpret
Determine whether the condition matters to the current job or decision.

### Constrain
Change what the capability may claim or do.

### Express
Make the relevant condition understandable to the right person.

### Control
Give that person the appropriate action, override, approval, escalation, or stop mechanism.

### Propagate
Carry important evidence, limits, permissions, and uncertainty downstream.

### Record
Preserve what happened and why.

### Re-evaluate
Update trust and authority when evidence or conditions change.

---

# 5. Trust Expression Architecture

Trust exists at four levels.

## A. Trust Infrastructure

Usually invisible.

Preserve:

- data and source provenance
- evidence lineage
- versions
- assumptions
- rules
- model/configuration where material
- permissions
- ownership
- approval state
- decision history
- changes
- overrides
- exceptions
- use restrictions
- organization/client boundaries
- audit history

---

## B. Capability Behavior

Trust must change behavior.

The capability may:

- proceed
- verify
- narrow
- ask
- pause
- reroute
- escalate
- require review
- block
- suspend
- withdraw a previous conclusion

A warning that changes nothing is not a meaningful control.

---

## C. Trust Surfaces

Users may experience trust through:

- status
- evidence views
- source links
- provenance
- redlines
- change alerts
- approval states
- review queues
- exception queues
- warnings
- disabled actions
- previews
- undo
- decision history
- audit views
- metrics

There should be **no universal Trust UI**.

Expression depends on the role, context, consequence, and moment.

---

## D. Organizational Record

The company should be able to reconstruct:

- what happened
- what evidence was available
- what was missing
- what the system concluded
- what AI did
- what humans decided
- what changed
- which rules applied
- what was approved
- what moved downstream
- who had authority
- what ultimately occurred

---

# 6. Core Product Principles

## Principle 1: Trust the capability, not the component

Model performance does not prove capability performance.

The full system must work across data, context, AI, tools, workflow, humans, controls, and downstream execution.

**Examples**

- Retrieval performs well but misses a critical exception. The capability downgrades the conclusion rather than presenting it as complete.
- A prediction model is accurate, but planners repeatedly override its recommendations. The model remains validated while the capability stays in an unresolved workflow-fit state.

---

## Principle 2: Evidence earns permission

Capability does not equal authority.

Evidence must justify the specific action being permitted.

**Examples**

- An agent may draft client communications before it earns permission to send them.
- A targeting capability may recommend account priority before it earns authority to change CRM targeting automatically.

---

## Principle 3: Trust must change behavior

Important uncertainty, conflict, failure, or change must alter what the capability does.

**Examples**

- A required source becomes stale, so a recommendation moves from **Current** to **Recheck required**.
- A claim conflicts with an approved use condition, so external distribution is blocked rather than merely flagged.

---

## Principle 4: Preserve what is known, inferred, assumed, and unknown

Do not collapse evidence and interpretation.

**Examples**

- **Observed:** five market-access roles were posted.  
  **Inferred:** launch preparation may be increasing.
- Agency analysis identifies a performance increase but does not call the campaign causal because targeting changed at the same time.

---

## Principle 5: Make the right thing visible at the right moment

Trust information should be progressively disclosed.

Normal work should remain simple. More detail should appear as uncertainty, novelty, disagreement, or consequence rises.

**Examples**

- A field user sees **Approved for use**, not the complete evidence graph.
- An MLR reviewer can expand the same asset into claim-level evidence, changes, and decision history.

---

## Principle 6: Preserve human judgment and decision rights

Do not use “human in the loop” as a generic safeguard.

Define who decides what.

**Examples**

- AI identifies an unusual commercial pattern; the brand lead decides whether it changes strategy.
- An agency produces a recommendation; client leadership retains the final commercial decision.

---

## Principle 7: Trust must travel with the work

Evidence, limits, permissions, and conditions cannot disappear at handoffs.

**Examples**

- A claim approved only for HCP use remains restricted when another capability tries to reuse it elsewhere.
- An agency recommendation marked as dependent on a segmentation assumption carries that dependency into the client deliverable.

---

## Principle 8: Organizational boundaries are part of trust

Commercial capabilities often operate across companies.

Client data, confidential information, permissions, ownership, and reuse rights must remain explicit.

**Examples**

- Client A knowledge cannot silently influence Client B work.
- An agency asset may be reusable internally but prohibited from reuse across brands or clients.

---

## Principle 9: Auditability, traceability, and observability should be built in

The capability should preserve enough information to explain and reconstruct consequential work.

Users should not have to manually create that record.

**Examples**

- A reviewer can reconstruct source → AI transformation → human edit → approval → final output.
- A capability owner can see repeated overrides and discover that missing access data is causing them.

---

## Principle 10: Trust is reversible

Previously earned permission is conditional.

Material changes can reduce authority.

**Examples**

- A model change triggers reassessment before autonomous execution resumes.
- A new client strategy invalidates assumptions behind several agency deliverables, moving them to **Review needed**.

---

## Principle 11: Learning does not automatically increase authority

The capability may learn from use without silently expanding what it can do.

**Examples**

- Override patterns improve future recommendations but do not automatically authorize autonomous execution.
- An agency capability learns a client's preferred planning format but does not reuse confidential strategic content elsewhere.

---

## Principle 12: Make the next move defensible

The capability should help people decide what to do next without manufacturing certainty.

**Examples**

- Weak competitive evidence produces **Monitor these two signals**, not **Competitor launch imminent**.
- A questionable source produces **Verify before client use**, not an unsupported recommendation.

---

# 7. Minimum Trust Payload

Every consequential output or action should preserve:

### Claim or action
What is being asserted or done?

### Evidence
What supports it?

### Provenance
Where did the evidence come from?

### Epistemic state
What is observed, inferred, assumed, or unknown?

### Conditions
When is the conclusion valid?

### Authority
What may the capability and the person do?

### Ownership
Who is accountable for the next decision?

### Restrictions
Audience, market, channel, client, regulatory, confidentiality, reuse, or other limits.

### Next move
What is the smallest defensible action?

### History
What changed and what decisions produced the current state?

This payload may remain mostly invisible, but it must travel with the work.

---

# 8. Core Trust Surfaces

A capability should select the appropriate expression rather than expose everything.

| Surface | Answers |
|---|---|
| **State** | Where does this stand? |
| **Evidence** | Why should I rely on it? |
| **Provenance** | Where did it come from? |
| **Change** | What changed since it was trusted? |
| **Authority** | What may happen now? |
| **Control** | What can I approve, reject, change, stop, or undo? |
| **Judgment** | What actually requires human review? |
| **Boundary** | What use is permitted? |
| **History** | How did we get here? |
| **Observability** | Is the capability behaving normally? |
| **Audit** | Can the work be reconstructed later? |
| **Measurement** | What conditions are actually being observed? |

---

# 9. Role-Specific Trust

The same underlying capability should express trust differently by role.

### Commercial user
Can I use this? What should I do?

### Agency strategist
What came from evidence versus our interpretation?

### Analytics
What was measured, inferred, or causally established?

### Medical / Legal / Regulatory
What requires judgment, and what evidence supports it?

### Field
Is this approved and appropriate for this use?

### Client lead
What is agency recommendation versus client decision?

### Capability owner
Where is performance, trust, or authority degrading?

### Compliance / Audit
Can the complete history be reconstructed?

Different experience.

Same underlying trust state.

---

# 10. Progressive Trust Disclosure

Use the least intrusive expression that preserves appropriate reliance.

### Normal condition
Keep trust mostly quiet.

> Approved for use

### Material context
Show relevant detail.

> Approved for HCP use only

### Meaningful uncertainty
Make it visible.

> Current evidence incomplete

### Changed dependency
Interrupt normal flow.

> Review required: underlying source changed

### Consequential conflict
Block or escalate.

> Cannot publish until this issue is resolved

Trust UI should scale with consequence.

---

# 11. Trust States

Recommended common states:

- **Exploratory**
- **Evidence incomplete**
- **Assisted**
- **Review required**
- **Authorized**
- **Authorized with conditions**
- **Restricted**
- **Suspended**
- **Superseded**
- **Revoked**

State must change what the capability can do.

---

# 12. Pharma and Regulated Contexts

Regulated workflows are one context within the broader architecture.

Capabilities may need to incorporate, where relevant:

- promotional review
- approved claims and content
- labeling
- medical/legal/regulatory review
- privacy
- security
- consent
- records requirements
- company policy
- market restrictions
- channel restrictions
- audience restrictions
- pharmacovigilance or escalation requirements
- contractual obligations

Do not encode every capability as an MLR workflow.

Instead:

> **Determine which requirements apply to this capability, job, organization, data, and action.**

---

# 13. Agency and Cross-Organization Requirements

Where work crosses organizational boundaries, preserve:

- client ownership
- data permissions
- confidentiality
- source ownership
- IP and reuse rights
- client-specific assumptions
- decision responsibility
- approved uses
- cross-client separation
- version and brief fidelity
- handoff integrity

Trust should survive the handoff from:

**client → agency → capability → agency team → client → downstream execution**

---

# 14. Security and Privacy

Security and privacy should operate primarily as capability constraints, not banners.

The capability should know:

- what data it may access
- why access is allowed
- where data may move
- what systems may process it
- what may be retained
- what must remain separated
- who may see or change it

Violations should change behavior automatically.

The UI should surface the restriction only when the person needs to understand or resolve it.

---

# 15. Failure and Incident Behavior

When trust conditions fail, the capability must not silently continue.

Possible responses:

- narrow
- verify
- ask
- reroute
- escalate
- block
- suspend
- rollback
- withdraw an earlier conclusion
- notify affected owners
- identify downstream impact

Material failures should create an inspectable incident record.

---

# 16. Change and Lifecycle Management

Trust must be maintained from creation through retirement.

Trigger reassessment when material dependencies change:

- model
- prompt
- data
- source
- label or approved content
- strategy
- policy
- workflow
- organization
- user population
- channel
- market
- external environment
- intended use

The key question:

> **Does the evidence that earned this permission still apply?**

---

# 17. Trust Measurement

Avoid universal scores such as:

> Trust score: 87%

Instead measure specific conditions.

Examples:

- 13/14 claims linked to current evidence
- 2 unresolved source conflicts
- 18% of recommendations overridden because of missing context
- 0 unverified autonomous actions in 500 executions
- 6 active outputs affected by a changed dependency
- 92% of review escalations resolved without rework

Measurements should support decisions, not simulate certainty.

---

# 18. Capability Design Template

For every AI-native commercial capability define:

### Job
What useful outcome should change?

### Actors
Who uses, owns, reviews, receives, or is affected by it?

### Organizational boundaries
Which companies, teams, or systems does it cross?

### Inputs and dependencies
What must remain true?

### Trust conditions
What must be reliable?

### Evidence standard
What proves that?

### Authority
What may the capability do?

### Human judgment
Where and why is it needed?

### Trust expressions
What does each role need to see?

### Controls
What can people approve, change, override, undo, escalate, or stop?

### Propagation
What state must travel downstream?

### Monitoring
What conditions must be watched?

### Failure behavior
What happens when they break?

### Auditability
What must be reconstructable?

### Reauthorization
What changes require trust to be re-earned?

---

# 19. Trust Expression Matrix

For every material trust condition document:

| Field | Question |
|---|---|
| **Condition** | What must remain trustworthy? |
| **Infrastructure** | What must be captured underneath? |
| **Behavior** | What changes if the condition changes? |
| **Expression** | How is that made visible? |
| **Audience** | Who needs to know? |
| **Moment** | When do they need to know? |
| **Control** | What can they do? |
| **Propagation** | What travels downstream? |
| **Record** | What must remain reconstructable? |

This is the core operational instrument.

---

# 20. Acceptance Criteria

A capability satisfies **Trust Is the Product** only when:

1. Trust is evaluated end to end, not at the model level.
2. Evidence supports the authority granted.
3. Important uncertainty changes behavior.
4. Human judgment and decision rights are explicit.
5. Role-specific trust expression exists.
6. Important trust state travels downstream.
7. Cross-company boundaries are preserved.
8. Security, privacy, and data-use limits affect behavior.
9. Auditability and traceability are built in.
10. Material changes trigger reassessment.
11. Failure produces a behavioral response.
12. Users retain appropriate control.
13. Learning cannot silently expand authority.
14. Trust conditions can be monitored.
15. The organization can reconstruct consequential decisions.
16. Measures describe real conditions rather than abstract “trust.”
17. The capability helps produce a defensible next move.

---

# 21. Anti-Patterns

Avoid:

- generic “trustworthy AI” language
- confidence scores without meaning
- warnings that do not change behavior
- compliance logs disconnected from the work
- requiring approval for every low-risk action
- hiding uncertainty to simplify the UI
- exposing every control to every role
- model testing presented as capability validation
- human review without defined decision rights
- approval states that lose their conditions downstream
- agency/client handoffs that strip away assumptions
- silent reuse of confidential or client-specific context
- learning that silently expands permission
- static approval when important dependencies have changed

---

# 22. Canonical Definition

> **Trust Is the Product means an AI-native commercial capability continuously earns reliance through how it behaves.**
>
> It preserves evidence, context, boundaries, and decision history.
>
> It changes its claims and authority when conditions change.
>
> It makes the right information visible to the right person at the right moment.
>
> It preserves human and organizational decision rights.
>
> It carries trust conditions across workflows and organizational boundaries.
>
> And it leaves consequential work defensible, traceable, and reconstructable.

The user should not need to think:

> “Can I trust this AI?”

They should develop a reliable expectation:

> **“I know how this capability behaves when it knows, when it does not know, when something changes, when it reaches its boundary, and when it needs human judgment.”**