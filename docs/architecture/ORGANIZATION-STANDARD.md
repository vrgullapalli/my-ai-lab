---
name: organization-standard
what: The Organization and Information Architecture standard. One answer to what belongs where, which copy is canonical, and how information becomes current, derived, historical, superseded, or temporary. Works the same in Dropbox, the wider estate, and, last, the lab.
status: APPROVED, his word 2026-09-15 02:51 (AD-40). Written 2026-09-15 by Alfred at his /goal (Step 2.5B) and proposed as AD-39; approved the same day. Marker name ROLE.md, area word Warehouse, and two of the four standard changes (proposed markers, derived rebuilds) are settled by AD-40; batching and quarantine are not yet authorized. Corrected after the first pilot on 2026-09-15 (AD-41, then his ruling AD-42 at 03:12): a same-id relocation is `relocated-from / relocated-to / relocated-on`, never a self-pointing `replaced-by`; lab snapshots are Work / ai-lab, role derived; Machine copies is for whole-machine, device, app, disk-image, or system-level copies only. No file, folder, or Dropbox object was moved, renamed, deleted, or refiled to write it.
home: docs/architecture/ (assumed; AD-09 put lab-as-a-system artifacts here and AD-34 opened the folder past three. One move if he picks another)
governed_by: Operational DNA, LAB-OPERATING-MODEL.md section 16 (AD-38)
evidence_base: docs/research/2026-09-14--step-2-5a-research-brief.md (the brief; "P-12" below means principle 12 of its section 12) · docs/research/assessments/STORAGE-ESTATE-BASELINE-2026-09-14.md (the baseline)
applies_to: any folder, collection, or file store Venkat owns. First the Dropbox estate, then the local disks and the warehouse, and the lab last, once the pattern has been proven on a pilot
does_not_do: design a folder tree for the estate, pick the sync shape, fix the backup, name the pilot's new paths, or write any marker file. Section 12 lists what is his to decide
tags: settled (already his word elsewhere) · proposed (this file, waiting on his yes) · open (his call, listed in section 12)
---

# Organization and information architecture standard

## 0. What this file is for

Filing, duplicate removal, the Dropbox cleanup, and the lab's own reorganization all need one stable answer to three questions:

1. Where does this belong?
2. Which copy is the real one?
3. Is this current, a copy, a build, history, or scratch?

This file gives that answer with five role words, six areas, one marker file, and a short set of rules. It is written so two people, or two sessions, reach the same answer without inventing a second vocabulary.

**The short version.** Every folder that matters declares what it is in one small file. Every piece of information has exactly one canonical home; every other copy says it is a copy and points home. Old structures point forward, in one hop, and stop governing. Nothing is filed by walking the tree; the machine keeps the map, notices drift, and proposes where things go. A person, Venkat, decides what is canonical, what moves, and what is adopted. Scripts prove the rest.

## 1. What organization becomes now that AI exists

**The old job.** A person files by hand into a taxonomy and remembers where things are. The folder tree is the index. When the person cannot keep up, backups absorb backups: the estate today has 12,103 folders holding one child and 241,966 files under names like `untitled folder 4` (baseline, section 3). That is not a hygiene failure. It is what hand filing does at 1.65 million objects.

**The redesigned job.** The tree stays shallow and declared. The machine, not the person, keeps the map: it reads the marker files, relates copies by content hash, classifies what is unfiled, recommends where a new thing goes, walks every supersession chain, and reports drift as three lists. The person rules on a short list of consequential calls: what is canonical, what moves, what is adopted, what is accepted. Filing becomes continuous instead of a one-time cleanup, and canonicality is kept true instead of checked once.

**Remove AI and the job no longer exists as designed.** The markers, hashes, manifests, and drift lists still hold true, because scripts own them. But nothing classifies, relates, or recommends. Filing goes back to the person, and the estate re-nests, which is exactly what happened before (baseline, section 3). The rules in this file are the guardrails and the sensors; the AI is the part that keeps the structure alive between cleanups.

**The value beyond speed.** Placement is proposed at the moment a thing is created. Copies are known, not discovered years later. A superseded folder cannot quietly become the one a session reads, because the map says so at every open. This is the same split the lab already runs on: the AI decides what to investigate, scripts decide what is true and what is forbidden.

## 2. The vocabulary

Five role words, one state, six areas, five scope words. Nothing else is added. Where a word already exists in the lab, this file uses that word and says where it came from.

### 2.1 The five roles

A role is what a folder, collection, or file store is, in relation to the truth.

