---
title: Lab orientation brief
date: 2026-09-11
author: Alfred (session 0d4e3709), at Venkat's ask
kind: orientation scan, read-only
status: draft, not reviewed by Venkat
method: context-check.sh run at 21:37; four parallel read-only scans (skills and agents, work folders, sessions before 09-05, sessions and receipts 09-05 to 09-11); root files read in full
evidence_tags: current | historical | emerging | inferred | unclear
sources:
  - CLAUDE.md, ROOT.md, TASTE.md, DONE.md, RULINGS-IN-FORCE.md, context/intent/STANDING.md
  - .claude/agents/alfred/{CHARTER,DUTIES,AUTHORITY,LOG,TODAY}.md and sensors/
  - .claude/skills/*/SKILL.md (27)
  - work-os/brand-os/DECISIONS.md, engagement-os/{README,WORKFLOW,PLAN}.md, telegraph-plus/{STATUS,CLAUDE}.md, scheduled-tasks/README.md
  - evidence/sessions/ (259 transcripts, indexed by date), evidence/receipts/, evidence/audits/2026-09-10-rule-audit/
---

Alfred — this is what the lab looks like tonight, and how it got here. Read the six headings. Each one stands on its own.

# 1. System at a glance

**One folder, one front door, one voice.** `CLAUDE.md` at the root routes everything. Every message comes from Alfred. Four standing intents in `context/intent/STANDING.md` say what Alfred looks at. Scripts say what is true. The AI decides what to investigate.

**The layers, top to bottom:**

- **Rules and rulings.** Three safety minimums, the five roots, the 10th-grade rule. Rulings live in `work-os/brand-os/DECISIONS.md` (41 rows) and `RULINGS-IN-FORCE.md`.
- **Who he is.** `work-os/brand-os/` is the identity canon. `docs/about-me/` holds four new draft layers built 09-11: voice profile, thinking model, point-of-view library, evidence library.
- **Getting work out.** `engagement-os/` finds clients from public signals and runs the publishing chain. The seedbank (680 seeds) lives here. So do ARCHIE, the dossier and committee skills, and the cultivator.
- **The product.** `telegraph-plus/` is the current Telegraph line. Its rule: intent is state, not output.
- **Routines in the cloud.** 28 on paper. As of 09-11 15:20 the account lists 2.
- **Evidence.** 259 rendered transcripts, 9 receipts, 1 audit. Every transcript line has a stable anchor.
- **Alfred's machinery.** Open and close routines, `facts.py` for every number, an append-only log, two hooks that block (root lock, unlazy stop), one that reminds.

**Eight git repos. Two have remotes.** The lab root ignores brand-os and engagement-os because they are their own repos. 98 uncommitted files sit in engagement-os, which is where the live memory is.

# 2. Existing capability map

| Area | What exists (tag) | Where | Read |
|---|---|---|---|
| **Context** | Five roots, taste file, writing canon (current). Four-layer model of him (emerging, all DRAFT). Three ruled context files `who-i-am`, `how-i-talk`, `how-i-work` (absent; item one on TODAY.md) | `ROOT.md`, `TASTE.md`, `brand-os/voice/VENKAT-WRITING-CANON.md`, `docs/about-me/`, `context/` | Strongest area by volume. Three homes for "who he is" and no ruling on which wins |
| **Authority and control** | Three minimums, Alfred's authority file, root lock hook with 37 tests, unlazy stop hook (current). Two-confirmation rule for new rules (current, lives only in a memory note). Tiered rules 1/2/3 (current, DECISIONS 031) | `CLAUDE.md`, `.claude/agents/alfred/AUTHORITY.md`, `.claude/hooks/`, `.claude/skills/unlazy/` | Rule audit: of 192 front-door rules, 44 quote him, 71 have no source from him. Only three things actually refuse |
| **Evidence** | Transcripts with anchors, receipts, audits, claim ledger skill, Telegraph evidence chain `source → observation → measurement → interpretation → belief → prediction` (current) | `evidence/`, `.claude/skills/claim-verification/`, `telegraph-plus/CLAUDE.md` | Unusually strong. Receipts are new files only, never edited |
| **Memory and state** | Seedbank, 680 seeds (current, live daily). Follow-ups as `F-` lines inside receipts, read back by `facts.py loops` (current). Observed file about how he works, append-only (current). Remember plugin (broken: `call-haiku error` in `.remember/logs/`). Four memory types from `DONE.md` (historical, never designed) | `engagement-os/seedbank/`, `evidence/receipts/`, `docs/about-me/how-i-work--observed.md` | Three trackers hold "waiting on Venkat": receipts, TODAY.md, `upskill-advisor/records/open-items.md`. `waiting.py` reads all three as one view |
| **Execution** | 27 skills. Publishing chain of nine skills (current; ran once for AS-006 and AS-002, both rejected at the first gate; development, expression, distribution never produced output). Dossier, committee, target-scan (current; collectors not built, "Approaches sent: 0"). worthy-tool-v2 (shipped, cold since 08-29) | `.claude/skills/`, `engagement-os/assets/`, `engagement-os/targets/` | Machinery is far ahead of use |
| **Coordination** | Alfred as the one interface (current). `public-value-advisor` coordinates the chain (current). ARCHIE inbox (current, empty). Cultivator (current; its index file does not exist). Five reviewer agents (current; nothing calls them) | `.claude/agents/` | Gabriel retired tonight after answering on his own |
| **Evaluation and observability** | `facts.py` (16 tests), `waiting.py`, `context-check.sh` plus `dead-pointers.py` plus `skill-check.py` with accepted-exception files, append-only duty log where a missing line is the alarm, `verify.sh` for routines (current). `prove-it-can-fail` (method current; its script is in the superseded Telegraph repo) | `.claude/agents/alfred/sensors/`, `.claude/skills/context-check/` | This is the lab's best idea, and it is enforced: "He does not grade himself" |
| **Capability architecture** | Career model: 5 stages, 26 subdomains, 92 capabilities (current, Stage 6 awaiting his approval). Six Capability Pillars (current, DECISIONS 025). Asset doctrine, five layers (current) | `brand-os/model/`, memory notes | "Capability" is a brand and product word here. It is not a lab-wide design word yet |

**Does not fit the eight:** the three-repo backup proof of 09-10 (7,185 files, restore-tested), the launchd session-sync job, and the root-locked folder list.

# 3. Evolution and recurring patterns

**Six eras, four restarts.**

1. Before August: `My_AI_Lab/`, an OSINT job-posting prompt (ancestor of dossier), a first Chief of Staff torn down on 07-30.
2. 08-11: `my-ai-lab-v2/chief-of-staff`. His words: "Severe ADHD makes initiation, closure, and state continuity the real constraints, so the system exists to carry those."
3. 08-16 to 08-23: the phase machine (Phases 1 to 6), then a seven-foundry federation with Codex. Alfred and Gabriel named 08-21.
4. 08-26: the reset. "I want to block all the rules and open loops. I'm going to start over." Work scattered to five repos.
5. 09-05 to 09-07: one three-day session scans the mess. "The problem with the chief of staff was that I just felt it wasn't proactive enough, and it was almost like a checklist."
6. 09-08 to 09-11: the current lab. Doctrine on 09-08, rebuilds on 09-09, sensors and routines on 09-10, the four layers of him on 09-11.

**What he asks for every time** (historical and current, same words): carry the executive function. Plain words. Recommend, don't report. Anticipate. One front door. Learn in a compounding way. Don't agree just to agree.

**Ideas that keep coming back under new names:**

- Memory types: four in `DONE.md`, seven in the 09-06 table he pasted, today's receipts plus seeds plus observed file.
- Gates: done-bar, phase gates, consequence classes, episode gates, now unlazy.
- Briefing: daily-brief, re-entry skill, now `alfred-open`.
- Seeds: MINT and GREENHOUSE study, `/plant`, seedbank, now `seed-capture`.
- Proof it ran: assurance agent (never built), shadow runtime (never built), now `LOG.md` and `facts.py`.

**What was dropped, and why:** the phase machine (ceremony outgrew the work), file permissions on Codex (same OS user, so no boundary), the 1,476-line decision log (nobody could tell what was still true), rules as text ("nearly the entire governance surface is behavioral text"), the foundry mesh (approved on paper, never wired).

**Failure modes he names, in his order of heat:** claimed done and not done. Files in the wrong place. Rules written and not enforced. Agents grading themselves. He is the one catching problems. Nothing remembered between sessions. Too many words. And, this week, a passing remark of his turned into a universal law: "seems like you are taking what i say at my word which can cause a lot of confusion."

# 4. Important observations

**Strengths worth keeping as they are**

- The sensor split. Scripts measure, the AI reasons, and it is enforced in `AUTHORITY.md`, not just described.
- Tests on the hooks and sensors, and accepted-exception files with a reason per line. "A new finding always shows up."
- Stable citation anchors on transcripts, so a receipt can quote a line that survives a re-render.
- Every superseded file carries the date, his words, and the warehouse path. That is why this scan was possible.

**Gaps**

- Telegram, the "always-on door" he ruled on 08-11, is absent. Only `DONE.md` mentions it.
- No sensor measures any of the five ADHD metrics in `DONE.md` section 10.
- The three ruled context files do not exist. Nothing loads the four draft layers.
- Telegraph governance is unruled: whether `upskill-advisor` governs `telegraph-plus` is open since 09-07.

**Overlap and duplication**

- Three writing guides, and they differ file by file: `brand-os/venkat-writing-guide/`, `brand-os/voice/venkat-writing-guide/` (generated), `engagement-os/references/writing-guide/`.
- Two voice skills: `my-voice` (rooted in the canon) and `contextual-voice` (no base directory, its own core file).
- Two whole-market briefs firing daily, flagged 09-09, not disabled.
- "Working with Venkat" guidance in two repos.

**Unclear boundaries**

- "Who he is" has three homes: brand-os (ruled canon), docs/about-me (drafts), context/ (ruled files, unwritten). `CLAUDE.md` says brand-os is "never copied into a project" and also names `context/` as the owner.
- `engagement-os/context/PROFILE.md` and `memory/concepts.md` were recovered 09-09 and never merged. The recovery note asks whether engagement-os is even the right home.

**Hidden dependencies**

- `prove-it-can-fail` runs a script inside the superseded Telegraph repo.
- The cultivator's first instruction is to read an index that does not exist.
- Session capture depends on Full Disk Access for Python.app and breaks on every Command Line Tools update.
- The root repo cannot see brand-os or engagement-os. Backup proof covers the tarball, not git.

**Drift between record and reality**

- The lab records 29 routine ids. The account lists 2. `verify.sh` cannot run. Logged 09-11 15:20.
- `RULINGS-IN-FORCE.md` Part 3: seven yes-or-no questions from 09-08 still open, including whether `DONE.md` is the bar.
- `DONE.md` section 9 says a correction updates the instruction. The current rule says a correction is evidence, not a rule. Both are live.
- Two sessions edited the front door at the same time tonight. The label rule changed on disk while this scan ran.

# 5. What is still unclear

1. **Is `DONE.md` still the definition of done?** It is the only full spec of the system, and Part 3 has not been answered.
2. **What happened to the 28 cloud routines?** Deleted, moved to another account, or a listing bug. This changes what "running" means for a third of the lab.
3. **Which home wins for "who he is"?** Until ruled, every new draft adds a fourth copy.
4. **Does `upskill-advisor` govern `telegraph-plus`?** The gates live in one, the doctrine in the other.
5. **What does "capability" mean to him at lab level?** The career model has 92. The pillars are six. The lab has none named.

# 6. Recommended next step

**Get his answers to the seven questions in `RULINGS-IN-FORCE.md` Part 3, starting with question 2: is `DONE.md` the bar.** Five minutes each, his own estimate. Every architectural read in this brief compares the lab against that file. If it is not the bar, the comparison is wrong. If it is, five of its ten sections are unbuilt and that becomes the map.

Not a roadmap. One sitting, seven yes-or-no answers, written to `brand-os/DECISIONS.md` with the two-confirmation rule.

*Separately, and not an understanding question: the routine gap (29 recorded, 2 live) is the open alarm from the 15:20 duty pass. The open routine already named it as today's next action.*
