---
title: Market signal to action scan
date: 2026-09-11
author: Alfred (session 325fd42f), at Venkat's ask
kind: read-only scan; this report is the only file written; nothing here is approved or built
question: "What currently happens between a market signal entering the lab and a decision about what useful thing to do with it?"
answers:
  signals_feed_seedbank_in_this_lab: no (observed; 0 seeds come from routine briefs)
  seedbank_holds_too_many_kinds: yes, but signals are not the cause (observed)
  seedbank_growth_last_4_days: 102 seeds, about 25 a day, against about 7 a day the four weeks before (observed)
  opportunity_synthesis: partial (observed)
  market_signal_routines_live: 0 of 21 (observed, RemoteTrigger list, 2026-09-11 about 23:45)
next_move: one hand test of a week's briefs against what the lab already holds, before any routine is recreated
needs_venkat:
  - ruling on the missing routines (open since 2026-09-11 15:20)
  - yes or no on the hand test
  - rewording of follow-ups F-20260910-1349-7 and F-20260910-1627-2 (a rule change, so two yeses)
  - where the 17 lab-rule seeds live
  - retiring two dormant signal tools to the warehouse
tags_used: observed (seen on disk or live) · inferred (my reading) · unknown
sources:
  - work-os/scheduled-tasks/README.md, market-signals/README.md, _shared/signal-structure.md, market-signals/_schema/friday.md
  - .claude/skills/alfred-open/SKILL.md lines 51-63; .claude/agents/alfred/LOG.md line 52
  - work-os/brand-os/engagement-os/WORKFLOW.md, docs/state.md lines 98-113, targets/index/
  - work-os/brand-os/engagement-os/seedbank/ (README, INDEX, SPEC draft, all 782 seed files by field)
  - work-os/brand-os/model/SPOKES.md; work-os/brand-os/DECISIONS.md 006 and 033
  - docs/about-me/POV-LIBRARY-venkat-gullapalli.md; docs/reports/2026-09-11--ai-native-possibility-brief.md
  - seeds A-LIVE-194 and A-LIVE-293; receipts of 2026-09-10 and 2026-09-11
---

Alfred — the short version first, then the detail.

**Signals are not in your seedbank today. Nothing is.** The 21 market-signal routines no longer exist on your account. When they did run, their briefs stopped at a private page on claude.ai. Nothing in the lab read them.

**The seedbank is crowded anyway.** The cause is old engineering notes and rules about the lab, not market news.

**The "signal → what could this become → ranked action" step half exists.** The briefs already ask what a signal could become and suggest up to three moves. They do it blind, with no view of your seeds, points of view, target companies, or projects.

---

# 1. Current flow

```
Cloud routine (21 market-signal + 7 others)
  web search only; cannot open pages
  reads only its own past briefs + a one-page "about Venkat"
        │
        ▼
Brief, per signal: what it is · fast value · deeper asset ·
learning question · one state (IGNORE … ACT)
Friday: which beliefs moved · three moves max
        │
        ▼
Private page on claude.ai ─────────────► STOPS HERE
        │
        ▼ (by hand, at the morning open, only for the 7 older tasks;
        │  the 21 market-signal routines are never pulled)
work-os/scheduled-tasks/<task>/outputs/<date>.md
        │
        ▼
Morning open checks the top line against seeds by word overlap.
Writes nothing. Nothing else reads the outputs.
```

**What is true tonight (observed):**

- **0 of 21 market-signal routines exist.** The account lists two routines: a calendar reminder and a morning brief. Alfred first raised this at 15:20 today: "account lists 2 routines; lab records 29 ids." It is still unruled.
- **0 live daily briefs are in the lab.** The 105 Wednesday and Friday files there are backfills written on this laptop on 2026-09-10.
- **No signal has ever reached action.** Across those briefs: 50 signals marked INVESTIGATE, 32 MONITOR, 7 TALK. None reached TEST, DEVELOP, or ACT.

**A second, separate path exists for companies** (the advisory workflow in `engagement-os/`):

```
Company research (dossier) → verdict: engage / watch / reject
  → signal record (type, source, confidence, what it might mean,
    useful window, next check, action state)
  → proof brief → review board → outreach → outcome
```

