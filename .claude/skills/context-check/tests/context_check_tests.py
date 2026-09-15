#!/usr/bin/env python3
"""Tests for context-check.sh, in the prove-it-can-fail form: a planted lab with one of each
fault must be reported in the right section with the right label, a clean lab must report none,
and the planted lab must be byte-for-byte unchanged afterwards.

Run:  python3 .claude/skills/context-check/tests/context_check_tests.py

Builds a throwaway lab in a temp folder and points the script at it through LAB_ROOT and
LAB_SNAPSHOTS, with a copy of dead-pointers.py inside it so section F runs. Cases, from the
Operational DNA repair of 2026-09-15 (AD-38):

  legend       the measured / word-match legend is printed, and C and E carry [word match]
  B            two identical files in two live places are listed together
  C            a file declaring itself superseded is listed
  D            docs/ and context/ areas are measured; an unlisted docs/ area is named
  E            a file nothing names is counted as an orphan
  F            the old four-name grep is gone; dead-pointers.py's OPEN and ACCEPTED lines appear
  clean lab    C says none found, E says 0 orphans, F says OPEN: 0 (control for the absences)
  read-only    the planted lab is unchanged after the run
  wrong root   an empty folder, or one with files but no CLAUDE.md, exits 2 with NOT A LAB ROOT
               and never prints a clean-lab line (second pass, 2026-09-15)
  crash        a helper that dies with a traceback is an ALERT in its section with the error,
               the section carries no result line, the closing line counts it, exit 1
  missing      a helper that is not there is an ALERT, exit 1
  findings     a helper that exits nonzero with findings and no traceback is printed, named,
               and is not an ALERT (the control for the crash case)

Prints CONTEXT CHECK TESTS PASSED only when every case passes.
"""
import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.dirname(HERE)
SCRIPT = os.path.join(SKILL, "context-check.sh")
DEAD = os.path.join(SKILL, "dead-pointers.py")
failures = 0


def check(name, ok, detail=""):
    global failures
    failures += 0 if ok else 1
    print(f"  {'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail[:400]})" if detail and not ok else ""))


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def run(lab):
    env = dict(os.environ, LAB_ROOT=lab, LAB_SNAPSHOTS=os.path.join(lab, "no-snapshots"),
               LAB_DOCS=os.path.join(lab, "no-docs"), TMPDIR=os.environ.get("TMPDIR", "/tmp"))
    r = subprocess.run(["/bin/bash", SCRIPT], capture_output=True, text=True, env=env, timeout=120, cwd=lab)
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


def section(out, letter):
    m = re.search(r"^" + letter + r"\. .*?(?=^\w\. |\Z)", out, re.M | re.S)
    return m.group(0) if m else ""


STUB_OK = "print('OK planted check: 0 finding(s)')\n"


def plant(lab):
    """A root that passes the lab-root guard, with the real dead-pointers.py and two stub
    section-G helpers that report clean and exit 0."""
    write(os.path.join(lab, "CLAUDE.md"), "# planted lab front door\n")
    os.makedirs(os.path.join(lab, ".claude", "skills", "context-check"), exist_ok=True)
    shutil.copy(DEAD, os.path.join(lab, ".claude", "skills", "context-check", "dead-pointers.py"))
    write(os.path.join(lab, ".claude", "skills", "context-check", "dead-pointers-accepted.txt"),
          "# accepted-by: Alfred | bulk | 2026-09-14 | a sweep\nwork-os/brand-os/voice/old.md :: gone/v.md | reviewed\n")
    write(os.path.join(lab, "docs", "architecture", "check.py"), STUB_OK)
    write(os.path.join(lab, "context", "sources", "check.py"), STUB_OK)


