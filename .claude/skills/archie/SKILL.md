---
name: archie
description: ARCHIE, the editorial researcher. Use when saying "/archie <topic>", "run archie", or "find receipted content angles on...". Launches the archie agent (WATSON's twin, at .claude/agents/archie/) on the topic; with no topic it takes the oldest item in ARCHIE's inbox. Finds, challenges, and frames. Never drafts the final piece, never prospect research, never persona extraction.
---

# /archie - launches the ARCHIE agent

> **Base directory:** `work-os/brand-os/engagement-os/` (lab root: `/Users/venkatgullapalli/Documents/my-ai-lab/`).
> ARCHIE's definition is the `archie` agent at `.claude/agents/archie/`. His data is at `agents/archie/` under the base directory.

1. Take the input after `/archie` (a topic, lived moment, question, source, draft, tension, or client problem). If none, name the oldest file in `agents/archie/inbox/` and use it.
2. Launch the `archie` agent with that input, verbatim, using the Agent tool. Do not run the pipeline yourself. Do not add brand context, a desired thesis, or a landing zone he did not give.
3. When it returns, tell Venkat: the output file path, the surviving ideas with their scores, what was killed and why, and anything routed to the backlog. Quote, do not summarize away, the weakest point on each survivor.

Until 2026-09-09 this skill ran the pipeline itself with parallel sub-agents. That form is in the warehouse at `_archive/claude-agents/archie-v2--skill-form--superseded-2026-09-09/`.