- 15 companies researched. 11 at "engage," 3 at "watch," 1 refused, by the latest verdicts in `targets/index/verdicts.jsonl`. (Corrected 2026-09-12. This line first said 8, from an out-of-date roster.) Last activity 2026-09-04.
- The signal record slot exists. **0 are filled in.**
- One outreach piece was drafted and tabled. The `outcomes/` folder is empty.
- This path never receives anything from the market-signal routines.

---

# 2. What already exists

| Piece | Job it does | Good at | Overlaps with | Used? |
|---|---|---|---|---|
| **Signal brief structure** (all routines) | Reads a signal, says what it could become, gives it one state, suggests up to three moves, tracks which beliefs moved | Already asks the right questions: fast value, deeper asset, what would change a belief | Public value gate, ARCHIE, the analysis skill | Routines gone. Backfills only |
| **Company research** (dossier, committee, target scan) | Finds where a company needs you. Scores fit and "is there a real problem" separately | Evidence-tagged. Strict: only a supported need earns outreach | Old opportunity map | Dormant since 09-04 |
| **Signal record** (`engagement-os/docs/state.md`) | Stores one outside observation with its likely meaning, useful window, next check, action state | Already the right shape for a signal. No new schema needed | The brief's per-signal fields | Defined, 0 records |
| **Proof brief + asset match** | Decides reuse, customize, or build for a proof piece | Stops rebuilding what exists | Public value gate | Dormant |
| **ARCHIE** | Turns a topic into ranked content ideas, with sources | Kills weak ideas first. Grades on seven counts | Brief's "deeper asset" | 2 runs (09-03, 09-04). Inbox empty |
| **Public value gate** | Asks whether private work should become public | Two human gates | Brief's "fast value" | 4 records, 08-30. Both finished pieces archived 09-10 |
| **Analysis skill** (`non-obvious-analysis`) | Finds what others miss in any material, ranks the top one to four insights | Most-used piece here (4 sessions) | Brief's analysis block | Active |
| **Cultivator** | Tends seeds, proposes the one action that moves each forward | Proposes only | none | 1 real pass (09-09 to 09-10) |
| **Career model hub** (`brand-os/model/`) | One home for what you can do. Readers listed in `SPOKES.md` | Already lists "a signal-intelligence capability" as a pending reader. Outreach: "no consumer" | none | Active hub, few readers |
| **Telegraph+** | Tracks what pharma competitors are trying to do, as beliefs that change | Its own ledger (64 events) | none. Keep it separate | Driver 3 |

**Three different action word lists do the same job** (observed): the briefs' seven states, the signal record's five action states, and a dormant weekly tool's six actions.

---

# 3. Gap analysis

**Keep**
- The brief structure. The per-signal questions are good.
- Company research and its two-score verdict.
- The seedbank's own definition: "one idea worth keeping."
- The two human gates: direction and publication.

**Reuse**
- The signal record from `docs/state.md` as the shape for any signal worth keeping. Nothing new to design.
- Seed A-LIVE-194 as the entry rule, already picked by you on 09-10: "An item that arrives with no reaction from him is a bookmark, not an idea."
- The asset match, ARCHIE, and the cultivator as the next step after a signal is judged worth acting on.

**Change**
- **Where the "what could this become" step runs.** Today it runs in the cloud with no lab context. It needs to run where your seeds, points of view, targets, and drivers are.
- **Follow-ups F-20260910-1349-7 and F-20260910-1627-2** say "design how the daily signal briefs flow into the seedbank." The possibility brief says "the 21 routines feed the seedbank." Both point the wrong way. Signals should link to seeds, not become seeds.
- **The routine build script** (`market-signals/assemble.sh` line 10) reads 10 columns, but `routines.tsv` has 11. The routine id comes out as "522d91f5-…|trig_01BQ7J2u…" (observed in `01-foundation/daily/build/routine-body.json`). Fix it before recreating anything.
- **The morning open's pull** covers only the 7 older tasks. The 21 were never pulled.

