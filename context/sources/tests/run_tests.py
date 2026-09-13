#!/usr/bin/env python3
"""Runner for the seven frozen retrieval tests (RETRIEVAL-TESTS.md), built 2026-09-12.

The model's part (semantic candidate selection, ranking, conflict flagging) is supplied as a selections file
written by a blind pass: {"T1": {"picks": [{"ref", "reason"}], "conflicts": [...], "missing_evidence": {...},
"semantic_pass": {...}}, ...}. Everything after that is deterministic: this runner fetches the evidence through
retrieve.py and scores each test's pass condition on the package, never on a judgment.

  python3 context/sources/tests/run_tests.py --candidates                 # deterministic candidates per test, and the compact index size
  python3 context/sources/tests/run_tests.py --selections selections.json # fetch + score; "RETRIEVAL TESTS: n of 7 passed"
  python3 context/sources/tests/run_tests.py --prove-boundary             # a pick outside the register must be refused
"""
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.dirname(HERE)
sys.path.insert(0, SRC)
import check      # noqa: E402
import retrieve   # noqa: E402

LAB = check.Lab(os.path.dirname(os.path.dirname(SRC)))
TESTS = os.path.join(HERE, "RETRIEVAL-TESTS.md")
OUT = os.path.join(SRC, "index", "runs")
E = "work-os/brand-os/engagement-os"
SEEDS = f"{E}/seedbank"


def tests():
    out, cur = [], None
    for line in open(TESTS):
        m = re.match(r"^## (T\d+)\. (.+)$", line)
        if m:
            cur = {"id": m.group(1), "name": m.group(2).strip()}
            out.append(cur)
            continue
        if cur and line.startswith("- **Question / job:**"):
            q = re.search(r'"(.+)"', line)
            cur["query"] = q.group(1) if q else line.split(":**", 1)[1].strip()
        if cur and line.startswith("- files:"):
            cur["files"] = check.split(line[len("- files:"):])
    return out


def refs(pkg, n=None):
    rs = pkg["results"] if n is None else pkg["results"][:n]
    return [r["ref"] for r in rs]


def paths(pkg, n=None):
    return [r.split("#")[0] for r in refs(pkg, n)]


def has_meta(pkg):
    return all(r.get("source") and r.get("date") and r.get("ceiling") for r in pkg["results"])


def evidence_text(pkg):
    return "\n".join("\n".join(r["evidence"]) for r in pkg["results"])


