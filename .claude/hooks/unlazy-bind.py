#!/usr/bin/env python3
"""unlazy-bind: binds a new scoped unlazy ledger to the session that wrote it.

A PostToolUse hook on Write, Edit, MultiEdit, NotebookEdit, and Bash. When the tool call
wrote a scope's ledger, `.unlazy/<scope>/GATES.md` or `.unlazy/<scope>/gates/<name>.md`,
and that scope has no `session` file yet, this writes the
hook payload's `session_id` there (the older `sessionId` key is read as a fallback only).
That file is the same binding `gate-check.mjs --bind` writes by hand, and the Stop hook
already reads it. An existing binding is never overwritten, so `--bind` stays the way to
reattach a scope on purpose. It prints nothing and never blocks.

Why (2026-09-15): the Stop hook only holds a session to a scope bound to it. Until this
hook, binding was a step to remember, and nothing in the lab had ever run it. Ownership
should follow the write, not memory.

What it reads: for the file tools, the path in `tool_input`; for Bash, the paths the
command would create or write, from `bash_targets` in root-lock.py, the lab's one parser
for that question. Reading a ledger never binds it, and neither does any other write inside
the scope (its plan, dispatch state, status log, or the folder itself). Tightened 2026-09-15
at Venkat's word: "working inside a scope does not prove ownership; establishing or
explicitly claiming its ledger does."
"""
import importlib.util
import json
import os
import sys

SCOPE_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789._-"
HOOKS_DIR = os.path.dirname(os.path.abspath(__file__))


def valid_scope(name):
    """Mirror of SCOPE_RE in the skill's gates.mjs, plus its `locks` exclusion."""
    if not name or len(name) > 64 or name in (".", "..", "locks"):
        return False
    if not (name[0].isalnum() and name[0].isascii()):
        return False
    return all(c in SCOPE_CHARS for c in name)


def root_lock():
    spec = importlib.util.spec_from_file_location("root_lock", os.path.join(HOOKS_DIR, "root-lock.py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def written_paths(payload, cwd):
    tool = payload.get("tool_name", "")
    tool_input = payload.get("tool_input") or {}
    lock = root_lock()
    if tool in ("Write", "Edit", "MultiEdit", "NotebookEdit"):
        path = tool_input.get("file_path") or tool_input.get("notebook_path") or ""
        resolved = lock.resolve(path, cwd)
        return [resolved] if resolved else []
    if tool == "Bash":
        try:
            return [path for path, _how in lock.bash_targets(tool_input.get("command", ""), cwd)]
        except ValueError:
            return []
    return []


def scope_of(path, root):
    """The scope id when `path` is one of the scope's ledger files, else None.

    Only the files the Stop hook reads as ledgers count: `.unlazy/<scope>/GATES.md`
    and `.unlazy/<scope>/gates/<name>.md`. Working inside a scope (its plan, dispatch
    state, status log, or any other file) does not prove ownership; writing its ledger does.
    """
    base = os.path.join(root, ".unlazy") + os.sep
    if not path.startswith(base):
        return None
    parts = path[len(base):].split(os.sep)
    name = parts[0]
    if not valid_scope(name):
        return None
    rest = parts[1:]
    is_ledger = (rest == ["GATES.md"] or
                 (len(rest) == 2 and rest[0] == "gates" and rest[1].endswith(".md") and rest[1] != ".md"))
    return name if is_ledger else None


def bind(root, name, session):
    folder = os.path.join(root, ".unlazy", name)
    if os.path.islink(folder) or not os.path.isdir(folder):
        return
    if os.path.realpath(folder) != os.path.join(os.path.realpath(root), ".unlazy", name):
        return
    target = os.path.join(folder, "session")
    try:
        fd = os.open(target, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    except FileExistsError:
        return
    with os.fdopen(fd, "w") as f:
        f.write(session + "\n")


def main():
    try:
        payload = json.loads(sys.stdin.read() or "{}")
    except ValueError:
        return
    session = str(payload.get("session_id") or payload.get("sessionId") or "").strip()
    if not session or "\n" in session:
        return
    root = os.environ.get("CLAUDE_PROJECT_DIR") or payload.get("cwd") or os.getcwd()
    root = os.path.normpath(os.path.abspath(root))
    cwd = payload.get("cwd") or root
    seen = set()
    for path in written_paths(payload, cwd):
        name = scope_of(path, root)
        if name and name not in seen:
            seen.add(name)
            bind(root, name, session)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass  # never let the binding step disturb a tool call
    sys.exit(0)
