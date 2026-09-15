#!/usr/bin/env python3
"""Tests for seed-capture's three helper scripts, in the prove-it-can-fail form: a clean case must
pass, and every kind of break the scripts claim to catch must make them fail and name the break.

Run:  python3 .claude/skills/seed-capture/tests/seed_check_tests.py

Builds a throwaway seedbank in a temp folder and points the scripts at it through the SEEDBANK
environment variable, so nothing here reads or writes the real bank. Cases, from the
Operational DNA repair of 2026-09-15 (AD-38):

  1. known seed        a well-formed seed passes seed-check --seed
  2. broken seed       a missing attribution class, a placeholder left, and a reused ID each fail
                       and name the field
  3. repeat            a near-repeat of an existing claim scores as a likely repeat; a fresh claim
                       does not
  4. no seed           a claim with no distinctive words in common returns none
  5. no write          the Scan tools (find-similar, next-id, seed-check) change no byte of the bank
  6. write boundary    a path under session/ passes; the README, the concepts file, and a path
                       outside the bank each break it and are named

A confirmed miss becomes a regression case: add (claim, expected seed id) to REGRESSION_MISSES
and the repeat check is proven against it from then on.

Prints SEED CHECK TESTS PASSED only when every case passes.
"""
import hashlib
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = os.path.join(os.path.dirname(HERE), "scripts")
FIND = os.path.join(SCRIPTS, "find-similar.py")
NEXT = os.path.join(SCRIPTS, "next-id.py")
CHECK = os.path.join(SCRIPTS, "seed-check.py")

# (claim as Venkat said it, the seed id it became). Empty until a miss is confirmed and captured.
REGRESSION_MISSES = []

SEED_1 = """# Monitoring that never feeds a decision is journaling

- ID: A-LIVE-001
- Source: evidence/sessions/claude/test.md#turn-1
- Date: 2026-09-12
- Status: seedling
- Attribution: endorsed — Alfred's line, Venkat: "go with whatever you pick"
- Tension: dashboards feel like work; a signal that moves nothing is a diary entry.

## The claim
Monitoring that never feeds a decision is journaling. The hand test rated 89 signals and moved nothing.

## Why it matters
It is the test for any brief or dashboard: name the decision it reached, or stop producing it.

## Connections
- [[A-LIVE-002]] — the same test applied to counts
"""

SEED_2 = """# The count was honest and wrong

- ID: A-LIVE-002
- Source: evidence/sessions/claude/test.md#turn-2
- Date: 2026-09-12
- Status: seedling
- Attribution: his — typed 2026-09-12 02:10
- Tension: a script can report exactly what it saw and still count the wrong thing.

## The claim
The count was honest and wrong. The boundary counted a generated copy as the source.

## Why it matters
A coverage number is questioned by asking what it counted as a record, not by rerunning it.

## Connections
- [[A-LIVE-001]] — the decision test
"""

failures = 0


def check(name, ok, detail=""):
    global failures
    failures += 0 if ok else 1
    print(f"  {'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail[:300]})" if detail and not ok else ""))


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def run(script, *args, bank):
    env = dict(os.environ, SEEDBANK=bank)
    r = subprocess.run([sys.executable, script, *args], capture_output=True, text=True, env=env, timeout=60)
    return r.returncode, r.stdout + r.stderr


def digest(folder):
    h = hashlib.sha256()
    for root, dirs, files in os.walk(folder):
        dirs.sort()
        for name in sorted(files):
            p = os.path.join(root, name)
            h.update(os.path.relpath(p, folder).encode())
            h.update(open(p, "rb").read())
    return h.hexdigest(), sum(len(f) for _, _, f in os.walk(folder))


