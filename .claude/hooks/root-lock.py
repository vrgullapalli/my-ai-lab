#!/usr/bin/env python3
"""root-lock: refuses to let anything new be created at the lab root.

A PreToolUse hook. Claude Code hands it the tool call as JSON on stdin. It prints a
deny decision, or it prints nothing and the call goes ahead.

Why it exists: on 2026-09-09 _archive/ and _backups/ reappeared at the root twice,
because the rules said to put them there. The rules were fixed. This is the guard.

Version 2, 2026-09-10. Version 1 looked for creation words anywhere in a command, so
"mcpServers" (it contains "cp") and "committee" (it contains "tee") made harmless reads
look like writes and got refused. It also ignored relative paths, so `mkdir _archive`
typed from the lab root walked straight past it. Version 2 reads the command properly:
it looks only at what a command would create or write, and it resolves relative paths
against the working folder, following any `cd` along the way.

What it cannot see: files written by a program (python, node) or by a plugin's own
hook. It guards the shell and the file tools, which is where the mistakes happened.

It fails open. If it cannot read something, it lets the call through and says so,
because a broken guard that refused every tool call would lock the session out.

To change what may live at the root, edit ALLOWED below. Ask Venkat first.
"""
import json
import os
import re
import shlex
import sys

LAB = "/Users/venkatgullapalli/Documents/my-ai-lab"

ALLOWED = {
    # what the lab root is for
    "CLAUDE.md", "ROOT.md", "TASTE.md", "RULINGS-IN-FORCE.md", "DONE.md",
    ".claude", "context", "evidence", "work-os", "docs",
    # machinery that has to sit at the root
    ".git", ".gitignore", ".DS_Store", ".remember",
    # unlazy's working ledger and its state. Git ignores them. Cleared when the work is done.
    "GATES.md", ".unlazy", ".unlazy-hook-state.json",
}

ALLOWED_TEXT = ("CLAUDE.md, ROOT.md, TASTE.md, RULINGS-IN-FORCE.md, DONE.md, .claude/, "
                "context/, evidence/, work-os/, docs/ -- plus .git, .gitignore, .remember, "
                "and unlazy's GATES.md and .unlazy/")

WRAPPERS = {"sudo", "env", "command", "nohup", "time", "exec", "builtin", "nice", "export"}
MAKE_EVERY_ARG = {"mkdir", "touch", "tee"}
MAKE_LAST_ARG = {"cp", "mv", "ln", "install", "rsync", "ditto", "scp"}
OPTS_WITH_VALUE = {
    "mkdir": {"-m"},
    "touch": {"-t", "-r", "-d", "-A"},
    "install": {"-m", "-o", "-g"},
    "rsync": {"-e", "--exclude", "--include", "--filter", "--exclude-from", "--include-from"},
    "scp": {"-P", "-i", "-o", "-F"},
    "tee": set(), "cp": set(), "mv": set(), "ln": set(), "ditto": set(),
}
PUNCT = set("();<>|&\n")
VAR = re.compile(r"\$\{?([A-Za-z_][A-Za-z0-9_]*)\}?")


def deny(entry, how):
    reason = (f'The lab root is locked. {how} "{entry}" there, and that is not one of the '
              f"things allowed at the root.\n\nAllowed at the root: {ALLOWED_TEXT}\n\n"
              "Put it inside a domain instead, or in ~/Documents/_warehouse/ if it is "
              "finished with. If it genuinely belongs at the root, ask Venkat first and "
              "add it to ALLOWED in .claude/hooks/root-lock.py.")
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": reason}}))
    sys.exit(0)


def allow_with_note(message):
    print(json.dumps({"systemMessage": "root-lock: " + message + " -- allowed without a check."}))
    sys.exit(0)


def resolve(path, cwd):
    """Absolute, normalised path, or None when it depends on something we cannot know."""
    if not path or any(c in path for c in "$`*?[{"):
        return None
    p = os.path.expanduser(path)
    if not os.path.isabs(p):
        p = os.path.join(cwd, p)
    return os.path.normpath(p)


def root_entry(abs_path):
    if abs_path and abs_path.startswith(LAB + os.sep):
        return abs_path[len(LAB) + 1:].split(os.sep)[0]
    return None


def strip_heredocs(cmd):
    """Drop heredoc bodies. Their text is data being written, not commands being run."""
    out, waiting = [], []
    for line in cmd.split("\n"):
        if waiting:
            if line.strip() == waiting[0]:
                waiting.pop(0)
            continue
        out.append(line)
        for m in re.finditer(r"<<-?\s*(['\"]?)([A-Za-z_][A-Za-z0-9_]*)\1", line):
            waiting.append(m.group(2))
    return "\n".join(out)


def tokenize(cmd):
    lex = shlex.shlex(cmd, posix=True, punctuation_chars="();<>|&\n")
    lex.whitespace = " \t\r"
    lex.whitespace_split = True
    lex.commenters = ""
    return list(lex)


def is_punct(tok):
    return bool(tok) and all(c in PUNCT for c in tok)


