# Evaluation Runbook

Use clean contexts. Run every output-quality case once without the skill and once with the skill.

## 1. Structural validation

From the parent directory:

```bash
skills-ref validate ./non-obvious-analysis
```

Confirm:

- The folder name matches the frontmatter name.
- YAML frontmatter is valid.
- The description is within the specification limit.
- All referenced files exist.
- Both JSON eval files parse successfully.

## 2. Trigger evaluation

Use `trigger-evals.json` with the skill installed and discoverable.

For every query, record whether the agent loaded `SKILL.md`.

A query passes when observed triggering matches `should_trigger`.

Suggested initial gate:

- At least 18 of 20 cases pass.
- No false positive occurs for basic summarization, rewriting, extraction, or translation.
- Review all failures before changing the description. Do not optimize only for the training set.

## 3. Output-quality evaluation

For each case in `evals.json`, create two isolated runs:

```text
workspace/
└── iteration-1/
    └── eval-[id]/
        ├── without-skill/
        │   └── output.md
        └── with-skill/
            └── output.md
```

Use the exact same prompt in both runs. Do not provide the skill's rules to the baseline run.

## 4. Grade assertions

For each assertion, record:

```json
{
  "text": "The response returns no more than four insights",
  "passed": true,
  "evidence": "Two numbered insights appear under the analysis section."
}
```

Use code for mechanical checks when practical. Use an independent model or human reviewer for semantic judgments.

## 5. Human review

For each paired output, judge:

- Did the skill reveal a mechanism the baseline missed?
- Did it reduce generic or duplicated content?
- Did it remain faithful to the evidence?
- Did it make uncertainty clearer?
- Did it improve the decision implication enough to justify added length?

## 6. Initial release gate

Before production use:

- All evidence-integrity assertions pass.
- The no-earned-insight case does not manufacture conclusions.
- The source-bound case introduces no outside factual claims.
- With-skill output is preferred over baseline on at least five of six cases.
- Any new failure becomes a targeted skill edit and a regression case.

## 7. Iteration rule

Change the smallest instruction that addresses an observed failure. Re-run the failing case and at least one unrelated case to check for regressions.

Do not keep adding instructions for hypothetical edge cases. Evidence from actual runs should drive version 0.2.
