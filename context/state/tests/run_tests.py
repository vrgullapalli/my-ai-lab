#!/usr/bin/env python3
"""Runner for the five frozen State tests (STATE-TESTS.md). Scores each pass condition on the Current State Package
the script returns; never on a judgment. S1 and S4 run on the real ledger; S2, S3, and S5 run on throwaway ledgers
so nothing they write reaches the record. Prints "STATE TESTS: n of 5 passed".

Run:  python3 context/state/tests/run_tests.py
"""
import json
import os
import subprocess
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(os.path.dirname(HERE), "state.py")
LAB = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
REAL = os.path.join(os.path.dirname(HERE), "STATE.jsonl")
tmp = tempfile.mkdtemp(prefix="state-tests-")
passed, lines = 0, []


def run(ledger, *args):
    r = subprocess.run([sys.executable, STATE] + list(args), capture_output=True, text=True, env=dict(os.environ, STATE_LEDGER=ledger), cwd=LAB, timeout=120)
    return r.returncode, r.stdout, r.stderr


def package(ledger, *args):
    t0 = time.time()
    rc, out, err = run(ledger, "package", *args)
    try:
        return json.loads(out), time.time() - t0
    except ValueError:
        return {"error": out + err}, time.time() - t0


def append(ledger, by, o):
    rc, out, err = run(ledger, "append", "--by", by, "--json", json.dumps(o))
    return rc == 0, out + err


def score(tid, name, conds):
    global passed
    ok = all(c for c, _ in conds)
    passed += ok
    lines.append(f"{'PASS' if ok else 'FAIL'} {tid} {name}")
    lines.extend(f"  {'ok  ' if c else 'FAIL'} {w}" for c, w in conds)


def by_id(items, key):
    return next((o for o in items if o.get("id") == key), None)


# S1 — real ledger
pkg, secs = package(REAL, "--fields", "decided", "--subject", "career-advisor-drop")
d = pkg.get("decided", [])
r37, r36 = by_id(d, "decision:brand-os/037"), by_id(d, "decision:brand-os/036")
opened = pkg.get("opened", [])
score("S1", "current versus superseded, without reading history", [
    (r37 is not None and r37.get("status") == "current" and "decision:brand-os/036" in r37.get("supersedes", []), "037 current and supersedes 036"),
    (r36 is not None and r36.get("status") == "superseded" and r36.get("superseded_by") == "decision:brand-os/037", "036 superseded by 037"),
    (bool(r37 and r36) and all(any("#row:" in s for s in o["source"]) and o.get("authority") for o in (r37, r36)), "each carries its row anchor and an authority"),
    (not any(p.startswith(("evidence/sessions", "evidence/receipts")) for p in opened), f"no transcript or receipt was opened ({len(opened)} files: {opened[:3]})"),
    (secs < 2, f"package built in {secs:.2f}s"),
])

# S2 — throwaway ledger, two sessions
L2 = os.path.join(tmp, "s2.jsonl")
src = "docs/reports/2026-09-13--retrieval-v0-1-close-out.md"
rcA, outA, _ = run(L2, "claim", "work:retrieval-v0-1-close-out", "--by", "session-A", "--what", "close Retrieval v0.1", "--next", "run the seven", "--source", src)
pkgB, _ = package(L2, "--fields", "active,ownership")
wB = by_id(pkgB.get("active", []), "work:retrieval-v0-1-close-out")
rcB, outB, _ = run(L2, "claim", "work:retrieval-v0-1-close-out", "--by", "session-B", "--what", "close Retrieval v0.1")
rcChk, outChk, _ = run(L2, "check")
rcR, outR, _ = run(L2, "release", "work:retrieval-v0-1-close-out", "--by", "session-A", "--status", "paused", "--next", "hand to the next session")
pkgN, _ = package(L2, "--fields", "active")
wN = by_id(pkgN.get("active", []), "work:retrieval-v0-1-close-out")
score("S2", "ownership across parallel sessions", [
    (rcA == 0, "session A claims the work"),
    (wB is not None and wB.get("status") == "active" and wB.get("owner") == "session-A" and wB.get("since") and wB.get("next"), "B's package shows the work active, owner A, since, next"),
    (rcB == 1 and "session-A" in outB and "REFUSED" in outB, "B's claim is refused with the owner named"),
    (rcChk == 0, "no silent overwrite: the ledger has no ownership conflict after the refusal"),
    (rcR == 0 and wN is not None and wN.get("status") == "paused", "A's close writes a paused line and the next open shows it"),
])

