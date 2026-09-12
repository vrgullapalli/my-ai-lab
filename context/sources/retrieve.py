#!/usr/bin/env python3
"""retrieve.py — Retrieval v0.1, the deterministic half (built 2026-09-12 at Venkat's word, AD-22).

Contract (his words): find the evidence that could materially change the judgment, preserve its
source and limits, and expose conflicts or gaps. The consumer reasons from the package.

What this script does, and only this:
  index        build the derived index: one record per file of every eligible source (status live or
               degraded in context/sources/REGISTER.md), plus one record per decision row, per career-model
               capability, and per verdict line. Rebuilt from the register at any time; nothing here is canonical.
  candidates   deterministic candidates for a query: exact matches (ids, names) and keyword overlap, with
               the record's source id, date, tier, ceiling, and marks. Also writes the compact one-line-per-record
               index the model reads for the semantic pass, and prints its size (records, bytes, ~tokens).
  fetch        after the model has picked candidates: pull the evidence deterministically. Refuses any path
               outside the eligible set. Carries source limits, record marks, pointer state, and current-versus-
               superseded marks. Flags what the model flagged as a conflict and adds its own conflict candidates.
               Sets a missing-evidence state from the script's floor, beside the model's. Appends one line to
               index/runs.jsonl (the write-back record).
  stats        the size of the full-index semantic pass, for the frozen tests to watch.

What the model does (in .claude/skills/retrieval/SKILL.md): read the compact index, pick candidates by meaning,
rank them, say why each matches, flag conflicts. It never fetches, never quotes a file this script did not return.

  python3 context/sources/retrieve.py index
  python3 context/sources/retrieve.py sources                                  # the 24 readable sources in one line each, for the model's first stage
  python3 context/sources/retrieve.py candidates "<query>" [--scope id,id] [--top N] [--scoped-out file]
  python3 context/sources/retrieve.py fetch --query "<query>" --picks picks.json [--out package.json]
  python3 context/sources/retrieve.py stats
"""
import datetime as dt
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import check  # noqa: E402

INDEX_DIR = os.path.join(HERE, "index")
INDEX = os.path.join(INDEX_DIR, "retrieval-index.jsonl")
COMPACT = os.path.join(INDEX_DIR, "compact.txt")
RUNS = os.path.join(INDEX_DIR, "runs.jsonl")

DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")
ID_RE = re.compile(r"\b(A-LIVE-\d+|A-[A-Z]{3,5}-[A-Z]?\d+|S\d{2}|CAP-\d{3}|D-\d{3}|AD-\d{2}|F-\d{8}-\d{4}-\d+|POV-\d{3}|AS-\d{3}|OI-\d{3})\b")
ROW_RE = re.compile(r"^\|\s*(\**)(\d{3}|D-\d{3}|AD-\d{2})\**\s*\|(.*)$")
PATH_RE = re.compile(r"(?:~|/Users)[^\s`'\")\]]+")
MARKS = {
    "claimed": r"\bclaimed\b|\[claimed\]|vendor claim|vendor opinion|seller's test",
    "observed": r"\bobserved\b",
    "inferred": r"\binferred\b",
    "unknown": r"\bunknown\b",
    "not-met": r"\bnot met\b",
    "page-not-opened": r"\b403\b|would not open|could not open|did not open",
    "vendor-owned-outlet": r"owned by eversana|eversana-owned|eversana owns",
    "his-word": r"locked by venkat|his word|his ruling|venkat:",
    "proposed": r"\bproposed\b",
    "correction": r"correction to \d{3}|corrected by \d{3}|supersede",
}
STOP = set("""the a an and or of to in on for with from by at as is are was were be been this that these those it its into
about what which who whom how when where why does do did has have had not no yes than then there their they them we our you your
his her he she will would should could can may might must one two three all any some each other more most such only also
just over under after before between through during without within being same own so if but per via""".split())


def rel(lab, p):
    return os.path.relpath(p, lab.root)


def tokens(text):
    return {t for t in re.findall(r"[a-z][a-z0-9\-']{3,}", text.lower()) if t not in STOP}


def names_in(query):
    """Exact terms: ids, all-caps words, and capitalized words that are not sentence starts."""
    terms = set(ID_RE.findall(query))
    words = re.findall(r"[A-Za-z][A-Za-z0-9\-']+", query)
    for i, w in enumerate(words):
        if len(w) < 4:
            continue
        if w.lower() in ("venkat", "alfred", "does", "what", "which", "lundbeck") and not w.isupper():
            pass  # names on nearly every file are not exact evidence; Lundbeck stays a keyword
        elif w.isupper() or (w[0].isupper() and i > 0 and w.lower() not in STOP):
            terms.add(w)
    return sorted(terms)


