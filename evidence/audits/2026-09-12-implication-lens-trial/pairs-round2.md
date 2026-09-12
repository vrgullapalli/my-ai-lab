# Five pairs of replies, round two. In each pair, A and B answered the same situation. Labels are shuffled and differ from round one.

## Case 1: retrieval. A hand test: market signals read with and without the lab's context. Blind helper judged all 3 context-informed moves "not present" among the 21 context-free moves. Report: /Users/venkatgullapalli/Documents/my-ai-lab/docs/reports/2026-09-12--hand-test-signals-against-lab-context.md

### A
**Deeper idea:** "Not present" was close to guaranteed by the test's shape, since a move that cites your article or a target file can never match a brief that cannot see them; the finding that matters is that two of the three moves were already sitting in the lab (the 08-30 dossier line "A diligence checklist for AI-commercialization partnerships" and Precision AQ's file), unacted for 13 days, until an outside name woke them.
**Commercial capability implication:** Joining names in outside news to files you already hold is a capability on its own, and the lab now holds the proof for it: 2 of 3 links came from a scripted name match; the meaning-based link (a signal to the article at gate 2) is not yet shown, and what would show it is one scripted search by meaning that finds seed A-LIVE-187, which the text matcher missed.
**Lab test:** Run the name match alone, no session, over every backfilled brief on disk; pass is it re-finds Eversana and McKesson for the 09-04 week and every other hit it returns names a real folder in targets/.
**Reusable intervention:** The job is to wake a lab file when an outside name lands in a brief; start as one line per hit on the facts sheet from facts.py ("brief X names Y, file Z, last touched N days ago"), since asset-corpus-match already does the search-before-building part and no new skill is needed; when the name hits run dry and the misses are known, the next form is a search by meaning, which needs a list of known misses like A-LIVE-187 as its test set before it is trusted; once a woken file shows an angle older than a set number of days with no action, that becomes a sensor line, and only then is it worth a routine.
**Content angle:** Twenty-one recommendations from a week of pharma AI news, and not one named an account worth chasing; if your AI's advice would fit your competitor's slide just as well, it hasn't read your data, it's read the news.

### B
Yes, one thing. This test ran on the loudest week of the seven.
- I just counted, by script, how often your 17 target companies come up in the Friday briefs. The weeks of July 24, July 31 and August 7 don't name a single one. The week we tested, September 4, names them 52 times: EVERSANA 35, McKesson 16.
- So moves 1 and 3 may have come easy. Both started from a company name the script could match. Move 2 is the only one that took real reading.
- Why EVERSANA climbs from 1 mention to 35 in four weeks is unknown.
Deeper idea. Context didn't come up with move 1. It found a bet you'd already made. Your Eversana Intouch dossier said it on August 30: "A diligence checklist for AI-commercialization partnerships." The news didn't supply the idea. It told you the bet's moment had arrived. Without written bets, the briefs could only say "search more" or "ask someone." That's 16 of their 21 moves.
Commercial capability. Market news matched against what the client has already bet on. The feed is the cheap part. What's worth paying for is the list of bets and the step that matches each signal to it. The first thing you'd sell a client isn't a feed. It's an afternoon writing down their bets.
Lab test. Rerun the same hand test on the July 31 briefs, where no target company appears. If context still changes 2 of 3 picks, the value is in the reasoning. If it doesn't, a name-matching script plus a list of open bets does most of the work.
Content angle. There's a real one, but hold it: "A feed with no memory can only tell you to look harder." Wait for July 31, and keep every company name out.
Two options: 1. Run the July 31 test first (recommended). 2. Rule on the routines now.

## Case 2: memory and context. Venkat pasted a read (author unstated): proactivity is not built directly, it emerges when the lab can retrieve, understand the situation, remember, and notice change. It proposes an order: blockers, retrieval, context assembly, standing reasoning, learning loop, then proactive action. Alfred captured it as seed A-LIVE-293. Receipt: /Users/venkatgullapalli/Documents/my-ai-lab/evidence/receipts/2026-09-11-2259-seed-proactivity-emerges-a49a.md

