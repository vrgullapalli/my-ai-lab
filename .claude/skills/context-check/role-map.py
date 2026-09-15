#!/usr/bin/env python3
"""role-map: walks a root for ROLE.md marker files, builds the derived map, and reports drift.

READ-ONLY. Writes nothing unless --write names a file for the rendered map. Exits 1 when any
finding is present, 0 when none, 2 when the root does not exist or holds no marker.

Usage:  python3 .claude/skills/context-check/role-map.py <root> [<root> ...] [--verify-manifests] [--write MAP] [--max-depth N]
        More than one root walks each and pairs markers across them (a pilot on two sibling
        folders without walking the whole estate). --max-depth N stops the walk N folders
        below each root (0 is the root itself), so an estate root with a million files can be
        read for its top-level markers in one listing.

        python3 .claude/skills/context-check/role-map.py resolve <id> <root> [--max-depth N]
        Prints the live folder for a stable id and exits 0. Exits 1 when no live marker carries
        the id, 3 when more than one does (a duplicate canonical). This is the one path from an
        id to its current location; a consumer that writes the path into its own file is taking
        a copy that goes stale (Organization Standard section 3; AD-40, AD-42).

The standard it enforces: docs/architecture/ORGANIZATION-STANDARD.md (AD-40, 2026-09-15),
sections 3, 4, 6, and 11. A marker is a ROLE.md with `- key: value` lines. Six fields are
always required: id, role, area, scope, as-of, declared-by. A marker carrying `replaced-by`
(a different thing took over) or `relocated-to` plus `relocated-on` (the same id moved; the
live marker says `relocated-from`; AD-42) is superseded. An id may appear once live and any
number of times superseded. A location in a relocation field is a folder name at the time of
the move; it matches a marker when it equals that marker's folder name, its path relative to
the walked root, or its full path.

Findings, with the materiality words of AD-11:
  duplicate canonical      two live markers (no replaced-by) with role canonical or derived
                           share one id                                        interrupt
  unconfirmed canonical    a live canonical marker declared by alfred-proposed  interrupt
  invalid marker           a required field missing, or a word not in the lists show at open
  supersession drift       replaced-by names the marker's own id (fake replacement), an id with
                           no marker at all, a superseded one (more than one hop), or a chain
                           that loops                                            show at open
  relocation drift         relocated-to with no live marker for that id; a live relocated-from
                           with no old marker behind it; location names that do not match the
                           other end; a relocation loop; or a marker carrying both relocated-to
                           and replaced-by                                       show at open
  one-way supersession     a superseded marker whose live target carries no `replaces` naming
                           it, or a `replaces` with no superseded marker behind it   show at open
  write after supersession a file under a superseded marker changed after replaced-on or
                           relocated-on                                          show at open
  hand-edited build        a file under a derived marker changed after built    show at open
  manifest drift           with --verify-manifests: a MANIFEST.txt line whose file is missing
                           or whose sha256 differs, or a payload file not in the manifest  show at open
  expired temporary        role temporary past expires                          record only
"""
import hashlib
import os
import sys
from datetime import date

ROLES = {"canonical", "replica", "derived", "historical", "temporary"}
AREAS = {"work", "library", "personal", "machine-copies", "temporary", "warehouse"}
SCOPES = {"ai-lab", "professional", "career", "public", "personal"}
DECLARED = {"venkat", "alfred-proposed"}
REQUIRED = ("id", "role", "area", "scope", "as-of", "declared-by")
LIVE_ROLES = {"canonical", "derived"}
SKIP_DIRS = {".git", "node_modules", ".venv", "__pycache__", ".Trash"}
NOT_PAYLOAD = {"ROLE.md", "MANIFEST.txt", ".DS_Store"}


