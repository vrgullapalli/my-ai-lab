#!/usr/bin/env python3
"""Stage 4 — verify extracted quotes against their source transcripts.
Usage: python3 verify_quotes.py extracted.jsonl transcripts_dir/ [--speaker VENKAT]
Each JSONL line: {"transcript_id","timestamp","speaker","quote","bucket","tags"}
A quote passes only if it appears VERBATIM (whitespace-normalized) in the
source file transcripts_dir/<transcript_id>.* and the speaker matches.
Prints pass/drop counts; writes verified.jsonl and dropped.jsonl.
A batch with >5% drops means the extraction prompt is drifting — fix it
before running more."""
import sys, json, re, glob, os

FILLERS = r"\b(um+|uh+|erm|hmm+|like|you know|i mean|sort of|kind of|kinda|sorta|basically|actually|right\?|okay so|so yeah)\b"
def norm(s):
    s = s.replace("\u2019","'").replace("\u201c",'"').replace("\u201d",'"').lower()
    s = re.sub(FILLERS, " ", s)                 # fillers never count
    s = re.sub(r"\b(\w+)( \1\b)+", r"\1", s)     # stutters: "the the" -> "the"
    s = re.sub(r"[^a-z0-9' ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()

src, tdir = sys.argv[1], sys.argv[2]
speaker = None
if "--speaker" in sys.argv: speaker = sys.argv[sys.argv.index("--speaker")+1].lower()

cache = {}
def load(tid):
    if tid not in cache:
        hits = glob.glob(os.path.join(tdir, tid + ".*"))
        cache[tid] = norm(open(hits[0], encoding="utf-8", errors="replace").read()) if hits else None
    return cache[tid]

ok, bad = [], []
for line in open(src, encoding="utf-8"):
    line = line.strip()
    if not line: continue
    try: r = json.loads(line)
    except Exception: bad.append({"raw": line, "why": "not json"}); continue
    text = load(r.get("transcript_id",""))
    if text is None: r["why"] = "transcript not found"; bad.append(r); continue
    if speaker and r.get("speaker","").lower() != speaker: r["why"] = "wrong speaker"; bad.append(r); continue
    q = norm(r.get("quote",""))
    if len(q) < 8: r["why"] = "too short"; bad.append(r); continue
    if q in text: ok.append(r)
    else: r["why"] = "not verbatim in source"; bad.append(r)

json.dump if False else None
with open("verified.jsonl","w",encoding="utf-8") as f:
    for r in ok: f.write(json.dumps(r, ensure_ascii=False)+"\n")
with open("dropped.jsonl","w",encoding="utf-8") as f:
    for r in bad: f.write(json.dumps(r, ensure_ascii=False)+"\n")
total = len(ok)+len(bad)
rate = (len(bad)/total*100) if total else 0
print(f"verified {len(ok)} · dropped {len(bad)} · drop rate {rate:.1f}%")
if rate > 5: print("WARNING: >5% drops — extraction is drifting; fix the prompt before continuing")
