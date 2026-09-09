---
name: session-receipt
description: Write the end-of-session receipt and persist canonical state before context is lost. Use when a session is ending, when asked to "wrap up" or "close out", or immediately after a meaningful unit of work completes mid-session. Delta-driven (D-137): writes a dated receipt when durable state changed, updates portfolio/NOW.md when the restart point moved, and touches other files only when a new fact belongs there. Zero writes is a valid close.
---

# Session Receipt

> **PARKED 2026-09-08.** This skill read chief-of-staff's portfolio/, traces/ and
> memory/, which were deleted when Venkat started over. The job is still right; it has
> nowhere to write until the new chief of staff has intent/, memory/ and records/.
> Do not run it. Rewrite it when that exists.
