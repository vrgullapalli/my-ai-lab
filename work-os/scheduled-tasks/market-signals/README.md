# Market Signals — 21 cloud routines

Seven subjects. Three cadences each. Created 2026-09-09.

This folder is the source of truth for the prompts. The cloud routines are copies.
Change the parts here, run the two build scripts, update the routine, then run
`verify.sh` to prove the live routine matches the file.

## The seven subjects

One is the whole market. Six are Venkat's Capability Pillars, one each.

| Folder | Subject | Question it asks |
|---|---|---|
| `00-all-market-signals/` | All Market | What changed across applied AI, customer data, and commercial pharma? |
| `01-foundation/` | Foundation | Can the organization reliably supply, connect, operate, secure, and scale the data and technology? |
| `02-meaning-and-context/` | Meaning and Context | Do people and systems mean the same thing by the same words? |
| `03-use-case/` | Use Case | Which specific work, decision, or outcome actually gets better, and for whom? |
| `04-operating-model/` | Operating Model | Who owns it, who decides, where does human judgment sit? |
| `05-trust-and-control/` | Trust and Control | What has it earned the right to do, and what happens when it is wrong? |
| `06-repeatability-and-scale/` | Repeatability and Scale | What can travel, and what must stay local? |

## The three cadences

- **Daily** (`daily/`). Up to five signals. Runs seven days a week. Model: claude-sonnet-5.
- **Midweek** (`wednesday/`). Up to three emerging patterns from the week so far. Wednesdays. Model: claude-opus-5.
- **Weekly** (`friday/`). Three to five weekly signals, belief updates, three moves. Fridays. Model: claude-opus-5.

The Midweek check does not repeat the dailies and does not do the Friday work early.
The Weekly synthesis uses the dailies as evidence, not as sections to summarize.

## The schedule

All times are UTC, which is what the cloud uses. Chicago is five hours behind
until early November, then six. So a 5:00 UTC run lands at midnight Chicago time.

Venkat asked for the market signals to start at midnight Chicago and run in order:
dailies first, then the Wednesday checks, then the Friday syntheses.

| Time (UTC) | Daily, every day | Wednesday | Friday |
|---|---|---|---|
| 5:00 | All Market | | |
| 5:20 | Foundation | | |
| 5:40 | Meaning and Context | | |
| 6:00 | Use Case | | |
| 6:20 | Operating Model | | |
| 6:40 | Trust and Control | | |
| 7:00 | Repeatability and Scale | | |
| 7:30 | | All Market | All Market |
| 7:50 | | Foundation | Foundation |
| 8:10 | | Meaning and Context | Meaning and Context |
| 8:30 | | Use Case | Use Case |
| 8:50 | | Operating Model | Operating Model |
| 9:10 | | Trust and Control | Trust and Control |
| 9:30 | | Repeatability and Scale | Repeatability and Scale |

Twenty minutes apart so a slow run does not collide with the next one.

## How a run delivers

Same pattern as the six original scheduled tasks. It is the only one that works
in the cloud today. See `../README.md` for why Google Drive and web page reading
do not.

1. Read memory. List the artifacts, then read the recent ones with a matching title prefix.
2. Write the brief to `/home/user/brief.html`.
3. Publish it as a private Artifact page titled `<Prefix> YYYY-MM-DD`.
4. Print the whole brief in the run, so it can be read there too.

**Only one push notification per batch.** The All Market brief sends it. The six
pillar briefs stay silent and say so in their own prompts. Without this rule
Venkat would get seven buzzes in two hours, three times a week.

## Title prefixes

Each routine reads its own history back by title. The prefixes must stay exactly
as written or memory breaks.

| Subject | Daily | Midweek | Weekly | Icon |
|---|---|---|---|---|
| All Market | All Signals | All Midweek | All Weekly | 🌐 |
| Foundation | Foundation Signals | Foundation Midweek | Foundation Weekly | 🧱 |
| Meaning and Context | Meaning Signals | Meaning Midweek | Meaning Weekly | 🗺️ |
| Use Case | Use Case Signals | Use Case Midweek | Use Case Weekly | 🛠️ |
| Operating Model | Operating Model Signals | Operating Model Midweek | Operating Model Weekly | ⚙️ |
| Trust and Control | Trust Signals | Trust Midweek | Trust Weekly | 🛡️ |
| Repeatability and Scale | Scale Signals | Scale Midweek | Scale Weekly | 🔁 |

