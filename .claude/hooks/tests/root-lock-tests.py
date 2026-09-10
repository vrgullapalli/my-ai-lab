#!/usr/bin/env python3
"""Tests for the lab root lock.

Run:  python3 root-lock-tests.py <path-to-hook>

Every case says what the hook must decide. A guard nobody has watched fail is not a
guard (the prove-it-can-fail skill): run this against a deliberately broken copy of
the hook and it must report failures. It prints ROOT-LOCK TESTS PASSED only when every
case passes, so a script can check for that line.

The lab path is built while the tests run, on purpose. If it sat in this file as one
literal string, the root lock would read this file's own contents as commands.
"""
import json
import subprocess
import sys

HOOK = sys.argv[1]
LAB = "/Users/venkatgullapalli/Documents/" + "my-ai-lab"


def p(rel):
    return LAB + "/" + rel


def bash(cmd, cwd=LAB):
    return ("Bash", {"command": cmd}, cwd)


def write(path, tool="Write"):
    return (tool, {"file_path": path}, LAB)


CASES = [
    # --- file tools
    ("Write a new folder at the root", write(p("_archive/x.md")), "DENY"),
    ("Write a loose file at the root", write(p("notes.md")), "DENY"),
    ("Edit CLAUDE.md", write(p("CLAUDE.md"), "Edit"), "ALLOW"),
    ("Edit .gitignore", write(p(".gitignore"), "Edit"), "ALLOW"),
    ("Remember plugin state", write(p(".remember/now.md")), "ALLOW"),
    ("Write inside work-os", write(p("work-os/brand-os/x.md")), "ALLOW"),
    ("Write inside .claude", write(p(".claude/skills/a/SKILL.md")), "ALLOW"),
    ("unlazy ledger at the root", write(p("GATES.md")), "ALLOW"),
    ("Write outside the lab", write("/tmp/x.md"), "ALLOW"),
    ("Read anything", ("Read", {"file_path": p("anything.md")}, LAB), "ALLOW"),
    # --- shell: creating things
    ("mkdir at the root, full path", bash(f"mkdir -p {p('_backups')}"), "DENY"),
    ("mkdir at the root, relative path", bash("mkdir -p _backups"), "DENY"),
    ("mkdir inside work-os, relative", bash("mkdir -p work-os/new"), "ALLOW"),
    ("mkdir with a mode value", bash("mkdir -m 755 work-os/x"), "ALLOW"),
    ("fd number is not a path", bash("mkdir -p work-os/x 2>/dev/null"), "ALLOW"),
    ("variable set in the same command", bash(f"L={LAB}; mkdir -p $L/_archive"), "DENY"),
    ("follows cd out of the lab", bash("cd /tmp && mkdir scratch"), "ALLOW"),
    ("follows cd into a domain", bash("cd work-os && mkdir new"), "ALLOW"),
    ("copy into a new root folder", bash(f"cp {p('work-os/a')} {p('newdir/')}"), "DENY"),
    ("copy out of the lab reads only", bash(f"cp {p('.mcp.json')} /tmp/"), "ALLOW"),
    ("move within work-os", bash(f"mv {p('work-os/a')} {p('work-os/b')}"), "ALLOW"),
    ("clone into the root", bash(f"git clone https://example.com/x.git {p('newrepo')}"), "DENY"),
    ("download into the root", bash(f"curl -sL -o {p('dl.zip')} https://example.com/a"), "DENY"),
    ("unpack into the root", bash(f"tar -xzf /tmp/x.tgz -C {LAB}"), "DENY"),
    ("unlazy state folder", bash(f"touch {p('.unlazy/x')}"), "ALLOW"),
    # --- shell: redirects
    ("redirect to the root, full path", bash(f"echo hi > {p('stray.txt')}"), "DENY"),
    ("redirect to the root, relative", bash("echo hi > stray.txt"), "DENY"),
    ("redirect outside the lab", bash("echo hi > /tmp/x.txt"), "ALLOW"),
    ("stderr to stdout is not a file", bash("ls work-os 2>&1 | head"), "ALLOW"),
    # --- shell: reads that version 1 wrongly refused
    ("'committee' contains 'tee'", bash(f"grep -rn committee {p('.claude/skills')}"), "ALLOW"),
    ("'mcpServers' contains 'cp'",
     bash(f"python3 -c \"import os; print(os.path.exists('{p('.mcp.json')}'))\" # mcpServers"), "ALLOW"),
    ("listing the root", bash(f"ls -la {LAB}"), "ALLOW"),
    ("a comment is not a command", bash("ls # mkdir _archive"), "ALLOW"),
    ("new line separates commands", bash("mkdir -p work-os/a\nls -la"), "ALLOW"),
    # --- heredocs
    ("heredoc body is data",
     bash(f"cat > {p('work-os/x.md')} <<'EOF'\nmkdir _archive\ncp a b\nEOF"), "ALLOW"),
    ("heredoc written to the root",
     bash(f"cat > {p('stray.md')} <<'EOF'\nhello\nEOF"), "DENY"),
]


def run(tool, tool_input, cwd):
    payload = json.dumps({"tool_name": tool, "tool_input": tool_input, "cwd": cwd})
    out = subprocess.run([HOOK], input=payload, capture_output=True, text=True, timeout=10)
    if out.returncode != 0:
        return "ERROR(exit %d)" % out.returncode
    return "DENY" if '"deny"' in out.stdout else "ALLOW"


def main():
    failures = 0
    for name, (tool, tool_input, cwd), expected in CASES:
        got = run(tool, tool_input, cwd)
        ok = got == expected
        failures += 0 if ok else 1
        print(f"  {'PASS' if ok else 'FAIL'}  {name:<40} expected {expected:<5} got {got}")
    # the guard must not crash or block on a payload it cannot read
    out = subprocess.run([HOOK], input="not json", capture_output=True, text=True, timeout=10)
    ok = out.returncode == 0 and '"deny"' not in out.stdout
    failures += 0 if ok else 1
    print(f"  {'PASS' if ok else 'FAIL'}  {'unreadable payload fails open':<40} exit {out.returncode}")
    total = len(CASES) + 1
    print(f"\n{total - failures} of {total} passed")
    if failures:
        sys.exit(1)
    print("ROOT-LOCK TESTS PASSED")


if __name__ == "__main__":
    main()
