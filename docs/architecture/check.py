#!/usr/bin/env python3
"""check.py — the sensor for the capability architecture. Deterministic; reports, never fixes.

  python3 docs/architecture/check.py             # findings, one line each; exit 1 if any
  python3 docs/architecture/check.py --summary   # one line for Alfred's facts sheet
  python3 docs/architecture/check.py <folder>    # same checks on another copy (to prove the check can fail)

Runs from context-check.sh (section G) and from facts.py (one line at every session start).

Checks (2026-09-12, the registry standard made testable):
  1. The registry block in CAPABILITY-MAP.md parses; each record has the required fields.
  2. Every status is one of: planned, building, live, degraded, retired.
  3. Ids are unique, and each heading equals its id.
  4. Every registry id has a definition heading in CAPABILITY-DEFINITIONS.md, and the other way round.
  5. Every path in canonical-store and sensors exists under the lab root ("not decided" and "none" allowed).
  6. added and changed are dates.
  7. Every id in related: is a registry id (relationships by stable reference).
  8. No two entries claim the same canonical-store path (competing canonical records).
  9. No other live markdown file in the lab carries a registry block (a second copy of the registry).
 10. A live or degraded entry carries '- proof:' (the building-to-live gate, AD-15).

Every finding is one line with the seven fields of the sensor standard:
  [materiality] what | system | evidence | why | next | status
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
LAB = os.path.dirname(os.path.dirname(HERE))
SYSTEM = "capability-architecture"
STATUSES = {"planned", "building", "live", "degraded", "retired"}
REQUIRED = ("id", "family", "status", "job", "canonical-store", "access", "consumers", "sensors",
            "defined-in", "added", "changed")
ALLOWED_WORDS = re.compile(r"^(not decided|none)\b", re.I)
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
MARKER = "<!-- registry:start -->"
SKIP_DIRS = {".git", "node_modules", "sessions", "_archive", ".playwright-mcp", "__pycache__"}


def finding(what, evidence, why, nxt, materiality="show at open"):
    return f"[{materiality}] {what} | system: {SYSTEM} | evidence: {evidence} | why: {why} | next: {nxt} | status: open"


def registry(text):
    start, end = text.find(MARKER), text.find("<!-- registry:end -->")
    if start < 0 or end < 0:
        return None
    records, current = [], None
    for line in text[start:end].split("\n"):
        if line.startswith("### "):
            current = {"_heading": line[4:].strip()}
            records.append(current)
        elif line.startswith("- ") and current is not None:
            key, _, value = line[2:].partition(":")
            current[key.strip()] = value.strip()
    return records


def definitions(text):
    body = text.split("\n## Definitions", 1)
    if len(body) < 2:
        return set()
    return {re.sub(r"\s*\(.*\)$", "", h.strip()) for h in re.findall(r"^### (.+)$", body[1], re.M)}


def paths(value):
    """Split a field on ';' and return the parts that look like lab paths."""
    out = []
    for part in value.split(";"):
        part = part.strip()
        if not part or ALLOWED_WORDS.match(part):
            continue
        token = part.split(" ")[0]
        if "/" in token or token.endswith((".md", ".py", ".sh")):
            out.append(token.split("#")[0].split("<")[0].rstrip("/"))
    return out


def other_registry_blocks(folder):
    """Live markdown files outside the map that carry a registry block."""
    hits = []
    keep = os.path.join(folder, "CAPABILITY-MAP.md")
    for root, dirs, files in os.walk(LAB):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in files:
            if not f.endswith(".md"):
                continue
            p = os.path.join(root, f)
            if os.path.abspath(p) == os.path.abspath(keep):
                continue
            try:
                if MARKER in open(p, errors="ignore").read():
                    hits.append(os.path.relpath(p, LAB))
            except OSError:
                pass
    return hits


def run(folder):
    findings = []
    map_path = os.path.join(folder, "CAPABILITY-MAP.md")
    def_path = os.path.join(folder, "CAPABILITY-DEFINITIONS.md")
    for p in (map_path, def_path):
        if not os.path.isfile(p):
            return [finding(f"{os.path.basename(p)} missing", p, "the architecture record has two files and one is gone",
                            "restore it from git", "interrupt him")], 0, 0
    map_text, def_text = open(map_path).read(), open(def_path).read()
    records = registry(map_text)
    if records is None:
        return [finding("registry markers missing", map_path, "without the markers no script can read the registry",
                        "put the registry:start and registry:end comments back", "interrupt him")], 0, 0
    ids = [r.get("id", r["_heading"]) for r in records]
    stores = {}
    for r in records:
        rid = r.get("id", r["_heading"])
        where = f"CAPABILITY-MAP.md ### {r['_heading']}"
        if rid != r["_heading"]:
            findings.append(finding(f"heading '{r['_heading']}' differs from id '{rid}'", where,
                                    "the heading is how a reader finds the record; the id is how a script does",
                                    "make them the same word"))
        if r.get("status") in ("live", "degraded") and not r.get("proof"):
            findings.append(finding(f"{rid}: {r['status']} with no '- proof:' line", where,
                                    "the building-to-live gate needs operational behavior, failure proof, and a valid contract (AD-15)",
                                    "add '- proof:' naming where the failure proof is, or set the status back to building"))
        for k in REQUIRED:
            if not r.get(k):
                findings.append(finding(f"{rid}: missing '{k}'", where,
                                        "a record a script cannot read is not a record", f"add '- {k}:' to the entry"))
        if r.get("status") and r["status"] not in STATUSES:
            findings.append(finding(f"{rid}: status '{r['status']}' is not a registry status", where,
                                    "status must be one of five words so a script can read it",
                                    "use planned, building, live, degraded, or retired"))
        for k in ("added", "changed"):
            if r.get(k) and not DATE.match(r[k]):
                findings.append(finding(f"{rid}: {k} '{r[k]}' is not a date", where,
                                        "timestamps are how freshness is measured", "write YYYY-MM-DD"))
        for k in ("canonical-store", "sensors"):
            for p in paths(r.get(k, "")):
                if not os.path.exists(os.path.join(LAB, p)):
                    findings.append(finding(f"{rid}: {k} path does not exist: {p}", where,
                                            "the record points at nothing, so the map is wrong about the lab",
                                            "fix the path, or set the entry to retired with a dated line"))
        for p in paths(r.get("canonical-store", "")):
            stores.setdefault(p, []).append(rid)
        anchor = r.get("defined-in", "").split("#")[-1]
        if anchor and anchor != rid:
            findings.append(finding(f"{rid}: defined-in anchor '{anchor}' differs from id", where,
                                    "the pointer to the definition must be the id", f"write CAPABILITY-DEFINITIONS.md#{rid}"))
        for rel in [x.strip() for x in r.get("related", "").split(",") if x.strip()]:
            if rel not in ids:
                findings.append(finding(f"{rid}: related id '{rel}' is not in the registry", where,
                                        "relationships are by stable reference, never by a name that is not registered",
                                        "use a registry id, or drop it"))
    for d in sorted({i for i in ids if ids.count(i) > 1}):
        findings.append(finding(f"id '{d}' appears {ids.count(d)} times", "CAPABILITY-MAP.md registry block",
                                "two records with one id means no stable reference", "keep one record; retire the other"))
    for p, owners in sorted(stores.items()):
        if len(owners) > 1:
            findings.append(finding(f"two entries claim one canonical store: {p} ({', '.join(owners)})",
                                    "CAPABILITY-MAP.md canonical-store fields",
                                    "one home per fact; two capabilities on one store are competing records",
                                    "merge them, or make one the owner and the other a consumer"))
    defs = definitions(def_text)
    for rid in ids:
        if rid not in defs:
            findings.append(finding(f"{rid}: no definition heading", "CAPABILITY-DEFINITIONS.md ## Definitions",
                                    "an entry with no definition has no job, consumers, or sensors written down",
                                    f"add '### {rid}' under Definitions using the shared system standard"))
    for d in sorted(defs - set(ids)):
        findings.append(finding(f"definition '{d}' has no registry entry", f"CAPABILITY-DEFINITIONS.md ### {d}",
                                "a definition nobody registered is a second source of truth",
                                "register it in CAPABILITY-MAP.md, or move the text under the entry it belongs to"))
    for hit in other_registry_blocks(folder):
        findings.append(finding(f"a second registry block lives in {hit}", hit,
                                "a second copy of the registry is a second source of truth",
                                "remove the copy, or mark it a generated view without the markers"))
    return findings, len(records), len(defs)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    folder = args[0] if args else HERE
    findings, n_rec, n_def = run(folder)
    summary = f"architecture check: {n_rec} registry entries, {n_def} definitions; {len(findings)} finding(s)"
    if "--summary" in sys.argv:
        tail = " (python3 docs/architecture/check.py)" if findings else ""
        print(("ALERT " if findings else "") + summary + tail)
    elif findings:
        print("FAIL " + summary)
        for f in findings:
            print("  " + f)
    else:
        print("OK " + summary + "; statuses valid; paths exist")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