def parse(path):
    rec = {}
    with open(path, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            line = line.rstrip("\n")
            if line.startswith("- ") and ": " in line:
                k, v = line[2:].split(": ", 1)
                rec[k.strip()] = v.strip()
    return rec


def as_date(s):
    try:
        y, m, d = s[:10].split("-")
        return date(int(y), int(m), int(d))
    except Exception:
        return None


def file_date(p):
    return date.fromtimestamp(os.path.getmtime(p))


def payload(folder):
    out = []
    for name in sorted(os.listdir(folder)):
        if name in NOT_PAYLOAD or name.startswith("."):
            continue
        p = os.path.join(folder, name)
        if os.path.isfile(p):
            out.append(p)
    return out


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def walk(root, max_depth=None):
    markers = []
    root = root.rstrip(os.sep)
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        if max_depth is not None:
            depth = 0 if dirpath == root else dirpath[len(root):].count(os.sep)
            if depth >= max_depth:
                dirnames[:] = []
        if "ROLE.md" in filenames:
            p = os.path.join(dirpath, "ROLE.md")
            rec = parse(p)
            rec["_folder"] = dirpath
            rec["_path"] = p
            markers.append(rec)
    return markers


def check(markers, root, verify_manifests=False):
    findings = []  # (level, kind, detail)

    def add(level, kind, detail):
        findings.append((level, kind, detail))

    for m in markers:
        missing = [k for k in REQUIRED if k not in m]
        if missing:
            add("show at open", "invalid marker", f"{m['_path']}: missing {', '.join(missing)}")
        if m.get("role") and m["role"] not in ROLES:
            add("show at open", "invalid marker", f"{m['_path']}: role '{m['role']}' not allowed")
        if m.get("area") and m["area"] not in AREAS:
            add("show at open", "invalid marker", f"{m['_path']}: area '{m['area']}' not allowed")
        if m.get("scope") and m["scope"] not in SCOPES:
            add("show at open", "invalid marker", f"{m['_path']}: scope '{m['scope']}' not allowed")
        if m.get("declared-by") and m["declared-by"] not in DECLARED:
            add("show at open", "invalid marker", f"{m['_path']}: declared-by '{m['declared-by']}' not allowed")

    live = {}      # id -> [markers that are neither replaced nor moved]
    superseded = []   # replaced-by
    moved = []        # relocated-to
    for m in markers:
        if "replaced-by" in m and "relocated-to" in m:
            add("show at open", "relocation drift", f"{m['_path']}: carries both relocated-to and replaced-by")
            superseded.append(m)
        elif "replaced-by" in m:
            superseded.append(m)
        elif "relocated-to" in m:
            moved.append(m)
        else:
            live.setdefault(m.get("id", "?"), []).append(m)
    by_id_superseded = {}
    for m in superseded:
        by_id_superseded.setdefault(m.get("id"), []).append(m)

    for i, ms in live.items():
        heads = [m for m in ms if m.get("role") in LIVE_ROLES]
        if len(heads) > 1:
            add("interrupt", "duplicate canonical",
                f"id '{i}' is live in {len(heads)} places: " + "; ".join(m["_folder"] for m in heads))
        for m in heads:
            if m.get("role") == "canonical" and m.get("declared-by") == "alfred-proposed":
                add("interrupt", "unconfirmed canonical", f"{m['_path']}: canonical but only alfred-proposed")

    for m in superseded:
        target = m["replaced-by"]
        if target == m.get("id"):
            add("show at open", "supersession drift", f"{m['_path']}: replaced-by names its own id '{target}' (a relocation is relocated-to and relocated-from, not a replacement)")
            continue
        if target not in live:
            # walk the chain through superseded markers to name the failure
            seen = [m.get("id")]
            cur = target
            kind = "dead id"
            while True:
                if cur in seen:
                    kind = "loop " + " -> ".join(seen + [cur]); break
                seen.append(cur)
                nxt = by_id_superseded.get(cur)
                if not nxt:
                    kind = "dead id" if cur not in live else "one hop"; break
                cur = nxt[0]["replaced-by"]
                if cur in live:
                    kind = "chain longer than one hop; ends at live '" + cur + "'"; break
            add("show at open", "supersession drift", f"{m['_path']}: replaced-by '{target}' has no live marker ({kind})")
        else:
            tgt = live[target]
            if not any(h.get("replaces") == m.get("id") for h in tgt):
                add("show at open", "one-way supersession", f"{m['_path']}: target '{target}' carries no replaces naming '{m.get('id')}'")
        rd = as_date(m.get("replaced-on", ""))
        if rd:
            for p in payload(m["_folder"]):
                if file_date(p) > rd:
                    add("show at open", "write after supersession", f"{p} changed {file_date(p)} after replaced-on {rd}")

    def names(m):
        f = m["_folder"]
        return {os.path.basename(f), os.path.relpath(f, root), f}

    moved_by_id = {}
    for m in moved:
        moved_by_id.setdefault(m.get("id"), []).append(m)
    for m in moved:
        i = m.get("id")
        target = m["relocated-to"]
        if i not in live:
            chain = [m]
            cur = m
            looped = False
            while True:
                nxt = [o for o in moved_by_id.get(i, []) if cur["relocated-to"] in names(o)]
                if not nxt:
                    break
                if nxt[0] in chain:
                    looped = True; break
                chain.append(nxt[0]); cur = nxt[0]
            if looped:
                add("show at open", "relocation drift", f"{m['_path']}: relocation loop for id '{i}': " + " -> ".join(os.path.basename(c['_folder']) for c in chain) + " -> " + os.path.basename(chain[0]['_folder']))
            else:
                add("show at open", "relocation drift", f"{m['_path']}: relocated-to '{target}' but no live marker carries id '{i}'")
        else:
            heads = live[i]
            if not any(target in names(h) for h in heads):
                add("show at open", "relocation drift", f"{m['_path']}: relocated-to '{target}' does not name the live location of '{i}' (" + ", ".join(os.path.basename(h['_folder']) for h in heads) + ")")
            if not any(h.get("relocated-from") in names(m) for h in heads):
                add("show at open", "relocation drift", f"{m['_path']}: live marker for '{i}' carries no relocated-from naming '{os.path.basename(m['_folder'])}'")
        rd = as_date(m.get("relocated-on", ""))
        if rd:
            for p in payload(m["_folder"]):
                if file_date(p) > rd:
                    add("show at open", "write after supersession", f"{p} changed {file_date(p)} after relocated-on {rd}")
    for i, ms in live.items():
        for h in ms:
            if "relocated-from" in h and not any(h["relocated-from"] in names(o) for o in moved_by_id.get(i, [])):
                add("show at open", "relocation drift", f"{h['_path']}: relocated-from '{h['relocated-from']}' but no old marker with id '{i}' sits there")

    superseded_ids = {m.get("id") for m in superseded}
    for i, ms in live.items():
        for m in ms:
            if "replaces" in m and m["replaces"] not in superseded_ids:
                add("show at open", "one-way supersession", f"{m['_path']}: replaces '{m['replaces']}' but no superseded marker carries that id")
            if m.get("role") == "derived":
                bd = as_date(m.get("built", ""))
                if bd:
                    for p in payload(m["_folder"]):
                        if file_date(p) > bd:
                            add("show at open", "hand-edited build", f"{p} changed {file_date(p)} after built {bd}")
            if m.get("role") == "temporary":
                ed = as_date(m.get("expires", ""))
                if ed and ed < date.today():
                    add("record only", "expired temporary", f"{m['_folder']} expired {ed}")

    if verify_manifests:
        for m in markers:
            mf = os.path.join(m["_folder"], "MANIFEST.txt")
            if not os.path.exists(mf):
                continue
            listed = {}
            with open(mf) as fh:
                for line in fh:
                    parts = line.split()
                    if len(parts) >= 2:
                        listed[parts[-1]] = parts[0]
            present = {os.path.basename(p): p for p in payload(m["_folder"])}
            for name, want in listed.items():
                if name not in present:
                    add("show at open", "manifest drift", f"{mf}: '{name}' listed but missing")
                elif sha256(present[name]) != want:
                    add("show at open", "manifest drift", f"{mf}: '{name}' sha256 differs")
            for name in present:
                if name not in listed:
                    add("show at open", "manifest drift", f"{mf}: '{name}' present but not listed")
    return findings


def render(markers, root):
    lines = [f"ROLE MAP for {root}", ""]
    for m in sorted(markers, key=lambda m: (m.get("id", ""), "replaced-by" in m or "relocated-to" in m, m["_folder"])):
        state = ("replaced by " + m["replaced-by"]) if "replaced-by" in m else ("relocated to " + m["relocated-to"] + " on " + m.get("relocated-on", "?")) if "relocated-to" in m else ("live, relocated from " + m["relocated-from"]) if "relocated-from" in m else "live"
        rel = os.path.relpath(m["_folder"], root)
        lines.append(f"- {m.get('id','?')} | {m.get('role','?')} | {m.get('area','?')}/{m.get('scope','?')} | {state} | {rel} | as-of {m.get('as-of','?')} | {m.get('declared-by','?')}")
    return "\n".join(lines)


def resolve(ident, root, max_depth=None):
    """The live folder for a stable id under root. Returns (code, path or message)."""
    heads = [m for m in walk(root, max_depth)
             if m.get("id") == ident and "replaced-by" not in m and "relocated-to" not in m
             and m.get("role") in LIVE_ROLES]
    if not heads:
        return 1, f"no live marker carries id '{ident}' under {root}"
    if len(heads) > 1:
        return 3, f"id '{ident}' is live in {len(heads)} places: " + "; ".join(h["_folder"] for h in heads)
    return 0, heads[0]["_folder"]


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    max_depth = None
    if "--max-depth" in argv:
        i = argv.index("--max-depth")
        max_depth = int(argv[i + 1])
        argv = argv[:i] + argv[i + 2:]
    if argv[1] == "resolve":
        if len(argv) < 4:
            print("usage: role-map.py resolve <id> <root> [--max-depth N]")
            return 2
        code, msg = resolve(argv[2], os.path.expanduser(argv[3]), max_depth)
        print(msg)
        return code
    verify = "--verify-manifests" in argv
    out = None
    if "--write" in argv:
        out = argv[argv.index("--write") + 1]
    roots = [os.path.expanduser(a) for a in argv[1:] if not a.startswith("--") and a != out]
    for r in roots:
        if not os.path.isdir(r):
            print(f"ALERT role-map: root does not exist: {r}")
            return 2
    markers = []
    for r in roots:
        markers += walk(r, max_depth)
    root = os.path.commonpath(roots) if len(roots) > 1 else roots[0]
    if not markers:
        print(f"ALERT role-map: no ROLE.md under {', '.join(roots)}")
        return 2
    text = render(markers, root)
    print(text)
    findings = check(markers, root, verify)
    print()
    order = {"interrupt": 0, "show at open": 1, "record only": 2}
    for level, kind, detail in sorted(findings, key=lambda f: order[f[0]]):
        print(f"FINDING [{level}] {kind}: {detail}")
    counts = {k: sum(1 for f in findings if f[0] == k) for k in order}
    print(f"ROLE MAP: {len(markers)} markers, {len({m.get('id') for m in markers})} ids; findings {len(findings)} "
          f"(interrupt {counts['interrupt']}, show at open {counts['show at open']}, record only {counts['record only']})")
    if out:
        with open(out, "w") as fh:
            fh.write(text + "\n\n" + "\n".join(f"FINDING [{l}] {k}: {d}" for l, k, d in findings) + "\n")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
