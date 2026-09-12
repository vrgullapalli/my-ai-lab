---
title: Career model capability scan
date: 2026-09-12
author: Alfred (session ad6b8e57), at Venkat's ask
kind: read-only scan; this report is the only file written; nothing here is approved, designed, or built
question: "Which parts of the career model can already support capability fit, proof, opportunity discovery, and capability evolution, and what relationships are missing?"
canonical_source: work-os/brand-os/model/ (ruled 2026-09-02, brand-os DECISIONS 001; hub since 2026-09-10, DECISIONS 033)
other_copies:
  - ~/Documents/_warehouse/career-advisor--snapshot-from-imac--2026-09-10/career-evolution/ (frozen; entity files byte-identical to the lab copy, checked by checksum)
  - ~/Desktop/my-ai-lab-v2/brand-identity/model/ (old lab copy; entity files byte-identical; lacks the three hub files)
not_on_this_machine:
  - Knowledge Layer MCP (~/My_AI_Lab is absent; no such MCP server is registered here; only descriptions exist: products.json PRD-011 and the Evidence Atlas copy on the Desktop)
  - the master work-corpus registry (schema approved 2026-08-31, never populated; "registry" per CE-D01 means four documents, not a table)
answers:
  capability_fit: partial (observed; one-hop match by reading, no recorded matches)
  evidence_backed_proof: partial (observed; walkable to a quote in an extract, not to an artifact from this machine; outcomes empty)
  opportunity_discovery: weak (observed; market language lives on skills; no company, role, job, or project links)
  capability_evolution: backward strong in prose, forward absent (observed)
  rebuild_needed: no (inferred; retrieval plus write-back covers the gaps found)
next_move: in today's approved hand test, every match to the career model cites a capability id and its extract, and the result lists what the model could not answer
tags_used: observed (seen on disk or measured by script) · inferred (my reading) · unknown
sources:
  - work-os/brand-os/model/ (README, 00-status, 14, 15, 16, 17, decision-log, SPOKES, REASONING-INDEX, all 8 entity JSONs, expertise-graph.json, stage1-extracts/, check_hub.py, build_who_i_am.py)
  - work-os/brand-os/DECISIONS.md 001, 005, 033 to 037
  - work-os/brand-os/docs/career-advisor-reasoning--2026-09-10/ (handoff, master registry proposal, asset audit index)
  - work-os/brand-os/engagement-os/ (targets/, docs/state.md, inputs/opportunity-map, agents/archie/config/data-sources.yaml)
  - work-os/brand-os/audience/ (weekly/taxonomy_demand.py and its 2026-09-02 output, buyer-terms-2026-08 report, icp v3)
  - .claude/skills/dossier and committee; docs/about-me/ (who-i-am generated, POV library, analyses inventory)
  - docs/reports/2026-09-11--market-signal-to-action-scan.md; docs/plans/2026-09-12--hand-test plan; receipt 2026-09-10-1630
  - ~/Desktop/my-ai-lab-v2/chief-of-staff/evidence/work-inventory/evidence-atlas (for the work-corpus map only)
---

Alfred — the short version first.

**The model is a good record and a weak instrument.** It holds 92 capabilities with sources, maturity, and a one-line problem each. It can be read against a need today. It cannot remember a match, point at an artifact from this machine, or say what a capability leads to next.

**Nothing has used it yet.** Seven readers are listed. One has run. None has sent a fact back. No target dossier, seed, point of view, or project cites a capability id, except one "near" match.

**Retrieval plus write-back covers the gaps.** No rebuild is warranted by what I found.

---

# Which copy is canonical

- **Canonical:** `work-os/brand-os/model/` in the lab. Ruled 2026-09-02 and again 2026-09-10 as the hub. [observed]
- **The warehouse iMac snapshot and the Desktop copy match it byte for byte** on every entity file and the decision log. Only `00-status.md` differs in the warehouse copy, and only the lab copy has the three hub files. [observed, checksums]
- **The model has not changed since 2026-09-02.** Every entity file is dated 2026-09-02 00:57. [observed]
- **The Career Advisor repo is retired** as a front door. Its 61 reasoning files are in the lab as evidence, not canon. [observed, DECISIONS 036]
- **The Knowledge Layer MCP is not on this MacBook.** `~/My_AI_Lab` does not exist here and no such server is registered. What exists is a description of it in the products file and the old Evidence Atlas on the Desktop. [observed]
- **The master work-corpus registry was never populated.** The schema was approved on 2026-08-31. The four documents ruled as "the registry" are maps, not a table. [observed]

# Current shape

| Layer | Count | What each record carries |
|---|---|---|
| Stages | 5 | dates to the month, central problems, capabilities developing (free text), carried forward, left behind, enabled next |
| Domains | 5 | includes, excludes, class, currency, contributing stages |
| Subdomains | 26 | anchors (named work, tagged observed or owner-stated) |
| Capabilities | 92 | problem (one line), outcome (one line), stages, maturity, relevance, judgment, sources |
| Skills | 82 | market terms, audience language, first appearance, evolution line, maturity |
| Techniques, tools | 48, 46 | his application, usage class |
| Products | 13 | era, stage, honest status, capability links |
| Graph | 317 nodes, 828 edges | see below |

