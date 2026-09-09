# Search strategy

How `target-scan` finds roles when a collector cannot. Adapted from the query
strategy in the job-search framework, with the parts that do not apply removed.

<!-- SETUP: replace the capability categories below with your own. -->

## Coverage, and the gap the fallback fills

`targets/collectors.json` records which applicant tracking system each company
runs on. Where a collector exists, use it — it returns structured data with
honest dates.

**The fallback exists for the gap between companies we want to scan and systems
we have built collectors for.** It fires in four cases:

1. No system was detected on the company's careers page
2. The system was detected but we have no collector for it — currently Jobvite,
   SuccessFactors, iCIMS and SmartRecruiters
3. A collector fails at runtime
4. The runtime is unavailable

Tag every fallback result with its origin. A stored entry whose URL later
resolves to nothing reads very differently depending on whether it came from a
live API or a search index that can be weeks stale.

## Where to search

**Primary — the company's own careers page.** We scan by company, not by
keyword, so this is the main path rather than a backup:

```
site:<company-domain> careers <capability keyword>
site:<company-domain>/careers <capability keyword>
```

**Secondary — the hosted board, when the company is on a platform we cannot
collect from:**

```
site:jobs.jobvite.com "<Company Name>" <capability keyword>
site:careers.smartrecruiters.com "<Company Name>" <capability keyword>
site:jobs.<company>.icims.com <capability keyword>
```

**Tertiary — aggregators, used only to discover that a role exists.** Never as
the record. Aggregator dates are refreshes, not openings, and the requisition
identifier and seniority grade are routinely dropped. Once a role is found this
way, go to the employer's own page for the authoritative version.

## Write queries by function, never by job title

The same work carries different titles at every company. Verified today: the
same underlying role appears as *Director, Real World Data*, *Senior Director,
Advertising Analytics*, and *Director, Data Enablement and Reporting* at three
different organisations.

**Name each category after the function. List several plausible titles inside
it.** Betting a whole category on one exact title string is how a scan returns
nothing and looks healthy doing it.

### Category 1 — [YOUR PRIMARY CAPABILITY]

```
"[TITLE VARIANT 1]"  "[TITLE VARIANT 2]"  "[TITLE VARIANT 3]"  "[FUNCTION KEYWORD]"
```

### Category 2 — [YOUR SECOND CAPABILITY]

```
"[TITLE VARIANT 1]"  "[TITLE VARIANT 2]"  "[FUNCTION KEYWORD]"
```

### Category 3 — [ADJACENT CAPABILITY]

```
"[TITLE VARIANT 1]"  "[TITLE VARIANT 2]"
```

### Category 4 — broader net

Wider terms that catch roles the specific categories miss. Expect noise; this
tier is for coverage, not precision.

## Read the whole board, not matching roles

When a collector is available, **request everything the company has open** and
filter afterwards. The set of roles read together discloses the roadmap and the
gaps; a single posting is marketing.

Keyword queries are for the fallback, where fetching everything is not possible.

## Date handling

Include a posting whose date cannot be established, and **flag it as date
unknown**. Never infer one.

This is not an edge case. Workday truncates every posting at "Posted 30+ Days
Ago" and most large organisations run on Workday, so unknown age is the normal
state for a large part of the target list until snapshots accrue.

## What is deliberately absent

**No location filter.** Delivery is remote; the location of a role does not
qualify or disqualify a company.

**No language filter.** Not applicable.

**No fit scoring.** Scoring belongs to a separate stage. Mixing it into
collection makes it impossible to re-score history when criteria change, which
is the reason the store keeps everything.
