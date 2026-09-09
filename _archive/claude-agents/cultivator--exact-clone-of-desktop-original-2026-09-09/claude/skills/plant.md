---
name: plant
description: "Plant a new idea — accept direct input or sync from notes (if MCP available), cross-reference, germinate, and update garden state"
---

# Plant — Plant a New Idea

## Check MCP Availability

First, check what integrations are available:
- Notion MCP available? (Check if you can call notion tools)
- Obsidian MCP available? (Check if you can read from obsidian vault)
- Neither? That's fine — direct input works perfectly

## Present Options Based on Availability

**If MCPs available:**
> How would you like to plant?
> 1. **Paste a new idea** (direct input)
> 2. **Sync from your notes** (Notion/Obsidian via MCP)

**If no MCPs:**
> Paste your idea, link, or observation below:

---

## Option 1 — Direct Plant

1. User pastes their idea or link
2. Read `garden-state.md` to check for connections
3. Decide: new seed or signal for an existing seed?
   - **New seed:** create file in `seeds/`, assign ID + name, set status to seedling
   - **Signal for existing:** attach to relevant seed file, update signal count and last activity
4. Ask germination questions:
   - "What made you notice this?"
   - "Do you agree with it or resist it?"
5. If answered: responses go into Germination section. Personal stake and tension criteria get boosted
6. If skipped: plant without context. No nagging
7. Update `garden-state.md`

### Link Handling

- **Link WITH context:** use both the URL content and the user's reaction
- **Link WITHOUT context:** read the URL, generate a summary, then ask: "Here's what I found in this link. What caught YOUR attention about it?" A seed without the person's fingerprint is just a bookmark.

---

## Option 2 — Sync from Notes (Only if MCP available)

1. Check connected Notion/Obsidian for new notes since last sync timestamp
2. If connection fails or no new notes: gracefully fall back to direct plant
3. Present findings: what matches existing seeds (auto-attach as signals) and what looks new
4. User confirms which notes become seeds. Unconfirmed notes are skipped
5. Run germination for each confirmed new seed
6. Update `garden-state.md` including last sync timestamp

**Fallback behavior:** If MCP is not available or sync fails, automatically switch to Option 1 (direct plant) without making the user choose again.
