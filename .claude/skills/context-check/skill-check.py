#!/usr/bin/env python3
"""skill-check: proves every skill and agent file still points at things that exist.

  python3 .claude/skills/context-check/skill-check.py             full report, exit 1 on any finding
  python3 .claude/skills/context-check/skill-check.py --summary   one line, for Alfred's facts sheet

READ-ONLY. Writes nothing.

Why, 2026-09-10: the skills audit that morning found seven stale pointers by hand, and the
general dead-pointers script caught one of them. That script accepts a path as found when any
file of that name exists somewhere in the lab, and it only reads text inside backticks. A
skill's pointers deserve a stricter test, because a skill that points at a missing file fails
silently the moment it is used. So this one:

  1. Flags a skill whose body is empty (a title and nothing under it). Six skills were like
     that on 2026-09-10 and nobody knew until one was called and returned nothing.
  2. Flags a skill with no "Base directory:" line, or one whose folder does not exist.
  3. Resolves every path the file names — in backticks, in links, in plain prose, and in the
     frontmatter description — against three places only: the file's own folder, the declared
     base directory, and the lab root (each plus one folder level below it, so `session/`
     inside a seedbank skill still counts). A bare file name with no folder is looked for a
     few levels under those same three places. Nothing is looked for lab-wide by name.
     A placeholder inside a path (`work/plans/{slug}/`) is cut off and the part before it
     must exist.
  4. Flags every skill the file names by name (`/name`, "the name skill", `name` skill) that
     is not on disk under .claude/skills, ~/.claude/skills, an installed plugin, or Claude
     Code's own built-in list below.

Files checked: every .claude/skills/*/SKILL.md and every .md directly inside .claude/agents/
and its agent folders (one level). Reference files are not walked.

Accepted exceptions live in skill-check-accepted.txt beside this script, one per line:
    <file relative to lab> :: <token> | <reason>
    <file relative to lab> :: * | <reason>          (the whole file, for vendored or dated text)
Anything accepted is counted, not listed. The goal is a report with zero unreviewed findings.
"""
import glob
import os
import re
import sys

LAB = os.environ.get("LAB_ROOT") or "/Users/venkatgullapalli/Documents/my-ai-lab"
PLUGINS = os.environ.get("CLAUDE_PLUGINS") or os.path.expanduser("~/.claude/plugins/cache")
USER_SKILLS = os.environ.get("CLAUDE_USER_SKILLS") or os.path.expanduser("~/.claude/skills")
HERE = os.path.dirname(os.path.abspath(__file__))
ACCEPTED = os.environ.get("SKILL_CHECK_ACCEPTED") or os.path.join(HERE, "skill-check-accepted.txt")

# skills built into Claude Code itself; they have no folder on disk to find
BUILTIN_SKILLS = {"artifact-design", "artifact-diagramming", "artifact-capabilities", "dataviz",
                  "design", "update-config", "keybindings-help", "code-review", "simplify",
                  "fewer-permission-prompts", "loop", "schedule", "claude-api", "workflow-authoring",
                  "run", "init", "security-review"}

BASE_LINE = re.compile(r"^.*Base directory:.*$", re.M)
TICKED = re.compile(r"`([^`\n]{2,200})`")
MDLINK = re.compile(r"\]\(([^)\s]{2,200})\)")
PROSE_PATH = re.compile(r"(?<![\w/`.@:-])((?:~/|\./|/)?[\w.@~+-]+(?:/[\w.@~+*{}<>-]+)+/?|(?<![\w/.-])[\w-]+\.(?:md|py|sh|json|jsonl|yaml|yml|txt|html|pdf|csv|mjs|plist)\b)")
SKILL_NAMED = [re.compile(r"(?<![\w/.~])/([a-z][a-z0-9]*(?:-[a-z0-9]+)+)(?![\w/.-])"),       # /seed-capture
               re.compile(r"\bthe `?([a-z][a-z0-9]*(?:-[a-z0-9]+)+)`? skill\b"),           # the my-voice skill
               re.compile(r"`([a-z][a-z0-9]*(?:-[a-z0-9]+)+)` (?:skill|runs|is run|is called)\b"),
               re.compile(r"\b(?:run|runs|use|uses|invoke|invokes|calls|call|via|by|hands|hand|launch|launches|trigger|triggers|then) `([a-z][a-z0-9]*(?:-[a-z0-9]+)+)`")]
PLACEHOLDER_CUT = re.compile(r"[<{*].*$")
NOISE = re.compile(r"[()=|\\$\[\]]|YYYY|NNN|XXX|\.\.\.|…")
FOREIGN = ("/home/", "/tmp/", "/private/", "/var/", "/opt/", "/mnt/", "C:", "/usr/", "/bin/",
           "/Library/", "/System/", "/Applications/", "/etc/", "/dev/")
