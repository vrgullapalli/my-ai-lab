---
name: lab-operating-model
what: How the AI Lab's capabilities, operating scopes, actors, connections and real working loops fit together in daily use and evolve over time.
status: working canonical operating model, added 2026-09-13 at Venkat's word (AD-34)
home: docs/architecture/
read_with: CAPABILITY-MAP.md; CAPABILITY-DEFINITIONS.md; ARCHITECTURE-DECISIONS.md
---

# AI Lab operating model

## 1. What the lab is

The AI Lab is a persistent AI-native operating system around Venkat's work and, selectively over time, parts of his personal life.

Its practical job is to help:

> **notice → retrieve → understand → decide → act → observe → learn → carry state forward**

without requiring Venkat to repeatedly reconstruct context or coordinate every routine step.

The lab is also a proving ground for reusable AI-native commercial capabilities.

- **Personal lab:** real work, real consequences, real corrections and outcomes.
- **Commercial proving ground:** realistic pharma/commercial scenarios used to test whether the same capability contracts transfer under different scope, evidence and authority.

The two inform each other without becoming the same thing.

## 2. Design basis: observed + intended jobs

Architecture uses two evidence sets.

### Observed jobs

What Venkat actually asks the lab to do today. The 2026-09-13 reconstruction found recurring jobs such as:

- resume work without rebuilding the situation
- know what was approved and which ruling is current
- carry open/waiting work forward
- coordinate parallel sessions and ownership
- give a brief with one useful next action
- run read-only scans and return decisions
- build shared capabilities against explicit boundaries/tests
- research/write with evidence
- support voice, seeds, signals and public work
- close sessions and preserve recoverable work

Observed jobs expose current friction and implementation priorities.

### Intended jobs

What the lab is deliberately being built toward:

- proactive chief-of-staff behavior
- dynamic context assembly
- continuous sensing and standing reasoning
- learning from corrections, outcomes and repeated patterns
- bounded proactive action
- email/calendar/Drive/other connections
- professional and personal scope separation
- portfolio career and multiple income directions
- products such as Telegraph+
- future specialist actors
- public proof
- future capabilities not yet identified

Intended jobs keep the architecture from simply automating today's workflow.

### Design rule

For every capability ask:

1. **Present:** does this solve jobs we know matter?
2. **Future:** does its contract remain reusable for the system we intend to build?
3. **Simplicity:** can we support both without building speculative machinery?

## 3. Foundational capability model

The working families remain:

1. Context
2. Authority & Control
3. Evidence
4. Memory & State
5. Execution
6. Coordination
7. Evaluation & Observability

Capability Architecture is the meta-capability.

Foundational capability necessity is an architecture decision. Tests evaluate implementation and assumptions, not whether a required capability deserves to exist.

Capability Architecture continuously notices Missing, Weak, Duplicated, Opportunity, Conflict, Drift, Legacy, Unused, Obsolete and Next.

## 4. Four independent dimensions

### Capabilities
What the system can do.

### Operating Scopes
Which world and boundary apply: AI Lab; Professional / Advisory; Career / Portfolio; Public / Content; Personal.

### Actors
Who/what uses or exercises capabilities: Venkat, Alfred, ARCHIE, future specialist agents, automations.

### Connections
Where evidence/events/actions enter or leave: email, calendar, Drive, Dropbox, web, APIs, CRM and future applications.

Do not collapse these dimensions into one another.

## 5. Current actors and systems

### Alfred
Main coordinator and operating interface. Alfred should use shared capabilities rather than become their hidden implementation. He increasingly understands the active job, retrieves evidence, uses State, assembles context, coordinates specialist actors, continues bounded approved work, surfaces material decisions and interrupts only when warranted.

### ARCHIE
Editorial/research specialist. ARCHIE consumes shared Retrieval, Context, Evidence, Memory/State, Authority and Evaluation. Its work should feed durable ideas/evidence back into the wider system rather than form a separate knowledge silo.

### Market Signals
Sensing inputs, not conclusions. Target flow:

**signal → evidence → Retrieval → current context/state → reasoning → belief/action implication → interrupt only if warranted**

Signals do not automatically become seeds, beliefs, opportunities or actions.

### Seedbank
Durable ideas Venkat actually develops, endorses or reacts to. Not a dumping ground for generated possibilities, build notes, lab rules, every signal or every wording candidate.

Useful lifecycle: **generate/discover → use/develop → endorse → persist**.

### Content
Output + learning surface + public proof + capability evidence + potential reusable IP/product input. A piece can simultaneously become evidence of expertise, a framework/instrument, a Career / Portfolio proof point, a product seed, a positioning input and a learning event.

### Career Model
Canonical model of Venkat's capabilities and professional evolution. Do not rebuild it. Its use expands into Career / Portfolio Intelligence:

**market need → capability → evidence → buyer/context language → opportunity/work → new evidence → portfolio evolution**

Portfolio reasoning may also consider income mix, reputation, reusable IP, product opportunities, concentration risk and emerging capability direction. Projections vary by buyer/context but remain traceable to canonical capability/evidence; inference does not silently edit the model.

