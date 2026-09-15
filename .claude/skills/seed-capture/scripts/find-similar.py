#!/usr/bin/env python3
"""find-similar: the seeds that already say something close to a new claim.

  python3 find-similar.py "the claim, as a full sentence"
  python3 find-similar.py --top 10 "the claim"

Read-only. seed-capture runs it before writing a seed (its duplicate and conflict check),
and the close routine runs it on each candidate it finds in a session.

How it scores: each seed's title and claim are cut into words and word pairs, common
words removed. A seed scores by how much of the new claim's wording it already contains,
with word pairs counting more than single words. Plain word overlap: no model, no
internet, the same answer every time. It finds near-repeats reliably and misses
paraphrases. A match it finds is almost always a real neighbour, so its top results are
the first candidates for a `Conflicts with:` line and the `## Connections` section. A
seed it misses is still yours to catch.

Built 2026-09-10. Before this, the duplicate check was "grep existing seeds for the
claim's key words", done by hand each time.
"""
import os
import re
import sys

SEEDBANK = os.environ.get("SEEDBANK") or "/Users/venkatgullapalli/Documents/my-ai-lab/work-os/brand-os/engagement-os/seedbank"
# SEEDBANK in the environment points the script at a test bank; the tests use it, nothing else does.
FOLDERS = ("session", "written", "spoken")
STOP = set("""a an and are as at be been but by can do does for from had has have he her his
how i if in into is it its it's just may me more most my no not of on or our out so than
that the their them then there these they this to too up us was we were what when which
who why will with would you your his him she about after all also any because before being
both each few very own same should now only over such""".split())


def words(text):
    return [w for w in re.findall(r"[a-z0-9']+", text.lower()) if w not in STOP and len(w) > 2]


def features(text):
    w = words(text)
    return set(w), set(zip(w, w[1:]))


def seed_text(path):
    text = open(path, encoding="utf-8", errors="replace").read()
    title = next((l[2:].strip() for l in text.split("\n") if l.startswith("# ")), "")
    claim = ""
    m = re.search(r"## The claim[^\n]*\n(.*?)(?=\n## |\Z)", text, re.S)
    if m:
        claim = m.group(1)
    sid = re.search(r"^- ID:\s*(\S+)", text, re.M)
    ident = sid.group(1) if sid else os.path.basename(path).split("-")[0]
    return ident, title, title + " " + claim[:1500]


def main():
    args = sys.argv[1:]
    top = 5
    if args[:1] == ["--top"]:
        top, args = int(args[1]), args[2:]
    if not args:
        print(__doc__)
        sys.exit(2)
    q_words, q_pairs = features(" ".join(args))
    if not q_words:
        print("The claim has no distinctive words to match on.")
        return
    scored = []
    for folder in FOLDERS:
        d = os.path.join(SEEDBANK, folder)
        if not os.path.isdir(d):
            continue
        for name in os.listdir(d):
            if not name.endswith(".md") or name.startswith(("SUMMARY", "garden-state")):
                continue
            path = os.path.join(d, name)
            ident, title, body = seed_text(path)
            s_words, s_pairs = features(body)
            w = len(q_words & s_words) / len(q_words)
            p = len(q_pairs & s_pairs) / len(q_pairs) if q_pairs else 0.0
            score = 0.4 * w + 0.6 * p
            if score > 0:
                scored.append((score, ident, title, os.path.join(folder, name)))
    scored.sort(reverse=True)
    print(f"Closest seeds to: {' '.join(args)[:120]}")
    for score, ident, title, rel in scored[:top]:
        flag = "  <- likely repeat, read it" if score >= 0.45 else ""
        print(f"  {score:.2f}  {ident:<14} {title[:90]}{flag}\n        seedbank/{rel}")
    if not scored:
        print("  none share any distinctive words")


if __name__ == "__main__":
    main()
