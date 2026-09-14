#!/usr/bin/env python3
"""check_tests.py — proves context/sources/check.py can fail (the prove-it-can-fail rule).

Builds a small lab in a temp folder, registers two sources, and plants one fault at a time:
missing location, moved location, duplicate id, two sources claiming one location, one location nested
inside another's, a folder whose only files sit under _archive, a location with nothing matching its pattern, an unreadable location, a bad word (standing, use), a replica with no canonical-at, an unavailable source that is
reachable, an unregistered folder of markdown, an unregistered git repo. Each must be caught. The clean
register must pass. Last, the real register must pass.

  python3 context/sources/tests/check_tests.py
"""
import os, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
CHECK = os.path.join(os.path.dirname(HERE), "check.py")
LAB = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
FAILS = []


def check(name, ok, out=""):
    print(("ok   " if ok else "FAIL ") + name)
    if not ok:
        FAILS.append(name)
        print("     " + out.replace("\n", "\n     ")[:1200])


def run(*args, lab=None):
    cmd = [sys.executable, CHECK] + list(args)
    if lab:
        cmd += ["--lab", lab]
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=lab or LAB)
    return r.returncode, r.stdout + r.stderr


def record(i, location, pattern="*.md", **over):
    f = {"id": i, "kind": "test", "location": location, "pattern": pattern, "owner": "test", "standing": "canonical",
         "tier": "system", "date-field": "mtime", "status": "live", "use": "evidentiary", "may-inform": "tests",
         "not-alone": "anything", "read-by": "the tests", "added": "2026-09-12", "changed": "2026-09-12"}
    f.update(over)
    return f"### {f.get('heading', i)}\n" + "\n".join(f"- {k}: {v}" for k, v in f.items() if k != "heading" and v is not None) + "\n"


def write_register(lab, *records):
    p = os.path.join(lab, "context", "sources", "REGISTER.md")
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w").write("# test\n\n<!-- register:start -->\n\n" + "\n".join(records) + "\n<!-- register:end -->\n")


def fresh():
    lab = tempfile.mkdtemp(prefix="sources-test-")
    os.makedirs(os.path.join(lab, "context", "intent"))
    open(os.path.join(lab, "context", "intent", "STANDING.md"), "w").write("# drivers\n")
    os.makedirs(os.path.join(lab, "notes"))
    for n in ("a", "b"):
        open(os.path.join(lab, "notes", n + ".md"), "w").write(n)
    good = (record("drivers", "context/intent/STANDING.md", "STANDING.md", use="authoritative"),
            record("notes", "notes"))
    write_register(lab, *good)
    return lab, good


# 0. a clean register passes
lab, good = fresh()
code, out = run("--report", lab=lab)
check("clean register: OK and exit 0", code == 0 and out.startswith("OK sources: 2 registered (2 live, 0 outside the lab), 3 files covered"), out)
check("clean register: report lists both sources with readers", "drivers" in out and "read by: the tests" in out, out)

# 1. missing canonical source
os.remove(os.path.join(lab, "context", "intent", "STANDING.md"))
code, out = run(lab=lab)
check("missing location is caught, exit 1", code == 1 and "drivers: location missing: context/intent/STANDING.md" in out, out)
check("summary line says ALERT", run("--summary", lab=lab)[1].startswith("ALERT sources:"), out)

# 2. moved: the file exists somewhere else in the lab, and the finding says where
os.makedirs(os.path.join(lab, "elsewhere"))
open(os.path.join(lab, "elsewhere", "STANDING.md"), "w").write("moved\n")
code, out = run(lab=lab)
check("moved location names where the file is now", code == 1 and "a file of that name is at elsewhere/STANDING.md" in out, out)
shutil.rmtree(lab)

# 3. duplicate id
lab, good = fresh()
write_register(lab, *good, record("notes", "notes"))
code, out = run(lab=lab)
check("duplicate id is caught", code == 1 and "id 'notes' appears 2 times" in out, out)

# 4. two sources claim one location (competing canonical records)
write_register(lab, *good, record("notes-again", "notes"))
code, out = run(lab=lab)
check("two sources claiming one location is caught", code == 1 and "two sources claim one location: notes (notes, notes-again)" in out, out)

# 4b. one source's location sits inside another's (a file counted under two ids)
write_register(lab, *good, record("note-a", "notes/a.md", "a.md"))
code, out = run(lab=lab)
check("a location nested inside another source's is caught",
      code == 1 and "one source's location sits inside another's: notes/a.md (note-a) inside notes (notes)" in out, out)

# 4c. archived files are not evidence: a folder whose only markdown sits under _archive is empty
os.makedirs(os.path.join(lab, "arch", "_archive"))
open(os.path.join(lab, "arch", "_archive", "old.md"), "w").write("old")
write_register(lab, *good, record("arch", "arch"))
code, out = run(lab=lab)
check("a folder with files only under _archive is caught as empty", code == 1 and "arch: location holds no file matching *.md: arch" in out, out)
shutil.rmtree(os.path.join(lab, "arch"))

# 5. broken location: it exists but nothing inside matches the pattern
write_register(lab, good[0], record("notes", "notes", pattern="*.csv"))
code, out = run(lab=lab)
check("location with no matching file is caught", code == 1 and "notes: location holds no file matching *.csv: notes" in out, out)

