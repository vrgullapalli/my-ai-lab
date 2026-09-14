#!/usr/bin/env python3
"""state.py — State v0.1, the implementation slice of continuity (designed and approved 2026-09-13, AD-29, AD-37).

The job: say what is currently true, active, changed, open, waiting, owned, or superseded, with a pointer to the
evidence, without reading history. The spec is CAPABILITY-DEFINITIONS.md, the State subsection under continuity;
the design is docs/reports/2026-09-13--state-v0-1-design.md.

State is an index over the registries, not a second store of facts. The ledger (STATE.jsonl, one JSON object per
line, append-only, the latest line per id wins, never edited or deleted) holds only the four things no registry
holds: supersession links, ownership, commitments, and materiality. Every line points at a registry id or an
evidence anchor; a line with no resolving pointer is refused. Registries own the durable objects.

  python3 context/state/state.py check [--summary]          the sensor: refusals and conflicts, one finding per line
  python3 context/state/state.py package --scope ai-lab [--consumer x] [--fields a,b] [--since DATE] [--subject s]
                                          [--authority his-word,system,proposed] [--in-hand]
      --authority keeps only lines with those authority words in changed and decided (the brief drops derived lines,
      F-20260913-0844-1); --in-hand keeps only work someone holds, owner not Venkat, so his to-do lines stay in
      waiting and are not shown as work in progress (F-20260913-0844-2). Both decided 2026-09-14 at the brief wiring.
  python3 context/state/state.py append --by WHO --json '{...}'   one line, validated first; refused if it lies
  python3 context/state/state.py claim ID --by WHO --what "..." [--next "..."] [--source p] [--scope s]
  python3 context/state/state.py release ID --by WHO --status done|paused|handed-off [--to OWNER]
  python3 context/state/state.py from-receipt PATH --by WHO    loops opened and closed, and the next-session commitment
  python3 context/state/state.py seed --by WHO                 derive the first lines from the registries (derived authority)
  python3 context/state/state.py current                       write CURRENT.md, the generated human view

Words a script checks. kind: decision, work, loop, commitment, status. status per kind: decision current|superseded|
proposed; work active|paused|done|handed-off; loop open|closed|waiting; commitment open|kept|missed; status: the
target registry's own word. scope: ai-lab, professional, career, public, personal. authority: his-word, proposed,
system, derived. his-word needs an anchor (a #row, #line, or a receipt or transcript path) and is never written by
the seed. STATE_LEDGER in the environment points the ledger elsewhere; the tests use that.
"""
import datetime as dt
import glob
import json
import os
import re
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
LAB = os.path.dirname(os.path.dirname(HERE))
LEDGER = os.environ.get("STATE_LEDGER") or os.path.join(HERE, "STATE.jsonl")
CURRENT_MD = os.path.join(HERE, "CURRENT.md")
SENSORS = os.path.join(LAB, ".claude", "agents", "alfred", "sensors")
MAP = os.path.join(LAB, "docs", "architecture", "CAPABILITY-MAP.md")
REGISTER = os.path.join(LAB, "context", "sources", "REGISTER.md")
TODAY_MD = os.path.join(LAB, ".claude", "agents", "alfred", "TODAY.md")
RECEIPTS = os.path.join(LAB, "evidence", "receipts")
AUDITS = os.path.join(LAB, "evidence", "audits")

KINDS = {"decision": {"current", "superseded", "proposed"}, "work": {"active", "paused", "done", "handed-off"},
         "loop": {"open", "closed", "waiting"}, "commitment": {"open", "kept", "missed"}, "status": None}
SCOPES = ("ai-lab", "professional", "career", "public", "personal")
AUTHORITY = ("his-word", "proposed", "system", "derived")
REQUIRED = ("id", "kind", "what", "status", "scope", "established", "changed", "source", "authority", "by", "when")
FRESH_DAYS = {"work": 7, "commitment": 3, "loop": 14}
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
OPENED = []


def now():
    return dt.datetime.now().strftime("%Y-%m-%dT%H:%M")


def today():
    return dt.date.today().isoformat()


def read(path):
    OPENED.append(os.path.relpath(path, LAB) if path.startswith(LAB) else path)
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return ""


def lines_of(path=None):
    """Every line of the ledger, in order, with its line number. A bad line is reported, never repaired."""
    path = path or LEDGER
    out, bad = [], []
    text = read(path) if os.path.exists(path) else ""
    for n, raw in enumerate(text.split("\n"), 1):
        if not raw.strip():
            continue
        try:
            o = json.loads(raw)
            o["_line"] = n
            out.append(o)
        except ValueError:
            bad.append(n)
    return out, bad


def current_of(lines):
    cur = {}
    for o in lines:
        cur[o.get("id")] = o
    return cur


# ---- pointers -------------------------------------------------------------------------------------------------

