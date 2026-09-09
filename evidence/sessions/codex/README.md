# Session transcripts — Codex and Claude Code

Built under `work/plans/codex-session-sync/codex-session-sync--integration--sync-job--v1--2026-08-20-1630.md`
(approved by Venkat 2026-08-20). Rendered by `tools/codex-session-sync.py`.

## What is here

- `codex-sessions/rollout-<start>-<thread-id>.md` — one file per Codex thread, same
  filename stem as Codex's own rollout file. Archived threads say `archived: yes`.
- `claude-sessions/<session-id>.md` — one file per Claude Code session for this repo.
- `../SYNC-LOG.md` — one line per sync run.

## What a file holds, and does not

- **Holds:** Venkat's turns and the assistant's replies, in order, **each under a
  stable anchor that is the source's own message id** (Codex `msg_…`, Claude record
  `uuid`) — cite as `<file>#<id>`; the anchor survives refreshes, line numbers do
  not (his ruling, 2026-08-20). Slash commands, tool calls, and web searches as
  **name-only** markers; reasoning or thinking whenever
  the source has readable text (his ruling, 2026-08-20). Today's Codex threads encrypt
  it and Claude Code keeps only a signature, but older Codex threads carry summaries
  (the archived 2025-10-27 thread renders 62). Each header counts what it found.
- **Never holds:** tool inputs (his ruling, 2026-08-20 — not part of the
  conversation, can carry sensitive material), tool outputs or tool results (hard
  rule 6 — they carry whole files), system-reminder injections, skill bodies injected after a slash command,
  anything matching the secret patterns (a hit skips the file and is logged).
- **Source of record** is the raw file outside the repo, named in every header. A
  render is a copy; the header's `Source mtime` is how the sync knows to refresh it.
- An open thread is refreshed in place at the same path, so citations do not move.
  Cite by anchor, not by line.

## How to refresh by hand

```
python3 tools/codex-session-sync.py                 # everything changed since last run
python3 tools/codex-session-sync.py --once <id>     # one thread or session
python3 tools/codex-session-sync.py --source codex  # one tool only
```

The sync **never commits**. Venkat commits, with purpose (his ruling, 2026-08-20).

## Boundaries

- Codex is a read-only advisor (D-128). Nothing in a Codex transcript is an approval;
  older conversations are context, not approval (A-LIVE-076).
- Subagent transcripts (Claude Code writes them beside each session, ~380 files today)
  are **not** rendered — open question for Venkat.
