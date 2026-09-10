# Skill: Idea Generation Pipeline

Execute this skill when a topic is received and has passed the `01-scope-assessment` check.

One worker, six steps, in order. Do every step yourself. No sub-agents. Load brand context at Step 4 and not before.

## STEP 1: WIDE RESEARCH SWEEP

Search broadly across the web and the lab. Target 20+ distinct sources.

- **Strategy:** 2-3 broad queries on the topic, followed by targeted queries per always-on research category (e.g., `[topic] reddit opinions`, `[topic] psychological framework`, `[topic] evidence against`), and situational categories.
- **Platforms:** General web (news, blogs), Reddit (threads, AMAs — apply rule 04 and use markdown.new), Forums (Hacker News), YouTube, primary sources (papers, filings, guidance).
- **The lab (tier 1 in the config):** the seedbank, topic cards, chronicles, the work corpus, voice notes, the Telegraph project. Verified IDs and file paths only. Never invent a reference; report a layer that is unavailable.

## STEP 2: CATEGORIZE FINDINGS

Organize all findings into the following research categories:

### Always-On Categories

1. **Breaking news / recent developments**
2. **Hot takes & opinions** (X, Reddit, blogs)
3. **Contrarian voices** (complaints, failure stories, dissent, both sides of live arguments)
4. **Psychological / behavioral frameworks** (loss aversion, status games, etc.)
5. **Analogies from other domains** (structural patterns, not keyword matches)
6. **Counterevidence** (kept from ARCHIE v2: whatever weakens the topic's obvious angle. Never removed, never merged away.)

### Situational Categories (activate when relevant)

1. **Business / monetization angles**
2. **Technical deep-dives**
3. **Cultural / meme layer**
4. **Historical parallels**
5. **Data & stats**
6. **Regulatory / legal implications** (FDA, EMA, MLR, state AI law; dated obligations beat think pieces)
7. **Creator / builder stories**
8. **Failure modes / cautionary tales**
9. **Market demand** (kept from ARCHIE v2: job postings, the weekly instrument first; verbatim requirement lines are the receipt)
10. **Friction** (kept from ARCHIE v2: workarounds, repeated work, manual compensating, redoing AI output before use, one-person dependencies)
11. **His own thinking** (kept from ARCHIE v2: seeds, corrections, reversals, questions he keeps returning to, statements that changed after evidence)
12. **His proven work** (kept from ARCHIE v2: the corpus and Telegraph, as historical proof)

## STEP 3: BUILD THE RESEARCH TABLE

Compile findings into a structured table (15–30 rows) with the following columns:
`| # | Category | Finding | Source | URL or file path | Date | Relevance Notes (the mechanism) |`
Do not filter aggressively at this stage. Preserve disagreement. Do not yet decide what the article is "about."

Then a light hygiene pass: dedupe, flag stale dates, separate observation from interpretation. No editorial judgment yet.

## STEP 4: LOAD AND ANALYZE BRAND DOCUMENTS

Read `claude/rules/03-data-source-config.md`, open the yaml it names, and read every tier 2 file. Extract:

- Core brand themes and content pillars
- Positioning statements and recurring angles
- Audience segments (the ideal customer, the thirty recognizable moments)
- The six Capability Pillars (Foundation · Meaning and Context · Use · Operating Model · Trust and Control · Repeatability and Scale). They are backstage: use them to diagnose why a reader is stuck, surface only the ones that bite, never force all six.
- Trust Is the Product principles
- Voice characteristics explicitly utilized or avoided (from tier 2 only; never open tier 3)

## STEP 5: CROSS-POLLINATE AND GENERATE IDEAS

Find cross-domain connections between research findings and brand positioning. Target:

- **Explainer-with-depth:** trending topic + psych framework + brand connection
- **Contrarian:** mainstream opinion + opposing evidence + brand-aligned reframe
- **Unexpected analogy:** unrelated domain pattern mapped onto a brand-relevant topic

For each candidate, also name (kept from ARCHIE v2): the reader and their practical pain · the decision or work problem · the structural mechanism · at least one receipt · the strongest counterevidence · the **Moonshot Shift** (FROM the reader's current state / TO a meaningfully different credible state / SO THEY CAN act, decide, verify, explain, or lead differently). Reader pain must be practical, never abstract. Moonshot means reader capability, not dramatic language. These are proposals until Venkat accepts them.

Select top 5 ideas based on Surprise (non-obvious), Natural fit (not forced), Audience interest, Substance, Avoidance of restricted territory, and different angles.

### STEP 5b: KILL TEST (kept from ARCHIE v2, run by you, not a sub-agent)

Run every candidate through all seven. Write the verdict down; it goes in the output.

1. **Swap test:** state the mechanism in one sentence using neither domain's nouns. If the vocabulary is doing the work, KILL.
2. **Receipt check:** spot-check the sources live; verify corpus IDs. Misquoted, overstated, or irrelevant, KILL.
3. **Generic test:** would an assistant with no corpus and no positioning produce this? Yes, KILL.
4. **Reader test:** a real reader problem, or a topic looking for a problem?
5. **Moonshot test:** does it materially change what the reader can see, decide, or do?
6. **Trust test:** does the claim outrun the evidence? Is the uncertainty visible?
7. **Counterargument test:** does the thesis survive the strongest reasonable objection?

Three routing flags (never kills): **Framework flag** (is it being forced into the six pillars?) · **Sprawl flag** (adjacent insights that are separate pieces go to `backlog/`) · **Instrument flag** (does the reader's new capability imply a checklist, diagnostic, map, or worksheet? Propose it; never build unasked).

Kills go to `archive/kills/` with the reason and a salvage path. If fewer than 3 ideas survive, go back to Step 5 once with the killed ideas' salvage paths in hand.

## STEP 6: SCORE IDEAS

Score each surviving idea (High/Medium/Low) on:

- **Timeliness** (Hot right now vs Evergreen)
- **Brand Fit** (Natural connection to pillars)
- **Originality** (Fresh vs Done-to-death)
- **Combo Strength** (Surprising/non-obvious connection)
- **Engagement Potential** (Reaction/share/reply potential)
- **Evidence Strength** (kept from ARCHIE v2: external primary source present? a verbatim job-posting line counts; a lived story does not)
- **Trust** (kept from ARCHIE v2: claim discipline, uncertainty shown)

Never reduce scores to one number. Proceed to Skill `02-output-format` to finalize output.
