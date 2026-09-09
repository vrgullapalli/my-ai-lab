# Critical Rules

- The agent ONLY interacts when the user interacts with it. Never push notifications or interrupt.
- **SANDBOX RULE: All greenhouse data lives ONLY in the garden/ folder and its subfolders (seeds/, ready/, compost/, inbox/). Never write outside this directory unless explicitly asked by the user.**
  - Can READ from Obsidian/Notion via MCP
  - Can READ from user-specified local folders
  - All seeds, state files, and agent-generated data stay inside garden/
  - The garden/ folder is the single source of truth and backup
- No images. Seeds are text and links only.
- When talking to users, always use human-readable seed names, never bare IDs.
- Germination happens at planting time ONLY. No queues, no deferred prompts.
- No single-seed viewing command. Users can open files directly.
- No special post-harvest command. `ready/` is a folder users open when ready to write.
- Every seed file operation must be followed by updating `garden-state.md`.
- Append to the History section of seed files for every change (status change, signal added, connection made).
- Nothing gets deleted. Everything goes to archive/ or compost/ first.
