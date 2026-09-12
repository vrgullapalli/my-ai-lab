#!/usr/bin/env python3
"""session-sync: copy Claude Code and Codex sessions into the lab as readable transcripts.

  session-sync.py                 render every session that changed since its last render
  session-sync.py --hook          SessionEnd hook: render the one session that just ended
  session-sync.py --once <id>     render one session or thread by id
  session-sync.py --usage         rebuild evidence/sessions/USAGE.jsonl from the renders only
  session-sync.py --dry-run       say what would be rendered, write nothing

Re-homed 2026-09-10 at Venkat's word from chief-of-staff/tools/codex-session-sync.py
(plan approved 2026-08-20, Option A; the old copy sits in ~/Desktop/my-ai-lab-v2). It stopped
running when the lab moved, because the launchd job pointed at the old folder. Python 3.9,
standard library only. Never commits.

What a rendered file holds: Venkat's turns and the assistant's replies, in order, each under a
stable anchor that is the source's own message id (Codex `msg_…`, Claude record `uuid`), so a
citation survives refreshes. Tool calls as name-only markers. Thinking whenever the source
holds readable text (his ruling, 2026-08-20). New since 2026-09-10, so that "which skills do I
use" is a grep and not an afternoon: the skill name on every Skill call (`[skill: my-voice]`),
the agent type and short label on every Agent call, one line per subagent the session spawned
(type, label, turn counts — the subagent transcripts themselves are not rendered), and a
machine-readable usage line in every header. `--usage` rebuilds the ledger from those lines.

What it never holds: tool inputs (except the skill or agent name), tool results, system
reminders, IDE notices, anything matching the secret patterns (each hit is replaced with
"[secret-like text removed]" and the file is named in the log with its count; before
2026-09-10 a file with a hit was skipped whole). Anthropic keys (`sk-ant-…`) were added to
the patterns that day: the old `sk-` pattern stopped at the hyphen and never matched them.

Writes only under evidence/sessions/: claude/<session>.md, codex/<thread>.md, SYNC-LOG.md,
USAGE.jsonl.
"""
import argparse
import datetime
import glob
import hashlib
import json
import os
import re
import sys

LAB = os.environ.get("LAB_ROOT") or "/Users/venkatgullapalli/Documents/my-ai-lab"
DEST = os.environ.get("SESSIONS_DIR") or os.path.join(LAB, "evidence", "sessions")
CLAUDE_PROJECTS = os.environ.get("CLAUDE_PROJECTS") or os.path.expanduser("~/.claude/projects")
CODEX_ROOT = os.environ.get("CODEX_ROOT") or os.path.expanduser("~/.codex")

SECRET = re.compile(r"(sk-ant-[A-Za-z0-9_-]{20,}|sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|"
                    r"xox[baprs]-[A-Za-z0-9-]{10,}|Bearer\s+[A-Za-z0-9._-]{20,}|AKIA[0-9A-Z]{16}|"
                    r"-----BEGIN [A-Z ]*PRIVATE KEY)")
MASK = "[secret-like text removed]"
STRIP_BLOCKS = re.compile(r"<(system-reminder|ide_opened_file|ide_selection)>.*?</\1>", re.S)
SKIP_USER_PREFIX = ("<environment_context>", "<permissions", "# AGENTS.md", "<INSTRUCTIONS>",
                    "<user_instructions>", "<turn_aborted>", "<system>", "<local-command-stdout>",
                    "<local-command-caveat>", "Base directory for this skill:", "<task-notification",
                    "[Request interrupted")
USAGE_LINE = re.compile(r"^- Usage: (\{.*\})$", re.M)


def now():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")


def iso(ts):
    return datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")


def home(p):
    return p.replace(os.path.expanduser("~"), "~")


def quote(text):
    return "\n".join("> " + l for l in text.splitlines())


def marker(kind, name=""):
    """One-line marker. Name or label only, never the input (his ruling, 2026-08-20)."""
    name = str(name).strip().replace("\n", " ")[:100]
    return f"\n*[{kind}: {name}]*\n" if name else f"\n*[{kind}]*\n"


def turn(who, mid, body, quoted=False):
    text = quote(body) if quoted else body
    sep = "\n---\n" if quoted else "\n"
    return f"{sep}\n<a id=\"{mid}\"></a>\n**{who}** · `{mid}`\n\n{text}\n"


def read_header_mtime(path):
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8", errors="replace") as f:
        for _ in range(40):
            m = re.match(r"- Source mtime: (\S+ \S+)", f.readline())
            if m:
                return m.group(1)
    return None