def registry_ids(path, marker):
    text = read(path)
    m = re.search(rf"<!-- {marker}:start -->(.*?)<!-- {marker}:end -->", text, re.S)
    body = m.group(1) if m else text
    out = {}
    for block in re.split(r"\n### ", body)[1:]:
        head, _, rest = block.partition("\n")
        rid = head.strip()
        st = re.search(r"^- status: (\S+)", rest, re.M)
        ch = re.search(r"^- changed: (\S+)", rest, re.M)
        out[rid] = {"status": st.group(1) if st else "", "changed": ch.group(1) if ch else ""}
    return out


def receipt_for(rid):
    m = re.match(r"R-(\d{4}-\d{2}-\d{2})-(\d{4})-([0-9a-f]{4})$", rid)
    if not m:
        return None
    hits = glob.glob(os.path.join(RECEIPTS, f"{m.group(1)}-{m.group(2)}-*-{m.group(3)}.md"))
    return hits[0] if hits else None


def follow_up_exists(fid):
    for folder in (RECEIPTS, AUDITS):
        for root, _, files in os.walk(folder):
            for f in files:
                if f.endswith(".md") and fid in read(os.path.join(root, f)):
                    return True
    return False


def resolves(pointer, maps=None):
    """A pointer resolves when its path exists (relative to the lab, or absolute), or it is an id a registry or
    the record can resolve: a source id, a map id, a follow-up id, a receipt id."""
    p = pointer.split("#", 1)[0].strip()
    if not p:
        return False
    if os.path.exists(os.path.join(LAB, p)) or (os.path.isabs(os.path.expanduser(p)) and os.path.exists(os.path.expanduser(p))):
        return True
    maps = maps or {}
    if p in maps.get("map", {}) or p in maps.get("register", {}):
        return True
    if re.match(r"F-\d{8}-\d{4}-\d+$", p):
        return follow_up_exists(p)
    if re.match(r"R-\d{4}-\d{2}-\d{2}-\d{4}-[0-9a-f]{4}$", p):
        return receipt_for(p) is not None
    return False


def anchored(sources):
    return any("#" in s or s.split("#")[0].startswith(("evidence/receipts", "evidence/sessions")) or receipt_for(s.split("#")[0]) for s in sources)


# ---- the check ------------------------------------------------------------------------------------------------

def finding(what, evidence, why, level="show at open", nxt="fix the line by appending a corrected one; never edit"):
    return f"[{level}] {what} | system: continuity/state | evidence: {evidence} | why: {why} | next: {nxt} | status: open"


def check_line(o, maps):
    """Hard refusals for one line. Returns a list of reasons; empty means the line may be appended."""
    why = []
    for k in REQUIRED:
        if k not in o or o[k] in ("", None, []):
            why.append(f"missing {k}")
    if why:
        return why
    kind = o["kind"]
    if kind not in KINDS:
        why.append(f"unknown kind {kind}")
    elif KINDS[kind] is not None and o["status"] not in KINDS[kind]:
        why.append(f"status '{o['status']}' is not a {kind} word ({', '.join(sorted(KINDS[kind]))})")
    if not str(o["id"]).startswith(f"{kind}:"):
        why.append(f"id must start with '{kind}:'")
    if o["scope"] not in SCOPES:
        why.append(f"scope '{o['scope']}' is not one of {', '.join(SCOPES)}")
    if o["authority"] not in AUTHORITY:
        why.append(f"authority '{o['authority']}' is not one of {', '.join(AUTHORITY)}")
    srcs = o["source"] if isinstance(o["source"], list) else [o["source"]]
    dead = [s for s in srcs if not resolves(s, maps)]
    if dead:
        why.append(f"source does not resolve: {'; '.join(dead)}")
    if o["authority"] == "his-word":
        if not anchored(srcs):
            why.append("his-word without an anchor (a #row or #line anchor, or a receipt or transcript path)")
        if str(o["by"]).startswith("seed/"):
            why.append("his-word written by the seed; the seed writes derived lines only")
    for k in ("established", "changed"):
        if not DATE.match(str(o.get(k, ""))):
            why.append(f"{k} is not a date")
    return why


def check(lines, maps, bad_lines=()):
    """Every refusal and conflict across the ledger, one finding each. Reports, never fixes."""
    out = []
    for n in bad_lines:
        out.append(finding("ledger line is not JSON", f"STATE.jsonl line {n}", "a line a script cannot read is a line nobody can trust", "interrupt him"))
    for o in lines:
        for w in check_line(o, maps):
            out.append(finding(f"line refused: {w}", f"{o.get('id', '?')} at line {o['_line']}", "a State line that lies is worse than none"))
    # ownership: a work line that takes an active claim from a different owner without a release in between
    last = {}
    for o in lines:
        if o.get("kind") != "work":
            continue
        prev = last.get(o["id"])
        if prev and prev.get("status") == "active" and o.get("status") == "active" and prev.get("owner") != o.get("owner"):
            out.append(finding(f"ownership overwritten: {o['id']} was active for {prev.get('owner')} and is now active for {o.get('owner')}",
                               f"lines {prev['_line']} and {o['_line']}", "parallel work on one thing; the plan said refuse, never overwrite",
                               nxt="release or hand off first, then claim"))
        last[o["id"]] = o
    cur = current_of(lines)
    # two current successors for one superseded decision
    succ = {}
    for o in cur.values():
        if o.get("kind") == "decision" and o.get("status") == "current":
            for s in o.get("supersedes", []) or []:
                succ.setdefault(s, []).append(o["id"])
    for s, ids in succ.items():
        if len(ids) > 1:
            out.append(finding(f"two current successors for {s}: {', '.join(ids)}", s, "a consumer cannot tell which ruling governs", "interrupt him",
                               "his word on which stands; then one superseded line"))
    # a status line that disagrees with its registry
    for o in cur.values():
        if o.get("kind") != "status":
            continue
        m = re.match(r"status:(capability|source)/(.+)$", o["id"])
        if not m:
            continue
        reg = maps["map"] if m.group(1) == "capability" else maps["register"]
        entry = reg.get(m.group(2))
        if entry and entry["status"] and entry["status"] != o.get("status"):
            out.append(finding(f"status disagrees with its registry: {o['id']} says {o.get('status')}, the registry says {entry['status']}",
                               o["id"], "the registry is canonical; State is an overlay", nxt="append a line with the registry's word, or fix the registry at his word"))
    return out


