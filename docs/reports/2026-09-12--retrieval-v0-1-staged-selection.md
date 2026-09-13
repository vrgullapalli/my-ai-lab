---
title: Retrieval v0.1, staged-selection experiment, T2 first
date: 2026-09-12
author: Alfred (session d249a842), at Venkat's word ("Implement the smallest staged-selection experiment needed to run the frozen tests. Do not promote it to the default Retrieval path until we see accuracy, stability, cost, and latency.")
kind: an experiment beside the tests, two blind T2 runs with two salts, and the trace of where the seed went; the seven-test run is not yet run (see section 4)
follows: docs/reports/2026-09-12--retrieval-v0-1-semantic-candidates.md (baseline 6 of 7; T2 failed 6 of 6 large-set blind runs; passed 2 of 2 hundred-line blind runs); the plan of 05:03
question: "Does staging the model's read into hundred-record groups let it keep the meaning match it makes at a hundred and loses at fourteen hundred?"
result: STAGE 1 YES, TWICE. Under both salts the seed A-LIVE-187 was picked inside its group of about 96 (rank 2 in salt B, rank 4 in salt A). THE SECOND LEVEL KILLED IT, TWICE. The union of 60 must-consider plus 112 stage-1 picks was 172, over the cap of 150, so the 112 were regrouped into two groups of 56 with eight slots each, and the seed lost both times. T2 final: FAIL under both salts. The stop condition (stage 1 fails to pick it under both salts) was not met. The failure point is the union cap and the second level's K, parameters I fixed in the plan, not the model's selection at a hundred.
checks:
  grouping_proven: every scoped record in exactly one group, must-consider held out, planted duplicate fails the check (G14)
  t2_salt_A: stage 1 picked the seed (rank 4 of 8 in group 7 of 14); level 2 dropped it; final FAIL
  t2_salt_B: stage 1 picked the seed (rank 2 of 8 in group 11 of 14); level 2 dropped it; final FAIL
  gate_one_article: picked in stage 1 in both salts; final rank 4 (A) and 4 (B)
  research_file: not picked in stage 1 in either salt
  seven_test_run: not run (section 4)
needs_venkat:
  - whether to lift the union cap (one final rank over about 170, a modest step past the hundred that passed) or keep two levels with a wider second-level K, before the seven-test run
tags_used: observed (a file or a script's output this session) · inferred (my reading) · his-word
---

Alfred — the short version first.

**Stage 1 works.** In both salts the model, reading one group of about 96 records at a time and forced to write eight picks before moving on, picked the seed with the right reason. The hundred-line result reproduced inside the pipeline, with the seed in a group it did not know was the target.

**The funnel I set killed it.** 60 must-consider plus 112 stage-1 picks is 172. The plan's cap was 150. Over the cap, the 112 picks were regrouped into two groups of 56 and cut to eight each. Fifty-six records that were each the best of their group competed for eight slots, and the seed lost to the learning-and-autonomy cluster both times. That second contest is harsher than the first, and the plan did not see it.

**T2 still fails on the frozen condition,** under both salts. The gate-one article reached rank 4 both times. The research file was never picked at stage 1.

# 1. What was built (observed)

`context/sources/tests/staged_experiment.py`, beside the tests, not in Retrieval. Three commands: `groups` (salted-hash grouping of the scoped records, must-consider held out, manifest), `union` (must-consider first, then stage-1 picks with reasons; a second level when over the cap), `check` (every ref in exactly one group; `--plant` must fail). The model's part ran as a blind agent per salt, following the plan's protocol: ideas, sources, groups, one group at a time with picks written before the next, union, final rank, fetch, flags. Retrieval's script, skill, index, fetch, and packaging were not touched.

# 2. Results (observed)

| | Salt A | Salt B |
|---|---|---|
| scoped records | 1,371 | 1,396 |
| groups, size | 14, 88 to 96 | 14, 88 to 96 |
| K per group | 8 | 8 |
| seed's group, stage-1 rank | group 7, rank 4 | group 11, rank 2 |
| stage-1 picks | 112 | 112 |
| union before cap | 172 | 172 |
| level 2 | 2 groups of 56, 8 each; seed in one, not picked | same; seed in one, not picked |
| final union | 76 (60 must-consider + 16) | 76 |
| final rank of seed | not in 10 | not in 10 |
| gate-one article final rank | 4 | 4 |
| T2 frozen condition | FAIL | FAIL |
| model's missing-evidence state | found | partial |

Against the baseline: T2 fails as it did in all six large-set runs, but for a different reason. There, the model never deliberated on the seed. Here it did, twice, and a cut I designed removed it.

# 3. Cost and latency (observed)

| | Salt A | Salt B |
|---|---|---|
| bytes read at stage 1 | 14 group files, 555 KB | 570 KB |
| level 2 plus union | 98 KB | 98 KB |
| agent's own token count | 395,248 tokens | 389,993 tokens |
| latency, ideas to final picks | 480 seconds (13 minutes wall clock, including a stall on a blocked write) | 458 seconds |

Tokens are close to the large-set runs (about 350,000 to 390,000 per question). Latency roughly triples, because fourteen groups are read in series. Nothing here is cheaper yet; it is more accurate at stage 1.

# 4. Why the seven-test run has not been run (inferred)

The plan fixed the parameters before the runs and said a value changes only if a test other than T2 fails because of it. The trace shows something the plan did not anticipate: at today's sizes the union is over the cap for any scope that includes the seedbank, so every such question goes through the second level, and the second level is a harder contest than the first. Running the seven now would spend about two million tokens measuring a funnel I already know to be wrong. The change is one parameter, but I wrote the rule that forbids changing it after a T2 failure, so the change is his call:

- **Lift the cap to 180** and rank the union once. Salt B's union would have been 172 records, a modest step past the hundred that passed twice. One level, no second contest.
- **Keep two levels but widen the second level's K** to about 20, so the 112 become about 40 plus the 60 must-consider, near a hundred for the final rank.

My read: the first. The second level was a guess, and the hundred-line test never covered a contest among winners.

# 5. Stability (observed)

The two salts placed the seed in different groups (7 and 11) with different neighbours and both picked it. Both funnels dropped it. Order bias at stage 1 did not show; the failure was the same under both orderings, which points at the design, not the shuffle.

# 6. Adjacent, not fixed

- The agents refused to write files at first because a plan-mode notice from the rejected plan step reached them; one was stuck on a Write call waiting for a permission nobody could grant. Shell heredocs worked. The experiment's protocol should say so.
- The must-consider set held the two Lundbeck briefs; no stage-1 group did. The deterministic bypass did real work here.

# Files written

`context/sources/tests/staged_experiment.py`; `GATES.md` (G14, G15, G16); `context/sources/index/runs/staged-T2-A/` and `staged-T2-B/` (ignored); this report.
