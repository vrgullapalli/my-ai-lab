---
name: public-asset-experience-design
version: 1.0.0
description: >
  Designs how the intended person actually receives an approved public
  asset's value — the stage between "we know what to make" and "build
  it". Produces a human Experience Recommendation and a build-ready
  Experience Spec. Triggers on: experience design, design the
  experience, how should this asset feel, first value moment, design
  before build, experience spec.
---

# Public asset experience design

> **Base directory:** all relative paths in this skill resolve from `work-os/brand-os/engagement-os/`
> (lab root: `/Users/venkatgullapalli/Documents/my-ai-lab/`). Consolidated to the lab-root
> `.claude/skills/` on 2026-09-07 so it runs from anywhere; its data stayed put.

PROJECT-SPECIFIC to this lab (`my-ai-lab`; the older project name it used to carry was retired in the 2026-09-10 rule audit). Never install globally. Never
publishes, posts, sends, or contacts anyone.

**Purpose.** Design the minimum complete experience that delivers the
approved asset's promised value, protects the person's attention, makes
the judgment understandable, and hands `public-asset-development` (the build stage, written 2026-09-10) an
implementable spec. Design the experience around the value the person
should receive, never around the interface we can build. Optimize for
what the person needs to understand, receive, or be able to do — never
for novelty, feature count, AI visibility, or conversion.

**Position.** After the Gate 1 asset-direction ruling on a Public Asset
Brief; before development. Development implements an approved
experience; it never invents one while coding. Claim verification may
run before or alongside this stage when a proposed experience depends on
a factual capability not yet established.

## Required inputs — stop if missing

Before ANY visual decision, the five pre-design foundations from the
canonical standard's addendum must have written answers: who lands
here and in what role · the decision the instrument supports (every
element passes "would this change what the user does today?") · the
one action it should trigger, in one sentence · the data source,
freshness, and trust model (staleness and unavailability designed,
timestamps and attribution where data is live) · the landing intent
it must match. No answers, no design.

An APPROVED Public Asset Brief (ruling: APPROVED — validate with
`tools/validate_public_value.py brief`); the asset identity and
classification; intended person, moment, job, promised value, intended
result; the proposed primary experience; what is excluded; evidence
constraints; the corpus disposition.

**If AI-native, additionally require** the earned AI-native design
(the evaluation record with verdict earned, plus judgment substrate,
inputs, AI behavior, branches, refusal conditions, uncertainty
behavior, human/AI boundary, acceptance tests). If these do not exist,
STOP — do not invent product logic while designing the experience.

## Two paths

**Lightweight** — simple static assets where the experience is
straightforward (a reference guide): answer the general standard's
questions in a page, produce a short spec. **Full** — mandatory for
AI-native, interactive, multi-step, adaptive, executive-facing,
consequential, decision-supporting, or commercial-role assets, and
whenever cognitive overload is a realistic failure mode. Never
lightweight for AI-native. Do not create ceremony where it adds
nothing.

## Process

1. Load the brief and (if AI-native) the design record. Verify the
   stop conditions below.
2. Apply `references/general-experience-standard.md` — always. Design
   backward from the **first value moment**: the first instant the
   person thinks "this is useful."
2a. For any interactive asset, apply
   `references/ai-native-instrument-design-standard.md` — Venkat's
   canonical AI-Native Executive Instrument Design Standard (ruling
   2026-08-31, verbatim): the governing sequence Recognition →
   Expectation → Interaction → Insight → Consequence → Control →
   Action → Depth, the ten-part page grammar, the AI-native
   principles (known/inferred/unknown, recovery as first-class), and
   the §14–16 test set. Build interfaces from
   `references/pattern-library.md` — purpose-named instrument
   patterns, never atomic primitives. The page around the instrument
   is designed WITH the instrument, never assumed.
3. Apply `references/executive-experience-standard.md` when the
   intended person is a senior leader AND/OR the asset performs
   consequential interpretation, recommendation, or decision support.
