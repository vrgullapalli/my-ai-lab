---
title: Retrieval v0.1, close-out for downstream use
date: 2026-09-13
author: Alfred (session 11ed46ab), at Venkat's word (the /goal of 05:29: "Finish Retrieval v0.1 from the current staged-selection state. Reuse the existing Salt A/B stage-one outputs, remove the unvalidated second-level cut, final-rank the existing ~172-record unions, then run the frozen test suite if T2 permits.")
kind: the close-out evaluation; four blind final ranks on the reused stage-one picks, one composite run of the seven frozen tests, the checks, the interface for downstream consumers, the known limitations, and one decision for him
follows: docs/reports/2026-09-12--retrieval-v0-1-staged-selection.md (stage one picked the seed under both salts; the second-level cut dropped it); docs/reports/2026-09-12--retrieval-v0-1-semantic-candidates.md (baseline 6 of 7)
question: "With the second level gone, does one final rank over the 172-record union keep the seed, and can State and Context Assembly consume Retrieval safely as it stands?"
result: T2 FAIL under both salts on the one-level union (172 records), and FAIL again under both salts on the one corrective pass (the 112 stage-one picks alone). The seed was in every union and was never in the ten. Its developed sibling, the article's locked gate-one file, was in the ten every time (ranks 5, 3, 2, 3). The seven frozen tests stand at 6 of 7, the same as the baseline, with no regression. Boundary, provenance, conflict, supersession, pointer state, and missing-evidence behavior all pass by script. Retrieval v0.1 is closed for downstream use with the meaning-recall limitation recorded; the staged path is not promoted.
checks:
  t2_one_level_salt_A: FAIL (seed union line 112, not picked; research file union line 156, not picked; gate-one file rank 5)
  t2_one_level_salt_B: FAIL (seed union line 142, not picked; research file not in the union; gate-one file rank 3)
  t2_corrective_salt_A: FAIL (112 winners only; seed not picked; gate-one file rank 2)
  t2_corrective_salt_B: FAIL (112 winners only; seed not picked; gate-one file rank 3)
  seven_tests: 6 of 7 (T2 from the salt A one-level run, the other six from run 5f re-scored today); no regression
  register: 24 sources, 0 findings; architecture: 0 findings after three map pointer fixes; reachability 24 of 24; boundary refused; planted faults all passed; career model untouched
  staged_path_promoted: no
needs_venkat:
  - the status word for the registry entry (building stays; live or degraded is his call under the building-to-live gate)
  - T2's second known answer and the seed-versus-article question (F-20260913-0502-6), before anyone spends more on the meaning test
