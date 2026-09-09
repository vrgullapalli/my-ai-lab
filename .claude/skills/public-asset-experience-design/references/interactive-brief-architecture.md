# AI-Made Interactive Brief — Shared Architecture

> CANON — Venkat, 2026-08-31, recorded verbatim; revised the same day
> to add §2 (the landing page) and the landing-first canonical
> experience. Companion to the AI-Native Executive Instrument Design
> Standard (same directory): the standard governs what an instrument
> IS; this architecture governs how an interactive experience TEACHES
> and how its page frames it. Test classes (input, model, decision,
> teaching, edge integrity) and the measures section are enforced at
> `public-asset-qa`.


An AI-made interactive brief is a compact, interactive experience designed to help someone **understand an idea, see how it works, and make a better decision because of it**.

Its core loop is:

**Context → Model → Interaction → Consequence → Explanation → Learning → Action**

## 1. Start with the learning and decision

Define two things before designing anything:

### Learning objective

What should the user understand differently after using the brief?

### Decision objective

What should the user be better able to decide, question, prioritize, or do?

**Start with the decision, not the data.** Design backward from the action the user should take.

The brief should not begin with available data, charts, or features. It begins with the user's question and the change in understanding or action the experience should create.

## 2. Landing page

The landing page should do only enough to establish relevance, trust, and momentum.

### Directional layout

**Hero**

* Name the problem or tension.
* State what the brief helps the user understand or decide.
* Make the value obvious within seconds.
* One primary CTA into the interactive brief.

**Why this matters**

* Briefly explain the consequence of getting the issue wrong.
* Use one strong insight, example, or tension rather than a long explanation.

**What you'll explore**

* Preview the key variables, tradeoffs, or questions the user will interact with.
* Show enough of the instrument to make it tangible.

**Interactive brief**

* Make the instrument the dominant element on the page.
* Bring users into interaction quickly rather than forcing them through long copy first.

**What to take away**

* Summarize the underlying lesson or mental model.
* Connect the interactive result back to the broader idea.

**Next step**

* One clear continuation path: another asset, deeper analysis, export, conversation, or related brief.

### Landing-page principles

* The page should **frame the experience, not compete with it**.
* Keep copy short and outcome-led.
* Avoid a traditional marketing-page sequence with excessive sections.
* Show the instrument early.
* Let interaction do much of the persuasion.
* Maintain one dominant CTA and one obvious path forward.
* Use progressive disclosure for methodology, evidence, and deeper explanation.

## 3. Define the core model

Identify the smallest useful model that explains the idea.

This may include:

* relationships,
* thresholds,
* tradeoffs,
* causal links,
* policies,
* assumptions,
* constraints,
* scenarios.

The model should be explicit enough that the user can understand why an outcome changes.

## 4. Choose the interactive variables

Let the user manipulate only the variables that help reveal the model.

Interaction should teach.

A slider, toggle, editable field, scenario, or comparison belongs only when changing it helps the user understand:

* what matters,
* what does not,
* what changes the outcome,
* where the boundaries are,
* or why two situations produce different results.

**Signal over noise.** Every element earns its place. Highlight exceptions and meaningful differences rather than displaying everything equally.

## 5. Show consequence immediately

When the user changes something, the brief should visibly respond.

Show:

* what changed,
* how much it changed,
* whether the status changed,
* what became more or less important,
* what new exception appeared.

The user should be able to build intuition through interaction.

## 6. Explain why

Do not leave the user with a changing number alone.

Explain the mechanism behind the change:

* which variable mattered,
* which rule fired,
* what assumption became binding,
* what threshold was crossed,
* or what tradeoff changed.

**Clarity beats cleverness.** Prefer simple charts, familiar interaction patterns, plain language, and benefit-driven copy.

## 7. Design the information hierarchy

Use a consistent three-tier hierarchy.

### Top: Status / headline answer

Immediately answer the main question.

Examples:

* Ship / Hold
* Healthy / At risk
* Within SLA / Breached
* Profitable / Unprofitable
* Ready / Not ready

### Middle: Context

Show the small number of signals needed to understand the headline result.

Include:

* material drivers,
* key comparisons,
* important thresholds,
* exceptions,
* concise explanation.

### Bottom: Drill-down

Make deeper detail available when needed:

* assumptions,
* calculations,
* source data,
* methodology,
* evidence,
* history,
* edge cases.

**Progressive disclosure.** Answer the headline question immediately. Make depth available on demand.

## 8. Give the user one primary action

Every brief should lead somewhere.

Examples:

* change the scenario,
* inspect the exception,
* fix the missing evidence,
* compare another case,
* export the conclusion,
* continue to the next relevant asset.

**One primary action.** One CTA, one conversion goal, one obvious next step.

Secondary controls should never compete with the main action.

## 9. Make trust visible

The brief should make it easy to understand why its output deserves attention.

Expose, where relevant:

* source attribution,
* data freshness,
* methodology,
* assumptions,
* logic version,
* unresolved uncertainty,
* missing data,
* error conditions.

**Trust is the product.** Fresh data, source attribution, methodology transparency, and graceful error states are part of the experience, not implementation details.

Never create false confidence when inputs are incomplete or invalid.

## 10. Protect the lesson with tests

Tests exist not only to keep the application working, but to protect the truthfulness of the experience.

Validate:

### Input integrity

Are required inputs present and valid?

### Model integrity

Are calculations and relationships internally consistent?

### Decision integrity

Can the interface accidentally show a misleading PASS, GO, Complete, or equivalent state?

### Teaching integrity

Can the interaction imply something the underlying model does not support?

### Edge cases

What happens at zero, missing values, extreme values, thresholds, or contradictory inputs?

Materially different inputs should be capable of producing materially different conclusions.

## 11. Design for real-world use

**Mobile-first, performance-first.** Design for the smallest screen and slowest connection first.

The core learning loop must still work at small screen sizes.

Prioritize:

* immediate render,
* low interaction cost,
* readable typography,
* minimal controls,
* touch-friendly targets,
* restrained visualization,
* graceful degradation.

## 12. Leave the user with a portable understanding

The experience should end with more than a result.

The user should leave able to:

* explain the underlying idea,
* recognize the pattern elsewhere,
* understand what drives the outcome,
* know what to inspect next,
* or make a better decision.

Where useful, provide an exportable takeaway containing:

* headline conclusion,
* key drivers,
* assumptions,
* important exceptions,
* next action,
* methodology/version.

## 13. Test, iterate, evolve

Treat the brief itself as a product.

**Test, iterate, evolve.** A/B test meaningful experience choices and measure whether users reach understanding and decisions faster, not just whether they click.

Useful measures may include:

* time to first understanding,
* time to decision,
* completion rate,
* interaction depth,
* number of unnecessary steps,
* change in confidence,
* ability to correctly explain the concept afterward,
* conversion to the intended next action.

## Core design principles

1. **Start with the decision, not the data.**
2. **Teach one important idea.**
3. **Make the underlying model visible.**
4. **Use interaction to reveal cause and consequence.**
5. **Signal over noise.**
6. **Use a three-tier hierarchy: status, context, drill-down.**
7. **Give the user one primary action.**
8. **Trust is the product.**
9. **Clarity beats cleverness.**
10. **Use progressive disclosure.**
11. **Design mobile-first and performance-first.**
12. **Test whether the experience improves understanding and decision speed.**

## Canonical experience

**Landing page → Headline question → Interactive brief → Manipulate → See consequence → Understand why → Inspect depth → Take action**

That is the reusable architecture underneath the interactive brief.
