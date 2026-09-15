#!/usr/bin/env python3
"""Tests for role-map.py, in the prove-it-can-fail form: a planted estate with one canonical, one
superseded location, and one derived folder must come back clean, and each planted fault must
be reported by name. Nothing here reads or writes the real lab or Dropbox.

Run:  python3 .claude/skills/context-check/tests/role_map_tests.py

Cases (Organization Standard sections 4, 6, 11; AD-40, 2026-09-15):
  1. clean          a valid estate reports 0 findings and exits 0
  2. duplicate      a second live derived marker with the same id is an interrupt finding
  3. resolved       remove the planted duplicate, rerun, and the finding is absent (closure by rerun)
  4. chain          replaced-by pointing at a superseded marker is supersession drift
  5. one-way        a superseded marker whose target has no `replaces` is one-way supersession
  6. write-after    a payload file changed after relocated-on is reported
  7. unconfirmed    a canonical marker declared by alfred-proposed is an interrupt finding
  8. manifest       a changed payload byte is manifest drift under --verify-manifests
  9. read-only      the planted estate is byte-for-byte unchanged after every run
 10. wrong root     a folder with no ROLE.md exits 2 with an ALERT line
 11. self           replaced-by naming the marker's own id is named as a fake replacement (AD-41)
 12. loop           two superseded markers replacing each other are named as a loop
 13. moved, no live relocated-to with no live marker for the id is relocation drift
 14. both           a marker carrying both relocated-to and replaced-by is relocation drift
 15. one-way move   a live marker without relocated-from, or a mismatched location name, is relocation drift
 16. move loop      two old locations relocated to each other with no live marker are named as a loop (AD-42)

Prints ROLE MAP TESTS PASSED only when every case passes.
"""
import hashlib
import os
import shutil
import subprocess
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(os.path.dirname(HERE), "role-map.py")
failures = 0


def check(name, ok, detail=""):
    global failures
    failures += 0 if ok else 1
    print(f"  {'ok ' if ok else 'FAIL'} {name}" + (f"  ({detail})" if detail and not ok else ""))


def run(*args):
    r = subprocess.run([sys.executable, SCRIPT, *args], capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


def marker(folder, **kv):
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, "ROLE.md"), "w") as fh:
        fh.write("# planted\n")
        for k, v in kv.items():
            fh.write(f"- {k.replace('_', '-')}: {v}\n")


def payload(folder, name, text, when="2026-09-01"):
    p = os.path.join(folder, name)
    with open(p, "w") as fh:
        fh.write(text)
    t = time.mktime(time.strptime(when, "%Y-%m-%d"))
    os.utime(p, (t, t))
    return p


def manifest(folder):
    lines = []
    for n in sorted(os.listdir(folder)):
        if n in ("ROLE.md", "MANIFEST.txt"):
            continue
        h = hashlib.sha256(open(os.path.join(folder, n), "rb").read()).hexdigest()
        lines.append(f"{h}  {n}")
    with open(os.path.join(folder, "MANIFEST.txt"), "w") as fh:
        fh.write("\n".join(lines) + "\n")


def tree_hash(root):
    h = hashlib.sha256()
    for dp, dn, fn in os.walk(root):
        for f in sorted(fn):
            p = os.path.join(dp, f)
            h.update(p.encode()); h.update(open(p, "rb").read())
    return h.hexdigest()


def build(root):
    base = dict(area="work", scope="ai-lab", as_of="2026-09-15", declared_by="venkat")
    new = os.path.join(root, "snapshots")
    old = os.path.join(root, "old-snapshots")
    marker(new, id="lab-snapshots", role="derived", derived_from="lab", built="2026-09-10", relocated_from="old-snapshots", **base)
    payload(new, "a.tar.gz", "aaa", "2026-09-08")
    payload(new, "b.tar.gz", "bbb", "2026-09-10")
    manifest(new)
    marker(old, id="lab-snapshots", role="historical", relocated_to="snapshots", relocated_on="2026-09-15", **base)
    marker(os.path.join(root, "lab"), id="lab", role="canonical", replaces="lab-old", **base)
    marker(os.path.join(root, "lab-old"), id="lab-old", role="historical", replaced_by="lab", replaced_on="2026-09-15", **base)
    return new, old