### Telegraph+
Product objective and proving surface. It should consume shared capabilities rather than recreate them. Its work may expose needs in sensing, Retrieval, State, belief history, Context, Evidence and Learning.

### Public site / public proof
External evidence of the work. Public claims should trace to actual work, evidence, artifacts, capabilities and permitted professional proof.

## 6. Core AI-native operating loop

**SENSE** — What changed?  
↓  
**RETRIEVE** — What evidence do we already have that could materially matter?  
↓  
**STATE** — What is currently true, decided, active, unresolved, waiting or owned?  
↓  
**ASSEMBLE CONTEXT** — What does this job need right now?  
↓  
**REASON** — What does it mean here?  
↓  
**DECIDE** — Does anything need to happen?  
↓  
**ACT** — What may happen within authority?  
↓  
**OBSERVE** — What happened?  
↓  
**LEARN** — What should change in future behavior or implementation?  
↓  
**MEMORY / STATE** — What must persist?

Not every job requires every step.

## 7. Practical build sequence

1. Finish Retrieval v0.1.
2. Implement Minimum Persistent State as a slice of existing Memory & State / continuity.
3. Wire the Morning Brief + One Prepared Next Action as the first integration loop.
4. Build Dynamic Context Assembly through that real loop and at least one other consumer.
5. Extend toward Standing Reasoning.
6. Add the Learning Loop.
7. Expand bounded proactive Action within explicit authority.

These are not seven independent architecture projects. Build the minimum missing capability inside real working loops.

## 8. First integrated proving loop

### Morning Brief + One Prepared Next Action

Job:

> **Tell Venkat where things stand, what materially changed, what needs attention, and the one next action most worth taking.**

It is the first integration proving loop because it is real, daily, low-overhead, already requested, and forces Retrieval + State + Context + Evidence + Authority + Coordination to work together.

It should eventually answer:

- where were we?
- what changed?
- what is still open?
- what is waiting on Venkat?
- which ruling is current?
- what one item most deserves attention?

The morning brief is not the architecture.

## 9. Secondary stress loops

### Signals → Moves
Tests semantic Retrieval, dynamic Context, belief change, Evidence limits, Standing Reasoning and interruption thresholds.

### Rule → Propagate
Tests Authority, current/superseded State, propagation and coordination without silent authority expansion.

### Content → Public Proof
Tests Retrieval, Context, Evidence, Voice, scope, Career/Portfolio proof and reusable outputs.

### Career / Portfolio Opportunity
Tests external need, canonical capabilities, proof, projections, market language, gaps and portfolio direction.

## 10. Connections and personal/professional separation

Connections are added to the shared system, not turned into new capability stacks.

Email can supply commitments, relationships, changes, opportunities and follow-ups; Calendar can supply events, constraints and preparation context; Drive/Dropbox/web/APIs can supply evidence/state and later action surfaces.

Operating Scope governs what may be used. For example, a Personal calendar item may constrain Professional availability without exposing the private reason. Public/Content may use approved professional proof without exposing confidential client material.

## 11. Commercial proving ground

Use the Use Case Registry as the scenario source. Adapt scope, evidence, authority, actors, organizational boundaries and job. ARCHIE/research may make scenarios vivid and source-backed; skeptical review may challenge scenario/evidence credibility.

Commercial tests evaluate implementation portability and usefulness. They do not make foundational capabilities audition for existence.

## 12. Capability evolution

**architecture necessity → operational contract → simplest robust implementation → downstream use → observed limitations/opportunities → implementation or contract refinement**

Do not confuse capability necessity with implementation maturity.

## 13. Capability development model

Default:

> **Operational Spec → one `/goal` → one review**

Claude plans internally, creates representative tests, implements, verifies and may make one local corrective pass. Human handoff is reserved for capability-contract changes, disputed frozen behavior, architecture, authority/scope/privacy boundaries or genuinely durable design forks.

Use Anthropic-native `/goal` prompts: concise references plus TASK / WHY / OUTCOME / CONSTRAINTS / VERIFICATION, with HANDOFF or BOUND only when needed.

## 14. Simplicity rules

Do not create a new agent for every capability, a new store for every workflow, separate Retrieval/Memory stacks by scope, duplicate state systems, speculative connector infrastructure or a new framework for each project.

Prefer shared capabilities, scoped use, deterministic facts/boundaries, AI interpretation where useful, explicit human authority and learning from real downstream use.

## 15. What good daily use feels like

- less repeated explanation
- easy continuation of interrupted work
- current decisions already known
- unresolved work carried forward
- relevant evidence surfaced without a scavenger hunt
- fewer noisy alerts
- one clear next decision/action when useful
- bounded proactive preparation
- easier movement across projects
- content/research/career/product work reinforcing each other
- public claims tied to evidence
- portfolio opportunities connected to actual capabilities
- personal and professional context kept appropriately separate
- AI acts where authorized and exposes uncertainty when it is not

The user experience should increasingly feel like:

> **The system already understands enough of the situation to be useful and makes it obvious when it does not.**
