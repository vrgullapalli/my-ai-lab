# TASTE.md — What Good Looks Like to Venkat

*What Venkat judges good, bad, or off, in writing, design, systems, and products.
Not ROOT.md (his five principles, held at a cost), not PROFILE.md (how to support
him), not DECISIONS.md (what is ruled). Rule of thumb: a principle he keeps even
when it costs him is a root; a preference seen in receipts is taste. He edits this
any time. Format adapted from the open TASTE.md spec (github.com/PitayaK/taste.md).*

**Hard cap: 150 lines.** Not arbitrary. It follows Anthropic's guidance on context
documents (Venkat, 2026-08-11). The cap does not move; the file fits inside it.
That is why entries are short rules and the proof lives in receipts.

---

## Rules of this file

**A line gets in only if it passes all three gates:**
1. **Observed, not imagined.** From a real accept or reject event: a quote, an
   edit he made, a choice between drafts. Never a guess at what he "probably" likes.
2. **Reversible.** The opposite has to be someone else's valid taste. "Values
   clarity" fails. "Evidence before narrative, even when the story would land
   harder" passes.
3. **Operational.** Name an output it would change, or cut it.

**Every entry carries:** signal label · date · **n** (how many times seen) ·
scope (where it applies) · **→** pointer to the receipt with the quote and story.

- `[explicit]` he said it · `[behavioral]` he chose it more than once ·
  `[inferred]` noticed but never stated (weakest, confirm or prune)
- **n=1 is a guess, not a rule.** Read every n=1 line as "once, so far."

**Maintenance:** prune entries not reinforced in ~3 months. A contradiction is
usually a missing condition, not a mistake, so park it in Unresolved instead of
forcing one side to win. Announce every update, never silent.

---

## Validation

- **Blind A/B, monthly.** Same artifact made twice, with and without this file.
  Venkat picks which sounds like him, blind. Target: 4 of 5. If he cannot tell,
  the file is not earning its space.
- **Rejection replay.** When he rejects a draft, did this file predict it? If no,
  the rejection becomes an entry.
- **Edit-trend.** Voice corrections per receipt should fall over weeks.

