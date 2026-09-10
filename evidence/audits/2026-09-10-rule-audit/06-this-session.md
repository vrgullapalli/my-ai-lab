# Rules this session (my-ai-lab-51) created or changed on 2026-09-09/10

Source key: A = his explicit ruling, confirmed as a rule · B = from something he said, not confirmed as a rule · C = mine, no Venkat source.
Enforcement: blocks / flags / guides.

| # | Rule (short) | Where | Source | Enforcement | Note |
|---|---|---|---|---|---|
| 1 | ARCHIE: one worker, no sub-agents | .claude/agents/archie/CLAUDE.md | B — from "it was supposed to be a twin" | guides | His words asked for a twin; "no sub-agents" is my reading of what a twin means |
| 2 | ARCHIE: 18 execution rules (7 WATSON, 11 kept from v2) | .claude/agents/archie/claude/rules/02-execution-rules.md | WATSON rules: C (Mia's); v2 rules: his approved v2 plan (A for the plan, not each line) | guides | Rule 18 "run the kill test on every idea" was moved from a sub-agent step into a rule by me |
| 3 | /archie skill: "Do not run the pipeline yourself. Do not add brand context…" | .claude/skills/archie/SKILL.md | C | guides | |
| 4 | Alfred duty seven: sync observations about him at every session close | .claude/agents/alfred/DUTIES.md | B — "make it part of your closing routing for every session" (one yes, before today's two-yes requirement) | guides; scorecard target 0 misses | |
| 5 | Duty seven: "Never write to context/how-i-work.md" | same | B — "id want to review it before it goes into context/how-i-work" | guides | |
| 6 | Observed file: append only, never rewrite, declined lines stay | docs/about-me/how-i-work--observed.md | C (my design) | guides | |
| 7 | Cultivator rule 09: append each pattern about him to the observed file | .claude/agents/cultivator/claude/rules/09-user-patterns.md | C (my extension of duty seven) | guides | |
| 8 | Cultivator: "agents cannot launch agents, so it cannot run ARCHIE" | cultivator CLAUDE.md + skills/research.md | C (a tool fact, stated as a rule) | guides | |
| 9 | who-i-am is generated, never hand-edited; --check refuses drift; --promote refuses a stale draft | work-os/brand-os/model/build_who_i_am.py | B — he chose "generated from the model with my words on top"; "never hand-edit" is DECISIONS 029 (writing guide) applied by me to a new file | blocks (--check exit 1, --promote refuses) | This is the exact pattern he warned about: a ruling for one room reused in another |
| 10 | Every spoke returns facts only through the model's decision-log.md | work-os/brand-os/model/SPOKES.md | C (my design; the model's own guide says updates go via the log) | guides | |
| 11 | check_hub.py: spoke must name the hub; never-cite numbers flagged in live text | work-os/brand-os/model/check_hub.py | spoke check: C · never-cite list: A (model rule 4, CE-D24) | flags (exit 1) | |
| 12 | "The reasoning drop is evidence, not canon; later ruling wins" | work-os/brand-os/model/REASONING-INDEX.md | C | guides | |
| 13 | New rulings about him go in brand-os DECISIONS.md | brand-os DECISIONS 034 | A — he approved it | guides | |
| 14 | Website front door: scripts compute the verdict, AI runs the conversation — this page only | brand-os DECISIONS 035 | A — "yes to all" (#7) | guides | |
| 15 | Client-meeting material stays in the warehouse only | brand-os DECISIONS 037 | C — my correction after another session's catch | guides | Stated as a consequence line; he has not ruled it |
| 16 | Memory: one point per message, most important first, bullets with context and examples | memory/venkat-one-point-at-a-time.md | A/B — his words, many times; not "confirmed as a rule" in the two-yes sense | loaded every session | |
| 17 | Memory: never use one of his lines as a universal law | memory/venkat-corrections-are-not-rules.md | B — "i dont think i want that as a blanket statement" | loaded every session | |
| 18 | Memory: any new rule needs two confirmations; actions must name their rule | same | A — his explicit words today | loaded every session | This is the new rule itself |
| 19 | iMac START-HERE banner: "Do not trust the claims in §8 below" | iMac career-advisor/START-HERE.md | A — "yes to all" (#4, banner) | guides | |
