#!/usr/bin/env python3
"""dead-pointers: finds every path the lab's live files mention that no longer exists.

READ-ONLY. Writes nothing. Prints a report.

Usage:  python3 .claude/skills/context-check/dead-pointers.py            unreviewed, live files
        python3 .claude/skills/context-check/dead-pointers.py --all      also dated records and
                                                                          reviewed mentions

Why: on 2026-09-10 a grep for known-dead folder names missed most of the lab's broken
pointers, because it only looked for names someone already knew were dead. This works the
other way round. It collects every path-shaped thing a file mentions, tries to find it, and
reports the ones it cannot find. A script decides what exists, not memory.

A mention counts as found if the path exists under any of:
  1. itself, when it is absolute or starts with ~
  2. the lab root
  3. the file's own folder, any folder one level below it, and every folder above it
  4. the home folders a skill or agent declares on its "Base directory:" line, and one
     level below each. A file with no such line inherits the line from the nearest
     CLAUDE.md or SKILL.md above it, so an agent's rule files share the agent's home.
  5. ~/Documents (for _warehouse/ and os-factory/)
A bare file name with no folder counts as found if any file of that name exists in the lab.

Skipped on purpose: web addresses and domains, slash commands (/archie), web page paths
(/about/careers), command lines, placeholders (<slug>, {id}, YYYY, gate-N), paths on other
machines, and folders that are history by design (evidence/, _archive/, records/, runs/,
outputs/, snapshots/, inputs/, research/, sources/, stage1-extracts/, reports/, traces/,
state/, logs/, receipts/, build/, the seedbank, and the upstream packages installed as skills).

Reviewed mentions: dead-pointers-accepted.txt, beside this script, lists mentions a person
has looked at and judged to be history, a plan for something not built yet, or a pointer
to another machine, each with its reason. Those are counted, not listed. Anything new
shows up. The goal is "LIVE DEAD POINTERS: 0" with every exception written down.
"""
import os
import re
import sys

LAB = "/Users/venkatgullapalli/Documents/my-ai-lab"
DOCS = os.path.expanduser("~/Documents")
HERE = os.path.dirname(os.path.abspath(__file__))
ACCEPTED_FILE = os.path.join(HERE, "dead-pointers-accepted.txt")
EXTS = (".md", ".sh", ".py", ".json", ".yaml", ".yml", ".mjs", ".txt", ".jsonl",
        ".html", ".csv", ".tsv", ".toml", ".docx", ".pdf", ".tar.gz")
SCAN_EXTS = (".md", ".sh", ".py", ".json", ".yaml", ".yml", ".mjs")
SKIP_DIRS = {".git", "node_modules", ".remember", "evidence", "_archive", "runs",
             "outputs", "snapshots", "inputs", "seedbank", "research", "__pycache__",
             ".venv", ".unlazy", "tests", "fixtures", "records", "stage1-extracts",
             "sources", "traces", "reports", "state", "logs", "receipts", "build"}
SKIP_TREES = tuple(os.path.join(LAB, ".claude", "skills", s) + os.sep
                   for s in ("unlazy", "book-to-skill"))
FOREIGN = ("/home/", "/tmp/", "/private/tmp/", "/var/", "/opt/", "/mnt/", "C:")
REAL_ROOTS = {"Users", "Library", "System", "private", "usr", "bin", "opt", "etc", "var",
              "tmp", "Applications", "Volumes", "sbin"}
DATED = re.compile(r"20\d\d-\d\d-\d\d")
BACKTICK = re.compile(r"`([^`\n]{2,200})`")
MDLINK = re.compile(r"\]\(([^)\s]{2,200})\)")
PLACEHOLDER = re.compile(r"[<>{}*$|\\]|YYYY|NNN|\.\.\.|…|XX|-N\.")
DOMAIN = re.compile(r"^[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*\.(com|org|net|io|ai|co|dev|app|gov|edu|us|uk)(/|$)", re.I)
SLASH_COMMAND = re.compile(r"^/[A-Za-z0-9_:-]+$")
BASE_LINE = re.compile(r"^.*Base directory:.*$", re.M)
TICKED = re.compile(r"`([^`]+)`")

_base_cache = {}


def declared_bases(text):
    m = BASE_LINE.search(text[:3000])
    if not m:
        return None
    bases = []
    for tok in TICKED.findall(m.group(0)):
        t = tok.strip().rstrip("/")
        if t.startswith("/"):
            t = os.path.relpath(t, LAB) if t.startswith(LAB) else t
        bases.append(t)
    return bases or None


def inherited_bases(dirpath):
    """The Base directory line of the nearest CLAUDE.md or SKILL.md at or above dirpath."""
    d = dirpath
    while d.startswith(LAB):
        if d in _base_cache:
            return _base_cache[d]
        for name in ("CLAUDE.md", "SKILL.md"):
            p = os.path.join(d, name)
            if os.path.isfile(p):
                try:
                    b = declared_bases(open(p, encoding="utf-8", errors="replace").read())
                except OSError:
                    b = None
                if b:
                    _base_cache[d] = b
                    return b
        if d == LAB:
            break
        d = os.path.dirname(d)
    return []


