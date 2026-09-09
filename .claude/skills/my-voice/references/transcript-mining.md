# Transcript mining — turning raw transcripts into specimens, lines,
# lens evidence, and judgment fragments.
# Prime rule: extraction is QUOTATION, never summarization. Paraphrase
# launders his words into AI prose and wastes the exercise.
# His turns only — AI replies in any transcript are contamination.

Paste-ready prompt:

MINE THESE TRANSCRIPTS. Extract, never summarize — every output line is a
verbatim quote with [file, location]. My turns only; ignore anything an AI
said back to me. Keep typos, fragments, self-repairs.

Produce four files:
1. voice-specimens.md — 15-30 passages where the speech is most
   distinctive: rants, blunt reactions, number runs, threshold idioms,
   point-blank questions. Tag each: [rant|client|teaching|blunt].
2. lines.md — sentences that could headline something: challenge
   questions, reframes, verdict sentences. Separate section: SAID MORE
   THAN ONCE, with count and each occurrence's pointer. (Recurrence is
   the signal — a line said three times is the real Q5.)
3. lens-evidence.md — every absence-move ("what's missing", "nobody's
   asking"), polish-distrust reaction, layer move, reproducibility
   demand. Map each quote to the lens line it supports, or mark NEW.
4. judgment-fragments.md — bucketed by subject: claims I made, break
   stories, thresholds, what-I-check-first. Fragments with pointers
   only — do NOT assemble them into a model; that happens in capture,
   with me.

Banned: paraphrase, "in essence", cleaned-up grammar, any sentence I
didn't say. If a passage is almost-great but unclear, quote it and mark
[unclear] — never repair it.

Afterward: specimens feed voice.md; recurring lines feed voice.md and the
open Q5; lens evidence updates lens.md (NEW items need his confirmation
before they join); judgment-fragments are PRE-capture ore — the capture
session still runs, with him, before any model exists.

## v2 — corpus scale (50+ transcripts). Adds a required pre-pass and six buckets.

PRE-PASS 0 — REDACTION, before anything else. Counterparty names,
companies, their numbers, their architectures, anything they said about
their own shop: described in one neutral line, never quoted. My side
stays verbatim. Output a redaction log (what was removed, where). Nothing
leaves the vault until this has run.

Additional buckets (same rules: quotation only, pointers on every line,
my turns only):
5. questions-by-moment.md — every question I asked, tagged
   [discovery|diagnosis|pushback|close]. Primary index: ASKED MORE THAN
   ONCE, with counts. Feeds room questions and all capture kits.
6. objections-and-answers.md — what they said back (described, per
   redaction) paired with what I said next (verbatim). Tag the
   misconception in their objection where visible. Feeds refusals,
   recovery, teachable foils, positioning.
7. calls-made.md — every dated prediction or warning I made ("if you do X,
   Y", "this will fail because"), with date and context; column for known
   outcome where any later transcript shows it. Seeds the scoreboard.
8. definitions.md — every term I defined in my own words. Glossary with
   pointers. Feeds lens line 9 (definitions-first).
9. refusals.md — every time I said don't, walked away, or declined to
   conclude. Feeds lens line 7 evidence and assessor rejection readings.
   If the corpus shows none, say so — that is a finding.
10. register-map.md — where the playful register surfaces: which
    counterparties, which moments. Feeds the voice pass's permission map.

Corpus-scale rules: stable pointers [transcript-id, timestamp, speaker]
on every line; SAID/ASKED MORE THAN ONCE indices are primary outputs, not
side sections; batch by client and date; never summarize a transcript —
200 summaries is 200 pages of AI prose about him.


## Methodology at corpus scale (the six stages)
1. PILOT on 5 transcripts; read every output; calibrate redaction first.
2. REDACT per transcript — strongest model, highest effort; redacted copy +
   log. His turns untouched.
3. EXTRACT per transcript — ONE transcript per call (parallel calls, never
   stuffed context); output the fixed schema in `scripts/schema.md`. A
   cheaper model is fine here: the verifier catches fumbles.
4. VERIFY by script — `scripts/verify_quotes.py`: verbatim substring match
   + speaker check; >5% drops = prompt drift, stop and fix.
5. AGGREGATE by code — `scripts/aggregate.py` over verified quotes only:
   recurrence clusters, per-bucket totals. Lens-mapping (judgment) runs
   here, strongest model.
6. HUMAN PASS, narrow — he reads the recurrence tops and lens NEW items
   only, never 200 files.
Model/effort principle (product specifics change — check docs): judgment
stages (redact, lens-map, final review) get the strongest model at high
effort; extraction gets default, because the verifier makes fidelity a
script property, not a model property.

## Light clean — the ONLY edits allowed on a specimen
REMOVE: fillers (um, uh, erm, hmm, like-as-filler, you know, I mean, sort
of, kind of, basically, actually-as-filler), stutters and repeated words,
false starts of under three words.
KEEP: self-repairs that carry meaning ("not expert, but..."), fragments,
sentence-final "right?", reactions, odd word order, everything else.
NEVER: complete a sentence, swap a word, merge two sentences, fix grammar,
reorder. If a line is unusable without those, it is not a specimen.
He does not want raw captured; he does not want polish either. This is
the middle, and the verifier matches with fillers ignored on both sides.

## Step 0 — speaker identification (when his name isn't on the transcript)
Run `scripts/speaker_id.py` first. It scores each speaker label on three
signals only he produces: fingerprint phrases (his recurring lines — grows
from verified quotes), question rate, reframe openers/reactions.
Talk-time and topic are reported but NEVER decide — he may be the one
asking, and counterparties talk strategy too. If the top two are close it
prints three lines from each and stops: ask him, never guess. The wrong
speaker poisons every downstream file. After each verified batch, append
the new "said more than once" lines to fingerprint.txt so identification
gets stronger over the corpus.
