---
title: Hand test, market signals read against lab context
date: 2026-09-12
author: Alfred (session 325fd42f), at Venkat's word ("Run the hand test", 2026-09-11 23:55)
kind: one read-only test; this report and a one-line fix to the 09-11 scan are the only files written
follows: docs/reports/2026-09-11--market-signal-to-action-scan.md
plan: docs/plans/2026-09-12--hand-test-signals-against-lab-context--plan.md
question: "If one session reads the same signals with the lab's context, does it choose materially different moves than the briefs chose without it?"
baseline: the 7 Friday briefs dated 2026-09-04, work-os/scheduled-tasks/market-signals/0*/friday/outputs/2026-09-04.md
result: CONTEXT CHANGED THE ANSWER (blind verdict 3 of 3 "not present"; prediction was 2 of 3)
checks:
  baseline_moves_extracted: 21 (3 per brief, count checked by script)
  cited_lab_items_resolved: 20 of 20 (check shown to reject a fake seed, a fake point of view, and a fake quote)
  blind_verdicts: {same: 0, sharper: 0, not_present: 3}
  seed_matcher: 40 of 41 signal claims scored under 0.4; the one higher match was off-topic
needs_venkat:
  - "why 'The buyer's test' was archived on 09-10, because move 1 overlaps it"
  - which of the three moves, if any, to act on
  - the routine ruling, now with this result in hand
tags_used: observed · inferred · unknown
---

Alfred — this section was written before any lab context was read. It does not change after the run.

# 1. Prediction and pass rule (fixed before the run)

**Prediction:** 2 of the 3 moves will change.

- **Why I expect that.** The All Market brief names Eversana, and `eversana-intouch` is a target company. The brief can't know that.
- **And.** The brief's "stop rule" question may match your decision-review seeds, A-LIVE-281 to 288.

**Pass rule:**

- **Context changed the answer:** at least 2 of the 3 moves are judged "not present" among the briefs' moves, and every lab item each one cites resolves.
- **No change:** at least 2 of the 3 are judged "same."
- **Partly:** anything else.

**Who judges:** a separate helper that sees only the two lists, labeled A and B. It does not see this prediction, the reasoning, or which list is which.

**Keeping the briefs' own moves is an allowed answer.**

---

*Everything below was written after the run.*

# Result, first

**Context changed the answer.**

- The blind helper judged all 3 new moves "not present" among the briefs' 21. It saw only the two lists, labeled A and B.
- I predicted 2 of 3.
- One test, one week, one reasoner. It shows the picks differ. It does not show they are better. That part is your call.

# 2. What the briefs picked without the lab (observed)

21 moves across 7 briefs fall into three kinds:

| Kind | Count | Examples |
|---|---|---|
| Change the daily searches | 8 | "Add 'found by outside researchers' to the daily searches" |
| Ask one leader a question | 8 | "Ask one commercial leader on a vendor AI platform, 'When it learned something wrong, who noticed?'" |
| Read or find something | 5 | "Look for a fuller account of Lundbeck's 'learned the wrong things'" |

- **None names a company on your target list.** None moves a piece of your writing. None uses a proof piece you already have.
- **The 8 search moves can't happen now.** The routines they would change are gone.
- **Several "ask" moves assume meetings.** Examples: "In the two planned buyer talks," "in a conversation already booked." Whether those talks exist: unknown.

# 3. The three moves with the lab in view

## Move 1: build a one-page diligence checklist for drug makers entering AI deals like Lundbeck's with EVERSANA

- **What it rests on:**
  - **Your dossier predicted this buyer on 08-30.** The Eversana Intouch file says: "pharma companies entering Lundbeck-style AI-commercialization deals need independent pre-signature diligence." Its angle map names the piece: "A diligence checklist for AI-commercialization partnerships."
  - **Four of the seven briefs turn on that one deal.** They also already hold the questions: where did it add work, what did it learn wrong and who caught it, what can it do before anyone is asked, must the vendor report misbehavior, was the "before" measured.
  - **It matches your points of view.** POV-010: "The danger is a decision nobody realized they had handed over." POV-020: "Vendors have a version of their truth." Seeds A-LIVE-240 and A-LIVE-242 say the same in your words.
  - **The proof library (AS-004)** has vendor claims ready to pull from.