def score(t, pkg):
    """Returns (passed, [reasons])."""
    why = []
    ok = True

    def need(cond, msg):
        nonlocal ok
        if not cond:
            ok = False
            why.append("FAIL " + msg)
        else:
            why.append("ok   " + msg)

    need(not pkg["refused"], "nothing from outside a registered source")
    need(has_meta(pkg), "every result names source id, date, and ceiling")
    tid = t["id"]
    if tid == "T1":
        top5 = paths(pkg, 5)
        need(f"{E}/targets/eversana-intouch/dossier-2026-08-30.md" in top5, "dossier in top 5")
        need(f"{E}/targets/index/verdicts.jsonl" in top5, "verdict line in top 5")
        limits = 0
        d = next((r for r in pkg["results"] if r["ref"].endswith("dossier-2026-08-30.md")), None)
        newest = sorted(os.listdir(os.path.join(LAB.root, f"{E}/targets/eversana-intouch")))[-1]
        if d and d["age_days"] and d["age_days"] > 0 and newest == "dossier-2026-08-30.md":
            limits += 1; why.append("     limit: dossier dated 2026-08-30, no newer dossier")
        marks = {}
        for r in pkg["results"]:
            for k, v in r["marks"].items():
                if isinstance(v, int):
                    marks[k] = marks.get(k, 0) + v
        for k, label in (("claimed", "claimed marks carried"), ("vendor-owned-outlet", "vendor-owned outlet named"), ("page-not-opened", "page could not be opened")):
            if marks.get(k):
                limits += 1; why.append(f"     limit: {label} ({marks[k]})")
        ev = evidence_text(pkg).lower()
        if "workable" in ev or "0 postings" in ev or "posting_count" in ev:
            limits += 1; why.append("     limit: wrong applicant system, 0 postings")
        need(limits >= 3, f"at least three of five limits carried ({limits})")
    elif tid == "T2":
        top5 = paths(pkg, 5)
        need(f"{SEEDS}/session/A-LIVE-187-the-green-checks-were-making-me-less-safe.md" in top5, "A-LIVE-187 in top 5")
        need(f"{E}/editorial/pieces/2026-09-08--green-means-something-different-now/05-research.md" in top5, "article research file in top 5")
        base = subprocess.run([sys.executable, os.path.join(LAB.root, ".claude/skills/seed-capture/scripts/find-similar.py"), "--top", "5", t["query"]],
                              capture_output=True, text=True, cwd=LAB.root)
        out = base.stdout + base.stderr
        need("A-LIVE-187" not in out and "05-research" not in out, "baseline word-overlap matcher returns neither (the miss is real)")
        t["baseline"] = out.strip().split("\n")[:8]
    elif tid == "T3":
        rs = {r["ref"]: r for r in pkg["results"]}
        r36, r37 = rs.get("work-os/brand-os/DECISIONS.md#row:036"), rs.get("work-os/brand-os/DECISIONS.md#row:037")
        need(r36 is not None and r37 is not None, "both rows 036 and 037 returned")
        need(r37 and r37["supersession"]["state"] == "current" and "work-os/brand-os/DECISIONS.md#row:036" in r37["supersession"].get("corrects", []), "037 marked current and correcting 036")
        need(r36 and r36["supersession"]["state"] == "superseded" and r36["supersession"].get("by", "").endswith("row:037"), "036 marked superseded by 037")
    elif tid == "T4":
        need(len(pkg["results"]) <= 10, f"ten or fewer results ({len(pkg['results'])})")
        top5 = paths(pkg, 5)
        need(f"{SEEDS}/spoken/08-data-strategy-defined.md" in top5, "S08 in top 5")
        need(f"{SEEDS}/spoken/15-orgs-dont-understand-data-strategy.md" in top5, "S15 in top 5")
        canon = [r for r in pkg["results"][:5] if r["ref"] in ("work-os/brand-os/positioning/README.md", "work-os/brand-os/positioning/context-brief--positioning-v5--2026-09-02.md")]
        need(bool(canon), "the current canonical positioning context in top 5 (README or the v5 brief; AD-23)")
        need(any("surround a capability" in "\n".join(r["evidence"]).lower() for r in canon), "its fetched evidence carries the throughline")
        d3 = next((r for r in pkg["results"] if r["ref"] == "RULINGS-IN-FORCE.md#row:D-003"), None)
        need(d3 is not None and d3["kind"] == "row" and d3["source"] == "rulings", "D-003 present as a rulings row (a rule, not context)")
        bad = [p for p in paths(pkg) if "_archive" in p or (p.startswith(SEEDS) and os.path.basename(p) in ("README.md", "INDEX.md", "missed.md"))]
        need(not bad, f"nothing from _archive or the seedbank's own README, INDEX, missed.md {bad}")
    elif tid == "T5":
        top3 = refs(pkg, 3)
        need("work-os/brand-os/model/capabilities.json#CAP-001" in top3, "CAP-001 in top 3")
        c = next((r for r in pkg["results"] if r["ref"].endswith("#CAP-001")), None)
        ex = (c or {}).get("marks", {}).get("extracts", [])
        need(bool(ex) and any(e["quote"] for e in ex), "batch2 extract quoted with the capability")
        dead = [p for e in ex for p in e["pointers"] if not p["resolves"]]
        need(bool(dead), f"pointer state reported: {len(dead)} cited path(s) do not resolve")
        g = subprocess.run(["git", "status", "--porcelain", "work-os/brand-os/model"], capture_output=True, text=True, cwd=LAB.root).stdout
        need(not g.strip(), "the canonical model is untouched (git status clean)")
    elif tid == "T6":
        ps = paths(pkg)
        need("CLAUDE.md" in ps, "the CLAUDE.md line is in the result")
        need(any(p.startswith("evidence/receipts/") for p in ps), "at least one receipt is in the result")
        fl = pkg["conflicts"]["flagged_by_model"]
        both = any("CLAUDE.md" in json.dumps(f) and ("receipts" in json.dumps(f) or "STANDING" in json.dumps(f)) for f in fl)
        need(both, "a conflict flag names the front-door line and a newer record")
        allt = evidence_text(pkg) + json.dumps(fl)
        need("F-20260910-1349-5" in allt, "the open follow-up to correct the front door is named")
    elif tid == "T7":
        me = pkg["missing_evidence"]["model"]
        need(isinstance(me, dict) and me.get("state") == "missing", f"missing-evidence state set by the model ({me})")
        why.append(f"     script floor: missing={pkg['missing_evidence']['script']}")
        need(bool(pkg["searched"]) and len(pkg["searched"]) >= 20, f"sources searched are listed ({len(pkg['searched'])})")
        unmarked = [r["ref"] for r in pkg["results"] if re.search(r"\d+\s?%|\$\d", "\n".join(r["evidence"])) and not (r["marks"].get("claimed") or r["marks"].get("observed"))]
        need(not unmarked, f"no figure returned without a claimed or observed mark {unmarked}")
    return ok, why


