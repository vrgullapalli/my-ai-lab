---
name: alfred-open
description: Alfred's open routine, which replaced daily-brief on 2026-09-10. Runs the duty pass (threats, record honesty, what is claimed running), writes receipts for any session that ended without one, pulls today's cloud briefs into the lab, rolls the to-do list forward, and gives Venkat a short brief with exactly one next action whose first step is already prepared. A SessionStart hook runs it on the first session of each day. Also use when Venkat says brief, morning brief, what does today look like, what's on my plate, where were we, catch me up, or after an interruption.
---

# Alfred — open routine

> **Base directory:** the lab root, `/Users/venkatgullapalli/Documents/my-ai-lab/`.
> Replaced `daily-brief` on 2026-09-10 at Venkat's word ("have daily-brief rebuilt as
> alfreds open-routine"). The old skill is in `~/Documents/_warehouse/skills-archived-2026-09-10/`.

## What it is for

Venkat's own definition of done, `DONE.md` section 2: *"The daily briefing is an ignition
system, not a report."* It must name **exactly one recommended next action, with the first
step already prepared**, and be *"short enough to read on a bad focus day. If I skim past
it, it's too long."*

Driver 1 in `context/intent/STANDING.md` names what would ruin it: *"A briefing that reports what he already
knows"* and *"Duties that depend on someone remembering to run them."* That is why a hook
starts this routine, and why the brief leads with what changed, not with what is.

## Where the facts come from

**Every number in the brief comes from the facts script. None come from memory or opinion.**

```bash
python3 .claude/agents/alfred/sensors/facts.py open     # the fact sheet
python3 .claude/agents/alfred/sensors/facts.py loops    # follow-ups still open
```

On the first session of a day the SessionStart hook has already run `facts.py open` and put
the sheet into the session. Use it; run the script again only if the session has been open
for more than an hour. Lines that start with `ALERT` are the ones worth his attention.

## Steps

0. **Read State first** (State v0.1, 2026-09-13, AD-37). Before anything else, ask the ledger what is
   currently true, so the brief starts from the record and not from a re-read of folders:
   ```bash
   python3 context/state/state.py package --scope ai-lab --consumer brief --fields active,changed,open,waiting,decided,carry_forward
   python3 context/state/state.py check
   ```
   The package's `carry_forward` holds the newest "next session starts with"; `waiting` is the three
   homes as one list with a source on each item; `active` says who holds what. Anything the check lists
   as a conflict or stale goes into the brief's "at risk" lines; never fix a line, append a corrected one.
   What the package cannot answer, the steps below still find; State is the index, the receipts are the record.

1. **Catch sessions that ended without a receipt.** For each `ALERT sessions that changed
   files but wrote no receipt` line, run `alfred-close` in late mode with that note
   (`.claude/agents/alfred/state/unreceipted/<id>.json`). It lists the files changed and the
   transcript path. When the late receipt is written, move the note into
   `.claude/agents/alfred/state/unreceipted/done/`. More than two waiting: write one combined
   late receipt and say so.

2. **Duty pass — D1, D2, D3** as `.claude/agents/alfred/DUTIES.md` scripts them, reading
   `context/intent/STANDING.md` first. The facts sheet already holds most sensor results
   (repos, unpushed commits, snapshot and off-machine copy ages, log gap). D2's lab-wide loop
   list is `facts.py loops`. D3's `work-os/scheduled-tasks/market-signals/verify.sh` runs at most once a day. D5 runs
   too when it is due (seven days after the last review line).

3. **Pull today's cloud briefs into the lab.** Only a Claude session can read them. List
   Artifact pages; for each task in `work-os/scheduled-tasks/` whose `ROUTINE.md` names a page
   title, read today's page (`<Title> YYYY-MM-DD`) and save it as plain text, headings kept,
   to `work-os/scheduled-tasks/<task>/outputs/YYYY-MM-DD.md`. Skip any already saved. Save
   the text as published; do not summarize inside the file. The facts sheet line `cloud
   routine briefs pulled into the lab today` shows how many remain.

