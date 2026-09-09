# Instrument Pattern Library — v1

> Ruling 22 (Venkat, 2026-08-31): the design library is organized by
> **purpose-named instrument patterns, never atomic primitives.** A
> pattern is named for the job it does in a decision experience and
> defined by its rules under the AI-Native Executive Instrument Design
> Standard (same directory). Reference implementation for every v1
> pattern: the built AS-006 instrument
> (`assets/releases/AS-006/instrument/` — template, tokens, and
> behavior), proven through cold review.

Visual ground for all patterns: the site tokens (warm paper, ink,
clay, gold; serif display, sans body, mono chrome). Epistemic visual
grammar, used identically everywhere: **solid = evidence · dashed gold
italic = the user's assumption.** No pattern may repurpose that
grammar.

---

## Recognition Header
**Job:** make the intended person think "this is the situation I'm in"
within three seconds (standard §5.01).
**Anatomy:** one serif headline naming their lived moment in their
words + one sentence of tension. No category language, no method, no
credentials.
**Rules:** second person allowed when naming their situation, never
their competence. Follows the one rule: examination points outward.

## Promise Line
**Job:** state the outcome and the cost before any interaction
(§5.02–03): what they'll know, and roughly how long it takes.
**Anatomy:** one bold sentence — outcome, never mechanism.
**Rules:** must be literally true of the instrument below it.

## Instrument Frame
**Job:** make the tool read as a bounded device, not page content
(ruling 20a: "distinct, closed off, a border").
**Anatomy:** 2px ink border + offset shadow; inverted nameplate strip
(mono, uppercase) carrying the instrument's name and its honest
figures; internal regions separated by hairlines.
**Rules:** the frame carries 60–80% of the initial visual weight;
everything outside it is quiet context. **The frame is the embeddable
unit** (Venkat, 2026-08-31: "it must be embeddable"): everything inside
the border must work when dropped into any host page or iframe —
styles scoped so nothing leaks in or out, no full-viewport
assumptions, functional at container widths down to ~320px, no
dependencies beyond its own markup. The page layers (recognition,
promise, interpretation, door) belong to the host, never to the embed.

## Status Readout
**Job:** the system's current judgment, legible in under one second
(§3.3, widget clause).
**Anatomy:** sticky panel: a mono STATE line with a gold state edge
(solid = active concern, dashed = withdrawn-on-assumptions), the full
authored sentence one tap below ("the reading ▾"), reserved-height
delta line beneath.
**Rules:** sticky region stays under ~150px on phones and never grows
on interaction; every state string is authored, none assembled.

## Verification Gauge
**Job:** show exactly what would end the concern — falsifiability as
UI (§7.2).
**Anatomy:** caption ("Ends when both are verified:") + one chip per
exit condition, named in plain words; chip flips to assumed treatment
when stipulated.
**Rules:** the caption is a state, not a constant; chips never show
raw IDs.

## Evidence Tag
**Job:** carry the claim vocabulary — verified / claimed / inferred /
unknown / assumed-for-the-challenge — on any element (§7.2).
**Anatomy:** small mono chip; verified = solid ink inverse; assumed =
dashed gold italic; others = outline.
**Rules:** grounding one tap away; never collapse categories.

## Condition Row
**Job:** one challengeable condition as a compact control (§3.3: one
cognitive job).
**Anatomy:** short name (bold) + Evidence Tag + ONE action button;
a single disclosure beneath ("What this means, and what would settle
it") holding the full statement, why-it-matters, falsifier, grounding.
**Rules:** exactly one action per row; 44px targets; row treatment
flips whole-card to assumed grammar when stipulated; the action's
label is executive speech ("Take this off the table" / "Put it back").

## Reading Response
**Job:** answer every user move with what changed — including honest
nothing (§3.5 information gain; §5.06).
**Anatomy:** one authored sentence in the Status Readout's delta slot;
null moves state outward-pointing why ("unification never depended on
this").
**Rules:** appears where the eye already is; never a full re-render;
focus and open disclosures survive.

## Refusal Case
**Job:** make declining-to-challenge a witnessable state — the
credibility anchor (§7.3, refusal as designed state).
**Anatomy:** one disclosure: the refusal verdict, its evidence basis,
one closing line ("a challenge only means something from a judgment
that can decline").
**Rules:** refusal differs on evidence, never on size or spend.

## Room Card
**Job:** the portable result — usable in a meeting by someone who
never saw the page (§5.09).
**Anatomy:** plain-text block: claim, verdict AS EVIDENCE STANDS, the
one question for the room, what would change the reading, date; user
assumptions quarantined under their own header with a conditional
reading.
**Rules:** copyable as plain text; never carries an assumption as a
finding; no instrument vocabulary inside.

## Reassurance Note
**Job:** answer the trust question at the moment of friction (§6.6).
**Anatomy:** one small line beside the interaction ("Runs entirely on
this page; nothing you do here is sent or stored").
**Rules:** must be mechanically true — backed by a test, not a claim.

## Interpretation Block
**Job:** after the experience, say why it mattered (§5.07) — never
before.
**Anatomy:** 1–3 quiet sentences translating the finding into
consequence and pattern.

## Door
**Job:** the continuation once value has landed (§5.09–10): specific,
pressure-free.
**Anatomy:** one line naming the work and leaving the move to them;
the takeaway is theirs either way. Never "Learn more," never a form.

---

**Adding a pattern:** it enters this library only after appearing in a
built, cold-reviewed instrument — patterns are extracted from proven
work, not designed speculatively. Each entry names its job, anatomy,
and rules, and must justify itself against the standard's §16
questions.
