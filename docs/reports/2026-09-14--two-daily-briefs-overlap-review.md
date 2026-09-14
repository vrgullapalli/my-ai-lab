# Two whole-market daily briefs: what repeats (week of 2026-09-14)

Follow-up F-20260914-0248-3. Read-only. Compared the three newest dates where both sides ran: 2026-09-11, 09-12, 09-13. Pages read in the cloud gallery, because nothing from either side has been pulled into the lab since 2026-09-09.

**Where the outputs are.** The 9 AM side has one pulled file, `work-os/scheduled-tasks/all-market-signals/outputs/2026-09-09.md`. The midnight side's folder `work-os/scheduled-tasks/market-signals/00-all-market-signals/daily/outputs/` is empty. There is no midnight page for 2026-09-09 at all: that routine was created on 09-09 and first ran at midnight on 09-10. So the 09-09 pair the task named does not exist. The 09-10 pair was not compared because "All Signals 2026-09-10" sits beyond the gallery's 50-item window.

## 1. What each brief is asked to do

Both prompts ask for the same thing in nearly the same words. The 9 AM one: "Surface exactly five signals that could change how Venkat thinks, advises, creates, or acts around AI, customer data, and commercial pharma." The midnight one: "Surface exactly 5 high-value signals that could change how Venkat thinks, advises, creates, or acts around applied AI, customer data, and commercial pharma."

The real differences are in the rules, not the goal. The 9 AM one says "Start with the last two days ... You may go back up to about eight weeks. Say in one line how far back you went and why," and reads "the most recent Market Signal Brief" first. The midnight one has no time window and says "Scan broadly across the six Capability Pillars," tagging each signal with a pillar. It reads only its own past pages.

## 2. What repeated, per shared date

| Date | In both | Only 9 AM | Only midnight |
|---|---|---|---|
| 09-11 | 0 | 5: FDA rule to end "adequate provision" in TV drug ads; Citi survey (72% scaling, 24% expect big gain); Justice Dept bulk data rule read onto life sciences; Omnicom and Publicis own the identity layer; a solo advisor's fractional data-officer rate card | 5: DeepIntent Cora launch; Veeva vs Salesforce CRM counts; DrFirst prior-auth 63% no-edit rate; three state AI disclosure laws; Aktana next-best-action case study |
| 09-12 | 0 | 5: OptimizeRx and Definitive Healthcare revenue drops; Fierce Pharma Week new data track; Novo Nordisk moves $600M media to Omnicom; Novo sues Lilly over ads; 12-digit drug code rule | 5: data-and-AI executive seat at eight pharma companies; PHM Verified physician-data scorecard; Lundbeck scales into EVERSANA's AI platform; AgentAudit research paper; McKesson buys Precision Medicine Group |
| 09-13 | 0 exact, 1 near miss | 5: Indegene 60% outcome-based contracts (earnings call); ChatGPT Health 300M weekly questions plus Epic; GoodRx Pharma Direct up 76%; Phreesia 4% lift study; two drugmakers' 10-Q "AI does not decide pricing" sentence | 5: McKesson breach; AstraZeneca 2030 AI target; Indegene "platformization vs agentification" blog; PHM Verified follow-up; fractional Chief AI Officer advisory content |

**Same-day repeats: zero out of 15 signals per side.** The one near miss is Indegene on 09-13, but the 9 AM side used its earnings call and the midnight side used a blog post, and they make different points.

**Themes that repeat across days, on both sides:** the combined data-and-AI executive seat (9 AM on 09-09 with the J&J and Takeda postings; midnight on 09-10 and 09-12), the fractional data or AI leader offer (9 AM 09-11; midnight 09-13), Veeva's Falcon (9 AM 09-09; midnight 09-10, per its own memory note), and Omnicom or Publicis identity work (9 AM 09-11 and 09-12; midnight's PHM Verified on 09-12 and 09-13). Each side arrives at these on its own, a day or two apart, and neither knows the other has already covered it.

## 3. What differs in form

- **Length.** The 9 AM pages ran 6,590, 7,025 and 7,345 words (tags stripped) at 51 to 55 KB each. The midnight pages are shorter; they came back whole where the 9 AM ones were too big to return inline. Not measured to the word.
- **Model and sources.** 9 AM runs on claude-opus-5 and leans on filings, earnings transcripts, law firm alerts, and a stated window up to eight weeks. Midnight runs on claude-sonnet-5 and leans on press releases, trade press, and trackers from the last few days.
- **Structure.** 9 AM: eight parts per signal, one-word confidence, no pillar tag. Midnight: thirteen parts, including an "Image" slot that printed "Image: none available" on all 15 signals, and it used "Low to Medium" confidence three times, which the 9 AM prompt forbids and the midnight prompt does not.
- **Delivery.** Both publish one private page and send one push. Titles differ: "All Market Signals 2026-09-xx" versus "All Signals 2026-09-xx". Two pushes a day for the same subject.
- **Memory.** 9 AM reads its own history plus the Market Signal Brief. Midnight reads only its own history. Neither reads the other, so the cross-day repeats above cannot be caught by either.
- **Family.** Midnight has Wednesday and Friday siblings that read its pages as evidence. The 9 AM one stands alone.

## 4. Recommendation

**Option 1, recommended: keep both, with a named split, and wire them together.** Reason: zero same-day repeats across three days means they already do different jobs; the waste is that they do not know about each other.
- Midnight is the news watch: last two days, launches and announcements, pillar-tagged, feeding the Wednesday and Friday syntheses. Drop its "Image" slot and forbid confidence ranges.
- 9 AM is the deeper read: filings, earnings calls, up to eight weeks, decision-oriented. Add one line to its prompt: read that morning's "All Signals" page first and do not repeat it.
- One push a day, not two. The midnight run goes silent (he is asleep at midnight anyway) and the 9 AM push links both pages.

**Option 2: retire the midnight daily, keep its Wednesday and Friday.** The 9 AM brief becomes the whole-market daily, with a pillar tag added. Cost: the Wednesday and Friday whole-market prompts read their memory by the "All Signals" title prefix and would need re-pointing, and the fresh-news catches (Cora the day after launch, the McKesson breach) would likely be lost to the 9 AM brief's habit of widening to older filings.
