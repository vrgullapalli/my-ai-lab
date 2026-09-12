---
title: Retrieval v0.1, built and run against the seven frozen tests
date: 2026-09-12
author: Alfred (session d249a842), at Venkat's word ("build Retrieval v0.1 using the proposed design, with the model limited to semantic candidate selection/ranking and conflict flagging. Fetch actual evidence deterministically after candidate selection. Instrument the size/cost of the full-index semantic pass")
kind: a build and four blind test runs; files written are listed at the end
follows: docs/reports/2026-09-12--step-2-closure-and-retrieval-test-set.md; context/sources/tests/RETRIEVAL-TESTS.md (frozen 02:31)
question: "Does the minimum Retrieval pass the seven frozen tests, and what does the full-index semantic pass cost?"
result: 5 OF 7 PASS in the final blind run (T1, T3, T5, T6, T7). T2 (meaning match) failed in all four blind runs. T4 failed on one file's rank in all four. The size line: 1,813 records, 760,507 bytes, about 190,000 tokens for the full index; a blind pass over it cost about 340,000 tokens per question.
checks:
  index_coverage: 1469 of 1469 eligible files indexed (G1)
  boundary: a pick outside the register is refused (G2, positive control inside returned)
  scorer_positive_control: 7 of 7 on the known-answer refs
  scorer_negative_control: 0 of 7 on wrong refs
  blind_run_1: 5 of 7 (full index, 633 KB)
  blind_run_2: 5 of 7 (T2, T4 rerun; richer gists, 760 KB)
  blind_run_3: 4 of 7 (model picks sources first; two passes scoped out the ruling)
  blind_run_4: 5 of 7 (sources picked first; rule-bearing sources always in scope; deterministic candidates shown first)
  register_check: 24 sources, 0 findings
  architecture_check: 0 findings
  reachability: 24 of 24
  model_untouched: git status clean on work-os/brand-os/model
needs_venkat:
  - whether the meaning test (T2) is passed by a different semantic method, or the test's named file changes; the tests are frozen and a change is his word
  - whether T4's known answer should be the positioning canon (README) instead of the v5 context brief; four blind picks chose the canon every time
  - whether v0.1 may be used by consumers at 5 of 7, with T2 and T4 marked open