# ---------------------------------------------------------------- Codex reader
def render_codex(src, archived=False, locks_dir=None):
    seen, lines, meta, last_ts = set(), [], None, None
    n_user = n_asst = n_tool = n_reason = 0
    tools = []
    for raw in open(src, encoding="utf-8", errors="replace"):
        try:
            o = json.loads(raw)
        except json.JSONDecodeError:
            continue
        t, p = o.get("type"), o.get("payload") or {}
        if t == "session_meta" and meta is None:
            meta = p
        last_ts = o.get("timestamp") or last_ts
        if t != "response_item":
            continue
        pt = p.get("type")
        if pt == "message":
            role = p.get("role")
            if role not in ("user", "assistant"):
                continue
            text = "\n".join(c.get("text", "") for c in p.get("content", [])
                             if c.get("type") in ("input_text", "output_text")).strip()
            if not text or text.startswith(SKIP_USER_PREFIX):
                continue
            if (role, text) in seen:          # compaction replays earlier turns
                continue
            seen.add((role, text))
            mid = p.get("id") or ("h-" + hashlib.sha1((role + text).encode()).hexdigest()[:12])
            if role == "user":
                n_user += 1
                lines.append(turn("Venkat", mid, text, quoted=True))
            else:
                n_asst += 1
                lines.append(turn("Codex", mid, text))
        elif pt == "reasoning":
            txt = "\n".join(s.get("text", "") for s in (p.get("summary") or []) if isinstance(s, dict)).strip()
            if txt and ("reasoning", txt) not in seen:
                seen.add(("reasoning", txt))
                n_reason += 1
                mid = p.get("id") or ("h-" + hashlib.sha1(txt.encode()).hexdigest()[:12])
                lines.append(turn("Codex, thinking", mid, txt))
        elif pt in ("custom_tool_call", "function_call"):
            n_tool += 1
            tools.append(p.get("name", ""))
            lines.append(marker("tool call", p.get("name", "")))
        elif pt == "web_search_call":
            n_tool += 1
            lines.append(marker("web search"))
    thread = os.path.basename(src)[-42:-6]
    is_open = bool(locks_dir and os.path.exists(os.path.join(locks_dir, thread + ".lock")))
    st = os.stat(src)
    started = (meta or {}).get("timestamp", "Unknown")
    usage = {"id": thread, "source": "codex", "started": started, "last": last_ts,
             "cwd": (meta or {}).get("cwd"), "venkat_turns": n_user, "replies": n_asst,
             "tool_calls": n_tool, "skills": [], "agents": [], "commands": [], "subagents": 0}
    head = f"""# Codex session — {thread}

- Thread: `codex://threads/{thread}`
- Source of record: `{home(src)}` (outside the repo; this file is rendered from it)
- Source mtime: {iso(st.st_mtime)} · size {st.st_size:,} bytes
- Started: {started} · last record: {last_ts} · rendered: {now()} · archived: {'yes' if archived else 'no'} · open at render: {'yes (lock held)' if is_open else 'no'}
- Codex cwd: `{(meta or {}).get('cwd', 'Unknown')}` · model: `{(meta or {}).get('model', 'Unknown')}`
- **What this is:** Venkat's messages and Codex's replies, in order, de-duplicated across compactions, each under an anchor that is Codex's own message id (cite as `<file>#<id>`). Tool calls and web searches as name-only markers; **tool inputs and outputs omitted** (his ruling 2026-08-20). **Reasoning kept whenever readable:** {n_reason} readable reasoning item(s) found{' — Codex stores reasoning encrypted with empty summaries' if n_reason == 0 else ''}.
- Counts: {n_user} Venkat turns · {n_asst} Codex replies · {n_tool} tool calls/searches
- Role boundary: Codex is a read-only advisor (D-128). Nothing in this file is an approval.
- Usage: {json.dumps(usage, ensure_ascii=False)}
"""
    return head + "".join(lines)


# ----------------------------------------------------------- Claude Code reader
def subagent_summary(sid_dir):
    """One line per subagent the session spawned: type, short label, counts. Never their text."""
    rows = []
    for meta_path in sorted(glob.glob(os.path.join(sid_dir, "subagents", "*.meta.json"))):
        try:
            meta = json.load(open(meta_path, encoding="utf-8"))
        except (OSError, ValueError):
            meta = {}
        jl = meta_path[:-len(".meta.json")] + ".jsonl"
        n_turns = n_tools = 0
        try:
            for raw in open(jl, encoding="utf-8", errors="replace"):
                if '"type":"assistant"' in raw:
                    n_turns += 1
                    n_tools += raw.count('"type":"tool_use"')
        except OSError:
            pass
        rows.append({"type": meta.get("agentType", "?"), "label": str(meta.get("description", ""))[:80],
                     "replies": n_turns, "tool_calls": n_tools})
    return rows


