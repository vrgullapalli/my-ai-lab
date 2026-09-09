---
name: first-time-setup
description: "Internal skill for conversational onboarding wizard. Creates garden structure at user-specified location. Do NOT invoke directly — triggered automatically by 00-start.md"
---

# /first-time-setup — Conversational Onboarding Wizard

**Note:** This skill is invoked automatically by `00-start.md` when the garden is unconfigured. Do not call directly.

## Steps

### 1. Display Welcome Banner

Show the compact greenhouse ASCII art:

```
    🌱       🌷        🌿        🌱         🌻
    |\       |         |        /|         |
    | \   🌿 |    🌱    |       / |    🌷   |
    |  \    \|    |     |      /  |    |   |
╔═══╧═══╤════╧════╧═════╧══════╧══╧════╧═══╧════╗
║ ┌───┐ │ ┌───┐  ┌───┐    ┌───┐  ┌───┐ ┌───┐   ║
║ │ ▓ │ │ │░▓░│  │▓▓▓│    │░▓░│  │▓▓▓│ │░▓░│ 🌡️║
║ │ ▓ │ │ │░▓░│  │▓▓▓│    │░▓░│  │▓▓▓│ │░▓░│   ║
║ └───┘ │ └───┘  └───┘    └───┘  └───┘ └───┘   ║
╚═══════╧═══════════════════════════════════════╝

     🌱  T H E   G R E E N H O U S E  🌱

     plant · tend · connect · harvest
```

### 2. Welcome Message

> Hey, welcome to the Greenhouse.
>
> The Greenhouse is where your half-formed ideas grow into writable content. You plant seeds — raw thoughts, links, observations — and I tend them over time. I cross-reference them, track their ripeness, and surface connections you didn't see.

### 3. Present Capabilities

> Here's what you can do:
> • **Greenhouse** — See your full garden dashboard anytime
> • **Plant** — Drop in ideas directly or sync from your notes app (optional)
> • **Ripen** — Check which ideas are ready to become content
> • **Compost** — Review and retire ideas that have run their course

### 4. Ask: Where Do You Capture Ideas?

Present as a numbered choice:

> First, where do you usually store your ideas?
> 1. Notion
> 2. Obsidian
> 3. A local folder on my machine
> 4. Just here for now — you'll manage everything in the greenhouse

**Handle response:**
- **Option 1-2 (Notion/Obsidian):** Note their preference. If MCP is available, mention sync will work. If not, explain they'll use direct input for now and can set up MCP later.
- **Option 3 (Local):** Ask for the folder path, verify it exists and is accessible
- **Option 4 (Just here):** Skip to garden location question

Store the choice in `01-config.md`.

### 5. Ask: Where to Store the Garden?

> Next, where would you like me to store your greenhouse data?
> 
> Default: `garden/` (inside this agent folder)
> 
> Use this location, or provide a custom path?

Wait for user response, confirm the chosen path.

### 6. Create Garden Structure

At the chosen location, create:
```
garden/
  seeds/
  ready/
  compost/
  inbox/
  garden-state.md
```

Populate `garden-state.md` with initial empty template:
- Last updated: [now]
- Last sync: never
- Next seed ID: 001
- All stats at zero
- All sections empty

### 7. Update Configuration

Set `01-config.md`:
- **STATUS: CONFIGURED**
- Garden path
- Idea source type and connection details (if MCP available, note it; if not, note "direct input only")
- Timestamp

### 8. Closing Message

> You're all set! Your garden is ready at **[path]**.
>
> Say **Greenhouse** anytime to see your dashboard.  
> Say **Plant** to drop in your first idea.
>
> Get back to me whenever you need any of these.

### 9. Hand Off

Return to processing the user's original command.
