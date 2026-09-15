---
what: Review of the 30 skills in .claude/skills/ against the Operational DNA standard (proposed, supplied by Venkat 2026-09-15). Read-only; nothing in the skills or architecture changed.
date: 2026-09-15
by: Alfred, session 4485630d
inputs: every SKILL.md read in full (three Explore subagents plus direct reads); docs/architecture/CAPABILITY-MAP.md; evidence/sessions/USAGE.jsonl (291 rows); receipts mentioning each skill; docs/reports/2026-09-14--q14-check-and-contextual-voice-findings.md; docs/about-me/how-i-work--observed.md
scope-note: seed-capture and context-check were read but not judged for change; another session owns them.
status: review, waiting on Venkat. Nothing here changes a skill until he says so.
---

# Skill architecture review, 2026-09-15

## Ruling

The skill system is basically sound. Thirty skills; fifteen stay as they are, thirteen need a small fix, one merges into another, and one repeatable job has no owner. No restructuring.

## What the numbers say (measured)

| Fact | Value | Source |
|---|---|---|
| Skills | 30 | ls .claude/skills |
| Skill check | 0 files with problems | facts sheet, 2026-09-15 00:29 |
| Sessions with 3+ turns and no skill or agent used | 115 of 291 | USAGE.jsonl |
| Most-used typed skill | session-receipt, 39 sessions | USAGE.jsonl |
| Publishing-chain skills that have never written a file | 2 (asset-expression, distribution-recommendation) | ls assets/ |
| Release manifest (release.yaml) that three skills gate on | exists in 0 files | find |
| Skills a hook starts | 3 (alfred-open, implication-lens, unlazy) | .claude/settings.json |

## Keep (15)

alfred-open, archie (launcher only, 15 lines, fine), asset-corpus-match, public-value-opportunity, public-asset-brief, retrieval, seed-capture (other session), context-check (other session), unlazy, dossier, design-brief, implication-lens, book-to-skill, godin-purple-cow, session-capture.

Notes:
- alfred-open has one internal contradiction: step 5a says republish the "Waiting on Venkat" page, the rules say no page is published by this routine. One line to fix, not material.
- book-to-skill and godin-purple-cow are generic by design. He runs the converter himself (three books, 2026-09-14). They are reference skills, not procedures. Count them apart when the skill count is quoted.
- session-capture is a manual button plus a report, by its own words. He asked for the button (2026-09-10). Keep.

## Change (13)

| Skill | Problem | Smallest change |
|---|---|---|
| my-voice | Reads its own 2026-09-02 references "as history" and waits for a re-spec; the canon is the authority (DECISIONS 028 to 030) | Make the canon and its generated guide folder the only source; take in contextual-voice's five format dials as media files |
| alfred-close | Copies seed-capture's 0.45 repeat rule instead of pointing at it; a normal close writes no transcript anchors | Take the anchor step from session-receipt; replace the copied rule with a pointer |
| session-receipt | Its one unique step (anchors) is reachable only from the manual button | Once alfred-close owns anchoring, shrink to a two-line alias. Keep the command; his word 2026-09-10 |
| non-obvious-analysis | Generic, written for redistribution; its default headings drew "lose the formalities" on 2026-09-11 | Output follows his reply rules; drop the install README |
| prove-it-can-fail | Its runner sits in the superseded Telegraph repo (known gap since 2026-09-10) | Move or rewrite the runner for telegraph-plus |
| design-review | Needs Playwright through the Docker gateway, which was down this session; no stop path for that | Add: no screenshot tool, say so and stop |
| committee | Copies dossier's constraint block near-verbatim | Point at dossier's block |
| target-scan | About a third of the file describes collectors that do not exist (it says so) | Cut the collector contract to a pointer until one is built |
| public-asset-development | Its worked example is the rejected, archived AS-006, and the warehouse path is wrong from its base directory | Fix the path; say the example was rejected |
| asset-expression | Cites "the four gates", which nothing defines; gates on a manifest field no file has | Name the two gates the advisor agent defines |
| claim-verification | Restates retrieval rules in prose instead of calling retrieval; no named input; no approver | Call retrieval; require the approved brief as input |
| public-asset-qa | Builds its own fresh-context reviewer while five reviewer agents and docs/review-board.md exist; never says who owns the verdict | Name the review board; add "PASS is QA's word, then Venkat's" |
| public-asset-experience-design | The Experience Recommendation has no file path and no named approver for draft to approved-for-build | Give it a path; say Venkat flips the status |

distribution-recommendation also carries a stale line ("the canonical payload lives in the release package"; none exists). One line, fix when first used.

## Merge / Retire