Edges in the graph, by kind [observed]:

| From | Relation | To | Count |
|---|---|---|---|
| skill | supports | capability | 214 |
| stage | developed | capability | 140 |
| product | evidences | capability | 23 |
| stage | produced | product | 13 |
| capability | part of, also serves | subdomain | 172 |

Readers on paper and in fact [observed]:

| Reader | Says it reads the model | Cites a capability id in any output | Has sent a fact back |
|---|---|---|---|
| Session file (who-i-am, generated) | yes, check passes | yes, by design | read-only |
| ARCHIE config | yes | no run since wiring | never |
| Dossier skill | yes | no; angle maps use gap numbers 1 to 5 from the old opportunity map | never |
| Committee skill | yes | one file, BioMarin, "CAP-006 (near)" | never |
| Strategist spec | yes | no | never |
| My-voice skill | yes | read-only | read-only |
| Weekly market instrument | no; the sensor reports it unwired | one run, 2026-09-02, 152 postings | that one run |

Zero seeds, zero points of view, zero project files, the positioning canon, and the ideal-client profile reference a capability id. [observed]

# 1. Capability fit

**Question:** given a problem or need, which capabilities are relevant?

**Already supports**
- Every capability has a one-line business problem. Example, CAP-001: "The same person appears as different records across systems." A reader can match a need to these by meaning today.
- Every skill has buyer language. Example, SKL-001: "We can't tell if these are the same customer across our systems." Plus market terms for search.
- The weekly instrument proved a text-match rollup once: postings matched to skills and tools, rolled up to capabilities and domains. [observed, 2026-09-02 output]

**Does not support**
- No match is ever recorded. Each reader starts from zero.
- No strength or reason on a match. The rollup counts word hits; the dossier reads by eye.
- Two problem vocabularies. The model's one-line problems and the dossier's five gap types are not mapped to each other.
- The broadest capabilities win any match. CAP-061 (translate across stakeholders) topped the demand run at 75 of 152 postings. CAP-006, CAP-075, and CAP-085 are the same shape. [observed]

**Missing relationship:** need → capability, with a strength, a reason, and a date, kept somewhere a later reader can find.

# 2. Evidence-backed proof

**Question:** what shows I actually did this?

**The chain today:** capability → source pointer → extract file (a quote with a path) → primary artifact.

| Link | State [observed] |
|---|---|
| Capability → source | 145 pointers on 92 capabilities. 126 resolve to an extract file. 17 are name-only, and 2 of those name documents that live in the reasoning drop, outside the model |
| Extract → artifact | 22 absolute paths cited in extracts. 2 exist on this MacBook. The rest are on the iMac, in Dropbox, or at old paths |
| Product → capability | 23 links cover 17 of 92 capabilities. The products file says links were "seeded from the DOM-001 chunk and will be completed as the catalog lands." Never completed. Three products link to nothing |
| Capability → outcome | The outcome field is a promised result, not a record. The outcome proof class was "formally closed empty" on 2026-08-09 |
| Capability → role | none. Roles are free text inside stages |
| Capability → work product | none. The ~40 works and 8 instruments from the asset audit are not entities |

**Strength today:** strong for "what kind of work," because the extract quotes are real and dated. Weak for "show me the thing." Empty for "what happened after."

**One sensor note.** The hub check reports 30 never-cite hits in live text. All 30 are lines that quote the ban itself, in the reasoning drop and the generated session file. The guard pattern misses them. Not a leak. [observed]

# 3. Opportunity discovery

**Question:** given a market signal, where might my capabilities create value?

What the model can connect today [observed]:

| Thing | Connected to capabilities? |
|---|---|
| Industries | one only, pharma, as DOM-004. No others |
| Business problems | one line per capability, not entities |
| Commercial jobs or offers | no. Offers live in the old opportunity map. CAP-074 is tagged "the active offer," CAP-090 "emerging" |
| Companies | no. 15 targets, 11 at engage, none cite a capability id |
| Roles | no |
| Market needs | 53-posting buyer-term crosswalk maps to skill ids. "Nothing from this run has been applied" |
| Signals | the signal record in `engagement-os/docs/state.md` has no capability field. Zero records anyway |
| Current projects | Telegraph+, worthy-tool-v2, decision-foundry: zero references to the model |

**The sharpest gap:** the model's own status file has listed "a signal-intelligence capability with three working expressions" as a pending amendment since 2026-09-02. Telegraph+ is that capability. The model does not hold it. [observed]

**What it can answer now:** "which capability does this need touch," if a person or model reads the capabilities file against the signal. **What it cannot:** "who else has this need," "what did I offer last time," "what came of it."

# 4. Capability evolution

**Question:** how did this develop, what built it, what next?