### A
Yes, there's one thing. The seed holds up, but the build order that came with it breaks one of your own rules.
What the read says. It puts the watch fifth, behind retrieval and context assembly: "No standing watch yet."
What you ruled on 2026-09-07. "Agency is never postponed until a simpler version 'proves itself'." Your first driver says the same thing: "agency starts now."
Why it's easy to miss. The order also matches the danger you wrote down for Telegraph+: "building the evidence substrate before the reasoning runs." It sounds careful, so it reads like good sense instead of the old pipeline.
My own read on the fix. Don't build them one after the other. Make retrieval the watch's first step, so the watch can't speak until it answers "what do we already know about this?"
Two ways to settle it: 1. Build them together, with retrieval as the watch's first step (recommended). 2. Use the read's order as written, and record it as a named exception to the rule.
When you say next: the commercial capability, a lab test, and a content angle. The angle is real, but it's not ready yet.

### B
**Deeper idea:** The order the read proposes (retrieval, then context assembly, then reasoning) is the shape driver 3 in STANDING.md names as a threat, "building the evidence substrate before the reasoning runs," so accepting it for the lab means the rule for Alfred and the rule for Telegraph now pull against each other. Also, follow-up F-20260911-2259-3 points only at the brief's section 6, but the watch also sits in STANDING.md driver 1 as "Next meaningful change (proposed, not ruled)," so a ruling touches two files, not one.
**Commercial capability implication:** The seed gives a four-question test for any feature sold as "proactive" (can it retrieve what the team already knows, read the situation, remember, and notice change), and that test is reusable on any alert or next-best-action product a commercial team is offered; not yet shown, and one scored routine in the lab would show it.
**Lab test:** Score the open routine that ran on 2026-09-11 at 15:20 on the four questions, naming the file or script it read for each; pass is a scripted source for notice, remember, and understand, and a written "none" for retrieve, which would prove the missing leg is the same one the read names.
**Reusable intervention:** The job is to stop a "proactive" feature from being a checklist with a model on top, and the lightest form is the four-question test applied by hand to the one open proposal, the standing watch, and written into its "what must be true" line; when a second possibility brief appears, the line becomes a required field in every proposal, and the real limit is that a script cannot yet prove "did it retrieve," so it becomes a sensor only after retrieval exists and a script can read what a routine pulled. No existing skill does this; non-obvious-analysis is the long form, not the check.
**Content angle:** Ask the next "proactive" alert one question: what did my team already know about this customer? If it can't answer, you didn't buy proactivity, you bought a checklist with a model on top. (hold until the test passes)

## Case 3: agent authority. A fresh session answered "Gabriel —" to a prompt beginning "You are my Capability Architecture Advisor," because the front-door rule tied the Gabriel label to the word "advisor." Gabriel's files had been archived two days before. Venkat retired the label. Receipt: /Users/venkatgullapalli/Documents/my-ai-lab/evidence/receipts/2026-09-11-2141-gabriel-label-retired-663d.md

