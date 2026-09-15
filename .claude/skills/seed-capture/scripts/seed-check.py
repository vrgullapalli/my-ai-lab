#!/usr/bin/env python3
"""seed-check: proves a written seed follows the template, and that a write stayed inside the
skill's one permitted destination.

  python3 seed-check.py --seed <file> [<file> ...]       each seed: title, matching unique ID,
                                                          source, dated moment, status, one of the
                                                          four attribution classes, both sections,
                                                          no placeholder left. Exit 1 names each
                                                          failing field.
  python3 seed-check.py --boundary <path> [<path> ...]   every path must sit under
                                                          seedbank/session/. Exit 1 names any that
                                                          does not.

READ-ONLY. Writes nothing. Built 2026-09-15 (AD-38): the Operational DNA audit found the skill's
declared writes did not match its real ones, and nothing proved a seed was well formed before it
was reported. SEEDBANK in the environment points at a test bank; the tests use it, nothing else does.
"""
import os
import re
import sys

SEEDBANK = os.environ.get("SEEDBANK") or "/Users/venkatgullapalli/Documents/my-ai-lab/work-os/brand-os/engagement-os/seedbank"
SESSION = os.path.join(SEEDBANK, "session")
CLASSES = ("his", "endorsed", "other", "system")
ID_LINE = re.compile(r"^- ID:\s*([A-Z]+-[A-Z]+-\d{3,})\s*$", re.M)
DATE_LINE = re.compile(r"^- Date:\s*(\d{4}-\d{2}-\d{2})\b", re.M)
ATTR_LINE = re.compile(r"^- Attribution:\s*\**([a-z]+)\**", re.M)
FIELD = lambda name: re.compile(r"^- " + name + r":\s*(\S.*)$", re.M)
PLACEHOLDER = re.compile(r"<[A-Za-z][^>\n]{0,80}>")


def ids_in_bank():
    """Every ID in use in session/, from file names and ID lines, with the files that carry it."""
    seen = {}
    if not os.path.isdir(SESSION):
        return seen
    for name in sorted(os.listdir(SESSION)):
        if not name.endswith(".md"):
            continue
        m = re.match(r"([A-Z]+-[A-Z]+-\d{3,})", name)
        ids = {m.group(1)} if m else set()
        try:
            text = open(os.path.join(SESSION, name), encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        m = ID_LINE.search(text)
        if m:
            ids.add(m.group(1))
        for i in ids:
            seen.setdefault(i, set()).add(name)
    return seen


def check_seed(path, bank_ids):
    problems = []
    try:
        text = open(path, encoding="utf-8", errors="replace").read()
    except OSError as e:
        return [f"cannot read ({e})"]
    first = text.lstrip().split("\n", 1)[0]
    if not first.startswith("# ") or len(first) < 12:
        problems.append("title: first line must be the claim as a sentence, after '# '")
    m = ID_LINE.search(text)
    if not m:
        problems.append("ID: missing or not of the form PREFIX-KIND-NNN")
    else:
        sid = m.group(1)
        if not os.path.basename(path).startswith(sid):
            problems.append(f"ID: {sid} does not match the file name")
        carriers = bank_ids.get(sid, set()) | {os.path.basename(path)}
        if len(carriers) > 1:
            problems.append(f"ID: {sid} used twice ({', '.join(sorted(carriers))})")
    src = FIELD("Source").search(text)
    if not src or PLACEHOLDER.search(src.group(1)):
        problems.append("Source: missing or still a placeholder")
    if not DATE_LINE.search(text):
        problems.append("Date: missing or not YYYY-MM-DD")
    if not FIELD("Status").search(text):
        problems.append("Status: missing")
    a = ATTR_LINE.search(text)
    if not a or a.group(1) not in CLASSES:
        problems.append("Attribution: missing or not one of his, endorsed, other, system")
    for section in ("## The claim", "## Why it matters"):
        if section not in text:
            problems.append(f"section missing: {section}")
    body = text.split("\n", 1)[1] if "\n" in text else ""
    left = [p for p in PLACEHOLDER.findall(body) if not p.startswith("<id>")]
    if left:
        problems.append(f"placeholder left in body: {left[0]}")
    return problems


def check_boundary(paths):
    root = os.path.realpath(SESSION) + os.sep
    outside = []
    for p in paths:
        real = os.path.realpath(os.path.abspath(os.path.expanduser(p)))
        if not real.startswith(root) or not real.endswith(".md"):
            outside.append(p)
    return outside


def main():
    args = sys.argv[1:]
    if len(args) < 2 or args[0] not in ("--seed", "--boundary"):
        print(__doc__)
        return 2
    mode, paths = args[0], args[1:]
    if mode == "--boundary":
        outside = check_boundary(paths)
        for p in outside:
            print(f"WRITE BOUNDARY BROKEN: {p}  (not a .md file under seedbank/session/)")
        if outside:
            return 1
        print(f"WRITE BOUNDARY OK: {len(paths)} file(s), all under seedbank/session/")
        return 0
    bank_ids = ids_in_bank()
    failed = 0
    for p in paths:
        problems = check_seed(p, bank_ids)
        if problems:
            failed += 1
            print(f"SEED FAIL {p}")
            for line in problems:
                print(f"    {line}")
        else:
            print(f"SEED OK {os.path.basename(p)}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