tags_used: observed (a script's output or a file read this session) · inferred (my reading) · his-word
---

Alfred — the short version first.

**Built.** The deterministic half is one script; the model's half is one skill. The model picks sources, then candidates by meaning, and flags conflicts. The script decides what may be read, fetches the evidence, and carries source, date, tier, ceiling, marks, pointer state, and which row corrects which. A pick outside the register is refused.

**Five of seven pass blind.** The exact test, the corrected ruling, the career-model proof, the authority conflict, and the honest miss all pass on the final run, with the judgment left to the consumer.

**Two fail every time.** The meaning test never surfaced seed A-LIVE-187 or the article's research file in four blind runs. The ARCHIE test never put the v5 positioning brief in the top five. The frozen tests have said what he asked them to say: at 1,813 records, a model reading one-liners is not a reliable meaning matcher, and it costs about 340,000 tokens a question to find that out.

# 1. What was built (observed)

| Part | File | What it does |
|---|---|---|
| Script | `context/sources/retrieve.py` | `index` builds the derived index from the register (one record per file, plus one per decision row, per career-model capability, per verdict line). `sources` prints the 24 readable sources in one line each. `candidates` runs exact and keyword matching and writes the scoped one-line index the model reads, with its size. `fetch` pulls the evidence for the model's picks, refuses anything outside the register, carries limits and marks, and appends the write-back line. `stats` prints the size line. |
| Skill | `.claude/skills/retrieval/SKILL.md` | The model's five steps: pick sources, get candidates, read the scoped index and pick by meaning, fetch, flag conflicts and the missing-evidence state, hand over the package. |
| Runner | `context/sources/tests/run_tests.py` | Scores the seven frozen tests on the package. Positive control 7 of 7, negative control 0 of 7. |
| Index | `context/sources/index/` | Derived, git-ignored, rebuilt from the register. `runs/` holds every blind pass's picks and packages. `runs.jsonl` is the write-back record. |

**What the model does, and only this:** choose which sources to read, choose and rank records by meaning, say why, flag conflicts, set the missing-evidence state. **What the script does:** everything else. The model never quotes a file the script did not fetch. Proven by G2: a planted pick outside the register was refused while a control inside it came back.

# 2. The four blind runs (observed)

Each pass was a fresh subagent that saw only the query, the one-line index, and the package the fetch wrote. It did not know the known answers.

| Run | Protocol | Index read per question | Cost per question (agent's own count) | Result |
|---|---|---|---|---|
| 1 | full index, first gists | 1,813 records, 633 KB, ~158k tokens | ~340k tokens, 16 chunked reads, ~150 s | 5 of 7 |
| 2 | full index, section-lead gists (T2, T4 only) | 1,813 records, 760 KB, ~190k tokens | ~395k tokens | 5 of 7 |
| 3 | model picks sources, reads only those | 138 to 1,380 records, 52 KB to 596 KB | 104k to 335k tokens | 4 of 7 |
| 4 | as 3, plus rule-bearing sources always in scope, deterministic candidates shown first | 163 to 1,454 records, 79 KB to 649 KB | 112k to 358k tokens | 5 of 7 |

Total spent on the four runs: about 6.9 million tokens across 23 blind passes.

| Test | Run 1 | Run 2 | Run 3 | Run 4 | Why it failed, when it did |
|---|---|---|---|---|---|
| T1 EVERSANA, exact | pass | | pass | pass | |
| T2 Lundbeck, meaning | fail | fail | fail | fail | A-LIVE-187 never picked; the article found only through its gate-1 file (ranks 7, 6, 8) |
| T3 corrected ruling | pass | | fail | pass | run 3 scoped out `rulings`; fixed by the always-in-scope rule |
| T4 data strategy | fail | fail | fail | fail | v5 brief never in top 5 (rank 10, absent, absent, absent); the canon README chosen instead every time; run 3 also lost D-003 by scope |
| T5 career proof | pass | | pass | pass | |
| T6 authority conflict | pass | | pass | pass | |
| T7 honest miss | pass | | pass | pass | |

# 3. What the runs taught, in order (inferred from the runs)

1. **The first gists were boilerplate.** A brief's first paragraph is its backfill note; a research file's is "Step 5, rules for this pass." No gist named Lundbeck. Fixed by section leads: title, first prose line, then up to three "heading: first line" pairs, bullets allowed when a section has no prose. Cost: 633 KB to 760 KB.
2. **A full read of 1,813 one-liners dilutes the picker.** Every agent read in 16 to 27 chunks and kept a shortlist by hand. Two said the useful records sat in about 20 lines at the end.
3. **Letting the model pick sources cut the cost but dropped the ruling twice.** T3 and T4 in run 3 both lost the row they turned on. Fixed by a deterministic rule: `rulings`, `root-doctrine`, `drivers`, `architecture` are always in scope (about 100 records).
4. **Big files win keyword scoring.** A 140 KB voice profile holds every word. Fixed by a size discount. Keyword matching stays a first cut, not a ranker.
5. **Fetched seeds came back with only their "Connections" line.** The excerpt took the lines matching the query, not the record's claim. Fixed: a record's evidence starts with its own title and gist.
6. **The two failures did not move.** T2's target seed has a good gist ("A passing check created false confidence") and was never chosen over seeds about learning and autonomy. T4's target file lost to the canon that carries its throughline, four times.

# 4. The size line, and what it means (observed, then inferred)

```
index size: 1813 records, 760507 bytes, ~190126 tokens (full-index semantic pass); 1469 files, 34644822 source bytes
```

- **Today** the full pass is 190,000 tokens of index and about 340,000 tokens of work per question. A scoped pass ranges from 20,000 tokens (T6, eight small sources) to 162,000 (T2, T7, seeds plus transcripts).
- **The 819 seeds and 318 transcripts are 63 percent of the index** and carry most of the noise. Transcript gists are session titles.
- **The tests already say a different semantic method is necessary for the meaning job.** Not because the pass is too big to read, but because reading it does not find the match. That is the evidence he asked the frozen tests to produce. What the method should be is his call; the tests and the runner are ready to score it.

# 5. Two questions about the tests themselves (inferred)

- **T2 names `05-research.md`.** Every run that reached the article reached it through `01-gate1--locked.md`, the gate he locked. The research file's gist now carries its conclusion, and it was still not chosen. The seed A-LIVE-187 miss is the real miss; the file choice may be mine, not the system's.
- **T4 names the v5 context brief.** Four blind picks chose `positioning/README.md`, the canon with dates, which carries v5's throughline. The register's own record calls the README the canon. The test may name the weaker file.

Both are his word. The tests are frozen.

# 6. Adjacent issues seen, not fixed

- `seedbank/spoken/garden-state.md` is a dashboard, not a seed, and is counted in the `seeds` source.
- The pointer check splits a path at a space, so the Dropbox path under "Venkat Gullapalli" reads as unresolved. One agent caught it.
- The script's conflict candidates pair every result with any authoritative one; agents called them "tier pairings, not disagreements" and ignored them. The model's flags were the useful ones.
- `career-advisor`, `public-site`, and `warehouse` are external sources that add zero records to a scope; agents picked them and got nothing. The `sources` line should say so.
- The 2026-09-11 interview produced about fifteen near-duplicate seeds on one theme (A-LIVE-212 to 232); one agent spent most of its ranking effort choosing among them.

# Files written this session for the build

`context/sources/retrieve.py`, `context/sources/tests/run_tests.py`, `.claude/skills/retrieval/SKILL.md`, `context/sources/index/` (ignored), one line in `context/sources/discovery-accepted.txt`, `GATES.md` (the ledger; G3 abandoned with this report as the handoff), the retrieval entries in `docs/architecture/`, and this report. Nothing in `work-os/brand-os/model/` changed.