# 5b. unreadable location: it exists, and this user cannot read it (F-20260912-0150-5)
write_register(lab, *good)
os.chmod(os.path.join(lab, "notes"), 0)
code, out = run(lab=lab)
os.chmod(os.path.join(lab, "notes"), 0o755)
if os.geteuid() == 0:
    print("skip unreadable location test: running as root, which can read anything")
else:
    check("unreadable location is caught", code == 1 and "notes: location unreadable: notes" in out, out)

# 6. invalid records: a bad word (standing, use), a missing use limit, a replica with no canonical-at, heading not equal to id
write_register(lab, good[0], record("notes", "notes", standing="copy"))
code, out = run(lab=lab)
check("bad standing word is caught", code == 1 and "notes: standing 'copy' is not an allowed word" in out, out)
write_register(lab, good[0], record("notes", "notes", use="opinion"))
code, out = run(lab=lab)
check("bad use word is caught", code == 1 and "notes: use 'opinion' is not an allowed word" in out, out)
write_register(lab, good[0], record("notes", "notes", **{"not-alone": None}))
code, out = run(lab=lab)
check("missing not-alone is caught", code == 1 and "notes: missing 'not-alone'" in out, out)
write_register(lab, good[0], record("notes", "notes", standing="replica"))
code, out = run(lab=lab)
check("replica without canonical-at is caught", code == 1 and "notes: standing is replica but no canonical-at" in out, out)
write_register(lab, *good, record("notes-copy", "elsewhere", standing="replica", **{"canonical-at": "notes"}))
os.makedirs(os.path.join(lab, "elsewhere")); open(os.path.join(lab, "elsewhere", "c.md"), "w").write("c")
code, out = run(lab=lab)
check("a copy with its own id is caught (one identity per source)", code == 1 and "notes-copy: canonical-at names another registered source 'notes'" in out, out)
shutil.rmtree(os.path.join(lab, "elsewhere"))
write_register(lab, good[0], record("notes", "notes", heading="Notes"))
code, out = run(lab=lab)
check("heading differing from id is caught", code == 1 and "heading 'Notes' differs from id 'notes'" in out, out)

# 7. an unavailable source that is reachable now: record only, exit 0
write_register(lab, *good, record("far", "elsewhere", standing="unavailable"))
os.makedirs(os.path.join(lab, "elsewhere"))
code, out = run(lab=lab)
check("reachable unavailable source is a record-only note, not a failure",
      code == 0 and "[record only] far: unavailable source is reachable now: elsewhere" in out, out)
shutil.rmtree(os.path.join(lab, "elsewhere"))

# 8. external location: existence checked, files not counted, and the summary names it; a missing one is caught
ext = tempfile.mkdtemp(prefix="sources-ext-")
write_register(lab, *good, record("outside", ext))
code, out = run("--report", lab=lab)
check("external source is named as outside the lab, not counted in files", code == 0 and "(3 live, 1 outside the lab: outside), 3 files covered" in out and "external" in out, out)
shutil.rmtree(ext)
code, out = run(lab=lab)
check("missing external location is caught", code == 1 and f"outside: location missing: {ext}" in out, out)

# 9. unregistered source references: a folder of markdown and a git repo
write_register(lab, *good)
os.makedirs(os.path.join(lab, "stuff"))
for k in range(10):
    open(os.path.join(lab, "stuff", f"{k}.md"), "w").write("x")
os.makedirs(os.path.join(lab, "repo", ".git"))
open(os.path.join(lab, "repo", "README.md"), "w").write("x")
code, out = run(lab=lab)
check("unregistered folder of 10 markdown files is proposed for review",
      code == 0 and "[show at open] folder with 10 markdown files that no source covers: stuff" in out, out)
check("unregistered git repo is proposed for review", "[show at open] git repo not under any registered source: repo" in out, out)
check("discovery never registers: register unchanged", "stuff" not in open(os.path.join(lab, "context", "sources", "REGISTER.md")).read())
os.makedirs(os.path.join(lab, "context", "sources"), exist_ok=True)
open(os.path.join(lab, "context", "sources", "discovery-accepted.txt"), "w").write("stuff | test, on purpose\nrepo | test\n")
code, out = run(lab=lab)
check("accepted candidates are counted, not listed", "stuff" not in out and "repo" not in out and "discovery: 0 to review" in out, out)

# 10. resolve: id to location, standing, and use limits; unknown id fails
code, out = run("resolve", "drivers", lab=lab)
check("resolve prints the current location and use limits",
      code == 0 and "location: context/intent/STANDING.md (exists)" in out and "use: authoritative" in out and "not-alone: anything" in out, out)
code, out = run("resolve", "nope", lab=lab)
check("resolve of an unknown id fails", code == 1 and "not registered: nope" in out, out)
write_register(lab, *good, record("old", "notes", status="retired"))
code, out = run("resolve", "old", lab=lab)
check("resolve of a retired source says do not read", code == 0 and "read: no (retired" in out, out)
code, out = run("list", lab=lab)
check("list prints one line per source", code == 0 and out.count("\n") == 3 and "old" in out, out)
shutil.rmtree(lab)

# 11. the real register passes
code, out = run()
check("the lab's own register passes", code == 0 and out.startswith("OK sources:"), out)

print()
print("all passed" if not FAILS else f"{len(FAILS)} failed: " + ", ".join(FAILS))
sys.exit(1 if FAILS else 0)
