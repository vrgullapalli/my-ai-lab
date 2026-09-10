#!/usr/bin/env python3
"""waiting: everything that is waiting on Venkat's word, in one place, measured.

  waiting.py           plain text, oldest first
  waiting.py --html    a page, for a private preview

Built 2026-09-10 at Venkat's word ("build me something else ... something for you to use").
The job it does for him: he should never have to hold state between messages, and the
things that stall the lab stall because nobody put them in front of him in one list.
DONE.md section 2: the brief is an ignition system. This is the part of it that says
"these are yours".

Read-only. Standard library. Reads:
  - follow-ups in evidence/receipts/ whose owner is Venkat (via facts.py loops)
  - the unchecked lines of .claude/agents/alfred/TODAY.md
  - the "Needs Venkat" section of work-os/upskill-advisor/records/open-items.md
  - public asset briefs whose ruling is PENDING or HOLD (assets/briefs/)
  - the ALERT lines of the morning facts sheet that only he can clear
"""
import datetime as dt
import glob
import html
import os
import re
import subprocess
import sys

LAB = "/Users/venkatgullapalli/Documents/my-ai-lab"
FACTS = os.path.join(LAB, ".claude", "agents", "alfred", "sensors", "facts.py")
TODAY = os.path.join(LAB, ".claude", "agents", "alfred", "TODAY.md")
OPEN_ITEMS = os.path.join(LAB, "work-os", "upskill-advisor", "records", "open-items.md")
BRIEFS = os.path.join(LAB, "work-os", "brand-os", "engagement-os", "assets", "briefs")
ONLY_HE_CAN = ("Full Disk Access", "unpushed", "no remote", "Venkat")


def read(path):
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return ""


def run(*args):
    try:
        return subprocess.run([sys.executable, FACTS] + list(args), capture_output=True, text=True, timeout=90).stdout
    except Exception:
        return ""


def follow_ups():
    rows = []
    for line in run("loops").split("\n"):
        m = re.match(r"\s+(F-\d{8}-\d{4}-\d+) \((\d+) days, from ([^)]+)\): (.*)", line)
        if not m:
            continue
        fid, age, src, text = m.groups()
        if "owner: Venkat" not in text:
            continue
        what, _, rest = text.partition(" — owner:")
        step = ""
        sm = re.search(r"first step: (.*)$", rest)
        if sm:
            step = sm.group(1).strip()
        rows.append({"kind": "follow-up", "id": fid, "age": int(age), "what": what.strip(),
                     "step": step, "source": "evidence/receipts/" + src})
    return rows


def today_items():
    rows = []
    for line in read(TODAY).split("\n"):
        m = re.match(r"- \[ \] \*\*(.+?)\*\*\s*(.*)", line)
        if m:
            rows.append({"kind": "to-do", "id": "", "age": 0, "what": m.group(1).strip(),
                         "step": m.group(2).strip()[:200], "source": ".claude/agents/alfred/TODAY.md"})
    return rows


