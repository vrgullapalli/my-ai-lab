#!/usr/bin/env python3
"""Tests for dead-pointers.py, in the prove-it-can-fail form: a planted lab with known dead and
live mentions must sort each one into the right count, and an accepted mention must never be
reported as open or as resolved.

Run:  python3 .claude/skills/context-check/tests/dead_pointers_tests.py

Builds a throwaway lab in a temp folder and points the script at it through LAB_ROOT, LAB_DOCS,
and DEAD_POINTERS_ACCEPTED, so it never reads or writes the real lab. Cases, from the Operational
DNA repair of 2026-09-15 (AD-38):

  1. open        a live file naming a path that does not exist is listed and counted OPEN
  2. found       a live file naming a path that exists is not listed
  3. dated       a dated file's dead mention is counted as dated, never as OPEN
  4. accepted    an accepted mention leaves OPEN and lands in ACCEPTED, tagged with its record;
                 item, bulk, and no-record groups are counted apart
  5. not resolved   the ACCEPTED line says "not resolved" and the OPEN count excludes accepted
  6. resolved    when the missing path appears, a rerun drops the mention: resolution is by rerun
  7. read-only   the planted lab is byte-for-byte unchanged after every run
  8. wrong root  an empty folder, or one with files but no CLAUDE.md, exits 2 with an ALERT
                 line and never prints LIVE DEAD POINTERS: 0 (second pass, 2026-09-15)

Prints DEAD POINTERS TESTS PASSED only when every case passes.
"""
import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(os.path.dirname(HERE), "dead-pointers.py")
failures = 0


def check(name, ok, detail=""):
    global failures
    failures += 0 if ok else 1
    print(f"  {'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail[:400]})" if detail and not ok else ""))


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def run(lab, accepted, *args):
    env = dict(os.environ, LAB_ROOT=lab, LAB_DOCS=os.path.join(lab, "no-docs"), DEAD_POINTERS_ACCEPTED=accepted)
    r = subprocess.run([sys.executable, SCRIPT, *args], capture_output=True, text=True, env=env, timeout=60)
    return r.returncode, r.stdout + r.stderr


def digest(folder):
    h = hashlib.sha256()
    for root, dirs, files in os.walk(folder):
        dirs.sort()
        for name in sorted(files):
            p = os.path.join(root, name)
            h.update(os.path.relpath(p, folder).encode())
            h.update(open(p, "rb").read())
    return h.hexdigest()


def count(out, label):
    m = re.search(r"^" + label + r": (\d+)", out, re.M)
    return int(m.group(1)) if m else None


