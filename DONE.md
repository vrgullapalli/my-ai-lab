> **Canonical.** This is Venkat's own definition of done, written 2026-08-11.
> It is the acceptance standard for the whole system (decision D-016). VISION.md
> says where we're going; this file says what "finished" means; DECISIONS.md
> settles conflicts. Change it the same way as any protected file: by explicit,
> recorded update — never silently.

# Chief of Staff OS: Definition of Done (ADHD-Native Version)

"Done" doesn't mean every feature exists. It means the system runs my work every day **without requiring the executive function I don't reliably have.** A system that works for a neurotypical user but needs me to self-start, remember to check it, or push through boredom is not done — it's a prototype that happens to compile.

**The loop stays the same:** Capture → Understand → Prioritize → Help act → Close the loop → Learn. What changes is the bar each step has to clear.

---

## 1. It knows me

The system understands who I am and operates on it as rules, not trivia:

- Who I am and the different roles I hold.
- What I'm working on, my priorities, deadlines, and constraints.
- My communication and writing style.
- Important people and relationships.
- What it may and may not do.

And specifically, how my brain works:

- My motivation runs on **interest, novelty, urgency, and stakes** — not importance.
- Task paralysis is real: knowing what to do and doing it are separate problems for me.
- Distant deadlines don't feel real until they're close (time blindness).
- I resist routine but need structure: **the frame stays, the picture changes.**
- I don't restart stalled work on my own — restarting is the system's job.
- Guilt and shame shut me down; a prepared next step starts me up.

And how my temperament works:

- I'm an introvert (INTJ). Visibility, self-promotion, and being on camera don't come naturally — but they're required for my goals.
- The system should treat "showing up publicly" as a real workstream it actively supports (see Section 8), not a personality flaw to nag me about.
- I do my best work in deep, private focus. The system protects that while making the public-facing work as low-friction as possible.

**Done test:** I never have to re-explain my brain or my temperament, and the system's behavior (not just its files) shows it knows this.

---

## 2. The daily briefing is an ignition system, not a report

The briefing tells me:

- What matters today.
- What's changed.
- What's at risk.
- What I'm forgetting.
- What needs preparation.
- What the system has already prepared.

And for me, "done" adds:

- **Exactly one recommended next action**, with the first step already prepared. Not "email the client" — the drafted email waiting for my edit.
- Short enough to read on a bad focus day. If I skim past it, it's too long.
- It reaches me where I already am (Telegram), because I will not reliably go open a dashboard.

**Done test:** On five consecutive workdays, the briefing got me to actually *start* something within a few minutes of reading it.

*(Whether that work also finishes on time is tested in Section 4 — a failed streak there points at loop-closing, not the briefing.)*

---

## 3. It remembers so I don't have to

The Chief of Staff OS uses four kinds of memory.

### Short-term memory

It remembers what's happening right now:

- What I'm focused on.
- Where I stopped.
- What changed today.
- What's waiting on me.
- What's waiting on someone else.
- What needs to happen next.

This memory should remain small, current, and easy to update. Outdated information should expire, be archived, or be promoted into long-term memory.

### Long-term memory

It remembers information that should remain useful over time:

- Decisions and why they were made.
- Commitments and follow-ups.
- Projects and their history.
- Important people and relationships.
- Preferences and working patterns.
- Corrections I've made.
- Facts, sources, and supporting evidence.

Every important memory should include its source, date, confidence, and whether it's a fact, inference, or assumption. New information shouldn't silently overwrite conflicting information.

### Procedural memory

It remembers how I did something before:

- The steps I followed.
- The tools I used.
- The prompts or templates that worked.
- Examples of the finished work.
- Shortcuts I discovered.
- What failed and why.
- What I would do differently next time.

Re-figuring out a process I've already completed is a major ADHD tax. "Here's how you did this in March, here's the template, and here's what you changed last time" is more valuable than most new features.