def render_claude(src, recent_minutes=30):
    lines, title, first_ts, last_ts, cwd, version = [], None, None, None, None, None
    n_user = n_asst = n_tool = n_think = n_cmd = 0
    skills, agents, commands = [], [], []
    for raw in open(src, encoding="utf-8", errors="replace"):
        try:
            o = json.loads(raw)
        except json.JSONDecodeError:
            continue
        t = o.get("type")
        uid = o.get("uuid") or ""
        if t == "ai-title" and not title:
            title = o.get("title") or o.get("aiTitle") or title
        ts = o.get("timestamp")
        if ts:
            first_ts = first_ts or ts
            last_ts = ts
        cwd = cwd or o.get("cwd")
        version = version or o.get("version")
        if t not in ("user", "assistant"):
            continue
        m = o.get("message") or {}
        content = m.get("content")
        if t == "user":
            if isinstance(content, str):
                text = content
            else:
                parts = []
                for b in content or []:
                    if b.get("type") == "text":
                        parts.append(b.get("text", ""))
                    elif b.get("type") == "tool_result":
                        n_tool += 1          # counted, never rendered
                text = "\n".join(parts)
            text = STRIP_BLOCKS.sub("", text).strip()
            cm = re.search(r"<command-name>(.*?)</command-name>", text)
            if cm:
                n_cmd += 1
                commands.append(cm.group(1).strip())
                lines.append(marker("command", cm.group(1)))
                continue
            if not text or text.startswith(SKIP_USER_PREFIX):
                continue
            n_user += 1
            mid = uid or ("h-" + hashlib.sha1(text.encode()).hexdigest()[:12])
            lines.append(turn("Venkat", mid, text, quoted=True))
        else:
            k = 0
            for b in content if isinstance(content, list) else []:
                bt = b.get("type")
                if bt == "text" and b.get("text", "").strip():
                    n_asst += 1
                    k += 1
                    mid = (uid or "h-" + hashlib.sha1(b["text"].encode()).hexdigest()[:12]) + ("" if k == 1 else f"-{k}")
                    lines.append(turn("Claude", mid, b["text"].strip()))
                elif bt == "thinking" and b.get("thinking", "").strip():
                    n_think += 1
                    lines.append(turn("Claude, thinking", (uid or "h") + "-t", b["thinking"].strip()))
                elif bt == "tool_use":
                    n_tool += 1
                    name = b.get("name", "")
                    inp = b.get("input") or {}
                    if name == "Skill":
                        skill = str(inp.get("skill", "")).strip()
                        skills.append(skill)
                        lines.append(marker("skill", skill))
                    elif name == "Agent":
                        kind = str(inp.get("subagent_type") or "general-purpose").strip()
                        label = str(inp.get("description", "")).strip()
                        agents.append(kind)
                        lines.append(marker("agent", f"{kind} — {label}" if label else kind))
                    else:
                        lines.append(marker("tool call", name))
    sid = os.path.basename(src)[:-6]
    subs = subagent_summary(src[:-6])
    st = os.stat(src)
    age_min = (datetime.datetime.now().timestamp() - st.st_mtime) / 60
    usage = {"id": sid, "source": "claude", "started": first_ts, "last": last_ts, "cwd": cwd,
             "venkat_turns": n_user, "replies": n_asst, "tool_calls": n_tool,
             "skills": sorted(set(skills)), "agents": sorted(set(agents)),
             "commands": sorted(set(commands)), "subagents": len(subs)}
    head = f"""# Claude Code session — {title or sid}

- Session: `{sid}`
- Source of record: `{home(src)}` (outside the repo; this file is rendered from it)
- Source mtime: {iso(st.st_mtime)} · size {st.st_size:,} bytes
- Started: {first_ts} · last record: {last_ts} · rendered: {now()} · open at render: {'possibly (modified in the last ' + str(recent_minutes) + ' min)' if age_min < recent_minutes else 'no'}
- cwd: `{cwd}` · Claude Code {version}
- **What this is:** Venkat's messages and Claude's replies, in order, each under an anchor that is the record's own uuid (cite as `<file>#<uuid>`). Slash commands and tool calls as name-only markers, with the skill name on Skill calls and the agent type and label on Agent calls; **tool inputs, tool results, system reminders and IDE notices omitted** (his ruling 2026-08-20). **Thinking kept whenever readable:** {n_think} readable block(s) found{' — Claude Code stores thinking as a signature without text' if n_think == 0 else ''}.
- Counts: {n_user} Venkat turns · {n_asst} Claude replies · {n_cmd} commands · {n_tool} tool calls/results · skills used: {', '.join(usage['skills']) or 'none'} · agents used: {', '.join(usage['agents']) or 'none'}
- Subagents this session spawned: {len(subs)}{' (listed at the end; their transcripts are not rendered — Venkat, 2026-09-10)' if subs else ''}
- Usage: {json.dumps(usage, ensure_ascii=False)}
"""
    tail = ""
    if subs:
        tail = "\n---\n\n## Subagents spawned by this session\n\n| Type | Label | Replies | Tool calls |\n|---|---|---:|---:|\n"
        tail += "".join(f"| {r['type']} | {r['label'].replace('|', '/')} | {r['replies']} | {r['tool_calls']} |\n" for r in subs)
    return head + "".join(lines) + tail


