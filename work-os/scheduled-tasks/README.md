# work-os/scheduled-tasks: 28 cloud routines

Twenty-eight scheduled tasks run in the cloud under Venkat's claude.ai account (not local cron
jobs). Each one starts with zero context, so its prompt is self-contained: the shared blocks in
`_shared/` plus the task's own body. Created 2026-09-08 and 2026-09-09.

They come in two groups.

- **The seven original tasks**, one folder each, listed below. Created 2026-09-08 and 2026-09-09.
- **The 21 market-signal routines** in `market-signals/`: seven subjects times three cadences,
  built from shared parts rather than written one by one. Created 2026-09-09. That folder has
  its own README, and it is the one to read before touching any of them.

## The seven original tasks

| Task folder | Runs (Chicago) | Model | Routine id |
|---|---|---|---|
| `daily-briefing/` | every day, 6:00 AM | claude-sonnet-5 | `trig_01S8ur3pNcAQKykxxmV4qSRK` |
| `market-signal-brief/` | Mon to Fri, 7:00 AM | claude-opus-5 | `trig_01XTvLibJh81Fp5vJNcKqLKy` |
| `pharma-intelligence-watch/` | Wednesday, 7:00 AM | claude-opus-5 | `trig_018DJxJcy1So9ZYpZ8J7E9Xq` |
| `weekly-signal-synthesis/` | Friday, 3:00 PM | claude-opus-5 | `trig_01K5mefF9qoU9QuoD3k4Ca85` |
| `weekend-read/` | Saturday, 7:00 AM | claude-opus-5 | `trig_018UhmYVgb84FGsAqeXDbFQv` |
| `matching-roles-scan/` | Monday, 8:00 AM | claude-sonnet-5 | `trig_01BcJjy6weLhRYcwKFTPwgNS` |
| `all-market-signals/` | every day, 9:00 AM | claude-opus-5 | `trig_01UvA4mcdFnJwFx2LM1gQrMK` |

Each task folder holds `ROUTINE.md` (id, schedule, output, log), `prompt.md` (the task body),
`runs/` (one record per run that Alfred inspected), `outputs/` (copies of published briefs
pulled into the lab), and `build/` (the generated full prompt and the exact cloud body).
Routine pages: `https://claude.ai/code/routines/<routine id>`. All of them: https://claude.ai/code/routines.

One more routine, "Delivery and Network Check" (`trig_017HDCtC8z1NsBmuepRryTMG`), is a disabled
one-shot used to test channels. Re-enable and run it to re-test after a settings change.

## The 21 market-signal routines (`market-signals/`)

Seven subjects: the whole market, then one for each of Venkat's six Capability Pillars.
Three cadences each: a daily brief, a Wednesday check on the week so far, and a Friday
synthesis. Venkat asked for them in that order, starting at midnight Chicago time.

They run 5:00 to 7:00 universal time every day, then 7:30 to 9:30 on Wednesdays and again on
Fridays, twenty minutes apart. Dailies use claude-sonnet-5; the Wednesday and Friday routines
use claude-opus-5.

**Only the All Market brief sends a push.** The six pillar briefs publish their page silently.
Otherwise Venkat would get seven notifications in two hours, three times a week.

Everything about them lives in `market-signals/README.md`: the schedule table, the title
prefixes each run reads its memory by, how the prompts are assembled, and `verify.sh`, which
proves each live routine still matches its file. Last full pass: 2026-09-09, all 21 matched.

**Open question for Venkat.** `all-market-signals/` (the seventh original task, daily at 9:00 AM
Chicago) and `market-signals/00-all-market-signals/daily/` (daily at midnight Chicago) cover the
same subject with two different structures, and both send a push. That is two whole-market
briefs and two notifications a day. They share no wording, so this is a real choice, not a
copy-paste mistake. Flagged 2026-09-09. Nothing disabled without his word.

## How a run delivers (what actually works, tested 2026-09-08)

1. **Memory.** The run lists the account's published Artifact pages, reads the recent ones with
   its own title prefix, and uses them to avoid repeats and say what changed.
2. **The brief.** The run writes the brief as a simple web page and publishes it as a private
   Artifact page titled `<Task> YYYY-MM-DD` (for example `Daily Briefing 2026-09-09`). The
   gallery is https://claude.ai/code/artifacts. Nobody else can see them.
3. **The ping.** One mobile push in the Claude app: the title, the top lines, and the page link.
4. **The session.** The full brief is also printed in the run, at https://claude.ai/code/routines.

Pulling copies into the lab: from any Claude Code session in the lab, list the artifacts, read
the ones with a task's title prefix, and save each as `<task>/outputs/YYYY-MM-DD.md` (plain
text, headings kept). This is a Claude action, not a script, because only a Claude session can
read artifacts. Nothing on the laptop runs on its own.

## Known blockers (found by running all six on 2026-09-08)

- **Web reading is blocked in the cloud.** Both cloud environments refuse to open web pages
  ("organization policy" on the egress proxy). Web search works, so the runs see titles and
  snippets, not articles, postings, or filings. Effect: the Daily Briefing, Market Signal Brief,
  Weekly Synthesis, and Pharma Watch run in a degraded mode and label every claim as unverified
  at the source. The Weekend Read and the Matching Roles Scan cannot do their job at all and
  say so instead of faking it. **Fix needs Venkat:** the network access setting on the cloud
  environment used by the routines (the "Default" environment, id
  `env_011CUK7ovEXytcue7Dpm4mu5`) at claude.ai/code, under environments. Then re-enable and run
  the check routine to confirm.
