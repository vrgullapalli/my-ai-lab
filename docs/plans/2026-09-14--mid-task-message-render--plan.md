# Plan: render the messages Venkat sends while Claude is mid-task (F-20260913-0602-2)

Source read: `~/Documents/_warehouse/session-sync-mid-task-change--reverted-2026-09-13/` (NOTE.md, session-sync.patch, session_sync_tests.py, the changed tool). Nothing applied.

## The record that holds them
Claude Code does not store a mid-task message as a `user` record. It stores an `attachment` record whose `attachment.type` is `queued_command`. The reader today keeps only `user` and `assistant` records, so every one of these is dropped. One real line from a raw session under `~/.claude/projects/`, trimmed (no secret-like text was in it):

    {"type":"attachment","uuid":"897f517c-0b18-44c7-b389-a9cbebfd2feb","timestamp":"2026-09-12T03:59:41.829Z","attachment":{"type":"queued_command","prompt":[{"type":"text","text":"is the ledger working?"}],"source_uuid":"65a2256a-498c-4a63-868f-7b5df17129f3","commandMode":"prompt","origin":{"kind":"human"}}, ...}

Count today, by a script: 253 of his messages across 21 sessions (it was 249 across 18 on 2026-09-13; the gap keeps growing).

## What the patch changes (one file, four hunks, applies clean to today's file)
- Reads `queued_command` attachments. His own messages render as a normal quoted turn labeled "Venkat, mid-task", under the record's own uuid anchor, in order.
- Same message recorded twice: skipped on a repeat `source_uuid`.
- `commandMode` of `task-notification` (a background job finished) becomes a marker with none of its text. `origin.kind` of `peer` (another session) renders as "Message from another session (name)".
- Editor-only notices and the usual skipped prefixes are dropped the same way as normal turns.
- Header counts change: "N Venkat turns (M sent mid-task)"; the Usage line gains one field, `venkat_midtask`.

## How it is tested
The warehouse test builds one fake session with eight planted records and renders it: shown once, labeled, anchored, deduped, notification masked, peer labeled, editor notice dropped, order kept, counts right. Ten checks. Prove-it-can-fail: run the same test against today's tool and require failures before applying.

## What could break
- Transcripts already rendered: 21 files change on re-render; anchors of existing turns do not move (they are uuids), so old citations still hold. Diff a sample before and after.
- USAGE.jsonl: rows gain `venkat_midtask` and `venkat_turns` rises for 21 sessions. One other script reads the rows: `.claude/skills/session-capture/scripts/capture-report.py`. It reads fields by name, so the new field is harmless and only its printed turn count changes.
- SessionEnd hook: same code path (`--hook` calls `render_claude`), so it picks the change up with no settings edit. Its 60 second timeout is unchanged; the hook renders one file.
- Secret mask: mid-task text goes through the same `SECRET.subn` in `sync_one`, so the mask covers it.
- Test file name clash: the warehouse tests are named `session_sync_tests.py`, the same as the mask tests written 2026-09-14. Merge the ten cases into the existing file; do not copy over it.

## Commands, on his word (copy, verify, no deletes)
    cd ~/Documents/my-ai-lab
    git apply ~/Documents/_warehouse/session-sync-mid-task-change--reverted-2026-09-13/session-sync.patch
    python3 .claude/agents/alfred/sensors/tests/session_sync_tests.py        # after the merge of the ten cases
    python3 .claude/agents/alfred/sensors/session-sync.py --source claude --force --tag mid-task-rerender
Then read the last line of `evidence/sessions/SYNC-LOG.md`, spot-check three of the 21 transcripts, and commit only at his word.