Each procedural memory records **when the method was last used and whether it still worked.** A stale recipe presented confidently costs more trust than no recipe — if a method hasn't been used recently or a tool has changed, the system says so.

### Transactive memory

It knows where knowledge lives, even when that knowledge isn't stored directly in the OS.

It should know:

- Which document contains the answer.
- Which person has the relevant expertise or authority.
- Which system owns the current record.
- Which agent or skill can handle the work.
- Which source is authoritative.
- When the information was last checked.

The OS shouldn't copy everything into memory. It should remember where to find the most reliable and current version.

Transactive memory about **people** falls under the same rights as everything else: I can inspect, correct, archive, or delete it, and it stays on the private side of the private-data/public-code separation. The public product ships with the capability, never with anyone's profile.

### Promotion between memory types

The system proposes promotions — short-term → long-term, completed work → procedural template — and **I approve them.** It never silently decides what's permanent. This keeps memory under the same governance as actions.

### How memory should behave

The system should:

- Retrieve relevant memory before asking me to repeat myself.
- Retrieve before creating something new.
- Bring back useful context without overwhelming me.
- Distinguish current state from historical information.
- Preserve sources and uncertainty.
- Record corrections so the same mistake isn't repeated.
- Show me how something was done previously when that would help.
- Know when it doesn't have the answer and where to look next.
- Let me inspect, correct, archive, or delete what it remembers.

### Done tests

Memory is working when:

- Resuming something from earlier today doesn't require re-explaining it.
- Restarting an old or stalled task takes minutes, not an afternoon of reconstructing context.
- The system can show how I handled a similar task before and retrieve the relevant template — and flags it if the method may be stale.
- Important decisions and commitments can be traced to their original sources.
- The system distinguishes facts from inferences and says when it doesn't know.
- It can identify the person, document, system, agent, or skill most likely to have an answer.
- Outdated or conflicting information is surfaced rather than silently treated as current.
- Promotions to permanent memory happened with my approval, not silently.
- Changing models doesn't erase the memory, because the memory belongs to the OS, not the model.

---

## 4. It closes loops — because I won't

This section matters more for me than any other. The loop-closing list — track commitments, detect slipping, verify what's still open, prepare next steps, recommend ship/block/kill, confirm approved actions succeeded, update records, bring work back at the right time — is exactly the executive function ADHD impairs. So the bar rises:

- Slippage detection is **assumed to be the only detection.** The system must not rely on me noticing anything is late.
- When something slips, it returns with **a recovery step attached and zero guilt framing.** No "this has been open for 3 weeks." Just: "here's the 10-minute version to get it moving."
- "The right time" to bring work back means **when it can feel like a now** — big deadlines are broken into small, near ones automatically, so work moves earlier without the system nagging harder.
- Restarts after focus loss are treated as a first-class workflow, not an edge case.

**Done tests:**

- A commitment I completely forgot about got closed anyway — and the return prompt made me act instead of avoid.
- **The work the briefing got me to start finished by or ahead of its deadline — not in a last-minute panic.** This is the outcome half of the Section 2 ignition test: starting is the briefing's job; landing on time is the loop's job. It connects directly to the "panic completions trending down" metric in Section 10.

---

## 5. It's trustworthy

The system:

- Never claims something happened without evidence.
- Never sends, publishes, deletes, spends, or commits without approval.
- Treats email, web pages, transcripts, and messages as untrusted input.
- Keeps private information out of public repositories.
- Logs important actions and decisions.
- Can explain why it made a recommendation.
- Fails safely when a model, connector, or source is unavailable.
- Supports undo, recovery, and rollback where possible.

Governance covers what the hooks can see. The root lock (`.claude/hooks/root-lock.py`) refuses new files at the lab root written through Claude Code's own tools. It cannot see writes made by a plugin, a connector, another program, or a shell outside a session (found in the 2026-09-10 rule audit; corrected 2026-09-14).

Plus one ADHD-specific guardrail:

