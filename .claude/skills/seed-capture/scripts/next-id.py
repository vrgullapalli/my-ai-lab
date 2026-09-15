#!/usr/bin/env python3
"""next-id: the next free live-session seed ID, and any ID used twice.

  python3 next-id.py            prints the next ID, e.g. A-LIVE-192
  python3 next-id.py --check    also lists any ID that appears on more than one seed

Read-only. seed-capture's rule is "next number in the existing sequence; never reuse or
renumber". Counting by eye is how two seeds end up sharing a number, so a script counts.
It reads both the file names and each seed's "- ID:" line, because the two can disagree.
"""
import os
import re
import sys

SESSION = os.path.join(os.environ["SEEDBANK"], "session") if os.environ.get("SEEDBANK") else "/Users/venkatgullapalli/Documents/my-ai-lab/work-os/brand-os/engagement-os/seedbank/session"
# SEEDBANK in the environment points the script at a test bank; the tests use it, nothing else does.
PREFIX = "A-LIVE-"


def main():
    seen = {}
    for name in sorted(os.listdir(SESSION)):
        if not name.endswith(".md"):
            continue
        ids = set(re.findall(r"A-LIVE-(\d+)", name[:14]))
        text = open(os.path.join(SESSION, name), encoding="utf-8", errors="replace").read()
        m = re.search(r"^- ID:\s*A-LIVE-(\d+)", text, re.M)
        if m:
            ids.add(m.group(1))
        for i in ids:
            seen.setdefault(int(i), []).append(name)
    if not seen:
        print(PREFIX + "001")
        return
    print(f"{PREFIX}{max(seen) + 1:03d}")
    if "--check" in sys.argv:
        dupes = {k: v for k, v in seen.items() if len(set(v)) > 1}
        gaps = sorted(set(range(1, max(seen) + 1)) - set(seen))
        print(f"highest in use: {PREFIX}{max(seen):03d}; seeds: {len(seen)}")
        print("IDs on more than one seed: " + (", ".join(f"{PREFIX}{k:03d}" for k in dupes) or "none"))
        print("numbers never used (gaps are fine; never fill them): " +
              (", ".join(str(g) for g in gaps[:20]) or "none"))


if __name__ == "__main__":
    main()
