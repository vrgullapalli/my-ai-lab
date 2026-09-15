#!/usr/bin/env python3
"""Tests for unlazy-bind.py, the hook that binds a new scoped unlazy ledger to the
session that wrote it.

Run:  python3 .claude/hooks/tests/unlazy-bind-tests.py .claude/hooks/unlazy-bind.py

Every case builds a fresh temporary lab root, points the hook at it through
CLAUDE_PROJECT_DIR, feeds it one PostToolUse payload, and reads what is under
.unlazy/<scope>/session afterwards.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile

HOOK = os.path.abspath(sys.argv[1])
TEMPLATE = "# Gates\n\n- [ ] G1: pending\n  EVIDENCE: pending\n"


def run_hook(root, tool, tool_input, session=None, key="session_id", cwd=None):
    payload = {"tool_name": tool, "tool_input": tool_input, "cwd": cwd or root,
               "hook_event_name": "PostToolUse", "tool_response": {}}
    if session is not None:
        payload[key] = session
    env = dict(os.environ, CLAUDE_PROJECT_DIR=root)
    return subprocess.run([sys.executable, HOOK], input=json.dumps(payload), capture_output=True,
                          text=True, env=env, timeout=20)


def scope(root, name, bound=None):
    d = os.path.join(root, ".unlazy", name)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "GATES.md"), "w") as f:
        f.write(TEMPLATE)
    if bound is not None:
        with open(os.path.join(d, "session"), "w") as f:
            f.write(bound + "\n")
    return d


def binding(root, name):
    p = os.path.join(root, ".unlazy", name, "session")
    if not os.path.exists(p):
        return None
    with open(p) as f:
        return f.read().strip()


CASES = []


def case(name):
    def wrap(fn):
        CASES.append((name, fn))
        return fn
    return wrap


@case("Write into a new scope binds it to the writing session")
def _(root):
    scope(root, "api")
    r = run_hook(root, "Write", {"file_path": root + "/.unlazy/api/GATES.md"}, "sess-A")
    assert r.returncode == 0, r.stderr
    assert binding(root, "api") == "sess-A", binding(root, "api")


@case("Edit into a nested gates file binds the scope")
def _(root):
    scope(root, "api")
    r = run_hook(root, "Edit", {"file_path": root + "/.unlazy/api/gates/leaf-1.md"}, "sess-A")
    assert r.returncode == 0 and binding(root, "api") == "sess-A"


@case("A relative Write path resolves against the payload cwd")
def _(root):
    scope(root, "api")
    run_hook(root, "Write", {"file_path": ".unlazy/api/GATES.md"}, "sess-A")
    assert binding(root, "api") == "sess-A"


@case("Bash copy of the template into a scope binds it")
def _(root):
    scope(root, "web")
    run_hook(root, "Bash", {"command": "cp templates/gates-leaf.md .unlazy/web/GATES.md"}, "sess-B")
    assert binding(root, "web") == "sess-B"


@case("Bash heredoc into a scope binds it")
def _(root):
    scope(root, "x1")
    cmd = "mkdir -p .unlazy/x1 && cat > .unlazy/x1/GATES.md <<'EOF'\n# Gates\n- [ ] G1: a\nEOF"
    run_hook(root, "Bash", {"command": cmd}, "sess-C")
    assert binding(root, "x1") == "sess-C"


@case("An ordinary file written inside an unowned scope does not bind it (Write tool)")
def _(root):
    scope(root, "api")
    for rel in ("notes.md", "PLAN.md", "dispatch.json", "status.log", "gates/README.txt"):
        run_hook(root, "Write", {"file_path": root + "/.unlazy/api/" + rel}, "sess-B")
        assert binding(root, "api") is None, rel


@case("An ordinary shell write inside an unowned scope does not bind it")
def _(root):
    scope(root, "api")
    run_hook(root, "Bash", {"command": "echo started >> .unlazy/api/status.log; cp plan.md .unlazy/api/PLAN.md"}, "sess-B")
    assert binding(root, "api") is None


@case("Making the scope folder alone does not bind it")
def _(root):
    scope(root, "api")
    run_hook(root, "Bash", {"command": "mkdir -p .unlazy/api/gates"}, "sess-B")
    assert binding(root, "api") is None


@case("After an ordinary write by B, the ledger write by A still makes A the owner")
def _(root):
    scope(root, "api")
    run_hook(root, "Write", {"file_path": root + "/.unlazy/api/notes.md"}, "sess-B")
    run_hook(root, "Write", {"file_path": root + "/.unlazy/api/GATES.md"}, "sess-A")
    assert binding(root, "api") == "sess-A"


@case("An ordinary write by another session never moves an existing binding")
def _(root):
    scope(root, "api", bound="sess-A")
    run_hook(root, "Write", {"file_path": root + "/.unlazy/api/notes.md"}, "sess-B")
    run_hook(root, "Bash", {"command": "echo x > .unlazy/api/status.log"}, "sess-B")
    assert binding(root, "api") == "sess-A"


@case("Bash that only reads a scope does not bind it")
def _(root):
    scope(root, "api")
    run_hook(root, "Bash", {"command": "cat .unlazy/api/GATES.md; node gate-check.mjs --scope api --status"}, "sess-Z")
    assert binding(root, "api") is None


@case("An existing binding is never overwritten by another session")
def _(root):
    scope(root, "api", bound="sess-A")
    run_hook(root, "Write", {"file_path": root + "/.unlazy/api/GATES.md"}, "sess-B")
    assert binding(root, "api") == "sess-A"


@case("The Read tool never binds")
def _(root):
    scope(root, "api")
    run_hook(root, "Read", {"file_path": root + "/.unlazy/api/GATES.md"}, "sess-A")
    assert binding(root, "api") is None


@case("No session id in the payload means no binding")
def _(root):
    scope(root, "api")
    run_hook(root, "Write", {"file_path": root + "/.unlazy/api/GATES.md"})
    assert binding(root, "api") is None


@case("The older sessionId key still binds")
def _(root):
    scope(root, "api")
    run_hook(root, "Write", {"file_path": root + "/.unlazy/api/GATES.md"}, "sess-old", key="sessionId")
    assert binding(root, "api") == "sess-old"


@case("A path outside the project root never binds")
def _(root):
    other = tempfile.mkdtemp(prefix="unlazy-bind-other-")
    try:
        scope(other, "api")
        run_hook(root, "Write", {"file_path": other + "/.unlazy/api/GATES.md"}, "sess-A")
        assert binding(other, "api") is None
    finally:
        shutil.rmtree(other, ignore_errors=True)


@case("The locks folder and a bad scope id never bind")
def _(root):
    os.makedirs(os.path.join(root, ".unlazy", "locks"), exist_ok=True)
    run_hook(root, "Write", {"file_path": root + "/.unlazy/locks/GATES.md"}, "sess-A")
    assert binding(root, "locks") is None
    run_hook(root, "Write", {"file_path": root + "/.unlazy/../GATES.md"}, "sess-A")
    assert not os.path.exists(os.path.join(root, "session"))


@case("A scope folder that does not exist (the write failed) is skipped quietly")
def _(root):
    r = run_hook(root, "Write", {"file_path": root + "/.unlazy/ghost/GATES.md"}, "sess-A")
    assert r.returncode == 0 and r.stdout.strip() == "", r.stdout + r.stderr
    assert not os.path.exists(os.path.join(root, ".unlazy", "ghost"))


@case("A symlinked scope folder is never bound")
def _(root):
    real = tempfile.mkdtemp(prefix="unlazy-bind-real-")
    try:
        os.makedirs(os.path.join(root, ".unlazy"), exist_ok=True)
        os.symlink(real, os.path.join(root, ".unlazy", "link"))
        run_hook(root, "Write", {"file_path": root + "/.unlazy/link/GATES.md"}, "sess-A")
        assert not os.path.exists(os.path.join(real, "session"))
    finally:
        shutil.rmtree(real, ignore_errors=True)


@case("Two sessions writing two scopes each own their own")
def _(root):
    scope(root, "one")
    scope(root, "two")
    run_hook(root, "Write", {"file_path": root + "/.unlazy/one/GATES.md"}, "sess-1")
    run_hook(root, "Write", {"file_path": root + "/.unlazy/two/GATES.md"}, "sess-2")
    assert binding(root, "one") == "sess-1" and binding(root, "two") == "sess-2"


@case("A root GATES.md write binds nothing and prints nothing")
def _(root):
    r = run_hook(root, "Write", {"file_path": root + "/GATES.md"}, "sess-A")
    assert r.returncode == 0 and r.stdout.strip() == ""
    assert not os.path.exists(os.path.join(root, ".unlazy"))


@case("Bad JSON on stdin exits 0 and prints nothing")
def _(root):
    env = dict(os.environ, CLAUDE_PROJECT_DIR=root)
    r = subprocess.run([sys.executable, HOOK], input="{not json", capture_output=True, text=True, env=env)
    assert r.returncode == 0 and r.stdout.strip() == ""


def main():
    if not os.path.exists(HOOK):
        print("HOOK NOT FOUND: " + HOOK)
        print("UNLAZY-BIND TESTS FAILED")
        sys.exit(1)
    failed = 0
    for name, fn in CASES:
        root = tempfile.mkdtemp(prefix="unlazy-bind-test-")
        try:
            fn(root)
            print("ok   " + name)
        except AssertionError as exc:
            failed += 1
            print("FAIL " + name + (" :: " + str(exc) if str(exc) else ""))
        except Exception as exc:
            failed += 1
            print("FAIL " + name + " :: " + exc.__class__.__name__ + ": " + str(exc))
        finally:
            shutil.rmtree(root, ignore_errors=True)
    print("%d of %d passed" % (len(CASES) - failed, len(CASES)))
    if failed:
        print("UNLAZY-BIND TESTS FAILED")
        sys.exit(1)
    print("UNLAZY-BIND TESTS PASSED")


if __name__ == "__main__":
    main()