| Skill(s) | Reason | Where the responsibility goes |
|---|---|---|
| contextual-voice into my-voice | Same job, two rulebooks. The 2026-09-14 findings hold: it rewrites its own rules without naming the canon, drops six of seven Tier 1 truth rules (no "never invent", no "never name a client"), is softer than the pick-a-side ruling, and covers 5 of 12 kinds of writing. Named in 6 receipts, but how-i-work.md names my-voice as the voice skill | my-voice, reading the canon. Its five format dials survive as media files |
| session-receipt's anchoring step | Only reachable from the manual button, so a normal close has no anchors | alfred-close. The button stays |

No other retirements. The two dormant publishing skills (asset-expression, distribution-recommendation) do different jobs (decide channels; write channel versions), and the advisor agent already sequences them. Merging two skills that have never run would be a guess.

## Missing skills (1)

| Skill | Job | Why existing owners cannot cover it | DNA gap it closes |
|---|---|---|---|
| long-form article run | Move one piece through the 30-step article workflow between his five gates, keep the run record, and call the owner of each step | The publishing chain owns assets, not articles (its records live in assets/, the article's in editorial/). ARCHIE owns research only and is fenced from drafting. my-voice owns step 22. claim-verification owns step 24. No skill names editorial/WORKFLOW--long-form-article.md (grep of .claude: zero hits). The run record is kept by hand and read by facts.py | Process and State for articles. His word 2026-09-08: every format gets a variant of this workflow (14 listed) |

Four checks:
1. Repeatable: every article, and 14 format variants required.
2. No owner: proven by grep; the workflow file is a standard, not a runner.
3. Needs AI judgment: thesis, adversarial edit, cut, reader test.
4. Material gap: the only state is a hand-kept table; the first piece has sat at Gate 2 since 2026-09-08 (that gate waits on him, not on a skill, but nothing prepares the next step for him either).

Caveat: the workflow file's own status says "NOT yet a validated rule". So the skill's first form is thin: keep the run record, route each step to its owner, prepare the next gate. It does not re-describe the steps.

Design check (the lab hook's five questions):
1. Job: move an article through the workflow between his gates and keep the record.
2. Covered by: nothing. See the table.
3. AI-native test: the judgment steps are the skill; without AI the outcome is a checklist he walks alone, so the outcome does change.
4. Standard: none of the three. A skill is a procedure, not a shared system, registry, or sensor.
5. New system: no. No registry entry.

## Misplaced responsibilities

| Responsibility | Lives in | Should live in |
|---|---|---|
| Transcript anchors on a receipt | session-receipt | alfred-close |
| Voice truth rules (Tier 1) | contextual-voice's own voice-core.md, partly; my-voice's old references | the canon, read by one voice skill |
| Fresh-context review of a built asset | public-asset-qa's own instruction | the review board and the five reviewer agents |
| Retrieval rules for claim research | claim-verification prose | the retrieval skill |
| Article run state | a hand-kept run record | the proposed article skill, still read by facts.py |
| Seed repeat threshold | copied into alfred-close | seed-capture |

## What not to build

- A cloud-routine editing skill. The README procedure, assemble.sh, and verify.sh cover it. No judgment needed.
- A file-move skill. "Copy, verify, remove" is a rule and a checksum. Deterministic.
- A DNA review skill. The design-check hook already asks five questions from the capability map. The DNA document is proposed, not ruled. When it is ruled, change the hook's questions.
- A research-brief skill. A general-purpose subagent plus retrieval does it; the job is ad hoc.
- A book lens per book by default. book-to-skill makes them; each one adds a reference, not a procedure.
- A skill for every agent. The archie launcher exists because he types /archie. Do not add launchers for the others.
- Merging asset-expression and distribution-recommendation. Different jobs; both dormant; the advisor sequences them.

## Recommended skill set (30)

- Alfred routines (5): alfred-open, alfred-close, session-capture, session-receipt (alias), seed-capture
- Lab checks (4): context-check, prove-it-can-fail, unlazy, retrieval
- Thinking (2): implication-lens, non-obvious-analysis
- Voice and design (3): my-voice (with contextual-voice folded in), design-brief, design-review
- Publishing chain (9): public-value-opportunity, asset-corpus-match, public-asset-brief, public-asset-experience-design, claim-verification, public-asset-development, public-asset-qa, asset-expression, distribution-recommendation
- Buyer research (3): dossier, committee, target-scan
- Launcher (1): archie
- Reference and tools (2): book-to-skill, godin-purple-cow
- New (1): long-form article run

Same count as today. One out, one in. The gain is one voice rulebook instead of two, anchors on every receipt, and an owner for the article process.

## Next

Merge the two voice skills into my-voice, reading the canon. Highest value because it is the one Trust gap in a skill that writes as him: six of seven truth rules are missing from the skill used in more recent receipts. The article skill, the QA voice check, and expressions all lean on it, and the 2026-09-14 findings already list the fixes.

## Not done in this session

- GATES.md at the lab root was not written or touched. The unlazy trigger fired on a subagent's text, not on his words, and the root ledger belongs to another session (scope context-check-repair).
- The open routine did not run; the review came first.
