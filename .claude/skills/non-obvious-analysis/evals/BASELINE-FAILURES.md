# Baseline Failure Hypotheses

## Status

These are expected failure modes derived from the original monolithic prompt and the design review. They are **not** claims from completed model runs.

Run the prompts in `evals.json` without the skill in clean contexts and replace the hypotheses below with observed behavior and exact excerpts.

## Expected baseline failures

### 1. Mechanical method application

The model may produce a section for every named method whether or not the method adds value.

**Why expected:** The original prompt says to always apply all ten methods and provides a mandatory section for each.

### 2. Forced insight quantity

The model may return four insights even when the source supports fewer.

**Why expected:** The original prompt specifies a minimum of four and asks for surprising or shocking insights.

### 3. Manufactured novelty

The model may exaggerate ordinary observations or introduce speculative mechanisms to satisfy the novelty requirement.

**Why expected:** Novelty is treated as an output quota rather than as a conclusion that must survive evidence tests.

### 4. Evidence and inference blending

The model may cite a source observation and then attach a stronger causal claim without labeling the inferential step.

**Why expected:** The original response format asks for evidence but does not define observation, inference, hypothesis, or confidence.

### 5. Duplicate insights

The model may express the same mechanism through several lenses and count each formulation as a separate insight.

**Why expected:** Each method is applied independently and the prompt does not include a distinctness test.

### 6. Generic recommendations

The model may append actions such as "align stakeholders," "gather more data," or "create a roadmap" that are not derived from a specific insight.

**Why expected:** The checklist asks for actionability and next steps but does not require traceability from insight to action.

### 7. Invented stakeholder context

The model may fabricate stakeholder roles, motivations, or power relationships when the source does not identify them.

**Why expected:** The response format requires primary and secondary stakeholders regardless of source completeness.

### 8. Excessive output

The model may produce a long response dominated by process narration rather than a small number of decision-relevant conclusions.

**Why expected:** The original prompt mandates multiple overlapping sections and a broad generic checklist.

## Baseline record template

For each eval, capture:

```markdown
### Eval [ID]

- **Observed failure:**
- **Exact excerpt:**
- **Which pressure caused it:**
- **Did the output still contain useful behavior:**
- **Skill instruction intended to correct it:**
```
