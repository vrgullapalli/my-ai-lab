# Current drivers

**What this file is.** The current drivers of the lab: what Venkat is working toward right
now. This is the one canonical definition. Alfred, the open routine, and the sensors read
this file to decide what to look at.

**What this file is not.** (Venkat's ruling, 2026-09-11.) These are not foundational
capabilities, not permanent pillars, and not what the architecture is built around. The lab
depends on the idea of changing drivers, never on these four. Any one of them can be replaced
without touching the machinery that reads this file. Telegraph+ can be swapped for another
product objective; the open routine, the duties, and the sensors stay as they are.

**The pattern each driver follows.**
Driver → current state or belief → evidence → threats and opportunities → next meaningful change.
Scripts establish the facts. The AI reads what the facts mean for each driver. Venkat is
interrupted only when something material changed. Adding, replacing, or retiring a driver is
his call (`.claude/agents/alfred/AUTHORITY.md`).

**How this file changes.** Append, never overwrite. To retire or replace a driver, add a dated
line saying so and why, and keep the old text under History. A driver that quietly disappears
teaches nothing. Four at a time is the cap (his word, 2026-09-08); it is a limit on attention,
not a design rule.

---

## 1. The lab notices and advances what matters without waiting for me

- **Kind:** a behavior of the lab. "Chief of staff" is one form of it. The capability is not
  wired to that metaphor.
- **Principle:** agency starts now. Authority grows over time.
- **Working when:** it surfaces or advances something material before I ask, with evidence and
  within its authority.
- **What a script can prove:** the gap since Alfred's last log line; whether an `OPEN` line was
  written on the day's first session; sessions that changed files and wrote no receipt
  (`facts.py open`, the facts sheet).
- **What would threaten it:** designing structure before anything runs · duties that depend on
  someone remembering to run them · Venkat being the one who catches problems first · a
  briefing that reports what he already knows.
- **State on 2026-09-11:** the open routine ran for the first time at 15:20. One session is
  unreceipted. Venkat caught two things first this week: the Gabriel label answering on its
  own (09-11) and a belief of his applied as an absolute in six places (09-10).
- **Next meaningful change (proposed, not ruled):** a watch that runs between sessions, not
  only at their edges. See `docs/reports/2026-09-11--ai-native-possibility-brief.md`, item 1.

## 2. My work survives the loss of any one machine

- **Kind:** a reliability invariant. It must stay true. It is never finished.
- **Working when:** a clean restore has been run and verified against the source.
- **What a script can prove:** repos with no remote, uncommitted and unpushed counts, snapshot
  age, off-machine copy age (`facts.py open`; `/context-check` section A). Not yet scripted:
  a restore run and diffed on a schedule.
- **What would threaten it:** the laptop and the iMac drifting apart with neither
  authoritative · repositories with no remote (six of eight on 2026-09-11) · brand-os and
  engagement-os invisible to the root repo because they are their own repos · the 1.6 GB no
  git backup covers · a backup nobody has restored from · two API keys in committed files
  that block pushing the lab root.
- **State on 2026-09-11:** last restore verified 2026-09-10 (7,185 files restored and diffed;
  one scratch file differed). Snapshot and Dropbox copy one day old. 98 files uncommitted in
  engagement-os, 31 at the root.
- **Next meaningful change:** the restore-and-diff becomes a scheduled sensor, so the invariant
  is measured, not remembered.

## 3. Telegraph+ becomes a product that changes a real belief

- **Kind:** the current product objective. Replaceable. When it is replaced, only this section
  changes.
- **Working when:** a real user changes a belief or decision based on intent evidence and can
  see how that belief changed over time.
- **What a script can prove:** unpushed commits in `work-os/projects/telegraph-plus` (the
  per-repo line on the facts sheet); "Needs Venkat" items and their age in
  `work-os/upskill-advisor/records/open-items.md` (the "Telegraph items needing Venkat" line;
  that sensor line belongs to this driver and retires with it).
- **What would threaten it:** drifting back into a pipeline, collect then process then reason
  at the end · building the evidence substrate before the reasoning runs · commits sitting
  unpushed · calling something done at stage two · the open question of whether
  `upskill-advisor` governs `telegraph-plus` (unruled since 2026-09-07).
- **State on 2026-09-11:** 11 commits unpushed. Two items needing Venkat, seven days old. No
  real user yet.
- **Next meaningful change:** the first belief that changed, with its history, shown to one
  real user.

## 4. Make my work visible enough for the right people to judge it

- **Kind:** an external outcome. Not a capability of the lab.
- **Working when:** a right-fit leader can see how I think from something public, and every
  material claim holds.
- **What a script can prove:** nothing yet. The claim-verification skill can check a finished
  asset by hand. Say so in every open routine until it changes.
- **What would threaten it:** claims he cannot support (two on LinkedIn on his list; four on
  the old site if it is still up, unchecked) · nothing shipping · building the system instead
  of doing the work.
- **State on 2026-09-11:** nothing published. Both finished assets were archived on 2026-09-10.
  One article is at gate 2.
- **Next meaningful change:** one public piece whose claims all hold.

---

## Deliberately not a driver

**Taxes.** Six figures and time-sensitive, but Venkat is handling it directly (his ruling,
2026-09-08). It is a task, not a direction. Alfred does not chase it.

**Everything else.** If everything is a driver, nothing drives anything.

---

## History

**2026-09-11 — reworded as current drivers at Venkat's word.** His ruling: the four are
"current drivers of the lab. They are not four foundational capabilities, permanent
architectural pillars, or four things the architecture should be built around. The
architecture should support changing drivers over time without needing to be redesigned."
Each driver's kind, working-when, and wording below are his. The sensor mapping moved here
from Alfred's `DUTIES.md` D1 so the duty stays generic. Nothing was removed; the 2026-09-08
text follows.

**2026-09-08 — opened as "Standing intent", approved by Venkat the same day.** Original text:

> What Venkat is working toward. **This drives what Alfred investigates.** Without it he
> can only check things somebody thought to put on a list.
>
> **The field that does the work is "what would threaten this."** It is not a risk register.
> It is where Alfred looks. When something on that list becomes true, that is the thing
> worth interrupting Venkat about.
>
> **1. A chief of staff that is proactive from day one.** Not earned, not phased. Agency
> starts now; authority grows over time. Threats: designing structure before anything
> actually runs · duties that depend on someone remembering to run them · Venkat being the
> one who catches problems first · a briefing that reports what he already knows. Working
> when: he learns something useful he did not already know, without asking.
>
> **2. My work survives losing a machine.** Recoverable and verified, not merely copied
> somewhere. Threats: the laptop and the iMac drifting apart, with neither being
> authoritative · eight repositories with no remote · the 1.6 GB that no git backup covers,
> recordings, private material, untracked folders · a backup nobody has restored from.
> Working when: a restore has actually been run and diffed clean.
>
> **3. Telegraph+ becomes a real product.** Pharma intent intelligence. The current line. Two
> predecessors failed and are kept for what they teach. Threats: drifting back into a
> pipeline, collect, process, then reason at the end · building the evidence substrate before
> the reasoning runs · seven commits sitting unpushed · calling something done at stage two.
> Working when: the first output is a belief that changed, with its history, not a report.
>
> **4. Public proof of the work.** Positioning, publishing, the site. Turning what he does
> into something other people can see. Threats: claims he cannot support · nothing shipping ·
> building the system instead of doing the work. Working when: something real is public and
> every claim in it holds.
>
> Deliberately not standing intents: taxes (his ruling, 2026-09-08), and everything else.
> Four is the cap until one is retired.
