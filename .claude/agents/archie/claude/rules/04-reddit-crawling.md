# Rule: Reddit Content Fetching

Always apply this rule implicitly whenever your research pipeline discovers a Reddit URL that needs to be read.

**Condition:** You are about to fetch, read, or scrape a URL containing `reddit.com`.

**Action:** You **MUST** prepend `https://markdown.new/` to the start of the URL before attempting to fetch it.

**Example:**
- Discovered URL: `https://www.reddit.com/r/ClaudeAI/comments/1rgcxpo/...`
- Fetch URL: `https://markdown.new/https://www.reddit.com/r/ClaudeAI/comments/1rgcxpo/...`

**Why:** Reddit aggressively blocks standard AI web scrapers and fetches (returning 403 Forbidden). Using `markdown.new` bypasses this limitation and returns perfectly structured markdown containing both the post and the comment discourse, which is critical for signal extraction.

## Source tactics (kept from ARCHIE v2)

- Reddit and Hacker News via the Firecrawl or Tavily tools when the Docker gateway is up; built-in web search as the fallback. Get posts AND comments where possible. The objection in the comments outranks the post.
- Substack comment sections and Medium responses via Firecrawl. X threads via search only; no direct scraping.
- **LinkedIn is never scraped.** Terms-of-service risk on his home platform. LinkedIn threads enter only as inbox drops (pasted text or screenshots).
- Prefer primary sources: papers, regulatory filings, first-party posts, the guidance documents themselves. Tech press is context, never the finding.
- Regulatory sources: FDA and EMA guidance, MLR precedent, state AI statutes, enforcement actions; law-firm client alerts as secondary.
- Job postings: the weekly instrument first, then live ATS sweeps (Greenhouse, Lever, Ashby, Workday) for gaps. LinkedIn Jobs and Indeed excluded. Verbatim requirement lines are the receipt; save a copy at run time, postings rot.
- When a tool is down, say so in the output. Never paper over a gap with tech press.
