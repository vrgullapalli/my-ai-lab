# THE GREENHOUSE — Onboarding Guide

## What Is This?

The Idea Greenhouse is a stateful idea-tending agent for Claude Code/Claude Desktop. It manages a garden of half-formed ideas over time, helping them connect, ripen into writable content, or gracefully compost when they've run their course.

Think of it as a gardener for your thoughts. You feed it scraps — observations, links, half-baked theories — and it maintains, connects, cross-references, and tracks them until they're ready to become something real.

## Quick Start

1. **Open this directory** in Claude Code (`claude`) or Claude Desktop (drag folder into project)
2. **The Onboarding wizard starts automatically** on first interaction
3. **Say "Plant"** to add your first idea
4. **Say "Greenhouse"** anytime to see the full dashboard

## The Four Commands

| Say this | What it does |
|----------|-------------|
| **Greenhouse** | Dashboard — see everything at a glance |
| **Plant** | Add a new idea or sync from notes |
| **Ripen** | Check what's closest to becoming content |
| **Compost** | Review dying ideas, retire or revive them |

## How Ideas Flow

```
New thought → Plant → seedling (seeds/)
                          ↓
                  Signals accumulate, connections form
                          ↓
                  Hits 3/5 ripeness criteria → ready/
                          ↓
                  You write the content (outside this agent)

         OR

                  No activity for 14 days → wilting
                  No connections for 10 days → orphan
                          ↓
                  Compost → compost/ (always retrievable)
```

## Ripeness Criteria (need 3 of 5)

1. **Signal Diversity** — 2+ different source types
2. **Cluster Size** — Connected to 2+ other seeds
3. **Tension Present** — Has an unresolved question or contrarian angle
4. **Personal Stake** — You've engaged beyond just planting
5. **Age Threshold** — At least 14 days old

## Directory Structure

```
greenhouse-idea-cultivator/
├── README.md              # Project overview
├── CLAUDE.md              # Agent identity (loaded by Claude)
├── ONBOARDING.md          # You are here
├── garden/                # The garden data (self-contained)
│   ├── seeds/             # Active idea files
│   ├── ready/             # Ripened ideas
│   ├── compost/           # Retired ideas (never deleted)
│   └── garden-state.md    # Brain: index, themes, tracking
└── claude/
    ├── rules/             # Always-on context (loaded every session)
    │   ├── 00-start.md    # Entry point + onboarding trigger
    │   ├── 01-config.md   # Your configuration
    │   ├── 02-critical-rules.md
    │   ├── 03-scope.md
    │   ├── 04-personality.md
    │   ├── 05-file-structure.md
    │   ├── 06-cross-referencing.md
    │   ├── 07-ripeness-criteria.md
    │   ├── 08-composting-logic.md
    │   ├── 09-user-patterns.md
    │   └── 98-end-of-session.md
    └── skills/            # On-demand workflows
        ├── greenhouse.md
        ├── plant.md
        ├── ripen.md
        ├── compost.md
        └── first-time-setup.md
```

## Integration (Optional)

The garden data lives inside this agent at `garden/`. Everything is self-contained — you can also browse it directly in any markdown editor or Obsidian vault.

**Optional sync:** If you have Notion or Obsidian MCP connected to Claude, you can sync notes directly into the garden via `Plant > Sync`. Otherwise, just paste ideas directly into the chat.

## Tips

- **Don't overthink planting.** Drop anything that catches your attention. The garden does the organizing.
- **Skip germination questions if you want.** The agent won't nag. But answering them makes seeds ripen faster.
- **Check "Greenhouse" weekly** to stay oriented. The agent notices patterns you won't.
- **Trust the compost.** Composted ideas aren't gone — they'll resurface if a new seed connects to them.

## Moving Your Garden

Everything important lives in `garden/`. To migrate:
1. Copy the entire `greenhouse-idea-cultivator/` folder to a new location
2. Open it in Claude
3. Your garden state persists — no re-setup needed

If you want to change the garden location after setup, edit `claude/rules/01-config.md` and update the path. The agent will use the new location going forward.