def main():
    argv = sys.argv[1:]
    records = check.parse(open(LAB.register).read())
    os.makedirs(OUT, exist_ok=True)
    if "--prove-boundary" in argv:
        picks = {"picks": [{"ref": "work-os/upskill-advisor/governance/README.md", "reason": "planted: a discovery candidate, not a source"},
                           {"ref": "CLAUDE.md", "reason": "control: inside the register"}]}
        pkg = retrieve.fetch(LAB, records, "boundary control", picks)
        inside = [r["ref"] for r in pkg["results"]]
        if pkg["refused"] == ["work-os/upskill-advisor/governance/README.md"] and inside == ["CLAUDE.md"]:
            print(f"boundary refused: {pkg['refused'][0]}; control inside the register returned: {inside[0]}"); return 0
        print(f"BOUNDARY NOT ENFORCED: refused={pkg['refused']} returned={inside}"); return 1
    if "--candidates" in argv:
        for t in tests():
            res = retrieve.candidates(LAB, t["query"])
            json.dump(res, open(os.path.join(OUT, f"{t['id']}-candidates.json"), "w"), indent=1, ensure_ascii=False)
            print(f"{t['id']}: {len(res['candidates'])} deterministic candidates; exact terms {res['exact_terms']}")
        print(retrieve.stats_line()); return 0
    if "--selections" in argv:
        sel = json.load(open(argv[argv.index("--selections") + 1]))
        passed, lines = 0, []
        for t in tests():
            picks = sel.get(t["id"])
            if not picks:
                lines.append(f"FAIL {t['id']} {t['name']}: no selections"); continue
            pkg = retrieve.fetch(LAB, records, t["query"], picks, os.path.join(OUT, f"{t['id']}-scored-package.json"))
            ok, why = score(t, pkg)
            passed += ok
            sp = picks.get('semantic_pass', {})
            lines.append(f"{'PASS' if ok else 'FAIL'} {t['id']} {t['name']} ({len(pkg['results'])} results; semantic pass read {sp.get('records_read', '?')} records, {sp.get('bytes_read', '?')} bytes, scope {sp.get('scope', '?')})")
            lines += ["  " + w for w in why]
            if t.get("baseline"):
                lines += ["  baseline top lines: " + " / ".join(t["baseline"][:4])]
        print("\n".join(lines))
        print(retrieve.stats_line())
        print(f"RETRIEVAL TESTS: {passed} of {len(tests())} passed")
        return 0 if passed == len(tests()) else 1
    print(__doc__); return 2


if __name__ == "__main__":
    sys.exit(main())
