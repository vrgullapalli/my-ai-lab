---
name: session-receipt
description: Manual button for the session receipt. Captures the transcript first, then runs Alfred's close routine (alfred-close), which replaced the old session-receipt skill on 2026-09-10, so the receipt can cite the rendered transcript by anchor. Use when Venkat types /session-receipt or says write the receipt, session receipt, receipt this session.
---

# Session receipt

> **Base directory:** the lab root, `/Users/venkatgullapalli/Documents/my-ai-lab/`.
> Added 2026-09-10 at Venkat's word ("session-receipt manually through a '/' hook"). The
> old skill of this name was parked on 2026-09-08 (it read folders that no longer existed)
> and sits in `~/Documents/_warehouse/skills-archived-2026-09-10/session-receipt/`. The
> receipt logic lives once, in `alfred-close`. This skill does not copy it.

**How it beats the old receipt.** The old one wrote from memory of the chat. This one renders
the transcript first, so every decision and correction in the receipt can point at a line
that exists on disk: `evidence/sessions/claude/<session>.md#<uuid>`. Anchors survive
re-renders; line numbers do not.

## Steps

1. **Capture this session.** Run `session-capture` for the current session id (it is in the
   context the SessionStart hook gave this session):

   ```bash
   python3 .claude/agents/alfred/sensors/session-sync.py --once <session id>
   python3 .claude/skills/session-capture/scripts/capture-report.py --session <session id>
   ```

   Note the render path and the skills and agents the report lists. The render is partial
   while the session is open; that is expected.

2. **Close.** Invoke `alfred-close` and follow it exactly: measure what changed, write the
   receipt to `evidence/receipts/`, record follow-ups, scan for seeds, once a day write the
   day review. Zero writes is a valid close.

3. **Anchor the receipt.** For each decision and each correction the receipt records, add
   the transcript anchor from step 1 after the quote, in the form
   `evidence/sessions/claude/<session>.md#<uuid>`. If the anchor cannot be found, say
   `(anchor not found)` rather than guessing one. Under the receipt's source line, add the
   skills and agents the report listed; if the report says none and the session did real
   work, say so, since that is a missed-skill signal.

4. **Report to him** in three lines: receipt path, transcript path, and the one next action
   `alfred-close` prepared.