def load_accepted():
    whole, exact = [], set()
    if not os.path.isfile(ACCEPTED_FILE):
        return whole, exact
    for line in open(ACCEPTED_FILE, encoding="utf-8"):
        line = line.split("|")[0].strip()
        if not line or line.startswith("#"):
            continue
        if " :: " in line:
            f, tok = line.split(" :: ", 1)
            exact.add((f.strip(), tok.strip()))
        else:
            whole.append(line)
    return whole, exact


def is_accepted(rel, tok, whole, exact):
    if (rel, tok) in exact:
        return True
    return any(rel == w or (w.endswith("/") and rel.startswith(w)) for w in whole)


def all_basenames():
    names = set()
    for root, dirs, files in os.walk(LAB):
        dirs[:] = [d for d in dirs if d not in {".git", "node_modules"}]
        names.update(files)
        names.update(dirs)
    return names


def looks_like_path(tok):
    if " " in tok or tok.startswith(("http://", "https://", "mailto:", "-", "#", "@")):
        return False
    if PLACEHOLDER.search(tok) or "=" in tok or tok.count(":") > 1:
        return False
    if SLASH_COMMAND.match(tok) or DOMAIN.match(tok) or tok.startswith(FOREIGN):
        return False
    if tok.startswith("/") and tok.strip("/").split("/")[0] not in REAL_ROOTS:
        return False  # a web page path such as /about/careers
    if "/" in tok:
        return True
    return tok.lower().endswith(EXTS)


def clean(tok):
    tok = tok.strip().strip("\"'")
    tok = re.sub(r"(#L?\d+.*|:\d+(-\d+)?)$", "", tok)
    tok = tok.split(" → ")[0].rstrip(".,;:)")
    return tok


def children(d):
    try:
        return [os.path.join(d, c) for c in os.listdir(d) if os.path.isdir(os.path.join(d, c))]
    except OSError:
        return []


def candidates(tok, fpath, bases):
    t = os.path.expanduser(tok)
    if os.path.isabs(t):
        yield t
        return
    yield os.path.join(LAB, t)
    here = os.path.dirname(fpath)
    for c in children(here):
        yield os.path.join(c, t)
    d = here
    while d.startswith(LAB):
        yield os.path.join(d, t)
        if d == LAB:
            break
        d = os.path.dirname(d)
    for base in bases:
        b = os.path.expanduser(base) if base.startswith("~") else os.path.join(LAB, base)
        yield os.path.join(b, t)
        for c in children(b):
            yield os.path.join(c, t)
    yield os.path.join(DOCS, t)


def found(tok, fpath, bases, basenames):
    if "/" not in tok.rstrip("/") and tok.rstrip("/") in basenames:
        return True
    return any(os.path.exists(c.rstrip("/")) for c in candidates(tok, fpath, bases))


def scan():
    basenames = all_basenames()
    whole, exact = load_accepted()
    live, dated, accepted = [], [], []
    for root, dirs, files in os.walk(LAB):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
        if any((root + os.sep).startswith(t) for t in SKIP_TREES):
            dirs[:] = []
            continue
        for name in sorted(files):
            if not name.endswith(SCAN_EXTS):
                continue
            fpath = os.path.join(root, name)
            try:
                if os.path.getsize(fpath) > 1_000_000:
                    continue
                text = open(fpath, encoding="utf-8", errors="replace").read()
            except OSError:
                continue
            bases = declared_bases(text) or inherited_bases(root)
            rel = os.path.relpath(fpath, LAB)
            is_dated = bool(DATED.search(name))
            seen = set()
            for lineno, line in enumerate(text.split("\n"), 1):
                for rx in (BACKTICK, MDLINK):
                    for mm in rx.finditer(line):
                        tok = clean(mm.group(1))
                        if not tok or tok in seen or not looks_like_path(tok):
                            continue
                        if found(tok, fpath, bases, basenames):
                            continue
                        seen.add(tok)
                        row = (rel, lineno, tok)
                        if is_accepted(rel, tok, whole, exact):
                            accepted.append(row)
                        elif is_dated:
                            dated.append(row)
                        else:
                            live.append(row)
    return live, dated, accepted


def report(rows, title):
    print(title)
    print("=" * len(title))
    last = None
    for rel, lineno, tok in rows:
        if rel != last:
            print("\n  " + rel)
            last = rel
        print(f"      line {lineno:<5} {tok}")
    print()


def main():
    live, dated, accepted = scan()
    report(live, f"Live files: {len(live)} unreviewed mentions of paths that do not exist")
    if "--all" in sys.argv:
        report(dated, f"Dated files (usually history; review before changing): {len(dated)}")
        report(accepted, f"Reviewed and accepted, with reasons in dead-pointers-accepted.txt: {len(accepted)}")
    else:
        print(f"Dated files: {len(dated)} dead mentions, not listed (usually history). "
              f"Reviewed and accepted: {len(accepted)}. Run with --all to list both.")
    print(f"\nLIVE DEAD POINTERS: {len(live)}")


if __name__ == "__main__":
    main()
