# File Structure & Formats

## Garden Location (Self-Contained)

The garden lives INSIDE the agent directory at `garden/` — this is the sandbox. All greenhouse data stays here:

```
greenhouse-idea-cultivator/
  claude/
    rules/
  garden/              <- EVERYTHING lives here
    seeds/             <- Individual .md files for each active idea
    ready/             <- Ideas that hit ripening criteria, ready to write
    compost/           <- Retired ideas (never deleted, always retrievable)
    inbox/             <- Temporary holding for external sync (Obsidian/Notion)
    garden-state.md    <- Brain: index, themes, ripeness tracking, patterns
```

**Important:** The agent can read from external sources (Obsidian via MCP, Notion via MCP, local folders) but all WRITES happen inside `garden/` only. This ensures:
- Complete backup of all ideas in one place
- No accidental writes to user files
- Agent can be moved/copied as a single unit

## Seed File Format

Files named: `{ID}-{slug}.md` (e.g., `001-pedagogy-as-hidden-ai-skill.md`)

When talking to the user, ALWAYS use the human-readable name (e.g., "Your seed *Pedagogy as the Hidden AI Skill*"). IDs only appear in garden-state.md as shorthand.

```markdown
# [Seed Title]
- ID: [number]
- Status: seedling | growing | ripening | wilting | orphan
- Planted: YYYY-MM-DD
- Last activity: YYYY-MM-DD
- Signals: [count]
- Connections: [list of connected seed IDs + names, or "none yet"]
- Ripeness: [X/5 criteria met — list which]

## Original signal
[What the person observed or thought, plus their context if provided]

## Germination
[User's responses to germination questions — blank if skipped]

## Attached signals
### Signal 1 — [date]
[Source + summary + how it connects]

## Agent notes
[Cross-references, editorial observations, convergence flags]

## History
- YYYY-MM-DD: Planted as seedling
```

## garden-state.md Format

Both internal brain AND user-facing dashboard. Contains:
- Last updated timestamp, last sync timestamp, next seed ID
- "How to Read This Garden" legend explaining all statuses
- Vital Stats (active, growing, ripening, wilting, orphans, composted)
- Active Themes (thematic clusters with connected seed IDs and names)
- Unattached Seeds
- Ripeness Tracker (seeds at 2+ of 5 criteria with breakdown)
- Convergence Warnings
- Orphan Watch
- Compost Candidates
- User Patterns (planting frequency, dominant themes, germination engagement, ripeness response)
