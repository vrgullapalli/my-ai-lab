# The cultivator

Tends the 680 ideas already in the lab. Reads the index first, finds ideas circling the
same question, flags ones that have gone quiet or have no links, says the one action
that would move each forward, and proposes what should change. Proposes only. He decides.

## What it answers to

| Say this | What you get |
|---|---|
| **cultivator** · tend the seedbank · review the seeds | The summary view |
| **what is close to ready** · what connects to what | Facts per idea, the one action for each, a named score if it helps |
| **what has gone quiet** · retire some of these | Every retire candidate at once, for your yes or no |
| **here is a new idea** | It decides new-or-evidence, asks what caught your eye, hands to `seed-capture` |
| **research this** · what did ARCHIE find | Drops the topic in ARCHIE's inbox for you to run; afterwards, marks the seeds ARCHIE cited as used and proposes the links |

## Where things are

- The ideas: `work-os/brand-os/engagement-os/seedbank/` — 191 session, 459 written, 30 spoken
- The tool: this folder. Identity in `CLAUDE.md`, standing rules in `claude/rules/`, one file per job in `claude/skills/`
- Its index: `seedbank/INDEX.md` — does not exist yet. The first time you call it, it will say so and offer to build it. That means reading all 680 files once; say yes when you have time for it.

## Where an idea stands

Plain words: **new · linked · used · gone quiet · unlinked · retired.**
Everything in `session/` says `seedling` today because nothing has ever moved. That is
the starting line, not a problem.

## Every answer has two parts

The answer to what you asked, then a few lines on what it noticed in passing. If you
keep ignoring the second part, it gets shorter.

## What it never does

Decide. Delete. Capture new ideas (that is `seed-capture`). Speak first. Change your
words. Rename anything. Write outside the seedbank folder.

## Origin

Adapted 2026-09-09 from a downloaded tool, then stripped of everything that was the
tool's rather than ours. The unchanged original is at
`.claude/agents/_archive/cultivator--exact-clone-of-desktop-original-2026-09-09/`.
