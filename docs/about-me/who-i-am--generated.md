---
name: who-i-am
what: Who Venkat is, generated from the career and expertise model. Loaded every session.
generated_by: work-os/brand-os/model/build_who_i_am.py
rule: never hand-edit; change the model (entity JSONs + decision-log.md) and rerun; --check refuses drift
sources:
  domains: work-os/brand-os/model/domains.json (md5 a22261887ade408729cd64146f89dfa4)
  capabilities: work-os/brand-os/model/capabilities.json (md5 ee3578282fe70cb651e328e80a265d56)
  stages: work-os/brand-os/model/career-stages.json (md5 d69d25bca1efea0016786a8cb203d5b4)
  doc15: work-os/brand-os/model/15-present-day-expertise-summary.md (md5 ca719ca5b6641ce71c11aedc4b40eca4)
  doc17: work-os/brand-os/model/17-semantic-usage-guide.md (md5 3b8c4f6b93f23027f69fd67d2d146a88)
  positioning: work-os/brand-os/positioning/README.md (md5 797b8d0d716a93f5faf8d892e709136b)
labels: observed / owner-stated / inferred stay as written in the model; nothing here is flattened
---

# Who I am

## In my words

*(Venkat has not written this section yet. It lives in `work-os/brand-os/model/HIS-WORDS.md` and is placed here verbatim when it exists.)*

## What I say I do (ruled, in the positioning canon)

- **Category label:** "AI & Customer Data Strategy Advisor for Pharma"
- **Anchor sentence:** "I help pharma teams trust their customer data enough to put AI on it."
- **Lead sentence:** "I help pharma leaders understand what their customer data can support, how AI changes what is possible, where the foundation may not hold, and what needs to change before they scale or invest more."
- Source and dates: `work-os/brand-os/positioning/README.md`

## In one sentence (approved 2026-08-31)

He helps organizations — above all in life sciences — turn fragmented data and unproven AI into systems
whose outputs can be identified, understood, verified, and acted on, drawing on a twenty-three-year arc
of building exactly those systems as founder, embedded expert, and AI-directing builder.

## The five domains

- **Customer Data & Identity Systems** (DOM-001, foundational, current). The substrate he builds: making fragmented customer/entity data into one reliable, well-modeled view.
- **Applied AI & Decision Systems** (DOM-002, emerging-to-established; differentiating in combination, current, most active). The new machines he designs and directs: GenAI architectures, agents, knowledge systems, decision instruments.
- **Data & AI Trust: Verification, Semantics, and Governance** (DOM-003, differentiating, current). The stance that makes the rest defensible: 'AI proposes, validation proves, humans decide.'
- **Healthcare & Life-Sciences Commercial Domain** (DOM-004, foundational / supporting, current as context and market; not a delivery role in itself). The world it all happens in: pharma commercial ecosystems, provider/patient data realities, regulated-industry fluency, clinical literacy.
- **Product, Strategy & Commercialization** (DOM-005, established / supporting-to-differentiating, current). The vehicle that carries it to buyers: product leadership, assessment and diagnosis, operating-model design, and converting judgment into repeatable, sellable shapes.

## How I got here, in five stages

