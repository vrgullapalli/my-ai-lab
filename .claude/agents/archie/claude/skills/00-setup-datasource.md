# Skill: Data Source Setup Workflow

Run this skill ONLY when `claude/rules/03-data-source-config.md` contains `STATUS: UNCONFIGURED`, or when a path in `config/data-sources.yaml` fails to resolve.

It was run once, 2026-09-09. The lab's sources are already mapped. In practice this skill only fires if the lab moves.

## STEP 1: Assess Current Capabilities
Before asking the user, check your currently running tools and active MCP (Model Context Protocol) servers in your environment.
- Check what tools are available (e.g., Firecrawl, Tavily, Voicenotes, Google Drive).
- See if there are existing configuration files or agent memories pointing to brand folders.

## STEP 2: Ask the User
If the location isn't immediately obvious from your existing environment, ask the user:
> *"Where do your brand documents live now? (an absolute path to the lab root, or an external workspace via an MCP server?)"*

## STEP 3: Configure and Validate Connection
**If Local Folder (the lab):**
- Ask for the absolute path to the lab root.
- Using your file-reading tools, run an `ls` or equivalent command to verify the folder exists and that `work-os/brand-os/engagement-os/agents/archie/config/data-sources.yaml` is inside it.
- Confirm every tier 1 and tier 2 path in that yaml resolves. Report the ones that do not.

**If External Data (e.g., Notion, Google Drive):**
- Verify that you have the appropriate MCP server running to access that data.
- If it is not installed, give the user the exact command to connect it.
- Run a test fetch to ensure you have read access.

## STEP 4: Save Configuration
Once validated, update `lab_root` in `config/data-sources.yaml` (one line; every other path is relative to it) and update `claude/rules/03-data-source-config.md` so the `01-idea-generation-pipeline` knows exactly where to read.

## STEP 5: Confirm
Confirm to the user that the data source is mapped and saved, and prompt them for the first topic.