tags_used: observed (a script's output or a file read this session) · inferred (my reading) · his-word
---

Alfred — the short version first.

**The seed loses the final contest, every time.** In four blind final ranks today (two salts, two union shapes) the seed A-LIVE-187 sat in the list and never made the ten. It won its group of about 94 twice yesterday. It loses when the field is other groups' winners, whether 172 records or 112. The cut was not the problem; the contest among winners is.

**The connection is found, the named file is not.** Every run returned the article's locked gate-one file, which is the seed written up, at rank 5, 3, 2, and 3. A consumer asking "does this connect to anything Venkat is writing?" gets the article. The frozen test names the seed and the research file, and the research file was never picked in any run, at any size, on any day.

**Nothing else moved.** Six of seven tests pass today as they did yesterday. Every package stayed inside the register, carried source, date, tier, and ceiling, and flagged conflicts and gaps where the tests ask. That is what downstream needs to consume safely. v0.1 closes on that, with the limitation written down below.

# 1. What was done (observed)

| Step | What | Where |
|---|---|---|
| Second level removed | `staged_experiment.py union` now writes one union and ranks it once; `UNION_HEADROOM=180` is headroom, not a cap (a bigger union is written anyway and marked) | `context/sources/tests/staged_experiment.py` |
| Stage one reused | the 14 `group-NN-picks.json` files per salt from 2026-09-12 were copied unchanged; nothing was rerun | `context/sources/index/runs/staged-T2-A-one-level/`, `-B-one-level/` |
| Unions rebuilt | 60 must-consider + 112 stage-one picks = 172 per salt; grouping check still OK, planted duplicate still fails | manifest.json in each folder |
| Final rank, one level | one blind agent per salt read the 172 lines and picked ten, then fetched, flagged, fetched again | final-picks.json, package.json |
| Corrective pass (the one allowed) | the model ranked the 112 stage-one picks alone; the script appended the ten highest must-consider records after (`merge`) | union-picks-only.txt, final-picks-picks-only.json, final-picks-merged.json |
| Seven-test run | one selections file: T2 from the salt A one-level run, the other six from run 5f, re-scored by the frozen runner | `context/sources/index/runs/staged-selections.json` |

# 2. T2 under both salts (observed)

| | Salt A, 172 | Salt B, 172 | Salt A, 112 winners | Salt B, 112 winners |
|---|---|---|---|---|
| seed A-LIVE-187 | in union (line 112), not picked | in union (line 142), not picked | in file (line 53), not picked | in file (line 83), not picked |
| research file 05-research.md | in union (line 156), not picked | not in union (never picked at stage one) | in file, not picked | not in file |
| gate-one locked file | rank 5 | rank 3 | rank 2 | rank 3 |
| model's missing-evidence state | found | found | partial | partial |
| conflicts flagged | 0 | 1 (brief vs written seed on where drift shows) | 0 | 0 |
| refused by the script | 0 | 0 | 0 | 0 |
| frozen condition | FAIL | FAIL | FAIL | FAIL |

The required T2 evidence outcomes: the seed was never in the top five (0 of 4); the research file was never in the top five (0 of 4); the baseline word matcher returns neither (the miss is real, 4 of 4); every result carried source, date, and ceiling (4 of 4); nothing came from outside the register (4 of 4).

**Where the seed has ever been picked blind.** In a group of about 94 with random neighbours: 2 of 2 (ranks 4 and 2). In a hundred-line list: 2 of 2 (rank 5 both times). Among winners at 112 or 172: 0 of 4. Over the full scoped pass of 1,100 to 1,400: 0 of 6. Ten final ranks, ten misses, one shape.

**What the model returned instead.** His own seeds on learning versus reacting (A-LIVE-249, 250, 272), on earning autonomy but not step by step (A-LIVE-209), on the careful path that never asks the question (A-LIVE-213), the gate-one article, and the offer draft that opens "Your pilot works." A writer gets the article and the mechanism. What the writer does not get is the seed's own line, "a check that has never failed may be evidence of nothing," and the research file's line, "No public pharma case of a wrong-question AI evaluation was found," which is the sentence the Lundbeck signal answers.

# 3. The seven frozen tests (observed)

```
PASS T1  exact company relationship      PASS T5  career model, need to proof
FAIL T2  meaning relationship (above)     PASS T6  authority and freshness in conflict
PASS T3  a corrected ruling               PASS T7  honest miss
PASS T4  idea context without the flood
RETRIEVAL TESTS: 6 of 7 passed
```

Same as the baseline of 2026-09-12 04:33. No regression: the six passing selections are unchanged files, re-fetched and re-scored today by the runner. The six staged runs were not made: the goal said "run the frozen test suite if T2 permits," and T2 did not, so about two million tokens were not spent on a path that had just failed its own first test.

# 4. Checks (observed)

| Check | Result |
|---|---|
| source register | 24 registered, 24 live, 0 findings |
| architecture check | 0 findings. It had 3 at session start, all pointer faults in the map's retrieval and context-assembly entries written yesterday (a prose phrase read as a path; two `defined-in` anchors not equal to the id). Fixed in the map only |
| reachability | 24 of 24 known-answer files inside the eligible set |
| boundary | a discovery candidate outside the register refused; the control inside returned |
| planted faults | 27 of 27 caught |
| career model | `git status` clean after every run |
| index | 1,813 records, 760,507 bytes, about 190,000 tokens for a full pass; built 2026-09-12 02:44; 19 markdown files are newer and not yet indexed |

# 5. Cost and latency (observed, the agents' own counts)

| Run | Records read | Bytes | Tokens | Wall clock |
|---|---|---|---|---|
| one level, salt A | 172 | 103,759 | 110,312 | 107 s |
| one level, salt B | 172 | 103,181 | 109,417 | 74 s |
| corrective, salt A | 112 | 69,058 | 98,641 | 114 s |
| corrective, salt B | 112 | 68,609 | 95,758 | 80 s |

The stage-one pass reused from yesterday cost about 390,000 tokens and 8 minutes per salt. A full scoped pass costs 117,000 to 358,000 tokens per question. Staging adds a level and triples latency and does not pass T2, so it stays an experiment beside the tests; the retrieval skill's default path is unchanged.

# 6. The K deviation, recorded (observed)

The goal names a K=10 plan and a K=8 run. The record shows: the plan summary in the transcript of 2026-09-12 says "keep eight per group"; the script's rule gives K=10 only when there are fewer than ten groups; both salt runs had 14 groups and used K=8. Recorded in the script's header. Stage one was not rerun.

# 7. What downstream consumers get (observed, the interface)

**Call sequence** (all from the lab root; the retrieval skill carries the model's part):

```
python3 context/sources/retrieve.py sources                                   # 24 sources, one line each
python3 context/sources/retrieve.py candidates "<question>" --scope id,id --scoped-out scoped.txt --expansions ideas.json
python3 context/sources/retrieve.py fetch --query "<question>" --picks picks.json --out package.json
```

**The Governed Evidence Package** (`package.json`), the fields a consumer may rely on:

- `query`, `when`: what was asked and when.
- `results[]`, in the model's rank order, each with `ref` (path, or path#row/#line/#CAP-id), `source` (register id), `kind`, `date`, `tier`, `ceiling` (the source's use ceiling), `title`, `why` (the model's one line), `evidence[]` (lines the script pulled from the record itself; the model never adds text), `marks` (claimed, observed, inferred, his-word, page-not-opened, vendor-owned-outlet; career-model results carry `extracts` with quotes and pointer state), `limits` (`not-alone`, `may-inform`, `source-notes` from the register), `supersession` (current or superseded, and which row corrects which), `pointers[]` (paths named in the record and whether each resolves), `age_days`.
- `refused[]`: any pick outside the register, by name. A consumer must treat a non-empty list as a model error to log.
- `conflicts`: `flagged_by_model` (both sides named, never settled) and `candidates_by_script` (cross-source pairs where one side is authoritative).
- `missing_evidence`: `script` (a floor: no exact hit and almost no word overlap) and `model` (state found, partial, or missing, with a reason).
- `searched[]`: every source read, with its file count, or external. This is the completeness scope. Absence is claimed only against this list.
- `index`: the size line, so a consumer can see how big the pass was.
- `semantic_pass`: what the model read (records, bytes, scope) and, for staged runs, how.

**Write-back record.** Every fetch appends one line to `context/sources/index/runs.jsonl` (query, picks, refused, missing state, pass size). Consumer write-back is the consumer's job; Retrieval writes nothing into any source.

**Rules a consumer must keep.** Ask by register id, never by path. Lower a source's ceiling for the job; never raise it. A figure marked claimed stays marked claimed. A meaning-match package is partial until proven otherwise (section 8). Judgment is the consumer's; the package is evidence.

# 8. Known limitations, recorded and not blocking (inferred from the observed runs)

1. **Meaning recall at scale is not proven.** A single seed among 819 was found blind only inside a list of about a hundred, never in a final contest among winners or a full scoped pass (0 of 10). A consumer asking a meaning question must read `missing_evidence.model` as at best partial, and must expect the developed form of an idea (an article file) before the seed it came from.
2. **"Found" is not "complete."** The model said found twice today while missing the named seed. Completeness is `searched[]`; the script floor only catches the no-overlap case. Context Assembly should carry `searched[]` into its package rather than the model's state alone.
3. **T2's second answer has never been picked.** The research file was shortlisted in both hundred-line runs and never chosen, and never chosen at stage one under salt B. F-20260913-0502-6 asks him whether the test should name the gate-one file; nothing here changes the test.
4. **Cost and latency are a scoped pass, not a service.** 90 KB to 660 KB read per question, one to six minutes. Fine for Alfred and the morning brief; not for anything interactive.
5. **The index is a snapshot.** Built 2026-09-12 02:44; 19 markdown files are newer. Rebuild is `python3 context/sources/retrieve.py index`. No facts-sheet line watches index age yet; the definition names it as a needed sensor.
6. **Operating Scope is implied, not passed.** The register is the only boundary; `--scope` is a source scope. The five operating scopes are represented in the definitions and not in the script. Every registered source is AI Lab scope today, so nothing crosses; when a Professional or Personal source is registered, scope must become an input before then.
7. **Four small defects stand** (F-20260913-0502-4): the pointer check splits a path at a space; the sources line does not say which sources are external; `seedbank/spoken/garden-state.md` is counted as a seed; the "reached by the idea alone" counter always reports 60.
8. **Staged selection is an experiment, not the path.** It sits beside the tests. Its one demonstrated win is inside a group of about a hundred; its final stage loses what stage one finds.

# 9. Why this closes v0.1 (inferred)

The acceptance line in the definition asks for eight things, and seven hold by script today: packages on representative jobs (six of seven pass), hard boundaries (refusal proven, 0 outside the register in 29 fetches today), evidence fetched deterministically (the model never added a line), provenance and limits travelling (every result), conflicts and gaps surviving (T6, T7), insufficient evidence representable (T7 and the partial states today), and the checks valid (section 4). The eighth, important failures visible, is this report and section 8. What State needs first is exact, ruling, correction, and conflict retrieval, and those pass. What Context Assembly needs is meaning selection with honest limits, and the limit is written down. The stopping rule says stop improving Retrieval in isolation once it is sufficient for downstream use; that is now.

Not promoted: the staged path. Not changed: the contract, the frozen tests, the register, the boundary, the fetch. Not done: the six staged runs, the index rebuild, the four small defects, any change to T2.

# 10. The one decision for him

The registry entry stays `building` because the building-to-live gate names him for the status change. All three gate conditions hold today (operational behavior through the skill and script, failure proof in the boundary refusal and the 27 planted faults, a valid contract with `check.py` at 0 findings). His options: `live`, with the meaning limitation in the proof line; `degraded`, if a known miss should show on the sheet; or `building` until the T2 ruling.

# Files written

`context/sources/tests/staged_experiment.py` (second level removed, headroom, `--picks-only`, `merge`, the K note); `context/sources/index/runs/staged-T2-A-one-level/` and `-B-one-level/` (ignored); `context/sources/index/runs/staged-selections.json` and the four T2 selections files (ignored); `docs/architecture/CAPABILITY-MAP.md` (three pointer fixes, the retrieval proof line); `docs/architecture/CAPABILITY-DEFINITIONS.md` (current evidence); `docs/architecture/ARCHITECTURE-DECISIONS.md` (AD-35, proposed); `context/sources/tests/RETRIEVAL-TESTS.md` (state section only; the seven tests unchanged); `.claude/skills/retrieval/SKILL.md` (status and the consumer section); `context/sources/REGISTER.md` (status line); `GATES.md` (G18 to G22); this report.