- **STG-001 Clinical credibility and evidence systems** (2003-02 to 2009-08; confidence medium). Evidence integrity as a designed system rather than a personal virtue; multi-stakeholder signal flow as what programs live or die on.
- **STG-002 The founder decade: healthcare data as a product** (2009-09 to 2019-11; confidence high (build years), medium (2016-2019 texture)). His own stated lesson: 'the hard part isn't collecting more data. It's connecting the data well enough to understand what's happening, decide what matters, and create something people can actually use.'
- **STG-003 Embedded expert: customer-data foundations for others** (2019-08 to 2023-06; confidence high). Organizational readiness gates technical work; every challenge pairs with a mitigation; definitional inconsistency as the root client failure.
- **STG-004 The turn: AI as the new medium** (2023-07 to 2025-06; confidence high). The technical barrier that defined him was gone; ADHD-AI fit ('maybe an ADHD mind is a perfect match for generative AI', typed 2025-04-09); title instability begins ('that's what I used to call it').
- **STG-005 Builder-verifier: AI systems and the machinery to distrust them** (2025-06 to None; confidence high). 'AI proposes, validation proves, humans decide'; 'Outputs are cheap and fakeable. Process is not'; semantics as the failure layer ('data worthiness'); his product is the judgment layer, not the tools.

## What I can do today

92 capabilities in `capabilities.json`, by maturity tag (re-counted at build time, never quoted forward):

- **advanced:** 30
- **established:** 50
- **emerging:** 7
- **foundational:** 5

The advanced ones, by name:

- CAP-001 — Design identity-resolution architectures that let an organization trust a single identifier
- CAP-004 — Diagnose identity fragmentation and quantify what it costs the business
- CAP-007 — Define single-customer-view and audience semantics that hold across teams
- CAP-009 — Rescue or reassess a customer-data program that is not delivering
- CAP-014 — Design layered data-platform architectures with role-appropriate access
- CAP-017 — Sequence platform builds so bounded versions ship while debt is logged deliberately
- CAP-019 — Quantify data quality so source and vendor choices become defensible
- CAP-020 — Document field-level lineage to an 'undeniable proof' standard
- CAP-033 — Design prompt frameworks and personas that encode a method, not just a request
- CAP-035 — Run the human-AI division of labor deliberately: ground truth from the human, breadth from the machine
- CAP-040 — Design verification ladders that match checking intensity to claim risk
- CAP-044 — Audit your own systems and accept adverse findings against your own claims
- CAP-045 — Design evidence chains where nothing enters as a bare assertion
- CAP-049 — Diagnose semantic ambiguity that ordinary data-quality checks miss
- CAP-052 — Establish data dictionaries and naming standards that teams actually adopt
- CAP-056 — Design human-in-the-loop authority boundaries for AI systems
- CAP-057 — Stand up decision-log and ADR governance as running infrastructure
- CAP-060 — Place data and AI work where pharma organizations will actually adopt it
- CAP-064 — Work provider and public data sources into commercial models
- CAP-066 — Design evidence-based scoring that narrows broad populations to ranked, qualified targets
- CAP-067 — Design patient- and provider-finding methods for rare and specialty populations
- CAP-073 — Run a structured customer-data and AI strategy assessment from goals to target design
- CAP-075 — Find the real question under the presenting question before answering it
- CAP-076 — Design phased roadmaps that give leadership real options, not a single path
- CAP-077 — Design governance cadences and decision-rights structures that keep programs aligned
- CAP-079 — Structure engagements so scope is discovered before it is priced
- CAP-080 — Produce consistent, decision-ready proposals from first conversations
- CAP-082 — Convert engagement work into named, reusable frameworks
- CAP-086 — Define product requirements and priorities from evidence rather than opinion
- CAP-093 — Teach complex data and AI ideas through everyday analogy

## Maturity, honestly (approved 2026-08-31)

- **Advanced and current:** identity/data architecture; assessment and diagnosis; verification and
  governance design; AI system direction; method extraction; the scoring/targeting family.
- **Emerging:** data-worthiness productization; delegation calibration; offer/pricing for the new
  practice (his own open question: "what's the value proposition for someone like me").
- **Dormant, judgment retained:** fundraising; reseller-channel motion.
- **Heritage, structurally load-bearing:** medical affairs; clinical practice (as literacy, not role).
- **Unproven and stated as such:** external users for the new products (namika's own file: "needs
  strangers actually using it"); outcome-class claims (formally an empty class by his ruling).

## The one constraint that gates everything

Distribution. The record's own verdict: "Creation was never the constraint. Finishing and distribution
are." Every capability above is stronger than its public evidence; closing that gap is downstream work
this model was built to feed — not work this analysis performs.

## How any agent must read this (binding, CE-D24)

1. **Identity flows top-down only.** Statements about who Venkat is come from `domains.json` and
   `capabilities.json`. Skills qualify; techniques and tools only *support*. No system may derive an
   identity claim ("data engineer," "developer," "analyst") from the technique or tool layer —
   this is the firewall against the documented past misread.
2. **No name without its qualifier.** A tool travels with its `usage_class` (hands-on / directed /
   conceptual / incidental). A technique travels with its `his_application`. A skill travels with its
   `usage_guidance`. A product travels with its `status` (including integrity caveats). A stage claim
   travels with its `confidence`.
3. **Authorship class is part of every build-era fact.** AI-era systems are "designed and directed,
   AI-built" (his ruling, verbatim in the source manifest). Never render directed work as hands-on
   engineering; never hedge it into less than direction either — direction is the claim, and it is
   evidenced.
4. **The never-cite list binds everything downstream.** No output may carry: 128% leads · $8.3M ·
   60–70% efficiency · 54ms P95 · commit totals including vendored/grafted repos (worthy-tool 601,
   sniff-decide 687, my-os 777) · any card count without denominator and date. Owner-defended but
   undocumented figures (Disney 425M/3×, Inizio 40%/70%) stay [owner-stated] and out of public copy.
5. **Confidentiality survives consumption.** Clients never named; Cambridge/Relevate patterns only;
   the S-04 transcript ruling ("INTERNAL-ONLY, PERMANENTLY") and every [internal-only detail] flag in
   the extracts propagate to anything built from this model.
6. **Interpretation stays labeled.** [observed] / [owner-stated] / [inferred] markers (and
   VERIFIED/CLAIMED/UNKNOWN where used) must not be flattened. An [inferred] reading presented as fact
   breaks the model's own standard.
7. **Counts are re-taken, never quoted forward.** Any consumer citing a count re-derives it from the
   canonical file at use time, with the date (the denominator discipline, TEC-038).
8. **Supersession is honored.** `decision-log.md` rulings are authoritative and dated; later entries
   supersede earlier ones; nothing is silently rewritten. Check it before relying on any structural
   fact.

## Never cite

No output may carry: 128% leads · $8.3M · 60–70% efficiency · 54ms P95 · commit totals including vendored/grafted repos (worthy-tool 601, sniff-decide 687, my-os 777) · any card count without denominator and date. Owner-defended but undocumented figures (Disney 425M/3×, Inizio 40%/70%) stay [owner-stated] and out of public copy.

---
Generated. To change a fact: edit the entity JSON, append a dated line to `model/decision-log.md`, rerun `build_who_i_am.py`.
