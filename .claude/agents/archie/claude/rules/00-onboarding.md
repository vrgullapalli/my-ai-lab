# Rule: Data Source Onboarding Check

Always run this check implicitly before processing any user request or starting the Idea Generation Pipeline.

**Condition:** Check the contents of `claude/rules/03-data-source-config.md`.

**If it contains "STATUS: UNCONFIGURED":**
1. HALT all other operations.
2. Inform the user that you need to connect to their brand data source first.
3. Execute the skill `00-setup-datasource` to guide them through the setup process.

**If it contains a valid configuration:**
- Load the configuration from it and proceed with the user's request normally.
- Then open the config file it names (`config/data-sources.yaml`) and confirm the tier 1 and tier 2 paths exist. If one is missing, stop and ask for the current location. That is the one setup question allowed beyond the scope assessment. Never guess a path.