def stale_of(cur, maps):
    out = []
    td = dt.date.today()
    for o in cur.values():
        kind = o.get("kind")
        if kind in FRESH_DAYS and o.get("status") in ("active", "paused", "open", "waiting"):
            try:
                age = (td - dt.date.fromisoformat(o["changed"])).days
            except ValueError:
                continue
            if age > FRESH_DAYS[kind]:
                out.append({"id": o["id"], "kind": kind, "age_days": age, "fresh_days": FRESH_DAYS[kind], "source": o["source"]})
        if kind == "status":
            m = re.match(r"status:(capability|source)/(.+)$", o["id"])
            if m:
                reg = maps["map"] if m.group(1) == "capability" else maps["register"]
                entry = reg.get(m.group(2))
                if entry and entry["changed"] and entry["changed"] > o.get("changed", ""):
                    out.append({"id": o["id"], "kind": kind, "registry_changed": entry["changed"], "line_changed": o.get("changed"), "source": o["source"]})
    return out


def load_maps():
    return {"map": registry_ids(MAP, "registry"), "register": registry_ids(REGISTER, "register")}


def counts(cur):
    c = {k: 0 for k in KINDS}
    for o in cur.values():
        if o.get("kind") in c:
            c[o["kind"]] += 1
    return c


def cmd_check(argv):
    lines, bad = lines_of()
    maps = load_maps()
    finds = check(lines, maps, bad)
    cur = current_of(lines)
    st = stale_of(cur, maps)
    c = counts(cur)
    conflicts = [f for f in finds if "ownership overwritten" in f or "two current successors" in f or "disagrees with its registry" in f]
    scopes = sorted({o.get("scope") for o in cur.values()})
    summary = (f"state: {len(cur)} current lines ({c['decision']} decisions, {c['work']} work, {c['loop']} loops, {c['commitment']} commitments, "
               f"{c['status']} statuses) in {len(scopes)} scope(s); conflicts {len(conflicts)}; stale {len(st)}; findings {len(finds)} (python3 context/state/state.py check)")
    if "--summary" in argv:
        print(("ALERT " if finds else "") + summary)
        return 1 if finds else 0
    for f in finds:
        print(f)
    for s in st:
        print(f"[record only] stale: {s['id']} | system: continuity/state | evidence: {json.dumps(s)} | why: older than its kind's freshness | next: refresh or close it | status: open")
    print(("FAIL " if finds else "OK ") + summary)
    return 1 if finds else 0


# ---- writing --------------------------------------------------------------------------------------------------

def append(o, by, maps=None):
    """Validate, then append. Refuses a line that lies. Never edits."""
    maps = maps or load_maps()
    o = dict(o)
    o.setdefault("by", by)
    o.setdefault("when", now())
    o.setdefault("established", today())
    o.setdefault("changed", today())
    if isinstance(o.get("source"), str):
        o["source"] = [o["source"]]
    why = check_line(o, maps)
    if why:
        return None, why
    o.pop("_line", None)
    with open(LEDGER, "a", encoding="utf-8") as f:
        f.write(json.dumps(o, ensure_ascii=False) + "\n")
    return o, []


def cmd_append(argv):
    by = opt(argv, "--by")
    raw = opt(argv, "--json")
    if not by or not raw:
        print("usage: append --by WHO --json '{...}'"); return 2
    o, why = append(json.loads(raw), by)
    if why:
        print("REFUSED: " + "; ".join(why)); return 1
    print(f"appended {o['id']} ({o['kind']} {o['status']})"); return 0