# S3 — throwaway ledger, a close then a new session
L3 = os.path.join(tmp, "s3.jsonl")
rcpt = "evidence/receipts/2026-09-13-0638-pushed-sensor-fixed-state-designed-2b87.md"
okA, _ = append(L3, "alfred-close/s3", {"id": "loop:F-20260913-0638-1", "kind": "loop", "what": "rule on the State design's two forks", "status": "waiting", "scope": "ai-lab",
                                          "owner": "Venkat", "established": "2026-09-13", "changed": "2026-09-13", "source": [rcpt], "authority": "system", "next": "two words and freeze"})
okB, _ = append(L3, "alfred-close/s3", {"id": "loop:F-20260913-0602-1", "kind": "loop", "what": "push the two repos", "status": "open", "scope": "ai-lab", "owner": "Venkat",
                                          "established": "2026-09-13", "changed": "2026-09-12", "source": [rcpt], "authority": "system"})
okC, _ = append(L3, "alfred-close/s3", {"id": "loop:F-20260913-0602-1", "kind": "loop", "what": "push the two repos", "status": "closed", "scope": "ai-lab", "owner": "Venkat",
                                          "established": "2026-09-13", "changed": "2026-09-13", "source": [rcpt], "authority": "system", "note": "both pushes ran at his word 06:30"})
okD, _ = append(L3, "alfred-close/s3", {"id": "commitment:R-2026-09-13-0638-2b87/next", "kind": "commitment", "what": "his two words on the State design", "status": "open",
                                          "scope": "ai-lab", "owner": "Alfred", "established": "2026-09-13", "changed": "2026-09-13", "source": [rcpt], "authority": "system"})
pkg3, _ = package(L3, "--since", "2026-09-13")
op = by_id(pkg3.get("open", []), "loop:F-20260913-0638-1")
closed_open = by_id(pkg3.get("open", []), "loop:F-20260913-0602-1")
closed_changed = by_id(pkg3.get("changed", []), "loop:F-20260913-0602-1")
cf = pkg3.get("carry_forward", [])
waiting = pkg3.get("waiting", [])
homes = {w.get("home", (w.get("source") or [""])[0]) for w in waiting}
active_ids = {o["id"] for o in pkg3.get("active", [])}
score("S3", "open, waiting, and carry-forward survive a close", [
    (all((okA, okB, okC, okD)), "the close wrote one waiting loop, one closed loop, and one commitment"),
    (op is not None and op.get("owner") == "Venkat" and op.get("age_days") is not None, "the new session's package holds the open loop with owner and age"),
    (closed_open is None and closed_changed is not None and closed_changed.get("status") == "closed", "the closed loop is absent from open and present in changed"),
    (bool(cf) and cf[0]["id"] == "commitment:R-2026-09-13-0638-2b87/next", "the commitment is first in carry_forward"),
    (len(homes) >= 3 and all(w.get("source") for w in waiting), f"waiting is one list from all three homes with a source on each item ({len(homes)} homes, {len(waiting)} items)"),
    ("loop:F-20260913-0638-1" not in active_ids and not any(o["id"].startswith("loop:") for o in pkg3.get("active", [])), "his item stays waiting and is not re-queued as active work"),
])

# S4 — real ledger
pkg4, _ = package(REAL, "--fields", "changed", "--since", "2026-09-12")
ch = pkg4.get("changed", [])
live = by_id(ch, "status:capability/retrieval")
t2 = by_id(ch, "status:retrieval/T2-known-limitation")
noise = [o for o in ch if any(s.startswith(("context/sources/index", "evidence/sessions")) for s in o.get("source", []))]
rcpt_id = "2026-09-13-0602-retrieval-live-tool-reverted-4f7b"
cites = [o for o in ch if any(rcpt_id in s for s in o.get("source", []))]
score("S4", "a material change carries its source; a trivial one does not appear", [
    (live is not None and live.get("status") == "live" and any("#row:AD-36" in s for s in live["source"]) and any(rcpt_id in s for s in live["source"]) and live.get("authority") == "his-word",
     "retrieval building to live, sourced to the AD-36 row and the receipt, his word"),
    (t2 is not None and t2.get("authority") == "system", "the T2 limitation is a status line with authority system"),
    (not noise, f"no derived index files or re-rendered transcripts in changed ({len(ch)} changes)"),
    (all(o.get("source") for o in ch), "every change carries a source"),
    (bool(cites), f"the 06:02 receipt's decisions have State lines that cite it ({len(cites)})"),
])