def marks_in(text):
    low = text.lower()
    out = {}
    for k, pat in MARKS.items():
        n = len(re.findall(pat, low))
        if n:
            out[k] = n
    m = re.findall(r"correction to (\d{3})|corrected by (\d{3})", low)
    corrects = sorted({a or b for a, b in m})
    if corrects:
        out["corrects"] = corrects
    return out


def eligible_sources(lab, records):
    """Live and degraded sources with their files. External and unavailable sources are listed, never read."""
    out = []
    for r in records:
        if r.get("status") not in ("live", "degraded"):
            continue
        locs = check.split(r.get("location", ""))
        ext = any(lab.where(l)[1] for l in locs) or r.get("standing") == "unavailable"
        files = []
        if not ext:
            for loc in locs:
                files += check.files_for(lab, loc, check.split(r.get("pattern", "*")))
        out.append((r, ext, sorted(set(files))))
    return out


def file_date(path, text, r):
    m = DATE_RE.search(os.path.basename(path))
    if m:
        return m.group(1)
    for pat in (r"^- (?:Date|Planted): \**(\d{4}-\d{2}-\d{2})", r"^date: (\d{4}-\d{2}-\d{2})", r"^\*\*Date:\*\* (\d{4}-\d{2}-\d{2})"):
        m = re.search(pat, text[:3000], re.M)
        if m:
            return m.group(1)
    return dt.datetime.fromtimestamp(os.path.getmtime(path)).strftime("%Y-%m-%d")


def record_tier(text, r):
    src = r.get("tier", "?")
    if src != "mixed":
        return src
    m = re.search(r"^- Attribution: \**([a-z]+)", text[:3000], re.M)
    if m:
        return {"his": "his-words", "endorsed": "endorsed", "system": "system", "other": "other"}.get(m.group(1), m.group(1))
    if r.get("id") == "editorial-work":
        return "his-word-inside" if "locked by venkat" in text.lower() else "generated"
    if "proposed" in text[:1500].lower():
        return "proposed"
    return "mixed (see record)"


def strip_md(s):
    s = re.sub(r"[*_`>#\[\]]", "", s)
    return re.sub(r"\s+", " ", s).strip()


def substantive(lines, bullets=False):
    """First line that reads as prose: not a heading, bullet, table row, note in italics, fence, image, or a
    placeholder in parentheses. With bullets=True, a bullet's text counts when no prose line exists."""
    for line in lines:
        s = line.strip()
        if not s or s[0] in "#-|_<>`(" or s.startswith("!["):
            continue
        return strip_md(s)
    if bullets:
        for line in lines:
            s = line.strip()
            if s.startswith(("- ", "* ", "1. ")) and len(s) > 12 and not s.startswith("- ("):
                return strip_md(s[2:])
    return ""


def gist_of(text):
    """Lead sentence, then up to three section leads ("heading: first line"), so a record's meaning is in the index,
    not only its opening boilerplate. Capped at 420 characters; the size line reports what that costs."""
    m = re.search(r"^- Tension: (.+)$", text, re.M)
    if m:
        return strip_md(m.group(1))[:420]
    body = re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.S).split("\n")
    first = substantive(body)[:160]
    parts, seen = [first], {first[:60]}
    heads = [i for i, l in enumerate(body) if re.match(r"^#{2,3} ", l)]
    for i in heads[:8]:
        lead = substantive(body[i + 1:i + 14], bullets=True)
        if lead and lead[:60] not in seen:
            seen.add(lead[:60])
            parts.append(f"{strip_md(body[i])[:60]}: {lead[:100]}")
        if len(parts) >= 4:
            break
    return " ¶ ".join(p for p in parts if p)[:420]


def title_of(text, path):
    m = re.search(r"^# (.+)$", text, re.M)
    if m:
        return strip_md(m.group(1))[:160]
    m = re.search(r"^title: (.+)$", text[:2000], re.M)
    return strip_md(m.group(1))[:160] if m else os.path.basename(path)


