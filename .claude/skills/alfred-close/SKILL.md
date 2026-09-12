---
name: alfred-close
description: Alfred's close routine, which replaced session-receipt and daily-review on 2026-09-10 and runs seed-capture every time. Measures what actually changed, writes an immutable receipt to evidence/receipts/, records follow-ups so the next open routine brings them back, scans the session for seeds, syncs observations about how Venkat works (duty seven), archives a finished unlazy ledger, and once a day writes the day review that feeds tomorrow's brief. Use when Venkat says wrap up, close out, done, done for today, end of day, daily review, session receipt, save where we are, or when a session that changed files is ending. Zero writes is a valid close.
---

# Alfred — close routine

> **Base directory:** the lab root, `/Users/venkatgullapalli/Documents/my-ai-lab/`.
> Replaced `session-receipt` and `daily-review` on 2026-09-10 at Venkat's word ("merge
> daily-review with session-receipt ... rebuild session-receipt as part of Alfred's close
> routine"). The old skills are in `~/Documents/_warehouse/skills-archived-2026-09-10/`.

## What it is for

*"Nothing decided, changed, or committed in a session may exist only in the chat context."*
That was the old receipt's purpose, and it still is. `DONE.md` section 4 raises the bar:
*"Slippage detection is assumed to be the only detection. The system must not rely on me
noticing anything is late."* So every follow-up leaves this routine with an owner and a
prepared first step, in a form the open routine can find again by script.

**If he just closes the window**, the SessionEnd hook notices a session that changed files
and wrote no receipt, and leaves a note. The next open routine writes the receipt late, from
the transcript. Closing properly is better; forgetting to is covered.

## Where the facts come from

```bash
python3 .claude/agents/alfred/sensors/facts.py close <session_id>   # what changed, measured
python3 .claude/agents/alfred/sensors/facts.py loops                # follow-ups still open
```

The session id is in the context the SessionStart hook gave this session. The script decides
what changed. Anything you remember doing that the script does not show is **unverified**,
and the receipt says so.

## Steps

1. **Measure.** Run `facts.py close`. If nothing changed and nothing was decided, say "no
   durable change", write no receipt, and go to step 7 (duties six and seven still run).

2. **Read the session back** and pull out, each checked against the measured changes:
   - **Decisions**, with his words quoted and the time.
   - **What changed**, one line per area. Anything claimed but not in the measured list is
     marked `unverified`.
   - **Follow-ups** (duty six, commissions). Every ask still open, written exactly as
     `- [ ] F-YYYYMMDD-HHMM-n: <what> — owner: <who> — first step: <prepared step>`,
     using the receipt's own date and time. The open routine finds them by that pattern.
     Audits use the same pattern, in a `follow-ups.md` inside their dated folder; the sensor
     reads audit folders too (Venkat, 2026-09-11: "a finding no sensor reads is a note to nobody").
   - **Closed.** Any follow-up from `facts.py loops` that this session finished, listed under
     `## Closed` as `- F-... — <the evidence>`. No evidence, not closed.
   - **Corrections** he made. Recorded as evidence with the context, never as new rules —
     a rule changes only when he confirms it.
   - **Seen outside the lab:** commits (with hash), pushes, published pages (with link), sends.
     Or "nothing".
   - **Next session starts with:** one action, first step prepared.