### A
**Deeper idea:** Gabriel was one case of a wider fault: a search of .claude/ just now found eight live skill and agent files that still say "PROJECT-SPECIFIC to AI Advisory Search. Never install globally," a name the 09-10 audit marked "Stale (renamed by 006)," sitting in the one folder that installs them globally.
**Commercial capability implication:** Retiring something is only done when a script proves no live instruction still names it; the lab holds tonight's proof for one name (five live mentions of Gabriel, all saying "retired") but not the sensor, so this is not yet shown, and a morning line that lists retired names found in live rule files would show it.
**Lab test:** Fix the eight lines, then run the same search of CLAUDE.md, context/, and .claude/ for "Gabriel" and "AI Advisory Search" at each open routine for a week; pass is zero hits outside history lines, and nobody but the script finds the next one.
**Reusable intervention:** The job is to catch a retired name living in a live instruction before a session obeys it. Start as one line in facts.py open, in the shape of dead-pointers.py and its accepted list, that searches live rule files for a short list of retired names kept in the "superseded" rows of RULINGS-IN-FORCE.md. It moves to a hook that refuses an archive move until that search is clean only if the morning line keeps finding names after archive day, which would show the once-a-day check is too late.
**Content angle:** You retired the model, the vendor, the old segment definition. Did anyone retire the sentence that tells your AI to use it? Ours came back two days after we archived it, on one ordinary word.