URLISH = re.compile(r"^(https?:|mailto:|codex:|file:)|^[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*\.(com|org|net|io|ai|co|dev|app|gov|edu|us|uk)(/|$)", re.I)
DATED = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ENVVAR = re.compile(r"^\$?[A-Z][A-Z0-9_]+(/|$)")
EXTS = (".md", ".py", ".sh", ".json", ".jsonl", ".yaml", ".yml", ".txt", ".html", ".pdf", ".csv", ".mjs", ".plist")
SKIP_WALK = {".git", "node_modules", "__pycache__", ".venv", "_archive"}


def read(path):
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return ""


def split_front(text):
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end > 0:
            return text[3:end], text[end + 4:]
    return "", text


def body_is_empty(body):
    real = [l for l in body.split("\n") if l.strip() and not l.strip().startswith("#")]
    return len(real) < 2


def declared_base(text):
    m = BASE_LINE.search(text[:4000])
    if not m:
        return None, None
    line = m.group(0)
    bases = []
    for tok in TICKED.findall(line):
        t = tok.strip().rstrip("/")
        if t == LAB or t.rstrip("/") == LAB.rstrip("/"):
            continue                      # "(lab root: `...`)" is context, not the base
        if "/" in t or t.startswith("~"):
            bases.append(t)
    if bases:
        return bases, line
    if re.search(r"the lab(?: root)?\b|lab root", line):
        return "lab", line
    return "", line


def clean(tok):
    tok = tok.strip().strip("\"'“”‘’")
    tok = re.sub(r"(#[\w-]+|:\d+(-\d+)?|#L\d+.*)$", "", tok)
    tok = tok.rstrip(".,;:!?)")
    tok = PLACEHOLDER_CUT.sub("", tok)          # work/plans/{slug}/  ->  work/plans/
    return tok


def looks_like_path(tok):
    if not tok or " " in tok or tok.startswith(("-", "#", "@", "--")):
        return False
    if NOISE.search(tok) or tok.count(":") > 1 or ENVVAR.match(tok):
        return False
    if URLISH.match(tok) or tok.startswith(FOREIGN) or DATED.match(tok):
        return False
    if tok.startswith("/") and not tok.startswith("/Users/"):
        return False           # a slash command or a web path, never a lab path
    segs = [s for s in tok.split("/") if s]
    if "/" in tok:
        if not segs:
            return False
        rooted = tok.startswith(("~", "/", ".")) or tok.endswith("/") or "." in segs[-1]
        if not rooted:
            return False       # dark/light/hybrid, read/write: words, not a path
        return True
    return tok.lower().endswith(EXTS)


def children(d):
    try:
        return [os.path.join(d, c) for c in os.listdir(d)
                if c not in SKIP_WALK and os.path.isdir(os.path.join(d, c))]
    except OSError:
        return []


def find_bare(name, roots, depth=4):
    """A bare file name: look a few levels under each root. Never lab-wide."""
    frontier = list(roots)
    for r in roots:
        frontier += children(r)          # `session/` inside a seedbank skill means seedbank/session/
    for _ in range(depth):
        nxt = []
        for d in frontier:
            if os.path.exists(os.path.join(d, name)):
                return True
            nxt.extend(children(d))
        frontier = nxt
    return False


def resolve(tok, roots):
    t = os.path.expanduser(tok)
    if os.path.isabs(t):
        return os.path.exists(t.rstrip("/") or "/")
    t = t[2:] if t.startswith("./") else t
    if "/" not in t.rstrip("/"):
        return find_bare(t.rstrip("/"), roots)
    return any(os.path.exists(os.path.join(r, t).rstrip("/")) for r in roots)


def known_skills():
    names = set(BUILTIN_SKILLS)
    for d in glob.glob(os.path.join(LAB, ".claude", "skills", "*", "SKILL.md")):
        names.add(os.path.basename(os.path.dirname(d)))
    for d in glob.glob(os.path.join(USER_SKILLS, "*", "SKILL.md")):
        names.add(os.path.basename(os.path.dirname(d)))
    for d in glob.glob(os.path.join(PLUGINS, "*", "*", "*", "skills", "*", "SKILL.md")):
        names.add(os.path.basename(os.path.dirname(d)))
    for d in glob.glob(os.path.join(PLUGINS, "*", "*", "*", "commands", "*.md")):
        names.add(os.path.basename(d)[:-3])
    return names


def retired_skills():
    """Skill names that were moved to the warehouse. A live file naming one is a finding even
    when the name appears in plain backticks with no verb around it."""
    names = set()
    for d in glob.glob(os.path.expanduser("~/Documents/_warehouse/skills-archived-*/*/")):
        names.add(os.path.basename(d.rstrip("/")).split("--")[0])
    return names - set(os.path.basename(os.path.dirname(p)) for p in glob.glob(os.path.join(LAB, ".claude", "skills", "*", "SKILL.md")))


