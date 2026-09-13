#!/usr/bin/env python3
"""Staged-selection experiment for the frozen retrieval tests (his word, 2026-09-12 05:03: "Implement the smallest
staged-selection experiment needed to run the frozen tests. Do not promote it to the default Retrieval path").

Not part of Retrieval. It sits beside the tests and uses retrieve.py read-only: candidates() for the scoped list and
the must-consider set, nothing else. The model's part (stage 1 per group, stage 3 final rank) is done by a blind
agent following the protocol in the dated report; this script does the deterministic parts:

  groups   split the scoped record list into groups of about G records by a salted hash of the ref (file order,
           source, date, and score play no part); write one file per group, the must-consider set separately,
           and a manifest that proves every scoped ref is in exactly one group.
  union    assemble the final-stage file from the per-group picks: must-consider first, then every stage-1 pick
           with its reason, deduplicated. If the union is larger than the cap, write a second level of groups.
  check    prove the manifest (each ref once; group sizes in range). --plant duplicates a ref so the check must fail.

  python3 context/sources/tests/staged_experiment.py groups --query "<q>" --scope id,id --ideas ideas.json --salt A --out DIR
  python3 context/sources/tests/staged_experiment.py union --out DIR [--level 2]
  python3 context/sources/tests/staged_experiment.py check --out DIR [--plant]

Parameters are fixed in the plan of 2026-09-12 05:03 and are the same for every test: G=100, K=8 (10 when fewer than
10 groups), union cap 150, N=10. They are not tuned per test.
"""
import hashlib
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.dirname(HERE)
sys.path.insert(0, SRC)
import check      # noqa: E402
import retrieve   # noqa: E402

LAB = check.Lab(os.path.dirname(os.path.dirname(SRC)))
G, UNION_CAP, N = 100, 150, 10


def k_for(n_groups):
    return 10 if n_groups < 10 else 8


def line_of(r):
    return f"{r['ref']} | {r['source']} | {r['date']} | {r['tier']} | {r['ceiling']} | {r['title']} — {r['gist']}"


def opt(argv, name, default=None):
    return argv[argv.index(name) + 1] if name in argv else default


def assign(refs, salt, size):
    """Deterministic, order-free grouping: sort refs by a salted hash, then cut into near-equal groups."""
    keyed = sorted(refs, key=lambda r: hashlib.sha1((salt + "|" + r).encode()).hexdigest())
    n = max(1, math.ceil(len(keyed) / size))
    per = math.ceil(len(keyed) / n)
    return [keyed[i * per:(i + 1) * per] for i in range(n)]


def cmd_groups(argv):
    q, out, salt = opt(argv, "--query"), opt(argv, "--out"), opt(argv, "--salt", "A")
    scope = opt(argv, "--scope")
    ideas = json.load(open(opt(argv, "--ideas"))) if opt(argv, "--ideas") else None
    if not q or not out:
        print("usage: groups --query <q> --scope id,id [--ideas f] [--salt S] --out DIR"); return 2
    os.makedirs(out, exist_ok=True)
    scoped_file = os.path.join(out, "scoped.txt")
    res = retrieve.candidates(LAB, q, scope.split(",") if scope else None, 40, scoped_file, ideas)
    idx = {r["ref"]: r for r in retrieve.load_index()}
    must = [c["ref"] for c in res["candidates"]]
    scoped = [l.split(" | ")[0] for l in open(scoped_file) if l.strip() and not l.startswith("#")]
    scoped = list(dict.fromkeys(scoped))
    rest = [r for r in scoped if r not in set(must)]
    groups = assign(rest, salt, G)
    k = k_for(len(groups))
    with open(os.path.join(out, "must-consider.txt"), "w") as f:
        for r in must:
            f.write(line_of(idx[r]) + "\n")
    for i, g in enumerate(groups, 1):
        with open(os.path.join(out, f"group-{i:02d}.txt"), "w") as f:
            for r in g:
                f.write(line_of(idx[r]) + "\n")
    manifest = {"query": q, "scope": res["scope"], "salt": salt, "G": G, "K": k, "union_cap": UNION_CAP, "N": N,
                "scoped_records": len(scoped), "must_consider": len(must), "groups": len(groups),
                "group_sizes": [len(g) for g in groups], "group_refs": {f"group-{i:02d}": g for i, g in enumerate(groups, 1)},
                "must_refs": must, "level": 1}
    json.dump(manifest, open(os.path.join(out, "manifest.json"), "w"), indent=1)
    print(f"groups: {len(groups)} of ~{G} from {len(rest)} scoped records (+{len(must)} must-consider held out), K={k}, salt {salt}, "
          f"sizes {min(manifest['group_sizes'])}..{max(manifest['group_sizes'])}; write group-NN-picks.json per group, then run union")
    return 0