## How the prompts are built

Nothing is written twice. A prompt is assembled from parts.

```
_schema/daily.md          the daily structure, shared by all seven subjects
_schema/wednesday.md      the midweek structure
_schema/friday.md         the weekly structure
_schema/defaults.txt      empty values for every optional slot
_schema/fill.awk          replaces {{SLOT}} with the ::SLOT:: text from a deltas file

<subject>/<cadence>/deltas.txt    only what makes this subject different
<subject>/<cadence>/prompt.md     built: header + cadence schema, slots filled
<subject>/<cadence>/build/        built: the full prompt and the routine body
```

`00-all-market-signals/` has no `deltas.txt`. Its three prompts are written by hand
because the whole-market brief is not a variation on a pillar. `build.sh` skips it.

Two scripts, run in this order:

- **`build.sh`** turns `deltas.txt` into `prompt.md` for the eighteen pillar prompts.
- **`assemble.sh`** reads `routines.tsv` and writes `build/full-prompt.md` and
  `build/routine-body.json` for all twenty-one, adding the shared blocks from
  `../_shared/` (about Venkat, the current lens, writing rules, network limits, delivery).

Running `assemble.sh` alone does not rebuild `prompt.md`. Run both.

## routines.tsv

One line per routine, pipe separated. The columns are:

`folder | cadence | routine name | title prefix | daily prefix | midweek prefix | icon | cron | model | uuid | trigger id`

The daily and midweek prefixes are there so a Midweek or Weekly run knows which
earlier briefs to read.

## make-records.sh

Regenerates each subject folder's `ROUTINES.md` from `routines.tsv`: the three routine names,
crons, models, page titles, and trigger ids. It also creates the `runs/` and `outputs/`
folders each cadence needs. Rerun it after any change to `routines.tsv`. Never hand-edit a
`ROUTINES.md`; the next run overwrites it.

## verify.sh

Scripts decide what is true. This one proves the live routine and the file agree.

```
./verify.sh <folder of RemoteTrigger JSON responses>
```

It reads each saved create, update, or get response, pulls the prompt the server
actually stored, and compares it to `build/full-prompt.md` by checksum. It prints
`OK` or `DIFF` per routine, and shows the first ten lines of any difference.

Last full pass: **2026-09-09, all 21 OK.**

## To change a prompt

1. Edit the part that owns the text: `_shared/` for anything all routines share,
   `_schema/` for anything a whole cadence shares, `deltas.txt` for one subject.
2. Run `./build.sh` then `./assemble.sh`.
3. Update the routine with `RemoteTrigger` `update`, using the trigger id from
   `routines.tsv` and the content from `build/routine-body.json`.
4. Run `./verify.sh` and confirm `OK`.

Never edit `prompt.md` or anything under `build/` by hand. They are generated and
the next build will overwrite the change.

## Run volume

Twenty-one routines produce **63 runs a week**: 49 dailies, 7 midweek, 7 weekly.
The six original scheduled tasks add 12 more. That is 75 runs a week in total.

This is a lot. It is what Venkat asked for, and it is worth watching. If the
pillar briefs turn out to repeat one another, the cheapest cut is to move some
pillar dailies to every other day, or to drop the pillar dailies and keep the
Midweek and Weekly work. Neither change has been made.

## Log

- **2026-09-09** — Created all 21 routines. Verified every live prompt against
  its build file; all 21 match.
- **2026-09-09** — Fixed a formatting bug in `build.sh`: the pillar header ran
  straight into the cadence schema with no blank line between them. Rebuilt all
  eighteen pillar prompts and updated the six pillar daily routines so the live
  copies match the files again.
- **2026-09-09** — Added the trigger id column to `routines.tsv`. The version
  before that is in `_archive/`.
- **2026-09-09** — Added `verify.sh`.
