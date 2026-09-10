# Page text Venkat supplied, 2026-09-10

Venkat pasted the full text of two pages that backfill writers could not open (both returned
403). The text below is what he pasted, lightly trimmed of share buttons and page menus.
Treat it as read at the source and cite the original link.

Dating rule: use a page only if its date is on or before your brief's date. Inside your
evidence window it can be a signal. Before your window it can only be labeled background.

---

## 1. CTO Magazine, "Semantic Layers Explained: Where They Sit Between Iceberg Tables and AI Agents"

- Link: https://ctomagazine.com/semantic-layer-ai-agents-iceberg-mcp/
- Author: Susan Nunziata
- Date: **2026-08-25** (shown on the page). Usable from the week of 2026-08-21 to 2026-08-28 onward. Not before.
- Fits: Meaning and Context first. Also Foundation and All Market.
- Caution: the page's "In brief" list contains two lines that do not belong to this article
  ("Designing an architecture that supports learning without unnecessary complexity." and
  "Recruiting the first developers and technical contractors."). Do not quote them.
- Caution: the Gartner figures are Gartner's predictions as reported by this article, not measured results.

Text:

Agentic AI is shining a spotlight on an area of data architecture that suffers from benign neglect: the semantic layer. Data engineers routinely struggle to get the budget they need for improving the semantic layer because it's seen as an intangible asset with no direct revenue.

But the semantic layer is most likely to determine whether the output of your AI agents is trustworthy. According to Gartner, neglecting semantics can make AI agents inaccurate and inefficient, exposing organizations to wasted spending and increased data and AI governance vulnerabilities.

An open table format such as Apache Iceberg gives an agent the openness and flexibility it needs to function. A Large Language Model (LLM) gives it reasoning ability. But only the semantic layer gives it an organization-agreed definition of what it's reasoning about. Getting that layer right now will save you a lot of heartache in the very near future.

Nearly two-thirds of data decision-makers (65%) expect many of their organization's business processes will be augmented or replaced by agentic AI in the next two years, according to an October 2025 Harvard Business Review study sponsored by Cloudera. Yet 73% say their organization has found it challenging to process and prepare data for AI.

Speaking at the Gartner Data & Analytics Summit in London on May 11, the firm's Rita Sallam, Distinguished VP Analyst, said: "Agentic AI outcomes depend on context, including semantic representations of data. Without context: a clear understanding of the specific relationships and rules within an organization's data, AI agents cannot operate accurately and are far more likely to hallucinate, introduce bias, and produce unreliable results. Organizations that fail to adopt comprehensive context structures, supported by a robust data layer, will perpetuate data inefficiencies and face heightened financial costs, as well as legal and reputational damage."

Gartner predicts that by next year, organizations that prioritize semantics in AI-ready data will increase their agentic AI accuracy by up to 80% and reduce costs by up to 60%.

Why does the semantic layer matter for AI agents? A semantic layer maps physical schema to context, such as metrics, dimensions, entities, and relationships, that are defined once and reused everywhere. It doesn't move or duplicate data; it defines meaning on top of data.

Agents and chained sub-agents run dynamic, autonomous, high-volume queries. So, an under-specified semantic layer could produce a different definition each time the same question is asked. Here's why: agents make independent decisions on how to interpret data schemas and join tables on the fly. Sub-agents generate new SQL or API queries dynamically without a fixed blueprint. Without a centralized semantic layer to lock down metrics and definitions, small context changes alter the output. Chained agents pass these shifting definitions to the next step, which multiplies the inconsistency.

Iceberg provides table format, schema evolution, time travel, and atomicity, consistency, isolation, and durability (ACID) guarantees on the storage layer. Model Context Protocol (MCP) standardizes how an agent discovers and requests metrics, but says nothing about whether governed metrics exist behind it. A semantic layer enforces one agreed-upon definition for every business metric and provides consistent logic, so agents aren't guessing column meanings or table relationships. Most importantly, it guarantees the exact same data is returned every time a question is repeated.

How to prepare a semantic layer for AI agents. If you already have a governed metrics layer for business intelligence, the fastest path to agent-readiness is exposing that same layer over MCP, rather than standing up a parallel, agent-specific layer that will drift from the first.

Metrics-layer tooling built to solve business intelligence metric drift can do that job well for agents: define metrics, dimensions, and joins once and expose them over MCP instead of re-deriving them per prompt. But keep in mind that it's deliberately narrow. For example, it knows what "active_subscription" sums to, but it doesn't know that "active_subscription," "renewal_risk," and "support_ticket" are related concepts an agent might need to reason across.

Semantic meaning, cross-system entity resolution, governance, lineage, and decision memory need to be combined into a single surface an agent can read.

Three additional considerations: Keep metadata and descriptions clear. Agents rely on rich text metadata to pick the right tools and attributes. Every metric, dimension, table, and join needs explicit, unambiguous natural language descriptions. Use business terms and explicitly state what a metric excludes. Don't just expose an open schema. Expose structured, parameterized semantic endpoints. Wrapping common business logic into predefined metric tools reduces the LLM's search space and minimizes hallucinated joins. Design for determinism and auditability. The same question must yield the same SQL logic every time an agent asks it. Implement logging within the semantic layer to track generated SQL, cache frequent metric requests, and return line-level lineage metadata so the agent can cite the precise logic used to calculate its answer.

Time to make those budget requests? If your organization is moving full speed ahead with agentic AI, now's the time to have that important budget conversation with your boss about upgrading your organization's semantic layer. It's the key to enabling your AI agents to perform accurately and efficiently.

---

## 2. Microsoft Fabric blog, "What's next for Fabric IQ Ontology: The operational context that powers your AI agents (Preview)"

- Link: https://blog.fabric.microsoft.com/en-gb/blog/whats-next-for-fabric-iq-ontology-the-operational-context-that-powers-your-ai-agents-preview?ft=All
- Author: Chafia Aouissi, Microsoft employee
- Date: **not shown exactly.** The page says "Published 5 months ago" and reports announcements from FabCon Atlanta 2026, so about March 2026. Before every backfill window.
- Use: background only, labeled as an older vendor post with an approximate date. Never as a signal inside a week.
- Caution: vendor source. Its claims are Microsoft's, and several features are marked "Preview" or "Coming Soon".

Text (key passages):

"Since introducing Fabric IQ, we've seen growing momentum around how organizations are using ontologies to establish a shared semantic foundation for analytics and AI. By modeling business concepts and relationships in the ontology, teams can move beyond fragmented data views and enable AI experiences that reason, automate, and act with confidence."

"AI is only as good as its understanding of your business. While Microsoft Fabric and OneLake unify where data lives, the meaning of that data often remains scattered across systems, tools, and teams. This leads to inconsistent definitions, brittle integrations, and AI outputs that are difficult to trust."

"At the center of Fabric IQ is the Ontology item, which connects data, processes, rules, and actions into a unified semantic layer. By binding real-world data to business entities and relationships, ontologies elevate raw tables and events into business-ready concepts that both people and AI can understand and use consistently."

Announced (Preview): rules that let the ontology start business processes through alerts and automated actions; sharing and permissions for Ontology items (read, edit, reshare); Azure Private Link support.
Announced (Coming Soon): Operations Agent using the Ontology as a knowledge source for its playbooks; public Model Context Protocol endpoints for the Ontology, "reinforcing the ontology as a central source of business understanding for AI."
