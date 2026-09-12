#!/usr/bin/env python3
"""check.py — retrieval's first sensor: the source register, source health, coverage, freshness, and source discovery.
Deterministic; reports, never fixes, never registers a source.

  python3 context/sources/check.py                 # findings, one line each; exit 1 on any register or health finding
  python3 context/sources/check.py --report        # plus one coverage line per source (files, newest change, who reads it)
  python3 context/sources/check.py --summary       # one line for Alfred's facts sheet
  python3 context/sources/check.py resolve <id>    # source id -> where it is now, status, standing, and its use limits
  python3 context/sources/check.py list            # one line per source: id, status, standing, use, tier
  python3 context/sources/check.py --lab <dir>     # run against another lab root (the tests build a small one)
  python3 context/sources/check.py <REGISTER.md>   # check another copy of the register only (no discovery)

Register (the registry standard on this register):
  ids unique and equal to headings; required fields present; status, standing, use, and tier from the allowed words;
  a replica names canonical-at; added and changed are dates; no two sources claim one location.
Health (for every live or degraded source):
  missing (location not there; says where a file or folder of that name is now, if one exists);
  unreadable (there, but this user cannot read it); empty (there, but no file matches the pattern);
  an unavailable source that is reachable now (record only, so a person can promote it).
  External sources (an absolute or ~ location, outside the lab) are checked for existence and readability, never counted.
Coverage and freshness: files matching pattern under each location inside the lab; the newest change per source.
Source discovery (AD-08; recommends review, never registers):
  git repos not under any registered location; folders with 10 or more markdown files that no source covers;
  data files (csv, json, jsonl) outside registered sources; web domains named 20 or more times across live markdown;
  the count of unreviewed broken paths from dead-pointers.py.
  Reviewed and left on purpose: context/sources/discovery-accepted.txt, one line with a reason.

Every finding is one line with the seven fields of the sensor standard:
  [materiality] what | system | evidence | why | next | status
"""
import datetime as dt
import fnmatch, os, re, subprocess, sys
from collections import Counter

SYSTEM = "retrieval"
STATUSES = {"planned", "building", "live", "degraded", "retired"}      # AD-05, the registry standard's five words
STANDINGS = {"canonical", "replica", "historical", "unavailable"}     # where this copy stands
USES = {"authoritative", "evidentiary", "contextual", "exploratory"}  # the strongest job the source may carry
TIERS = {"his-ruling", "his-words", "endorsed", "system", "proposed", "generated", "mixed"}
REQUIRED = ("id", "kind", "location", "pattern", "owner", "standing", "tier", "date-field", "status",
            "use", "may-inform", "not-alone", "read-by", "added", "changed")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".playwright-mcp", ".remember", ".unlazy", ".DS_Store", ".next", "out"}
DOC_FOLDER_MIN, DOMAIN_MIN = 10, 20
DOMAIN = re.compile(r"https?://([a-zA-Z0-9.-]+)")


class Lab:
    """Paths for one lab root. The default is the lab this file lives in; --lab points at another."""
    def __init__(self, root):
        self.root = os.path.abspath(root)
        self.here = os.path.join(self.root, "context", "sources")
        self.register = os.path.join(self.here, "REGISTER.md")
        self.accepted = os.path.join(self.here, "discovery-accepted.txt")
        self.dead_pointers = os.path.join(self.root, ".claude", "skills", "context-check", "dead-pointers.py")

    def where(self, loc):
        """A location's full path and whether it is external (outside the lab: absolute or ~)."""
        if loc.startswith("~") or loc.startswith("/"):
            return os.path.expanduser(loc), True
        return os.path.join(self.root, loc), False


def finding(what, evidence, why, nxt, materiality="show at open"):
    return f"[{materiality}] {what} | system: {SYSTEM} | evidence: {evidence} | why: {why} | next: {nxt} | status: open"


def parse(text):
    start, end = text.find("<!-- register:start -->"), text.find("<!-- register:end -->")
    if start < 0 or end < 0:
        return None
    records, cur = [], None
    for line in text[start:end].split("\n"):
        if line.startswith("### "):
            cur = {"_heading": line[4:].strip()}
            records.append(cur)
        elif line.startswith("- ") and cur is not None:
            k, _, v = line[2:].partition(":")
            cur[k.strip()] = v.strip()
    return records


def rid(r):
    return r.get("id", r["_heading"])


def split(value):
    return [p.strip() for p in value.split(";") if p.strip()]


