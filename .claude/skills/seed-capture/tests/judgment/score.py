#!/usr/bin/env python3
"""score: compares a blind judge's verdicts on cases.md with the frozen answers.

  python3 score.py <verdicts.json>     score one run; prints one line per case and a summary
  python3 score.py --check-set         prove the set itself: five cases of the five required
                                       kinds, and the cases file carries no answers

READ-ONLY. Writes nothing. A run passes when at least four of five verdicts match AND the
tempting non-seed (case 3) is not called a seed, because telling a strong candidate from a
plausible non-seed is the claim this set exists to prove. Built 2026-09-15 (Operational DNA
v2 repair of seed-capture). The judge must be a session or subagent that has not read
answers.json; the same session that wrote the answers grading itself is not evidence.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CASES = os.path.join(HERE, "cases.md")
ANSWERS = os.path.join(HERE, "answers.json")
KINDS = {"clear seed", "subtle seed", "tempting non-seed", "repeat", "honest ambiguous"}
VERDICTS = {"seed", "not-seed", "repeat", "ask"}


def load_answers():
    data = json.load(open(ANSWERS, encoding="utf-8"))
    return {k: v for k, v in data.items() if k.startswith("case-")}


def check_set():
    answers = load_answers()
    problems = []
    if len(answers) < 5:
        problems.append(f"only {len(answers)} cases in answers.json")
    kinds = {v.get("kind") for v in answers.values()}
    missing = KINDS - kinds
    if missing:
        problems.append("kinds missing: " + ", ".join(sorted(missing)))
    for k, v in answers.items():
        if v.get("verdict") not in VERDICTS:
            problems.append(f"{k}: verdict '{v.get('verdict')}' is not one of {sorted(VERDICTS)}")
    cases = open(CASES, encoding="utf-8").read()
    for k in answers:
        if f"## Case {k.split('-')[1]}" not in cases:
            problems.append(f"{k} has no section in cases.md")
    body = cases.split("## Case 1", 1)[1] if "## Case 1" in cases else cases
    body = body.split("## Verdict file shape")[0]
    for k, v in answers.items():
        n = k.split("-")[1]
        sec = re.search(rf"## Case {n}\n(.*?)(?=\n## |\Z)", body, re.S)
        text = sec.group(1) if sec else ""
        if re.search(r"\b(verdict|expected|answer)\b", text, re.I):
            problems.append(f"{k}: the case text names a verdict or answer")
    for p in problems:
        print("  " + p)
    print(f"cases: {len(answers)}; kinds: {len(kinds & KINDS)} of 5")
    print("JUDGMENT SET OK" if not problems else "JUDGMENT SET BROKEN")
    return 1 if problems else 0


def score(path):
    answers = load_answers()
    try:
        run = json.load(open(path, encoding="utf-8"))
    except (OSError, ValueError) as e:
        print(f"cannot read the verdict file: {e}")
        print("JUDGMENT EVAL FAILED")
        return 1
    matched = 0
    non_seed_ok = True
    for k in sorted(answers):
        want = answers[k]["verdict"]
        got = (run.get(k) or {}).get("verdict")
        ok = got == want
        matched += ok
        if answers[k]["kind"] == "tempting non-seed" and got == "seed":
            non_seed_ok = False
        reason = (run.get(k) or {}).get("reason", "")[:90]
        print(f"  {'MATCH' if ok else 'MISS '}  {k} ({answers[k]['kind']}): judge said {got!r}, expected {want!r}  {reason}")
    print(f"JUDGMENT EVAL: {matched} of {len(answers)} matched; tempting non-seed called a seed: {'no' if non_seed_ok else 'YES'}")
    passed = matched >= 4 and non_seed_ok
    print("JUDGMENT EVAL PASSED" if passed else "JUDGMENT EVAL FAILED")
    return 0 if passed else 1


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    if sys.argv[1] == "--check-set":
        return check_set()
    return score(sys.argv[1])


if __name__ == "__main__":
    sys.exit(main())