def main():
    tmp = tempfile.mkdtemp(prefix="context-check-test-")
    try:
        lab = os.path.join(tmp, "lab")
        os.makedirs(os.path.join(lab, ".claude", "skills", "context-check"))
        plant(lab)
        write(os.path.join(lab, "docs", "architecture", "x.md"), "---\nname: x\n---\n# x\nSee [y](../about-me/y.md).\n")
        write(os.path.join(lab, "docs", "about-me", "y.md"), "# y\nNo front matter, no link. Named by x.md.\n")
        write(os.path.join(lab, "docs", "surprise", "s.md"), "# an area the list does not know\n")
        write(os.path.join(lab, "context", "state", "lonely.md"), "# nobody names this file\n")
        write(os.path.join(lab, "context", "README.md"), "# loose at the root of context/, counted as its own row\n")
        write(os.path.join(lab, "work-os", "brand-os", "voice", "one.md"), "# same\nidentical text\n")
        write(os.path.join(lab, "work-os", "brand-os", "messaging", "one-copy.md"), "# same\nidentical text\n")
        write(os.path.join(lab, "work-os", "brand-os", "voice", "old.md"), "> Superseded by one.md. See `gone/v.md`.\n")
        write(os.path.join(lab, "work-os", "brand-os", "voice", "live.md"), "Plan at `gone/w.md`; also x.md, one.md, one-copy.md, old.md, live.md.\n")

        before = digest(lab)
        code, out = run(lab)
        check("script exits 0", code == 0, out[-400:])

        print("legend and labels")
        check("legend printed", "[measured]" in out and "[word match]" in out and "How to read a section header" in out, out[:600])
        check("C and E are word match; A, B, D, F, G are measured",
              "C. [word match]" in out and "E. [word match]" in out and "B. [measured]" in out
              and "D. [measured]" in out and "F. [measured]" in out and "G. [measured]" in out, out)

        print("B. duplicates")
        b = section(out, "B")
        check("both identical files listed", "voice/one.md" in b and "messaging/one-copy.md" in b, b)

        print("C. superseded")
        c = section(out, "C")
        check("the superseded file is listed, the live one is not", "voice/old.md" in c and "voice/live.md" not in c, c)

        print("D. linkability")
        d = section(out, "D")
        check("docs/architecture row: 1 file, 1 front matter, 1 followable", re.search(r"docs/architecture\s+1\s+1\s+1", d) is not None, d)
        check("docs/about-me row: 1 file, 0 front matter, 0 followable", re.search(r"docs/about-me\s+1\s+0\s+0", d) is not None, d)
        check("context/state row present", re.search(r"context/state\s+1", d) is not None, d)
        check("an unlisted docs/ area is named", "docs/surprise" in d, d)
        check("exclusions are stated", "excluded on purpose" in d, d)
        check("files loose at the root of context/ get their own row", re.search(r"context/ \(files at its root\)\s+1\s", d) is not None, d)

        print("E. orphans")
        e = section(out, "E")
        check("lonely.md counted as an orphan", "context/state/lonely.md" in e and re.search(r"TOTAL ORPHANS: [1-9]", e) is not None, e)
        check("y.md, named by x.md, is not an orphan", "about-me/y.md" not in e, e)

        print("F. dead pointers")
        f = section(out, "F")
        check("old four-name grep is gone from the output", "my-ai-lab-v2/" not in out and "files mention it" not in out, out)
        check("dead-pointers OPEN line shows the one unaccepted dead path", re.search(r"OPEN: 1\b", f) is not None, f)
        check("dead-pointers ACCEPTED line shows the bulk one, not resolved", "ACCEPTED: 1" in f and "bulk by Alfred, unconfirmed: 1" in f and "not resolved" in f, f)

        print("G. helpers ran")
        g = section(out, "G")
        check("both stub helpers ran and printed", g.count("OK planted check") == 2, g)
        check("no ALERT anywhere on a lab whose helpers all run", "ALERT:" not in out, out)

        print("read-only")
        check("planted lab unchanged after the run", before == digest(lab))
        check("closing line says nothing was changed", "nothing was changed" in out, out[-200:])

        print("control: clean lab")
        clean = os.path.join(tmp, "clean")
        os.makedirs(os.path.join(clean, ".claude", "skills", "context-check"))
        plant(clean)
        write(os.path.join(clean, "docs", "architecture", "README.md"), "---\nname: r\n---\n# r\n")
        code, out2 = run(clean)
        check("clean lab: C none found", "none found" in section(out2, "C"), section(out2, "C"))
        check("clean lab: 0 orphans", "TOTAL ORPHANS: 0" in section(out2, "E"), section(out2, "E"))
        check("clean lab: OPEN: 0 in F", re.search(r"OPEN: 0\b", section(out2, "F")) is not None, section(out2, "F"))
        check("clean lab: no unlisted docs area", "\n  none" in section(out2, "D"), section(out2, "D"))

        print("wrong root: an empty folder")
        empty = os.path.join(tmp, "empty")
        os.makedirs(empty)
        code, out3 = run(empty)
        check("exits 2", code == 2, out3)
        check("says NOT A LAB ROOT and names the folder", "NOT A LAB ROOT" in out3 and empty in out3, out3)
        check("prints no clean-lab line", "TOTAL ORPHANS" not in out3 and "none found" not in out3 and "OPEN:" not in out3
              and "nothing was changed" not in out3, out3)

        print("wrong root: files but no CLAUDE.md")
        notlab = os.path.join(tmp, "notlab")
        os.makedirs(os.path.join(notlab, ".claude", "skills", "context-check"))
        write(os.path.join(notlab, "docs", "a.md"), "# a\n")
        code, out4 = run(notlab)
        check("exits 2 and says NOT A LAB ROOT", code == 2 and "NOT A LAB ROOT" in out4 and "TOTAL ORPHANS" not in out4, out4)

        print("crash: a helper that dies with a traceback")
        crash = os.path.join(tmp, "crash")
        os.makedirs(os.path.join(crash, ".claude", "skills", "context-check"))
        plant(crash)
        write(os.path.join(crash, ".claude", "skills", "context-check", "dead-pointers.py"),
              "import sys\nprint('partial output before the crash')\nraise RuntimeError('planted crash')\n")
        write(os.path.join(crash, "docs", "architecture", "README.md"), "---\nname: r\n---\n# r\n")
        code, out5 = run(crash)
        f5 = section(out5, "F")
        check("run exits 1", code == 1, out5[-300:])
        check("section F carries an ALERT naming the helper and the exit code", "ALERT: dead-pointers.py crashed (exit 1)" in f5, f5)
        check("the error text is shown in the section", "RuntimeError: planted crash" in f5, f5)
        check("section F has no OPEN or LIVE DEAD POINTERS line", "OPEN:" not in f5 and "LIVE DEAD POINTERS" not in f5, f5)
        check("closing line counts the alert", "Done with 1 ALERT(s)" in out5 and "Nothing was changed" in out5, out5[-300:])

        print("missing: a helper that is not there")
        os.remove(os.path.join(crash, "context", "sources", "check.py"))
        code, out6 = run(crash)
        g6 = section(out6, "G")
        check("section G carries an ALERT naming the missing helper", "ALERT: context/sources/check.py not present" in g6, g6)
        check("run exits 1 and the closing line counts 2 alerts", code == 1 and "Done with 2 ALERT(s)" in out6, out6[-300:])

        print("control: a helper with findings, nonzero exit, no traceback, is not an ALERT")
        findings = os.path.join(tmp, "findings")
        os.makedirs(os.path.join(findings, ".claude", "skills", "context-check"))
        plant(findings)
        write(os.path.join(findings, "docs", "architecture", "check.py"),
              "import sys\nprint('ALERT architecture: 1 finding(s)')\nprint('  AC-1 planted finding')\nsys.exit(1)\n")
        write(os.path.join(findings, "docs", "architecture", "README.md"), "---\nname: r\n---\n# r\n")
        code, out7 = run(findings)
        g7 = section(out7, "G")
        check("the finding is printed and the helper is named with its exit code",
              "AC-1 planted finding" in g7 and "(docs/architecture/check.py exited 1: it found problems" in g7, g7)
        check("no ALERT: line, and the run exits 0", "ALERT:" not in out7 and code == 0, out7[-300:])
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print()
    if failures:
        print(f"CONTEXT CHECK TESTS FAILED: {failures}")
        return 1
    print("CONTEXT CHECK TESTS PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