def accepted(lab):
    out = set()
    if os.path.isfile(lab.accepted):
        for line in open(lab.accepted):
            line = line.strip()
            if line and not line.startswith("#"):
                out.add(line.split("|")[0].strip().rstrip("/"))
    return out


def under(rel, locations):
    return any(rel == loc or rel.startswith(loc + "/") for loc in locations)


def matches(name, rel, patterns):
    for p in patterns:
        if "/" in p:
            if fnmatch.fnmatch(rel, "*/" + p) or fnmatch.fnmatch(rel, p):
                return True
        elif fnmatch.fnmatch(name, p):
            return True
    return False


def files_for(lab, location, patterns):
    """Files under a location (or the file itself) matching any pattern; a pattern with a slash matches the tail of the path."""
    full, _ = lab.where(location)
    if os.path.isfile(full):
        return [full] if matches(os.path.basename(full), full, patterns) else []
    out = []
    for root, dirs, names in os.walk(full):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for n in names:
            if matches(n, os.path.relpath(os.path.join(root, n), lab.root), patterns):
                out.append(os.path.join(root, n))
    return out


def find_moved(lab, name, limit=3):
    """Where a file or folder of this name is now, inside the lab. For the 'moved' hint; never a fix."""
    hits = []
    for root, dirs, names in os.walk(lab.root):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for n in dirs + names:
            if n == name:
                hits.append(os.path.relpath(os.path.join(root, n), lab.root))
                if len(hits) >= limit:
                    return hits
    return hits


def integrity(lab, records):
    findings = []
    ids = [rid(r) for r in records]
    for r in records:
        i, where = rid(r), f"REGISTER.md ### {r['_heading']}"
        if i != r["_heading"]:
            findings.append(finding(f"heading '{r['_heading']}' differs from id '{i}'", where,
                                    "the heading is how a reader finds the record; the id is how a script does", "make them the same word"))
        for k in REQUIRED:
            if not r.get(k):
                findings.append(finding(f"{i}: missing '{k}'", where, "a record a script cannot read is not a record", f"add '- {k}:'"))
        for k, allowed in (("status", STATUSES), ("standing", STANDINGS), ("use", USES), ("tier", TIERS)):
            if r.get(k) and r[k] not in allowed:
                findings.append(finding(f"{i}: {k} '{r[k]}' is not an allowed word", where,
                                        f"{k} must be one word a script can read; retrieval weighs results by it",
                                        "use " + ", ".join(sorted(allowed))))
        if r.get("tier") == "mixed" and not r.get("tier-field"):
            findings.append(finding(f"{i}: tier is mixed but no tier-field", where,
                                    "mixed means each record carries its own tier; the register must say where", "add '- tier-field:'"))
        if r.get("standing") == "replica" and not r.get("canonical-at"):
            findings.append(finding(f"{i}: standing is replica but no canonical-at", where,
                                    "a copy must say where the original is, or it becomes a second source of truth", "add '- canonical-at:'"))
        for k in ("added", "changed"):
            if r.get(k) and not DATE.match(r[k]):
                findings.append(finding(f"{i}: {k} '{r[k]}' is not a date", where, "timestamps are how freshness is measured", "write YYYY-MM-DD"))
    for d in sorted({i for i in ids if ids.count(i) > 1}):
        findings.append(finding(f"id '{d}' appears {ids.count(d)} times", "REGISTER.md", "two records with one id means no stable reference", "keep one record"))
    seen = {}
    for r in records:
        for loc in split(r.get("location", "")):
            seen.setdefault(loc.rstrip("/"), []).append(rid(r))
    for loc, owners in sorted(seen.items()):
        if len(owners) > 1:
            findings.append(finding(f"two sources claim one location: {loc} ({', '.join(owners)})", "REGISTER.md location fields",
                                    "one home per fact; a file counted twice is weighed twice", "give the location to one source"))
    return findings


