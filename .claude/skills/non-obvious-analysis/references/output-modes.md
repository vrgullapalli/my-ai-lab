# Output Modes

Use the user's requested format. When no format is specified, use standard mode.

## Contents

- Brief mode
- Standard mode
- Deep mode
- Signal mode
- No-earned-insight mode
- Audience adaptation
- Method visibility

## Brief mode

Use when the user asks for a quick take, an executive read, or a small number of bullets.

```markdown
## The apparent issue

[One or two sentences.]

## What may be easy to miss

1. **[Insight]**: [Evidence-based explanation and why it matters.]
2. **[Optional second insight]**: ...

## What changes

- **Reconsider:** ...
- **Test next:** ...
- **Confidence:** ...
```

Rules:

- Return one to three insights.
- Keep evidence attached to each insight.
- Include one uncertainty that could change the conclusion.
- Do not include a methods section.

## Standard mode

This is the default.

```markdown
## What this appears to be

- **Surface reading:** ...
- **Primary stakeholder:** ...
- **Stakeholder tension:** ...
- **Core problem:** ...

## What may actually be going on

### 1. [Insight]

- **Why it is easy to miss:** ...
- **Evidence:** ...
- **Counterevidence or competing explanation:** ...
- **Interpretation:** Inferred | Hypothesized
- **Why it matters:** ...
- **Confidence:** ...
- **What would change this conclusion:** ...

## The insight that matters most

...

## What changes now

- **Reconsider:** ...
- **Next action or test:** ...
- **Critical uncertainty:** ...
```

Rules:

- Return one to four earned insights.
- Keep the surface framing short.
- The top insight is selected by decision consequence, not novelty alone.

## Deep mode

Use when the user asks for comprehensive analysis, multiple perspectives, system effects, or a reusable analytical artifact.

```markdown
## 1. Frame

- Material and scope
- Primary and secondary stakeholders
- Decision or unresolved tension
- Source and verification boundaries

## 2. Surface reading

- Apparent explanation
- Core problem in one sentence

## 3. Evidence map

- Strong observations
- Contradictions
- Missing information
- Assumptions
- Incentives and dependencies

## 4. Non-obvious insights

[Use the full insight fields from standard mode.]

## 5. Competing explanations

- Alternative explanations
- Evidence for and against each

## 6. Second and third-order implications

- Likely effects
- Conditional effects
- Risks of intervention

## 7. Decision implications

- What changed in the interpretation
- What to stop, continue, test, or decide
- Critical unknowns
```

Rules:

- Depth does not increase the maximum insight count beyond four.
- Expand evidence and alternatives, not rhetorical repetition.
- Name analytical lenses only when requested.

## Signal mode

Use when analyzing a market, research, competitive, product, customer, or operating signal for a recurring brief.

```markdown
## SIGNAL

- **What happened:** ...
- **Evidence quality:** ...
- **Obvious explanation:** ...

## NON-OBVIOUS ANALYSIS

### Insight 1: ...

- **Observation:** ...
- **Why it is non-obvious:** ...
- **Supporting evidence:** ...
- **Counterevidence or competing explanation:** ...
- **Practical implication:** ...
- **Confidence:** ...

[Repeat only for one to four earned insights.]

## VALUE

- **Fast Value:** What can help someone within two minutes?
- **Deeper Asset:** What larger job becomes visible if the fast value works?
- **Learning Question:** What uncertainty would most change the interpretation?
- **Long-Term Value:** What durable capability could emerge if the problem keeps proving real?

## DECISION

- **What changed in our beliefs:** ...
- **State:** IGNORE | MONITOR | INVESTIGATE | TALK | TEST | DEVELOP | ACT
```

Rules:

- Choose exactly one decision state.
- Do not promote a signal to action merely because it is interesting.
- Keep signal, interpretation, value, and decision as separate layers.
- Use the best-fit lenses rather than a fixed checklist.

## No-earned-insight mode

Use when the evidence does not support a non-obvious conclusion.

```markdown
## What the material supports

...

## What it does not yet support

...

## What would unlock deeper analysis

...
```

Do not apologize. Do not manufacture a weak insight to satisfy the requested count.

## Audience adaptation

### Executive audience

Lead with the changed decision, risk, or opportunity. Minimize method language.

### Practitioner audience

Include mechanisms, dependencies, and the next test in more detail.

### Research audience

Make evidence boundaries, competing hypotheses, and confidence calibration explicit.

### Public-facing asset

Use plain language, protect confidential details, and separate transferable principle from client-specific evidence.

## Method visibility

If the user explicitly asks which methods were applied, add a short appendix:

```markdown
## Lenses that produced useful evidence

- **[Lens]:** [What it revealed.]
```

List only methods that contributed to a surviving insight. Never reproduce private chain-of-thought.
