#!/usr/bin/env python3
"""dead-pointers: finds every path the lab's live files mention that no longer exists.

READ-ONLY. Writes nothing. Prints a report.

Usage:  python3 .claude/skills/context-check/dead-pointers.py            live files only
        python3 .claude/skills/context-check/dead-pointers.py --all      also dated records

Why: on 2026-09-10 a grep for known-dead folder names missed most of the lab's broken
pointers, because it only looked for names someone already knew were dead. This works
the other way round. It collects every path-shaped thing a file mentions, tries to find
it, and reports the ones it cannot find. A script decides what exists, not memory.

A mention counts as found if the path exists under any of:
  1. itself, when it is absolute or starts with ~
  2. the lab root
  3. the file's own folder, any folder one level below it, and every folder above it
  4. the "Base directory:" a skill declares at its top, and one level below that
  5. ~/Documents (for _warehouse/ and os-factory/)
A bare file name with no folder counts as found if any file of that name exists in the
lab, because a bare name does not say where to look.

Skipped on purpose:
  - web addresses, domains (github.com/...), slash commands (/archie), command lines
    (anything with a space), placeholders (<slug>, {id}, YYYY, *), and paths on other
    machines (/home/, /tmp/)
  - folders that are history by design: evidence/, _archive/, records/, runs/,
    outputs/, snapshots/, inputs/, research/, sources/, stage1-extracts/, reports/,
    traces/, state/, logs/, receipts/, the seedbank, generated build/ folders, and
    the upstream packages installed as skills (unlazy, book-to-skill)
A dead path inside history is correct history. Changing it would falsify the record.

Files whose names carry a date (2026-09-08) are usually records too. They are scanned
but reported separately, so nobody fixes history by accident.
"""
import os
import re
import sys

LAB = "/Users/venkatgullapalli/Documents/my-ai-lab"
DOCS = os.path.expanduser("~/Documents")
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
DATED = re.compile(r"20\d\d-\d\d-\d\d")
BACKTICK = re.compile(r"`([^`\n]{2,200})`")
MDLINK = re.compile(r"\]\(([^)\s]{2,200})\)")
PLACEHOLDER = re.compile(r"[<>{}*$|\\]|YYYY|NNN|\.\.\.|…|XX")
DOMAIN = re.compile(r"^[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*\.(com|org|net|io|ai|co|dev|app|gov|edu|us|uk)(/|$)", re.I)
SLASH_COMMAND = re.compile(r"^/[A-Za-z0-9_:-]+$")
BASE = re.compile(r"Base directory:\**\s*(?:all relative paths in this skill resolve from\s*)?`([^`]+)`")


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


def candidates(tok, fpath, base):
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
    if base:
        b = os.path.join(LAB, base)
        yield os.path.join(b, t)
        for c in children(b):
            yield os.path.join(c, t)
    yield os.path.join(DOCS, t)


def found(tok, fpath, base, basenames):
    if "/" not in tok.rstrip("/"):
        if tok.rstrip("/") in basenames:
            return True
    return any(os.path.exists(c.rstrip("/")) for c in candidates(tok, fpath, base))


def scan():
    basenames = all_basenames()
    live, dated = [], []
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
            m = BASE.search(text[:2000])
            base = m.group(1).rstrip("/") if m else None
            is_dated = bool(DATED.search(name))
            seen = set()
            for lineno, line in enumerate(text.split("\n"), 1):
                for rx in (BACKTICK, MDLINK):
                    for mm in rx.finditer(line):
                        tok = clean(mm.group(1))
                        if not tok or tok in seen or not looks_like_path(tok):
                            continue
                        if found(tok, fpath, base, basenames):
                            continue
                        seen.add(tok)
                        rel = os.path.relpath(fpath, LAB)
                        (dated if is_dated else live).append((rel, lineno, tok))
    return live, dated


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
    live, dated = scan()
    report(live, f"Live files: {len(live)} mentions of paths that do not exist")
    if "--all" in sys.argv:
        report(dated, f"Dated files (usually history; review before changing): {len(dated)}")
    else:
        print(f"Dated files not shown: {len(dated)} dead mentions. Run with --all to list them.")
    print(f"\nLIVE DEAD POINTERS: {len(live)}")


if __name__ == "__main__":
    main()