| Role | Meaning | How a reader tells | What may be done to it |
|---|---|---|---|
| **canonical** | The one place this information is true. Edits happen here and only here | Marker says `role: canonical` | Edited, added to, filed into. Never a second one for the same id |
| **replica** | The same information, copied from the canonical, read-only, one direction | Marker says `role: replica` and `canonical-at:` names the id | Read. Refreshed from the canonical. Never edited in place; a differing replica is drift, and the canonical wins |
| **derived** | Built from canonical material by a script: an index, a rendered view, a snapshot, an export, a packed archive | Marker says `role: derived`, `derived-from:` names the id, `built:` gives the date, `rebuild:` gives the command | Rebuilt, overwritten by its builder. Never hand-edited. A derived file newer than its `built:` date is a finding |
| **historical** | Frozen. What was true, kept as a record. Nothing in it is current | Marker says `role: historical` and `as-of:` gives the freeze date | Read as evidence of what was. Never edited. Never the answer to what is now |
| **temporary** | Scratch, inbox, screenshots, downloads. Expected to expire | Marker says `role: temporary` and `expires:` gives a date (default 180 days from `as-of`) | Used, then batched to the warehouse with a manifest when expired. Never referenced by anything durable |

The first three words, canonical, replica, historical, are already the source register's `standing` words (AD-17, AD-19, settled). The register's fourth word, `unavailable`, is not a role; it says a copy cannot be reached from this machine, and it stays in the register as is. This file adds two roles, derived and temporary, and uses `canonical-at` exactly as the register does.

**One rule under all five** (settled, AD-19): one logical identity, whatever the copies. A replica never gets its own id. A derived view gets its own id, because it is a different thing built from the canonical. A historical collection keeps the id it had.

### 2.2 The one state: superseded

Superseded is not a sixth role. It is a state any structure can be in, shown by one of two fields, for two different events:

- `replaced-by: <other id>`: a **different thing** now governs. The old content is frozen in place (role historical). The new home says `replaces: <old id>`. An id never replaces itself.
- `relocated-to: <location>` plus `relocated-on: <date>`: the **same stable id** moved to a new location. The old folder holds only its marker. The live marker at the new location says `relocated-from: <old location>`, so the move is written in both directions. Nothing was replaced. Identity stays the id; the two location fields are a dated record of where the thing was and went, and the map still resolves the id.

A marker carries `replaced-by` or `relocated-to`, never both. This split was settled after the first pilot (2026-09-15, AD-41 and AD-42): the pilot had written a relocation as a replacement, which made the old marker point at its own id. Section 6 says what each does.

### 2.3 The six areas

An area is a top-level home with one job. Areas are by the job of the information, not by year, file type, client, or device.