- **Urgency yes, dread no.** The system may create real, near-term stakes (timers, mini-deadlines, check-ins) but never manufactures panic or piles on pressure. Dread is the fuel I'm trying to stop running on, and a system that makes me anxious is a system I'll stop opening.

**Done test:** After a month, I still open it willingly. Avoidance is a failed audit.

---

## 6. It works through Telegram

I can securely use Telegram to:

- Get my briefing.
- Capture a thought, task, or commitment.
- Ask what's on my plate.
- Request meeting preparation.
- Review pending approvals.
- Approve or reject a specific action.
- Check system status.

The reason is explicit: **capture must cost nothing.** A thought I can't dump in five seconds is a thought that's gone. Telegram is the zero-friction front door; my memory, policies, and authority remain inside the governed system.

**Done test:** Capturing a stray thought mid-task doesn't derail the task.

---

## 7. It can swap tools and models

I can:

- Add or replace a model without redesigning the system.
- Add a data source through a defined connector.
- Add MCP tools without giving them unlimited access.
- Add a skill without rewriting the main agent.
- Disable a broken connector without breaking the Briefing Room.
- Use faster models for routine work and stronger models for difficult judgment.

The architecture owns the workflow. The model is a replaceable component.

One note: a broken connector must degrade quietly. An error wall at briefing time is exactly the kind of friction that ends my streak of using the system at all.

---

## 8. It helps me show up publicly (the introvert's content engine)

I need visibility — videos, posts, a public presence — and it doesn't come naturally. The system treats this as a supported workstream with the same seriousness as any project, not something I have to white-knuckle.

### What it does

- **Separates the part I'm good at from the part that drains me.** I can think, write, and decide in private; the system handles as much of the packaging and publishing pipeline as governance allows.
- **Maintains an AI-assisted production path** so one input becomes public content through low-exposure methods, such as:
  1. **Avatar/likeness video** — I approve a script; an AI version of me delivers it on camera so I don't have to perform on demand.
  2. **Voice-first or faceless formats** — narrated video, screen-share walkthroughs, voice-cloned narration over visuals, where my thinking is the star and my face is optional.
  3. **Repurposing** — one deep piece of work (a doc, a talk, a long recording made in comfortable conditions) becomes clips, posts, and threads without me re-performing it.
- **Batches recording into sprints.** Instead of "be on camera regularly" (dread), it's "one 90-minute session produces two weeks of content" (a finishable mission — which also fits how my motivation works).
- **Keeps a content procedural memory:** what formats I've done, what scripts worked, my hooks, my visual templates, what performed — so every piece doesn't start from zero.
- **Finds the organic angle.** Content ideas come from work I'm already doing (this document is content), so putting myself out there never requires becoming a different person — just showing the work.

### Governance still applies

- Nothing publishes without my approval — publishing is a consequential external action like any other.
- Anything AI-generated in my likeness or voice exists only with my explicit approval per use, is logged, and is disclosed where disclosure is expected. My likeness is the most sensitive credential in the system.

**Done tests:**

- Public content ships on a steady cadence without me dreading it or the pipeline depending on my social energy that day.
- A single batch session reliably converts into multiple published pieces.
- I can point to content that exists *because* the system made the path low-friction — content that wouldn't exist otherwise.

---

## 9. It learns from me — including what moves me

When I correct the system:

- The correction is recorded.
- The related instruction or memory is updated.
- The change is tested.
- The same mistake becomes less likely.
- I can inspect and reverse the change.

It also learns from what recommendations I accept or ignore, how I complete tasks, repeated blockers, and changes in my priorities. Plus:

- It tracks **which motivational framings I respond to** — sprints, streaks, "beat yesterday," a witnessed check-in — and which I ignore, and adapts the briefing accordingly.
- It learns **which content formats and production methods I'll actually follow through on** (Section 8), and steers the pipeline toward those.
- It notices **when I go quiet.** Disengagement is data. The right response is to simplify and shrink, never to escalate volume.
- I can inspect what it's learned about my patterns, because being silently profiled — even accurately — erodes trust.

