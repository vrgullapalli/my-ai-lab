#!/usr/bin/env python3
"""Planted-fault tests for the State check (context/state/state.py). Each fault is written to a throwaway ledger and
the check must refuse or flag it; the clean ledger must pass. Prints "all passed" only when every case holds.

Run:  python3 context/state/tests/check_tests.py
"""
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(os.path.dirname(HERE), "state.py")
LAB = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
tmp = tempfile.mkdtemp(prefix="state-check-tests-")
failures = 0


def ledger(name, lines):
    p = os.path.join(tmp, name + ".jsonl")
    with open(p, "w") as f:
        for o in lines:
            f.write(json.dumps(o) + "\n")
    return p


def run(path, *args):
    r = subprocess.run([sys.executable, STATE] + list(args), capture_output=True, text=True, env=dict(os.environ, STATE_LEDGER=path), cwd=LAB, timeout=120)
    return r.returncode, r.stdout + r.stderr


def check(name, ok, detail=""):
    global failures
    failures += 0 if ok else 1
    print(f"  {'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail[:200]})" if detail and not ok else ""))


BASE = {"kind": "decision", "what": "a ruling", "status": "current", "scope": "ai-lab", "owner": "Venkat", "established": "2026-09-10", "changed": "2026-09-10",
        "source": ["work-os/brand-os/DECISIONS.md#row:037"], "authority": "his-word", "by": "alfred-close/test", "when": "2026-09-13T07:00"}
good = [dict(BASE, id="decision:brand-os/037", supersedes=["decision:brand-os/036"]),
        dict(BASE, id="decision:brand-os/036", status="superseded", superseded_by="decision:brand-os/037", source=["work-os/brand-os/DECISIONS.md#row:036"]),
        {"id": "work:w1", "kind": "work", "what": "a job", "status": "active", "scope": "ai-lab", "owner": "A", "established": "2026-09-13", "changed": "2026-09-13",
         "source": ["docs/reports/2026-09-13--state-v0-1-design.md"], "authority": "system", "by": "A", "when": "2026-09-13T07:00"}]

rc, out = run(ledger("clean", good), "check")
check("clean ledger passes the check", rc == 0 and "findings 0" in out, out)

faults = {
    "no pointer": dict(BASE, id="decision:brand-os/038", source=["docs/nowhere/missing.md#row:1"]),
    "bad scope word": dict(BASE, id="decision:brand-os/038", scope="everywhere"),
    "bad status word for the kind": dict(BASE, id="decision:brand-os/038", status="active"),
    "bad authority word": dict(BASE, id="decision:brand-os/038", authority="gospel"),
    "his-word without an anchor": dict(BASE, id="decision:brand-os/038", source=["docs/reports/2026-09-13--state-v0-1-design.md"]),
    "derived shown as his word (written by the seed)": dict(BASE, id="decision:brand-os/038", by="seed/test"),
    "missing required field": {k: v for k, v in dict(BASE, id="decision:brand-os/038").items() if k != "established"},
    "id does not start with its kind": dict(BASE, id="ruling:brand-os/038"),
    "not a date": dict(BASE, id="decision:brand-os/038", changed="yesterday"),
}
for name, bad in faults.items():
    rc, out = run(ledger("fault", good + [bad]), "check")
    check(f"planted fault refused: {name}", rc == 1 and "line refused" in out, out)

# conflicts across lines
rc, out = run(ledger("two-owners", good + [dict(good[2], owner="B", by="B", when="2026-09-13T07:05")]), "check")
check("planted fault flagged: ownership overwritten without a release", rc == 1 and "ownership overwritten" in out, out)
rc, out = run(ledger("two-successors", good + [dict(BASE, id="decision:brand-os/039", supersedes=["decision:brand-os/036"], source=["work-os/brand-os/DECISIONS.md#row:037"])]), "check")
check("planted fault flagged: two current successors for one decision", rc == 1 and "two current successors" in out, out)
rc, out = run(ledger("status-disagrees", good + [{"id": "status:capability/retrieval", "kind": "status", "what": "x", "status": "planned", "scope": "ai-lab", "owner": "x",
                                                   "established": "2026-09-13", "changed": "2026-09-13", "source": ["docs/architecture/CAPABILITY-MAP.md#retrieval"],
                                                   "authority": "derived", "by": "seed/test", "when": "2026-09-13T07:00"}]), "check")
