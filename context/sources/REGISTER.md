---
name: source-register
what: Retrieval's list of what it may depend on. One record per source the lab treats as knowledge, with where it is now, what kind it is, who owns it, where this copy stands, how much authority its records carry, what jobs it may inform, and what it must never establish on its own.
status: live since 2026-09-12. Build step 2 (AD-06) complete at his word, 2026-09-12 01:44 (AD-19), and closed after the acceptance review at his word, 02:10 (AD-20, AD-21). Retrieval itself is not built and step 3 has not started.
home: context/sources/ (proposed, AD-16). The same idea as intent/STANDING.md: the list changes, the reader does not.
reads_this: context/sources/check.py (register, health, coverage, freshness, source discovery, resolve); one line on the facts sheet; context-check section G
proof: context/sources/tests/check_tests.py (planted faults: missing, moved, duplicate id, competing location, nested location, broken location, an archive-only folder, bad words, unregistered folder and repo)
part_of: retrieval (docs/architecture/CAPABILITY-DEFINITIONS.md#retrieval, "Source register"). A store, not a capability (AD-12).
rules: sources stay canonical where they live. Nothing here is a copy. Adding a source is an edit here plus a run of the check. Retiring one sets status retired and adds a dated line; nothing is deleted.
---

# Source register

**What this answers.** For retrieval, and for any session before it leans on a file: what sources may it depend on, where are they now, what are they good for, and when should they not influence a judgment.

**How to read it.** One record per source, a heading plus `- key: value` lines, between the two `register` markers. `check.py` parses exactly that. Paths are relative to the lab root, split by `;`. A path that starts with `~` or `/` is outside the lab: its existence is checked, its files are not counted. `pattern` is what counts as a record inside the location.

**How to reach a source.** Ask by id, never by path. One command, deterministic:

```
python3 context/sources/check.py resolve career-model
```

It prints the current location and whether it exists, the status, the standing, and the use limits below. A consumer that writes the path into its own file is taking a copy that will go stale.

## Words a script checks

- `status`: the registry standard's five (AD-05): planned · building · live · degraded · retired. Only live and degraded may be read.
- `standing`: where the copy being read stands. One source has one id, whatever copies exist: a replica is the same source read from a copy, and `canonical-at` names the original. A copy never gets its own id (his word, 2026-09-12 01:44). canonical (the original) · replica (a copy; `canonical-at` says where the original is) · historical (kept as a record; nothing in it is current) · unavailable (known, not reachable from this machine).
- `tier` (authority): his-ruling · his-words · endorsed · system · proposed · generated · mixed. `mixed` means each record carries its own tier; `tier-field` says where.
- `use`: the ceiling, meaning the maximum influence this source is permitted to have. It may be lowered for a specific job, never raised (his word, 2026-09-12 01:44). authoritative (may settle a judgment on its own, inside its job) · evidentiary (shows what happened or what was said; supports, never settles; cite the pointer) · contextual (shapes how to read or write; never establishes a fact) · exploratory (a lead to check; nothing rests on it alone).
- `date-field`: how a record's date is read. `mtime` means the file's change time. Anything else names a line or key inside the record.

## Use limits

**The rule.** The strength of the action must not exceed the strength of the evidence. `use` is the ceiling: the maximum influence permitted, which a consumer may lower for the job in front of it and may never raise. `may-inform` says which jobs the source may reasonably influence. `not-alone` says what it must never establish by itself, even when it is the only thing that mentions it. These are job limits, not a grade: a source can be authoritative for one question and useless for the next. The AI reads all three before it leans on a source. A script checks that they are there and that the words are allowed. Nothing scores them.

## Adding a source

Seven questions, answered in the record, not in a rules engine. What job could it help with (`may-inform`). What does it actually represent (`kind`). How authoritative is it for that job (`tier`, `use`). Is it current enough (`date-field`, `standing`). Can it be traced (`location`, `pattern`, and anchors inside). Is it distinct from a source already here (if not, extend that record). What can it not safely tell us (`not-alone`). Then run the check. Source discovery proposes candidates; a person answers the seven and adds the record. Nothing registers itself.

**Not registered yet, on purpose:** most of what sits outside the lab root (the iMac, the two peer folders `~/Documents/os-factory` and `~/Documents/claude-cowork`), the `.claude/` folder, which holds procedures, not knowledge, and three parts of the warehouse: `old-mac-documents` (client material), `_backups` (snapshots of the whole lab), and `research-sources` (other people's articles). A folder named `_archive` inside a registered location is never counted. Source discovery reports what it sees inside the lab; a person decides. Reviewed and left: `discovery-accepted.txt`.

<!-- register:start -->

### seeds
- id: seeds
- kind: one idea per file, with source, date, attribution, tension
- location: work-os/brand-os/engagement-os/seedbank/session; work-os/brand-os/engagement-os/seedbank/written; work-os/brand-os/engagement-os/seedbank/spoken
- pattern: *.md
- owner: brand-os, engagement-os
- standing: canonical
- tier: mixed
- tier-field: "- Attribution:" (his, endorsed, other, system)
- date-field: "- Date:"
- status: live
- use: evidentiary
- may-inform: what he has said and thought about a subject; what to write next; whether an idea is a repeat (the repeat check); what connects to what
- not-alone: a rule or a ruling (those live in the rulings files); a fact about the world outside the lab; anything public without the seed's own source checked
- read-by: seed-capture (find-similar.py), cultivator, ARCHIE, hand tests
- notes: 797 files on 2026-09-12. Written seeds are older batches; session seeds are live captures. Nothing else in the seedbank folder counts (README, INDEX, missed.md are about the seeds).
- added: 2026-09-12
- changed: 2026-09-12

### receipts
- id: receipts
- kind: session receipts and day reviews; follow-up lines, decisions, corrections
- location: evidence/receipts
- pattern: *.md
- owner: evidence-record
- standing: canonical
- tier: system
- date-field: front matter "date:"
- status: live
- use: evidentiary
- may-inform: what happened in a session and what changed; what was decided, in his quoted words; what is still open (the follow-up lines)
- not-alone: his current position when a later receipt or a ruling exists (read the newest); a ruling itself (the DECISIONS file of its domain is the home); whether a task is done (the facts sheet wins)
- read-by: facts.py (follow-ups), alfred-open, alfred-close
- notes: new files only, never edited. Decisions quoted inside carry his words; the receipt itself is Alfred's record.
- added: 2026-09-12
- changed: 2026-09-12

### audits
- id: audits
- kind: dated audits about the lab itself, one folder each
- location: evidence/audits
- pattern: *.md
- owner: evidence-record
- standing: canonical
- tier: system
- date-field: folder name (YYYY-MM-DD-name)
- status: live
- use: evidentiary
- may-inform: the state of the lab on the audit's date; which rules had no source; open conflicts with owners
- not-alone: the state of the lab today (an audit is dated and never edited); a rule change
- read-by: facts.py (follow-ups written in audits), alfred-open
- added: 2026-09-12
- changed: 2026-09-12

### transcripts
- id: transcripts
- kind: rendered session transcripts, Claude Code and Codex, every line with a stable anchor
- location: evidence/sessions
- pattern: *.md
- owner: evidence-record
- standing: canonical
- tier: mixed
- tier-field: the speaker of each line (his lines are his-words; the rest is system)
- date-field: front matter "date:" where present, else mtime
- status: live
- use: evidentiary
- may-inform: what was said, by whom, and when, with an anchor; the origin of a seed, a correction, or a claim
- not-alone: a decision (it must appear in a receipt or a ruling to count); anything public (two raw session logs once held real-looking API keys; scrubbed 2026-09-12 01:43, receipt R-2026-09-12-0143-7c21, and a search finds none today); his position when a later line reverses it
- read-by: seed-capture (anchors), alfred-close (late receipts), claim checks
- notes: 266 files on 2026-09-12; SYNC-LOG.md and USAGE.jsonl in the same folder are about the capture, not records. The 154 transcripts from before 2026-09-05 have no raw source left; these renders are the only copy.
- added: 2026-09-12
- changed: 2026-09-12

### alfred-log
- id: alfred-log
- kind: append-only duty log, one proof line per duty per run
- location: .claude/agents/alfred/LOG.md
- pattern: LOG.md
- owner: Alfred
- standing: canonical
- tier: system
- date-field: each line starts with the timestamp
- status: live
- use: evidentiary
- may-inform: whether a duty ran and when; the gap since the last run
- not-alone: whether the duty achieved anything (the facts sheet and the driver's own proof lines say that)
- read-by: facts.py (log gap), the duty pass
- added: 2026-09-12
- changed: 2026-09-12

### drivers
- id: drivers
- kind: the current drivers of the lab, with state, threats, and proof lines
- location: context/intent/STANDING.md
- pattern: STANDING.md
- owner: Venkat; Alfred appends state
- standing: canonical
- tier: his-ruling
- date-field: dated state lines and History entries
- status: live
- use: authoritative
- may-inform: what matters now and what would threaten it; how to weigh a result against a driver; what the open routine looks at first
- not-alone: a fact about the lab (each driver names the script that proves it); anything about a driver that is not in this file (four is the cap, his word)
- read-by: alfred-open, the duty pass, implication-lens, hand tests
- added: 2026-09-12
- changed: 2026-09-12

### rulings
- id: rulings
- kind: rulings and decision logs, dated and numbered
- location: RULINGS-IN-FORCE.md; work-os/brand-os/DECISIONS.md
- pattern: *.md
- owner: each file's domain; brand-os/DECISIONS.md is the front door for rulings about Venkat (ruling 034)
- standing: canonical
- tier: mixed
- tier-field: each row says "his word", "proposed", or quotes him; RULINGS-IN-FORCE.md Part 3 is open questions, not rulings
- date-field: the date column of each row
- status: live
- use: authoritative
- may-inform: any judgment about a rule, the voice, publishing, the lab's shape; whether something needs his word
- not-alone: a row marked proposed or assumed (it is Alfred's design until he says yes, twice for a rule); a superseded row (read the newest row on the subject; 036 is corrected by 037)
- read-by: sessions by hand; nothing reads them by script yet
- notes: the Telegraph decisions file and the architecture decisions file are rulings too, but each is read through its own source (telegraph-plus, architecture) so no file is counted twice (fixed 2026-09-12 after the acceptance review).
- added: 2026-09-12
- changed: 2026-09-12

### root-doctrine
- id: root-doctrine
- kind: the front door and the fixed core: roots, taste, done bar, how he wants work done
- location: CLAUDE.md; ROOT.md; TASTE.md; DONE.md; context/how-i-work.md
- pattern: *.md
- owner: Venkat
- standing: canonical
- tier: mixed
- tier-field: CLAUDE.md and how-i-work.md mix his rulings with system text; ROOT.md and TASTE.md are his; DONE.md is his from 2026-08-11 and whether it is still the bar is open
- date-field: mtime
- status: live
- use: authoritative
- may-inform: how to work, how to write to him, what is forbidden, where a file goes
- not-alone: whether DONE.md is still the bar (open, RULINGS-IN-FORCE.md Part 3); the "known broken" list, which the facts sheet measures fresh every session
- read-by: every session (loaded by Claude Code)
- notes: how-i-work.md was changed by another session at 00:54 on 2026-09-12 and now reads DRAFT while still imported live.
- added: 2026-09-12
- changed: 2026-09-12

### about-me
- id: about-me
- kind: drafts about who he is: voice profile, thinking model, point-of-view library, observed working notes, taste interview, specimens
- location: docs/about-me
- pattern: *.md
- owner: Venkat; drafts until he approves
- standing: canonical
- tier: proposed
- date-field: mtime, or the date in the file name where present
- status: live
- use: contextual
- may-inform: how he sounds, how he reasons, what he believes and how strongly (the point-of-view library's own rule: only when the subject genuinely touches it); how he has corrected the lab
- not-alone: a public claim about him; his position on anything he has not reviewed here (every file says DRAFT); a rule (observed corrections are evidence, not rules)
- read-by: my-voice, implication-lens, hand tests, generated who-i-am
- notes: 9 files on 2026-09-12. how-i-work--observed.md is append-only evidence about how he works. who-i-am--generated.md is a generated view of the career model.
- added: 2026-09-12
- changed: 2026-09-12

### career-model
- id: career-model
- kind: the career model hub: stages, domains, subdomains, 92 capabilities, skills, tools, products, and a graph
- location: work-os/brand-os/model
- pattern: *.json; *.md
- owner: brand-os (ruled canonical 2026-09-02 and hub 2026-09-10)
- standing: canonical
- tier: his-ruling
- date-field: mtime (entity files dated 2026-09-02)
- status: live
- use: authoritative
- may-inform: which capability a need, a posting, or a signal matches (by CAP- id); what he has done and where the evidence for it is; the generated who-i-am; the dossier and committee skills
- not-alone: what he should do next or where he is heading (it is derived only from past work; its own doc 14 says the profile says advisor, the record shows builder-verifier); a match without a capability id and an extract; any change to the model itself
- rule: every career-model match cites the capability id and the supporting extract, records the match where the work happens, and states what the model could not answer. Nothing updates the canonical model on its own (his hand-test rule, 2026-09-12).
- read-by: build_who_i_am.py, ARCHIE config, dossier and committee skills, my-voice; check_hub.py is its sensor
- notes: 20 of 22 artifact paths cited in its extracts do not resolve on this machine (scan of 2026-09-12). Not a reason to skip it; a reason retrieval must carry the pointer state. Three byte-identical copies exist elsewhere (the Desktop copy among them); they are replicas and are not registered.
- added: 2026-09-12
- changed: 2026-09-12

### voice-canon
- id: voice-canon
- kind: the one merged writing canon and its generated guide folder
- location: work-os/brand-os/voice/VENKAT-WRITING-CANON.md; work-os/brand-os/voice/README.md
- pattern: *.md
- owner: brand-os (ruling 028, 029)
- standing: canonical
- tier: his-ruling
- date-field: mtime
- status: live
- use: authoritative
- may-inform: any writing in his voice; the voice pass before anything ships
- not-alone: what he believes (the point-of-view library); a fact; the wording of a ruling
- read-by: my-voice, contextual-voice, build_guide.py
- notes: the generated guide folder (112 files) and voice/system are left out on purpose: the folder is a view, never hand-edited (ruling 029), and retrieval should return the canon, not the view.
- added: 2026-09-12
- changed: 2026-09-12

### positioning
- id: positioning
- kind: positioning, audience and ideal client profile, messaging
- location: work-os/brand-os/positioning; work-os/brand-os/audience; work-os/brand-os/messaging
- pattern: *.md
- owner: brand-os
- standing: canonical
- tier: mixed
- tier-field: file front matter or title says canon, draft, or report
- date-field: date in file name where present, else mtime
- status: live
- use: contextual
- may-inform: who the work is for, what they care about, what to say and not say; which angle fits the audience
- not-alone: a public number or claim (the "70% productivity lift" line on LinkedIn is the case, TODAY.md 2026-09-10); a file marked draft or report as if it were canon
- read-by: implication-lens, ARCHIE, the publishing skills
- added: 2026-09-12
- changed: 2026-09-12

### targets
- id: targets
- kind: target companies: dossiers, people, verdicts, signals
- location: work-os/brand-os/engagement-os/targets
- pattern: *.md; *.jsonl
- owner: engagement-os
- standing: canonical
- tier: system
- date-field: front matter or the ts field in JSON lines
- status: live
- use: evidentiary
- may-inform: what a target company shows in public (postings, news, vendors) as of the scan date; the latest verdict per company; who decides what, as far as postings say
- not-alone: a decision to reach out (his); a fact older than its scan date; anything about a person beyond what a posting states
- read-by: dossier, committee, target-scan, hand tests
- notes: 15 companies; the latest verdict per company is the last line for it in index/verdicts.jsonl (11 engage, 3 watch, 1 refused on 2026-09-12).
- added: 2026-09-12
- changed: 2026-09-12

### assets
- id: assets
- kind: the public value system's records: registry, opportunities, briefs, claim ledgers, QA, releases
- location: work-os/brand-os/engagement-os/assets
- pattern: *.md; *.yaml
- owner: engagement-os
- standing: canonical
- tier: mixed
- tier-field: registry.yaml status and decided_by per asset
- date-field: dates in file names and decided_by fields
- status: live
- use: authoritative
- may-inform: whether a public asset exists, its status, who decided it, which claims were checked; whether a new idea is a repeat (asset-corpus-match)
- not-alone: whether a checked claim is still true today (claim ledgers are dated); anything external (publishing needs his word every time)
- read-by: asset-corpus-match, the publishing skills, public-value-advisor
- added: 2026-09-12
- changed: 2026-09-12

### routine-outputs
- id: routine-outputs
- kind: briefs published by cloud routines and pulled into the lab, one file per run
- location: work-os/scheduled-tasks
- pattern: outputs/*.md
- owner: scheduled-routines
- standing: replica
- canonical-at: the routines' private pages on claude.ai, pulled by alfred-open; the page is the original, the file is the copy
- tier: system
- date-field: file name (YYYY-MM-DD.md)
- status: live
- use: exploratory
- may-inform: what moved in the market that week; leads to check; which signals kept coming back
- not-alone: anything about him or the lab (written blind, with no lab context, hand test 2026-09-12); a fact without opening the cited page (the routines could not open pages); a move to make (the hand test found their moves were "search more" and "ask someone")
- read-by: alfred-open (pulls them), hand tests; nothing reads them by script after that
- notes: 107 files on 2026-09-12; newest 2026-09-10. Evidence about the market, never about him.
- added: 2026-09-12
- changed: 2026-09-12

### lab-reports
- id: lab-reports
- kind: read-only scans, briefs, and plans about the lab itself
- location: docs/reports; docs/plans
- pattern: *.md
- owner: Alfred, at his ask
- standing: canonical
- tier: proposed
- date-field: file name (YYYY-MM-DD--name.md)
- status: live
- use: contextual
- may-inform: what was scanned and what it found on that date; the reasoning behind a plan; what was recommended
- not-alone: a ruling (a report proposes; the rulings files decide); the state of the lab today; a rule
- read-by: sessions by hand
- added: 2026-09-12
- changed: 2026-09-12

### telegraph-plus
- id: telegraph-plus
- kind: the current Telegraph line: doctrine, status, records
- location: work-os/projects/telegraph-plus
- pattern: *.md
- owner: the Telegraph project (its own repo)
- standing: canonical
- tier: mixed
- tier-field: its records/views/DECISIONS.md rows; CLAUDE.md there is doctrine
- date-field: mtime
- status: live
- use: authoritative
- may-inform: any Telegraph work: its doctrine, status, decisions, what needs him
- not-alone: rulings about Venkat himself (brand-os/DECISIONS.md); anything from the two superseded predecessors
- read-by: sessions working on Telegraph
- notes: the two superseded predecessors are not registered (retained for learning, not use).
- added: 2026-09-12
- changed: 2026-09-12

### upskill-records
- id: upskill-records
- kind: the Telegraph private instruction package's records: gates, governance decisions, open items, learning
- location: work-os/upskill-advisor/records
- pattern: *.md
- owner: upskill-advisor
- standing: canonical
- tier: mixed
- tier-field: decisions.md rows; open-items.md "Needs Venkat" section
- date-field: dates in file names and rows
- status: live
- use: evidentiary
- may-inform: Telegraph's history, gates passed, what still needs him
- not-alone: what governs telegraph-plus (unruled since 2026-09-07); a current Telegraph decision (telegraph-plus is the current line)
- read-by: facts.py (Telegraph items needing Venkat), sessions by hand
- notes: a session widened this record to governance/ and research/ on 2026-09-12 to close two discovery findings. Reverted at his word, 02:10 (AD-21): "a session cannot silently expand what Retrieval is allowed to depend on." Both folders are discovery candidates again and stay that way until he registers or accepts them. The telegraph/ repo and plans/ beside them are superseded and not registered.
- added: 2026-09-12
- changed: 2026-09-12

### concepts
- id: concepts
- kind: settled wording and the recovered profile notes
- location: work-os/brand-os/engagement-os/memory/concepts.md; work-os/brand-os/engagement-os/context/PROFILE.md
- pattern: *.md
- owner: engagement-os (recovered 2026-09-09, never merged)
- standing: canonical
- tier: mixed
- tier-field: each concepts.md line says his, endorsed, or system
- date-field: dates on each line where present, else mtime
- status: live
- use: contextual
- may-inform: the settled word for a thing; how a concept was first phrased
- not-alone: a rule; anything the voice canon or the rulings already settle differently
- read-by: seed-capture (step 5 writes here)
- notes: the recovery note asks whether engagement-os is even the right home. Registered where it is; a move changes one line here.
- added: 2026-09-12
- changed: 2026-09-12

### architecture
- id: architecture
- kind: the capability map, definitions, and architecture decisions
- location: docs/architecture
- pattern: *.md
- owner: capability-architecture
- standing: canonical
- tier: mixed
- tier-field: each decision row says his word, proposed, or assumed
- date-field: dates in rows and records
- status: live
- use: authoritative
- may-inform: whether a shared system exists and what covers a job; the three standards; the build sequence
- not-alone: rulings about Venkat himself; a row marked proposed or assumed, until his word
- read-by: docs/architecture/check.py, sessions before adding a system
- added: 2026-09-12
- changed: 2026-09-12

### public-site
- id: public-site
- kind: the public site, a Next.js repo with its own git remote (github.com/venkat-ai-portfolio/gullapalli-site)
- location: ~/Desktop/my-ai-lab-v2/gullapalli-site
- pattern: *.md; *.tsx
- owner: Venkat
- standing: canonical
- tier: his-words
- date-field: git log of that repo
- status: live
- use: evidentiary
- may-inform: what is public under his name today; what a reader of the site sees; whether a claim is already public
- not-alone: his current position (the site can lag the canon and the rulings); whether a public claim is true (the claim ledgers)
- read-by: sessions by hand; nothing in the lab reads it by script
- notes: outside the lab, found 2026-09-10 on the Desktop inside an old copy of the lab; check its remote before relying on it (CLAUDE.md). External: existence is checked, files are not counted. 12 markdown files on 2026-09-12.
- added: 2026-09-12
- changed: 2026-09-12

### career-advisor
- id: career-advisor
- kind: the analyses about him and the old work corpus from the career-advisor repo, as snapshotted from the iMac on 2026-09-10
- location: ~/Documents/_warehouse/career-advisor--snapshot-from-imac--2026-09-10
- pattern: *.md
- owner: Venkat
- standing: replica
- canonical-at: the career-advisor repo on the iMac; not reachable from this machine
- tier: mixed
- tier-field: each file's own front matter or header; unmarked text counts as proposed
- date-field: dates in file names and headers, else the snapshot date 2026-09-10
- status: live
- use: exploratory
- may-inform: where an analysis about him came from; the inputs behind the career model; the inventory in docs/about-me
- not-alone: anything current about him; anything docs/about-me or the career model already settles; anything public
- read-by: the inventory in docs/about-me (by hand, 2026-09-10); nothing by script
- notes: a snapshot, so it ages. The iMac copy may have moved on since 2026-09-10; the TODAY.md scan item is still open.
- added: 2026-09-12
- changed: 2026-09-12

### warehouse
- id: warehouse
- kind: what moved out of the lab, in dated folders, each with a note on what replaced it
- location: ~/Documents/_warehouse/README.md; ~/Documents/_warehouse/_archive; ~/Documents/_warehouse/_audit; ~/Documents/_warehouse/_templates; ~/Documents/_warehouse/agents-from-lab-2026-09-09; ~/Documents/_warehouse/alfred--before-charter-v2--2026-09-09; ~/Documents/_warehouse/career-advisor--recovered-handoff--2026-09-10; ~/Documents/_warehouse/engagement-os-archived-2026-09-10; ~/Documents/_warehouse/hooks-archived-2026-09-10; ~/Documents/_warehouse/skills-archived-2026-09-10; ~/Documents/_warehouse/unlazy-ledgers; ~/Documents/_warehouse/vscode-markdown-style-2026-09-11; ~/Documents/_warehouse/writing-guide-copies--moved-2026-09-11
- pattern: *.md
- owner: Venkat
- standing: historical
- tier: mixed
- tier-field: each moved file keeps its own marks; nothing here is current
- date-field: the date in each folder name
- status: live
- use: exploratory
- may-inform: what replaced what, and why; the wording of a superseded file when a live one still cites it; the history of a decision
- not-alone: anything current; anything public; a rule
- read-by: sessions by hand; snapshot.sh writes into it; nothing reads it by script
- notes: narrowed to the dated lab-move folders at his word, 2026-09-12 01:55 (AD-20); it was the whole warehouse root. Left out: old-mac-documents (named clients, RFPs, a 2020 non-compete; retrieval never reads it), _backups (snapshots of the whole lab, a second copy of every source here), research-sources (other people's articles; a separate decision), and the career-advisor snapshot, which has its own record above. Outside the lab on purpose: nothing there is a git repository and nothing there is published (CLAUDE.md).
- added: 2026-09-12
- changed: 2026-09-12

<!-- register:end -->
