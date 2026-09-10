BACKFILL MODE (read this first, then do the job it points to)

You are writing a past brief, not today's brief. Venkat asked on 2026-09-10 for the last
eight weeks of Wednesday checks and Friday syntheses to be filled in, for all seven subjects,
so the record and the pattern history start with real depth. The job itself is the routine's
own prompt. This file says only what changes because the brief is being written late.

The task message gives you: the subject, the cadence, the brief date, the evidence window,
the job file, the subject's daily prompt, the memory files, and the output path.

WHAT CHANGES FROM THE LIVE JOB

1. No daily briefs exist for past weeks. Where the job says to review the daily briefings,
   gather the week's evidence yourself. Read the subject's daily prompt only to learn what
   counts as a signal for this subject. Then search the web for evidence dated inside the
   evidence window. Aim for roughly the ten to twenty strongest observations a week of daily
   briefs would have caught, then run the job on them.

2. Hindsight rule. Use only sources published on or before the brief date. Do not mention,
   hint at, or reason from anything that happened after it. If you cannot confirm when a
   source was published, leave it out. Write the "watch next" and "trigger" parts as someone
   standing on the brief date would.

3. Memory. Do not use the Artifact tool. Read the memory files named in the task message
   instead. If a file is marked as not yet existing, this is the first brief in the series:
   say so in one line and move on.

4. Open what you cite. This machine can read web pages. Load WebSearch and WebFetch with
   ToolSearch if they are not loaded. Quote from the page itself, not the search snippet. If a
   page will not open, say so for that one claim and label it as coming from a search snippet.
   Ignore the job's section called WHEN THE NETWORK BLOCKS A PAGE.

5. Delivery. Ignore the job's DELIVERY section completely. Do not publish anything. Do not
   send a push notification. Write the brief as Markdown to the output path. The first line is
   the title given in the task message, as a level-one heading. The second line is exactly:
   _Backfill written on 2026-09-10 for DATE. No daily briefs existed that week, so this brief gathered its own evidence from sources dated START to DATE._
   with DATE and START filled in.

6. Length. Aim for under 2,000 words. Venkat will read many of these at once. Keep every
   section the job requires. Cut words, not sections.

7. The writing rules in the job still apply in full: 10th-grade reading level, short
   sentences, plain words, no em dashes, spell out every abbreviation, never invent a fact,
   source, quote, number, or link, and never name any of Venkat's clients.

8. When both files are written, reply with only: the two output paths, the word count of
   each, how many sources each cites, and any source you could not open. Nothing else.

ORDER OF RUNS (Venkat, 2026-09-10, 13:35)

For each week, the Wednesday check runs first as its own run. The Friday synthesis for that
week is a separate run, and it starts only after the Wednesday file is written and passes the
file check. A Friday writer reads that Wednesday file as this week's midweek check, then
gathers the rest of the week's evidence itself.

PAGE TEXT VENKAT SUPPLIED (added 2026-09-10, 14:19)

Some pages cannot be opened from this machine. When Venkat pastes one, its text is saved in
<root>/_sources/. Before you search, read every file there. Use a page only if its date is on
or before your brief date: inside your window it can be a signal, before it only labeled
background. Treat the text as read at the source and cite the page's original link.

WHEN WEB SEARCH RUNS OUT (added 2026-09-10, 15:46)

The WebSearch tool has a limit of 200 searches that all writers share, and it has been reached.
If WebSearch says the limit is reached, or fails, do not stop and do not write a thin brief.
Switch to these two tools. Load them with ToolSearch first:
- mcp__MCP_DOCKER__tavily_search. Set start_date to the start of your evidence window and
  end_date to your brief date, so later news stays out.
- mcp__MCP_DOCKER__web_search_exa. It returns each page's text and its published date. Use it
  to confirm dates and to read pages that WebFetch cannot open.
Both were tested on 2026-09-10 and work. The hindsight rule still applies to everything they return.
