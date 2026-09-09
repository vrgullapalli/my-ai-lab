# Files and formats

## Where things are

The data lives in the seedbank, not in this folder.

```
work-os/brand-os/engagement-os/seedbank/
  session/       191 ideas. Files named A-LIVE-NNN-<slug>.md
  written/       459 ideas. Prefixes A-TOPIC-, A-SEED-, A-CHR-, A-ADR-, A-CDR-
                 plus four SUMMARY-*.md files that are ways in, not ideas
  spoken/        30 ideas, plus garden-state.md, a finished test from 2026-08-13
  missed.md      one row per idea he says should have been caught
  README.md      how the collection was built; what is unreliable in it
  INDEX.md       the cultivator's working index
  _archive/      superseded material, never deleted
```

## The real idea format

This is what the files actually look like. Do not add fields that are not here.

```markdown
# <The claim, written out as the title>
- ID: A-LIVE-001
- Source type: live session, typed by Venkat himself
- Source file: session transcript, August 14, 2026, midday
- Grade: none
- Archived: no
- Date: 2026-08-14
- Status: seedling
- Label: **explicit — he named it and defined it in the same message**
- Evidence label: provided
- Tension: <the unresolved pull inside the idea>

## The claim as stated
> his words, quoted
```

Written ideas carry `Series` and `Transferable` instead of `Label` and `Evidence label`.
Some carry `Conflicts with:` naming an idea they disagree with.

**Whose it is.** Session ideas carry an attribution class: **his · endorsed · other ·
system.** This is the most valuable field in the collection and the only one that says
which ideas he can actually claim. Never drop it, never guess it, never quietly turn
endorsed into his. Written ideas mostly lack it; chronicle ideas say on each file whether
the words are his — check that line before quoting one as his.

## Plain words for where an idea stands

| Say this | It means |
|---|---|
| new | Just captured. No links yet. |
| linked | Points at other ideas, or they point at it. |
| used | Something happened because of it. |
| gone quiet | Nothing has touched it in 30 days. |
| unlinked | Nothing connects to it and it connects to nothing. |
| retired | Set aside. Still there. Still findable. |

Everything in `session/` currently says `seedling`, because nothing has ever moved.
That is the starting condition, not an error. Do not mass-rename it. When an idea
changes state, write the plain word.

## What the cultivator may add to an idea file

- A `## History` section, appended, one dated line per change
- Link lines, saying which idea and why
- A status change, in the plain words above

Nothing else. His claim stays as he wrote it.

## INDEX.md

Both the cultivator's working memory and his view of the collection. Holds:

- Last updated, and the count checked the right way (680, not 685)
- How to read it: the plain-word statuses above
- Counts by status
- Ideas circling the same question, with why
- Ideas gone quiet, with dates
- Ideas with no links
- Retire candidates
- How he works: how often he adds, which themes grow, whether he answers questions,
  whether he acts on flags
