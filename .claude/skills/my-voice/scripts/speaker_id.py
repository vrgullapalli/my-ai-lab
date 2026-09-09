#!/usr/bin/env python3
"""Step 0 — identify which speaker label is HIM in an unlabeled transcript.
Usage: python3 speaker_id.py transcript.txt [--fingerprint fingerprint.txt]
Transcript lines must look like "Speaker 1: ..." / "S2: ..." / "NAME: ...".
Scores each speaker on three signals only he produces:
  1. fingerprint phrases (his recurring lines; grows from verified quotes)
  2. question rate (share of turns that ask)
  3. reframe openers / reactions at turn start
Talk-time and topic are NOT used to decide — only reported.
Prints a ranked table. If the top two are close, it prints three sample
lines from each and exits 2 = ASK HIM. Never guesses silently."""
import sys, re, json
from collections import defaultdict

DEFAULT_FP = ["let me back up","let me put it this way","let me just ask","how can you tell",
  "what did you do to prove","wow, okay","what's missing","what is that fear","that's it?",
  "but that's not","conversion is the same word","same data, same","twenty times","i hate it",
  "let's look at it this way","what happens if","see what i did there","who decides that",
  "who maintains production","who sees the bigger picture","do they have that skill set"]
OPENERS = r"^(so |ok(ay)? |but |oh |wow|let me|here's what|that's it|really\?)"

path = sys.argv[1]
fp = DEFAULT_FP
if "--fingerprint" in sys.argv:
    fp += [l.strip().lower() for l in open(sys.argv[sys.argv.index("--fingerprint")+1]) if l.strip()]

turns = defaultdict(list)
for line in open(path, encoding="utf-8", errors="replace"):
    m = re.match(r"^\s*([A-Za-z][\w .\-]{0,30}?)\s*:\s*(.+)$", line)
    if m: turns[m.group(1).strip()].append(m.group(2).strip())
if len(turns) < 2: print("fewer than 2 labeled speakers found — check transcript format"); sys.exit(1)

rows = []
for spk, ts in turns.items():
    text = " ".join(ts).lower()
    words = len(text.split())
    fp_hits = sum(text.count(p) for p in fp)
    q_rate = sum(1 for t in ts if "?" in t) / len(ts)
    op_rate = sum(1 for t in ts if re.match(OPENERS, t.lower())) / len(ts)
    # decision score: only the three "him" signals, normalized per 1k words
    score = (fp_hits / max(words,1) * 1000) * 3 + q_rate * 2 + op_rate * 1
    rows.append((score, spk, len(ts), words, fp_hits, round(q_rate,2), round(op_rate,2)))
rows.sort(reverse=True)

print(f"{'score':>6}  {'speaker':<14}{'turns':>6}{'words':>7}{'fp':>4}{'q-rate':>8}{'open':>6}")
for r in rows: print(f"{r[0]:6.2f}  {r[1]:<14}{r[2]:>6}{r[3]:>7}{r[4]:>4}{r[5]:>8}{r[6]:>6}")
top, second = rows[0], rows[1]
margin = top[0] - second[0]
if margin < 0.5 or top[4] == 0:
    print("\nAMBIGUOUS — do not proceed. Ask him. Samples:")
    for r in (top, second):
        print(f"\n  [{r[1]}]")
        for t in [t for t in turns[r[1]] if len(t.split()) > 6][:3]: print("   -", t[:160])
    sys.exit(2)
print(f"\nHIM = {top[1]}  (margin {margin:.2f}; talk-time was NOT used to decide)")
json.dump({"transcript": path, "him": top[1], "margin": round(margin,2)}, open(path + ".speaker.json","w"))
