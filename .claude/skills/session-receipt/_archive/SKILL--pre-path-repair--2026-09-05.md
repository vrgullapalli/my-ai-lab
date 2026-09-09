---
name: session-receipt
description: Write the end-of-session receipt and persist canonical state before context is lost. Use when a session is ending, when asked to "wrap up" or "close out", or immediately after a meaningful unit of work completes mid-session. Delta-driven (D-137): writes a dated receipt when durable state changed, updates portfolio/NOW.md when the restart point moved, and touches other files only when a new fact belongs there. Zero writes is a valid close.
---

# Session Receipt

## Purpose
Nothing decided, changed, or committed in a session may exist only in the chat
context. This skill converts session context into durable state so the next session
can restart from files, not memory.

## Steps
**Delta-driven (D-137, 2026-08-21).** Facts land in their one home when they
happen. At close, each step below runs only if its trigger fired this
session; otherwise say "none" and move on. Zero writes is a valid close. If
nothing durable changed, say "no durable change" in the final message and
write no receipt.

1. **Extract from the session:** decisions made; artifacts created or changed;
   commitments and follow-ups; corrections or preferences learned; state
   transitions; what became externally visible; open questions.
2. **Verify before recording:** for every artifact claimed, confirm the file exists
   at the stated path; for every "published/sent" claim, confirm a receipt. Anything
   unconfirmed is recorded as **unverified**, not as fact.
3. **Update `portfolio/open-loops.md`** — *trigger: a new commitment, blocker,
   or pending decision exists, or a loop closed with evidence.* Append it; mark
   closed loops closed with their evidence. One loop per fact; never several.
4. **Update the touched project's card** (`portfolio/projects/`) — *trigger:
   that project's stopped-at or next step changed.* Last worked, stopped-at,
   and the prepared next step.
5. **Update `portfolio/NOW.md`** — *trigger: the restart point moved (primary
   item, next action, or blocker).* Otherwise untouched, including the date
   line.
6. **Write the receipt** to
   `traces/receipts/YYYY-MM-DD-HHMM-<slug>-<id>.md` — *trigger: durable
   state changed (a file he will rely on was created or edited, a decision
   was recorded, a commitment was made).* Use the template below; keep it
   compact; point to facts, do not retell them. Record the model/version
   that ran the session (D-010). Naming and collision rules (stabilization,
   2026-08-24 — permanent safety behavior):
   - `<slug>` is 2-5 plain words for the session; `<id>` is 4 random
     hex characters minted at write time (e.g. `openssl rand -hex 2`), so
     two sessions closing in the same minute never share a target.
   - **Before writing, check the target path. If it already exists, do not
     overwrite it** — mint a new `<id>` and, in the receipt and the final
     session message, say plainly that a collision was hit and refused.
     A refusal is always visible, never silent.
   - Never rewrite or replace an existing receipt for any reason; a
     correction is a new dated receipt that names the one it corrects.
7. If any decision made this session touches an entry in `DECISIONS.md`, do not edit
   that file silently — surface it as a proposed supersession for Venkat.
8. **Feed the case log** — *trigger: a real before/after with a number, or a
   fix.* Append one line to `traces/case-log.md` with the receipt pointer.
   Only things that actually happened.
9. **Propose, never promote (DONE.md §3)** — *trigger: a correction from
   Venkat this session.* From the session's corrections, propose
   (a) TASTE.md entries (with the quote, date, and signal label) and (b) memory
   promotions — anything worth keeping long-term or turning into a reusable
   how-I-did-it recipe, landing per `memory/README.md` (how-to recipes get a
   last-used/still-worked stamp). Venkat approves; nothing becomes permanent
   silently.
10. **Run the `seed-capture` skill** — *trigger: Venkat asked for seeds, or a
   candidate was marked during the work ("this is a seed").* No unconditional
   sweep. When it runs, it triages the marked or requested moments against
   Venkat's threshold, writes survivors to `/Users/venkatgullapalli/Documents/my-ai-lab-v2/engagement-os/seedbank/session/` under the
   fixed conventions, and asks the label question. Zero seeds is a valid
   outcome. D-137 (2026-08-21) amends the 2026-08-14 standing consent, which
   had chained a full sweep to every close.

## Receipt template
```
# Session Receipt — <date time>
Model: <exact model/version>
Decisions made:            (or "none")
Artifacts created/changed: (verified paths; unverified items labeled)
Commitments & follow-ups:  (appended to open-loops)
Corrections learned:       (appended to PROFILE.md corrections log if behavioral)
Externally visible:        (with receipts, or "nothing")
Labels coined:             (new labels + one sentence each, or "none")
Seeds captured:            (IDs with one-line claims, or "not run" / "none")
Open questions:
Next session starts with:  (one concrete action)
```

## Rules
- Append, never overwrite history; receipts are immutable once written.
- Run this *before* ending the session, not as an afterthought — if the session is
  interrupted, a partial receipt beats none.
- No secrets, tokens, or restricted client content in receipts.
- Memory hygiene: one lesson, one home — update an existing entry rather than
  duplicating it; propose deleting entries proven wrong.
