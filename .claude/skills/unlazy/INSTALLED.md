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