def main():
    tmp = tempfile.mkdtemp(prefix="seedbank-test-")
    try:
        bank = os.path.join(tmp, "seedbank")
        session = os.path.join(bank, "session")
        s1 = os.path.join(session, "A-LIVE-001-monitoring-that-never-feeds-a-decision.md")
        s2 = os.path.join(session, "A-LIVE-002-the-count-was-honest-and-wrong.md")
        write(s1, SEED_1)
        write(s2, SEED_2)
        write(os.path.join(bank, "README.md"), "# Seeds\n\n| session/ | 2 |\n")
        write(os.path.join(tmp, "memory", "concepts.md"), "# CONCEPTS\n")

        print("1. known seed")
        code, out = run(CHECK, "--seed", s1, s2, bank=bank)
        check("both fixture seeds pass", code == 0 and out.count("SEED OK") == 2, out)

        print("2. broken seeds fail and name the field")
        bad_attr = os.path.join(tmp, "bad-attr", "A-LIVE-003-no-class.md")
        write(bad_attr, SEED_1.replace("- ID: A-LIVE-001", "- ID: A-LIVE-003").replace(
            "- Attribution: endorsed — Alfred's line, Venkat: \"go with whatever you pick\"\n", ""))
        code, out = run(CHECK, "--seed", bad_attr, bank=bank)
        check("missing attribution class fails, names Attribution", code == 1 and "Attribution" in out, out)
        placeholder = os.path.join(tmp, "bad-ph", "A-LIVE-004-placeholder.md")
        write(placeholder, SEED_1.replace("- ID: A-LIVE-001", "- ID: A-LIVE-004").replace(
            "- Tension: dashboards feel like work; a signal that moves nothing is a diary entry.",
            "- Tension: <the friction that makes it worth keeping>"))
        code, out = run(CHECK, "--seed", placeholder, bank=bank)
        check("placeholder left fails, names it", code == 1 and "placeholder" in out, out)
        reused = os.path.join(tmp, "bad-id", "A-LIVE-002-second-file-same-id.md")
        write(reused, SEED_2)
        code, out = run(CHECK, "--seed", reused, bank=bank)
        check("reused ID fails, names A-LIVE-002", code == 1 and "A-LIVE-002 used twice" in out, out)
        code, out = run(CHECK, "--seed", s1, reused, bank=bank)
        check("a good and a bad seed together: exit 1, good one still OK", code == 1 and "SEED OK" in out and "SEED FAIL" in out, out)
        code, out = run(NEXT, "--check", bank=bank)
        check("next-id on the clean bank: A-LIVE-003, no duplicates", "A-LIVE-003" in out and "IDs on more than one seed: none" in out, out)

        print("3. repeat")
        code, out = run(FIND, "monitoring that never feeds a decision is journaling", bank=bank)
        check("near-repeat scores as a likely repeat of A-LIVE-001", "A-LIVE-001" in out and "likely repeat" in out, out)
        code, out = run(FIND, "a seed's date is the moment it happened, not the day it was written", bank=bank)
        check("fresh claim is not flagged as a repeat", "likely repeat" not in out, out)
        for claim, sid in REGRESSION_MISSES:
            code, out = run(FIND, claim, bank=bank)
            check(f"regression miss found: {sid}", sid in out, out)

        print("4. no seed")
        code, out = run(FIND, "zebra quartz umbrella", bank=bank)
        check("claim with no shared words returns none", "none share any distinctive words" in out, out)

        print("5. scan tools write nothing")
        before = digest(bank)
        run(FIND, "the count was honest and wrong", bank=bank)
        run(NEXT, "--check", bank=bank)
        run(CHECK, "--seed", s1, s2, bank=bank)
        run(CHECK, "--boundary", s1, bank=bank)
        after = digest(bank)
        check("bank checksum and file count unchanged after the Scan tools", before == after, f"{before} vs {after}")

        print("6. write boundary")
        code, out = run(CHECK, "--boundary", s1, os.path.join(session, "A-LIVE-003-new.md"), bank=bank)
        check("paths under session/ pass", code == 0 and "WRITE BOUNDARY OK: 2" in out, out)
        code, out = run(CHECK, "--boundary", os.path.join(bank, "README.md"), bank=bank)
        check("the seeds README breaks the boundary", code == 1 and "BROKEN" in out and "README.md" in out, out)
        code, out = run(CHECK, "--boundary", os.path.join(tmp, "memory", "concepts.md"), bank=bank)
        check("the concepts file breaks the boundary", code == 1 and "concepts.md" in out, out)
        code, out = run(CHECK, "--boundary", s1, os.path.join(bank, "missed.md"), bank=bank)
        check("one bad path in a list: exit 1, the bad one named", code == 1 and "missed.md" in out and "README" not in out, out)
        code, out = run(CHECK, "--boundary", os.path.join(session, "..", "README.md"), bank=bank)
        check("a path that climbs out of session/ breaks the boundary", code == 1, out)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print()
    if failures:
        print(f"SEED CHECK TESTS FAILED: {failures}")
        return 1
    print("SEED CHECK TESTS PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