**Backward, in prose: strong.** Five dated stages. Five transitions with causes. What recurred, compounded, merged, and faded. Four new combinations named in doc 14. [observed]

**Backward, in data: moderate.** [observed]
- 82 of 82 skills carry a first appearance and an evolution line. Example: "Product feature (Medikly) → enterprise practice (Disney) → client platform design (Ele) → AI-era entity pipelines."
- 37 of 92 capabilities span two or more stages, so progression is visible. 36 exist only in the current stage.
- Stage records list "capabilities developing" as free text, not ids.

**Forward: absent, by design.** [observed]
- No capability-to-capability relation of any kind. No combination, adjacency, or leads-to edge. The four combinations are prose only.
- Seven capabilities are tagged emerging. No date on any maturity tag, no rule for moving one.
- The current stage's "enabled next" reads: "open, this analysis is itself part of the answer."
- Nothing since 2026-09-02 has entered the model: not Telegraph+, the point-of-view library, the taste interview, or the work of the last week.

# Already useful

- Answering "what kind of work have I done, and where is the quote" for any of the 92 capabilities.
- Generating the session identity file, with a drift check that passes.
- The identity firewall: tools and techniques cannot become identity claims.
- Buyer language and market terms on every skill, ready for matching.
- The honest maturity and status tags, including "unproven" and "dormant."

# Partial

- Matching a need to capabilities. Works by reading, not by record.
- Proof. Reaches a quote, not an artifact, from this machine.
- Demand measurement. One run exists, the script is unwired, and the runner points at dead paths.
- Product evidence. 17 of 92 capabilities have a product behind them.
- Evolution. Rich for skills and stages, thin for capabilities, nothing forward.

# Missing relationships

Three would unlock the most, in order:

1. **Need → capability → evidence, written back.** When a dossier, a brief, or a hand test matches a need to a capability, the match is recorded with the capability id, the evidence pointer, and the date. Today every match evaporates.
2. **Capability → artifact on this machine.** The extract quotes need one path each that resolves here, or an honest "on the iMac" or "in Dropbox" tag. Twenty of 22 cited paths do not resolve.
3. **Capability → capability: combination, adjacent, leads to.** Doc 14 already names the compounds in prose. Without the relation, retrieval matches him to single labels, and the single labels that match most are the broadest ones.

Behind these, one bookkeeping link: **current project → capability**, so Telegraph+ can move "emerging" tags and the pending signal-intelligence capability can land.

# Risks

- **Broad capabilities swamp matches.** CAP-006, CAP-061, CAP-075, CAP-085 match almost anything. [observed in the demand run]
- **Overlap clusters.** Assessment: CAP-004, 009, 062, 073, 074. Pre-ingestion: CAP-022 and CAP-050, near-identical wording, both emerging, both evidenced by the same two products. Standards: CAP-011, 052, 053, 055. Adoption: CAP-060 and 078. [observed]
- **Evidence implied, not linked.** 75 capabilities have no product behind them. 17 sources are name-only.
- **Old work with no connection.** The ~40 works, 8 instruments, 14 architecture decision records, the relationship registry workbook, and the false-agreement episodes are outside the model.
- **Sections with no consumer.** Techniques, tools, the LinkedIn crosswalk, six generated CSV files, and the graph file itself. Nothing outside the model folder reads the graph. [observed]
- **Duplicated structures.** Three buyer-problem vocabularies. Three byte-identical model copies, and two live files still point at the Desktop copy's paths (the hand-test plan's demand file and the weekly runner). A stale "Stage 6 awaiting approval" line resurfaced in the 2026-09-11 orientation brief; the decision log says approved 2026-08-31.
- **The past as a trap.** The model is 100% derived from work done. Its own doc 14 says "the profile says advisor, the record shows builder-verifier." The buyer-term report shows his most distinctive capabilities have zero buyer language: "data worthiness" 0 of 53, "verification" 0 of 53. Word matching will keep pairing him with yesterday's job titles and miss the crossings doc 14 calls the differentiation. [observed, then inferred]
- **Another finished, unshipped artifact.** Built 2026-08-31. Seven readers, zero returns, zero outputs citing it in twelve days. Doc 14's own competing interpretation applies to the model itself. [inferred]

# Highest-value opportunity

**Turn every reader into a writer.** The readers already exist and already claim to read the hub. The one change that activates the model across the lab is that each match they make is recorded: the need, the capability id, the evidence pointer, the date, and later what happened. That gives the lab a growing record of where his capabilities met real needs, which is the thing none of the four questions can be answered from today. It uses retrieval and one relationship. It needs no new schema, agent, graph, or embeddings. [inferred]

# Next move

**One step.** Today's hand test is already approved and already lists the career model as a context store. Add one rule to it: every match to the model cites a capability id and its extract, and the result report lists what the model could not answer. That is the cheapest proof of whether retrieval plus write-back is enough, before anything is designed.

**Needs from Venkat:** yes or no to the rule. Nothing else.
