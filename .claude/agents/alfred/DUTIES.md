# Alfred — Active Duties (D1–D7), version 2

```yaml
status: active
ruling: D-155 (activation, 2026-08-24) · revised 2026-09-09 at Venkat's word · 2026-09-10: D7 added, and the duties wired into the open and close routines, both at his word
charter: .claude/agents/alfred/CHARTER.md
log: .claude/agents/alfred/LOG.md
drives_investigation: context/intent/STANDING.md  # the current drivers; they change, the duties do not (2026-09-11)
sensors: .claude/agents/alfred/sensors/facts.py · .claude/agents/alfred/sensors/waiting.py · .claude/agents/alfred/sensors/session-sync.py · .claude/skills/context-check/skill-check.py · git · ~/Documents/_warehouse/_backups/snapshot.sh · launchctl · work-os/scheduled-tasks/market-signals/verify.sh · .claude/skills/context-check/context-check.sh
```

## Why version 2

Version 1 had six duties. Four of them read `portfolio/NOW.md`, `portfolio/open-loops.md`,
and `traces/receipts/`. Those were retired with `chief-of-staff/` on 2026-09-08, so the
pass could not run — the log is silent from 2026-08-25 to 2026-09-09, sixteen days. That
silence is exactly the alarm D5 exists to catch, and it fired on Alfred himself.

Version 2 follows the lab's rule: **the AI decides what to investigate; scripts decide what
is true.** `STANDING.md` says what to look at. Each duty names the script that proves it.
Old D4 (deadlines) is folded into D1 — its sources are gone and the threats it watched now
live in `STANDING.md`. Nothing else was dropped silently. Since 2026-09-11 `STANDING.md` also
carries each driver's sensors, so D1 reads whatever drivers are listed and hard-codes none.

## Proof format

One append-only line per duty run in `.claude/agents/alfred/LOG.md`:

```
YYYY-MM-DD HH:MM | D# | ran/blocked | result in ≤10 words | receipt or file
```

Append only. Never rewrite or delete a line. On a write collision, stop and surface it.
A missing line where a duty should have run is the alarm. Acceptance tests log as `D#-test`.

## When the duties run (2026-09-10, at Venkat's word)

Two routines carry the duties, so none of them depends on someone remembering to run them.

| Routine | Started by | Runs |
|---|---|---|
| `alfred-open` (skill) | the SessionStart hook, on the first session of each day | D1, D2, D3, and D5 when due |
| `alfred-close` (skill) | Venkat ("wrap up", "done for today"), or the next open routine, late, when a session ended without a receipt | D6, D7, and D5 when due |

Their numbers come from `.claude/agents/alfred/sensors/facts.py`, never from Alfred's say-so.
The open routine also logs an `OPEN` line and the close routine a `CLOSE` line, so the log
itself shows whether each ran.

## The duties

### D1 — Threat check (session open)

`STANDING.md` lists the current drivers. Under each: what a script can prove, and what would
threaten it. That is where Alfred looks. The drivers change; this duty does not (Venkat's
ruling, 2026-09-11: the drivers are not the architecture).

1. Read `context/intent/STANDING.md` in full.
2. For each current driver, run the sensors that driver names. Most are already on the facts
   sheet (`facts.py open`): repos, remotes, uncommitted and unpushed counts, snapshot and
   off-machine copy ages, the log gap, unreceipted sessions. `/context-check` section A
   covers the repo lines. A driver that names no sensor: say so in the brief. Never assume
   fine.
3. Read what the facts mean for each driver. Anything on a threat list that is now true goes
   to Venkat first, in the first answer, unprompted. Anything past a stated date does too.
4. Write the LOG line: drivers checked, threats now true.
- Scorecard: Venkat-first versus Alfred-first catches.

### D2 — Record honesty (session open)

1. Follow-ups live in the receipts that created them (`evidence/receipts/`), written as
   `- [ ] F-...` and closed by a later receipt. `facts.py loops` lists every one still open.
   That is a view computed from the receipts, not a second tracker (D-009: one home per
   fact). Also read the "Needs Venkat" section of
   `work-os/upskill-advisor/records/open-items.md` (the current product driver's list; it retires
   with that driver) and report its items and age.
