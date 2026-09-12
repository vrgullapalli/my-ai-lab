#!/usr/bin/env python3
"""Reachability check for the retrieval known-answer tests (his word, 2026-09-12 02:24).

One job: for every known-answer test in RETRIEVAL-TESTS.md, are the expected files
actually inside the Retrieval-eligible source set? The eligible set is every file of every
registered source with status live or degraded, as context/sources/check.py counts it.
This is a precondition check, not retrieval. It reads; it writes nothing.

Usage: python3 context/sources/tests/reachability.py [path-to-tests-file]
Exit 0 when every file of every test is reachable, 1 otherwise.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import check  # noqa: E402  (context/sources/check.py)


def eligible(lab, records):
    """Every file retrieval may read, mapped to the source id that owns it."""
    owners = {}
    for r in records:
        if r.get("status") not in ("live", "degraded"):
            continue
        locs = check.split(r.get("location", ""))
        if any(lab.where(l)[1] for l in locs) or r.get("standing") == "unavailable":
            continue
        for loc in locs:
            for f in check.files_for(lab, loc, check.split(r.get("pattern", "*"))):
                owners[os.path.normpath(os.path.abspath(f))] = check.rid(r)
    return owners


def tests_in(path):
    """(test id, [paths]) for every '## Tn.' heading followed by a '- files:' line."""
    out, cur = [], None
    for line in open(path):
        m = re.match(r"^## (T\d+)\.", line)
        if m:
            cur = m.group(1)
            continue
        if cur and line.startswith("- files:"):
            out.append((cur, check.split(line[len("- files:"):])))
            cur = None
    return out


def main():
    root = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
    lab = check.Lab(root)
    tests_file = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "RETRIEVAL-TESTS.md")
    records = check.parse(open(lab.register).read())
    if records is None:
        print("ALERT reachability: register markers missing"); return 1
    owners = eligible(lab, records)
    tests = tests_in(tests_file)
    if not tests:
        print(f"ALERT reachability: no '- files:' lines found in {tests_file}"); return 1
    bad = 0
    for tid, paths in tests:
        misses = []
        for p in paths:
            full = os.path.normpath(os.path.join(root, p))
            if full not in owners:
                misses.append(p + ("" if os.path.exists(full) else " (missing)"))
        bad += len(misses)
        state = "ok  " if not misses else "FAIL"
        print(f"{state} {tid}: {len(paths) - len(misses)} of {len(paths)} inside the eligible set")
        for m in misses:
            print(f"       outside: {m}")
    total = sum(len(p) for _, p in tests)
    print(f"{'OK' if not bad else 'FAIL'} reachability: {total - bad} of {total} known-answer files reachable "
          f"across {len(tests)} tests; eligible set {len(owners)} files from {len(set(owners.values()))} sources")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