# ------------------------------------------------------------------- driver
def sync_one(src, dest_path, render_fn, force, log, **kw):
    st = os.stat(src)
    prev = read_header_mtime(dest_path)
    if prev == iso(st.st_mtime) and not force:
        return "unchanged"
    body = render_fn(src, **kw)
    # Blank each secret-like string and keep the transcript (Venkat, 2026-09-10: "just save it").
    # Until then a single hit skipped the whole file, and a 185-message session was lost to four
    # harmless "BEGIN PRIVATE KEY" labels. The count goes in the log so a real hit stays visible.
    body, hits = SECRET.subn(MASK, body)
    if hits:
        log.append(f"MASKED (secret-like string, {hits} hit/s blanked): {os.path.basename(src)}")
    status = "refreshed" if os.path.exists(dest_path) else "rendered"
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(body)
    return status


def claude_sources():
    """Every top-level session file in every Claude Code project folder. Subagent files sit
    one level down and are summarized by their parent, never listed here."""
    out = []
    for d in sorted(glob.glob(os.path.join(CLAUDE_PROJECTS, "*"))):
        if os.path.isdir(d):
            out.extend(sorted(glob.glob(os.path.join(d, "*.jsonl"))))
    return out


def codex_sources():
    live = sorted(glob.glob(os.path.join(CODEX_ROOT, "sessions", "**", "*.jsonl"), recursive=True))
    arch = sorted(glob.glob(os.path.join(CODEX_ROOT, "archived_sessions", "*.jsonl")))
    return [(s, False) for s in live] + [(s, True) for s in arch]


OLD_COUNTS = re.compile(r"- Counts: (\d+) Venkat turns · (\d+) (?:Claude|Codex) replies · (?:(\d+) commands · )?(\d+) tool calls")
OLD_STARTED = re.compile(r"- Started: (\S+)")
OLD_COMMAND = re.compile(r"^\*\[command: /?([^\]]+)\]\*$", re.M)
BUILTIN_COMMANDS = {"model", "clear", "mcp", "compact", "help", "status", "config", "cost", "init", "login",
                    "logout", "doctor", "memory", "permissions", "resume", "review", "terminal-setup", "vim",
                    "exit", "quit", "bug", "release-notes", "add-dir", "agents", "hooks", "ide", "install",
                    "upgrade", "context", "export", "rewind", "usage", "plugin", "skills", "tasks", "artifacts"}


def usage_from_old_render(path, text):
    """Rows for the 227 renders made before 2026-09-10, which carry no Usage line. Their tool
    markers dropped the skill name, so skills here come only from slash commands (which the old
    render kept by name) and stay marked as partial."""
    m = OLD_COUNTS.search(text[:6000])
    if not m:
        return None
    started = OLD_STARTED.search(text[:6000])
    commands = sorted(set(c.strip() for c in OLD_COMMAND.findall(text)))
    return {"id": os.path.basename(path)[:-3], "source": "claude" if "/claude/" in path else "codex",
            "started": started.group(1) if started else None, "last": None, "cwd": None,
            "venkat_turns": int(m.group(1)), "replies": int(m.group(2)), "tool_calls": int(m.group(4)),
            "skills": [c for c in commands if c and c[0].isalpha() and c.split(":")[-1] not in BUILTIN_COMMANDS],
            "agents": [], "commands": commands,
            "subagents": 0, "partial": "rendered before 2026-09-10; skill names known only from slash commands"}


