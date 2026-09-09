# Agents — reserved

Empty by design. No agent exists in this repository.

> **Authority to approve rests in `governance/AUTHORITY.md` Part 10** — approved by DR-0001B
> on 2026-08-19. This file implements the per-mechanism criteria; it does not originate the
> authority. No capability may grant an agent any authority reserved to the owner under Part 5,
> regardless of how its definition is written. Approval is recorded in `governance/decisions/`
> as `DR-NNNN` — capability promotion is repository-wide.


`.claude/agents/` is reserved for **bounded standing roles with distinct responsibility**.
A subagent that merely runs a task is a task, not a role.

## Promotion criteria

A role becomes an agent only when **all** of the following hold:

1. **Standing responsibility exists** — the role recurs; it is not a one-off assignment.
2. **The responsibility spans several workflows** — a role covering one workflow is a skill.
3. **Separate context improves performance** — the role needs a different working set than the
   main session, and mixing them measurably degrades one or both.
4. **Tool and authority boundaries are explicit** — which tools it may use, which paths it may
   write, and which decisions it may never make.
5. **Escalation conditions are explicit** — the specific conditions under which it stops and
   returns to the owner.
6. **Verification does not depend only on self-review** — an external check, test, or second
   reader confirms its output.
7. **Owner approval.**

## Procedure

Draft the role definition and its boundaries as a decision record. Status `proposed`. Stop.
No agent is authorised to approve product purpose, buyer, supported decision, positioning,
releases, external actions, or canonical governance — regardless of its definition.