def cmd_claim(argv):
    wid, by = argv[0] if argv and not argv[0].startswith("--") else None, opt(argv, "--by")
    if not wid or not by:
        print("usage: claim work:ID --by WHO --what '...' [--next '...'] [--source p] [--scope s]"); return 2
    if not wid.startswith("work:"):
        wid = "work:" + wid
    lines, _ = lines_of()
    cur = current_of(lines).get(wid)
    if cur and cur.get("status") == "active" and cur.get("owner") != by:
        print(f"REFUSED: {wid} is active for {cur.get('owner')} since {cur.get('established')} (line {cur['_line']}); release or hand off first"); return 1
    o = {"id": wid, "kind": "work", "what": opt(argv, "--what") or (cur or {}).get("what", ""), "status": "active",
         "scope": opt(argv, "--scope") or (cur or {}).get("scope", "ai-lab"), "owner": by,
         "source": (opt(argv, "--source") or ";".join((cur or {}).get("source", []))).split(";"),
         "authority": "system", "established": (cur or {}).get("established") or today(), "changed": today()}
    if opt(argv, "--next"):
        o["next"] = opt(argv, "--next")
    if opt(argv, "--subject"):
        o["subject"] = opt(argv, "--subject")
    o, why = append(o, by)
    if why:
        print("REFUSED: " + "; ".join(why)); return 1
    print(f"claimed {wid} for {by}"); return 0


def cmd_release(argv):
    wid, by, status = argv[0] if argv and not argv[0].startswith("--") else None, opt(argv, "--by"), opt(argv, "--status", "done")
    if not wid or not by or status not in ("done", "paused", "handed-off"):
        print("usage: release work:ID --by WHO --status done|paused|handed-off [--to OWNER] [--next '...']"); return 2
    if not wid.startswith("work:"):
        wid = "work:" + wid
    lines, _ = lines_of()
    cur = current_of(lines).get(wid)
    if not cur:
        print(f"REFUSED: {wid} has no line to release"); return 1
    o = {k: cur[k] for k in cur if not k.startswith("_")}
    o.update({"status": status, "changed": today(), "owner": opt(argv, "--to") or (by if status != "handed-off" else cur.get("owner")), "by": by, "when": now()})
    if status == "handed-off" and opt(argv, "--to"):
        o["owner"] = opt(argv, "--to")
    if opt(argv, "--next"):
        o["next"] = opt(argv, "--next")
    if opt(argv, "--source"):
        o["source"] = list(dict.fromkeys(o["source"] + opt(argv, "--source").split(";")))
    o, why = append(o, by)
    if why:
        print("REFUSED: " + "; ".join(why)); return 1
    print(f"released {wid}: {status}" + (f" to {o['owner']}" if status == "handed-off" else "")); return 0


FOLLOW_RE = re.compile(r"^- \[( |x)\] (F-\d{8}-\d{4}-\d+): (.*?)(?: — owner: ([^—]+?))?(?: — first step: (.*))?$", re.M)   # re.M: the one local correction, 2026-09-13; without it the open follow-ups were never read