def rebuild_usage():
    """USAGE.jsonl, one row per rendered session, from the Usage line each render carries.
    Rebuilt from the renders, not the raw files, so it survives the raw store expiring."""
    rows = []
    for path in sorted(glob.glob(os.path.join(DEST, "claude", "*.md")) + glob.glob(os.path.join(DEST, "codex", "*.md"))):
        with open(path, encoding="utf-8", errors="replace") as f:
            text = f.read()
        m = USAGE_LINE.search(text[:8000])
        row = None
        if m:
            try:
                row = json.loads(m.group(1))
            except ValueError:
                row = None
        if row is None:
            row = usage_from_old_render(path, text)
        if row:
            row["render"] = os.path.relpath(path, LAB)
            rows.append(row)
    rows.sort(key=lambda r: (r.get("started") or "", r.get("id") or ""))
    os.makedirs(DEST, exist_ok=True)
    with open(os.path.join(DEST, "USAGE.jsonl"), "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    return len(rows)


def append_log(source, counts, log):
    line = (f"| {now()} | {source} | {counts['rendered']} | {counts['refreshed']} | "
            f"{counts['unchanged']} | {counts['skipped']} | {'; '.join(log) or '—'} |\n")
    logp = os.path.join(DEST, "SYNC-LOG.md")
    os.makedirs(DEST, exist_ok=True)
    if not os.path.exists(logp):
        with open(logp, "w", encoding="utf-8") as f:
            f.write("# Session sync log\n\nOne line per run of `.claude/agents/alfred/sensors/session-sync.py`. "
                    "Never commits; Venkat commits with purpose.\n\n"
                    "| Run (local time) | Source | Rendered | Refreshed | Unchanged | Skipped | Notes |\n"
                    "|---|---|---:|---:|---:|---:|---|\n")
    with open(logp, "a", encoding="utf-8") as f:
        f.write(line)
    return line.strip()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--source", choices=["codex", "claude", "all"], default="all")
    ap.add_argument("--once", help="one Codex thread id or Claude session id (substring match)")
    ap.add_argument("--hook", action="store_true", help="SessionEnd hook: read the payload on stdin, render that session")
    ap.add_argument("--usage", action="store_true", help="only rebuild USAGE.jsonl from the renders")
    ap.add_argument("--force", action="store_true", help="re-render even if the source is unchanged")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--tag", default="", help="who ran it, for the log's Source column (launchd, manual)")
    a = ap.parse_args()

    if a.usage:
        print(f"USAGE.jsonl: {rebuild_usage()} rows")
        return 0

    counts = {"rendered": 0, "refreshed": 0, "unchanged": 0, "skipped": 0}
    log = []
    source = a.tag or a.source

    def run(src, dest_path, fn, **kw):
        if a.dry_run:
            print("would sync", home(src), "->", os.path.relpath(dest_path, LAB))
            return
        r = sync_one(src, dest_path, fn, a.force, log, **kw)
        counts[r] += 1

    if a.hook:
        try:
            payload = json.loads(sys.stdin.read() or "{}")
        except ValueError:
            payload = {}
        src = payload.get("transcript_path") or ""
        if not (src and os.path.isfile(src) and src.endswith(".jsonl")):
            return 0   # a hook must never break a session end
        source = "hook"
        run(src, os.path.join(DEST, "claude", os.path.basename(src)[:-6] + ".md"), render_claude, recent_minutes=0)
    else:
        if a.source in ("codex", "all"):
            locks = os.path.join(CODEX_ROOT, "thread-writer-locks")
            for src, archived in codex_sources():
                if a.once and a.once not in src:
                    continue
                stem = os.path.basename(src)[:-6]
                run(src, os.path.join(DEST, "codex", stem + ".md"), render_codex, archived=archived, locks_dir=locks)
        if a.source in ("claude", "all"):
            for src in claude_sources():
                if a.once and a.once not in src:
                    continue
                run(src, os.path.join(DEST, "claude", os.path.basename(src)[:-6] + ".md"), render_claude)

    if not a.dry_run:
        if counts["rendered"] or counts["refreshed"]:
            rebuild_usage()
        print(append_log(source, counts, log))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:  # never break a hook or a launchd run silently: log and exit clean
        try:
            with open(os.path.join(DEST, "SYNC-LOG.md"), "a", encoding="utf-8") as f:
                f.write(f"| {now()} | error | 0 | 0 | 0 | 0 | {type(exc).__name__}: {str(exc)[:160]} |\n")
        except OSError:
            pass
        print(f"session-sync error: {exc}", file=sys.stderr)
        sys.exit(0 if "--hook" in sys.argv else 1)