4. Apply `references/executive-demand-gate.md` ONLY when the asset also
   carries a commercial role (discovery, warming, proof, lead
   generation, conversion). The commercial role is an overlay; the
   primary user job stays primary.
5. Design the non-happy paths before the happy one is finalized:
   insufficient input, uncertainty, refusal, disagreement, correction,
   no useful finding, stale or superseded information, failure. For
   AI-native assets, uncertainty must never auto-generate confident
   output, and refusal must be a designed, legitimate outcome.
6. Write interface language as part of the design: recognizable words,
   plain verbs, one job per element — "I'd rather not guess" over
   "instrument refusal." The person never learns our internal
   vocabulary to use the asset.
7. Accessibility and cognitive load are requirements, not polish:
   plain language, clear hierarchy, one task at a time, limited visible
   choices, keyboard access, visible focus, contrast, semantic
   structure, reduced motion, no AI theater, no result dumps. No
   invented numeric "load scores" — mechanical signals (choices per
   screen, block counts, repeated explanations) are flags for
   judgment, never verdicts.
8. Where a prototype or the site exists, inspect it as a user — move
   through states, desktop and mobile, screenshots where they sharpen
   judgment — never by reading source alone.
9. Produce the two outputs, validate the spec
   (`python3 tools/validate_public_value.py experience <spec>`), stop.

## Outputs

**Experience Recommendation** (human; written for Venkat). Opens, in
order: *What the experience should do · First value moment ·
Recommended flow · What should win · What we deliberately keep out ·
Special requirements (only those that apply) · Recommendation —
Proceed / Revise / Hold, Strength ★–★★★★★, main reason, main risk,
what would change it.* No IDs, paths, or machine fields needed to
understand it.

**Experience Spec** (machine; consumed by development), at
`assets/experience/<ASSET-ID>--spec--<date>.md`, PRIVATE. Frontmatter:
`asset`, `brief` (path), `classification`, `path` (full|lightweight),
`executive_facing`, `consequential`, `commercial_role`,
`executive_standard`, `demand_gate`, `first_value_moment`, `status`
(draft|approved-for-build), `date`, and `ai_native_design` (path,
AI-native only). Body: states and hierarchy (what wins per screen),
inputs and what each materially changes, branches, progressive
disclosure layers, failure/refusal/correction states, result structure
and portability, next-step rules, accessibility and responsive
requirements, which standards applied and why, acceptance tests.
Venkat is not asked to read this unless it carries a consequential
decision.

## Stop / refuse and route back when

No approved brief · promised value still unclear · person or moment
missing · AI-native claimed without an earned design · the experience
would require evidence the asset does not have · the primary expression
is unresolved in a way that makes design meaningless · brief conflicts
with canonical standards · the design would amount to inventing product
strategy. Name the specific missing decision; never fill the gap
silently. If design work reveals the approved direction itself is
wrong, STOP and recommend revisiting the brief.

## Authority

MAY: design flow, hierarchy, and language; simplify; remove steps;
design failure/refusal/correction states; choose among reversible
experience alternatives consistent with the brief; inspect prototypes;
produce the spec. MAY NOT: change the asset's job, classification, or
audience; invent underlying judgment; change commercial strategy or
standing policy; publish, send, or contact; write production code
(that is the development stage, separately authorized).

## Tools

Existing only: Read/Grep/Glob for briefs, standards, and the corpus;
the browser/webapp tooling already available in this workspace for
prototype walks and screenshots; `tools/validate_public_value.py
experience` for deterministic spec validation. For AI-native assets,
route/refusal test cases are DEFINED here as acceptance tests and
executed at QA; semantic-stability comparisons target structured
decision-relevant fields (reading, priority, evidence state,
recommended action, refusal, confidence), never raw prose.

## Acceptance

A spec is acceptable when the validator passes it, every applicable
standard is marked applied with a reason, the first value moment is
stated, the non-happy paths exist, and `public-asset-qa` could test
the built asset against it without asking what was intended.