def health(lab, records):
    """Missing, unreadable, empty, or an unavailable source that is reachable now."""
    findings, notes = [], []
    for r in records:
        if r.get("status") not in ("live", "degraded"):
            continue
        i, where = rid(r), f"REGISTER.md ### {r['_heading']}"
        patterns = split(r.get("pattern", "*"))
        for loc in split(r.get("location", "")):
            full, external = lab.where(loc)
            exists = os.path.exists(full)
            if r.get("standing") == "unavailable":
                if exists:
                    notes.append(finding(f"{i}: unavailable source is reachable now: {loc}", where,
                                         "the register says retrieval cannot reach it, and today it can",
                                         "review it; if it is the real thing, change its standing", "record only"))
                continue
            if not exists:
                moved = [] if external else find_moved(lab, os.path.basename(loc.rstrip("/")))
                hint = f"; a {'file' if os.path.isfile(os.path.join(lab.root, moved[0])) else 'folder'} of that name is at {', '.join(moved)}" if moved else ""
                findings.append(finding(f"{i}: location missing: {loc}{hint}", where,
                                        "retrieval would read from a place that is not there",
                                        "fix the path, or set the source to retired with a dated line"))
            elif not os.access(full, os.R_OK):
                findings.append(finding(f"{i}: location unreadable: {loc}", where,
                                        "it is there, and this user cannot read it", "check permissions or Full Disk Access"))
            elif not external and os.path.isdir(full) and not files_for(lab, loc, patterns):
                findings.append(finding(f"{i}: location holds no file matching {'; '.join(patterns)}: {loc}", where,
                                        "a registered source with nothing to read is a broken canonical location",
                                        "fix the pattern, or the location, or retire the source"))
    return findings, notes


def coverage(lab, records):
    rows, total, newest = [], 0, 0.0
    for r in records:
        if r.get("status") not in ("live", "degraded"):
            continue
        locs = split(r.get("location", ""))
        if any(lab.where(l)[1] for l in locs) or r.get("standing") == "unavailable":
            rows.append((rid(r), None, 0.0, r.get("read-by", "")))
            continue
        files = []
        for loc in locs:
            files += files_for(lab, loc, split(r.get("pattern", "*")))
        mt = max((os.path.getmtime(f) for f in files), default=0.0)
        rows.append((rid(r), len(files), mt, r.get("read-by", "")))
        total += len(files)
        newest = max(newest, mt)
    return rows, total, newest


def discovery(lab, records, acc):
    findings = []
    live_locs = [loc.rstrip("/") for r in records if r.get("status") in ("live", "degraded")
                 for loc in split(r.get("location", "")) if not lab.where(loc)[1]]
    quiet = lambda rel: under(rel, list(acc)) or rel in acc
    # 1. git repos not under a registered source
    for root, dirs, names in os.walk(lab.root):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        if ".git" in os.listdir(root) and root != lab.root:
            rel = os.path.relpath(root, lab.root)
            if not under(rel, live_locs) and not quiet(rel):
                findings.append(finding(f"git repo not under any registered source: {rel}", rel,
                                        "a repo is a body of work; if it holds knowledge, retrieval cannot see it",
                                        "register it, or add it to discovery-accepted.txt with a reason"))
        if root.count(os.sep) - lab.root.count(os.sep) >= 4:
            dirs[:] = []
    # 2. folders with many markdown files no source covers; 3. data files outside sources
    md_by_folder, data_files = Counter(), []
    for root, dirs, names in os.walk(lab.root):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        rel_root = os.path.relpath(root, lab.root)
        if rel_root == ".":
            rel_root = ""
        for n in names:
            rel = os.path.join(rel_root, n) if rel_root else n
            if n.startswith(".") or under(rel, live_locs) or quiet(rel) or quiet(rel_root):
                continue
            if n.endswith(".md"):
                md_by_folder[rel_root or "(lab root)"] += 1
            elif n.endswith((".csv", ".jsonl", ".json")):
                data_files.append(rel)
    for folder, n in sorted(md_by_folder.items(), key=lambda x: -x[1]):
        if n >= DOC_FOLDER_MIN:
            findings.append(finding(f"folder with {n} markdown files that no source covers: {folder}", folder,
                                    "a collection this size is usually knowledge or history; either way retrieval should know which",
                                    "register it, or accept it with a reason"))
    if data_files:
        head = ", ".join(data_files[:3]) + (" ..." if len(data_files) > 3 else "")
        findings.append(finding(f"{len(data_files)} data file(s) outside registered sources", head,
                                "datasets are sources too; unregistered ones cannot be weighed or dated",
                                "register the folder that holds them, or accept it with a reason"))
    # 4. repeated web domains across live markdown, outside transcripts
    domains = Counter()
    for root, dirs, names in os.walk(lab.root):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and d not in ("sessions", "_archive")]
        for n in names:
            if n.endswith(".md"):
                try:
                    domains.update(d.lower().removeprefix("www.") for d in DOMAIN.findall(open(os.path.join(root, n), errors="ignore").read()))
                except OSError:
                    pass
    for dom, n in domains.most_common():
        if n < DOMAIN_MIN:
            break
        if dom not in acc:
            findings.append(finding(f"web domain named {n} times across live files: {dom}", dom,
                                    "a domain the lab keeps citing is an outside source retrieval cannot reach yet",
                                    "decide whether it is a source to register later, or accept it with a reason", "record only"))
    # 5. broken paths, counted from the existing sensor
    if os.path.isfile(lab.dead_pointers):
        try:
            out = subprocess.run([sys.executable, lab.dead_pointers], capture_output=True, text=True, timeout=120, cwd=lab.root).stdout
            n = len(re.findall(r"^\s+line \d+", out, re.M))
            if n:
                findings.append(finding(f"{n} unreviewed broken path(s) in live files", "python3 .claude/skills/context-check/dead-pointers.py",
                                        "some point at useful material that moved; retrieval should not inherit them",
                                        "review them with dead-pointers-accepted.txt; the ones that name useful material become register lines", "record only"))
        except Exception:
            pass
    return findings


