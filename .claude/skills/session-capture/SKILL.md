---
name: session-capture
description: Copies Claude Code and Codex sessions into the lab as readable transcripts under evidence/sessions/ by running Alfred's session-sync sensor by hand, then reports what the lab actually used (skills, agents, subagents), what was skipped and why, which renders are partial, and whether the timed job is alive. Use when Venkat says session capture, capture this session, capture the sessions, sync the transcripts, render the transcripts, which skills did I use, or types /session-capture. The SessionEnd hook and a launchd job run the same sync on their own; this is the manual button plus the report.
---

# Session capture

> **Base directory:** the lab root, `/Users/venkatgullapalli/Documents/my-ai-lab/`.
> Manual button added 2026-09-10 at Venkat's word ("id like to manually session-capture ...
> through a '/' hook"). The sync itself is Alfred's sensor
> `.claude/agents/alfred/sensors/session-sync.py`, re-homed the same day from the old
> `chief-of-staff/tools/codex-session-sync.py` (285 lines then, 458 now; every old function
> kept, seven added). The report script beside this file is new.

## What it is for

Two scripts decide what is true. This skill runs them and reads the result to Venkat. It
adds no judgment of its own about what happened in a session.

**How it beats the old capture.** The old job could only say "N rendered". This one also
answers, from the ledger the sync writes: which skills and agents the lab used and how often,
which sessions ran with no skill at all, which sessions were skipped for a secret-like string,
which older renders are partial, and whether the timed launchd job ran clean. All by script.

## What the sync writes, and never writes

- Writes only under `evidence/sessions/`: `claude/<session>.md`, `codex/<thread>.md`,
  `SYNC-LOG.md`, `USAGE.jsonl`. Never commits.
- Each render: Venkat's turns and the replies under stable anchors, tool calls as name-only
  markers, the skill name on every skill call, the agent type on every agent call, one line
  per subagent, one machine-readable usage line in the header.
- Never: tool inputs, tool results, system reminders, IDE notices, or anything matching the
  secret patterns. A source with a hit is skipped and named in the log, never written.

## Steps

1. **Sync.** Plain call renders every session that changed since its last render:

   ```bash
   python3 .claude/agents/alfred/sensors/session-sync.py
   ```

   Variants, only when he asked for one:

   ```bash
   python3 .claude/agents/alfred/sensors/session-sync.py --dry-run     # say what would render, write nothing
   python3 .claude/agents/alfred/sensors/session-sync.py --once <id>   # one session or thread, id substring
   python3 .claude/agents/alfred/sensors/session-sync.py --force       # re-render even if unchanged
   python3 .claude/agents/alfred/sensors/session-sync.py --usage       # rebuild USAGE.jsonl from the renders
   ```

   The current session is still open, so its render is partial until the window closes. The
   SessionEnd hook renders it again then.

2. **Report.** Run the report and read it to him in plain words, four short blocks:

   ```bash
   python3 .claude/skills/session-capture/scripts/capture-report.py            # last run + last 7 days
   python3 .claude/skills/session-capture/scripts/capture-report.py --days 30
   python3 .claude/skills/session-capture/scripts/capture-report.py --session <id>
   ```

   - **Last run:** rendered, refreshed, unchanged, skipped, and the note.
   - **Last N days:** turns, tool calls, subagents; skills and agents used with counts;
     sessions with three or more turns that used no skill or agent (worth a look: either the
     work needed none, or a skill was missed).
   - **Skipped, ever:** each source never written, with its reason.
   - **Timed job:** loaded or not, last exit code, last error line if any.

3. **Say what needs him, if anything.** Two known cases:
   - Timed job says `Operation not permitted`: macOS Full Disk Access is missing for the
     Python the job runs. He grants it in System Settings, Privacy and Security, Full Disk
     Access, for `/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app`.
   - A skipped source he wants rendered anyway: the secret pattern is in the sync script.
     He decides; this skill does not loosen it.

4. **If a script fails,** quote the error and stop. Do not patch either script from inside
   this skill.

## What this is not

- Not the receipt. That is `alfred-close`, also reachable as `/session-receipt`, which runs
  this skill first so the receipt can cite the rendered transcript.
- Not seed capture. That is `seed-capture`, which `alfred-close` runs every time.
