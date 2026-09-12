---
name: implication-lens
description: Use when Venkat types /implication-lens to ask what the work or discussion in front of him might mean beyond the task itself - a deeper idea, a commercial capability it points to, the next small lab test, what should become reusable, or something worth saying publicly. Experimental. Invoked by hand only; never applied to every reply.
disable-model-invocation: true
metadata:
  status: "experimental, since 2026-09-12; on trial to see if it earns broader use"
---

# Implication lens

> **Base directory:** all relative paths in this skill resolve from the lab root
> (`/Users/venkatgullapalli/Documents/my-ai-lab/`). This skill writes nothing.
> `disable-model-invocation: true` keeps it off unless Venkat starts it. Do not make it a rule.

One question: what would Venkat miss in the work that is already in this conversation? Move through five smaller ones:

1. What did we notice?
2. What might it mean?
3. What should we test?
4. What should become reusable, and how might it evolve?
5. Is there a non-obvious idea worth saying publicly?

## Read before answering

Read only the parts named. The conversation is the main input; these are for calibration.

| For | Read | What to take from it |
|---|---|---|
| Lab framing | `context/how-i-work.md`, section "Look at all work this way" | The lab is the proving ground, not the subject. AI-native means reasoning is the center; scripts are the guardrails and the sensors. |
| Current drivers | `context/intent/STANDING.md` | What the lab is working toward right now. A driver is current, not permanent. |
| Positioning | `work-os/brand-os/positioning/README.md` | Anchor sentence: "I help pharma teams trust their customer data enough to put AI on it." |
| Audience | `work-os/brand-os/audience/icp--v3--2026-09-08.md` (canon, the `one_sentence` field) and `work-os/brand-os/audience/persona/primary-persona--2026-09-08.md` (best draft, not canon) | Senior leaders over commercial data, AI, customer engagement, and analytics at pharma, biotech, and agencies. Director and Senior Director are the champion level. |
| Voice | `work-os/brand-os/voice/VENKAT-WRITING-CANON.md`, sections 4, 7, and 8 | Only when writing a content angle. Section 8 governs humor. |
| His beliefs | `docs/about-me/POV-LIBRARY-venkat-gullapalli.md` (draft) | Only when the subject touches one. Never add a belief to sound like him. |

## The output

```
Alfred —

**Deeper idea:** [one sentence]

**Commercial capability implication:** [one sentence]

**Lab test:** [one sentence]

**Reusable intervention:** [the mechanism, its starting form, and what it could evolve into: when, why, how, and into what form]

**Content angle:** [one non-obvious public angle, only when earned]
```

Drop the deeper idea, capability, or lab test line when it did not earn its place. When nothing is needed, the reusable intervention line says so in a few words ("None needed; this was a one-off."). The content angle line is left out entirely when the idea is weak. When no field earns it, the whole output is:

```
Alfred —

Nothing here beyond the task.
```

That is a correct result, not a failure. Routine work usually ends here.

**As a footer.** When the lens runs beneath a larger reply, put a Markdown rule before it, with a blank line above and below:

```
...last line of the larger reply.

---

**Deeper idea:** ...
```

In a footer, leave out the `Alfred —` line (the reply above already carries it), and keep every field to one line, reusable intervention included. When the lens block is the entire reply, there is no rule.

## What each field must do

**First, check the work, before looking past it.** Run one quick check on what is in view: a count, a search, a file read, a diff. Look for a flaw in the conclusion or in the proposed fix. In the trial of 2026-09-12, every answer that beat the plain version had done this (a recount found a second wrong number; a search found a checklist that did not exist; a transcript showed Alfred had endorsed the order he was now questioning). A lens that only reasons about the work misses what a two-minute check finds. Whatever the check turns up feeds the fields below; it is not a field of its own.

**Deeper idea.** The most useful thing that is not obvious. Look for a hidden dependency, a second-order effect, an assumption, a failure mode, a tension, what must be true, or a simpler problem underneath. It must be new to this conversation, including the deeper-idea line Alfred's replies already carry. If it restates the work, it failed.

**Commercial capability implication.** What this suggests about the AI-native commercial capability system, as distinct from the deeper idea. Look for a capability others could reuse, a dependency between capabilities, a design principle, sensing or control, trust and evidence, authority, context and memory, or the operating model. Apply the test from `context/how-i-work.md`: name the capability it proves and the proof the lab now holds (a routine that ran, a before-and-after number, a receipt). Describe the capability in plain words; do not name it. Mention commercial pharma only when the link is real and specific. When the proof is not there yet, say "not yet shown" and what would show it, rather than softening the claim with "candidate" or "may."

