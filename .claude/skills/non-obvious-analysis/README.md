# Non-Obvious Analysis Skill

A portable Agent Skill for turning reports, research, plans, case studies, meeting notes, market signals, and business problems into a small number of evidence-grounded, decision-relevant insights.

## What this package changes

The original prompt contained valuable analytical methods, but it required every method and a minimum of four surprising insights on every run. That structure can create method theater, duplicated conclusions, and unsupported novelty.

This version changes the operating logic:

- Analytical lenses are selected, not mechanically enumerated.
- One to four insights are returned only when earned.
- Zero insights is a valid result when evidence is weak.
- Source evidence, inference, hypothesis, unknowns, and recommendations remain separate.
- Every insight must change a belief, decision, risk, priority, or opportunity.
- Detailed guidance is loaded progressively from focused reference files.

## Package structure

```text
non-obvious-analysis/
├── SKILL.md
├── README.md
├── references/
│   ├── analytical-lenses.md
│   ├── evidence-and-confidence.md
│   ├── insight-quality-standard.md
│   ├── output-modes.md
│   └── worked-examples.md
└── evals/
    ├── BASELINE-FAILURES.md
    ├── RUNBOOK.md
    ├── evals.json
    └── trigger-evals.json
```

## Install

Place the complete `non-obvious-analysis` folder in the skills directory supported by your agent client.

A common project-level location for Agent Skills-compatible clients is:

```text
.agents/skills/non-obvious-analysis/
```

Claude Code also supports personal and project skill directories. Use the location appropriate to the scope you want.

## Use

The skill should trigger automatically for requests such as:

- "What is everyone missing in this report?"
- "Rethink this case study using non-obvious principles."
- "What hidden assumptions are driving this recommendation?"
- "What are the second-order implications of these signals?"

It should not trigger for simple summarization, extraction, rewriting, translation, or fact lookup.

## Validate

With the Agent Skills reference validator installed:

```bash
skills-ref validate ./non-obvious-analysis
```

## Evaluate

- `evals/trigger-evals.json` contains 20 positive and negative trigger cases.
- `evals/evals.json` contains six output-quality cases and initial assertions, including the established signal format.
- `evals/RUNBOOK.md` describes clean-context, with-skill, and without-skill testing.
- `evals/BASELINE-FAILURES.md` records the expected baseline failure modes derived from the original prompt.

The evaluation cases are part of the package, but model-level with-skill and without-skill runs must be executed in the target agent environment before production deployment.

## Version

`0.1.0`
