---
name: public-asset-qa
version: 1.0.0
description: >
  Judges whether a finished public asset is actually useful and good —
  separate from privacy and safety. Triggers on: asset QA, is this asset
  good, quality pass on the asset, review the finished asset.
---

# Public asset QA

> **Base directory:** all relative paths in this skill resolve from `work-os/brand-os/engagement-os/`
> (lab root: `/Users/venkatgullapalli/Documents/my-ai-lab/`). Consolidated to the lab-root
> `.claude/skills/` on 2026-09-07 so it runs from anywhere; its data stayed put.

PROJECT-SPECIFIC to this lab (`my-ai-lab`; the older project name it used to carry was retired in the 2026-09-10 rule audit). Never install globally. Never
publishes or sends anything.

Safety says it may ship. QA says it is worth shipping. Different
questions; this skill answers only the second. Where practical, run the
evaluation in a fresh-context reviewer (a subagent given the artifact
and this rubric, not the build conversation) so the builder is not
grading their own work.

## Inputs

The built asset AND its **Experience Spec**
(`assets/experience/<ASSET-ID>--spec--<date>.md`, from
`public-asset-experience-design`). Experience design asked "what
experience should we create?"; QA asks "**did we actually create
it?**" — against the SAME standards the spec declared applied
(general, executive, demand gate, AI-native). An asset that predates
the experience stage is graded against the general standard and the
gap is noted. A missing spec for a full-path asset is itself a
finding: development invented the experience.

## Five dimensions, never averaged

Judgment quality · experience quality · executive experience quality
(when the spec applied that standard) · commercial experience quality
(when the demand gate applied) · technical/accessibility quality. One
convenient score never hides a failure; a near-zero on any important
dimension is grounds for REVISE or HOLD on its own.

## The rubric

- **Value** — does it create meaningful progress, or restate the known?
- **Recognition** — will the intended person see their situation in the
  first screen?
- **Core idea** — is the one-week-later message unmissable?
- **Judgment** — does the experience demonstrate judgment, or claim it?
- **Genericity** — could a general model or a generic checklist produce
  substantially this? If yes, it fails; that is the bar the examiner
  position sets.
- **Experience fit** — does the format match the job?
- **Cognitive load** — is it asking too much of a busy person?
- **Voice** — under-claim, evidence-dense, no invented terms, no
  category boilerplate; matches the public-site register where it
  applies. AND the positioning ruling (2026-08-30): the author reads as
  a strategic advisor to accountable executives — flag any operator or
  day-to-day language ("do the work," delivery detail without a
  judgment purpose, hands-on framing) as a failure, not a style note.
- **Evidence** — does confidence match support? Every number sourced?
- **Actionability** — can someone use it tomorrow without the author in
  the room?
- **Portability** — does the result travel when forwarded?

For any interactive asset, apply the canonical instrument standard
(`../public-asset-experience-design/references/ai-native-instrument-design-standard.md`):
run its §14 Instrument Design Test dimension by dimension, its §15
Primary Acceptance Test and AI-native recovery test as pass/fail, and
its §16 twenty evaluation questions — an element that cannot justify
itself against them is a finding. Verify the §17 governing sequence
(Recognition → Expectation → Interaction → Insight → Consequence →
Control → Action → Depth) and that reassurance sits beside any
friction (§6.6).

For AI-native assets, additionally test with real input variation:
meaningfully different inputs must produce meaningfully different,
coherent routes or outputs; inappropriate inputs must be refused;
behavior must be reproducible to the degree the asset type promises;
and the AI must demonstrably perform work a static version could not.

## Real-user validation

AI self-review and real-user evidence are different things; never
present the first as the second. RECOMMEND real-user validation (a
small number of representative users, tasks framed around their real
goals, not "click through this prototype") when the asset is
consequential, the experience novel, the audience specialized,
interaction nontrivial, comprehension genuinely uncertain, or failure
reputationally expensive. Observe hesitation, misunderstanding,
language mismatch, backtracking, abandonment, what they remember, and
whether the result works without help. Participant suggestions are
evidence for `docs/candidate-learnings.md`, never automatic
requirements.

## Output contract

Write `assets/qa/<ASSET-ID>--qa--<date>.md` (PRIVATE).
Verdict first: **PASS / REVISE / HOLD**, with the human rationale — what
is strong, what fails, what one change matters most. Machine detail
(per-criterion notes, test inputs and outputs for AI-native) after.
