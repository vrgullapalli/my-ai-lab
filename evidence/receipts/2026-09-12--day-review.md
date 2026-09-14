---
id: R-2026-09-12-day-review
type: day-review
date: 2026-09-12
status: late
computer: laptop
session_id: d249a842-c33f-40cc-aca7-ae37a1595d5d
connects: [R-2026-09-13-0502-b134, R-2026-09-12-0154-cc95, R-2026-09-12-0220-55af, F-20260912-0134-3]
supersedes:
---
# Day review — 2026-09-12 (written late, 2026-09-13 05:02)

Written by the close routine at the next session because the day had receipts and no review.

**Did the brief get him started?** No brief ran. The log has no OPEN line for 2026-09-12; the open routine was owed from 01:34 and skipped at every session start, including 02:13. The day started from his pasted specs, not from a prepared next action. By the facts sheet, 13 sessions ran that day, nine at once at the peak, and 13 sessions changed files without a receipt.

**What worked**
- Tests before code. The seven frozen tests, approved at 02:24 with his boundary rule, gave every later run a fixed target and made "5 of 7, then 6 of 7, then stage one twice" mean something. Evidence: `docs/reports/2026-09-12--retrieval-v0-1-first-runs.md`, `-semantic-candidates.md`, `-staged-selection.md`.
- Blind agents as proof. Every semantic pass was a fresh agent that saw only the index and the package; the positive and negative controls and the boundary refusal made the scorer trustworthy. Evidence: run_tests.py controls, 7 of 7 and 0 of 7.
- The forensic trace before the fix. The nine-layer trace and the hundred-line test located the failure at selection overload and stopped a build on embeddings that the probe shows would have missed too. Evidence: the read-only pass at 04:50, the probe ranks 699 and 516.

**What didn't**
- About 6.9 million tokens went into six full-index blind runs before the small test that settled the question in two runs of 76,000 tokens. Evidence: the cost tables in the first-runs report.
- The staged experiment's second level was never tested on its own and dropped the seed twice. Evidence: staged-selection report section 2.
- The open routine did not run, and the receipt for this session came at 05:02 the next day on his `/session-receipt`. Evidence: LOG.md has no OPEN line for 09-12.

**What to change**
- Run the smallest test that can settle a question before the big run. The hundred-line test should have come after the first two failures, not after six.
- Every cut a pipeline makes gets a planted-record test before it goes live.
- Run the open routine before answering the first message, whatever it says.

**Slipping**
- F-20260912-0134-3, the open routine, two days owed. Ten minutes back in: type `/alfred-open` at the next start.
- F-20260910-1349-5, the front-door line "No off-machine copy of anything," three days. Ten minutes: one line replaced on his yes; T6 returned the conflict twice today.
- The routine ruling from the 11th, named in three reports. Ten minutes: read section 5 of the hand-test report and rule.

**Public value**
- The planted-record selection test: put the known record in a set of a hundred and see whether the pick changes. A cheap, repeatable way to tell "did the system read it" from "did it understand it." For `public-value-opportunity`.
- A retrieval system saying "found" about a package that is missing the one record that matters, with the case that shows how.

**Tomorrow starts with:** his choice on the staged-selection cap (180 for one final rank, or a wider second level) — first step: section 4 of `docs/reports/2026-09-12--retrieval-v0-1-staged-selection.md`; then the seven staged tests run.
