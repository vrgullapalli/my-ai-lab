# Installed 2026-09-10

Source: https://github.com/Leonxlnx/unlazy, commit `16671491f6679ad9378f52604d3bc2415b4120c7`
(2026-09-03, "fix: bind gate evidence and harden Windows identity"). MIT license, kept in `LICENSE`.

## Why it was replaced

The copy that was here had its instructions stripped: `SKILL.md` was a title and a
description and nothing else, so the skill triggered and did nothing. The rest of it was an
older snapshot of the same 2.1.0 line. That copy is in the warehouse at
`~/Documents/_warehouse/skills-archived-2026-09-10/unlazy--old-copy-with-instructions-stripped/`.

## What changed from upstream

- `SKILL.md`: a new "In this lab" section at the top; the description rewritten for Claude
  Code and Venkat's own phrases; `$unlazy` (Codex) removed; the Stop hook section says it is
  installed rather than offered. Everything else is upstream text.
- `scripts/stop-hook.mjs` (2026-09-10, Venkat: "3. yes"): the hook reads the ledger from
  `CLAUDE_PROJECT_DIR`, the project root Claude Code gives every hook, and falls back to the
  payload's `cwd` only when that is unset. Upstream uses `cwd`, which follows the shell. A `cd`
  into `work-os/upskill-advisor/` made it parse Telegraph's release gates (`gates/README.md`,
  `gate-0.md` to `gate-5.md`) as ledgers and block the stop with "ledger contains zero live
  gates". Not chosen: skipping ledgers with no gates, because then emptying a ledger would
  release the stop. Proof: the block reproduced without the fix and cleared with it; a real
  root ledger still blocked with a decoy `gates/` folder underneath; all seven suites pass
  (34, 27, 51, 29, 8, 24, 15), run with `CLAUDE_PROJECT_DIR` unset.
- `scripts/lib/gates.mjs` and `scripts/stop-hook.mjs` (2026-09-15, Venkat's goal: "one Claude session
  cannot be blocked by another session's active gate scope"): when the caller names a session, the
  resolver only returns a scope whose `session` file matches that session. Upstream handed a lone
  scope under `.unlazy/` to every session, so a session that opened no ledger was blocked by the
  `context-check-repair` ledger another session had left open. The gate-check CLI passes no session,
  so `--status`, `--bind`, and `--log` still resolve a lone scope without `--scope`. Explicit `--scope`
  on the hook, the `sessionId` payload fallback, a root `GATES.md`, and dispatch state are unchanged.
  The cost: a scope must be bound (`--bind`) or the hook holds nobody to it; `SKILL.md` now says so.
  Proof: a planted two-session case blocked the unrelated session before the fix and let it stop after,
  while the bound owner stayed blocked; three new tests in `tests/run-tests.mjs`; all seven suites
  pass (37, 27, 51, 24, 29, 8, 15), run with `CLAUDE_PROJECT_DIR` unset.
- Not copied: `.git/`, `.github/` (upstream CI), and `agents/openai.yaml` (Codex interface
  settings). Nothing else was left out.

## What was checked before it went in

- **No network access** anywhere in `scripts/`. The only process it starts is the shell that
  runs a gate's `CHECK:` line, which is its whole job, and only after explicit approval.
- **Its own tests, run with Node 24.21.0:** all seven suites pass (34, 27, 51, 24, 29, 8, 15)
  once `TMPDIR` points at a writable folder. Under the Bash sandbox's default temp folder, the
  tests that execute checks fail. That is the sandbox, not the code.
- **A smoke test end to end:** lint, status, approve, run, and reverify on a one-gate ledger.
  All met, with evidence written into the ledger.

## What else was installed for it

- Node.js 24.21.0 LTS at `~/.local/node-v24.21.0-darwin-arm64`, linked as `~/.local/node`,
  downloaded from nodejs.org with its SHA-256 checked against the published list. On the login
  PATH through one line added to `~/.zprofile`. No admin rights used.
- The approval store `~/.unlazy/approved`, owner-only.
- The Stop hook, in `.claude/settings.local.json`.
- A trigger hook, `.claude/hooks/unlazy-trigger.py`, in `.claude/settings.json`.
- A binding hook, `.claude/hooks/unlazy-bind.py`, in `.claude/settings.json` (PostToolUse on
  Write, Edit, MultiEdit, NotebookEdit, and Bash; added 2026-09-15). When a tool call writes the
  scope's ledger, `.unlazy/<scope>/GATES.md` or `.unlazy/<scope>/gates/<name>.md`, and the scope has
  no `session` file, it writes the payload's `session_id`
  there, the same file `gate-check.mjs --bind` writes by hand. It never overwrites a binding, never
  binds on a read, prints nothing, and never blocks. For shell commands it asks `bash_targets` in
  `root-lock.py` which paths the command writes, so the lab keeps one parser for that question.
  Any other write inside the scope (plan, dispatch state, status log, the folder) binds nothing;
  tightened the same day at Venkat's word, "working inside a scope does not prove ownership".
  Tests: `.claude/hooks/tests/unlazy-bind-tests.py` (22 cases; breaking the rule four ways on a
  scratch copy failed 5, 2, 3, and 8 of them). Proof: a planted case fed the hook a
  Write payload, the binding file held the writer's id, the writer was blocked and an unrelated
  session stopped; a second scope made by shell bound to its own session; a write from another
  session did not move the binding; `--bind` did. Hooks are read at session start, so it fires
  from the next session after install.