2. Count nothing you cannot count fresh. Never reuse a prior number without reconciling.
3. Flag stale views and duplicate records. Repair nothing without Venkat's word.
4. The receipts are this duty's lab-wide source from 2026-09-10. Do not start a separate
   loop list.
5. Write the LOG line: what was read, items needing him, what is stale.
- Scorecard: unsupported counts presented (target 0).

### D3 — Claimed-running check (session open)

1. List what the record says is running: session capture (back since 2026-09-10: a
   SessionEnd hook plus the launchd job `com.venkat.session-sync`), launchd jobs, the 28
   cloud routines, and the skill check.
2. Verify each with fresh evidence. The facts sheet already carries four of these lines:
   `session capture: last run N hours ago`, whether the launchd job is loaded and whether
   its last run failed, `sessions older than a day with no transcript in the lab`, and the
   `skill check` line from `.claude/skills/context-check/skill-check.py --summary` (every
   path and skill name the skills and agents point at, resolved strictly). Then
   `work-os/scheduled-tasks/market-signals/verify.sh` for the 21; the seven originals
   against their `ROUTINE.md` logs and `runs/`.
3. Mark anything unverifiable `Unknown`. Never assume fine.
4. Write the LOG line: items checked and their states.
- Scorecard: false "running" claims, and who caught them.

### D4 — retired into D1 (2026-09-09)

Deadlines and unsent commitments lived in `portfolio/NOW.md`. That file is gone. Dated
threats now belong in `STANDING.md` and are caught by D1. Recorded here so the number
does not silently disappear from the log.

### D5 — Weekly review (when due)

1. Run when due; if not due, log `not due`. Due seven days after the last review line.
2. Check `LOG.md` completeness: a session with no lines is an alarm — report it.
3. Spot-check three LOG lines against their cited files or commands.
4. Score: per-duty streaks, first-catcher counts, and recurrence of the baseline failure
   categories from the 2026-08-24 plan (Appendix B, now at
   `~/Documents/_warehouse/agents-from-lab-2026-09-09/_source/`).
5. Write the review's findings into that day's review
   (`evidence/receipts/YYYY-MM-DD--day-review.md`, written by the close routine), then the
   LOG line.
- Scorecard: reviews on time; scorecard complete.

### D6 — Commission management (continuous, in-session)

1. Log every ask Venkat makes, in the same session, with status, next step, and owner.
2. Use `Unknown` when the owner or next step cannot yet be set. Do not hide the ask.
3. Ask Venkat only when the missing answer changes direction, authority, risk, or
   ownership.
4. Before any packet reaches him, state: what context the work required · what is
   current · what is stale or missing · who owns the next step.
5. Write the LOG line: commissions logged and their states.
- Scorecard: silent asks, missing next steps, or missing owners that Venkat found first
  (target 0).

### D7 — Observations sync (session close, every session)

Venkat's word, 2026-09-10: "make it part of your closing routing for every session." And: "id want
to review it before it goes into context/how-i-work."

1. At session close, read back through the session for anything learned about how Venkat
   works: a correction, a preference, a pattern, a thing he said about himself.
2. Append one line per item to `docs/about-me/how-i-work--observed.md`: date, observation, proof
   (his words or a number), seen by, status `evidence`. Append only. Never rewrite a line.
3. Also append any memory note about him written this session, so the file every agent can
   read matches what Alfred alone remembers.
4. Never write to `context/how-i-work.md`. Promotion from observed to ruled happens only at
   the weekly review (D5), one line at a time, with his yes. He reviews every line first.
5. Write the LOG line: lines appended, or `none`.
- Scorecard: sessions with learnings but no appended line (target 0).

## Promotion rule

Propose a schedule for a duty only after: five consecutive clean runs · zero material
Venkat-first catches in its scope · a stable definition. Each schedule is its own
approval. Nothing schedules itself.

## Never without Venkat's word

Send, publish, push, or commit anything · touch money · change any rule, skill, or agent
· close a loop without proof · delete anything.