# S5 — throwaway ledger, a synthetic Professional / Advisory scenario (marked synthetic; the Use Case Registry has no file yet)
L5 = os.path.join(tmp, "s5.jsonl")
scen = os.path.join(tmp, "scenario-synthetic.md")
with open(scen, "w") as f:
    f.write("# Synthetic scenario (S5). Not a real account.\n\n## decisions\n- D1 positioning v1\n- D2 positioning v2, replaces D1\n\n## loops\n- L1 the client contact owes the claims list\n")
common = {"scope": "professional", "established": "2026-09-01", "changed": "2026-09-12", "authority": "system", "note": "synthetic scenario, S5"}
rows = [
    dict(common, id="decision:account-x/D1", kind="decision", what="Brand X positioning v1", status="superseded", superseded_by="decision:account-x/D2", subject="brand:X", owner="client-lead", source=[scen + "#D1"]),
    dict(common, id="decision:account-x/D2", kind="decision", what="Brand X positioning v2, replaces v1", status="current", supersedes=["decision:account-x/D1"], subject="brand:X", owner="client-lead", source=[scen + "#D2"]),
    dict(common, id="loop:account-x/L1", kind="loop", what="the client contact owes the claims list", status="open", subject="brand:X", owner="client-contact", source=[scen + "#L1"], next="ask at Friday's call"),
    dict(common, id="commitment:account-x/C1", kind="commitment", what="deliver the positioning deck by 2026-09-19", status="open", subject="brand:X", owner="Venkat", source=[scen], next="draft by Wednesday"),
    dict(common, id="status:account-x/workflow", kind="status", what="claims review workflow", status="in-review", subject="brand:X", owner="client-lead", source=[scen]),
    dict(common, id="work:account-x/campaign-q4", kind="work", what="Q4 campaign plan for brand X", status="active", subject="campaign:Y", owner="Venkat", source=[scen]),
]
oks = [append(L5, "alfred-close/s5", r)[0] for r in rows]
p5, _ = package(L5, "--scope", "professional", "--subject", "brand:X")
d5 = p5.get("decided", [])
cur5, old5 = by_id(d5, "decision:account-x/D2"), by_id(d5, "decision:account-x/D1")
l5 = by_id(p5.get("open", []), "loop:account-x/L1")
c5 = by_id(p5.get("carry_forward", []), "commitment:account-x/C1")
s5 = by_id(p5.get("changed", []), "status:account-x/workflow")
p5lab, _ = package(L5, "--scope", "ai-lab")
leaked = json.dumps({k: v for k, v in p5lab.items() if k not in ("opened",)}).count("account-x")
rcC, outC, _ = run(L5, "claim", "work:account-x/campaign-q4", "--by", "another-session", "--what", "take the campaign")
score("S5", "scoped commercial state, same kinds, withheld across scopes (synthetic)", [
    (all(oks), "all six professional lines were accepted by the check"),
    (cur5 is not None and cur5.get("status") == "current" and old5 is not None and old5.get("status") == "superseded", "the current decision with its predecessor superseded"),
    (l5 is not None and l5.get("owner") == "client-contact", "the open loop with the external owner"),
    (c5 is not None and s5 is not None, "the commitment and the workflow status are present"),
    (all(o.get("source") for o in d5 + p5.get("open", []) + p5.get("carry_forward", [])), "each with a pointer"),
    (leaked == 0 and p5lab.get("withheld") == 6, f"the ai-lab package holds none of the content and withheld: {p5lab.get('withheld')}"),
    (rcC == 1 and "Venkat" in outC, "S2's claim refusal holds on a professional work line"),
])

print("\n".join(lines))
print(f"STATE TESTS: {passed} of 5 passed  (scratch folder: {tmp})")
sys.exit(0 if passed == 5 else 1)