**Retire** (to the warehouse, on your yes)
- The weekly buyer-language tool (`brand-os/audience/weekly/`). Hand-ranked, never ran live, points at dead paths, and its timed job is missing.
- The old opportunity map (`engagement-os/inputs/opportunity-map--from-career-advisor--2026-08-26/`). Dead since 08-26. The pipeline it needed was never built. Check its contact list (`relationship-registry.xlsx`) first. It is the only contact list this scan found.

**Missing**
- **The context step.** Nothing reads a signal next to what you already hold.
- **Shared retrieval** across stores (section 6).
- **Outcomes.** Nothing records what a signal led to, so no ranking can ever get better.

---

# 4. Seedbank ruling

**Is it storing too many kinds of things? Yes.** Signals are not the reason.

**What is in it (782 seed files, observed):**

| Folder | Count | What it mostly is |
|---|---|---|
| `written/` | 459 | Loaded in one scripted batch on 08-13 from old AI build notes: 186 topic cards, 77 chronicles, 43 decision records, 153 seed cards. Its README: only 13 are "confidently his own writing" |
| `session/` | 293 | Your ideas, plus rules about how the lab runs |
| `spoken/` | 30 | 25 of your voice notes, 5 other creators' content |

- Market or news items: **about 6 in the whole store** (inferred from a sample).
- Used: 52. Retired: 0. The README still says 680.

