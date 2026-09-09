---
name: non-obvious-analysis
description: Use when a user wants supplied material examined for hidden assumptions, structural patterns, non-obvious implications, second-order effects, power or incentive dynamics, strategic opportunities, or insights others may miss. Applies to reports, research, plans, case studies, meeting notes, market signals, and business problems. Do not use for straightforward summarization, extraction, rewriting, translation, or simple fact lookup.
metadata:
  version: "0.1.0"
---

# Non-Obvious Analysis

> **Base directory:** all relative paths in this skill resolve from `work-os/brand-os/engagement-os/`
> (lab root: `/Users/venkatgullapalli/Documents/my-ai-lab/`). Consolidated to the lab-root
> `.claude/skills/` on 2026-09-07 so it runs from anywhere; its data stayed put.

## Purpose

Find the few evidence-grounded insights that materially change how a stakeholder understands a problem or acts on it.

**Core principle:** Novelty is not the goal. Earned surprise is.

An insight is earned only when it:

1. Is not merely a restatement of the supplied material.
2. Is traceable to specific evidence or clearly labeled as a hypothesis.
3. Explains a mechanism, relationship, contradiction, or implication.
4. Changes a belief, decision, priority, risk, or opportunity.
5. Survives at least one plausible alternative explanation.

Return **one to four insights only when earned**. Returning zero is valid and preferable to manufacturing novelty.

## When to use

Use this skill when the user asks to:

- Find what others are missing.
- Rethink a report, plan, case study, recommendation, or signal.
- Surface hidden assumptions, tensions, incentives, or dependencies.
- Identify second or third-order effects.
- Connect apparently unrelated elements.
- Reframe an apparent problem around its deeper mechanism.
- Turn analysis into decision-relevant implications or opportunities.

Do not use this skill when the task is only to:

- Summarize or extract information.
- Rewrite, edit, translate, or proofread.
- Look up or verify a simple fact.
- Explain a thinking method in the abstract.
- Generate provocative claims without source material.

If a broader task contains both straightforward work and non-obvious analysis, apply this skill only to the analytical portion.

## Defaults

Unless the user says otherwise:

- Use **source-bound mode**: analyze only the supplied material.
- Use the **standard output mode**.
- Infer the primary stakeholder and decision only when the material supports the inference. Label material assumptions.
- Do not display the full analytical process or private chain of thought. Present concise conclusions, evidence, uncertainty, and decision logic.
- Do not enumerate every analytical method. Name methods only when the user asks or when method visibility materially improves the result.

Use external verification only when the user requests it, when current or high-stakes facts materially affect the analysis, or when governing tool instructions require it. If verification tools are unavailable, state the limitation and keep external claims out of the analysis.

## Required references

Use the reference files through progressive disclosure:

- Before selecting final insights, read [references/insight-quality-standard.md](references/insight-quality-standard.md).
- When evidence, citations, uncertainty, current facts, or source boundaries matter, read [references/evidence-and-confidence.md](references/evidence-and-confidence.md).
- When choosing analytical lenses or when the obvious framing is not yielding useful candidates, read [references/analytical-lenses.md](references/analytical-lenses.md).
- When the user requests a particular depth, audience, or response shape, read [references/output-modes.md](references/output-modes.md).
- When application is unclear, read [references/worked-examples.md](references/worked-examples.md). Do not copy its conclusions into unrelated work.

## Analysis workflow

Track the workflow privately. Do not print a progress checklist unless the user asks.

### 1. Frame the real analytical job

Identify:

- The material being analyzed.
- The primary stakeholder, if supported.
- The decision, tension, frustration, or unresolved question.
- The intended audience and level of detail.
- Whether the task is source-bound or verification-enabled.

Ask a question only when the missing answer would materially change the analysis. Otherwise make a narrow assumption and label it.

### 2. Establish the obvious reading

Briefly state:

- What the material appears to say.
- The most obvious explanation.
- The stakeholder tension.
- The core problem, reframed in one sentence.

This baseline is required. An insight can be called non-obvious only relative to a defined obvious reading.

### 3. Build an evidence map

Privately record:

- Explicit observations and claims.
- Repeated patterns.
- Contradictions and anomalies.
- Supporting, disconfirming, and non-diagnostic evidence.
- Missing or underemphasized information.
- Unstated assumptions.
- Actors, incentives, dependencies, constraints, and feedback loops.

