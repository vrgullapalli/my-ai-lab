# Blind grade, round two (01:14 to 01:16)

After three fixes to the skill (check the work first; name the capability it proves and the proof held, no hedges; drop fields the lab already covers; "(hold until the test passes)"). Same five cases, same plain answers as round one, labels reshuffled. Key: **cases 1, 3, 5: A = skill, B = plain. Cases 2, 4: A = plain, B = skill.**

Verdict by the key: **the skill won 1 of 5 (case 3); the plain answer won 4.** The grader called all five "close." Trivial cases, skill only: 2 of 2 returned "Nothing here beyond the task." The grader's own text follows, unedited.

---

Grades below. Facts checked against the source files and a few scripts run now.

**Case 1: retrieval**
1. A: "'Not present' was close to guaranteed by the test's shape." B: "This test ran on the loudest week of the seven." B is more useful; its counts hold (EVERSANA 35, McKesson 16 on 09-04; zero on 07-31, checked by grep). A's "unacted for 13 days" and A-LIVE-187 both check out. Neither is wrong.
2. B's is sharper: "The first thing you'd sell a client isn't a feed. It's an afternoon writing down their bets." A's names real proof (2 of 3 by name match) but hedges the rest.
3. B's July 31 rerun is a real test with a pass rule, though it is a few hours, not one. A's is scripted and under an hour.
4. B's line is safe and holds it. A's "it's read the news" is sharp but generic.
5. B natural. A dense.
6. A caught the "search by meaning" gap and A-LIVE-187 miss. B caught the confound, which matters more.
7. B yes. A no.
8. B, because it tells him the result might be an artifact of the week.

**Case 2: memory and context**
1. A: "the build order that came with it breaks one of your own rules." B: same conflict, plus "a ruling touches two files, not one." Both true. A says the watch sits "fifth"; the receipt says fourth. Small slip.
2. B's four-question test is distinct and says "not yet shown." A defers it to "when you say next."
3. B's is runnable now, one routine, clear pass. A has none.
4. B's angle fits a pharma buyer of alerts. A holds the angle.
5. A natural. B stiff but clear.
6. B caught the two-file ruling. A caught the fix (retrieval as the watch's first step).
7. A yes. B borderline.
8. A, because it gives him one decision with a fix, but B's test is the better follow-up.

**Case 3: agent authority**
1. A: "eight live skill and agent files that still say... Never install globally." Confirmed, 8 files. B: "The checks watch paths, not words." Both true; A's is a live bug found now.
2. Both say the proof is thin. B's "files, words, and a test" is cleaner. A's is more honest about the missing sensor.
3. Both fine. B's replay of the 21:36 prompt is a sharp pass.
4. Both good. A's "Did anyone retire the sentence that tells your AI to use it?" wins.
5. B natural. A dense.
6. A found a second live instance. B found the follow-up with nowhere to land (no archive checklist).
7. B yes. A no.
8. A, because it found a second fault tonight that B did not.

**Case 4: architecture**
1. Both: the file promises a swap the code does not allow. B counts four files; my grep confirms all four (facts.py, waiting.py, open skill line 19, charter line 37). A counts three. Both cite facts.py line 342; the Telegraph line is 355 today.
2. A: "The honest claim is 'built to swap,' not 'swaps.'" Better than B.
3. Both runnable. B's is more precise.
4. B's "a few lines on your Monday deck" is fresh. A holds a decent one.
5. A natural.
6. A's "retire when" line is the non-obvious catch. B found the fourth file.
7. A yes. B no.
8. A, but B's count is the more accurate one.

**Case 5: routine fix**
1. Both: the 12 is the real error and it is 23. Confirmed by cron count: 23 plus 63 is 86. A adds "26 skills" vs 28 folders, confirmed. B adds the third whole-market read; I could not confirm the 7 AM run.
2. A's is cleaner: count from the source, not the hand.
3. Both under an hour. B's overlap check is a week.
4. A's "we typed the right one" is strong. B's is held.
5. B natural.
6. B caught the `_archive/` folder inside market-signals (it exists). A caught the skill count.
7. B yes.
8. B, because it found a rule break on the way.

**Tally:** A 3 (cases 2, 3, 4), B 2 (cases 1, 5). Close in all five.

**What separates them.** The stronger reply in each pair found one fact by running something now, then led with it: a grep count of company names, an `_archive/` folder, eight stale files, a fourth code file. The weaker one restated the source file at greater length or hid the fact inside a long bold-labelled block. Both formats can carry a real catch; the dense block hurts when tired, and the short one hurts when it skips the test.
