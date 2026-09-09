# work-os/scheduled-tasks: the six cloud routines

Six scheduled tasks run in the cloud under Venkat's claude.ai account (not local cron jobs).
Each one starts with zero context, so its prompt is self-contained: the shared blocks in
`_shared/` plus the task's own `prompt.md`. Created 2026-09-08, tested the same day.

## The six

| Task folder | Runs (Chicago) | Model | Routine id |
|---|---|---|---|
| `daily-briefing/` | every day, 6:00 AM | claude-sonnet-5 | `trig_01S8ur3pNcAQKykxxmV4qSRK` |
| `market-signal-brief/` | Mon to Fri, 7:00 AM | claude-opus-5 | `trig_01XTvLibJh81Fp5vJNcKqLKy` |
| `pharma-intelligence-watch/` | Wednesday, 7:00 AM | claude-opus-5 | `trig_018DJxJcy1So9ZYpZ8J7E9Xq` |
| `weekly-signal-synthesis/` | Friday, 3:00 PM | claude-opus-5 | `trig_01K5mefF9qoU9QuoD3k4Ca85` |
| `weekend-read/` | Saturday, 7:00 AM | claude-opus-5 | `trig_018UhmYVgb84FGsAqeXDbFQv` |
| `matching-roles-scan/` | Monday, 8:00 AM | claude-sonnet-5 | `trig_01BcJjy6weLhRYcwKFTPwgNS` |

Each task folder holds `ROUTINE.md` (id, schedule, output, log), `prompt.md` (the task body),
`runs/` (one record per run that Alfred inspected), `outputs/` (copies of published briefs
pulled into the lab), and `build/` (the generated full prompt and the exact cloud body).
Routine pages: `https://claude.ai/code/routines/<routine id>`. All of them: https://claude.ai/code/routines.

A seventh routine, "Delivery and Network Check" (`trig_017HDCtC8z1NsBmuepRryTMG`), is a disabled
one-shot used to test channels. Re-enable and run it to re-test after a settings change.

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

- **Model choice.** The four analysis tasks run on claude-opus-5; the two lighter ones on
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
| `about-venkat.md` | all six | Who he is, the six Capability Pillars, how he thinks |
| `writing-rules.md` | all six | The 10th-grade rule, no em dashes, never invent, never name a client |
| `network-limits.md` | all six | What to do when the cloud blocks a page: say it once, label snippets, never fake |
| `delivery.md` | five (not pharma watch, which carries its own) | Read recent artifacts first, publish one page, one push |
| `market-lens.md` | market brief, weekly synthesis | Positioning, buyers, hypotheses, territories, the qualification gate |
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
