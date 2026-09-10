# Skill: Idea Output Format

Follow this exact format when outputting ideas from the Ideation Pipeline.

## FILE SPECIFICATION
Save to: `outputs/YYYY-MM-DD--topic-slug--ideas.md` (the lab path in rule 03).
Use today's actual date. Slugify the topic: lowercase, spaces to hyphens, remove special characters. This naming matches the eight runs already in the folder.

## CONTENT STRUCTURE
```markdown
# Topic Research: [Original Topic Input]
**Generated:** [timestamp]
**Categories activated:** [list all categories used — always-on + which situational ones and why]
**Tools down this run:** [none, or which, and what that cost]

---

## Research Table

| # | Category | Finding | Source | URL or file path | Date | Relevance Notes |
|---|----------|---------|--------|------------------|------|-----------------|
| 1 | ... | ... | ... | ... | ... | ... |

---

## Top 5 Content Ideas

### Idea 1: [Suggested Title]

**Combo type:** [e.g., Psychological framework + cultural reference + technical risk]

**Angle:** [Contrarian / Explainer-with-depth / Unexpected analogy]

**The connection:** [2-3 sentence paragraph explaining WHY these things connect. Demonstrate genuine cross-domain thinking. Show the structural or conceptual similarity.]

**Reader and reader pain:** [who, and the practical problem they are stuck on]

**Moonshot Shift:** FROM [current state] / TO [credible different state] / SO THEY CAN [act, decide, verify, explain, or lead differently]

**Pillars that bite:** [only the Capability Pillars that explain why the reader is stuck; often one or two]

**Suggested title:** [Title]

**Suggested subtitle:** [Subtitle]

**One-line hook:** [Draft opening sentence to start writing from]

**Controversy level:** [Safe / Spicy / Nuclear]

**Why this fits your brand:** [2-3 sentences explaining which specific brand pillars/audiences this aligns with]

**Receipts:**
- External: [url] ([what it proves])
- Internal corpus: [verified ID or file path] ([what it proves])
- Lived: [voice note / seed / chronicle ref] ([the real moment]) — anchors only, never load-bearing
- Counterevidence: [the strongest disconfirming finding]

**Strongest counterargument:** [and whether the thesis survives it]

**Kill test:** [7 verdicts in one line, e.g., swap pass · receipt pass · generic pass · reader pass · moonshot pass · trust pass · counter pass] — **weakest point:** [required, even for survivors]

**Scores:**

| Timeliness | Brand Fit | Originality | Combo Strength | Engagement | Evidence | Trust |
|------------|-----------|-------------|----------------|------------|----------|-------|
| [H/M/L] | [H/M/L] | [H/M/L] | [H/M/L] | [H/M/L] | [H/M/L] | [H/M/L] |

**Sources:**
- [Source name](url)

**Adjacent ideas:**
- If you like this angle, you could also explore... (anything that is really a separate piece goes to `backlog/`)

---

### Idea 2: ...
```

## LOW SIGNAL ALERT (Edge Case)
If fewer than 8-10 meaningful findings were found across all categories, prepend or append this section to the bottom of the output file:

```markdown
## ⚠️ Low Signal Alert

Research on this topic was thin. Here's what was sparse and why:
[Explain what categories had weak signal]

**Adjacent topics that would likely yield richer research:**
- [Topic 1]
- [Topic 2]
```

## KILLED IDEAS (kept from ARCHIE v2)
Save to `archive/kills/YYYY-MM-DD--topic-slug--kills.md`:

```markdown
### KILLED: <title>
- Verdict + reasons (which tests failed, and why)
- What was confirmed en route (receipts that DID verify)
- Salvage path: <the specific fix that would let a resubmission survive>
```

## BACKLOG ENTRIES (kept from ARCHIE v2)
Save to `backlog/YYYY-MM-DD--topic-slug--backlog.md`:

```markdown
### <insight, one line>
- Source moment:
- Reader pain:
- Possible Moonshot Shift:
- Receipts:
- Why it was removed from the current piece:
```

Rule: **Do not solve sprawl by deleting good thinking. Route it.**

## HANDOFF (kept from ARCHIE v2)
ARCHIE stops here. Once Venkat approves an idea, the writing system takes: reader pain, Moonshot Shift, the receipts, the counterargument, the adjacent backlog. Voice and style load there, not here. ARCHIE never drafts the piece.

**Formats excluded, hard rule:** comment-gated drops, manufactured poll bait, strategic-tag farming, AI-generated comment tactics, any "DM me" CTA.