| Date | Test | Result | Action |
|---|---|---|---|
| 2026-08-11 | Seeded from first real accept/reject events | 6 entries, 1 pending | First A/B after ~10 receipts (loop #5) |
| 2026-08-24 | First blind A/B attempt (loop #5) — **directional first attempt, not a clean causal test** (his correction, same day). 5 pairs, two fresh same-model writers; the with-file arm received an embedded TASTE.md excerpt, not the literal file. Limitations on record: the control output existed before the answer key was committed; raw outputs reached the presenting session before the blind packet was shown; the key file was path-mangled at write; at least one with-file output altered supplied facts | Observed: 4 pairs "neither sounds like me" · 1 weak preference for the with-file version ("barely, maybe 15% like me"). Target 4/5 not met | His ruling: verdicts preserved as evidence for later research; no rejection replay, no voice-entry revision now. File thinness noted as a hypothesis, not a proven cause |

---

## Writing voice (constant across channels)
*(An entry moved out of here 2026-08-11 when he said it does not apply
everywhere.)*

- `[explicit]` 2026-08-17 · n=1 · **Contractions, a lot,** in his public
  writing. Stated directly while reviewing LinkedIn drafts. → experiment
  trace `traces/public-reasoning-simulation/2026-08-17-next-best-action-context/`
- `[explicit]` 2026-08-17 · n=1 · **",..." as a pacing device** — used
  strategically to move the story forward. His notation, verbatim.
  Sparingly: a device, not a tic. → same trace
- `[explicit]` 2026-08-17 · n=1 · **Witty, warm, contrarian, sarcastic wit
  paces the writing.** Sarcasm aims at situations and industry patterns,
  never at people (his no-bashing rule constrains it). → same trace
  **Relabeled an AIM, not a description — his ruling, 2026-08-24 (reading
  sitting, R3/R5):** the raw-voice run found 3 instances of humor and no
  sarcasm in 126k words of his professional speech; he confirmed that side
  of him lives with his wife and close friends ("maybe light irreverence"
  at work) and that he wants it in his writing anyway. The entry stands as
  a target for drafts, not as how he talks.

### Do / don't pairs
- 2026-08-11 · n=1 · Answering a status request you are not ready to answer.
  **Off:** "Before I confirm anything formally, can you tell me what your team
  needs?" **On:** "Everything on my end was completed in June… Could you confirm
  your team has both on file?" *Why:* the first asks a question and leaks
  caution; the second answers, gives away something free, and hands back the
  next move. → `receipts/2026-08-11-1848`

## Tone by channel (flexes)
- `[explicit]` 2026-08-11 · n=1 · **Careful reading them, relaxed writing back.**
  Hedging and clarifying questions both read as tells.
  **Scope corrected same day: everyone, always on.** Not just counterparties.
  People he knows, including clients and friends, have taken advantage before,
  so the watching never switches off for anyone. The starting assumption stays
  generous: benefit of the doubt first. → `receipts/2026-08-11-1848`
- `[behavioral]` 2026-08-11 · n=2, one thread · Same mode: cuts true things that
  would invite a reply he does not want. → `receipts/2026-08-11-1848`

## Structure & argument
- `[explicit]` 2026-08-11 · n=1 · **Scannable without losing words.** Structure
  earns its space, compression does not. Break into labelled lines rather than
  tightening the prose. → `receipts/2026-08-11-1848`
- `[behavioral]` 2026-08-11 · n=1 · **When a draft misses, show the menu of
  moves, not a silent rewrite.** Name the levers, then recommend one.
  → `receipts/2026-08-11-1848`

## Systems, code & product taste
*(empty)*

## Naming & vocabulary
**Reaches for:** (empty)

**Banned:**
- `[explicit]` 2026-08-11 · n=1 · **Em dashes.** Confirmed by him directly: "em
  dashes are my rule." Applies to anything written in his voice and anything
  written to him. Replace with a comma, a colon, parentheses, or a full stop,
  chosen per sentence. A blind swap for a hyphen degrades the prose and is not
  the fix. Flag any draft that uses one. → loop #18
  *(History, kept because it is the file's first worked example of the entry
  gate: the rule arrived from another session labelled `[explicit]` with no
  source, and was refused. The source turned out to be
  `reference/context-pack-v0.2.md`, which is written about him by a model, so it
  was refused a second time. It only became an entry when he said it himself.)*

## Anti-taste
- `[explicit]` 2026-08-11 · n=1, **independently confirmed 2026-08-24** ·
  **Hedging and visible caution.** A careful question in place of a plain
  answer is a tell. → `receipts/2026-08-11-1848` · Upgrade, his nod in the
  reading sitting (R3): the raw-voice run measured him hedging at roughly a
  quarter of the rate of everyone he talks to — the best-evidenced finding
  in 126k words (`evidence/research/raw-voice/VOICE-EVIDENCE-PACK-v1.md` §A.1).
- `[explicit]` 2026-08-11 · n=1 · **A category handed over as if it were a step.**
  "Book an hour with an attorney," said four times, never broken down. The
  complaint showed up as non-action. → `receipts/2026-08-11-1848`
- `[explicit]` 2026-08-11 · n=2 · **Absolute rules built from one instance.**
  "It's too early in the game to make absolute conclusions."
  → `receipts/2026-08-11-1848`
- `[explicit]` 2026-08-11 · n=2 · **Jargon, even when accurate.** Asked twice
  what a word meant. Full rule in `context/PROFILE.md → Reading level`.
  → `receipts/2026-08-11-1848`

## Unresolved — looks like a clash, condition not found yet
*A contradiction is usually a missing condition. Park it here instead of throwing
half of it away. Worked example from 2026-08-11: "be confident, not careful"
looked like it clashed with "he is very careful," until he said he is careful
when reading and confident when writing. Two modes, not one contradiction.*

- (none open)

## Adopted influences (per D-006)
*Enters only after it has been translated into his own version and seen working
in his output. Never copy wording, structure, or examples from the source.*
(empty)

## Aspirations (NOT observed taste)
*Kept separate so hope does not contaminate evidence.*
(empty)
