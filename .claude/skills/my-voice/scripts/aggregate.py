#!/usr/bin/env python3
"""Stage 5 — recurrence indices over VERIFIED quotes only.
Usage: python3 aggregate.py verified.jsonl [--min 2]
Clusters near-duplicate quotes (token-Jaccard >= 0.6) and prints the
SAID MORE THAN ONCE index with counts and pointers, plus per-bucket
totals. Run lens-mapping (a judgment step) on this output, not on raw
transcripts."""
import sys, json, re
from collections import defaultdict
mn = int(sys.argv[sys.argv.index("--min")+1]) if "--min" in sys.argv else 2
rows = [json.loads(l) for l in open(sys.argv[1], encoding="utf-8") if l.strip()]
def toks(s): return set(re.findall(r"[a-z']+", s.lower())) - {"the","a","an","and","or","to","of","is","it","that","this","i","you","we","they"}
clusters = []
for r in rows:
    t = toks(r["quote"])
    if not t: continue
    for c in clusters:
        if len(t & c["toks"]) / len(t | c["toks"]) >= 0.6:
            c["rows"].append(r); c["toks"] |= t; break
    else: clusters.append({"toks": set(t), "rows": [r]})
rec = sorted([c for c in clusters if len(c["rows"]) >= mn], key=lambda c: -len(c["rows"]))
print(f"# SAID MORE THAN ONCE — {len(rec)} clusters (min {mn})\n")
for c in rec:
    print(f"[{len(c['rows'])}x] {c['rows'][0]['quote']}")
    for r in c["rows"]: print(f"     - {r['transcript_id']} @ {r.get('timestamp','?')} [{r.get('bucket','')}]")
    print()
by = defaultdict(int)
for r in rows: by[r.get("bucket","?")] += 1
print("# per-bucket totals"); [print(f"  {k}: {v}") for k,v in sorted(by.items())]