- **Uses it serves:** a proof piece, a client lead (drug makers signing such deals), and content.
- **Human gate:** under your advisory workflow, a proof brief comes to you before anything is built (`WORKFLOW.md` Stage 6).
- **Blind verdict:** not present. Closest was A-16, "Ask two or three pharma commercial contacts the two fast-value questions." The helper: "Building something for a buyer is a different action with a different purpose."
- **⚠ Open question, and it matters.** This looks close to "The buyer's test" (AS-002): "15 questions a buyer should ask an AI-intelligence vendor." You archived it on 09-10 with "buyers test -archive." The record doesn't say why.
  - If the reason was the format (a list of questions), this move has the same problem.
  - If it was the audience (a general public page), this one differs: private, for one kind of deal, used in outreach.
  - An asset search (the `asset-corpus-match` skill) would have flagged this overlap. I caught it by reading the registry.

## Move 2: use this week's evidence to close the research check on your article at gate 2

- **What it rests on:**
  - **Driver 4 says:** "nothing published… One article is at gate 2."
  - **That article is "Green means something different now":** a passing test only shows that nothing the tests knew to look for went wrong.
  - **Its first research check is:** "Whether this problem shows up in other pharma companies, not only in your project."
  - **This week answers it.** Lundbeck's rollout was "stepwise, guided by results from a series of internal pilots," and the tool still "learned the wrong things." KPMG: certification "doesn't actually eliminate or provide immunity from risks." Both agent breakouts were found by outsiders.
  - **It matches your record.** Seed A-LIVE-187, "The green checks were making me less safe." POV-012 and seed A-LIVE-249: "A system changing its recommendation isn't necessarily learning."
- **Uses it serves:** a content priority confirmed, content moved forward, and a belief strengthened.
- **Blind verdict:** not present. Closest was A-8, "look for a fuller account of Lundbeck's 'learned the wrong things.'" The helper: "No A move mentions the article or moves writing forward."
- **Limit.** The evidence comes from an event hosted by the vendor. One outlet reporting it (pharmaphorum) is owned by EVERSANA. The article's claim check would have to carry that.

## Move 3: record two dated signals on Precision AQ's file and hold contact

- **What it rests on:**
  - **McKesson signed to buy Precision AQ's parent on August 25.** Precision AQ is on your "engage" list, and its dossier says: "The deal clock is the procurement solvent."
  - **The Foundation brief tracks McKesson's data theft** through rented systems. The thieves claim data was taken between August 21 and 25, the same week the deal was signed.
  - **Precision AQ is "building a Data Hub"** on the same kind of rented platform. Integration planning starts before the close.
  - **This would be the first signal record ever filled in**, using the format in `docs/state.md`, with a "before the deal closes" window.
- **Why hold contact:**
  - **Your ruling:** "The first outreach is a rehearsal target, not the best target." Precision AQ is not small.
  - **The approach would have to point outward.** Raising the buyer's new parent's breach could read as pointing at them.
- **Uses it serves:** a client lead, with timing.
- **Blind verdict:** not present. Closest was A-5, "follow what McKesson's posted files hold." The helper: "That is timing an approach to one account, not tracking a leak."

# 4. How each link was found

This is what the test teaches about the missing step.

| Move | What connected the signal to the lab | Could a script do it today? |
|---|---|---|
| 1 | The brief named EVERSANA. A name match led to the Eversana Intouch file, and reading it found the angle | **The name match, yes** (done here by script). Finding the angle meant reading the file |
| 2 | Driver 4 points to the one article at gate 2. Reading its research check found the match | **No.** Matching a signal to an idea needs search by meaning |
| 3 | The brief named McKesson, a name in Precision AQ's file | **Yes**, done here by script |

- **The seed matcher added nothing.** 40 of 41 claims scored under 0.4. The one higher match (A-LIVE-110, 0.57) was off-topic. It also missed seed A-LIVE-187, the closest seed to move 2.
- **This backs up the scan:** company matches can be scripted today, and idea matches need search by meaning.

# 5. What it means for the routine ruling

- **Don't recreate the 21 routines blind as they were.** Without the lab in view, their three moves are mostly "search more" and "ask someone." With it, all three picks changed.
- **The simplest reading (inferred):** keep the briefs for gathering evidence. Run the "three moves" step in the lab after the briefs land, where the company files, the article, and your points of view are.
- **That's a ruling for you, not a design.** Nothing here is built.

# 6. Seed candidates

**None written. None proposed.** Under seed A-LIVE-194, a signal becomes a seed only when you react to it. If one of these three moves gets a reaction from you, that reaction is the candidate.

# Limits of this test

- **One week of briefs, and one reasoner who knew the hypothesis.** The blind judge and the script check reduce that bias. They don't remove it. I chose the moves.
- **"Not present" means different, not better.** The judge compared actions, not value.
- **Lab context is from 09-12, the briefs from 09-04.** The question was whether context changes the pick, not what was knowable on 09-04.
- **The briefs are backfills written on this laptop,** with the same limits as the live routines: no lab context, only their own past briefs and the shared "about Venkat" blocks (`market-signals/_schema/backfill.md`).