It shouldn't silently rewrite its own rules.

**Done test:** The system's second month works noticeably better than its first, and I can see why.

---

## 10. It delivers measurable value — with ADHD-native metrics

Baseline metrics:

- Reduces the time needed to understand my day.
- Decreases forgotten commitments.
- Improves meeting preparation.
- Reduces repeated explanations.
- Helps finish more important work.
- Reduces cognitive overhead.
- Produces fewer incorrect or unsupported claims over time.
- Saves more time than it requires to maintain.

Promoted to top tier:

- **Days I open the system but start nothing** — trending down. This is the single truest measure.
- **Last-minute panic completions** — trending down. Work moving earlier without the system nagging harder. (This is the metric the Section 4 done test feeds.)
- **Time to restart** stalled work — trending down.
- **Repeated explanations of myself** — near zero.
- **Public content shipped per month** — trending up, without a matching rise in dread.

And the master test: if the system is technically impressive but I avoid using it, it isn't done.

---

## Three practical definitions of done

### Private MVP done

The first private version is done when:

- My identity, temperament, and operating files are accurate.
- The governance rules are working.
- The briefing recommends exactly one next action with the first step prepared.
- The briefing has gotten me to *start* (not just read) five workdays running.
- Memory works across sessions, with tasks and memory separated.
- Slipped items return with a recovery step, not a guilt trip.
- Calendar access is read-only and reliable.
- Every important claim has a source.
- No external action can happen without approval.
- Telegram can deliver the briefing and capture information.
- The system can recover from a failed run.

This is the version I should build first.

### Operational v1 done

The operational version is done when:

- I've used it for approximately 30 real working days — including bad focus days. The system proved itself on the bad ones.
- The daily and weekly workflows work consistently.
- Customer Intelligence is useful and auditable.
- Follow-ups are reliably captured and closed — including at least one commitment I fully forgot that the system caught and closed.
- Work the briefing started is landing by or ahead of deadline; panic completions and "opened but started nothing" days both measurably declined.
- Corrections persist, and I can name a motivational framing the system learned about me.
- The content pipeline (Section 8) has produced published pieces from at least two batch sessions.
- Retrieval performance is measured.
- Connectors can fail without breaking the system.
- Logs, approvals, rollback, and recovery work.
- A second model configuration can run the core workflow.
- Maintenance is manageable.

At this point, the OS is a real working system rather than a prototype.

### Public product done

The open-source version is done when someone else can:

- Download or install it, and complete a guided setup **in one sitting, with value on day one** — a two-day setup is a setup I'd never have finished either.
- Understand what information is being collected.
- Customize its behavior without changing core code — including the **operating profile (ADHD, temperament, motivation style), which ships as a customizable template, not hardcoded assumptions.** The next person's brain runs on different fuel, and they configure theirs the way I configured mine.
- Connect their own tools safely.
- Learn why the system works.
- Test changes before promoting them.
- Update without losing personal customizations.
- Remove it and retain or delete their data.

It should include: clear documentation, setup and onboarding, templates, default skills and workflows, example data, security guidance, tests and evaluations, extension instructions, upgrade and migration support, and a clean separation between private data and public code — including all transactive memory about people and anything involving my likeness or voice, which never ship.

---

## The clearest finish line

The Chief of Staff OS is done when I open Telegram on an ordinary morning — including a bad one — and get a short, accurate briefing that catches what I forgot, hands me one prepared next step small enough to start *right now*, brings stalled work back without shame, keeps my public presence shipping without draining me, lands work by its deadline instead of in a midnight panic, and keeps everything consequential visible and under my control.

Not "it organized my work." **It got me moving, and the work landed on time.** That's the difference between a task manager and a Chief of Staff for a brain like mine.

Everything after that should be an improvement, not a requirement for the system to become useful.