def bash_targets(cmd, cwd):
    """Every (absolute path, how) this command would create or write inside the lab."""
    tokens = tokenize(strip_heredocs(cmd))
    found = []
    shell_vars = {"HOME": os.path.expanduser("~")}
    state = {"cwd": cwd}

    def expand(tok):
        return VAR.sub(lambda m: shell_vars.get(m.group(1), m.group(0)), tok)

    def add(path, how):
        p = resolve(expand(path), state["cwd"])
        if p:
            found.append((p, how))

    def run_simple(argv):
        # leading VAR=value words set variables (or prefix one command)
        while argv and re.match(r"^[A-Za-z_][A-Za-z0-9_]*=", argv[0]):
            name, _, value = argv[0].partition("=")
            shell_vars[name] = expand(value)
            argv = argv[1:]
        while argv and argv[0] in WRAPPERS:
            argv = argv[1:]
            while argv and re.match(r"^[A-Za-z_][A-Za-z0-9_]*=", argv[0]):
                name, _, value = argv[0].partition("=")
                shell_vars[name] = expand(value)
                argv = argv[1:]
        if not argv or argv[0].startswith("#"):
            return
        name = os.path.basename(argv[0])
        args = [a for a in argv[1:]]
        cut = next((i for i, a in enumerate(args) if a.startswith("#")), None)
        if cut is not None:
            args = args[:cut]

        if name == "cd":
            dest = next((a for a in args if not a.startswith("-")), "~")
            p = resolve(expand(dest), state["cwd"])
            if p:
                state["cwd"] = p
            return

        if name == "git" and args and args[0] in ("clone", "init"):
            ops = [a for a in args[1:] if not a.startswith("-")]
            if args[0] == "clone" and len(ops) >= 2:
                add(ops[-1], "Cloning a repository into")
            if args[0] == "init" and ops:
                add(ops[-1], "Creating a repository at")
            return

        if name in ("curl", "wget"):
            flags = {"curl": ("-o", "--output"), "wget": ("-O", "--output-document")}[name]
            for i, a in enumerate(args):
                if a in flags and i + 1 < len(args):
                    add(args[i + 1], "Downloading to")
            return

        if name == "tar":
            creating, archive, outdir, extracting = False, None, None, False
            i = 0
            while i < len(args):
                a = args[i]
                if a in ("-C", "--directory") and i + 1 < len(args):
                    outdir = args[i + 1]; i += 2; continue
                if a.startswith("--directory="):
                    outdir = a.split("=", 1)[1]; i += 1; continue
                if a.startswith("--file="):
                    archive = a.split("=", 1)[1]; i += 1; continue
                if a == "-f" and i + 1 < len(args):
                    archive = args[i + 1]; i += 2; continue
                if re.fullmatch(r"-?[A-Za-z]+", a) and (a.startswith("-") or i == 0):
                    letters = a.lstrip("-")
                    creating = creating or "c" in letters
                    extracting = extracting or "x" in letters
                    if letters.endswith("f") and i + 1 < len(args):
                        archive = args[i + 1]; i += 2; continue
                i += 1
            if creating and archive and archive != "-":
                add(archive, "Creating an archive at")
            if extracting:
                target = resolve(expand(outdir), state["cwd"]) if outdir else state["cwd"]
                if target == LAB:
                    found.append((LAB + os.sep + "(unpacked files)", "Unpacking an archive into the root, creating"))
            return

        if name == "unzip":
            outdir = None
            for i, a in enumerate(args):
                if a == "-d" and i + 1 < len(args):
                    outdir = args[i + 1]
            target = resolve(expand(outdir), state["cwd"]) if outdir else state["cwd"]
            if target == LAB:
                found.append((LAB + os.sep + "(unpacked files)", "Unpacking an archive into the root, creating"))
            return

        if name in MAKE_EVERY_ARG or name in MAKE_LAST_ARG:
            opts = OPTS_WITH_VALUE.get(name, set())
            operands, skip = [], False
            for a in args:
                if skip:
                    skip = False
                    continue
                if a == "--":
                    continue
                if a.startswith("-") and len(a) > 1:
                    if a in opts:
                        skip = True
                    continue
                operands.append(a)
            if name in MAKE_EVERY_ARG:
                for o in operands:
                    add(o, "This would create")
            elif len(operands) >= 2:
                add(operands[-1], "This would copy or move something into")

    current, i = [], 0
    while i < len(tokens):
        tok = tokens[i]
        if is_punct(tok):
            if ">" in tok:
                nxt = tokens[i + 1] if i + 1 < len(tokens) else ""
                # >&2 and 2>&1 duplicate a file descriptor; they write no file
                if tok.endswith("&") or nxt.startswith("&") or nxt.isdigit() or nxt == "-":
                    i += 2
                    continue
                if nxt and not is_punct(nxt):
                    add(nxt, "Writing output to")
                    i += 2
                    continue
                i += 1
                continue
            if "<" in tok:  # input redirection reads a file
                i += 2
                continue
            run_simple(current)
            current = []
            i += 1
            continue
        # a file-descriptor number sitting right before a redirect is not a path
        if tok.isdigit() and i + 1 < len(tokens) and is_punct(tokens[i + 1]) and (
                ">" in tokens[i + 1] or "<" in tokens[i + 1]):
            i += 1
            continue
        current.append(tok)
        i += 1
    run_simple(current)
    return found


def main():
    raw = sys.stdin.read()
    try:
        payload = json.loads(raw or "{}")
    except ValueError:
        allow_with_note("could not read the tool call")
    tool = payload.get("tool_name", "")
    tool_input = payload.get("tool_input") or {}
    cwd = payload.get("cwd") or LAB

    if tool in ("Write", "Edit", "MultiEdit", "NotebookEdit"):
        path = tool_input.get("file_path") or tool_input.get("notebook_path") or ""
        entry = root_entry(resolve(path, cwd))
        if entry and entry not in ALLOWED:
            deny(entry, "This would write")
        sys.exit(0)

    if tool == "Bash":
        command = tool_input.get("command", "")
        try:
            targets = bash_targets(command, cwd)
        except ValueError as exc:  # unbalanced quotes and the like
            allow_with_note("could not read the command (" + str(exc) + ")")
        for path, how in targets:
            entry = root_entry(path)
            if entry and entry not in ALLOWED:
                deny(entry, how)
    sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as exc:  # never let a bug in the guard block the session
        allow_with_note("hit an internal error (" + exc.__class__.__name__ + ")")