check("planted fault flagged: a status line that disagrees with its registry", rc == 1 and "disagrees with its registry" in out, out)
with open(os.path.join(tmp, "notjson.jsonl"), "w") as f:
    f.write(json.dumps(good[0]) + "\nthis is not json\n")
rc, out = run(os.path.join(tmp, "notjson.jsonl"), "check")
check("planted fault flagged: a ledger line that is not JSON", rc == 1 and "not JSON" in out, out)

# the writers refuse too
p = ledger("append", good)
rc, out = run(p, "append", "--by", "test", "--json", json.dumps(dict(BASE, id="decision:brand-os/040", source=["docs/nowhere.md#row:1"])))
check("append refuses a line with no resolving pointer", rc == 1 and "REFUSED" in out, out)
rc, out = run(p, "claim", "work:w1", "--by", "B", "--what", "take it")
check("claim refuses to take active work from another owner and names the owner", rc == 1 and "REFUSED" in out and "active for A" in out, out)
rc, out = run(p, "claim", "work:w2", "--by", "B", "--what", "new work", "--source", "docs/reports/2026-09-13--state-v0-1-design.md")
check("claim succeeds on unclaimed work", rc == 0 and "claimed work:w2" in out, out)
rc, out = run(p, "release", "work:w1", "--by", "A", "--status", "paused")
rc2, out2 = run(p, "claim", "work:w1", "--by", "B", "--what", "take it")
check("after a release, another owner may claim, and the check stays clean", rc == 0 and rc2 == 0 and run(p, "check")[0] == 0, out + out2)

# from-receipt: the deterministic close path reads open follow-ups, closed ones, and the next-session line (regression for the 2026-09-13 correction)
rcpt = os.path.join(tmp, "2026-09-13-0900-test-receipt-abcd.md")
with open(rcpt, "w") as f:
    f.write("---\nid: R-2026-09-13-0900-abcd\ntype: receipt\ndate: 2026-09-13\n---\n# Session receipt\n\n**Next session starts with:** the next thing — first step: do it\n\n"
            "## Follow-ups\n\n- [ ] F-20260913-0900-1: an open ask — owner: Venkat — first step: one word\n- [ ] F-20260913-0900-2: an Alfred ask — owner: Alfred — first step: run it\n\n"
            "## Closed\n\n- F-20260913-0638-9 — done, the evidence\n")
p2 = ledger("from-receipt", good)
rc, out = run(p2, "from-receipt", rcpt, "--by", "alfred-close/test")
check("from-receipt writes the open loops, the closed loop, and the commitment (4 lines)", rc == 0 and "4 lines written" in out, out)
rc, out = run(p2, "package", "--fields", "open,waiting,carry_forward")
pk = json.loads(out) if rc == 0 else {}
check("the waiting loop carries owner Venkat and the commitment leads carry_forward",
      any(o["id"] == "loop:F-20260913-0900-1" and o["status"] == "waiting" for o in pk.get("open", [])) and pk.get("carry_forward", [{}])[0].get("id") == "commitment:R-2026-09-13-0900-abcd/next", out[:300])
rc, out = run(p2, "from-receipt", rcpt, "--by", "alfred-close/test")
check("from-receipt run twice writes nothing new (idempotent)", rc == 0 and "0 lines written, 4 already current" in out, out)

print(f"\n{'all passed' if not failures else str(failures) + ' failed'}  (scratch folder: {tmp})")
sys.exit(1 if failures else 0)