- **Google Drive is share, trash, and rename only inside a routine.** No search, read, or
  create, whatever the routine's tool allowlist says. So Drive is not used. The folder
  structure created in Drive on 2026-09-08 (see `_shared/drive-folders.md`) is reserved and
  empty. If Drive ever exposes create and search in routines, delivery can move there.
- **The condensed run log truncates long text.** Full briefs are only in the session page and
  the artifact. That is why artifacts are the delivery, not the log.

## Design decisions, and why

- **Model choice.** The five analysis tasks run on claude-opus-5; the two lighter ones on
  claude-sonnet-5. Venkat said "that's fine" on 2026-09-08. One line in `assemble.sh` changes it.
- **Market Signal Brief is Monday to Friday.** Accepted by Venkat on 2026-09-08. Seven days
  would be cron `0 12 * * *`.
- **Cron is universal time.** Chicago is UTC-5 until early November, then UTC-6. Every task
  will fire one hour earlier on the clock after the change unless the crons move by one hour.
- **Context lives in the prompt, not in a repo.** The lab has no git remote.
  `_shared/about-venkat.md` and `_shared/market-lens.md` carry the minimum: positioning, the six
  Capability Pillars, hypotheses, intellectual territories, the audience canon (ICP v3,
  2026-09-08). No client names anywhere. When those change, these files change, then the
  routines are updated.
- **One push per run, never for failures.** The first test runs pushed about tool failures
  and one check run pushed a placeholder by mistake. The delivery block now forbids both.
- **Length.** The first Market Signal Brief and Weekly Synthesis ran eleven to twelve minutes
  and produced about 40,000 characters each. Watch the first week; tighten if it stays long.

## Shared parts (`_shared/`)

| File | In which prompts | What it is |
|---|---|---|
| `about-venkat.md` | all seven | Who he is, the six Capability Pillars, how he thinks |
| `writing-rules.md` | all seven | The 10th-grade rule, no em dashes, never invent, never name a client |
| `network-limits.md` | all seven | What to do when the cloud blocks a page: say it once, label snippets, never fake |
| `delivery.md` | six (not pharma watch, which carries its own) | Read recent artifacts first, publish one page, one push |
| `market-lens.md` | market brief, weekly synthesis, all market signals | Positioning, buyers, hypotheses, territories, the qualification gate |
| `signal-structure.md` | market brief, weekly synthesis | The exact SIGNAL / NON-OBVIOUS / VALUE / DECISION block |
| `drive-folders.md` | none | The reserved Drive folders and their ids |

`assemble.sh` builds every task's `build/` from these parts. Needs `jq`. Safe to rerun.

## To change a task

1. Edit the task's `prompt.md`, or a file in `_shared/` if the change is shared.
2. Run `./assemble.sh`. Read the task's `build/full-prompt.md`.
3. Update the routine with the RemoteTrigger tool (`action: update`, the task's `trigger_id`,
   `body` from its `build/routine-body.json`), or paste the prompt on the routine page. The
   auto-mode permission classifier sometimes blocks an update on the first try; a second try
   has worked every time so far.
4. Add a dated line to the task's `ROUTINE.md` log.

The tool cannot delete a routine. Disable or delete at https://claude.ai/code/routines.

## Log

- 2026-09-08: six routines created by Alfred at Venkat's request. First home was
  `os-factory/work/signals/prompts/routines/`; moved here the same day on Venkat's word. Old
  folder archived at `os-factory/work/signals/prompts/_archive/routines--moved-to-work-os-2026-09-08/`.
- 2026-09-08: all six run once at Venkat's request ("make sure they are working"). Records in
  each `runs/`. Found the two blockers above. Delivery moved from Google Drive to Artifact
  pages plus one push, with a network-limits block added to every prompt. All six routines
  updated. Daily Briefing re-run under the new delivery: it published a page, sent one push, and
  the page was pulled into `daily-briefing/outputs/`. The delivery works.
- 2026-09-09: seventh routine added, "All Market Signals" (`all-market-signals/`), daily at 9:00 AM
  Chicago on claude-opus-5. Venkat supplied the structure: exactly five signals a day, each with
  eight fixed parts, plus a four-part synthesis. It overlaps the Market Signal Brief on subject
  but not on shape, and it reads that brief at the start of every run so it can say what is new.
  Flagged the overlap to Venkat the same day. Run once immediately; record in its `runs/`.
- 2026-09-09: 21 market-signal routines created in `market-signals/`, from 21 prompts Venkat
  supplied, organised by pillar. Built from shared parts, not written one at a time. Created in
  the order he asked for: the seven dailies, then the seven Wednesday checks, then the seven
  Friday syntheses. Every live prompt was then compared to its build file by checksum. Six
  pillar dailies differed by one blank line, caused by a formatting bug in the market-signals
  `build.sh`; the bug was fixed, all eighteen pillar prompts rebuilt, and the six routines
  updated. Final pass: all 21 match. Details and the check script are in
  `market-signals/README.md`.
- 2026-09-09: run volume is now 75 a week. The 21 market-signal routines produce 63 (49 daily,
  7 Wednesday, 7 Friday) and the seven original tasks produce 12. Raised with Venkat with
  options for thinning it. Nothing cut.