def resolve(lab, records, want):
    """The one deterministic path from a source id to where it is now and what it may carry."""
    for r in records:
        if rid(r) != want:
            continue
        lines = [f"id: {want}", f"status: {r.get('status', '?')}", f"standing: {r.get('standing', '?')}"]
        if r.get("status") not in ("live", "degraded"):
            lines.append(f"read: no ({r.get('status', '?')}; not a source retrieval may read)")
        for loc in split(r.get("location", "")):
            full, external = lab.where(loc)
            state = "exists" if os.path.exists(full) else "MISSING"
            lines.append(f"location: {loc} ({state}{'; external, outside the lab' if external else ''})")
        for k in ("canonical-at", "pattern", "kind", "owner", "tier", "tier-field", "date-field", "use", "may-inform", "not-alone", "rule", "read-by", "notes", "changed"):
            if r.get(k):
                lines.append(f"{k}: {r[k]}")
        print("\n".join(lines))
        return 0
    print(f"not registered: {want} (python3 context/sources/check.py list shows the ids)")
    return 1


def main():
    argv = sys.argv[1:]
    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    if "--lab" in argv:
        k = argv.index("--lab"); root = argv[k + 1]; del argv[k:k + 2]
    lab = Lab(root)
    flags = [a for a in argv if a.startswith("--")]
    args = [a for a in argv if not a.startswith("--")]
    cmd = args[0] if args and args[0] in ("resolve", "list") else None
    path = args[0] if args and not cmd else lab.register
    if not os.path.isfile(path):
        print(f"ALERT sources: register missing ({path})"); return 1
    records = parse(open(path).read())
    if records is None:
        print("ALERT sources: register markers missing in " + path); return 1
    if cmd == "resolve":
        if len(args) < 2:
            print("usage: check.py resolve <id>"); return 2
        return resolve(lab, records, args[1])
    if cmd == "list":
        for r in records:
            print(f"{rid(r):<18} {r.get('status', '?'):<9} {r.get('standing', '?'):<12} {r.get('use', '?'):<14} {r.get('tier', '?')}")
        return 0
    bad = integrity(lab, records)
    sick, notes = health(lab, records)
    bad += sick
    rows, total, newest = coverage(lab, records)
    disc = discovery(lab, records, accepted(lab)) if path == lab.register else []
    live = sum(1 for r in records if r.get("status") in ("live", "degraded"))
    external = sum(1 for n, *_ in rows if n is None) if False else sum(1 for _, n, _, _ in rows if n is None)
    age = (dt.datetime.now() - dt.datetime.fromtimestamp(newest)).days if newest else "?"
    show = [f for f in disc if "[show at open]" in f]
    summary = (f"sources: {len(records)} registered ({live} live, {external} outside the lab), {total} files covered, "
               f"newest change {age} day(s) ago; discovery: {len(show)} to review, {len(disc) - len(show)} recorded; "
               f"register findings: {len(bad)}")
    if "--summary" in flags:
        print(("ALERT " if bad else "") + summary + (" (python3 context/sources/check.py)" if bad or show else ""))
        return 1 if bad else 0
    print(("FAIL " if bad else "OK ") + summary)
    if "--report" in flags:
        for i, n, mt, readers in rows:
            when = dt.datetime.fromtimestamp(mt).strftime("%Y-%m-%d") if mt else "no files"
            count = "external" if n is None else f"{n:>5} files"
            print(f"  {i:<18} {count:>10}, newest {when:<10}  read by: {readers}")
    for f in bad + notes + disc:
        print("  " + f)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
