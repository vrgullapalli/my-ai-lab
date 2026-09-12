# Hand test: do the market briefs pick different moves when they can see the lab?

## Context

Tonight's scan ([docs/reports/2026-09-11--market-signal-to-action-scan.md]) found that the market briefs already ask "what could this become" and end with "three moves max," but they run blind. They see only their own past briefs and a one-page "about Venkat." They never see seeds, points of view, target companies, or drivers.

The 21 market-signal routines are gone from the account, so this is the cheapest moment to decide where that reasoning should run. Venkat said "run the hand test."

**The question the test answers:** if one session reads the same signals *with* the lab's context, does it choose materially different moves than the briefs chose without it?

**Why the baseline is fair (checked):** the 09-04 Friday briefs were backfills written with only the job prompt, the `_shared/` blocks (about 3,600 words: about-venkat, market lens, writing rules), and earlier briefs as memory (`market-signals/_schema/backfill.md` lines 8-9, 24-26). No seedbank, points of view, or targets.

## Inputs (all already in the lab)

- **Signals (baseline):** the 7 Friday briefs dated 2026-09-04, `work-os/scheduled-tasks/market-signals/0{0..6}-*/friday/outputs/2026-09-04.md`. About 2,000 words each. Each ends with `## Three moves max`, so up to 21 baseline moves.
- **Lab context:**
  - seedbank: `work-os/brand-os/engagement-os/seedbank/` (INDEX.md plus hits from the matcher)
  - points of view: `docs/about-me/POV-LIBRARY-venkat-gullapalli.md` (section 1 map, section 8 runtime card, full records as needed)
  - target companies: all 15 in `engagement-os/targets/`, latest verdicts in `targets/index/verdicts.jsonl` (11 engage, 3 watch, 1 refused)
  - drivers: `context/intent/STANDING.md`
  - ideal client profile: `work-os/brand-os/audience/icp--v3--2026-09-08.md`
  - career model hub: `work-os/brand-os/model/`
- **Existing tool reused:** `.claude/skills/seed-capture/scripts/find-similar.py --top 5 "<claim>"` (word overlap, read-only)

## Steps

0. **Write the prediction and the pass rule first**, at the top of the result report, before reading any context.
   - **Prediction:** 2 of 3 moves will change. A brief names Eversana, and `eversana-intouch` is a target company. The "stop rule" signal may match seeds A-LIVE-281 to 288 (the decision review).
   - **Pass rule, fixed before the run:**
     - **"Context changed the answer":** at least 2 of the 3 moves are judged "not present" among the 21 baseline moves, and each cites a lab item that resolves.
     - **"No change":** at least 2 of the 3 are judged "same."
     - **"Partly":** anything else.
1. **Script (scratchpad only): pull the baseline.** From each brief, extract every signal's title, state, trigger, fast value, and its three moves into `scratchpad/baseline.md`. Check by script that the move count matches the `1.`/`2.`/`3.` lines under each `## Three moves max`.
2. **Script: company matches.** Match the 15 target company names (plus obvious short forms like "Eversana") against all 7 briefs' text. Output which signals name a target, with its verdict. This needs no model.
3. **Script: seed matches.** Run `find-similar.py --top 5` on each signal's key-insight line. Save the hits.
4. **Reasoning pass (this session, no web search):**
   - Read the 7 briefs in full, then the context above. Read only the seeds and points of view the matches point to, plus any the session judges relevant.
   - For each signal, note what it touches, using IDs: seed IDs, point-of-view numbers, company slugs, driver numbers.
   - Note which of the scan's possible uses apply: client or sales lead, company to approach, proof piece, content, a content priority confirmed or killed, an existing seed, a point of view, the career model, Telegraph+, a belief that changes.
   - Then rank **the top 3 moves across all 7 briefs**, each with its reason and the lab items it rests on.
   - Keeping the briefs' own moves is an allowed answer.
5. **Script check: every cited ID resolves.** Seed files exist, point-of-view numbers exist in the library, company folders exist. Any that fail are listed.
6. **Blind comparison (one general-purpose subagent):**
   - Give it the 21 baseline moves as "List A" and the 3 new moves as "List B." Labels only; it does not see the hypothesis, the reasoning, or the prediction.
   - For each List B move it answers "same," "sharper version of A-n," or "not present," quoting the closest A move.
   - This keeps the session from grading its own work.
7. **Apply the pass rule. Write the result.**
8. **Fix one line in tonight's scan report:** "8 at engage" becomes "11 at engage" (the latest verdicts; the earlier reader's roster was out of date).

## Output

- One new file: `docs/reports/2026-09-12--hand-test-signals-against-lab-context.md`. Front matter for machines, plain body, tags "observed / inferred / unknown." Sections:
  1. prediction and pass rule (written first)
  2. the 3 moves with their lab items
  3. the blind verdict per move
  4. the result
  5. what it means for the routine ruling
  6. seed candidates, if any: listed only, none written
- One-line edit to `docs/reports/2026-09-11--market-signal-to-action-scan.md`.
- Scratch work stays in the session scratchpad.

## Guardrails

- No seeds written. No routines recreated. Nothing sent or published. No commits.
- No web search. The test is about lab context, not new market news.
- Lab context is as of today, 09-11/12, even though the briefs are dated 09-04. That's fine because the question is "does context change the pick," not "what was knowable on 09-04." The report says so.
- No new scripts saved in the lab. No new agent type, no new schema.

## Verification

- Step 1's count check matches the brief files. Step 5's resolve check passes, or lists what fails.
- The blind subagent's verdicts are quoted as returned, with no smoothing.
- `git status` shows only the new report and the one-line edit as changes from this run.
- The report is re-read for 10th-grade wording and spelled-out abbreviations before handing back.