4. **Connect what came in to what he cares about.** Keep this to three connections at most.
   - Each brief's top items against the current drivers and the open follow-ups.
   - The strongest headline or takeaway of each brief against the seeds:
     `python3 .claude/skills/seed-capture/scripts/find-similar.py "<the takeaway>"`.
     A seed scoring 0.30 or more means the market is talking about it today. Name it by its
     title. Write nothing to the seedbank; the cultivator acts on it only at his word.

5. **Roll the to-do list.** `.claude/agents/alfred/TODAY.md` is his list for the day. If its
   date is past, copy it to `evidence/receipts/<its date>--today-list.md` (a record), then
   start a fresh `TODAY.md` for today carrying every unchecked item forward, marked
   `(from <date>)`. Checked items stay in the record. Never drop an item silently.

5a. **Refresh the waiting list** (Venkat, 2026-09-10 16:42: "add it to the morning brief").
   Run `python3 .claude/agents/alfred/sensors/waiting.py --html`, save the output to the
   session scratchpad, and republish it to the private page "Waiting on Venkat" (find its
   link with the Artifact tool's list action; publish to that `url`, never a new one). The
   facts sheet's `waiting on Venkat` line carries the count and the oldest item; the brief
   quotes that line and gives the link. Nothing else about the list goes in the brief.

6. **Prepare the first step of the one next action.** Pick it from, in order: an unlazy
   ledger left open (`GATES.md`), the newest receipt's `Next session starts with`, a follow-up
   that is slipping, a pending gate on the article in progress, the top of `TODAY.md`. Then
   actually prepare it, inside what Alfred may do alone (`AUTHORITY.md`): open and read the
   file, draft the text, write the exact command. Never send, publish, push, or commit it.

7. **Give the brief.** Under 150 words, in this shape:

   ```
   Alfred — Thursday brief

   **Start here:** <the one action> — <the prepared first step: a path, a draft, a command>

   **What changed:** up to three bullets, newest first
   **Waiting on you:** the count and the oldest item, with the link to the page
   **At risk:** up to three — a threat from STANDING.md that became true, or a follow-up
     slipping, each with a 10-minute way to get it moving
   **You might be forgetting:** up to three
   **Already done for you:** late receipts written, briefs pulled, list rolled
   ```

   *"Urgency yes, dread no"* (`DONE.md` section 5). Never "this has been open for three
   weeks." Give the recovery step instead. Anything that cannot be verified is `Unknown`.

8. **Log it.** One line per duty in `.claude/agents/alfred/LOG.md`, append only, plus:
   `YYYY-MM-DD HH:MM | OPEN | ran | next action: <≤10 words> | facts.py open`.
   The facts script reads that `OPEN` line to know the open routine already ran today.

9. **Ask once for anything that needs his word** — uncommitted repositories, the unpushed
   `telegraph-plus` commits, a routine decision. One line, one question.

## Skills it brings in, and when

The routine suggests these; it runs none of them without a reason in the facts.

| When the facts show | Offer |
|---|---|
| A seed scored 0.30 or more against today's market briefs, or it is Monday | the cultivator's "what is close to ready" |
| ARCHIE's inbox has an item waiting more than three days | `/archie` on the oldest |
| The article in progress has a pending gate | that gate as the next action |
| A lot moved since the last check (many files, or files moved) | `/context-check`, and `python3 .claude/skills/context-check/dead-pointers.py` |
| A Tier 1 target's board snapshot is more than 14 days old | `/scan <company>` (runs locally) |
| A `GATES.md` ledger is open | finishing it, via `unlazy`, before anything new |
| Yesterday's day review flagged a public-value candidate | `public-value-opportunity` on it |
| The Matching Roles Scan brief arrived today | its top match, in one line |

## Rules

- Scripts decide what is true. If the facts script fails, say so and give a brief without
  numbers rather than guessing them.
- Three items per section at most. The brief is not an inventory.
- Nothing external. No sending, publishing, pushing, or committing, and no Artifact page is
  published by this routine. Reading pages is fine; publishing one needs his word.
- Everything written is append-only or a new file. Nothing is deleted; anything retired goes
  to `~/Documents/_warehouse/`.
- First line of the brief is `Alfred —`.
