#!/usr/bin/env python3
"""retrieve_tests.py — proves the deterministic half of context/sources/retrieve.py can fail (the prove-it-can-fail rule).

Builds a small lab in a temp folder, points retrieve.py's index at a temp folder, and plants one fault at a time:
a seedbank file with no id line (a dashboard, not a seed) must stay out of the index and be refused by fetch;
the "reached by the idea alone" counter must count only candidates that no query word hit; a path with a space
in a folder name must resolve whole, and a missing path must not. Last, the lab's own index must hold no
seedbank file without an id line. Added 2026-09-14 for F-20260913-0502-4.

  python3 context/sources/tests/retrieve_tests.py
"""
import json, os, shutil, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.dirname(HERE)
sys.path.insert(0, SRC)
import check      # noqa: E402
import retrieve   # noqa: E402

REAL_INDEX = retrieve.INDEX
FAILS = []


def result(name, ok, out=""):
    print(("ok   " if ok else "FAIL ") + name)
    if not ok:
        FAILS.append(name)
        print("     " + str(out).replace("\n", "\n     ")[:1200])


def record(i, location, pattern="*.md", **over):
    f = {"id": i, "kind": "test", "location": location, "pattern": pattern, "owner": "test", "standing": "canonical",
         "tier": "system", "date-field": "mtime", "status": "live", "use": "evidentiary", "may-inform": "tests",
         "not-alone": "anything", "read-by": "the tests", "added": "2026-09-14", "changed": "2026-09-14"}
    f.update(over)
    return f"### {i}\n" + "\n".join(f"- {k}: {v}" for k, v in f.items()) + "\n"


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w").write(text)


# a small lab: three notes and a seedbank folder with one seed and one dashboard
lab_dir = tempfile.mkdtemp(prefix="retrieve-test-")
write(os.path.join(lab_dir, "notes", "tart.md"), "# Apple tart\n\napple tart is a dessert dish\n")
write(os.path.join(lab_dir, "notes", "plate.md"), "# Fruit plate\n\nfruit dessert dish plate for guests\n")
write(os.path.join(lab_dir, "notes", "other.md"), "# Nothing\n\nunrelated words only\n")
write(os.path.join(lab_dir, "seedbank", "spoken", "01-first.md"), "# First seed\n\n- ID: S01\n- Date: 2026-09-14\n\nA seed with its id line.\n")
write(os.path.join(lab_dir, "seedbank", "spoken", "garden-state.md"), "# Garden State\n\nA dashboard about the seeds. No id line.\n")
write(os.path.join(lab_dir, "context", "sources", "REGISTER.md"),
      "# test\n\n<!-- register:start -->\n\n" + record("notes", "notes") + "\n" + record("seeds", "seedbank/spoken") + "\n<!-- register:end -->\n")
lab = check.Lab(lab_dir)
records = check.parse(open(lab.register).read())

# the index goes to a temp folder, never the lab's own
idx_dir = tempfile.mkdtemp(prefix="retrieve-index-")
retrieve.INDEX_DIR = idx_dir
retrieve.INDEX = os.path.join(idx_dir, "retrieval-index.jsonl")
retrieve.COMPACT = os.path.join(idx_dir, "compact.txt")
retrieve.RUNS = os.path.join(idx_dir, "runs.jsonl")

# 1. a seedbank file with no id line is not a record: out of the index, refused by fetch
import io, contextlib
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    code = retrieve.build_index(lab, records)
line = buf.getvalue()
paths = [json.loads(l)["path"] for l in open(retrieve.INDEX) if l.strip()]
result("index builds with coverage complete", code == 0 and "coverage complete" in line, line)
result("a seed with its id line is indexed", "seedbank/spoken/01-first.md" in paths, paths)
result("a seedbank file with no id line is left out of the index", "seedbank/spoken/garden-state.md" not in paths, paths)
result("the index line says one file was left out as not a record", "1 file(s) without an id line left out as not records" in line, line)
stats = json.load(open(os.path.join(idx_dir, "stats.json")))
result("stats.json names the file left out", stats.get("left_out_no_id_line") == ["seedbank/spoken/garden-state.md"], stats)
pkg = retrieve.fetch(lab, records, "garden", {"picks": [{"ref": "seedbank/spoken/garden-state.md"}, {"ref": "seedbank/spoken/01-first.md"}]})
result("fetch refuses the file with no id line and returns the seed",
       pkg["refused"] == ["seedbank/spoken/garden-state.md"] and [r["ref"] for r in pkg["results"]] == ["seedbank/spoken/01-first.md"], pkg["refused"])

# 2. "reached by the idea alone" counts candidates no query word hit. tart.md is hit by the query and also by
#    the idea (so the idea outscores the query's words there: the old rule counted it); plate.md is hit by the
#    idea only; other.md by nothing.
res = retrieve.candidates(lab, "apple tart", expansions=["a fruit dessert dish plate"])
refs = [c["ref"] for c in res["candidates"]]
result("candidates: the query file and the idea-only file, not the unrelated one",
       "notes/tart.md" in refs and "notes/plate.md" in refs and "notes/other.md" not in refs, refs)
tart = next(c for c in res["candidates"] if c["ref"] == "notes/tart.md")
result("planted: the idea outscores the query's own words on the query file (the case the old rule miscounted)",
       tart["semantic"] > tart["score"] - tart["semantic"], tart)
result("reached by the idea alone is 1, not every candidate", res["reached_by_idea_only"] == 1, res["reached_by_idea_only"])

# 3. a path with a space in a folder name resolves whole; a missing path does not
spaced = "~/Library/Application Support"
if not os.path.isdir(os.path.expanduser(spaced)):
    print(f"skip path-with-a-space test: {spaced} is not on this machine")
else:
    text = f"the copy sits in {spaced}/ and a note follows; a dead one at /Users/nobody/gone with words after it."
    ps = {p["path"]: p["resolves"] for p in retrieve.pointer_state(lab, text)}
    result("a path with a space is kept whole and resolves", ps.get(spaced + "/") is True, ps)
    result("a missing path is cut at the first space and does not resolve", ps.get("/Users/nobody/gone") is False, ps)
    result("no pointer is split at the space", "~/Library/Application" not in ps, ps)

shutil.rmtree(lab_dir)
shutil.rmtree(idx_dir)

# 4. the lab's own index, when built, holds no seedbank file without an id line
if os.path.isfile(REAL_INDEX):
    seed_paths = [json.loads(l)["path"] for l in open(REAL_INDEX) if l.strip() and '"source": "seeds"' in l]
    bad = [p for p in seed_paths if os.path.basename(p) in ("garden-state.md",) or os.path.basename(p).startswith("SUMMARY-")]
    result("the lab's own index holds no seedbank dashboard or summary", not bad, bad)
else:
    print("skip: the lab's own index is not built (python3 context/sources/retrieve.py index)")

print()
print("all passed" if not FAILS else f"{len(FAILS)} failed: " + ", ".join(FAILS))
sys.exit(1 if FAILS else 0)
