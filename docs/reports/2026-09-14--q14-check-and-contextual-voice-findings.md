# Two voice checks, 2026-09-14 (read-only; nothing in the lab changed)

## Check 1: does the Restart Q14 match his correction? (F-20260911-1510-10)

**Verdict: no.** The Restart Q14 is a different question. It does not touch the Q14 he corrected.

**His correction, in full.** `evidence/sessions/claude/199de402-e922-43fb-9c3f-e0fd256e11d0.md`, line 5291 (the rendered transcript has no per-message clock; the 01:12 time comes from the receipt):

> we're going to go through each question because some are fine and some are not. For example, 37 and 14 are not what I said or meant. Tell me what the final version of step one looks like.

**What he was objecting to.** The two readings Alfred had just given, same file, lines 5281 and 5282:

> - **Q37, gimmicks.** Hooks and carousels are the easy, safe choice for a feed. You do not trust the easy, safe choice. Same reason your tool picked the easy option at every step and you hated it.
> - **Q14, warmth.** You said a draft is warm when it sets the reader up first. Your building belief is the same: put the thinking in first. Where something starts decides what it can become.

**What the restart section is.** `docs/about-me/taste-interview--2026-09-09.md`, line 523 onward. The header and the question:

> ## Restart Q14 (Beliefs), 2026-09-11, 04:00
> **Alfred:** "So what do we do now?" sits there after every report. What is the smallest thing a brand team could do next quarter, with no new platform and no vendor, that would start closing the judgment gap? If the answer is "nothing without a system," say that.

His answer (lines 527 to 615) is about a one-page decision ritual and a quarterly test. It ends: "Deeper idea: before automating decision support, prove that a better decision process actually changes decisions." The restart re-numbered Section 1 (Beliefs) as Q1 to Q15, so "Restart Q14" is the fourteenth belief question, not a redo of the warmth question.

**The Q14 he corrected is still in as written.** Original at line 800 of the interview file, "## Q14 (Voice)". The reading he rejected is still in the profile, `docs/about-me/VOICE-PROFILE-venkat-gullapalli.md` line 1108: "His definition of warmth is not tone. Warmth is context. A draft is cold when it makes the point before the reader is set up to receive it. **STRONG TENDENCY.**" The same session later called "warmth is context" a settled "voice fact, already in the profile" (transcript line 6734).

**Q37 has no restart.** No "Restart Q37" header exists in the interview file (checked with grep). The gimmicks answer stands unchanged at interview line 990 and profile line 1296 (labelled Q84 there). Still owed, as the receipt says.

**What is not on record:** what he meant instead. His message names the two numbers and nothing more. Both questions need a fresh answer from him, not a rewrite by Alfred.

## Check 2: findings 2 to 5 on the contextual-voice skill (F-20260913-0540-5)

The skill reads only two files: `SKILL.md` line 16 says read `references/voice-core.md` "for stable voice rules" and line 17 `references/context-dials.md`. A third file, `references/contextual-voice-core.md` (477 lines, built from the profile on 09-11), sits in the folder but nothing in `SKILL.md` points at it. The findings below are about what the skill actually loads.

**Finding 2, it rewrites its own rules. Holds.**
Evidence: `voice-core.md` is a stand-alone rulebook. Line 18: "Use plain, everyday language at roughly an 8th- to 10th-grade reading level." Line 26: "Never use em dashes. Avoid semicolons." A grep of `SKILL.md`, `voice-core.md`, `context-dials.md`, and `evidence-updates.md` for "canon", "VOICE-PROFILE", "about-me", "my-voice", or "brand-os" finds nothing. The canon and profile are never named.
Fix: replace the rules in `voice-core.md` with a pointer to `work-os/brand-os/voice/VENKAT-WRITING-CANON.md` and the profile, keeping only what is not already there.

**Finding 3, it drops the truth rules. Holds; six of seven are missing.**
The canon's Tier 1, `VENKAT-WRITING-CANON.md` line 57: "Seven items. A script may block on these. They are about truth and trust, not style." Items 1 and 2 (lines 58 and 59): "Never invent a personal experience, fact, quote, memory, emotion, evidence, or certainty." and "The voice pass never changes claims, evidence, confidence, personal facts, or refusals." Also item 3, "The edge is never aimed at the reader or at a person."
In the skill, only item 7 (no em dashes) appears, `voice-core.md` line 26. The nearest thing to the rest is `SKILL.md` line 22, "Do not add stronger claims, certainty, wit, or contrarianism than the evidence earns," and `voice-core.md` line 58, "Do not let a polished sentence outrun the evidence." Neither bans inventing, changing claims, or aiming at a person. A grep for "invent" in the two files returns nothing. "Never name a client" is also absent (profile line 1286, HARD RULE).
Fix: add the seven Tier 1 items to `SKILL.md` as a "never" block, quoted from the canon, above the drafting priorities.

**Finding 4, softer than the pick-a-side ruling. Holds, with one line in its favour.**
The ruling, profile line 1146: "**RULING:** write the firmer Venkat. Picks a side and stays on it. Some post types still show both sides." His words, line 1142: "the firmer me that I say I need to be is the one who picks a side and stays on it."
The skill never says pick a side. `voice-core.md` line 5: "skeptical without performing contrarianism, and confident without pretending certainty." `SKILL.md` line 39: "Prefer a precise question over an inflated declaration when the evidence is incomplete." The one line that leans firm is `voice-core.md` line 60: "Do not manufacture balance when the evidence points clearly one way." That is a rule against fake balance, not a rule to take a side. The unwired core file does have it, line 419: "Grant the other side first, then pick a side."
Fix: add the ruling, quoted, to `voice-core.md` under "Evidence and judgment", with the exception for post types that show both sides.

**Finding 5, it covers 5 of 12 kinds of writing. Holds; the count on the other side is 12 or 13.**
The skill's five, `SKILL.md` line 3: "long-form articles, Field Notes, executive writing, website copy, and casual messages." `context-dials.md` has exactly those five sections (lines 5, 18, 31, 44, 57).
The `my-voice` skill, `SKILL.md` line 3, names twelve: "LinkedIn posts and comments, Substack articles and notes, website copy, emails, DMs, proposals, bios, talk scripts, recommendations, texts, instrument readings." Its `references/media/` folder holds 13 files (the twelve plus `interview.md`). Only website copy is in both lists by name. LinkedIn posts, the kind he writes most, have no dial in contextual-voice.
Fix: either add dials for the missing kinds, or say in `SKILL.md` line 3 that `my-voice` owns the other kinds and this skill covers only these five.