def cmd_from_receipt(argv):
    """The deterministic half of the close routine's State write: loops opened and closed, and the commitment."""
    path, by = argv[0] if argv else None, opt(argv, "--by")
    if not path or not by:
        print("usage: from-receipt PATH --by WHO"); return 2
    full = path if os.path.isabs(path) else os.path.join(LAB, path)
    text = read(full)
    rel = os.path.relpath(full, LAB)
    rid = (re.search(r"^id: (R-\S+)", text, re.M) or [None, ""])[1]
    date = (re.search(r"^date: (\d{4}-\d{2}-\d{2})", text, re.M) or [None, today()])[1]
    maps = load_maps()
    written, refused, skipped = [], [], 0
    cur0 = current_of(lines_of()[0])

    def same(o):
        h = cur0.get(o["id"])
        return bool(h) and h.get("status") == o["status"] and rel in h.get("source", [])
    for m in FOLLOW_RE.finditer(text):
        box, fid, what, owner, step = m.groups()
        owner = (owner or "Alfred").strip()
        o = {"id": f"loop:{fid}", "kind": "loop", "what": what.strip(), "status": "waiting" if owner.lower().startswith("venkat") else "open",
             "scope": "ai-lab", "owner": owner, "source": [rel], "authority": "system",
             "established": f"{fid[2:6]}-{fid[6:8]}-{fid[8:10]}", "changed": date}
        if step:
            o["next"] = step.strip()
        if same(o):
            skipped += 1; continue
        o, why = append(o, by, maps)
        (written if o else refused).append(o["id"] if o else f"loop:{fid}: {why}")
    closed = re.search(r"^## Closed\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    if closed:
        for m in re.finditer(r"^- (F-\d{8}-\d{4}-\d+) — (.*)$", closed.group(1), re.M):
            fid, ev = m.groups()
            lines, _ = lines_of()
            prev = current_of(lines).get(f"loop:{fid}", {})
            o = {"id": f"loop:{fid}", "kind": "loop", "what": prev.get("what") or ev.strip()[:160], "status": "closed", "scope": prev.get("scope", "ai-lab"),
                 "owner": prev.get("owner", "Alfred"), "source": [rel], "authority": "system", "established": prev.get("established") or date, "changed": date,
                 "note": ev.strip()[:200]}
            if same(o):
                skipped += 1; continue
            o, why = append(o, by, maps)
            (written if o else refused).append(o["id"] if o else f"loop:{fid}: {why}")
    nxt = re.search(r"\*\*Next session starts with:\*\*\s*(.*)", text)
    if nxt and rid:
        whole = nxt.group(1).strip()
        what, _, step = whole.partition(" — first step:")
        o = {"id": f"commitment:{rid}/next", "kind": "commitment", "what": what.strip()[:300], "status": "open", "scope": "ai-lab",
             "owner": "Alfred", "source": [rel], "authority": "system", "established": date, "changed": date}
        if step.strip():
            o["next"] = step.strip()[:300]
        if same(o):
            skipped += 1
        else:
            o, why = append(o, by, maps)
            (written if o else refused).append(o["id"] if o else f"commitment: {why}")
            if o:
                # one open "next session starts with" at a time: the newest governs, the older ones are carried into it (2026-09-14)
                for old in list(cur0.values()):
                    if old.get("kind") == "commitment" and old.get("status") == "open" and old["id"].endswith("/next") and old["id"] != o["id"]:
                        k = {k2: v for k2, v in old.items() if not k2.startswith("_")}
                        k.update({"status": "kept", "changed": date, "note": f"carried into {o['id']}", "source": list(dict.fromkeys(k.get("source", []) + [rel]))})
                        w, _ = append(k, by, maps)
                        if w:
                            written.append(w["id"] + " (carried)")
    print(f"from-receipt {rel}: {len(written)} lines written, {skipped} already current" + (f"; {len(refused)} refused: {refused}" if refused else ""))
    return 0 if not refused else 1


# ---- the seed -------------------------------------------------------------------------------------------------

DECISION_FILES = (("brand-os", "work-os/brand-os/DECISIONS.md"), ("rulings-in-force", "RULINGS-IN-FORCE.md"),
                  ("architecture", "docs/architecture/ARCHITECTURE-DECISIONS.md"), ("upskill", "work-os/upskill-advisor/records/decisions.md"))
TELEGRAPH_DECISIONS = ("telegraph-plus", "work-os/projects/telegraph-plus/records/views/DECISIONS.md")
ROW = re.compile(r"^\|\s*\**((?:[A-Z]+-)?\d{2,3})\**\s*\|(.*)$")
CORRECTS = re.compile(r"(?:Correction to|corrects|supersedes|replaces row)\s+\**((?:[A-Z]+-)?\d{2,3})", re.I)
APPROVED = re.compile(r"((?:[A-Z]+-)?\d{2,3})(?: and [A-Z]+-\d{2,3})?\s+(?:stands|approved|is history|are history)", re.I)


def seed_decisions(by, maps):
    out = []
    for ns, rel in DECISION_FILES:
        text = read(os.path.join(LAB, rel))
        rows = []
        for line in text.split("\n"):
            m = ROW.match(line)
            if not m or m.group(1) in ("#", "ID"):
                continue
            cells = [c.strip() for c in m.group(2).split("|")]
            date = next((c for c in cells if DATE.match(c)), "")
            body = max(cells, key=len) if cells else ""
            rows.append({"id": m.group(1), "date": date, "cells": cells, "body": body, "text": line})
        seen = set()
        for i, r in enumerate(rows):
            if r["id"] in seen:
                continue
            seen.add(r["id"])
            later = " ".join(x["text"] for x in rows[i + 1:])
            status = "current"
            who = " ".join(c for c in r["cells"] if len(c) < 80).lower()
            if ("proposed" in who or "assumed" in who) and not re.search(rf"\b{re.escape(r['id'])}\b[^|]*?(stands|approved|is history|are history|this row is the ruling)", later, re.I) \
                    and not re.search(rf"AD-\d+ and {re.escape(r['id'])} approved|{re.escape(r['id'])} and AD-\d+ approved", later, re.I):
                status = "proposed"
            sup = [f"decision:{ns}/{c}" for c in CORRECTS.findall(r["body"]) if c != r["id"]]
            title = re.search(r"\*\*(.+?)\*\*", r["body"])
            what = (title.group(1) if title else r["body"])[:200]
            o = {"id": f"decision:{ns}/{r['id']}", "kind": "decision", "what": what, "status": status, "scope": "ai-lab", "owner": "Venkat",
                 "source": [f"{rel}#row:{r['id']}"], "authority": "derived", "established": r["date"] or today(), "changed": r["date"] or today()}
            if sup:
                o["supersedes"] = sup
            out.append(o)
        # the corrected rows become superseded
        by_id = {o["id"]: o for o in out}
        for o in list(out):
            for s in o.get("supersedes", []):
                if s in by_id and o["status"] == "current":
                    by_id[s]["status"] = "superseded"
                    by_id[s]["superseded_by"] = o["id"]
                    by_id[s]["changed"] = max(by_id[s]["changed"], o["changed"])
    ns, rel = TELEGRAPH_DECISIONS
    text = read(os.path.join(LAB, rel))
    for m in re.finditer(r"^### (DEC-\d{3}) — (.+?)\n(.*?)(?=^### |\Z)", text, re.M | re.S):
        did, title, body = m.groups()
        when = re.search(r"\*\*When:\*\* (\d{4}-\d{2}-\d{2})", body)
        o = {"id": f"decision:{ns}/{did}", "kind": "decision", "what": title.strip()[:200], "status": "current", "scope": "ai-lab", "owner": "Venkat",
             "source": [f"{rel}#{did}"], "authority": "derived", "established": when.group(1) if when else today(), "changed": when.group(1) if when else today()}
        sup = [f"decision:{ns}/{c}" for c in re.findall(r"supersedes (DEC-\d{3})", body)]
        if sup:
            o["supersedes"] = sup
        out.append(o)
    return out


def seed_loops():
    out = []
    try:
        txt = subprocess.run([sys.executable, os.path.join(SENSORS, "facts.py"), "loops"], capture_output=True, text=True, timeout=120).stdout
    except Exception:
        return out
    for line in txt.split("\n"):
        m = re.match(r"\s+(F-\d{8}-\d{4}-\d+) \((\d+) days, from ([^)]+)\): (.*)", line)
        if not m:
            continue
        fid, _, src, text = m.groups()
        what, _, rest = text.partition(" — owner:")
        owner = rest.split(" — first step:")[0].strip() or "Alfred"
        step = (re.search(r"first step: (.*)$", rest) or [None, ""])[1].strip()
        where = "evidence/receipts/" + src if os.path.exists(os.path.join(RECEIPTS, src)) else (glob.glob(os.path.join(AUDITS, "*", src)) or [None])[0]
        where = os.path.relpath(where, LAB) if where and os.path.isabs(where) else where
        if not where:
            continue
        o = {"id": f"loop:{fid}", "kind": "loop", "what": what.strip()[:300], "status": "waiting" if owner.lower().startswith("venkat") else "open",
             "scope": "ai-lab", "owner": owner, "source": [where], "authority": "system", "established": f"{fid[2:6]}-{fid[6:8]}-{fid[8:10]}",
             "changed": f"{fid[2:6]}-{fid[6:8]}-{fid[8:10]}"}
        if step:
            o["next"] = step[:300]
        out.append(o)
    return out


def seed_commitment():
    files = sorted(glob.glob(os.path.join(RECEIPTS, "20*-*.md")))
    files = [f for f in files if "--day-review" not in f and "--today-list" not in f and "--gates" not in f]
    for f in reversed(files):
        text = read(f)
        rid = (re.search(r"^id: (R-\S+)", text, re.M) or [None, ""])[1]
        nxt = re.search(r"\*\*Next session starts with:\*\*\s*(.*)", text)
        date = (re.search(r"^date: (\d{4}-\d{2}-\d{2})", text, re.M) or [None, today()])[1]
        if rid and nxt:
            return [{"id": f"commitment:{rid}/next", "kind": "commitment", "what": nxt.group(1).strip()[:300], "status": "open", "scope": "ai-lab",
                     "owner": "Alfred", "source": [os.path.relpath(f, LAB)], "authority": "system", "established": date, "changed": date}]
    return []


def seed_work():
    out = []
    text = read(TODAY_MD)
    date = (re.search(r"(\d{4}-\d{2}-\d{2})", text.split("\n")[0]) or [None, today()])[1]
    for n, line in enumerate(text.split("\n"), 1):
        m = re.match(r"- \[ \] \*\*(.+?)\*\*", line)
        if not m:
            continue
        title = m.group(1).strip()
        owner = "Venkat"
        om = re.match(r"(Venkat|Alfred):\s*(.*)", title)
        if om:
            owner, title = om.group(1), om.group(2)
        slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")[:60]
        out.append({"id": f"work:today/{slug}", "kind": "work", "what": title[:200], "status": "active", "scope": "ai-lab", "owner": owner,
                    "source": [f".claude/agents/alfred/TODAY.md#line:{n}"], "authority": "system", "established": date, "changed": date})
    return out


def seed_statuses(maps):
    out = []
    for rid, e in maps["map"].items():
        out.append({"id": f"status:capability/{rid}", "kind": "status", "what": f"capability {rid} status", "status": e["status"], "scope": "ai-lab", "owner": "capability-architecture",
                    "source": [f"docs/architecture/CAPABILITY-MAP.md#{rid}"], "authority": "derived", "established": e["changed"] or today(), "changed": e["changed"] or today()})
    for rid, e in maps["register"].items():
        out.append({"id": f"status:source/{rid}", "kind": "status", "what": f"source {rid} status", "status": e["status"], "scope": "ai-lab", "owner": "retrieval",
                    "source": [f"context/sources/REGISTER.md#{rid}"], "authority": "derived", "established": e["changed"] or today(), "changed": e["changed"] or today()})
    return out


def cmd_seed(argv):
    by = opt(argv, "--by") or "seed/unknown"
    if not by.startswith("seed/"):
        by = "seed/" + by
    maps = load_maps()
    lines, _ = lines_of()
    cur = current_of(lines)
    cands = seed_decisions(by, maps) + seed_loops() + seed_commitment() + seed_work() + seed_statuses(maps)
    written = skipped = refused = 0
    for o in cands:
        have = cur.get(o["id"])
        same = have and all(have.get(k) == o.get(k) for k in ("status", "what", "owner")) and (have.get("supersedes") == o.get("supersedes")) and (have.get("superseded_by") == o.get("superseded_by"))
        if same:
            skipped += 1
            continue
        if have and have.get("authority") == "his-word" and have.get("status") == o.get("status"):
            skipped += 1          # never overwrite his word with a derivation that agrees
            continue
        w, why = append(o, by, maps)
        if w:
            written += 1
        else:
            refused += 1
            print(f"refused {o['id']}: {'; '.join(why)}")
    print(f"seed: {written} lines written, {skipped} unchanged, {refused} refused (derived authority; nothing hand-written)")
    return 0


# ---- the package ----------------------------------------------------------------------------------------------

def opt(argv, name, default=None):
    return argv[argv.index(name) + 1] if name in argv and argv.index(name) + 1 < len(argv) else default


def age(o):
    try:
        return (dt.date.today() - dt.date.fromisoformat(o.get("established") or o.get("changed"))).days
    except (ValueError, TypeError):
        return None


def slim(o):
    return {k: v for k, v in o.items() if not k.startswith("_")}


def waiting_homes():
    """The three homes of 'waiting on Venkat', read as one list with the source of each item. waiting.py owns the readers."""
    sys.path.insert(0, SENSORS)
    try:
        import waiting  # noqa: E402
    except Exception:
        return []
    out = []
    for r in (waiting.today_items() + waiting.telegraph_items()):
        out.append({"id": r.get("id") or f"{r['kind']}:{re.sub(r'[^a-z0-9]+', '-', r['what'].lower())[:50]}", "what": r["what"], "owner": "Venkat",
                    "home": r["source"], "source": [r["source"]], "next": r.get("step", "")[:200], "authority": "system"})
    OPENED.extend([os.path.relpath(TODAY_MD, LAB), "work-os/upskill-advisor/records/open-items.md"])
    return out


def closed_but_listed(cur):
    """A loop closed in the ledger whose id still sits unchecked in TODAY.md."""
    text = read(TODAY_MD)
    out = []
    for o in cur.values():
        if o.get("kind") == "loop" and o.get("status") == "closed":
            fid = o["id"].split(":", 1)[1]
            for n, line in enumerate(text.split("\n"), 1):
                if line.startswith("- [ ]") and fid in line:
                    out.append({"kind": "closed-but-listed", "id": o["id"], "where": f".claude/agents/alfred/TODAY.md#line:{n}", "why": "closed in a receipt, still open on his list"})
    return out


def cmd_package(argv):
    t0 = time.time()
    scope = opt(argv, "--scope", "ai-lab")
    consumer = opt(argv, "--consumer", "session")
    since = opt(argv, "--since", (dt.date.today() - dt.timedelta(days=1)).isoformat())
    subject = opt(argv, "--subject")
    auth = opt(argv, "--authority")
    auth = set(auth.split(",")) if auth else None
    in_hand = "--in-hand" in argv
    fields = opt(argv, "--fields")
    fields = set(fields.split(",")) if fields else None
    lines, bad = lines_of()
    maps = load_maps()
    cur = current_of(lines)
    mine, other = {}, 0
    for o in cur.values():
        if subject and o.get("subject") != subject:
            continue
        if o.get("scope") == scope:
            mine[o["id"]] = o
        else:
            other += 1
    newest = lambda xs: sorted(xs, key=lambda o: (o.get("changed", ""), o.get("when", "")), reverse=True)
    decided = []
    for o in newest([o for o in mine.values() if o["kind"] == "decision" and o["status"] in ("current", "proposed") and (not auth or o.get("authority") in auth)]):
        decided.append(slim(o))
        for s in o.get("supersedes", []) or []:
            p = cur.get(s)
            if p and (not subject or p.get("subject") == subject or True):
                decided.append({**slim(p), "status": "superseded", "superseded_by": p.get("superseded_by") or o["id"]})
    finds = check(lines, maps, bad)
    pkg = {
        "as_of": now(), "scope": scope, "consumer": consumer, "since": since,
        "active": [dict(slim(o), since=o.get("established")) for o in newest([o for o in mine.values() if o["kind"] == "work" and o["status"] in ("active", "paused")
                                                                                and not (in_hand and str(o.get("owner", "")).lower().startswith("venkat"))])],
        "decided": decided,
        "changed": [slim(o) for o in newest([o for o in mine.values() if o.get("changed", "") >= since and (not auth or o.get("authority") in auth)])],
        "open": [dict(slim(o), age_days=age(o)) for o in newest([o for o in mine.values() if o["kind"] == "loop" and o["status"] in ("open", "waiting")])],
        "waiting": [dict(slim(o), age_days=age(o), home=o["source"][0]) for o in newest([o for o in mine.values() if o["kind"] in ("loop", "commitment") and o["status"] in ("open", "waiting")
                    and str(o.get("owner", "")).lower().startswith("venkat")])] + (waiting_homes() if scope == "ai-lab" and (not fields or "waiting" in fields) else []),
        "ownership": {},
        "superseded": [slim(o) for o in newest([o for o in mine.values() if o["kind"] == "decision" and o["status"] == "superseded" and o.get("changed", "") >= since])],
        "carry_forward": sorted([slim(o) for o in mine.values() if o["kind"] == "commitment" and o["status"] == "open"],
                                key=lambda o: (not o["id"].endswith("/next"), o.get("established", "")), reverse=False),
        "conflicts": [f for f in finds if "ownership overwritten" in f or "two current successors" in f or "disagrees with its registry" in f] + (closed_but_listed(mine) if scope == "ai-lab" else []),
        "stale": [s for s in stale_of(cur, maps) if cur[s["id"]].get("scope") == scope],
        "withheld": other,
        "refused_lines": [f for f in finds if "line refused" in f],
    }
    pkg["carry_forward"] = sorted(pkg["carry_forward"], key=lambda o: (0 if o["id"].endswith("/next") else 1, o.get("when", ""), o.get("established", "")), reverse=False)
    pkg["carry_forward"] = sorted(pkg["carry_forward"], key=lambda o: (1 if o["id"].endswith("/next") else 0, o.get("when", ""), o.get("established", "")), reverse=True)
    pkg["filters"] = {"authority": sorted(auth) if auth else None, "in_hand": in_hand, "subject": subject}
    for o in pkg["active"]:
        pkg["ownership"].setdefault(o.get("owner", "?"), []).append(o["id"])
    if fields:
        keep = fields | {"as_of", "scope", "consumer", "since", "withheld", "refused_lines"}
        pkg = {k: v for k, v in pkg.items() if k in keep}
    pkg["opened"] = sorted(set(OPENED))
    pkg["built_in_seconds"] = round(time.time() - t0, 3)
    print(json.dumps(pkg, ensure_ascii=False, indent=1))
    return 0


# ---- the view -------------------------------------------------------------------------------------------------

def cmd_current(argv):
    lines, bad = lines_of()
    maps = load_maps()
    cur = current_of(lines)
    c = counts(cur)
    finds = check(lines, maps, bad)
    st = stale_of(cur, maps)
    out = [f"# Current state — generated {now()} from STATE.jsonl", "",
           "**This is a view, not the record.** The record is `STATE.jsonl` beside this file (append-only, latest line per id wins). "
           "Regenerate with `python3 context/state/state.py current`. Do not edit this file.", "",
           f"{len(cur)} current lines: {c['decision']} decisions, {c['work']} work, {c['loop']} loops, {c['commitment']} commitments, {c['status']} statuses. "
           f"Findings {len(finds)}, stale {len(st)}.", ""]
    def sec(title, rows):
        out.append(f"## {title} ({len(rows)})")
        out.append("")
        for o in rows[:40]:
            extra = f" — owner {o.get('owner')}" if o.get("owner") else ""
            sup = f" — supersedes {', '.join(o['supersedes'])}" if o.get("supersedes") else ""
            out.append(f"- `{o['id']}` {o.get('status')}: {o.get('what', '')[:140]}{extra}{sup} — {o.get('authority')} — {o['source'][0]}")
        if len(rows) > 40:
            out.append(f"- … and {len(rows) - 40} more")
        out.append("")
    newest = lambda xs: sorted(xs, key=lambda o: o.get("changed", ""), reverse=True)
    sec("Active work", newest([o for o in cur.values() if o["kind"] == "work" and o["status"] in ("active", "paused")]))
    sec("Carry forward", newest([o for o in cur.values() if o["kind"] == "commitment" and o["status"] == "open"]))
    sec("Waiting on Venkat (ledger loops)", newest([o for o in cur.values() if o["kind"] == "loop" and o["status"] == "waiting"]))
    sec("Open loops (others)", newest([o for o in cur.values() if o["kind"] == "loop" and o["status"] == "open"]))
    sec("Decisions changed in the last 3 days", [o for o in newest([o for o in cur.values() if o["kind"] == "decision"]) if o.get("changed", "") >= (dt.date.today() - dt.timedelta(days=3)).isoformat()])
    out.append(f"## Conflicts and refusals ({len(finds)})")
    out.append("")
    out += [f"- {f}" for f in finds] or ["- none"]
    out.append("")
    out.append(f"## Stale ({len(st)})")
    out.append("")
    out += [f"- `{s['id']}` {json.dumps({k: v for k, v in s.items() if k not in ('id', 'source')})}" for s in st[:30]] or ["- none"]
    out.append("")
    with open(CURRENT_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print(f"wrote {os.path.relpath(CURRENT_MD, LAB)}: {len(cur)} current lines, {len(finds)} findings, {len(st)} stale")
    return 0


def main():
    argv = sys.argv[1:]
    if not argv:
        print(__doc__); return 2
    cmds = {"check": cmd_check, "package": cmd_package, "append": cmd_append, "claim": cmd_claim, "release": cmd_release,
            "from-receipt": cmd_from_receipt, "seed": cmd_seed, "current": cmd_current}
    if argv[0] not in cmds:
        print(__doc__); return 2
    return cmds[argv[0]](argv[1:])


if __name__ == "__main__":
    sys.exit(main())
