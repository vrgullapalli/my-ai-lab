# Research — ARCHIE, in both directions

He says: research this · run ARCHIE on it · what did ARCHIE find · fold in ARCHIE's run.

ARCHIE is the lab's researcher. It hunts outside, challenges, and frames. It lives at
`work-os/brand-os/engagement-os/agents/archie/` (data) and `.claude/agents/archie/` (the agent). `/archie` launches it.
The cultivator does not hunt. It owns both ends of the hand-off.

## The one hard limit

ARCHIE is an agent. So is the cultivator, and an agent cannot launch another agent.
**It cannot run ARCHIE.** It hands the topic over, and Venkat or Alfred runs `/archie` from
the main session. Never pretend otherwise. Never report an ARCHIE run as done unless its output
file exists on disk.

## Direction 1 — cultivator to ARCHIE

When an idea is close to ready and would be stronger with outside evidence, or when he
says research this:

1. Write one file into ARCHIE's inbox: `agents/archie/inbox/YYYY-MM-DD--<slug>.md`.
   Contents: the idea's own title as the topic, the seed ID, the tension line, and one
   sentence on what outside evidence would move it. Nothing else. ARCHIE's rules say it
   does not need a polished brief.
2. Say to him, in one line: "Dropped in ARCHIE's inbox. Run `/archie` from the main
   session when you want it; with no input it takes the oldest item."
3. Append a history line to the seed: date, "sent to ARCHIE", the inbox file.
4. Update `INDEX.md`.

This is the **one write outside the seedbank** the cultivator is allowed. It is spelled
out in `claude/rules/02-critical-rules.md`.

## Direction 2 — ARCHIE back to the cultivator

After any ARCHIE run, or when he says what did ARCHIE find:

1. Read the newest files in `agents/archie/outputs/*--ideas.md`, `agents/archie/backlog/`,
   and `agents/archie/archive/kills/`.
2. Find every seed ID they name. They appear on `Seed-bank connection:` lines, in
   `Receipts:` and `Lived:` entries, and in backlog `Source moment:` lines. IDs look like
   `A-LIVE-187`, `A-CHR-04`, `A-TOPIC-…`, `A-SEED-…`.
3. For each named seed, propose — do not do — two things:
   - **Mark it used.** An ARCHIE card that cites a seed is the strongest signal in the
     collection: something happened because of it. That is the `used` status in plain
     words. Say which run, which card, and whether the card survived, was routed to
     backlog, or was killed.
   - **Add the link line.** From the seed to the ARCHIE output file, saying why.
4. Run every backlog entry and every killed idea's salvage path through
   `claude/skills/add.md`: is this a new idea, or evidence for an existing one? Most will
   be evidence. Hand anything new to `seed-capture`. Get his fingerprint first — an
   ARCHIE finding he has not reacted to is a bookmark, not an idea.
5. Report: seeds ARCHIE touched · which are now used · new links · anything that looks
   new · anything ARCHIE killed that argues for retiring a seed.
6. He decides each one. Then append history lines and update `INDEX.md`.

## What is already sitting there

Two runs exist from before this seam was built: `2026-09-03--green-eval-scores` and
`2026-09-04--activity-ahead-of-proof`. Between them they name at least twelve seeds. None
has been marked used. The first time he asks for anything from this job, start there.

## What the cultivator never does here

- Run ARCHIE, or claim to.
- Write into `agents/archie/` anywhere except `inbox/`.
- Change an ARCHIE output. Those are ARCHIE's records.
- Treat an ARCHIE score as a fact about a seed. ARCHIE's scores are for the article idea,
  not the seed. If the cultivator scores on top, it says what for, per
  `claude/rules/07-what-to-report.md`.