def read_picks(path):
    try:
        return json.load(open(path)).get("picks", [])
    except (OSError, ValueError):
        return []


def cmd_union(argv):
    out, level = opt(argv, "--out"), int(opt(argv, "--level", 1))
    man = json.load(open(os.path.join(out, "manifest.json")))
    idx = {r["ref"]: r for r in retrieve.load_index()}
    prefix = "group" if level == 1 else f"l{level}-group"
    names = sorted(n for n in os.listdir(out) if n.startswith(prefix + "-") and n.endswith("-picks.json"))
    if not names:
        print(f"REFUSED union level {level}: no {prefix}-NN-picks.json files in {out}; nothing written"); return 1
    picks, seen = [], set()
    for n in names:
        for p in read_picks(os.path.join(out, n))[:man["K"]]:
            if p["ref"] in idx and p["ref"] not in seen:
                seen.add(p["ref"]); picks.append({**p, "from": n})
    must = [r for r in man["must_refs"] if r in idx]          # deterministic candidates bypass every level
    stage = [p["ref"] for p in picks if p["ref"] not in set(must)]
    union = must + stage
    if len(union) > UNION_CAP:
        groups = assign(stage, man["salt"] + str(level + 1), G)   # only the model's picks are regrouped
        for i, g in enumerate(groups, 1):
            with open(os.path.join(out, f"l{level + 1}-group-{i:02d}.txt"), "w") as f:
                for r in g:
                    f.write(line_of(idx[r]) + "\n")
        man[f"level{level + 1}_groups"] = len(groups)
        json.dump(man, open(os.path.join(out, "manifest.json"), "w"), indent=1)
        print(f"union level {level}: {len(union)} records > cap {UNION_CAP}; wrote {len(groups)} level-{level + 1} groups "
              f"(l{level + 1}-group-NN.txt); pick K per group into l{level + 1}-group-NN-picks.json, then run union --level {level + 1}")
        return 0
    reasons = {p["ref"]: p.get("reason", "") for p in picks}
    with open(os.path.join(out, "union.txt"), "w") as f:
        f.write(f"# final stage: {len(must)} must-consider (deterministic) then {len(union) - len(must)} stage-1 picks; pick up to {N} by meaning\n")
        for r in union:
            f.write(line_of(idx[r]) + (f"  [stage-1 reason: {reasons[r][:120]}]" if r in reasons else "") + "\n")
    man.update({"union_size": len(union), "stage1_picks": len(picks), "groups_with_picks": len(names), "final_level": level})
    json.dump(man, open(os.path.join(out, "manifest.json"), "w"), indent=1)
    print(f"union: {len(union)} records ({len(must)} must-consider + {len(union) - len(must)} stage-1 picks from {len(names)} groups) -> {os.path.join(out, 'union.txt')}; "
          f"pick up to {N} into final-picks.json")
    return 0


def cmd_check(argv):
    out = opt(argv, "--out")
    man = json.load(open(os.path.join(out, "manifest.json")))
    groups = {k: list(v) for k, v in man["group_refs"].items()}
    if "--plant" in argv:
        first = next(iter(groups)); last = list(groups)[-1]
        groups[last].append(groups[first][0])
    counts = {}
    for g, refs in groups.items():
        for r in refs:
            counts[r] = counts.get(r, 0) + 1
    dup = [r for r, c in counts.items() if c > 1]
    missing = [r for r in man["group_refs"] and sum(groups.values(), []) if r in man["must_refs"]]
    sizes = [len(v) for v in groups.values()]
    ok = not dup and not missing and all(int(G * 0.6) <= s <= int(G * 1.4) for s in sizes)
    expected = man["scoped_records"] - man["must_consider"]
    ok = ok and sum(sizes) == expected
    print(f"{'OK' if ok else 'FAIL'} manifest: {len(groups)} groups, {sum(sizes)} refs (expected {expected}), "
          f"{len(dup)} in more than one group, {len(missing)} must-consider leaked into groups, sizes {min(sizes)}..{max(sizes)}")
    return 0 if ok else 1


def main():
    argv = sys.argv[1:]
    if not argv:
        print(__doc__); return 2
    return {"groups": cmd_groups, "union": cmd_union, "check": cmd_check}.get(argv[0], lambda a: (print(__doc__), 2)[1])(argv[1:])


if __name__ == "__main__":
    sys.exit(main())