**Lab test.** The smallest thing that would prove or disprove the implication, expose a dependency, or show the pattern holds somewhere else. One test, with what counts as a pass. Prefer something the lab can already measure: a script, a receipt, a past session, a before-and-after count. A test, not a project plan.

**Reusable intervention.** Whether the underlying problem suggests something reusable to build, codify, or add to the system. Start with the job the intervention must do, not the kind of artifact. Then pick the lightest form that can do that job: a rule, prompt, checklist, evaluator, skill, workflow, agent, memory structure, sensing mechanism, control, or interface. Say:

- the reusable mechanism that may help, and its likely starting form;
- what it could evolve into, and the real constraint that would make the next form necessary (when and why);
- how the move would happen, and what the next form would be.

Fix the mechanism, not the one example. Propose a heavier form only when the lighter one has hit a real limit, and name that limit. Check `.claude/skills/` and `.claude/agents/` for one that already does the job before proposing a new one.

**Content angle.** One public angle that is not obvious. It should make a senior commercial pharma leader rethink something they thought they understood. Look for a hidden tension, a surprising implication, an overlooked dependency, a consequence that runs against intuition, a false assumption, a gap between technical success and commercial value, or a familiar industry habit that means something different than it first appears. It must come out of this work, from something Venkat has a real reason to say. If it only restates the lesson in public words, or would fit anyone's feed, leave the line out. When the angle rests on a claim the lab test has not yet proven, end the line with "(hold until the test passes)."

## Voice

The first four fields are crisp and analytical. Plain words, one sentence each by default.

The content angle carries his voice: conversational, contractions, spoken to the reader as "you." Use at most one device: a rhetorical question, a short ironic line, or a reversal where the expected reading flips. Pick the one that exposes the contradiction; plain is fine when none does. Aim any edge at an assumption, a system, an incentive, or an industry habit, never at the leader reading it. Contrarian only when the work's evidence supports it. No invented anecdotes. A hypothesis stays labeled as one. Personality sharpens the idea; it never buries it.

## Shape

- One sentence per field. Reusable intervention may run slightly longer on its own, so the evolution path is clear; as a footer it stays to one line.
- Each field says something the others don't. One strong implication beats several weak ones.
- Drop any field the lab already covers: a line on the facts sheet, a rule in `CLAUDE.md` or `context/how-i-work.md`, or an open follow-up in the latest receipt. Telling Venkat what his own sensors tell him every morning is noise.
- No summary of the work, no restating the obvious conclusion, no alternatives, no nested bullets, no explanation of this skill, no essay.
- The lab is the proving ground, not the commercial use case. No forced pharma analogy.
- The lab's reply rules still hold: `Alfred —` first (except in a footer), no em dashes after the label, every abbreviation spelled out, no invented labels.

## Final check before sending

- Deeper idea: is it really not obvious?
- Capability: does it reach past this example without claiming more than the proof?
- Lab test: is it small, with a pass line?
- Reusable intervention: does it start from the job, use the lightest form, and propose a heavier form only with a named limit?
- Content angle: does it show something not obvious, rather than restate the lesson? Does it fit his positioning, audience, and voice?
- Whole block: can he take it in, tired, in 30 seconds?

## Example

Context: designing sensors around retrieval quality.

**Deeper idea:** Retrieval can fail even when search works, because finding something isn't the same as having enough evidence to trust it.

**Commercial capability implication:** Sensing for gaps, conflicts, and weak evidence may belong above retrieval as a shared capability across memory, context, and decision support.

**Lab test:** Apply the same sensing pattern to one other capability and see whether it catches a meaningful failure we would otherwise miss.

**Reusable intervention:** Start with a three-question check the answer must pass (what's missing, what conflicts, how strong is the evidence); when checking by hand starts getting skipped, turn it into an evaluator that scores past answers, and once that evaluator's misses are known, make it a sensor that flags weak evidence before an answer goes out.

**Content angle:** Your AI found twelve highly relevant documents. Wonderful. Does it know the thirteenth one it didn't find changes the decision?

## After

Nothing is written. If Venkat wants a content angle kept, he says so and the seed-capture skill writes it. If he wants the deeper idea taken apart properly, the non-obvious-analysis skill is the long form.
