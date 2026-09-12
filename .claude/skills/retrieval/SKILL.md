---
name: retrieval
description: Shared Retrieval v0.1 (build step 3, AD-22). Use when a session, Alfred, ARCHIE, signal reasoning, or a career-model reader needs the evidence the lab already holds on a question, with its source, date, authority tier, use ceiling, limits, conflicts, and gaps. Triggers on "retrieve", "what does the lab hold on", "what have I said about", "find the evidence for", "does this connect to anything", "/retrieval". Returns an evidence package. Never the judgment.
---

# Retrieval v0.1

> **Base directory:** all relative paths in this skill resolve from the lab root
> (`/Users/venkatgullapalli/Documents/my-ai-lab/`). The script is `context/sources/retrieve.py`.
> The tests it must pass are `context/sources/tests/RETRIEVAL-TESTS.md`, frozen 2026-09-12.

**The contract** (Venkat, 2026-09-12 02:24): find the evidence that could materially change the judgment,
preserve its source and limits, and expose conflicts or gaps. Retrieval returns relevant evidence, current versus
superseded material, authority and freshness, conflicts, source limits, and a missing-evidence state.
**The consumer reasons from that package.** Retrieval never answers the question.

**Who does what.** The script decides what is true: what may be read (the register), what a record says, its
date, tier, ceiling, marks, pointer state, which row corrects which. The model decides what is relevant: it reads
the compact index, picks candidates by meaning, ranks them, says why each matches, and flags conflicts. The model
never quotes a file the script did not fetch, and never reads outside the register to fill a gap.

## The five steps

0. **Pick the sources first (the model's first stage; added after the first two blind runs, 2026-09-12).**
   ```
   python3 context/sources/retrieve.py sources
   ```
   Twenty-four lines: id, ceiling, tier, kind, what it may inform, what it must not establish alone. Pick the
   ids that could hold evidence for the question, from the register's own words, not from a guess. Be inclusive:
   two to eight sources. The first two blind runs read all 1,813 records (633 KB, then 760 KB) for every
   question and missed the meaning test twice; a pass over the sources that can hold the answer is smaller and
   sharper. Use no scope only when the question gives no clue at all.

1. **Candidates and the compact index.**
   ```
   python3 context/sources/retrieve.py index          # only if the index is older than the newest source change
   python3 context/sources/retrieve.py candidates "<the question, as asked>" --scope id,id --scoped-out <file>
   ```
   The command prints the deterministic candidates (exact ids and names, keyword overlap), the size of the full
   compact index, and the size of the scoped file it wrote: one line per record,
   `ref | source | date | tier | ceiling | title — gist`. That scoped size is the cost of this pass; record it.
   Two rules the script applies to every scope (from run 3, 2026-09-12): the four small rule-bearing sources
   (rulings, root-doctrine, drivers, architecture) are always in scope, because two blind passes scoped out the
   ruling their question turned on; and the scoped file opens with a "must consider" section, the deterministic
   candidates in score order, before the full scoped list, because an exact name or a shared word is evidence
   the model should see first, not rediscover.

2. **The semantic pass (the model's only job, with step 4).** Read the compact index in full, or the scoped
   part when the consumer gave a scope. Pick up to ten records by meaning, not by shared words. Rank them.
   Write `picks.json`:
   ```
   {"picks": [{"ref": "<ref from the compact index>", "reason": "<one line: why this matches>"}],
    "semantic_pass": {"records_read": <n>, "bytes_read": <n>, "scope": "full" | "<ids>"}}
   ```
   A ref is copied from the index, never invented. A ruling that constrains the topic is a pick, marked in its
   reason as a rule. The index is too big for one read (first run, 2026-09-12: 16 reads of about 120 lines), so
   keep a running shortlist of up to 20 refs while reading, and rank the union at the end; do not rank chunk by
   chunk. If nothing in the index answers the question, pick the nearest records that show the
   absence and say so in the reasons.

3. **Fetch, deterministically.**
   ```
   python3 context/sources/retrieve.py fetch --query "<the question>" --picks picks.json --out package.json
   ```
   The script refuses any ref outside the eligible set and says so. Each result carries: evidence lines from
   the record itself; the source's `not-alone` and `may-inform` limits; the record's marks (claimed, observed,
   his word, page not opened, vendor-owned outlet); current or superseded, with the correcting row; pointers
   named inside the record and whether they resolve; age in days. The package also lists every source
   searched, the script's own missing-evidence floor, and the index size line.

4. **Flag, then hand over.** Read `package.json`. Add to `picks.json` and fetch once more:
   - `"conflicts": [{"a": ref, "b": ref, "what": "<one line: what disagrees, and the marks that let the consumer weigh it>"}]`
     when two results from different sources disagree. Name both sides. Do not choose.
   - `"missing_evidence": {"state": "missing" | "partial" | "found", "reason": "<one line>"}`
     when the package does not hold what was asked. `missing` means: say the gap, list what was searched,
     return the evidence of absence.
   Then give the consumer the package, not a summary of it. A figure marked claimed stays marked claimed.

## Rules

- Only registered sources with status live or degraded (`context/sources/REGISTER.md`). The script enforces it.
- A career-model match without a capability id and an extract is not returned (ruling 038). Nothing writes into `work-os/brand-os/model/`.
- Every run appends one line to `context/sources/index/runs.jsonl` (the write-back record: query, picks, refused, missing state, size of the semantic pass). Git ignores the index folder; it is derived.
- **Watch the size line.** `python3 context/sources/retrieve.py stats` prints records, bytes, and estimated tokens of the full-index pass. When the frozen tests start failing because the pass is too big to read whole, that is the evidence a different semantic method has become necessary. Not before.

## Proof, and where v0.1 stands

`python3 context/sources/tests/run_tests.py --selections <file>` fetches every test's picks deterministically and
scores the seven pass conditions on the package. Four blind runs on 2026-09-12: final 5 of 7. T2 (the meaning
match to seed A-LIVE-187) failed every run; T4 failed on one file's rank every run. Details, sizes, and costs:
`docs/reports/2026-09-12--retrieval-v0-1-first-runs.md`. **Status: building, not trusted for the meaning job.**
A consumer may use the package for exact, ruling, career-model, conflict, and missing-evidence questions, and
must treat a meaning match as unproven until he rules on the method or the test.