**How fast it grew (session seeds, by each seed's own date):**

| Week | Seeds |
|---|---|
| Aug 10–16 | 49 |
| Aug 17–23 | 83 |
| Aug 24–30 | 2 |
| Aug 31–Sep 6 | 56 |
| **Sep 8–11 (4 days, seeds A-LIVE-192 to 293)** | **102** |

- The four weeks before: about 47 a week, or **7 a day**.
- The last four days: **about 25 a day**, three to four times faster.
- **Take out the one interview night and it is slower than usual.** 85 of the 102 came from your 09-09 taste interview, done with you last night into this morning (your words, 23:49). The other 17 came in four days, about 4 a day.

**Quality of the 102 new seeds:**

- **Seeds 206–290 (85): strong material.** 83 are marked yours, word for word or close. The other 2 are Alfred's sentences that you endorsed. The files are well made. Example, A-LIVE-235: the claim is a vendor claim that is "true for one channel … and sold as if it were true for all," with the reason it matters.
- **But they are sentences, not separate ideas.** They come from about six arguments. Seeds 259–272 are 14 seeds from one argument (the rep can challenge the model's reasoning). Seeds 273–290 are 18 seeds from another (reporting against decision support).
- **Some titles don't stand on their own.** "There's a version of their truth there." "What AI changes is that it makes it practical." The bodies carry the meaning. The titles don't.
- **They are stored twice.** The same interview built the points-of-view library (22 points of view) the same night. Neither one points at the other.
- **Seeds 192–205 and 291–293 (17): rules about the lab**, mostly Alfred's wording that you endorsed. Examples: "Nothing sits loose," "A finding no sensor reads is a note to nobody." These are operating rules, not things to think or write about. The seedbank draft spec already proposes that build ideas go "in the lab-wide build ledger, not here."
- **Record gap:** no receipt records the interview-night batch. You've now said you were there, so this is a missing record, not a missing pick.

**Where signals should live: in an existing store. No new Signal Bank.**

- **Briefs:** in `work-os/scheduled-tasks/<task>/outputs/`. This folder already exists and is already the designed landing spot.
- **A signal worth tracking:** as a signal record in the existing format. Put it in the company's folder if it names a target company.
- **A seed is written only when you react** (A-LIVE-194). The signal is the evidence. Your reaction is the seed. The seed links back to the signal.

This is the simplest option. It needs no new folder, schema, or tool. It means rewording the two follow-ups above.

**One open fact:** the seedbank draft spec says the iMac copy holds "market seeds 213 to 252." That may be where signals did flow in before. The Desktop copy on this laptop stops at 191 and has none. I can't reach the iMac from here (unknown).

---

# 5. Opportunity synthesis ruling

**Partial. It exists under other names, and it runs blind.**

| Part of the job | Where it lives now | State |
|---|---|---|
| What does this signal mean? | Brief analysis block; analysis skill | Exists |
| What could it become? | Brief: fast value, deeper asset | Exists |
| Did a belief move? | Friday brief: strengthens, weakens, complicates, nothing changed | Exists, but against the brief's own past beliefs, not your points of view |
| Which company needs you? | Company research verdict | Exists, separate path |
| Reuse or build the proof? | Asset match | Exists |
| **What do I already hold that this touches?** | nothing | **Missing** |
| **Rank across kinds (outreach vs content vs proof vs product)** | nothing | **Missing** |
| What happened after we acted? | `outcomes/`, empty | **Missing** |

**Is a separate capability needed? No.** The job is needed. A new build is not.

The job, in one sentence: *take a new signal, check it against what the lab already holds, and name the one to three things most worth doing about it, ranked, with the reason.*

Its home already exists: the closing step of the brief ("three moves max"). What's missing is the context it reads.

**Through the AI-native lens:**

- **Commercial job:** find the one buyer, proof, or piece worth doing this week, especially one that could change someone's decision (drivers 3 and 4).
- **AI reasons about:** what the signal means, what it touches, what it could become, and the ranking.
- **Scripts decide:** whether briefs arrived, whether a signal names a target company, whether a window or next-check date has passed, whether names are stripped, and how many signals ever reached ACT.
- **You decide:** contacting anyone, publishing, whether a signal becomes a seed, and whether a belief changes.
- **Continuous instead of manual:** link and rank after each batch of briefs, not at the next morning open.
- **Reuse, not rebuild:** the brief structure, signal record, asset match, ARCHIE, and cultivator.

---

# 6. Retrieval dependency

| Store | Can a signal be matched to it today? |
|---|---|
| Seedbank | Word overlap only (`find-similar.py`). Misses the same idea in different words |
| Points of view (POV library) | No. No reader at all. Not yet in git |
| Work corpus | No. Its search script needs a module that is not in the lab |
| Career model | Hub exists. The signal reader is listed as pending, not wired |
| Positioning and ideal client profile | ARCHIE reads them. The briefs get a one-page summary |
| Target companies | Readable by name, but nothing matches incoming signals to them |
| Current drivers (`STANDING.md`) | Read by Alfred only |

**One split matters:**

- **Company matches don't need retrieval.** A company name is exact text. A script can check it now.
- **Idea matches do.** Examples: "does this touch a point of view," "does this repeat a seed," "does this weaken a belief." Word overlap can't find these reliably.

**What retrieval would enable:** one question, "what do we already hold on this?", answered by meaning, across all seven stores, in one pass. Without it, any ranking guesses at what you already have. That is also the order in seed A-LIVE-293: retrieval first, then the standing watch. You have not ruled on that order yet.

---

# 7. Next move

**One hand test, before any routine is recreated.**

1. Take the seven Friday briefs dated 2026-09-04. They are already in the lab.
2. Have one session read each signal against the seedbank, the points-of-view library, the target companies (11 at "engage"; corrected from 8 on 2026-09-12), and the current drivers.
3. Rank the top three moves across all kinds.
4. Put that list next to the briefs' own "three moves."

- **If the lab's context changes the answer,** the gap is proven. The routines should be rebuilt to run where the context is, not recreated blind.
- **If it doesn't,** the briefs already do the job, and the fix is just pulling them in.

**Why now:** the routines are gone. This is the cheapest moment to change where the reasoning runs. The test is read-only and writes one report.

**First step, under two minutes:** say "yes, run the hand test," or "recreate the routines first."

---

# 8. After that, in order

| # | What | Owner | Needs |
|---|---|---|---|
| 1 | Rule on the 21 missing routines: recreate all, some, or none, after the test | Venkat | His ruling |
| 2 | Fix the build script column bug before any recreate | Alfred | Standing work, reversible |
| 3 | Reword F-20260910-1349-7 and F-20260910-1627-2: "signals stay in brief outputs; a seed is written only on his reaction" | Venkat | Two yeses (rule change) |
| 4 | Decide where the 17 lab-rule seeds live (the spec proposes the build ledger), and whether seeds 206–290 link to the points of view they support | Venkat | His ruling |
| 5 | Retire the weekly buyer-language tool and the old opportunity map to the warehouse, after checking the contact list | Venkat | His yes |