Keep evidence separate from interpretation. Do not treat an analogy, intuition, or plausible story as source evidence.

### 4. Select analytical lenses

Choose the **smallest useful set of lenses**, usually two to four, most likely to expose a material mechanism. One lens is enough when it does the job. Do not apply every available lens.

Use the selection guidance in `references/analytical-lenses.md`. A lens is useful only if it generates a candidate insight that survives the quality tests.

### 5. Generate candidate insights

Draft candidates as causal or structural claims:

> Because **X and Y interact**, the apparent problem **Z** may actually be **A**, which changes **B**.

Generate more candidates than will be returned. Do not optimize for provocative wording.

### 6. Challenge each candidate

For each candidate, test:

- **Restatement:** Is this already explicit in the material?
- **Evidence:** Which exact observations support it?
- **Alternative:** What simpler or competing explanation could account for the same evidence?
- **Disconfirmation:** Which observation weakens the candidate or remains unexplained?
- **Materiality:** What belief, decision, risk, priority, or opportunity changes if it is true?
- **Falsifiability:** What evidence would weaken or overturn it?
- **Distinctness:** Is it materially different from the other candidates?

Reject candidates that fail these tests. When several explanations remain plausible, prefer the least-disconfirmed explanation, not the most attractive story.

### 7. Rank and prune

Use the scoring standard in `references/insight-quality-standard.md`.

Remove:

- Restatements dressed as insights.
- Generic strategy advice that could apply to any source.
- Unsupported speculation.
- Duplicate mechanisms expressed with different words.
- Interesting observations with no decision consequence.
- Claims made more dramatic than the evidence permits.

Return the strongest one to four insights. Do not fill empty slots.

### 8. Translate insight into consequence

For every returned insight, explain:

- Why it is easy to miss.
- The specific supporting evidence.
- Counterevidence or the strongest competing explanation.
- Whether the claim is inferred or hypothesized.
- Why it matters to the stakeholder or decision.
- Confidence and the reason for it.
- What evidence would change the conclusion.

Recommendations must follow from the insight. Do not append generic next steps.

## Default response contract

Use this structure unless the user requests another format:

```markdown
## What this appears to be

- **Surface reading:** ...
- **Primary stakeholder:** ...
- **Stakeholder tension:** ...
- **Core problem:** ...

## What may actually be going on

### 1. [Decision-relevant insight]

- **Why it is easy to miss:** ...
- **Evidence:** ...
- **Counterevidence or competing explanation:** ...
- **Interpretation:** Inferred | Hypothesized
- **Why it matters:** ...
- **Confidence:** High | Medium | Low, because ...
- **What would change this conclusion:** ...

[Repeat only for additional earned insights. Maximum four.]

## The insight that matters most

[Select the insight with the greatest decision consequence, not merely the most surprising wording.]

## What changes now

- **Reconsider:** ...
- **Next action or test:** ...
- **Critical uncertainty:** ...
```

## When no strong insight is earned

Do not force the normal template. Use:

```markdown
## What the material supports

[The strongest defensible reading.]

## What it does not yet support

[The conclusions that would exceed the evidence.]

## What would unlock deeper analysis

[The smallest set of missing evidence, comparison, or stakeholder context needed.]
```

## Non-negotiable guardrails

- Do not force four insights.
- Do not use words such as "shocking," "breakthrough," or "counterintuitive" unless the evidence earns them.
- Do not treat all analytical methods as mandatory.
- Do not invent stakeholders, motives, evidence, quotes, data, or citations.
- Do not blend external facts into source-bound analysis.
- Do not present an inference as an observation.
- Do not use cross-disciplinary analogy as proof.
- Do not claim a fact was verified unless verification actually occurred.
- Do not expose hidden chain-of-thought. Provide a concise evidence trail and reasoning summary instead.

## Final quality gate

Before responding, confirm privately:

- Every insight is traceable to specific evidence.
- Every inference or hypothesis is labeled.
- Supporting, disconfirming, and missing evidence were distinguished.
- At least one plausible alternative explanation was considered.
- Each insight changes something material.
- No two insights describe the same mechanism.
- The number of insights is earned by the evidence.
- Recommendations follow from the analysis.
- Current external claims are verified and cited when required.
- The response is no longer than the user's decision requires.