3. **Seeds — every close.** Run `seed-capture` in **Scan** mode over the session (Venkat,
   2026-09-10: "have seed capture be triggered when session-reciept is run or triggered").
   For each candidate run `python3 .claude/skills/seed-capture/scripts/find-similar.py
   "<the claim>"`; a match of 0.45 or more is probably a repeat, a lower one is a candidate
   connection or conflict. Show at most five, numbered. **Write seeds only on his pick** ("1
   and 3"), or when a moment was marked "this is a seed" during the session — writing stays
   governed by D-137. Ask seed-capture's one question once: "did any wording get fixed
   today?" No candidates is a normal answer.

4. **Duty seven — observations.** As `DUTIES.md` D7 says: anything learned about how Venkat
   works is appended, one line each, to `docs/about-me/how-i-work--observed.md`. Never to
   `context/how-i-work.md`.

5. **An open unlazy ledger.** If `GATES.md` sits at the lab root, run
   `node .claude/skills/unlazy/scripts/gate-check.mjs --status GATES.md`. All met: copy it to
   `evidence/receipts/<receipt name>--gates.md`, then move the root copy to
   `~/Documents/_warehouse/unlazy-ledgers/`. Anything unmet becomes a follow-up. Never tick a
   gate by hand.

6. **Write the receipt**, only when something durable changed.
   - Path: `evidence/receipts/YYYY-MM-DD-HHMM-<two to five plain words>-<id>.md`, where `<id>`
     is four random hex characters (`openssl rand -hex 2`). If the path exists, never
     overwrite: mint a new id and say a collision was refused.
   - Receipts are never edited after writing. A correction is a new receipt naming the old one.
   - Template:

   ```
   ---
   id: R-YYYY-MM-DD-HHMM-<id>
   type: receipt
   date: YYYY-MM-DD
   status: final            (late, when written by the open routine from a transcript)
   computer: laptop
   session_id: <from the SessionStart context>
   connects: []             (seed IDs, follow-up IDs, and receipt IDs this one touches)
   supersedes:
   ---
   # Session receipt — YYYY-MM-DD HH:MM — <the plain words>

   **Next session starts with:** <one action> — <its first step, prepared>

   ## Decisions
   ## What changed
   ## Follow-ups
   - [ ] F-YYYYMMDD-HHMM-1: <what> — owner: <who> — first step: <prepared step>
   ## Closed
   ## Corrections
   ## Seen outside the lab
   ## Seeds
   ## Open questions
   Model: <exact model id>
   ```
   Keep the headings exactly as written; the facts script reads them.

7. **Keep the lists.** Tick finished items in `.claude/agents/alfred/TODAY.md` and add any new
   one he asked for today. Append the log lines:
   `D6` (commissions and their states), `D7` (observation lines appended, or `none`), and
   `YYYY-MM-DD HH:MM | CLOSE | ran | <receipt name or "no durable change"> | facts.py close`.

8. **The day review — once a day.** Write `evidence/receipts/YYYY-MM-DD--day-review.md` when
   he says end of day, done for today, or daily review; or when it is after 5 PM and today has
   none; or when the open routine finds yesterday has receipts but no review (then it is
   yesterday's, marked late). Front matter as a receipt, with `type: day-review`. Body:
   - **Did the brief get him started?** Compare today's `OPEN` log line's next action with
     the receipts: started, or not. `DONE.md` calls "days I open the system but start
     nothing" the single truest measure.
   - **What worked, what didn't, what to change** — three each at most, each with a pointer
     to its evidence.
   - **Slipping** — each open follow-up past its moment, with a ten-minute way back in.
   - **Public value** — anything today that could help someone else, for
     `public-value-opportunity` to look at later. Or "none".
   - **Tomorrow starts with** — one action. The open routine reads it.
   When duty five is due, run it here and put its result in the review.

9. **Close the session in under 150 words:** the receipt path; follow-ups opened and closed;
   seed candidates, numbered, "say the numbers to capture"; and one question for anything that
   needs his word, such as "commit these three repositories?". Never commit without it.

## Late mode

Called by the open routine with a note from `.claude/agents/alfred/state/unreceipted/`. Read
its changed-file list and the transcript at its `transcript_path`. Write the receipt with
`status: late` and one line under the title: *"Reconstructed from the transcript after the
session ended without a receipt. Not confirmed by Venkat."* Skip the seed scan's questions;
list candidates in the receipt instead, for the next brief.

## Skills it brings in, and when

| When the session | Bring in |
|---|---|
| Ran at all | `seed-capture`, Scan mode, every close |
| Produced an insight that could help someone outside | a line in the day review for `public-value-opportunity` |
| Left a research question open | offer to drop it in ARCHIE's inbox |
| Moved or renamed many files | `/context-check` and `dead-pointers.py` before closing, and the result in the receipt |
| Drafted anything public in his voice | a reminder that `my-voice` runs its voice pass before it ships |
| Opened an unlazy ledger | step 5 |

## Rules

- A script decides what changed. You decide what it means.
- One home per fact: the receipt points to files, it does not copy them.
- No secrets, tokens, or client-confidential material in a receipt.
- Nothing external without his word. Nothing deleted; retired things go to the warehouse.
- First line of the close message is `Alfred —`.
