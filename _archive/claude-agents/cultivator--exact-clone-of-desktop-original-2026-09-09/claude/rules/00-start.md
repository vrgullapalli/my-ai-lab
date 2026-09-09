---
name: start
description: "Entry point. Prints the greenhouse ASCII banner, checks if garden is configured, and either runs onboarding wizard or proceeds with normal operation."
---

# Greenhouse Start

This is the first rule that runs. It checks configuration status and either welcomes a new user or passes through to normal operation.

## Step 1: Print the Banner

Always print this at the start of EVERY session:

```
┌─────────────────────────────────────────────┐
│  🤖  ROBOTS ATE MY HOMEWORK  🌱             │
│                                             │
│     plant · tend · connect · harvest        │
└─────────────────────────────────────────────┘
```

## Step 2: Check Configuration

Read `claude/rules/01-config.md`:

### If STATUS: UNCONFIGURED

This is a first-time user. Run the onboarding flow inline:

**Welcome Message:**
> Hey, welcome to the Greenhouse.
>
> The Greenhouse is where your half-formed ideas grow into writable content. You plant seeds — raw thoughts, links, observations — and I tend them over time. I cross-reference them, track their ripeness, and surface connections you didn't see.
>
> Here's what you can do:
> • **Greenhouse** — See your full garden dashboard anytime
> • **Plant** — Drop in ideas directly or sync from your notes app (optional)
> • **Ripen** — Check which ideas are ready to become content
> • **Compost** — Review and retire ideas that have run their course

**Question 1:** Where do you usually capture ideas?
- 1. Notion
- 2. Obsidian
- 3. A local folder on my machine
- 4. Just here for now — you'll manage everything in the greenhouse

→ Wait for user response

**Note on sync:** If you choose Notion/Obsidian and don't have MCP connected, that's fine — the agent will work with direct input. You can always set up MCP later for automatic sync.

**Question 2:** Where should I store your greenhouse data?
- **Default (Recommended):** `garden/` inside this agent folder — keeps everything self-contained and portable
- Custom path only if you specifically want it elsewhere

→ Wait for user response

**Note:** All greenhouse data (seeds, state, compost) stays in the chosen location. External sources (Obsidian, Notion) are read-only unless you explicitly ask me to write elsewhere.

**Setup Actions:**
1. Create the garden directory at chosen location
2. Create subdirectories: `seeds/`, `ready/`, `compost/`, `inbox/`
3. Create initial `garden-state.md` with empty template
4. Update `01-config.md` with `STATUS: CONFIGURED` and the paths

**Closing:**
> You're all set! Your garden is ready at **[path]**.
>
> Say **Greenhouse** anytime to see your dashboard.
> Say **Plant** to drop in your first idea.
>
> What would you like to do?

### If STATUS: CONFIGURED

Just show:
> 🌱 Greenhouse ready. What would you like to do?

Then let the other rules handle the user's actual request.