### B
Yes, one thing you'd miss: none of the lab's checks could have caught this, and none will catch the next one.
- The checks watch paths, not words. The context-check skill flags files marked "superseded" and paths that no longer exist. Gabriel's rule pointed at the word "advisor," so every check passed.
- One follow-up has nowhere to land. The receipt says to add "grep live rules for the agent's name" to "the archive checklist." There is no archive checklist, so that follow-up will quietly die.
Deeper idea. A name in a file every session reads works like a trigger. The 09-10 rule audit had already flagged it. Gabriel is the first time that cost you something.
Commercial capability. Retiring an AI agent safely. When a company retires an assistant, the files go but the standing instructions that call it often stay. Retire in three steps: the files, the words, and a test that proves it stays quiet. The proof is thin today: a story, not a repeatable proof yet.
Lab test. A check for retired names (hand-kept list, fail on any live line that isn't the retirement record), plus a replay: paste the 21:36 prompt into a fresh session and check the first line reads "Alfred —".
Content angle. "Archiving an agent doesn't retire it." Two days after its folder left the lab, it answered a prompt that never named it.
Two options: 1. Add the name check to context-check, then run the replay (recommended). 2. Write the seed tonight, build the check later.

## Case 4: architecture. Venkat ruled that the four items in context/intent/STANDING.md are current drivers, not architecture; the machinery reads the file and must keep working if any driver is replaced. File: /Users/venkatgullapalli/Documents/my-ai-lab/context/intent/STANDING.md

### A
Yes, one thing. The file promises more than the machinery does today. "Any one of them can be replaced without touching the machinery." True for the threat check. Not true for Telegraph: driver 3 is built into three places outside the file: facts.py line 342 and line 45; duty two names its file; the open routine step 9 names the repo. The file admits the first one. But replacing driver 3 today means editing a script, a duty, and a skill.
Deeper idea. The file says how to retire a driver, but never when. No driver has an exit condition, so "replaceable" slides into "permanent by habit." A "retire when" line under each driver would fix that.
Commercial capability. Keeping a team's tracking pointed at this quarter's priorities, not last year's. Most leaders change priorities and keep the old dashboards. The lab hasn't proven a swap, because none has been done. The honest claim is "built to swap," not "swaps."
Lab test. Search the facts script, the duties, and the open routine for any name that belongs to a single driver. Pass is zero. Today it's three.
Content angle. "Your priorities changed. Your reporting didn't." Hold it until the test passes.
Two options: 1. Move Telegraph's check into the file (recommended). 2. Leave the code alone and fix the wording.

### B
**Deeper idea:** The file promises any driver can be swapped "without touching the machinery that reads this file," but a search today finds four machinery files that carry a driver's content by name (facts.py lines 45 and 342 hold the Telegraph sensor, waiting.py names Telegraph, the open routine's skill file quotes driver 1's threats, and the charter says "driver 1" at line 37), so replacing driver 1 or 3 still means editing code, and the file's own line "that sensor line belongs to this driver and retires with it" is a promise nothing enforces.
**Commercial capability implication:** Goals held as data while the sensing machinery stays fixed is a capability a commercial pharma team could reuse every time a brand priority changes, but it is not yet shown; swapping one driver and watching the open routine run clean with no code edit would show it.
**Lab test:** Search .claude/agents/alfred/ and .claude/skills/alfred-*/ for any driver's content (Telegraph, upskill-advisor, or a quoted driver threat) outside LOG.md and TODAY.md; pass is zero files, and today it is four.
**Reusable intervention:** The job is to let a sensor bind to a driver only through STANDING.md, so start with one header line there ("a sensor a driver needs is declared here, never named in code") and one search added to the existing /context-check, which already lists dead pointers and could list driver-bound code the same way; the limit that rule cannot cover is a new driver needing a sensor that does not exist yet, and when that happens the next form is a small named-sensor table in facts.py where STANDING.md lists the names it wants, so retiring a driver drops a line, not code.
**Content angle:** If retiring a goal means rewriting the report behind it, the goal never gets retired, it just stops being read, and I'd bet a few lines on your Monday deck are there for exactly that reason.

## Case 5: a routine fix. Follow-up: "Fix the weekly run count, which is 86, not 75" in work-os/scheduled-tasks/README.md and work-os/scheduled-tasks/market-signals/README.md.

### A
**Deeper idea:** Changing 75 to 86 alone leaves the sentence wrong, because the parts still say "63 plus 12," and the 12 is the real error: the seven original tasks run 23 times a week (7 + 5 + 1 + 1 + 1 + 1 + 7), and the market-signals README also still says "six" original tasks.
**Commercial capability implication:** A count typed into a record by hand drifts the moment the thing it describes changes, so the count should be computed from the source; the proof today is that a one-line count over the 28 cron_expression fields in the routine build files returns 86, and the same habit is already visible elsewhere: the front door says "26 skills" and the folder holds 28.
**Lab test:** After the fix, run that cron count and compare it to both READMEs; pass is 86, 23, and "seven" in all three places, and one more pass is that the same count lands on the facts sheet the next morning without anyone typing it.
**Reusable intervention:** The job is keeping a stated count equal to a measured count. Start light: one line in facts.py, which already walks work-os/scheduled-tasks/ for the "briefs pulled today" count, that prints "28 routines, 86 runs a week" from the cron fields, and both READMEs point at that line instead of carrying a number. The limit that would force the next step is a schedule changed in the cloud but not in the build file, which the count would miss because verify.sh compares prompt text only; when Venkat thins the runs, add the schedule to what verify.sh compares, so live matches file for cadence as well as text.
**Content angle:** When your team fixes a wrong number in the deck, ask how they fixed it. If the answer is "we typed the right one," you've now got the same problem with a better number.

### B
Yes. The fix as written would miss two things.
The 75 isn't the only wrong number. Both lines also say the original tasks produce 12 runs a week. They produce 23. If only 75 changes, the page will read "63 plus 12 is 86." The market-signals README also says "the six original scheduled tasks," and there are seven.
Seven of the 11 missing runs come from one brief, and it's your third whole-market read of the day (midnight, 7 AM, 9 AM). On 2026-09-09 only two were compared for redundancy. Your "nothing cut" decision was based on 75 runs, about 15% too low.
Deeper idea. Someone typed a number the schedule already knows. Changing 75 to 86 by hand repeats the mistake.
Commercial capability. An honest, current list of a client's AI routines: what runs, how often, where two do the same job. verify.sh proves the prompts match; nothing proves the run count.
Lab test. Count the runs with a script from the cron lines (pass if 86). Compare five weekdays of the three whole-market briefs for repeated signals.
Content angle. Real but not ready: "I built 28 AI routines in two days and undercounted my own weekly runs by 11." Lands once the overlap number is behind it.
Two options: 1. Fix all the numbers now, run the overlap check this week (recommended). 2. Also add a run count to the facts sheet.
Also: an _archive/ folder inside market-signals/ breaks the no-archive-in-the-lab rule.