def build_index(lab, records):
    os.makedirs(INDEX_DIR, exist_ok=True)
    srcs = eligible_sources(lab, records)
    n_files, total_bytes, out = 0, 0, []
    for r, ext, files in srcs:
        for path in files:
            n_files += 1
            try:
                raw = open(path, "rb").read()
            except OSError:
                continue
            total_bytes += len(raw)
            text = raw.decode("utf-8", "replace")
            base = {"path": rel(lab, path), "source": check.rid(r), "ceiling": r.get("use", "?"),
                    "source_tier": r.get("tier", "?"), "date": file_date(path, text, r)}
            if path.endswith(".json") and os.path.basename(path) == "capabilities.json":
                try:
                    for c in json.loads(text).get("capabilities", []):
                        out.append({**base, "ref": base["path"] + "#" + c["id"], "kind": "capability",
                                    "tier": r.get("tier"), "title": c.get("name", "")[:160],
                                    "gist": strip_md(" ".join([c.get("description", "")] + c.get("problems", [])))[:240],
                                    "ids": [c["id"]], "marks": {"sources": c.get("sources", [])}})
                except (ValueError, KeyError):
                    pass
                continue
            if path.endswith(".jsonl"):
                for i, line in enumerate(text.split("\n"), 1):
                    if not line.strip():
                        continue
                    try:
                        d = json.loads(line)
                    except ValueError:
                        continue
                    out.append({**base, "ref": f"{base['path']}#line:{i}", "kind": "line", "tier": r.get("tier"),
                                "date": (str(d.get("ts", d.get("date", base["date"])))[:10]),
                                "title": " ".join(str(d.get(k, "")) for k in ("company", "slug", "id", "verdict") if d.get(k))[:160],
                                "gist": line[:240], "ids": ID_RE.findall(line), "marks": marks_in(line)})
                continue
            if path.endswith(".json"):
                out.append({**base, "ref": base["path"], "kind": "file", "tier": r.get("tier"),
                            "title": os.path.basename(path), "gist": text[:240].replace("\n", " "),
                            "ids": sorted(set(ID_RE.findall(text)))[:20], "marks": marks_in(text)})
                continue
            out.append({**base, "ref": base["path"], "kind": "file", "tier": record_tier(text, r),
                        "title": title_of(text, path), "gist": gist_of(text),
                        "ids": sorted(set(ID_RE.findall(text)))[:20], "marks": marks_in(text)})
            for line in text.split("\n"):
                m = ROW_RE.match(line)
                if not m:
                    continue
                rid_, rest = m.group(2), m.group(3)
                cells = [c.strip() for c in rest.split("|")]
                date = cells[0] if cells and DATE_RE.fullmatch(cells[0]) else base["date"]
                body = " | ".join(cells)
                tm = re.search(r"\*\*(.+?)\*\*", rest)
                low = rest.lower()
                tier = "his-ruling" if ("his word" in low or "venkat:" in low or "his ruling" in low) else ("proposed" if "proposed" in low else r.get("tier"))
                out.append({**base, "ref": f"{base['path']}#row:{rid_}", "kind": "row", "tier": tier, "date": date,
                            "title": strip_md(tm.group(1))[:160] if tm else f"row {rid_}", "gist": strip_md(body)[:240],
                            "ids": sorted(set(ID_RE.findall(rest)) | {rid_}), "marks": marks_in(rest)})
    with open(INDEX, "w") as f:
        for rec in out:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    with open(COMPACT, "w") as f:
        for rec in out:
            f.write(f"{rec['ref']} | {rec['source']} | {rec['date']} | {rec['tier']} | {rec['ceiling']} | {rec['title']} — {rec['gist']}\n")
    eligible = sum(len(files) for _, _, files in srcs)
    stats = {"built": dt.datetime.now().strftime("%Y-%m-%d %H:%M"), "records": len(out), "files": n_files, "eligible_files": eligible,
             "sources": len(srcs), "source_bytes": total_bytes, "compact_bytes": os.path.getsize(COMPACT),
             "compact_tokens_est": os.path.getsize(COMPACT) // 4}
    json.dump(stats, open(os.path.join(INDEX_DIR, "stats.json"), "w"), indent=1)
    cov = "coverage complete" if n_files == eligible else f"COVERAGE GAP: {n_files} indexed of {eligible} eligible"
    print(f"OK index: {len(out)} records from {n_files} files across {len(srcs)} sources; {cov}; "
          f"compact index {stats['compact_bytes']} bytes (~{stats['compact_tokens_est']} tokens)")
    return 0 if n_files == eligible else 1


def load_index():
    if not os.path.isfile(INDEX):
        sys.exit("ALERT retrieval: no index; run `python3 context/sources/retrieve.py index`")
    return [json.loads(l) for l in open(INDEX) if l.strip()]


def stats_line():
    p = os.path.join(INDEX_DIR, "stats.json")
    if not os.path.isfile(p):
        return "index size: no index built"
    s = json.load(open(p))
    return (f"index size: {s['records']} records, {s['compact_bytes']} bytes, ~{s['compact_tokens_est']} tokens "
            f"(full-index semantic pass); {s['files']} files, {s['source_bytes']} source bytes, built {s['built']}")


ALWAYS_IN_SCOPE = ["rulings", "root-doctrine", "drivers", "architecture"]  # small, rule-bearing; a scope never drops them (runs 3 of 2026-09-12: two tests lost their ruling by scoping it out)


def candidates(lab, query, scope=None, top=40, scoped_out=None):
    idx = load_index()
    if scope:
        scope = list(dict.fromkeys(list(scope) + ALWAYS_IN_SCOPE))
        idx = [r for r in idx if r["source"] in scope]
    exact = names_in(query)
    q_tokens = tokens(query)
    text_cache = {}

    def text_of(path):
        if path not in text_cache:
            try:
                text_cache[path] = open(os.path.join(lab.root, path), "rb").read().decode("utf-8", "replace")
            except OSError:
                text_cache[path] = ""
        return text_cache[path]

    scored = []
    for r in idx:
        head = (r["title"] + " " + r["gist"]).lower()
        body = r["gist"].lower() if r["kind"] != "file" else text_of(r["path"]).lower()
        hits_exact = [t for t in exact if t.lower() in body or t in r.get("ids", [])]
        hits_head = q_tokens & tokens(head)
        hits_body = {t for t in q_tokens if t in body}
        weight = 1.0 if len(body) < 20000 else (0.5 if len(body) < 100000 else 0.25)  # a big file holds every word; that is not evidence
        score = 10 * len(hits_exact) + 2 * len(hits_head) + len(hits_body) * weight
        if score:
            scored.append((score, r, hits_exact, sorted(hits_head | hits_body)))
    scored.sort(key=lambda x: (-x[0], x[1]["date"]), reverse=False)
    out = [{"ref": r["ref"], "source": r["source"], "date": r["date"], "tier": r["tier"], "ceiling": r["ceiling"],
            "title": r["title"], "score": s, "exact": e, "keywords": k} for s, r, e, k in scored[:top]]
    compact, size = COMPACT, None
    if scope:
        compact = scoped_out or os.path.join(INDEX_DIR, "compact-scoped.txt")
        line = lambda r: f"{r['ref']} | {r['source']} | {r['date']} | {r['tier']} | {r['ceiling']} | {r['title']} — {r['gist']}\n"
        by_ref = {r["ref"]: r for r in idx}
        with open(compact, "w") as f:
            f.write(f"# must consider: {len(out)} deterministic candidates (exact ids and names, keyword overlap), best score first\n")
            for c in out:
                f.write(line(by_ref[c["ref"]]))
            f.write(f"# all {len(idx)} records in scope {','.join(scope)}\n")
            for r in idx:
                f.write(line(r))
        size = {"records": len(idx), "bytes": os.path.getsize(compact), "tokens_est": os.path.getsize(compact) // 4, "scope": scope, "must_consider": len(out)}
    return {"query": query, "exact_terms": exact, "keyword_terms": sorted(q_tokens), "scope": scope,
            "candidates": out, "index_records": len(idx), "compact": rel(lab, compact), "scoped_size": size, "stats": stats_line()}


def eligible_paths(lab, records):
    paths = {}
    for r, ext, files in eligible_sources(lab, records):
        for f in files:
            paths[rel(lab, f)] = r
    return paths


def excerpt(text, terms, n=6):
    lines = [l.strip() for l in text.split("\n") if l.strip()]
    hits = [l for l in lines if any(t.lower() in l.lower() for t in terms)]
    pick = hits[:n] if hits else [l for l in lines if not l.startswith("---")][:n]
    return [strip_md(l)[:300] for l in pick]


def pointer_state(lab, text):
    """Paths named inside a record, and whether each resolves on this machine."""
    out = []
    for p in sorted(set(PATH_RE.findall(text)))[:12]:
        full = os.path.expanduser(p)
        out.append({"path": p, "resolves": os.path.exists(full)})
    return out


def supersession(lab, rec, idx_by_ref):
    """Row-level: a later row that says 'Correction to NNN' or 'corrected by' marks NNN superseded."""
    if rec["kind"] != "row":
        return None
    my = rec["ref"].rsplit("#row:", 1)[1]
    rows = [r for r in idx_by_ref.values() if r["kind"] == "row" and r["path"] == rec["path"]]
    for r in rows:
        if my in r.get("marks", {}).get("corrects", []):
            return {"state": "superseded", "by": r["ref"], "because": r["gist"][:160]}
    if rec.get("marks", {}).get("corrects"):
        return {"state": "current", "corrects": [f"{rec['path']}#row:{c}" for c in rec["marks"]["corrects"]]}
    return {"state": "current"}


def fetch(lab, records, query, picks, out_path=None):
    idx = load_index()
    by_ref = {r["ref"]: r for r in idx}
    allowed = eligible_paths(lab, records)
    terms = names_in(query) + sorted(tokens(query))
    results, refused = [], []
    for p in picks.get("picks", []):
        ref = p["ref"]
        path = ref.split("#", 1)[0]
        if path not in allowed:
            refused.append(ref)
            continue
        rec = by_ref.get(ref) or by_ref.get(path)
        if rec is None:
            refused.append(ref + " (not in index)")
            continue
        src = allowed[path]
        text = open(os.path.join(lab.root, path), "rb").read().decode("utf-8", "replace")
        if rec["kind"] == "row":
            rid_ = ref.rsplit("#row:", 1)[1]
            row = next((l for l in text.split("\n") if ROW_RE.match(l) and ROW_RE.match(l).group(2) == rid_), "")
            evidence = [strip_md(row)[:600]]
            marks = marks_in(row)
        elif rec["kind"] == "capability":
            cid = ref.rsplit("#", 1)[1]
            cap = next((c for c in json.loads(text).get("capabilities", []) if c["id"] == cid), {})
            evidence = [json.dumps({k: cap.get(k) for k in ("id", "name", "description", "problems", "outcomes", "maturity", "sources")}, ensure_ascii=False)]
            marks = {"sources": cap.get("sources", [])}
            extracts = []
            for s in cap.get("sources", []):
                key = s.split(" ")[0].split("(")[0]
                for ef in glob.glob(os.path.join(lab.root, os.path.dirname(path), "stage1-extracts", key + "*")):
                    et = open(ef, "rb").read().decode("utf-8", "replace")
                    inner = re.findall(r"\(([^)]+)\)", s)
                    words = [w.strip() for w in (inner[0].split(",") if inner else []) if w.strip()] or [cap.get("name", "")[:30]]
                    extracts.append({"file": rel(lab, ef), "quote": excerpt(et, words, 3), "pointers": pointer_state(lab, et[:4000])})
            marks["extracts"] = extracts
        elif rec["kind"] == "line":
            n = int(ref.rsplit("#line:", 1)[1])
            evidence = [text.split("\n")[n - 1][:600]]
            marks = marks_in(evidence[0])
        else:
            # the record's own claim first (title and gist), then the lines that match the question
            own = [l for l in (rec.get("title", ""), rec.get("gist", "")) if l]
            evidence = own + [l for l in excerpt(text, terms) if l not in own]
            marks = marks_in(text)
        fm = re.search(r"^supersedes: ?(.*)$", text[:2000], re.M)
        results.append({
            "ref": ref, "source": src.get("id"), "kind": rec["kind"], "date": rec["date"], "tier": rec["tier"],
            "ceiling": src.get("use"), "title": rec["title"], "why": p.get("reason", ""), "rank": len(results) + 1,
            "evidence": evidence, "marks": marks,
            "limits": {"not-alone": src.get("not-alone", ""), "may-inform": src.get("may-inform", ""), "source-notes": src.get("notes", "")},
            "supersession": supersession(lab, rec, by_ref), "supersedes_field": fm.group(1).strip() if fm else None,
            "pointers": pointer_state(lab, text[:6000]) if rec["kind"] == "file" else [],
            "age_days": (dt.date.today() - dt.date.fromisoformat(rec["date"])).days if DATE_RE.fullmatch(rec["date"]) else None,
        })
    # conflict candidates the script can see: two results from different sources, one of them authoritative, on the same query
    pairs = []
    for i, a in enumerate(results):
        for b in results[i + 1:]:
            if a["source"] != b["source"] and "authoritative" in (a["ceiling"], b["ceiling"]):
                pairs.append({"a": a["ref"], "b": b["ref"], "why": f"{a['source']} ({a['ceiling']}, {a['date']}) vs {b['source']} ({b['ceiling']}, {b['date']})"})
    exact_hit = any(r["marks"] and r["kind"] != "file" or any(t.lower() in " ".join(r["evidence"]).lower() for t in names_in(query)) for r in results)
    script_missing = not results or (not exact_hit and all(len(tokens(" ".join(r["evidence"])) & tokens(query)) < 3 for r in results))
    searched = [{"source": check.rid(r), "files": len(files) if not ext else None, "external": ext}
                for r, ext, files in eligible_sources(lab, records)]
    package = {
        "query": query, "when": dt.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "results": results, "refused": refused,
        "conflicts": {"flagged_by_model": picks.get("conflicts", []), "candidates_by_script": pairs},
        "missing_evidence": {"script": script_missing, "model": picks.get("missing_evidence", {})},
        "searched": searched, "index": stats_line(),
        "semantic_pass": picks.get("semantic_pass", {}),
    }
    if out_path:
        json.dump(package, open(out_path, "w"), indent=1, ensure_ascii=False)
    os.makedirs(INDEX_DIR, exist_ok=True)
    with open(RUNS, "a") as f:
        f.write(json.dumps({"when": package["when"], "query": query, "picked": [r["ref"] for r in results], "refused": refused,
                            "missing": package["missing_evidence"], "semantic_pass": package["semantic_pass"]}) + "\n")
    return package


def main():
    argv = sys.argv[1:]
    if not argv:
        print(__doc__); return 2
    lab = check.Lab(os.path.dirname(os.path.dirname(HERE)))
    records = check.parse(open(lab.register).read())
    if records is None:
        print("ALERT retrieval: register markers missing"); return 1
    cmd, rest = argv[0], argv[1:]

    def opt(name, default=None):
        return rest[rest.index(name) + 1] if name in rest else default

    if cmd == "index":
        return build_index(lab, records)
    if cmd == "stats":
        print(stats_line()); return 0
    if cmd == "sources":
        n = 0
        for r in records:
            if r.get("status") not in ("live", "degraded"):
                continue
            n += 1
            print(f"{check.rid(r)} | {r.get('use')} | {r.get('tier')} | {r.get('kind')} | may inform: {r.get('may-inform')} | not alone: {r.get('not-alone')}")
        print(f"sources: {n} readable; pick the ids that could hold evidence for the question, then run candidates --scope id,id")
        return 0
    if cmd == "candidates":
        q = next((a for a in rest if not a.startswith("--") and rest[rest.index(a) - 1] not in ("--scope", "--top", "--out", "--scoped-out")), None) if rest else None
        if not q:
            print("usage: retrieve.py candidates \"<query>\" [--scope id,id] [--top N] [--out file]"); return 2
        scope = opt("--scope")
        res = candidates(lab, q, scope.split(",") if scope else None, int(opt("--top", 40)), opt("--scoped-out"))
        out = opt("--out")
        if out:
            json.dump(res, open(out, "w"), indent=1, ensure_ascii=False)
        print(f"candidates: {len(res['candidates'])} for {res['exact_terms']} + {len(res['keyword_terms'])} keywords; {res['stats']}")
        if res["scoped_size"]:
            z = res["scoped_size"]
            print(f"scoped pass: {z['records']} records, {z['bytes']} bytes, ~{z['tokens_est']} tokens in {res['compact']} (scope {','.join(z['scope'])})")
        for c in res["candidates"][:15]:
            print(f"  {c['score']:>3} {c['ref']} [{c['source']} {c['date']} {c['tier']} {c['ceiling']}] {c['title'][:70]}")
        return 0
    if cmd == "fetch":
        q, picks_path = opt("--query"), opt("--picks")
        if not q or not picks_path:
            print("usage: retrieve.py fetch --query \"<q>\" --picks picks.json [--out package.json]"); return 2
        pkg = fetch(lab, records, q, json.load(open(picks_path)), opt("--out"))
        print(f"package: {len(pkg['results'])} results, {len(pkg['refused'])} refused, conflicts flagged {len(pkg['conflicts']['flagged_by_model'])}, "
              f"missing-evidence script={pkg['missing_evidence']['script']} model={pkg['missing_evidence']['model'].get('state', '?') if isinstance(pkg['missing_evidence']['model'], dict) else pkg['missing_evidence']['model']}")
        if pkg["refused"]:
            print("REFUSED outside the register: " + "; ".join(pkg["refused"]))
            return 1
        return 0
    print(__doc__); return 2


if __name__ == "__main__":
    sys.exit(main())