| Area | Job | Belongs | Does not belong | Default role | Default scope |
|---|---|---|---|---|---|
| **Work** | Things Venkat makes or is making: the lab, projects, engagements, writing, products | One folder per body of work, under its scope | Other people's material he only uses (Library); frozen past work that has been replaced whole (Warehouse); scratch (Temporary) | canonical | Second level names it: `ai-lab`, `professional`, `career`, `public` |
| **Library** | Material other people made that he keeps to use: purchased assets, stock icons, fonts, templates, articles, books, datasets | Replaceable reference material | Anything he authored; anything a client gave him under confidence (that is Work, professional) | canonical, low authority (never better than contextual in the register's `use` words) | `ai-lab` or `professional` |
| **Personal** | Family, household, photos, video, personal planning | Personal-scope material | Anything professional or public | canonical | `personal`, always |
| **Machine copies** | Whole or partial copies of a computer, phone, or app: disk images, old desktops, app exports, installers | A whole-machine, device, app, disk-image, or system-level copy, packed, with a manifest | Working files. Lab-generated snapshots and exports of one body of work: those are derived views and live beside their source (Work / ai-lab for the lab's own snapshots, AD-42). Anything needed from a machine copy is filed out to its home and the copy stays whole | replica of a machine, or historical once the machine is gone | inherited from what it holds; treated as `professional` until read, because it may hold client material |
| **Temporary** | Inbox, screenshots, downloads, scratch | Anything with an expiry | Anything referenced by a durable file | temporary | the scope of the job that made it |
| **Warehouse** | Superseded and finished material, moved out of a working tree on purpose, with a note saying what replaced it | Dated folders, add-only, each with its note | Anything current. Anything a live pointer still depends on | historical | inherited, recorded per folder |

The Warehouse area already exists for the lab at `~/Documents/_warehouse/` (settled, 2026-09-09). This file uses the same word for the same job everywhere, so there is one word. Whether Dropbox's `Archive` and `Archives` folders become the Warehouse area is a pilot question, not a rule (section 13). Inside the lab, nothing changes: the rule "never an `_archive/` inside the lab" stands, and the warehouse stays outside it.

**Depth rule.** Area, then scope where the area is split by it, then one folder per body of work. Three levels to reach a collection. Inside a collection the owner's structure is free, but the marker at the collection root governs everything below it until another marker appears (the walk-up rule, section 3). Two wide levels beat three narrow ones (P-19); the baseline's 57% single-child folders are the evidence.

**Names carry no status words** (P-11, proposed). No `-v2`, `-plus`, `-old`, `-final`, `_archive` in a new name. The marker carries status; the name carries identity. This applies to new names only. Existing names are not renamed to comply; renaming would create the moves this rule exists to prevent. Whether it ever applies backward is his call (section 12).

### 2.4 The five scope words

Settled (AD-27): `ai-lab`, `professional`, `career`, `public`, `personal`. Every marker names one. Scope is not a role and not an area; it is the boundary that says who may read and what may cross.

## 3. How a folder declares what it is

**One marker file, fixed name, at the root of every area and every collection.** Proposed name: `ROLE.md`. A fixed name is the point: a script finds every marker with one search, and a person landing in any folder reads one file. Whether `ROLE.md` is the name, or the existing `STATUS.md` in `telegraph-plus` is promoted to the job, is his call (section 12). The fields do not change with the name.

**Shape.** Same as every registry in the lab: a heading and `- key: value` lines, because the machine has no YAML reader (AD-10, settled).

```
# Telegraph plus
- id: telegraph-plus
- role: canonical
- area: work
- scope: ai-lab
- as-of: 2026-09-15
- steward: alfred-close
- declared-by: venkat
- note: the current Telegraph line; two predecessors are superseded and point here
```

**Fields.** Six are always present: `id`, `role`, `area`, `scope`, `as-of`, `declared-by`. The rest appear only when the role or state needs them:

| Field | When | What it holds |
|---|---|---|
| `canonical-at` | replica | the id of the canonical |
| `derived-from`, `built`, `rebuild` | derived | the id it was built from, the build date, the command that rebuilds it |
| `expires` | temporary | the date after which it is batched out |
| `replaced-by`, `replaced-on` | superseded by a different thing | the other id that now governs, and the date. Never the marker's own id |
| `replaces` | a new home that replaced a different thing | the old id, so the link is written in both directions. Not used for a relocation |
| `relocated-to`, `relocated-on` | the old location of the same id | where the content went, as the folder name at the time of the move, and the date. The id still resolves through the map; these fields are the dated record of the move |
| `relocated-from` | the live marker at the new location | the old location, as its folder name at the time of the move, so a relocation is written in both directions |
| `steward` | any | which routine, skill, agent, or person keeps this marker true (P-9; owner is always Venkat, so the useful field is steward) |
| `declared-by` | any | `venkat`, or `alfred-proposed`. A marker Alfred wrote is proposed until his word; it may not say canonical until then |
| `root: true` | the estate root only | the walk-up stop |
| `note` | any | one line, plain words |

**Walk-up rule** (P-10). A reader, human or script, at any path walks up to the nearest marker; that marker governs. The estate root carries `root: true`. A folder with no marker above it before the root is unfiled, which is a finding, not an error.

**Manifest.** Anything outside git, and anything packed, carries `MANIFEST.txt` beside its marker: one line per file, `hash  path`, in the shape BagIt uses (P-18, P-20). The manifest sits outside the packed object, so "is this file in there" is answered by reading one text file. Inside git, git is the manifest.

**Identity and the resolver** (P-11). An id is plain words, set once, never renamed (AD-04, settled). The resolver is a walk of the markers, written out as a derived map: one derived file that lists every id, its role, its path, its scope, its replaced-by, and its replicas. The map is rebuilt by a script, never edited, and is not a registry: it holds nothing the markers do not hold. Consumers ask the map by id, the way the source register already works (`check.py resolve <id>`). A path written into a consumer's own file is a copy that goes stale; `facts.py` holds one such copy today, the Dropbox snapshot path (section 13).

## 4. Canonical ownership

**Rule 1. One canonical per id, ever.** Two markers that both say canonical for one id is the highest-priority finding this standard produces. Nothing else is trusted until it is resolved.

**Rule 2. The canonical is chosen by home, then by context, then by date.** When copies of the same content exist and none is yet declared, the surviving canonical is:

1. the copy at the correct home under section 2, if one is there;
2. else the copy with the most complete surrounding context: the folder that holds its siblings, its provenance, its own notes;
3. else the newest by change time;
4. never a copy inside a machine copy, a temporary area, or a quarantine folder.

Where two copies differ in content, they are not duplicates. The newer one becomes canonical only by his word; until then the older keeps its place and the newer is filed beside it with its own marker. "Newer wins" is never applied automatically to a tree two machines edit (P-28).

**Rule 3. The canonical wins every conflict with its copies.** A replica whose hash differs from the canonical is refreshed from the canonical, never merged into it. A derived view that disagrees with its source is rebuilt. This is the lab's one survivorship rule (P-16), written once.

**Rule 4. Canonical is a declaration, not a discovery.** A folder is canonical because its marker says so and `declared-by` is `venkat`, not because it is the newest, biggest, or most complete copy. The baseline's career-model case shows why: three complete copies, one canonical, and the middle one was the one a reader stopped at (baseline, section 7).

**Rule 5. Canonical material never moves without a tombstone** (section 6) **and the three controls** (section 8).

## 5. Replicas, derived views, history, temporary material

**Replicas.** One direction, canonical to replica, always. A replica carries the canonical's id and `canonical-at`. It carries the canonical's authority only while its hash matches; a stale replica is used only if the output says so (P-35). A replica is not a backup (P-24): the backup is the copy no sync client can write to, and that is a storage decision, not a role.

**Derived views.** Built by a script from canonical material, named with `derived-from`, `built`, and `rebuild`. **A derived view lives in the area and scope of what it was built from** (settled 2026-09-15, AD-41, confirmed by his word in AD-42): lab snapshots belong in Work / ai-lab, role derived, never in Machine copies, which is for whole-machine, device, app, disk-image, or system-level copies. Rebuilt, never edited; overwriting by the builder is allowed because the canonical holds the truth. The lab already runs this way: the retrieval index, `context/state/CURRENT.md`, the guide folder, and the map in section 3 are all derived. A derived file whose change time is newer than its `built` date is a finding: someone edited a build.

**Historical material.** Frozen at `as-of`. Read as evidence of what was, with the register's `use` ceiling at `evidentiary` or lower; a consumer that leans on it says so in plain words. Old dated records inside it keep the paths that were true when they were written (settled; the front door's "known broken" list). The forward pointer lives in the marker and the map, never inside an old record (P-9).

**Temporary material.** Has `expires`. Nothing durable may reference it. Past its date it is batched to the Warehouse with a manifest, never deleted (the no-delete minimum). The batch is run by hand twice before any job runs it (P-21). Screenshots are the first case: 53,160 older than six months today (baseline, section 4).

**Packed collections.** A collection may give up per-item search by being packed into one archive (the icon library case, baseline section 5). Packing is a governed exemption and carries five things in its marker and manifest: the reason, the steward, the manifest outside the archive, the restore path with its expected time, and a review date (P-20). Packing is for Library and Machine copies. Work is never packed.

## 6. Supersession: how old structures point forward and stop governing

**Rule 6. Replacement is written in both directions, on the same day** (P-12). When a different thing takes over, the new home's marker says `replaces: <old id>`, and the old structure's marker says `replaced-by: <new id>` and `replaced-on`. One without the other is a finding. A `replaced-by` that names the marker's own id is a fake replacement and a finding.

**Rule 6a. Relocation is written in both directions, with the same id on both ends** (his word, AD-42). When the same thing moves, the old folder keeps its marker with the same id, `role: historical`, `relocated-to: <new location>`, and `relocated-on: <date>`. The live marker at the new location adds `relocated-from: <old location>`. No `replaces` or `replaced-by` is written, because nothing was replaced. A location is named by its folder name at the time of the move; identity stays the id. The map pairs the two by id: a `relocated-to` with no live marker for that id, a `relocated-from` with no old marker behind it, or a location name that does not match the other end is a finding.

**Rule 7. One hop** (P-12, RFC 6596 in the brief). `replaced-by` names the current canonical, never another superseded thing. When a chain forms, every older marker is updated to point at the end. The map walks every chain and reports any longer than one hop, any that ends at a non-canonical id, any loop, and any pointer to an id that does not exist. The career model's chain, broken at hop two for five days while a check said "81 records valid," is the case this rule closes.

**Rule 8. Every old location keeps a tombstone.** When content moves, the old folder is left holding only its marker, with `relocated-to` and `relocated-on`. When a different thing took over and the content stays frozen, the marker says `role: historical` plus `replaced-by`. Either way the marker is the loudest thing in the folder, or the only thing. A tombstone is never removed.

**Rule 9. A superseded structure stops governing.** Nothing new is written into it. A script proves this: any file under a superseded marker with a change time after `replaced-on` or `relocated-on` is a finding. Consumers that resolve by id are already pointed at the new home; consumers that hold a path copy are found by the same check and listed for repair.

**Rule 10. Old records are never edited to look current.** History is corrected by a new dated line that names what it corrects (settled; the decisions file's own rule).

### 6.1 Adoption: how a new structure becomes the one in use

**Rule 15, adoption** (the foundry lesson, baseline amendment F). A structure is adopted, and becomes the one in use, only when all five hold on the same day: its root marker says canonical with `declared-by: venkat`; a dated decision row names it; the structure it replaces carries `replaced-by` (rule 6); the map is rebuilt and reports no duplicate canonical for that family; and consumers that resolve by id get the new path. Until all five, it is a candidate, and the map says so. After all five, a write into the old structure is a finding (rule 9). A structure with `activation.approved: false` for three weeks is what this rule prevents.

## 7. What moves, and what stays and is referenced

**Default: stay.** Mark in place. A move is undoable but never free, and every move creates a tombstone, a manifest, a receipt, and a stale-path risk.

Move only when staying costs something real:

- it would sit inside a working tree that agents walk or sync clients count, and it is large (the count rule, P-19);
- it is client-confidential and the tree it sits in is a repository or a publishing path (settled: that is why the warehouse is outside the lab);
- it has been replaced whole and its presence beside the current one has already caused a misread (the two "Documents" folders; the three career-model copies);
- it is a machine copy or temporary material past its expiry.

Otherwise it stays, gets a marker, and is reached by id. Referencing is one line in a marker or the map; moving is section 8.

## 8. Filing and duplicate removal, in that order

The baseline recorded two controls held and one skipped, at a cost that cannot be recovered (section 8 there). This standard makes the order a rule.

**Rule 11. Home first, then copies.** No redundant copy is removed until the canonical home is declared (marker, `declared-by: venkat`) and the canonical copy is in it. Duplicate removal that runs before a home exists can only reduce; it cannot organize, and it can remove the last good copy (the two skips in the baseline that saved a 21.7 GB and a 13.0 GB archive).

**Rule 12. Three controls on every mutating operation, named separately** (P-26):

1. **Baseline before.** A manifest of what exists, with hashes, kept outside the tree being changed. Terraform's state backups "cannot be disabled"; neither can this.
2. **Revalidate at each write.** Each move or removal re-checks that both the retained copy and the redundant copy still exist with the expected hash, and skips on any mismatch. A skip is a normal outcome, not a failure.
3. **Verify after, both directions.** A new manifest, reconciled against the baseline: every planned move landed, every source that should be gone is gone, nothing unplanned changed, hashes match. The output is the receipt.

Around them: a dry run first, a reverse recorded per move, one writer per tree while a run is in progress, and copy, verify, remove, never `mv` (settled).

**Rule 13. Completeness is proven per file, never per folder name** (P-27). A claim that can only be proven at folder level is written at folder level.

**Rule 14. Removed copies are quarantined, not deleted.** They go to a dated folder in the Warehouse with the manifest that names their canonical. The three underscore folders in Dropbox today (`_DUPLICATES-EXACT-2026-09-13` and its two siblings) are that pattern already; under this standard they carry a marker and sit in the Warehouse area.

**The procedure, end to end.** Declare the home. File the canonical copy in (controls 1 to 3). Rebuild the map. Quarantine hash-identical copies (controls 1 to 3 again). Re-scan: the finding "copies of `<id>` outside its canonical" must come back absent. That re-scan, not a receipt line, closes the job (Operational DNA: resolved is a sensor's word).

## 9. What constrains organization

Each of these is a lab rule already in force. This section says what it does to filing. None is restated.

| Constraint | What it means for organization |
|---|---|
| **Operating Scope** (AD-27) | Every marker names one scope. Work is split by scope at its second level, so a client folder is a folder boundary a script can refuse, not a tag a model must notice. Technical access is not permission to use |
| **Privacy and client boundaries** | Professional-scope material never sits in a repository or a publishing path. Machine copies are treated as professional until read. Nothing client-named goes into a public or lab tree, which is why the warehouse is outside the lab |
| **Trust** | Role lowers the ceiling, never raises it: historical and temporary are at most evidentiary; Library is at most contextual; a replica has its canonical's authority only while hashes match. The register's `use` words are the only trust words (no new vocabulary, AD-38) |
| **Authority** | Declaring canonical, setting `replaced-by`, moving, quarantining, adopting, and accepting a finding are his word. Alfred writes the line on his word. A marker with `declared-by: alfred-proposed` may not say canonical. The three safety minimums stand: no deletes, nothing external, no secrets |
| **State** | The marker on the object owns its role and supersession; the map is derived from markers; State's ledger holds overlays only for things that have neither a marker nor a registry field (AD-37: registries stay canonical, State stores what they do not own). One fact, one home |
| **Context** | Context assembly reads the map, never walks the tree. It filters on scope, role, and `as-of`, and refuses historical or temporary material unless the job asks for history (P-34) |
| **Evidence** | Manifests, move logs, and receipts are the evidence and live in the shared record (`evidence/receipts/`, DriveAtlas for the estate). No ledger per area |
| **Process** | Every consequential change is one bounded goal with the three controls and a re-scan, in the existing shape: operational spec, one goal, one review (AD-33) |

## 10. What AI does here, and what it may not do

**AI does five jobs**, each ending in a proposal:

1. **Classify.** For an unfiled folder or a new item: propose area, scope, role, and the nearest existing collection, with the evidence it read and its confidence. Write the marker as `declared-by: alfred-proposed`.
2. **Relate.** Find that two folders are one body of work; find copies that are not hash-identical but are versions; propose `replaces` and `replaced-by` links; propose which copy should survive under rule 2.
3. **Read drift.** The script lists three lists (declared but missing, present but undeclared, present but different). The AI says which items threaten a driver and which are noise, and raises materiality with a reason, never lowers it (AD-11).
4. **Recommend placement.** For a new item at creation time, one answer: area, folder, role, and why.
5. **Maintain.** Propose expiries, packing candidates, marker updates when a folder's contents have changed character, and the standard changes below.

**AI may not, on its own:** move, rename, delete, quarantine, set or change `role: canonical`, set `replaced-by`, adopt a structure, accept a finding, or widen a scope. Each is his word, recorded. This is the same line the lab already holds for sources (AD-21: a session cannot widen what retrieval may depend on).

**The dangerous mix, named** (Operational DNA, property 8). A filing agent reads private data (client material), reads untrusted content (whatever is in the estate), and would write. All three together is the mix to avoid. Resolution: the classifier reads and proposes only, with no write tool; the executor writes markers and runs moves only from an approved plan, with revalidation at each write, and has no external communication. No single agent holds all three.

**Standard changes** (proposed; widening agent authority is his word, P-2). A written list of what an agent may do without asking, each local, reversible, and receipted:

- write a proposed marker on a folder that has none;
- rebuild any derived view, including the map;
- batch expired temporary material to the Warehouse with a manifest, once the batch has been run by hand twice;
- quarantine hash-identical copies of a declared canonical, under the three controls.

Everything else is a normal change: plan first, his go.

## 11. What a script proves

Sensors report, never fix (settled). Each check is proven able to fail before it counts (settled). Findings carry the seven fields and three materiality levels (AD-11) plus a baseline state, new, unchanged, or absent, computed against the last run (P-50). A finding closes only when its own check reports it absent (P-5).

| Check | Finding | Materiality |
|---|---|---|
| two canonical markers for one id | duplicate canonical | interrupt |
| a `replaced-by` chain longer than one hop, ending at a non-canonical id, looping, naming an id that does not exist, or naming the marker's own id | supersession drift | show at open |
| a `relocated-to` marker whose id has no live marker, a live `relocated-from` with no old marker behind it, mismatched location names between the two ends, a relocation loop, or a marker carrying both `relocated-to` and `replaced-by` | relocation drift | show at open |
| `replaces` without matching `replaced-by`, or the reverse | one-way supersession | show at open |
| a file changed after `replaced-on` or `relocated-on` under a superseded marker | write into a superseded structure | show at open |
| a replica whose hash differs from its canonical | replica drift | show at open |
| a derived file newer than its `built` date | hand-edited build | show at open |
| a folder under Work with no marker between it and the root | unfiled | record only, until it is written into |
| temporary material past `expires` | expired | record only |
| a consumer file holding a path that the map says is superseded | stale path copy | show at open |
| a packed collection missing any of its five exemption fields | ungoverned exemption | show at open |
| a canonical marker with `declared-by: alfred-proposed` | unconfirmed canonical | interrupt |

**Where the checks live.** First form, 2026-09-15: `.claude/skills/context-check/role-map.py`, a walk of markers under one or more roots with the checks above and ten planted-fault tests beside it. Inside the existing sensors from there, not a new platform: `dead-pointers.py` grows from "does the path resolve" to "does it resolve to a marker without `replaced-by`" (this is the replace verdict in the brief, section 11); `context/sources/check.py` already tests `canonical-at` and gains the map as an input; `facts.py` carries one line: markers found, findings by level, checks run, seconds taken (P-51). No new registry, store, or platform.

**Evaluation of the AI part.** A frozen set of 20 real items from the estate, each with the area, scope, and role two readers agreed on, code-graded: the classifier's proposal matches or it does not. Grown only from real misfilings. Changed only by his word (settled, AD-22 and AD-37 for the pattern). Plus one planted case per kind: an item with not enough context to classify must come back as "cannot place, here is what is missing," not a guess (P-36).

## 12. Open decisions

His calls. Each names what waits on it. **Settled 2026-09-15 02:51 (AD-40):** items 1 (`ROLE.md`), 3 (Warehouse everywhere), and 5 in part (agents may write proposed markers and rebuild derived views; batching and quarantine stay his go). Items 2, 4, 6, and 7 are still open.

1. **The marker file's name.** `ROLE.md` as proposed, or `STATUS.md` promoted. Everything in section 3 waits on it; the fields do not change.
2. **Whether `docs/architecture/` is this file's home.** One move if not.
3. **The Warehouse word for Dropbox.** Same word everywhere as proposed, or Dropbox keeps `Archive` for the same job. Two words for one job is the thing this file exists to prevent, so my read is one word.
4. **Whether "no status words in names" applies backward.** Proposed: new names only, tombstones for the rest.
5. **The standard-changes list** in section 10. It widens agent authority.
6. **The sync shape for two Macs plus Dropbox, the immutable backup's home, the Time Machine fix, which classes are local on which Mac, and the canonical node per class.** These are the brief's open decisions 1 to 5 and the baseline's decisions 2 to 4. This standard requires only that the answer is written once as a five-row table (class, canonical node, mirrors, backup, last verified restore; P-23). It does not pick the values.
7. **The routine count and the disposition of the superseded lab** (baseline decision 5). Not organization questions; listed so they are not lost.

None of these creates two different durable standards. The vocabulary, the marker shape, the ordering rule, and the supersession rules hold under every answer.

## 13. The next pilot: one bounded Dropbox area

**Candidate: the two Dropbox folders that hold the lab's snapshot files**, `my-ai-lab/` and `my-ai-lab-backups/`, at the top of the Dropbox account. Observed today, read only:

| Folder | Files | Newest |
|---|---|---|
| `my-ai-lab/` | 3 (one tar, one manifest, one checksum) | 2026-09-08 |
| `my-ai-lab-backups/` | 3 (same shape) | 2026-09-10 |

**Why this one.** It is small (six files), hash-provable, and reversible. It exercises every rule in this file on real material: one class of information with two homes (rule 1); a role that is not obvious, derived from the lab, not a replica of it, because a tar is built by `snapshot.sh` (section 5); a canonical home to declare and one folder to tombstone (rules 6a and 8); the three controls on a move (rule 12); a consumer holding a path copy, `facts.py` line 72, which the map should replace with an id (section 3); and an open follow-up, five days old, already waiting on his name pick (F-20260910-1349-4). It touches the second driver, "my work survives the loss of any one machine," so a mistake matters and would be caught: the lab itself is canonical, in git, and pushed.

**What the pilot would prove.** That two readers file the same six files the same way from this document alone; that a tombstone plus map makes the old folder unreadable to a consumer within one open routine; that the drift check catches a planted second canonical; and that the facts-sheet line survives the move by id, not by path.

**Runner-up.** `Archive/` and `Archives/`, two top-level Dropbox folders with one job: the first live case of rule 1 at the top level, and the place the Warehouse-word decision gets tested.

**Not changed.** Nothing in Dropbox was touched to write this section. Both folders and their six files are exactly as found.

## 14. Two readers, six items

The test the goal asks for: can two readers place these without a second vocabulary?

| Item | Area | Scope | Role | Canonical? |
|---|---|---|---|---|
| A new client deck, in progress | Work / professional / `<engagement>` | professional | canonical | yes, the working copy |
| A screenshot taken today | Temporary | the job's scope | temporary, `expires` in 180 days | no; nothing durable may point at it |
| The purchased icon library, packed | Library | ai-lab | canonical, packed, five exemption fields | yes, low authority |
| The lab's snapshot tar in Dropbox | Work / ai-lab, beside the lab (his word, AD-42: lab snapshots are Work / ai-lab, role derived) | ai-lab | derived, `derived-from: my-ai-lab`, `rebuild: snapshot.sh` | no; the lab is |
| The middle career-model folder (`my-ai-lab-v2/brand-identity/model/`) | stays where it is, or Warehouse; section 7 says stay unless it misleads again, which it did once | career | historical, `replaced-by: career-model` | no |
| `context/state/CURRENT.md` | Work / ai-lab / the lab | ai-lab | derived, `derived-from: state`, `built:` each close | no |

No row has a choice left. The snapshot row had one until the pilot; AD-42 settled it.

## 15. Operational DNA

Recorded here as the standard requires (LAB-OPERATING-MODEL.md section 16). The component is this standard's mechanisms: the marker, the map, the ordering rule, the checks.

- **Job:** OWN. One answer to where a thing belongs, which copy is real, and what state it is in, for Dropbox, the estate, and the lab.
- **Scope:** INHERIT the Operating Scope contract (AD-27); every marker carries one of its five words.
- **Process:** OWN. Declare, file, verify, remove, re-scan; adoption and supersession as written in sections 6 and 8.
- **State:** INHERIT. The marker on the object owns role and supersession; State's ledger holds only what has neither a marker nor a registry field (AD-37).
- **Context:** INHERIT. Context assembly reads the derived map and filters on scope, role, and date; this standard supplies the fields, not the assembly.
- **Evidence:** INHERIT evidence-record and DriveAtlas: manifests, move logs, receipts. No ledger per area.
- **Trust:** INHERIT the register's `use` words; a role lowers the ceiling, never raises it. No new vocabulary.
- **Authority and control:** INHERIT authority (the three minimums, the root lock) and OWN the short list of what is his word (section 10). Dangerous mix named and split across two agents.
- **Experience:** OWN. A person gets one answer to "where does this go," one to "which is real," three lists of drift, and a short list of what needs his word. No tree walking, no path hunting.
- **Evaluation and learning:** OWN. Eleven checks proven able to fail; a frozen 20-item filing set; a cannot-place case. Learning grows the set from real misfilings and never moves a canonical.

**Portfolio lens:** NONE BY DESIGN. Filing changes no goal, capacity, asset, or commitment. The estate's reliability touches driver 2, which is a storage decision (section 12, item 6), not this standard.

**Removal test, answered in section 1.** Remove AI and the scripts still hold; the filing goes back to a person and the estate re-nests.

**Anti-bloat check.** Nothing new is created to satisfy the standard: no registry (the map is derived from markers), no store, no agent, no folder tree (six areas are named, none is built here), no schema beyond `- key: value` lines the lab already uses, no trust words, no approval step beyond his existing word.

## 16. Every Step 2.5A problem, and where it lands

| Problem the brief raised | Treatment here, or why not here |
|---|---|
| Supersession one-directional; existence-only canonicality check; career-model chain broken at hop two | Rules 6 to 9 (6a for a relocation); the `dead-pointers.py` replace in section 11 |
| No folder declares itself | Section 3, the marker and walk-up rule |
| Names carry status words | Section 2.3, new names only; open decision 4 |
| Derived views marked but nothing refuses a hand edit | Section 5 and the "hand-edited build" check |
| No fixed tombstone name, so no script can list them | Rule 8: the marker is the tombstone |
| Two "Documents" folders; three career-model copies | Rule 1, rule 4, section 7; the lab's move out of iCloud closed the first case (baseline, amendment D) |
| Duplicate removal ran before a home existed; baseline capture skipped once | Rules 11 to 13; the three controls as one rule |
| 723,197 redundant objects; count binds, not bytes | Rules 11 and 14, P-19 in the depth rule; per-machine sync count is open decision 6 |
| Icon-library exemption with no fields | Section 5, packed collections, five fields; the "ungoverned exemption" check |
| 53,160 old screenshots, no rule | Section 5, temporary material, 180 days, hand-run twice |
| 57% single-child folders; 25% of files under uninformative names | Depth rule; the "unfiled" check; collapse only in Work, on the pilot's evidence, never the stock corpora |
| Foundry operating model stalled at the adoption gate | Section 6.1, rule 15: adoption is five conditions with a date and a consequence, not a flag |
| Closure by a person, not a re-scan; accepted findings with no expiry | Section 11, baseline state and closure by absence; expiry on acceptance belongs to the Governance standard, not here |
| Registry standard enforced on three of seventeen registries | Outside this standard. It belongs to the Registries standard of Step 2.5B |
| Specialist identity, budgets, handoffs; evaluation kinds | Outside this standard, except the filing agent's tool split and its frozen set. Belongs to the Specialist Agents and Evaluation standards |
| Time Machine, sync shape, immutable backup, canonical node per class | Open decision 6; this standard requires the five-row table and picks no value |
| The "76%" sentence in the front door | Outside; Governance or Evaluation standard |
| `currentphase` sensor verb | Outside; storage sensors, with open decision 6 |

## 17. Sources

This file cites the brief by principle number (P-n, its section 12) and the baseline by section. The brief's section 16 holds the 342 source rows; none is re-cited here. Settled rulings are cited by decision number from `ARCHITECTURE-DECISIONS.md`. Where this file and a later ruling disagree, the ruling governs.
