---
title: Retrieval v0.1, one focused improvement to semantic candidate selection
date: 2026-09-12
author: Alfred (session d249a842), at Venkat's word ("Improve only the semantic candidate-selection part of Retrieval. Goal: find conceptually related evidence that exact and keyword matching miss. Use the simplest robust semantic method that fits the current lab.")
kind: one change, one T2 run, one full run, one probe; the files written are listed at the end
follows: docs/reports/2026-09-12--retrieval-v0-1-first-runs.md (baseline: T2 failed 4 of 4, overall 5 of 7)
question: "Does the simplest semantic method that fits the lab find the meaning match the baseline missed?"
result: T2 STILL FAILS (0 of 2 more blind runs; 0 of 6 overall). FULL SET 6 OF 7, up from 5 of 7, and the gain is T4 under his changed condition (AD-23), not the new method. A local embedding probe shows embeddings on the one-line index would not have found T2 either: seed A-LIVE-187 ranks 699 of 1,813 for the question.
checks:
  baseline: T2 0 of 4, overall 5 of 7 (run 4, 03:00)
  t2_first_run: FAIL (run 5, idea statements, scoped 1429 records, 651 KB)
  full_run: 6 of 7 (run 5f); T2 FAIL; T1, T3, T4, T5, T6, T7 PASS
  new_failures: none; T4 moved from fail to pass under AD-23
  boundary_and_controls: unchanged (refusal proven; positive control 7 of 7; negative 0 of 7)
  register_check: 24 sources, 0 findings; architecture_check: 0 findings; reachability 24 of 24
needs_venkat:
  - the next move on T2 (one proposal in section 5)
tags_used: observed (a script's output or a file read this session) · inferred (my reading) · his-word
---

Alfred — the short version first.

**The method.** Before any search, the model writes five to eight plain statements of the idea behind the question. The script scores each statement's words and two-word phrases against every record's title, gist, and text, and the hits join the must-consider list the model reads first. No new dependency. No vector store. The model writes; the script matches.

**It did not find the meaning match.** Two more blind runs, two more misses. The blind agents' statements never said "checks passed" or "green"; they said "learned the wrong lessons" and "went slow and it still went wrong." The seed says "a passing check created false confidence." No bridge, so nothing to score.

**Embeddings would not have found it either.** A small local model (bge-small, 384 dimensions, 34 seconds to embed the index) ranks the seed 699th for the question, 516th for the blind statements, 117th for the bare quote. Only my own statements, which I wrote knowing the answer, pull it to 19th. The link is a reasoning step, not a similarity.

# 1. What changed (observed)

| Where | Change |
|---|---|
| `context/sources/retrieve.py` | `candidates --expansions ideas.json`: each idea statement scored by shared words (3 per word in the title or gist, 1 per word in the text) and shared two-word phrases (6 per phrase in the title or gist, 3 in the text), size-discounted like keywords; the must-consider list grows to 60 when statements are given |
| `.claude/skills/retrieval/SKILL.md` | step 1 now says: write the idea statements first, then run candidates with them |
| `context/sources/tests/run_tests.py` | T4's pass condition follows AD-23: the canon README or the v5 brief in the top five, with the throughline in its fetched evidence |
| `context/sources/tests/RETRIEVAL-TESTS.md` | T4 changed at his word; T2 unchanged |

Unchanged: the register boundary, exact and keyword search, metadata and limits, deterministic fetch, conflict and gap handling, consumer judgment.

# 2. Results against the baseline (observed)

| Test | Baseline (run 4) | T2 first (run 5) | Full run (run 5f) |
|---|---|---|---|
| T1 EVERSANA, exact | pass | | pass |
| T2 Lundbeck, meaning | fail | fail | fail |
| T3 corrected ruling | pass | | pass |
| T4 data strategy | fail (canon at rank 6) | | pass (canon at rank 5, throughline in evidence; AD-23) |
| T5 career proof | pass | | pass |
| T6 authority conflict | pass | | pass |
| T7 honest miss | pass | | pass |
| **Total** | **5 of 7** | | **6 of 7** |

New failures introduced: none.

T2 in the two new runs: the gate-one article file at ranks 7 and 5; the seed A-LIVE-187 and the research file never in the ten picks. Six blind runs across the day, the same shape every time.

# 3. Cost and context size (observed, the agents' own counts)

| Run | Passes | Index read per question | Tokens per question | Total |
|---|---|---|---|---|
| 5 (T2 first) | 1 | 1,429 records, 651 KB | 354,000 tokens | 354,000 tokens |
| 5f (full) | 7 | 163 to 1,454 records, 91 KB to 661 KB | 117,000 to 358,000 tokens | about 1.8 million tokens |

The idea statements add nothing to the read size; they change what sits at the top of it. The scoped pass still reads about 1,100 to 1,450 records when seeds are in scope, because the seedbank is 819 of the 1,813 records.

# 4. The probe: would embeddings have done it? (observed)

Run in the scratchpad, outside the lab, nothing installed in the lab.

| Query given to the embedding model | Rank of A-LIVE-187 | Rank of the research file |
|---|---|---|
| the T2 question as written | 699 | 1,043 |
| the blind agent's 8 idea statements, best match | 516 | 1,533 |
| the bare Lundbeck quote | 117 | 1,063 |
| my 8 statements, written knowing the answer | 19 | 976 |

Other tests for scale: T4's canon README ranks 22, CAP-001 ranks 19 for T5. Embeddings on one-line gists would carry the exact and near-exact cases and miss the meaning case, the same shape as every method tried today.

# 5. Tradeoff, and the one next move (inferred)

**The tradeoff.** Idea statements are cheap and honest: no dependency, the model's semantic work happens on the question, not on the index, and the script does the matching. Their reach ends where the model's vocabulary guess ends. Blind, the guess did not reach "checks passed." My own guess did, but I knew the answer. That is the whole gap: the T2 link is "pilots passed, so this is a case of a green check that proved less than it seemed." Nothing today makes that inference before search.

**Why this matters beyond T2.** The hand test of 2026-09-12 found this link by reading the article's research check, which said what the article still needed, and recognising the signal as that missing thing. The direction was article to signal, not signal to article. Every method today searched signal to article.

**One next move.** Add the reverse direction as a deterministic input, not a new method: at index time, extract each editorial piece's open questions (the research file's "still owed" and "gap" lines, the seed's tension line) as standing queries, and let the candidates step match an incoming signal against those standing questions as well as against gists. The article's own line, "No public pharma case of a wrong-question AI evaluation was found," is a question the Lundbeck signal answers by words alone. One index field, one scoring pass, no model in the loop for the bridge. If it fails T2 blind, the method question goes back to him with that evidence.

# 6. Adjacent, not fixed

- The "reached by the idea alone" counter on the candidates line reports 60 whenever statements are given; its rule is wrong and it measures nothing yet.
- Agents put external sources (`career-advisor`, `warehouse`, `public-site`) in scope and got zero records each time; the `sources` line should mark them external.
- Every agent hit the output cap reading 100-line chunks of the scoped file and fell back to smaller reads; the compact lines are long.

# Files written for this job

`context/sources/retrieve.py` (idea-statement scoring), `.claude/skills/retrieval/SKILL.md` (step 1), `context/sources/tests/run_tests.py` and `RETRIEVAL-TESTS.md` (T4 under AD-23), `docs/architecture/ARCHITECTURE-DECISIONS.md` (AD-23), `GATES.md` (G12, G13), `context/sources/index/runs/` (run 5 and 5f picks, packages, ideas; ignored), and this report. The embedding probe lives in the session scratchpad only.