def telegraph_items():
    text = read(OPEN_ITEMS)
    m = re.search(r"^## Needs Venkat\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    if not m:
        return []
    rows = []
    for item in re.split(r"\n(?=- )", m.group(1).strip()):
        item = " ".join(item.split())
        if item.startswith("- "):
            head = re.sub(r"\*\*", "", item[2:]).split(" — ")[0]
            rows.append({"kind": "telegraph", "id": "", "age": 0, "what": head[:160], "step": re.sub(r"\*\*", "", item[2:])[:300],
                         "source": "work-os/upskill-advisor/records/open-items.md"})
    return rows


def briefs():
    rows = []
    for path in sorted(glob.glob(os.path.join(BRIEFS, "*.md"))):
        text = read(path)
        rm = re.search(r"^ruling:\s*(\S+)", text, re.M)
        if not rm or rm.group(1) not in ("PENDING", "HOLD"):
            continue
        title = re.search(r"^# .*?—\s*(.+)$", text, re.M)
        date = re.search(r"^date:\s*(\S+)", text, re.M)
        age = (dt.date.today() - dt.date.fromisoformat(date.group(1))).days if date else 0
        rows.append({"kind": "brief", "id": rm.group(1), "age": age,
                     "what": (title.group(1) if title else os.path.basename(path)) + f" — ruling is {rm.group(1)}",
                     "step": "say APPROVED, REVISE, HOLD, or REJECTED", "source": os.path.relpath(path, LAB)})
    return rows


def alerts():
    rows = []
    if os.environ.get("WAITING_FROM_FACTS"):
        return rows          # facts.py is the caller; it already holds the alert lines. No loop.
    for line in run("open").split("\n"):
        if line.startswith("ALERT ") and any(k in line for k in ONLY_HE_CAN):
            rows.append({"kind": "alert", "id": "", "age": 0, "what": line[6:].strip()[:200], "step": "",
                         "source": "facts.py open"})
    return rows


def collect():
    rows = follow_ups() + briefs() + telegraph_items() + today_items() + alerts()
    rows.sort(key=lambda r: (-r["age"], r["kind"]))
    return rows


def as_text(rows):
    out = [f"WAITING ON VENKAT — {dt.datetime.now().strftime('%A %Y-%m-%d %H:%M')} — {len(rows)} items, oldest first"]
    for r in rows:
        age = f"{r['age']}d" if r["age"] else "new"
        out.append(f"- [{r['kind']}] ({age}) {r['what']}" + (f"\n    first step: {r['step']}" if r["step"] else "")
                   + f"\n    from: {r['source']}")
    return "\n".join(out)


def as_html(rows):
    e = html.escape
    kinds = {"follow-up": "follow-up", "brief": "ruling", "telegraph": "Telegraph", "to-do": "to-do", "alert": "alert"}
    items = "".join(
        f"<li><span class='k'>{kinds.get(r['kind'], r['kind'])}</span><span class='age'>{(str(r['age']) + ' days') if r['age'] else 'today'}</span>"
        f"<p class='w'>{e(r['what'])}</p>" + (f"<p class='s'>{e(r['step'])}</p>" if r["step"] else "")
        + f"<p class='src'>{e(r['source'])}</p></li>" for r in rows)
    return f"""<title>Waiting on Venkat</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&family=Newsreader:opsz,wght@6..72,500&family=JetBrains+Mono:wght@500&display=swap">
<style>
:root{{--bg:#FAF9F7;--surface:#FFFFFF;--surface2:#F3F1EE;--border:#D8D5D0;--text:#1A1918;--text2:#5C5B58;--text3:#8A8985;--accent:#A8663F}}
@media (prefers-color-scheme: dark){{:root:not([data-theme="light"]){{--bg:#0C0C0E;--surface:#131316;--surface2:#1A1A1E;--border:#2A2A2F;--text:#E8E6E3;--text2:#9B9A97;--text3:#5C5B58;--accent:#C17F59}}}}
:root[data-theme="dark"]{{--bg:#0C0C0E;--surface:#131316;--surface2:#1A1A1E;--border:#2A2A2F;--text:#E8E6E3;--text2:#9B9A97;--text3:#5C5B58;--accent:#C17F59}}
body{{background:var(--bg);color:var(--text);font-family:"DM Sans",system-ui,sans-serif;font-size:15px;line-height:1.55;margin:0}}
main{{max-width:760px;margin:0 auto;padding:40px 20px 80px}}
h1{{font-family:"Newsreader",Georgia,serif;font-weight:500;font-size:32px;letter-spacing:-.03em;margin:0 0 6px}}
.lead{{color:var(--text2);margin:0 0 24px}}
.label{{font-family:"JetBrains Mono",monospace;font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--text3)}}
ul{{list-style:none;padding:0;margin:0;display:grid;gap:10px}}
li{{background:var(--surface);border:1px solid var(--border);padding:14px 16px;display:grid;grid-template-columns:auto auto 1fr;gap:4px 12px;align-items:baseline}}
li .k{{font-family:"JetBrains Mono",monospace;font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--accent)}}
li .age{{font-family:"JetBrains Mono",monospace;font-size:11px;color:var(--text3)}}
li .w{{grid-column:1/-1;margin:0;font-weight:500}}
li .s{{grid-column:1/-1;margin:0;color:var(--text2)}}
li .s::before{{content:"first step: ";font-family:"JetBrains Mono",monospace;font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--text3)}}
li .src{{grid-column:1/-1;margin:0;font-family:"JetBrains Mono",monospace;font-size:11px;color:var(--text3)}}
.foot{{color:var(--text3);font-size:13px;margin-top:32px;border-top:1px solid var(--border);padding-top:12px}}
</style>
<main>
<span class="label">Alfred · {e(dt.datetime.now().strftime('%A %Y-%m-%d %H:%M'))}</span>
<h1>Waiting on Venkat</h1>
<p class="lead">{len(rows)} things only you can move, oldest first. Each one has its first step ready. Say the word and it moves.</p>
<ul>{items}</ul>
<p class="foot">Every line is read from a file or a script, none from memory: the receipts' follow-ups with owner Venkat, the open to-do lines, Telegraph's "Needs Venkat" section, briefs whose ruling is PENDING or HOLD, and the morning ALERT lines only you can clear. Rebuild: <code>python3 .claude/agents/alfred/sensors/waiting.py --html</code>.</p>
</main>
"""


if __name__ == "__main__":
    rows = collect()
    print(as_html(rows) if "--html" in sys.argv else as_text(rows))