def known_agents():
    names = set()
    for p in glob.glob(os.path.join(LAB, ".claude", "agents", "*")):
        n = os.path.basename(p)
        names.add(n[:-3] if n.endswith(".md") else n)
    return names


def load_accepted():
    exact, whole = set(), set()
    for line in read(ACCEPTED).split("\n"):
        line = line.split("|")[0].strip()
        if line and not line.startswith("#") and " :: " in line:
            f, tok = line.split(" :: ", 1)
            (whole if tok.strip() == "*" else exact).add((f.strip(), tok.strip()) if tok.strip() != "*" else f.strip())
    return exact, whole


def files_to_check():
    out = sorted(glob.glob(os.path.join(LAB, ".claude", "skills", "*", "SKILL.md")))
    out += sorted(glob.glob(os.path.join(LAB, ".claude", "agents", "*.md")))
    out += sorted(glob.glob(os.path.join(LAB, ".claude", "agents", "*", "*.md")))
    return out


def check_file(path, skills, agents, exact, whole, retired=frozenset()):
    rel = os.path.relpath(path, LAB)
    text = read(path)
    front, body = split_front(text)
    is_skill = rel.startswith(".claude/skills/")
    findings, accepted_hits = [], 0

    def add(kind, tok, line):
        nonlocal accepted_hits
        if rel in whole or (rel, tok) in exact:
            accepted_hits += 1
        else:
            findings.append((kind, tok, line))

    if is_skill and body_is_empty(body):
        add("EMPTY BODY", "(the file has a title and nothing under it)", 1)

    base, base_line = declared_base(text)
    roots = [os.path.dirname(path), LAB]
    if base is None:
        if is_skill:
            add("NO BASE DIRECTORY LINE", "(add one: > **Base directory:** `...`)", 1)
    elif base == "":
        add("BASE DIRECTORY NAMES NO FOLDER", base_line.strip()[:80], 1)
    elif base != "lab":
        for one in base:
            b = os.path.expanduser(one) if one.startswith(("~", "/")) else os.path.join(LAB, one)
            if os.path.isdir(b):
                roots.insert(1, b)
            else:
                add("BASE DIRECTORY MISSING", one, 1)

    seen = set()
    for lineno, line in enumerate(text.split("\n"), 1):
        toks = []
        for rx in (TICKED, MDLINK):
            for raw in rx.findall(line):
                # a command line in backticks (`python3 tools/x.py brief <file>`) names paths word by word
                toks += raw.split() if (" " in raw.strip() and not re.search(r"[<{]", raw)) else [raw]
        bare = re.sub(r"`[^`]*`", " ", line)          # prose only, so a ticked token is not read twice
        bare = re.sub(r"\]\([^)]*\)", " ", bare)
        toks += PROSE_PATH.findall(bare)
        for raw in toks:
            tok = clean(raw)
            if not tok or tok in seen or not looks_like_path(tok):
                continue
            seen.add(tok)
            if not resolve(tok, roots):
                add("DEAD PATH", tok, lineno)
        for name in TICKED.findall(line):
            if name in retired and "skill:" + name not in seen:
                seen.add("skill:" + name)
                add("RETIRED SKILL", name, lineno)
        for rx in SKILL_NAMED:
            for name in rx.findall(line):
                key = "skill:" + name
                if key in seen:
                    continue
                seen.add(key)
                if name not in skills and name not in agents:
                    add("MISSING SKILL", name, lineno)
    return rel, findings, accepted_hits


def main():
    skills, agents = known_skills(), known_agents()
    retired = retired_skills() - skills      # a name still served by a plugin is not retired
    exact, whole = load_accepted()
    files = files_to_check()
    total_findings, n_accepted, bad_files = 0, 0, 0
    kinds = {}
    report = []
    for path in files:
        rel, findings, acc = check_file(path, skills, agents, exact, whole, retired)
        n_accepted += acc
        if findings:
            bad_files += 1
            total_findings += len(findings)
            report.append("  " + rel)
            for kind, tok, line in findings:
                kinds[kind] = kinds.get(kind, 0) + 1
                report.append(f"      line {line:<5} {kind}: {tok}")
    n_skills = sum(1 for f in files if "/skills/" in f)
    n_agents = len(files) - n_skills
    parts = ", ".join(f"{v} {k.lower()}" for k, v in sorted(kinds.items()))
    summary = (f"skill check: {n_skills} skills and {n_agents} agent files checked; "
               f"{bad_files} files with {total_findings} problems" + (f" ({parts})" if parts else "")
               + f"; {n_accepted} accepted")
    if "--summary" in sys.argv:
        print(("ALERT " if total_findings else "") + summary)
    else:
        print("Skill check — every path and skill name a skill or agent file mentions, resolved strictly\n")
        print("\n".join(report) if report else "  (no findings)")
        print(f"\n{summary}")
        print(f"\nSKILL CHECK PROBLEMS: {total_findings}")
    return 1 if total_findings else 0


if __name__ == "__main__":
    sys.exit(main())