def main():
    tmp = tempfile.mkdtemp(prefix="role-map-test-")
    try:
        root = os.path.join(tmp, "estate")
        new, old = build(root)
        before = tree_hash(root)

        print("1. clean")
        code, out = run(root)
        check("exit 0", code == 0, out)
        check("findings 0", "findings 0 (" in out, out)
        check("read-only", tree_hash(root) == before)

        print("2. duplicate canonical")
        dup = os.path.join(root, "snapshots-copy")
        marker(dup, id="lab-snapshots", role="derived", area="work", scope="ai-lab", as_of="2026-09-15", declared_by="venkat", built="2026-09-10")
        code, out = run(root)
        check("exit 1", code == 1, out)
        check("named", "[interrupt] duplicate canonical: id 'lab-snapshots' is live in 2 places" in out, out)

        print("3. resolved by rerun")
        shutil.rmtree(dup)
        code, out = run(root)
        check("finding absent", code == 0 and "duplicate canonical" not in out, out)

        print("4. chain longer than one hop")
        mid = os.path.join(root, "middle")
        marker(mid, id="lab-snapshots-mid", role="historical", replaced_by="lab-snapshots", replaced_on="2026-09-15", area="work", scope="ai-lab", as_of="2026-09-15", declared_by="venkat")
        chain = os.path.join(root, "oldest")
        marker(chain, id="lab-snapshots-oldest", role="historical", replaced_by="lab-snapshots-mid", replaced_on="2026-09-15", area="work", scope="ai-lab", as_of="2026-09-15", declared_by="venkat")
        code, out = run(root)
        check("named", "supersession drift" in out and "replaced-by 'lab-snapshots-mid' has no live marker" in out, out)
        shutil.rmtree(mid); shutil.rmtree(chain)

        print("5. one-way supersession")
        p = os.path.join(root, "lab", "ROLE.md")
        text = open(p).read()
        open(p, "w").write(text.replace("- replaces: lab-old\n", ""))
        code, out = run(root)
        check("named", "one-way supersession" in out and "carries no replaces naming 'lab-old'" in out, out)
        open(p, "w").write(text)

        print("6. write after supersession")
        late = payload(old, "sneaked.txt", "x", "2026-09-16")
        code, out = run(root)
        check("named", "write after supersession" in out and "sneaked.txt" in out, out)
        os.remove(late)

        print("7. unconfirmed canonical")
        prop = os.path.join(root, "proposed")
        marker(prop, id="new-thing", role="canonical", area="work", scope="ai-lab", as_of="2026-09-15", declared_by="alfred-proposed")
        code, out = run(root)
        check("named", "[interrupt] unconfirmed canonical" in out, out)
        shutil.rmtree(prop)

        print("8. manifest drift")
        code, out = run(root, "--verify-manifests")
        check("clean manifests first", code == 0, out)
        a = os.path.join(new, "a.tar.gz")
        keep = open(a).read()
        open(a, "w").write("changed"); t = time.mktime(time.strptime("2026-09-08", "%Y-%m-%d")); os.utime(a, (t, t))
        code, out = run(root, "--verify-manifests")
        check("named", "manifest drift" in out and "'a.tar.gz' sha256 differs" in out, out)
        open(a, "w").write(keep); os.utime(a, (t, t))

        print("9. read-only after all runs")
        check("unchanged", tree_hash(root) == before)

        print("10. wrong root")
        empty = os.path.join(tmp, "nothing"); os.makedirs(empty)
        code, out = run(empty)
        check("exit 2 with ALERT", code == 2 and "ALERT role-map" in out, out)

        print("11. self-replacement")
        selfy = os.path.join(root, "selfy")
        marker(selfy, id="selfy", role="historical", replaced_by="selfy", replaced_on="2026-09-15", area="work", scope="ai-lab", as_of="2026-09-15", declared_by="venkat")
        code, out = run(root)
        check("named", "replaced-by names its own id 'selfy'" in out, out)
        shutil.rmtree(selfy)

        print("12. genuine loop")
        la = os.path.join(root, "loop-a"); lb = os.path.join(root, "loop-b")
        marker(la, id="loop-a", role="historical", replaced_by="loop-b", replaced_on="2026-09-15", area="work", scope="ai-lab", as_of="2026-09-15", declared_by="venkat")
        marker(lb, id="loop-b", role="historical", replaced_by="loop-a", replaced_on="2026-09-15", area="work", scope="ai-lab", as_of="2026-09-15", declared_by="venkat")
        code, out = run(root)
        check("named as loop", "supersession drift" in out and "(loop loop-a -> loop-b -> loop-a)" in out, out)
        shutil.rmtree(la); shutil.rmtree(lb)

        print("13. moved with no live marker")
        gone = os.path.join(root, "gone")
        marker(gone, id="vanished", role="historical", relocated_to="nowhere", relocated_on="2026-09-15", area="work", scope="ai-lab", as_of="2026-09-15", declared_by="venkat")
        code, out = run(root)
        check("named", "relocation drift" in out and "no live marker carries id 'vanished'" in out, out)
        shutil.rmtree(gone)

        print("14. both fields")
        both = os.path.join(root, "both")
        marker(both, id="lab-old", role="historical", relocated_to="lab", relocated_on="2026-09-15", replaced_by="lab", replaced_on="2026-09-15", area="work", scope="ai-lab", as_of="2026-09-15", declared_by="venkat")
        code, out = run(root)
        check("named", "carries both relocated-to and replaced-by" in out, out)
        shutil.rmtree(both)
        check("clean again", run(root)[0] == 0)

        print("15. one-way relocation")
        p = os.path.join(new, "ROLE.md")
        text = open(p).read()
        open(p, "w").write(text.replace("- relocated-from: old-snapshots\n", ""))
        code, out = run(root)
        check("missing relocated-from named", "carries no relocated-from naming 'old-snapshots'" in out, out)
        open(p, "w").write(text.replace("- relocated-from: old-snapshots\n", "- relocated-from: elsewhere\n"))
        code, out = run(root)
        check("mismatch named", "relocated-from 'elsewhere' but no old marker" in out, out)
        open(p, "w").write(text)
        check("clean again", run(root)[0] == 0)

        print("16. relocation loop")
        ra = os.path.join(root, "ring-a"); rb = os.path.join(root, "ring-b")
        marker(ra, id="ring", role="historical", relocated_to="ring-b", relocated_on="2026-09-15", area="work", scope="ai-lab", as_of="2026-09-15", declared_by="venkat")
        marker(rb, id="ring", role="historical", relocated_to="ring-a", relocated_on="2026-09-15", area="work", scope="ai-lab", as_of="2026-09-15", declared_by="venkat")
        code, out = run(root)
        check("named as loop", "relocation loop for id 'ring': ring-a -> ring-b -> ring-a" in out or "relocation loop for id 'ring': ring-b -> ring-a -> ring-b" in out, out)
        shutil.rmtree(ra); shutil.rmtree(rb)
        check("clean again", run(root)[0] == 0)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    if failures:
        print(f"ROLE MAP TESTS FAILED: {failures}")
        return 1
    print("ROLE MAP TESTS PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