def main():
    tmp = tempfile.mkdtemp(prefix="dead-pointers-test-")
    try:
        lab = os.path.join(tmp, "lab")
        write(os.path.join(lab, "CLAUDE.md"), "# planted lab front door\n")
        os.makedirs(os.path.join(lab, ".claude"))
        write(os.path.join(lab, "live", "a.md"), "See `gone/x.md` for the plan.\n")
        write(os.path.join(lab, "live", "b.md"), "See `real/y.md` for the record.\n")
        write(os.path.join(lab, "real", "y.md"), "# y\n")
        write(os.path.join(lab, "notes", "2026-09-01-old.md"), "Once at `gone/z.md`.\n")
        write(os.path.join(lab, "live", "c.md"), "Moved: `warehouse-copy/old.md`.\n")
        write(os.path.join(lab, "old-plans", "p.md"), "Was `gone/q.md` and `gone/r.md`.\n")
        write(os.path.join(lab, "live", "d.md"), "Legacy `gone/legacy.md`.\n")
        accepted = os.path.join(tmp, "accepted.txt")
        write(accepted, "\n".join([
            "# header comment",
            "live/d.md :: gone/legacy.md | reviewed before any marker existed",
            "# accepted-by: Venkat | item | 2026-09-15 | his word on this line",
            "live/c.md :: warehouse-copy/old.md | a warehouse folder, outside the lab on purpose",
            "# accepted-by: Alfred | bulk | 2026-09-14 | a sweep under a follow-up; not item review",
            "old-plans/ | dated plans folder",
            "",
        ]))

        print("1 to 5. planted lab: open, found, dated, accepted, not resolved")
        before = digest(lab)
        code, out = run(lab, accepted)
        check("open mention listed under OPEN", "live/a.md" in out and "gone/x.md" in out, out)
        check("OPEN count is exactly 1", count(out, "OPEN") == 1, out)
        check("LIVE DEAD POINTERS line agrees with OPEN", "LIVE DEAD POINTERS: 1" in out, out)
        check("a path that exists is not listed", "real/y.md" not in out, out)
        check("dated file's dead mention is not OPEN", "gone/z.md" not in out and "Dated files: 1" in out, out)
        check("accepted mentions are not OPEN", "warehouse-copy/old.md" not in out and "gone/q.md" not in out, out)
        check("ACCEPTED count is 4 (1 item, 2 bulk, 1 no record)",
              count(out, "ACCEPTED") == 4 and "item by item: 1" in out and "bulk by Alfred, unconfirmed: 2" in out
              and "no acceptance record: 1" in out, out)
        check("ACCEPTED line says not resolved", re.search(r"^ACCEPTED:.*not resolved", out, re.M) is not None, out)
        check("RESOLVED line says it is proven by a rerun, not counted", re.search(r"^RESOLVED: not counted", out, re.M) is not None, out)

        code, out_all = run(lab, accepted, "--all")
        check("--all lists each accepted mention with its record",
              "[accepted: Venkat | item" in out_all and "[accepted: Alfred | bulk" in out_all
              and "[accepted: no acceptance record]" in out_all, out_all)

        print("6. resolved by rerun")
        write(os.path.join(lab, "gone", "x.md"), "# back\n")
        code, out2 = run(lab, accepted)
        check("after the path exists again, OPEN drops to 0 on rerun", count(out2, "OPEN") == 0 and "gone/x.md" not in out2, out2)
        check("accepted count did not change when an open one resolved", count(out2, "ACCEPTED") == 4, out2)
        os.remove(os.path.join(lab, "gone", "x.md"))
        os.rmdir(os.path.join(lab, "gone"))

        print("7. read-only")
        after = digest(lab)
        check("planted lab unchanged after three runs", before == after)

        print("control: an empty accepted file makes every accepted mention OPEN again")
        empty = os.path.join(tmp, "empty.txt")
        write(empty, "# nothing accepted\n")
        code, out3 = run(lab, empty)
        # five: a.md, c.md, d.md, and the two lines in old-plans/p.md; the dated file stays dated
        check("without acceptances OPEN is 5 and ACCEPTED is 0", count(out3, "OPEN") == 5 and count(out3, "ACCEPTED") == 0, out3)

        print("8. wrong root")
        empty = os.path.join(tmp, "empty")
        os.makedirs(empty)
        code, out4 = run(empty, accepted)
        check("empty folder: exits 2 with an ALERT naming the folder",
              code == 2 and out4.startswith("ALERT dead pointers: NOT A LAB ROOT") and empty in out4, out4)
        check("empty folder: no clean-lab line", "LIVE DEAD POINTERS" not in out4 and "OPEN:" not in out4, out4)
        notlab = os.path.join(tmp, "notlab")
        write(os.path.join(notlab, "live", "a.md"), "See `gone/x.md`.\n")
        code, out5 = run(notlab, accepted)
        check("files but no CLAUDE.md: exits 2 with the ALERT, nothing counted",
              code == 2 and "NOT A LAB ROOT" in out5 and "OPEN:" not in out5, out5)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print()
    if failures:
        print(f"DEAD POINTERS TESTS FAILED: {failures}")
        return 1
    print("DEAD POINTERS TESTS PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
