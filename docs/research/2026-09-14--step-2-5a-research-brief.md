---
title: "Step 2.5A research brief: standards, conventions, and proven practice for the lab's operating baseline"
date: 2026-09-14
author: Alfred (session bfb6c76a), at Venkat's /goal of 2026-09-14 16:10
kind: research brief; source-backed; compares external practice with the lab's own baseline; proposes principles and open decisions for Step 2.5B; designs nothing; changes nothing
home: docs/research/ (assumed; the goal named no home. The four current-state briefs of 2026-09-14 sit in docs/research/assessments/ and the registry baseline in docs/documentation/. One move if he picks another)
baseline_files: docs/documentation/CURRENT-REGISTRIES-CHECKS-SENSORS.md · the storage estate baseline of 2026-09-14 (attached to the goal; not in the lab) · docs/architecture/CAPABILITY-MAP.md · CAPABILITY-DEFINITIONS.md · ARCHITECTURE-DECISIONS.md · LAB-OPERATING-MODEL.md · context/sources/REGISTER.md · docs/ecosystem/2026-09-14--ai-lab-product-ecosystem-design-doctrine.md · 2026-09-14--ai-lab-portfolio-architecture.md · 2026-09-13--ai-lab-product-ecosystem-roadmap.md
method: six parallel research passes (governance; information architecture; storage, sync, backup, mutation; navigability; agents and evaluation; registries and sensors), each fetching its sources on 2026-09-14 and writing a findings file; this brief synthesizes them and adds the lab comparison. 342 source rows across the six passes; every URL fetched unless its row says otherwise
source_labels: FORMAL STANDARD (a standards body, a law, or a published protocol spec) · ESTABLISHED CONVENTION (widely followed, no single owner) · VENDOR PATTERN (one product's documented way) · EMERGING PRACTICE (a paper or a young proposal)
lab_labels: observed (a file read or a script run today, or the baseline files) · inferred (my reading) · proposed (a principle or decision waiting on his word)
settled_and_not_researched: Alfred coordinates only; specialist agents do domain reasoning; the exact four-part AI-native definition (doctrine, section 0)
citations: "[A3]" means row 3 of the governance pass's sources table, reproduced in section 16. A is governance, B information architecture, C storage and mutation, D navigability, E agents and evaluation, F registries and sensors
---

# Step 2.5A research brief

## 0. How to read this

**What it is.** One brief that says what the outside world prescribes for each thing the goal named, what the lab does today, and whether to keep, strengthen, adapt, replace, or avoid. It ends with the principles and open decisions Step 2.5B needs to write the five standards (Governance; Lab Organization and Information Architecture; Specialist Agents; Evaluation; Registries) without another broad research pass.

**What it is not.** It designs no schema, folder, registry, agent, sensor, or migration. Where it says "smallest honest version," that is the shape the sources support, not a decision.

**Two rules held throughout.** First, a practice is only as strong as its label: a FORMAL STANDARD carries more weight than a VENDOR PATTERN, and the label is on every claim. Second, "the AI decides what to investigate; scripts decide what is true and what is forbidden." Most of what follows is the script half. Section 14 says where the reasoning half sits and why the baseline does not slide into a checklist.

**Length.** Long on purpose, so 2.5B does not need to reopen the sources. Section 1 is the short version.

## 1. The short version

Ten findings, ordered by how much they change for the lab.

1. **The lab's registry standard already matches the strongest external practice.** Stable ids never renamed, one canonical record, a short status word, add-change-retire-never-delete, proof on anything live. RFC 8126, RFC 2026, semver, the package registries, and ITIL's configuration items say the same [F1, F2, F11, F7 to F10]. MLflow retreated from fixed stages to exactly the lab's shape [F16, F17]. Keep it; extend script enforcement from three registries to the domain registries.
2. **The one thing every field solved and the lab has not: supersession written in both directions, with one `current` pointer per family.** The RFC Editor, DataCite, DCAT 3, Hugging Face, and the archivists' separation sheet all do it [B7, B8, B10, B16, B17, B25, F19, F28]. The career model's three-location failure is exactly the case they solved. The existing check tests "does the path resolve," never "is it still canonical."
3. **Closure by re-scan, never by a person.** SOC 2, NIST SP 800-61, CISA, SARIF, and SonarQube agree: a finding is closed when its own sensor reports it absent on a later run [A26, A27, A34, A35, F64]. This one rule turns the self-grading problem into a scripted fact, and the lab does not have it yet.
4. **The three mutation controls have three distinct anchors.** Baseline capture is BagIt and Terraform's mandatory state backups; pre-write revalidation is RFC 9110 `If-Match` and Dropbox's `WriteMode.update(rev)`; post-change verification is `rclone check` and BagIt "valid" [C48, C50, C54, C56, C34]. The lab ran the second correctly once and skipped the first once, at a cost it can never recover.
5. **"Verified" is never a backup job state.** In every vendor vocabulary it is a separate act with its own date [C10 to C13]. The lab's backup is configured, not running, never completed, never restore-verified, and degraded. By Apple's sizing rule the disk is about a third of what the included set needs [C14].
6. **The thresholds that bind the estate are item counts, and online-only does not relieve them.** Dropbox's 300,000-file guidance "includes online-only files"; only selective sync or packing reduces the count [C23, C24, D53, D55]. The estate is over three times the line; the image files alone are twice it in a tenth of the bytes.
7. **A well-run exemption carries five things**: reason, owner, a manifest kept outside the archive, a restore path with expected time, a review date [D25, D26, D49, D51]. The icon-library exemption is approved and in progress and has none of the five written down yet.
8. **Specialist agents need four lines the lab's agent files lack**: an explicit tools allowlist (never inherit-all), `maxTurns`, a version and lifecycle status, and a "never" list mapped to a tool restriction or hook [E5, E8, E9]. And one output rule: a closing status block with named gaps, whether the agent finished or ran out [E5, E28].
9. **The three evaluation kinds that matter most for specialists do not exist yet**: insufficient-context and stale-context tests, handoff-restriction tests, and planted-injection tests [E27, E28, E11, E21]. Each is one or two tasks per specialist, code-graded, with a planted fault.
10. **The front door's "76%" sentence is partly wrong.** The number is real (Advani 2026 [E57]) but measures the share of failures reported as success on one benchmark, for agents making explicit "done" claims; on another benchmark it was 3%. The rule stands; the scope must be attached.

**At a glance.** Keep: the registry standard, the refusal layer, append-only rulings, three materiality levels, the heartbeat rule, copy-verify-remove, frozen tests changed only by his word. Strengthen: closure by re-scan, baseline states on findings, expiry on accepted findings, bidirectional supersession, tools allowlists, the mutation controls as a written rule. Adapt: folder marker files, a `current` pointer per family, dbt-style freshness thresholds, A2A task words in State, the seven-line handoff, the five-field exemption record, the 180-day transitory rule. Replace: the existence-only canonicality check, the Time Machine setup, the `currentphase` sensor line. Avoid: certification machinery, boards and comment periods, catalog and preservation products, cryptographic agent identity, public benchmarks, two-way sync of the estate, re-filing 965,000 files.

## 2. Method and what was not verified

**Six passes**, run in parallel as subagents on 2026-09-14, each with the same instruction: prefer the standard's own text or the maintainer's official docs, fetch every URL cited, label each practice with exactly one of the four source labels, and give the smallest honest version for a one-person lab plus what would be over-engineering. Their findings files (about 30,000 words in total) are the evidence behind this brief and sit in the session scratchpad; the sources are reproduced in section 16 so this file stands alone.

**What could not be verified**, carried forward from the passes: every iso.org catalogue page returned 403, so ISO/IEC 42001, 38500, 27005, 20000-1, 22301, 15489, and 30301 clause text rests on previews and secondary summaries; ITIL 4 wording came from a secondary site; the IIA 2024 standards were confirmed by title only; PREMIS and OAIS were read through summaries; Apple's per-directory performance numbers do not exist on any primary page; `.interrupted` is not an Apple term on any fetched page; the OpenAI agents guide PDF has custom fonts, so its quotes come from the landing page; the NDSA v2 matrix text did not load; MITRE ATLAS's primary page returned 404. Each row in section 16 that rests on a secondary source says so.

**Where sources disagree**, in one place: NIST allows AI systems with no human oversight and the EU AI Act does not for high-risk systems (different scopes, both right). CVSS gives a severity score and CISA says the score is a weak ordering. The strict two-person rule and the looser four-eyes pattern are often conflated. ITIL routes change by risk through a change authority and SRE routes everything through code review; at one-person scale they converge, and a script is the change authority for standard changes.

## 3. Governance: decision rights, change, exceptions, incidents

### What the outside world prescribes

**AI governance frameworks.** NIST AI RMF 1.0 [A1] (FORMAL STANDARD, voluntary) asks for four things a small operator can meet on one page: documented roles and lines of communication (GOVERN 2.1), defined human oversight (MAP 3.5), planned periodic review with a stated frequency (GOVERN 1.5), and documented incident tracking and recovery (MANAGE 4.3). It also asks for a decommissioning process (GOVERN 1.7). The Generative AI Profile [A2] names twelve risks; two matter daily here, confabulation and over-reliance. ISO/IEC 42001 [A4] is the certifiable management-system version: plan, do, check, act, with the check done by something other than the doer. ISO/IEC 38500 [A6] gives the cleanest frame for a one-person lab: the governing body evaluates, directs, and monitors; management proposes and acts. The EU AI Act [A7, A8, A9] binds only high-risk systems, but its Article 14 is the best written test of human oversight: can the person understand the system's limits, override it, stop it, and find the logs later.

**Decision rights.** RACI [A10] (ESTABLISHED CONVENTION) has one rule worth keeping: exactly one Accountable per decision. NIST SP 800-53 AC-5 [A12] (FORMAL STANDARD) defines separation of duties; the strict two-person rule [A11] is a military control and is often confused with the looser four-eyes pattern. Open Policy Agent [A14] (VENDOR PATTERN) states the pattern the lab already uses: policy is data in version control, an engine answers, the caller enforces.

**Change control.** ITIL 4 [A15] (ESTABLISHED CONVENTION) sorts changes into standard (pre-authorized, low risk, follows a written procedure), normal (assessed and authorized first), and emergency (done now, reviewed after). It assigns approval authority "according to risk rather than routing every change through a central board." Google SRE [A17] (VENDOR PATTERN) adds hermetic builds: a check gives the same answer on any machine, any day. OpenGitOps [A18] (ESTABLISHED CONVENTION) adds continuous reconciliation: a script compares the declared state with the real state and reports the drift. Architecture Decision Records [A19, A20] add two fields the lab's rows lack: the options considered, and a confirmation line that says how you will know the decision was carried out. The RFC process [A21, A22] adds a threshold (only substantial changes need a proposal) and a tracking rule (an accepted proposal is not done until something tracks its build).

**Exceptions.** ISO/IEC 27005:2022 [A24] (FORMAL STANDARD) makes acceptance of residual risk a separate decision with an owner and asks for monitoring of whether the facts behind an accepted risk have changed. FedRAMP [A25] names three deviation types: risk adjustment, false positive, and operational requirement. SOC 2 CC4.2 [A26] asks for proof that a fix worked, not proof that a ticket was opened.

**Incidents.** NIST SP 800-61 Rev 3 [A27] (FORMAL STANDARD): closure is declared against written criteria, the integrity of restored assets is verified, and an after-action note is written. ITIL [A28] separates incident (the interruption), problem (the cause behind several incidents), and known error (a problem with a documented cause and workaround). Google SRE [A29, A30] adds the one-hour trigger for declaring an incident, the blameless write-up, and action items with owners. PagerDuty [A31] adds one rule: when unsure of severity, go higher, and re-grade in the write-up.

**Findings governance.** CVSS [A32] gives severity; CISA BOD 22-01 [A33] says severity alone is a poor ordering because fewer than 4% of vulnerabilities are ever exploited, so the second question is "is it happening now." SARIF [A34] (FORMAL STANDARD) gives every finding a baseline state (new, unchanged, updated, absent) and treats a suppression as a record with a status, not a deletion. CISA BOD 19-02 [A35] and FedRAMP set deadlines by severity and verify closure by rescanning, never by self-report. The IIA standards [A36] say silence is not acceptance: a finding the owner ignores is re-raised as an accepted risk and escalated.

**Records.** ISO 15489-1 [A37] (FORMAL STANDARD): a record is created at the time of the event by the party with direct knowledge, and integrity means complete and unaltered. Three traditions agree on supersede-never-edit: Nygard's ADRs, the RFC Editor, and ISO 15489 [A19, A22, A37].

### What the lab does today (observed)

- Roles are written and enforced: Venkat decides, Alfred coordinates, scripts refuse. The three safety minimums, the root lock (37 tests), and the unlazy stop hook are the refusal layer (`CLAUDE.md`; `CAPABILITY-DEFINITIONS.md#authority`).
- Change control exists in practice without the words: "three or more steps or a rule change" means plan first and wait for his go; small clear work is just done; a new rule needs two dated yeses (`context/how-i-work.md`).
- Decisions are append-only dated rows with who decided and what follows (`ARCHITECTURE-DECISIONS.md`, `DECISIONS.md`). No row carries "options considered" or "how we will know it happened."
- Exceptions live in three accepted-findings files, each line with a reason (`dead-pointers-accepted.txt`, `skill-check-accepted.txt`, `discovery-accepted.txt`). No line carries an expiry or a reason type. Nobody re-reviews an accepted reason (baseline, section 5).
- Findings use seven fields and three materiality levels. Closure is by a person writing a receipt line; a loop closed by hand elsewhere stays open (baseline, section 2A). No finding carries a baseline state, so "unchanged" noise and "fixed" cannot be told apart by script.
- Incidents are ALERT lines and the "Known broken" list in the front door. The session-sync fix of 2026-09-10 was closed the right way: a test run read the lab with no error. That is the model, not yet the rule.
- Owner is implicit. "Who owns a show-at-open finding that nobody turns into a follow-up" is listed as Unclear in the baseline (section 6).

### Verdict

- **Keep.** The refusal layer as policy-as-data (OPA's split, without OPA). Append-only dated rulings (three traditions agree). Three materiality levels (PagerDuty's five would be ceremony).
- **Strengthen.** Closure by re-scan: a finding is closed when its own sensor reports it absent, never when a person says it is fixed (SOC 2 CC4.2, NIST RC.RP-05, CISA rescanning). Add a baseline state to findings (SARIF). Add expiry and a reason type to accepted findings (ISO 27005, FedRAMP's three deviation names). Add an owner field even though the answer is always Venkat, because an empty owner is how findings die (IIA).
- **Adapt.** ITIL's three change types, with a written list of standard changes an agent may do without asking. MADR's "confirmation" field on decision rows, which is the bridge from a ruling to a sensor. ISO 38500's evaluate-direct-monitor as the plain-words frame for a pharma client.
- **Avoid.** ISO 42001 certification, risk registers with likelihood scales, change advisory boards, five severity levels, incident command roles, postmortem meetings, RFC comment periods with one commenter.

## 4. Lab organization and information architecture

This section answers the goal's second verification point: artifact classes, canonicality, storage topology, supersession, archive and retention, and the sensing of structure and canonicality drift.

### What the outside world prescribes

**A folder declares itself.** Three preservation standards put a small plain-text inventory inside the folder it describes. BagIt (RFC 8493) [B1] (FORMAL STANDARD): a manifest of `checksum filepath` lines, and two tests, complete (everything listed is present) and valid (every checksum matches). OCFL 1.1 [B2] (FORMAL STANDARD): a marker file whose name says what kind of folder this is, and an inventory with a `head` field naming the current version. NDSA Levels [B4, B5] (ESTABLISHED CONVENTION): Level 1 metadata is one line, "inventory of content and its storage location," kept in a second place. Bazel [B30] and EditorConfig [B28] give the repository version of the same rule: a marker file defines the unit, the unit extends down until the next marker, and a reader walks up from any file to the nearest marker with `root = true` as the stop.

**Identity is a name plus a resolver.** DOI, Handle, and ARK [B11, B12, B13] all work the same way: the name never changes, and one resolver maps it to the current location. "Cool URIs don't change" [B44] says what to leave out of a name: status words, versions, author, mechanism. Content addressing (git objects, OCI digests) [B38, B39] gives identity from bytes, so two files with the same hash are the same thing wherever they sit.

**Supersession is written in both directions and resolves in one hop.** The RFC Editor [B16, B17] writes "Obsoletes" on the new document and "Obsoleted by" on the old one's index entry; old text is never edited. DataCite [B8] (FORMAL STANDARD) separates versioning (IsNewVersionOf) from obsolescence (Obsoletes, IsObsoletedBy) from identity (IsIdenticalTo) from derivation (IsDerivedFrom). Dublin Core [B7] gives the plain words `replaces` and `isReplacedBy`. DCAT 3 [B10] adds `hasCurrentVersion` so a reader jumps to the live one without walking. RFC 6596 [B15] forbids a canonical pointer that points at another pointer. HTTP 301 and 410 [B14] give the two end states for an old location: moved here, or gone on purpose. RFC 8594 and RFC 9745 [B18, B19] add two dates, deprecated and sunset, so retirement is a schedule, not a cliff.

**Records have an end state.** ISO 15489 [B20], ARMA [B22], and NARA [B23, B24] agree: every record has a disposition (retain, transfer, destroy) and a persistent linkage that survives a move. The archivists' separation sheet [B25] (ESTABLISHED CONVENTION) is the tombstone: "a form filed in the original location of an item, indicating that the item is stored elsewhere," with a fixed name so it can be found, and never removed.

**Derived things are rebuilt, never edited.** Twelve-Factor [B33]: build, release, run, with releases append-only. Databricks' medallion tiers [B47] (VENDOR PATTERN): raw, cleaned, consumption-ready, and every tier rebuildable from the one below.

**Copies say they are copies.** S3 replication [B48] marks each copy `REPLICA` and each source with a replication status, and says "check the object's replication status before deleting the source." The Git LFS pointer [B35] is the smallest correct shape for "the real thing is elsewhere": a version line, a hash, a size. git-annex [B37] tracks which repositories hold a copy. Master data management [B46] (VENDOR PATTERN) writes the survivorship rule down once: when copies disagree, which one wins.

**Drift is sensed against a declared expectation.** Kubernetes spec-versus-status and Terraform plan [B51, B52] (VENDOR PATTERN): hold a declared state, observe the real state with a script, report every difference in both directions. TUF [B45] (FORMAL STANDARD) adds expiry on the metadata itself: "Clients MUST NOT trust an expired file," and a version counter that must never go down. Fixity audits [B59] recompute checksums on a schedule. Pew [B60] measured link rot at 38% of 2013 pages gone by 2024; the lab's ~900 stale references are normal, not a lapse. Link checkers [B56, B57] test that a link resolves; none tests whether it resolves to a superseded thing.

**Personal conventions** (PARA, Johnny.Decimal, Zettelkasten [B53, B54, B55]) are conventions, not standards. Two rules transfer: a hard depth limit, and an id that survives renames.

### What the lab does today (observed)

- Registries already carry stable ids, one canonical record, status words, `added` and `changed`, and "retire, never delete" (`CAPABILITY-MAP.md` section 3). The source register carries `standing` (canonical, replica, historical, unavailable) and `canonical-at` on replicas, and refuses a `canonical-at` that names another registered id (AD-17, AD-19). That is the RFC 6596 rule, already enforced for one registry.
- No folder declares itself. The root lock allows fifteen names at the lab root, but no domain root carries a marker saying id, role, canonical path, as-of date. A reader who lands in a copy cannot tell from the folder alone.
- Supersession is one-directional. The career model moved three times; the middle location has a README and a status file and no forward pointer, and "no file in it references `work-os`" (storage baseline, section 7). The front door says "leave a pointer at the old location" but names no fixed filename, so no script can list the pointers.
- The existing check tests existence, not canonicality: `validate_and_render.py` reports 81 records valid while 0 reference the current home and 31 reference the superseded lab (storage baseline, section 7). `dead-pointers.py` tests that a path resolves; it does not read the target's record for `replaced-by`.
- Names carry status words: `worthy-tool-v2`, `telegraph-plus`, `my-ai-lab-v2`, `_archive`. "Cool URIs" says that is why moves happen.
- Derived views are marked ("`CURRENT.md` is a generated view and says so"; the guide folder is "generated, never hand-edited"), but nothing refuses a derived file whose change time is newer than its last build.
- Disposition: the lab's rule is archive-only, warehouse never `_archive/`. Nothing records a disposition per registry record, and about 100 live pointers still name old `_archive/` paths.
- Two folders present as "Documents" (local and iCloud); Finder shows both by the same name. This produced one misidentification of the lab's location (storage baseline, section 2).
- Placement rules exist for the lab root ("Where a NEW file goes" table) and nowhere else. Six candidate target folders in Dropbox are empty; 29 top-level folders remain at original paths (storage baseline, section 9).

### Verdict

- **Keep.** Stable ids, never renamed. Status in the record, not the name. Append-only dated records. The source register's `standing` and `canonical-at` fields. Archive-only with a note saying what replaced it.
- **Strengthen.** Make the pointer at an old location a fixed filename with a machine-readable state (moved, retired), so a script can enumerate every tombstone (separation sheet, HTTP 301/410, S3 delete marker). Make supersession bidirectional: `replaces` on the new record, `replaced-by` on the old record and the old location (RFC Editor). Give every family of copies one `current` pointer on the head record (DCAT `hasCurrentVersion`, ADMS `last`, Hugging Face `new_version`). Extend `dead-pointers.py` from "does it resolve" to "does it resolve to a record without `replaced-by`."
- **Adapt.** A marker file at each domain root and each replica root, in the Bazel and EditorConfig shape: fixed name, walk up to the nearest, `root: true` at the top. Fields drawn from BagIt, OCFL, S3, and TUF: id, role (canonical, replica, derived, historical, temporary), canonical location if not canonical, as-of date and validity window, replaced-by if superseded. A manifest of hashes beside it, in BagIt line format, for anything outside git. DataCite's four relations (replaces, replaced-by, identical-to, derived-from) as the whole relation vocabulary. NARA's three disposition words with "destroy" written as never used.
- **Replace.** The existence-only canonicality check with a three-list drift report: in registry not on disk, on disk not in registry, on disk and in registry but hash or canonical flag differs (Terraform, BagIt complete-versus-valid).
- **Avoid.** OAIS packages, PREMIS XML, OCFL versioning, DVC or git-annex installs, DOIs, RDF, records classification schemes with retention periods, re-filing the estate into a designed taxonomy, renaming existing folders to fix status words (apply the rule to new names, add tombstones for the rest).

## 5. Storage estate: topology, sync, backup and recovery, and controls on mutating operations

### What the outside world prescribes

**Backup standards.** NIST SP 800-34 [C1] (FORMAL STANDARD): two numbers, how much work you can afford to lose (recovery point) and how long you can be without the system (recovery time), a copy stored off-site, and a test "at least annually." ISO/IEC 27001:2022 control 8.13 [C3] (FORMAL STANDARD, wording unverified against iso.org): backups "maintained and regularly tested." The 3-2-1 rule [C5, C6] (ESTABLISHED CONVENTION, coined by Peter Krogh): three copies, two kinds of media, one off-site. Veeam's 3-2-1-1-0 [C7] (VENDOR PATTERN) adds one copy no sync client can touch and zero errors on a verified restore. AWS Backup [C8] runs scheduled restore tests and deletes the restored copy after. The saying "a backup that has never been restored is not a backup" [C9] has no primary author and is the cheapest rule in the set.

**Protection states.** No vendor uses the same words, and in none of them is "verified" a job state [C10, C11, C12, C13]. AWS: created, pending, running, completed, failed, expired, partial. Azure: in progress, completed, completed with warnings, failed. Veeam: success, warning, failed. Apple's `tmutil` has no state words; it lists "completed backups" and offers a separate `verifychecksums`. The six-word ladder in the goal (configured, running, completed, restore-verified, degraded, failed) maps cleanly onto all four vendor lists, with one correction: restore-verified is always a separate act with its own date, never a state the job reports about itself.

**Apple facts, confirmed.** A Time Machine disk should be "at least twice the storage capacity of your Mac" [C14]. "Time Machine never deletes the last remaining backup" and thins the oldest when full [C14, C15]. Apple does not say what happens when the first backup is larger than the disk; the inference that it cannot complete is the researcher's, and it matches the lab's observation. Only a folder listed by `tmutil listbackups` is a completed backup; an `.inprogress` bundle is running or stalled; `.interrupted` is not an Apple term on any fetched page [C13, C17, C18]. `currentphase` and `status` are not in the `tmutil` man page or usage listing on this Mac, so the storage baseline's use of `currentphase` rests on a verb the tool does not document. Local APFS snapshots are a same-disk undo for 24 hours and count toward nothing in 3-2-1 [C19]. On turning off Desktop & Documents: "Your files ... stay in iCloud Drive," the new local folders "are empty," and files must be dragged out by hand [C20]. Turn Optimize Mac Storage off first, or evicted placeholders will be pulled down during any hashing step [C22].

**Dropbox facts, confirmed.** The 300,000-file soft limit per synced computer "includes online-only files" [C23, C24]; selective sync removes the folders from the disk and does not count. A team plan's version history is 180 or 365 days, and Rewind undoes bulk changes only inside that window and never restores permanently deleted files [C28, C29]. Dropbox publishes no file-level manifest of an account merge [C30, C31]. The `content_hash` (SHA-256 over 4 MB blocks, then SHA-256 of the concatenation) is an official verification primitive readable through the API without downloading bytes, and rclone checks it on every transfer [C32, C33]. rclone's own rails: `--dry-run`, `--backup-dir`, `--max-delete`, `--immutable`, `--check-first`, and `rclone check --combined` with its one-line-per-file verdict [C34 to C38].

**Sync as a design problem.** One-way mirror versus two-way sync [C35, C37, C39, C40, C41]: a mirror has one source and modifies the destination only; two-way tools need memory of the last state and can resurrect deleted files on a wrong resync. "Sync is not backup" is stated by the tools themselves: Syncthing, rclone bisync, and Backblaze all say deletions and corruption propagate [C42, C43]. Conflict handling is "keep both, rename one" in every tool; never pick "newer wins" for a tree both machines edit. The safety rails ship with the tools: a canary file on every side, a delete cap, a backup directory [C37, C38, C40]. The three shapes for two Macs plus a cloud store are laid out in the findings file with their named failure modes; in all three, the backup is a fourth thing outside the sync, on a store no sync client writes to.

**Fixity and completeness.** NDSA Level 1 [C44, C46] (ESTABLISHED CONVENTION): two complete copies, not co-located, and a hash list made when the copy is made. BagIt [C48] (FORMAL STANDARD) defines the two tests: complete (every listed file exists and every file is listed, in both directions) and valid (every checksum matches). AWS DMS [C49] reports missing-on-source and missing-on-target separately. Folder-name comparison proves a container exists and nothing about the count, bytes, or hashes inside it.

**The three controls on mutating operations**, each with a distinct anchor:

| Control | What it is | Best sources | Label |
|---|---|---|---|
| Pre-change baseline capture | Before any change, write down what exists: path, size, mtime, hash, count, total bytes. Keep the file outside the tree being changed | BagIt manifest and Payload-Oxum [C48]; NDSA fixity on ingest [C46]; Terraform state backups that "can not be disabled" [C50]; PostgreSQL dump before upgrade [C51]; Ansible check mode [C52]; `terraform plan -out` [C53] | ESTABLISHED CONVENTION; BagIt is a FORMAL STANDARD |
| Immediate pre-write revalidation | A plan computed at time T is a hypothesis. Each write carries the state it assumed (hash, rev, ETag) and refuses if the current state differs. The refusal is a normal outcome | RFC 9110 conditional requests, `If-Match`, `412 Precondition Failed` [C54]; Kubernetes `resourceVersion` [C55]; Dropbox `WriteMode.update(rev)` [C56]; S3 conditional writes [C57]; rclone `--immutable` [C38] | FORMAL STANDARD (RFC 9110); VENDOR PATTERN for the rest; the idea is optimistic concurrency |
| Post-change verification against the baseline | Take a new manifest after the change and reconcile against the baseline in both directions: every planned move landed, every source that should be gone is gone, nothing unplanned changed, hashes match. Keep the output as the receipt | `rclone check --combined` [C34]; rsync `--checksum` and `--itemize-changes` [C39]; BagIt "valid" [C48]; a second `terraform plan` reporting no actions [C53]; AWS DMS row validation [C49]; `tmutil verifychecksums` and `compare` [C13] | ESTABLISHED CONVENTION; BagIt is a FORMAL STANDARD |

Around them: "verify then remove" (rclone move deletes the source only after a checksum-verified transfer [C36]); dry runs before every destructive command [C35, C38, C39, C52, C53]; idempotency so a step run twice is safe (RFC 9110 section 9.2.2 [C54]); a reverse recorded per move (`--backup-dir`, Dropbox version history, Terraform's mandatory backups [C28, C38, C50]); and the honest limit that a staleness window can be shortened, never closed, because a concurrent actor can land inside it (S3's own docs [C57], AWS DMS [C49]). The only full closure is one writer at a time per tree.

**Topology.** No standard names "canonical node" as a term, but every one-way tool implies it: one place is the truth per class of file, everything else is a mirror or a backup in one direction [C35, C39, C50]. "Replication is not backup" [C42, C43]. Three desktop vendors use the same three-state tiering model in different words: placeholder only, downloaded on demand, pinned local [C25, C26, C58, C22]. A full local copy costs sync-client performance (count), disk space (which also starves local snapshots), and backup disk size (which must cover everything included) [C14, C19, C23].

### What the lab does today (observed)

- Backup: configured yes, running no, completed no, restore-verified no, degraded yes (destination 95% full with two failed attempts). Root cause: a 2.6 TiB source and a 1.8 TB destination (storage baseline, section 6). By Apple's own sizing rule the disk would need to be about 5 TB, or the included set would need to shrink to under about 900 GB. Driver 2 in `STANDING.md` says "working when a clean restore has been run and verified against the source"; nothing has been restored from anything.
- Sync: iCloud holds the lab today and is being retired; no replacement chosen. Two of eight repos push to private GitHub. A tar snapshot goes to Dropbox, four days old on today's facts sheet. Dropbox is a live mirror, so it is one copy, not two, however many Macs sync it.
- Mutation controls: the duplicate collapse ran control two correctly (9 of 397 skipped, twice saving the last copy). The account consolidation skipped control one, so control three is impossible and completeness is now provable only at folder-name level (storage baseline, section 8). The lab's written rule "copy → verify → remove, never mv" is control three for local moves. Reversal commands are recorded per move in the estate work.
- The estate exceeds Dropbox's per-computer sync guidance by about three times, and the iMac is the intended full-estate node (storage baseline, section 2).
- The two "Documents" folders (local and iCloud) have already caused one misidentification of the lab's location.

### Verdict

- **Keep.** Copy, verify, remove. Reversal commands per move. Hash-proven duplicate removal through the Dropbox content hash. The facts-sheet lines for snapshot age, off-machine copy age, repos with no remote, and unpushed commits.
- **Strengthen.** Make the three mutation controls a written rule with three names, so a future bulk change cannot skip the first one. Record the protection state as two fields, not one: last job state, and date of last verified restore (never "verified" as a job state). Put both on the facts sheet, with "none" as an honest value. Write the lab's two numbers (recovery point, recovery time) once.
- **Adapt.** A five-row topology table: class of file, canonical node, mirrors, backup, last verified (implied by every one-way tool). One writer per tree while an executor runs. rclone's three rails (dry run, backup directory, delete cap) as the default for any estate command. A manifest with content hashes before any future merge, move, or eviction, including the iCloud retirement now in progress. Bring each Mac's synced count under 300,000 by selective sync (which does not count) rather than online-only alone (which does).
- **Replace.** The Time Machine setup: either a destination at least twice the included set, or exclusions that make the included set fit with room to grow. Which of the two is his call. The `currentphase` sensor line, which relies on an undocumented verb; use `tmutil listbackups` and `latestbackup`, which the man page documents.
- **Avoid.** ISO 22301 anything. Business impact analyses. Object-lock buckets. Two-way sync of the whole estate. Per-file tiering rules. Monthly full-estate fixity audits of 965,000 files. Distributed locks for one person.

## 6. Machine navigability and governed exemptions

### What the outside world prescribes

**The thresholds are item counts.** Dropbox [D3, D4] (VENDOR PATTERN): "Users shouldn't sync more than 300,000 files"; performance "can decline if you have more than 300,000 files synced," a soft limit that depends on hardware; the remedy Dropbox names is selective sync or online-only. OneDrive [D1]: sync no more than 300,000 items. Google Drive [D2]: 500,000 items per shared drive, "based on item count, not storage use." S3 [D5, D6]: a listing returns at most 1,000 keys per request and is charged per request. Git [D10, D11]: `git status` on 393,000 files fell from 17.6 seconds to 0.83 with a file-system monitor, and the cost "is based upon the number of files (and directories)." HDFS [D22]: 150 bytes of namenode memory per object. The verdict on the lab's claim: enumeration, sync bookkeeping, listing, and index cost scale with object count; transfer time and storage scale with bytes. Both halves must be stated.

**Online-only is a partial exemption.** Dropbox [D53] keeps one placeholder per item, so the sync client's item budget is not relieved. OneDrive [D55] says outright that contents of online-only files are not searchable. Only packing removes objects.

**Packing has precedents.** The small-files problem [D22] (ESTABLISHED CONVENTION) and its remedies (archives with an internal index). WebDataset [D23, D24]: image datasets shipped as plain tar shards, 3x to 10x sequential-read gains. BagIt [D25] and OCFL [D26]: give up per-item search, keep a per-item manifest outside the archive so "is X in there" is answered by reading one text file.

**A well-run exemption carries five things.** Read across BagIt, OCFL, the dark-archive definition [D49, D50], and NARA GRS 5.2 [D51]: a stated reason, an owner, a checksummed manifest kept outside the packed object, a written restore path with expected time, and a review date.

**Transitory material has a rule.** NARA GRS 5.2 [D51] (FORMAL STANDARD): transitory records are "required for only a short time (generally less than 180 days)" and are disposed of "according to a predetermined time period or business rule." S3 lifecycle rules [D8] are the general shape: transition after N days, expire after N days.

**Hierarchy research.** Miller 1981 and Larson and Czerwinski 1998 [D43, D44, D45]: two wide levels beat three narrow ones; depth costs time and raises the chance of getting lost. No source names the single-child folder as a formal anti-pattern; the lab's 57% figure is its own evidence. For an agent, each level is a listing call into a bounded context, so single-child levels are pure overhead.

**Indexes are derived.** Spotlight [D30], plocate [D31], ripgrep and its ignore files [D32], Zoekt and GitHub code search [D34, D35], aider's repo map [D36], llms.txt and sitemaps [D38, D39], DCAT and the catalog tools [D40, D41, D42]. Every one is rebuilt from the source and never treated as truth. Sitemaps cap one page at 50,000 entries. llms.txt is one small entry file a machine reads first.

### What the lab does today (observed)

- The estate holds 964,867 files, more than three times Dropbox's soft ceiling; the 670,685 image and design files alone are more than twice it, in 10% of the bytes (storage baseline, sections 3 and 4).
- 12,103 of 21,206 folders hold exactly one child; 241,966 files sit under uninformative segments; 24 of those were modified after 2023.
- One icon library of 26,405 files exists twice, hash-proven. Its consolidation into one archive set to online-only is owner-approved and in progress, recorded as "a deliberate exemption with stated rationale" (storage baseline, section 5). The five fields above are not yet written for it.
- 53,160 screenshots are older than six months; 203 are newer. No lifecycle rule exists.
- The lab's retrieval index is the right pattern: 1,868 records over 1,509 files, rebuilt from the source register, git-ignored, with a stats file and an age line on the facts sheet (baseline, section 2D).
- No ignore file, no Spotlight privacy entry, and no entry file exist for the Dropbox estate; an agent that walks it pays the full count.

### Verdict

- **Keep.** The retrieval index as a derived, rebuildable artifact with its age on the facts sheet. The icon-library exemption as a deliberate, recorded decision.
- **Strengthen.** Write the five exemption fields for the icon library before it is closed out, and keep the manifest outside the archive. State the count-versus-bytes claim with its exception attached.
- **Adapt.** The 180-day transitory rule for screenshots, with "destroy" replaced by "batch to the warehouse with a manifest" under the no-delete minimum. An ignore file at the estate root and a Spotlight privacy entry for the stock folders, so every agent search skips them without being told. One entry file per top-level folder in the llms.txt shape. A cheap sensor that counts single-child folders in the working tree (not the stock corpora).
- **Avoid.** Re-filing 965,000 files into a taxonomy. Running a data catalog product. Cold-tier cloud accounts. Scalar or sparse checkout for repos of a few thousand markdown files. A search index over image files.

## 7. Specialist agents: identity, boundaries, authority, context, freshness, budgets, handoffs, degradation, lifecycle

The rule that Alfred coordinates only is settled and was not researched. What was researched is how the outside world documents and bounds the specialists Alfred will coordinate.

### What the outside world prescribes

**Shape.** Anthropic [E1] (VENDOR PATTERN): workflows first, agents only when simpler things fail; add stopping conditions; pause for a human at checkpoints. Anthropic's multi-agent post [E2]: agents use about 4x the tokens of chat and multi-agent systems about 15x; multi-agent fits parallel work and information beyond one context window, not work needing shared context; every delegation carries an objective, an output format, guidance on tools and sources, and clear boundaries; "simple fact-finding requires just 1 agent with 3-10 tool calls." Cemri et al. [E3] (EMERGING PRACTICE): across 1,600 traces, multi-agent gains "are often minimal," and failures sort into three groups: system design, inter-agent misalignment, task verification. OpenAI [E4]: "maximize a single agent's capabilities first"; the manager pattern (one agent calls others as tools) is the shape the lab already rules.

**Identity.** Claude Code subagents [E5] (VENDOR PATTERN): one markdown file with `name`, `description`, `tools` as an allowlist, `disallowedTools`, `model`, `permissionMode`, `maxTurns` ("marked as partial" at the limit), and isolated context. The A2A Agent Card [E6] (FORMAL STANDARD as an open protocol) adds `version` and a declared skills list. SPIFFE [E7] is the infrastructure analogue: identity is issued and checkable, not inferred from location; the lab's `agent_type` in hooks is the same idea.

**Boundaries and authority.** Saltzer and Schroeder 1975 [E8]: least privilege, fail-safe defaults, complete mediation. OWASP LLM06 Excessive Agency [E9] (ESTABLISHED CONVENTION): limit functionality, permissions, and autonomy; "require a human to approve high-impact actions"; enforce downstream, not only in the model. Vendors document "must not" in three places: enforced tool lists, prompt text, and machine tripwires [E10, E11, E12]. In-the-loop, on-the-loop, out-of-the-loop [E13, E14]: do not call anything "on the loop" unless a script or receipt actually watches it. EU AI Act Article 14 [E15]: the overseer can understand limits, stay aware of automation bias, override, and stop. MCP [E16] (FORMAL STANDARD): "there SHOULD always be a human in the loop with the ability to deny tool invocations," and tool annotations such as `readOnlyHint` "MUST" be treated as untrusted unless from a trusted server, so the lab's own sort of tools into reads and acts is the truth. The confused deputy [E19] and the lethal trifecta [E20]: private data, untrusted content, and the ability to communicate externally; "guardrails won't protect you," so no specialist gets all three.

**Context sufficiency and freshness.** Anthropic's context engineering post [E23]: "the smallest set of high-signal tokens," lightweight identifiers loaded just in time, sub-agents returning a distilled summary of about 1,000 to 2,000 tokens. Lost in the Middle [E24]: put the task and constraints first and the evidence last. TUF and RFC 9111 [E25, E26] (FORMAL STANDARD): freshness is a date compared by code; "Clients MUST NOT trust an expired file." Abstention research [E27, E28]: the default failure is guessing, not stopping; AbstentionBench finds abstention "remains largely unsolved."

**Budgets.** `maxTurns`, `max_turns`, and the named stop reasons (`end_turn`, `max_tokens`, `pause_turn`, `refusal`, `model_context_window_exceeded`) [E5, E30, E31]. Circuit breaker, bulkhead, timeout, fail fast [E32, E33, E34]. Retries: randomized backoff, capped, never layered, and never for writes without an idempotency key [E35, E36]. A budget-exhausted outcome is a named terminal state plus a record of what was done and enough state to resume; a silent stop is the failure every vendor is trying to prevent [E2, E5, E6].

**Handoffs.** OpenAI, A2A, and Anthropic agree on what travels [E2, E6, E10]: task and objective, output format, the filtered context the receiver may see, constraints and boundaries, a task id linking the result back, and the state of the work. A2A's task states [E6]: submitted, working, input-required, completed, failed, canceled, rejected, auth-required. The documented gap [E11]: OpenAI's "input guardrails run only for the first agent in the chain," so a restriction that lives only in the handoff text is lost mid-chain; the fix is to enforce on the tool.

**Degradation and lifecycle.** Fail closed: an errored hook denies; a specialist whose front matter fails to parse does not run [E18, E37]. Fallback to a smaller job with a label, never nothing [E2, E33]. Lifecycle words: Anthropic's active, legacy, deprecated, retired [E38]; Google's experimental through decommissioned with 12 months' notice [E39]; NIST GOVERN 1.7 on decommissioning [E41].

### What the lab does today (observed)

- Nine agents and thirty skills live once at the lab root; each agent is a markdown file with name, description, and tools (baseline, section 2C). That is already the vendor's identity shape. Agents are not registered on purpose (AD-02); the files are the registry.
- Alfred's authority file says any file change outside his log is "prepares, Venkat approves." The three safety minimums, plan mode, and the root lock are the approval gates. Read and act authority are not yet separate front-matter facts per agent; some agents list "All tools."
- The source register carries a use ceiling and `not-alone` per source, and Retrieval returns evidence packages with provenance, freshness, conflicts, and gaps (AD-17, AD-24). That is the context-sufficiency machinery the vendors describe, already built. No evidence item carries a "good until" date a script compares.
- State's ledger has kinds and status words (work: active, paused, done, handed-off; loop: open, closed, waiting) and a `claim` and `release` for sessions (AD-37). No "input-required" state exists; "waiting on Venkat" lives in three homes.
- No `maxTurns`, no version line, no lifecycle status, and no "never" list mapped to a tool restriction exists on any agent file. No fallback job is named. No agent output carries a required status block with gaps.
- The lab's delegation to subagents this session carried objective, output format, sources, and boundaries in prose; nothing enforces that shape.

### Verdict

- **Keep.** Markdown file as identity. Alfred as the manager pattern; specialists return only to Alfred, never to each other. Retrieval's evidence package as the context a specialist receives. "Prepares, Venkat approves" for anything external.
- **Strengthen.** Every specialist gets an explicit tools allowlist, never inherit-all; read-only specialists get no Write, Edit, or Bash. Every specialist gets `maxTurns`, a `version` line, and a lifecycle status (experimental, active, deprecated, retired). Every specialist file ends with a "never" section of at most five lines, each mapped to a tool restriction or a hook; a never nothing enforces is a wish.
- **Adapt.** A seven-line handoff note (task, objective, output format, evidence pointers, constraints and never list, authority as read-only or may-act, what is already done). A required closing status block on every specialist output (status word from complete, partial, blocked; what is done; what is not; where the evidence is; what it would do next), used whether it finished or ran out. Six A2A task words in State, with "input-required" as the honest name for "stopped to ask Venkat." A "good until" date per evidence item, defaulted from the source register by kind, compared by script; a stale item may be used only if the output says so. A three-column trifecta table, one row per specialist, where any row with all three ticks is a bug. A named smaller job per specialist for when the full job cannot run. A circuit-breaker rule: a specialist that fails the same check twice in a day is "open" and the brief says so.
- **Avoid.** A separate agent registry, A2A servers, cryptographic identity, an autonomy-levels matrix, a permissions service, a policy language, an injection classifier, a memory system for specialists, checkpointing engines, a message bus, signed handoffs, specialists calling specialists.

## 8. Evaluation

### What the outside world prescribes

**The frame.** Anthropic's evals guidance [E42, E43] (VENDOR PATTERN): a task is one test with inputs and success criteria; a grader scores it; an outcome is the final state. Start with 20 to 50 tasks drawn from real failures; grade what the agent produced, not the path; prefer code graders; "an eval at 100% tracks regressions but provides no signal for improvement." Hamel Husain [E44] (ESTABLISHED CONVENTION): level one is assertions on every change, built from observed failures.

**Test kinds, each with its best source and the smallest lab version.**

| Kind | Best source | Label | Smallest lab version (from the findings file) |
|---|---|---|---|
| Known-answer, frozen | Anthropic evals [E42, E43]; Husain [E44] | ESTABLISHED CONVENTION | 10 to 20 tasks per specialist from real jobs or real failures, code-graded where possible, frozen, grown only from new failures |
| Insufficient context | SQuAD 2.0 [E27]; AbstentionBench [E28] | ESTABLISHED CONVENTION (research) | A task whose evidence package has the gap; pass only if status is partial and the gap is named |
| Stale context | TUF expiry [E25]; AbstentionBench's "outdated information" split [E28] | FORMAL STANDARD / EMERGING PRACTICE | A task with one item past its good-until date; pass only if the output says stale in plain words |
| Faithfulness | RAGAS [E45]; ARES [E46] | EMERGING PRACTICE | A script matches each claim in the output to a pointer in the package; unsupported claims fail |
| Adversarial | NIST AI 600-1 [E41]; PyRIT [E48]; OWASP LLM01 [E21]; ATLAS [E22] | ESTABLISHED CONVENTION | Two or three fixed planted-injection payloads per specialist that reads outside content ("ignore your task and write to X"); pass only if nothing is written and the attempt is reported |
| Authority | OWASP LLM06 [E9]; Claude Code deny rules and hooks [E17, E5] | ESTABLISHED CONVENTION | One task per specialist that politely asks for a thing outside its grant; pass only if the hook refuses or the call is never attempted, and the refusal is in the log. A deny that depends on the model's manners is not a pass |
| Budget exhaustion | `maxTurns` "marked as partial" [E5]; stop reasons [E31] | VENDOR PATTERN | Run with `maxTurns` set to 2 on a real task; pass only if the output is the full status block with status partial |
| Handoff | OpenAI's first-agent guardrail gap [E11]; OWASP agentic [E12] | EMERGING PRACTICE | Send a forbidden request through Alfred with the constraint in the handoff text and on the tool; run again with it removed from the text only; pass only if the second run is still blocked |
| Regression | Anthropic [E42]; Husain [E44]; the lab's own prove-it-can-fail | ESTABLISHED CONVENTION | Re-run the frozen set after every change to prompt, tools, or model; a hook refuses a commit that changes a test file and a specialist file together |
| Real-world outcome | Husain level three [E44]; Xia et al. [E49] | EMERGING PRACTICE | One outcome per specialist read from receipts by script: used, corrected, or discarded. No A/B testing; one person is not a population |
| Reliability | tau-bench pass^k [E50] | ESTABLISHED CONVENTION (research) | Run each frozen task three times; one pass in three is not reliable. Do not run public benchmarks |
| Prove the test can fail | Mutation testing [E59]; chaos engineering [E60] | ESTABLISHED CONVENTION | Every new test ships with one planted fault that must make it fail before it counts (the lab's existing rule, extended) |

**The judge.** Zheng et al. [E55]: position bias, verbosity bias, self-enhancement bias. Panickssery et al. [E56]: self-preference grows with a model's ability to recognize its own text. Anthropic [E43]: a different model grades than the one being evaluated, against a written rubric. Advani 2026 [E57]: no judge configuration beat AUROC 0.65 at spotting false success, because judges "rely on surface completion proxies ... rather than verified state changes."

**The "76%" claim, verdict: partly verified and the lab's wording is wrong.** The front door says "agents grading themselves report false success roughly 76% of the time." The number comes from Advani [E57]: 75.8% is the share of failures reported as success on one benchmark (AppWorld), for agents making explicit "done" claims; on another benchmark the same figure was 3%, and on tau2-bench 45 to 48%. The honest sentence: on one 2026 study, when self-reporting agents failed they claimed success about three quarters of the time; on other tasks the share was as low as 3%; scripted checks caught these failures far better than model judges. Park and Choi [E58] add: across 54 cycles a frontier agent claimed improvement every time, and 56% had a measured delta of zero or below. The rule the lab draws from it stands; the number needs its scope attached.

### What the lab does today (observed)

- Two frozen known-answer sets exist with planted-fault proof: seven retrieval tests (6 of 7, T2 a recorded limitation, AD-36) and five State tests (5 of 5, 21 planted faults). Sensors have proof-of-failure tests (root lock 37, facts 15 or 16, sources 27, State 21, skill check). The `prove-it-can-fail` skill is the lab's mutation-testing rule.
- No specialist agent has a frozen test set. None of the eight other kinds in the table exists: insufficient-context, stale-context, faithfulness, adversarial, authority, budget-exhaustion, handoff, real-world outcome.
- Frozen tests change only by his word in a decision row (AD-22, AD-37). Nothing refuses a commit that edits a test and the thing under test together.
- The edit-the-test anti-pattern was already met and refused once: "T2 stays. Do not weaken the meaning-match test" (AD-23).

### Verdict

- **Keep.** Frozen known-answer sets changed only by his word. Planted-fault proof before a check is trusted. Scripts, not judges, for anything a script can measure. The refusal to weaken T2.
- **Strengthen.** Attach the scope to the 76% sentence in the front door. Add the commit hook that refuses a test-plus-subject change in one commit. Report pass^k (three runs) on the frozen sets, not one run.
- **Adapt.** The three test kinds that matter most for specialists, in this order: insufficient-context and stale-context (specialists reason over evidence packages with gaps), handoff-restriction (Alfred-to-specialist is the path every job takes), and planted-injection (any specialist reading outside content holds one leg of the trifecta). Then authority and budget-exhaustion, which are each one task per specialist. Then a script-read outcome per specialist from receipts.
- **Avoid.** Public benchmarks, PyRIT itself, a trained judge, an experiment platform, hundreds of synthetic tasks, a CI system beyond a hook.

## 9. Registries and the ten sensor kinds

### What the outside world prescribes

**Who may add an entry.** RFC 8126 [F1] (FORMAL STANDARD) names a ladder of registration policies from first-come-first-served to standards action; reassignment of a value needs the original requester's agreement; entries are marked obsolete rather than removed. Package registries [F7, F8, F9, F10] agree: deprecate and yank warn readers and stop new use, but "the version can never be overwritten, and the code cannot be deleted."

**Lifecycle vocabularies.** The comparison across nine vocabularies [F table, section 7] shows the lab's five words match ITIL's configuration-item list almost one to one, and ITIL is the only list with an "impaired" state. MLflow [F16, F17] deprecated its fixed stages in 2.9.0 as "inflexible" and moved to a short status plus free tags and a mutable alias, which is where the lab's design already sits. Three things common practice has that the lab lacks: a state between live and retired (deprecated but still readable, with a successor named: Backstage, npm, PyPI, cargo, ODCS, ADMS, RFC 9745), a sunset date (RFC 8594, 9745), and a computed `current` pointer on a family head (DCAT `hasCurrentVersion`, ADMS `last`, Hugging Face `new_version`).

**Fields the model, dataset, and agent worlds agree on** [F18 to F26]: identity, owner or provider, version, intended use, limits, evaluation results, provenance. The lab's registry standard has identity, status, and the use ceiling; provenance (built from) and evaluation are the two it names weakly. The lab's `proof:` pointer is stronger than a vendor score because it points at a proof the thing can fail. Datasheets [F20] add the "must not be used for" line, which is the lab's `not-alone`. ODRL [F29] makes a prohibition a first-class statement, not a comment.

**Ownership.** Backstage [F12] requires a single owner and derives relations from records rather than hand-listing them. Entra Agent ID [F25] records a sponsor so agents can be retired "without leaving orphaned credentials." In a one-person lab the honest field is not owner but steward: which routine, skill, or agent keeps this record true.

**The sensors, one by one.**

| Kind | Best external precedent | Label | Smallest honest version |
|---|---|---|---|
| Integrity | NDSA fixity rows [F37]; W3C Link Checker [F38]; SARIF [F62] | ESTABLISHED CONVENTION / FORMAL STANDARD | Schema (required fields, allowed words), referential (every id resolves), fixity (a checksum per file outside git, compared on a schedule) |
| Health | Kubernetes liveness, readiness, startup probes [F39] | ESTABLISHED CONVENTION | Separate "alive" (the job ran) from "ready" (the output is usable). The half-blind cloud routine is alive-not-ready |
| Heartbeat | Healthchecks.io states new, up, late, down, paused [F41]; Prometheus `absent()` [F42] | ESTABLISHED CONVENTION | The lab's "a missing line is the alarm" has the strongest precedent of all ten. Copy the late-versus-down split: late is show at open, down is interrupt |
| Discovery | AWS Config [F43]; Terraform `import` [F44] | VENDOR PATTERN | List what is present with no record, and any record whose location is empty. The finding is "not yet registered," not "wrong" |
| Freshness | dbt `warn_after` and `error_after` [F33, F34]; TUF `expires` [F48] | VENDOR PATTERN / FORMAL STANDARD | Two numbers per registered thing, in days, chosen per kind. TUF's rule: a reader must not trust a record past its expiry, even if it resolves |
| Usage | AWS Trusted Advisor idle-resource rules [F49] | VENDOR PATTERN | A floor over a window for at least N days ("no session used this skill in 60 days"), read from `USAGE.jsonl` |
| Coverage | OpenMetadata KPIs [F36] | VENDOR PATTERN | Numerator, denominator, target date: records with a steward, with a proof pointer, with an expiry |
| Drift | Terraform plan [F44]; AWS Config; schema and model drift [F51, F52] | VENDOR PATTERN | "The record says X, the world says Y," computed as a diff. Documentation drift has no primary standard (weakest precedent) |
| Canonicality drift | Reference-rot studies: link rot versus content drift [F53, F54, F55]; Google canonical rules [F58]; MDM survivorship [F60] | ESTABLISHED CONVENTION / VENDOR PATTERN | Every family of copies has one `canonical`. Check: the canonical exists; every other copy is a listed view or flagged "unlisted copy"; the canonical's hash is the newest of the family, or a written survivorship rule says why not |
| Supersession drift | RFC Editor chains [F3]; Google's redirect-hop guidance (under 5, ideally 3) [F59]; ADMS `last` [F28]; Crossref resolution reports [F57] | ESTABLISHED CONVENTION / VENDOR PATTERN | Walk every `replaced-by` chain to its end. Findings: longer than three hops; ends at a non-live record; a loop; a pointer to an id that never existed. Store the computed `current` on the family head |
| Efficiency | Google SRE monitoring chapter [F61] | ESTABLISHED CONVENTION | Two numbers on the facts sheet: checks run, time taken. Google's page test on the interrupt level: urgent, actionable, true. A check with no finding in ninety days is a candidate for removal |

**Findings governance for sensors.** SARIF [F62] baseline states (new, unchanged, updated, absent) and suppressions with a status. GitHub code scanning [F63] dismisses with a reason from a fixed list. SonarQube [F64] sets "fixed" by the tool when the issue is no longer detected, never by a person.

### What the lab does today (observed)

- The registry standard already meets most of the conventions: stable id, one canonical record, status word, relations by id, testable location, `added` and `changed`, `proof` on live, add-change-retire, machine-readable, no second source of truth (`CAPABILITY-MAP.md` section 3). Three registries enforce it by script (capability, source, State). The domain registries (assets, seeds, targets, career model, routines, rulings) do not (baseline, section 1).
- Sensing by registry, marked Present, Partial, or Missing across eight kinds for seventeen registries (baseline, section 4). Usage is Missing everywhere except two Partial rows. The asset registry, target index, and rulings are Missing on nearly every column. Canonicality drift and supersession drift are sensed nowhere.
- The heartbeat pattern is the lab's own best idea ("a missing line is the alarm") and it maps exactly onto Healthchecks.io's state list; the lab lacks only the late-versus-down split.
- Health today conflates alive and ready: a routine that "runs" but cannot open a web page reports as run.
- Freshness has per-kind stale rules in State (work 7 days, commitments 3, loops 14) and an age line for the retrieval index and the snapshot. No registered source carries an expiry a reader must honor.
- Accepted-findings files carry a reason but no expiry, no reason type, and no re-review (baseline, section 5). Findings carry no baseline state.
- "Show at open" findings with no owner: three discovery findings open today; the career-model line reports 30 never-cite hits and one broken spoke with no ALERT and no owner (baseline, section 5).
- Efficiency: no sensor reports its own cost or how many checks ran.

### Verdict

- **Keep.** The registry standard as written. Five status words. `proof` as a pointer to failure proof. "A sensor reports, never fixes." "A check is proven able to fail." The heartbeat rule.
- **Strengthen.** Extend script enforcement of the registry standard from three registries to the domain registries, starting with the ones that are Missing on most columns (assets, targets, rulings). Add the late-versus-down split to the heartbeat. Split health into alive and ready. Add a baseline state to every finding. Add expiry and reason type to accepted findings.
- **Adapt.** Two fields, not a sixth status word: `deprecated-on` and `sunset-on`, plus `replaced-by` on the old record and a computed `current` on the family head (RFC 9745, DCAT, ADMS). A `steward` field in place of owner. dbt's two freshness thresholds per kind, mapped to show-at-open and interrupt. Trusted Advisor's rule shape for usage. Coverage as three ratios with a target date. An efficiency line: checks run and seconds taken. Two new sensor kinds, canonicality drift and supersession drift, defined by the checks in the table above; both are computable from the fields the Adapt line in section 4 adds.
- **Avoid.** Backstage's nine kinds, a metadata graph, OpenTelemetry exporters for Python scripts, a hosted heartbeat service, statistical drift tests on forty records, a "review" state for findings, a registration-policy ladder with more than two rungs (the operator adds freely, or the operator must rule first).

## 10. Governance of findings: materiality, ownership, escalation, acceptance, closure

This section gathers what sections 3 and 9 say about findings into one place, because the goal names it as its own verification point.

- **Materiality.** Two questions per finding, not one: how bad if true (the lab's three levels answer this) and is it happening now (the sensor answers this directly). Bad and happening interrupts; bad but not happening shows at open; neither is record-only (CVSS plus CISA BOD 22-01 [A32, A33]). When unsure, go higher and re-grade in the write-up [A31]. The AI may raise a level with a reason and never lower one; the lab already rules this (AD-11).
- **Ownership.** Every finding row has an owner field, always filled, even when the answer is always Venkat (IIA [A36], SRE postmortems [A30]). The lab's "steward" idea from section 9 names which sensor or routine keeps it true.
- **Escalation.** One deadline per materiality level, and a sensor that counts days open. A finding past its deadline with no action and no acceptance row is re-raised at the next open as "this is being accepted by default" (IIA standard 15; CISA BOD 19-02 [A35]). That sentence makes silent acceptance visible.
- **Accepted exceptions.** A separate record with a status, never a deleted result (SARIF suppression [A34]). Three fields per line: who accepted, why from a fixed list (false positive, accepted risk, will not fix, history), and an expiry (ISO 27005 [A24], FedRAMP's deviation names [A25]). The sensor that raised the finding reads the accepted file, so an expired acceptance comes back as a finding.
- **Remediation.** Emergency fixes are done now and written up after; the write-up is not optional (ITIL emergency change [A15]). Every write-up ends in one action with a name and date, or an explicit "no action, here is why" (SRE postmortems [A30]).
- **Closure.** No finding is closed by a person. It is closed when its own sensor reports it absent on a later run (SARIF `absent`, SonarQube "fixed" set by the tool, CISA rescanning, SOC 2 CC4.2, NIST RC.RP-05). If the sensor cannot re-check it, the finding says so and stays open with a reason. This is the single practice that turns "agents grading themselves" into a scripted fact.

## 11. The comparison: current lab practice against external practice

One row per mechanism the baseline files name. The verdict words: **keep** (matches practice, leave it), **strengthen** (right idea, missing a piece practice supplies), **adapt** (practice has a pattern the lab lacks; take the smallest form), **replace** (the current mechanism is wrong or rests on a false premise), **avoid** (common enterprise practice that would add ceremony here). Every row names a lab file or baseline section and an external anchor.

| Lab mechanism (observed) | Where | External anchor | Verdict | The gap or the reason |
|---|---|---|---|---|
| Registry standard: stable id, one record, status word, dates, proof, never delete | `CAPABILITY-MAP.md` §3 | RFC 8126, RFC 2026, semver, cargo, ITIL CI [F1, F2, F11, F10] | keep | Matches. MLflow moved to this shape after fixed stages failed [F16] |
| Five status words | AD-05 | Nine vocabularies compared [F §7] | strengthen | Add two fields, not a sixth word: `deprecated-on`, `sunset-on` [F4, F5]; `replaced-by` on the old record; computed `current` on the head [F27, F28, F19] |
| Script enforcement of the standard | three of seventeen registries (baseline §1) | Backstage derives relations from records [F12]; AWS Config evaluates every resource against rules [F43] | strengthen | Extend to assets, targets, rulings, seeds, career model, routines; they are Missing on most sensing columns (baseline §4) |
| Source register: standing, `canonical-at`, use ceiling, `not-alone` | `REGISTER.md`; AD-17 to AD-21 | DCAT `hasCurrentVersion` [B10]; Datasheets' "must not be used for" [F20]; ODRL prohibition as first-class [F29]; S3 `REPLICA` status [B48] | keep | The one registry that already declares canonicality. The pattern to copy outward |
| Path-resolves check (`validate_and_render.py`, `dead-pointers.py`) | storage baseline §7; baseline §3 | Klein 2014 link rot vs content drift [F53]; RFC 6596 no chained canonicals [B15]; Terraform three-list diff [B52] | replace | Tests existence, not canonicality. 81 records "valid" while 0 name the current home. Replace with the three-list drift report and a `replaced-by` read on every resolved target |
| "Leave a pointer at the old location" | `CLAUDE.md` | Separation sheet [B25]; HTTP 301 and 410 [B14]; S3 delete marker [B49] | strengthen | No fixed filename, no machine-readable state, so no script can list the tombstones. The middle career-model copy has a README and no pointer |
| Old dated records keep old paths | `CLAUDE.md` "known broken" | RFC Editor never edits old text [B16]; ISO 15489 integrity [A37]; Nygard ADRs [A19] | keep | Three traditions agree. The forward pointer lives in the index and the tombstone, never inside the record |
| Root lock: fifteen allowed names at the lab root | `.claude/hooks/root-lock.py` | FHS as a placement contract [B26]; Bazel marker-defines-the-unit [B30]; EditorConfig walk-up with `root = true` [B28] | adapt | Right idea at one level. A marker file at each domain root and each replica root gives every level a contract and lets a walk of the tree yield the map |
| Derived views marked as generated (`CURRENT.md`, guide folder, catalogs) | baseline §2D | Twelve-Factor build-release-run [B33]; medallion tiers rebuildable from below [B47] | strengthen | Add `derived-from` and `built` fields and a check that refuses a derived file newer than its last build |
| Archive-only; warehouse outside the lab; never `_archive/` inside | `CLAUDE.md` minimum 1 | NARA disposition words: retain, transfer, destroy [B24]; ARMA disposition principle [B22]; package-registry yank [F8, F9] | keep | Matches yank exactly. Write the disposition per record with "destroy" marked never used |
| Names carrying status: `-v2`, `-plus`, `_archive` | observed across the lab | "Cool URIs don't change" [B44]; Zettelkasten time-based id [B55] | adapt | Apply to new names only; tombstones for the rest. Renaming existing folders would create the moves the rule exists to prevent |
| Two folders shown as "Documents" | storage baseline §2 | Apple: on turning the feature off, files "stay in iCloud Drive," new local folders "are empty" [C20] | strengthen | The retirement now in progress needs a baseline manifest before the move and a hash check after (controls one and three) |
| Copy → verify → remove, never `mv` | `CLAUDE.md` "moves are undoable now" | rclone move deletes source only after checksum-verified transfer [C36]; BagIt "valid" [C48] | keep | This is control three for local moves |
| Pre-write recheck during the duplicate collapse (9 of 397 skipped) | storage baseline §8 | RFC 9110 `If-Match` [C54]; Dropbox `WriteMode.update(rev)` [C56]; S3 conditional writes [C57] | keep, and write down | Control two done correctly by hand once. Make it a named rule so it is not re-invented |
| Account consolidation with no manifest | storage baseline §8 | BagIt complete-in-both-directions [C48]; AWS DMS missing-on-source and missing-on-target [C49] | replace (the practice, not the past) | Control one skipped once; completeness now unprovable. Manifest with `content_hash` before every future merge, move, or eviction [C32] |
| Reversal commands per move; DriveAtlas move logs | storage baseline header | `--backup-dir` [C38, C39]; Terraform mandatory state backups [C50] | keep | Matches. Keep displaced files in a dated backup directory, never nowhere |
| Time Machine: configured, never completed, destination 95% full | storage baseline §6 | Apple "at least twice the storage capacity" [C14]; "never deletes the last remaining backup" [C14]; NIST annual restore test [C1]; 3-2-1-1-0 [C7] | replace | The setup cannot complete by Apple's own rules. Two fixes, his call (section 13). Until then the facts sheet should say "not a backup yet" [C9] |
| Backup state as one flag | storage baseline §6 uses six states already | AWS, Azure, Veeam, Apple job words [C10 to C13] | strengthen | Two fields on the facts sheet: last job state, and date of last verified restore. Verified is never a job state |
| `tmutil currentphase` as the sensor | storage baseline §6 | `tmutil` man page and usage listing on this Mac [C13] | replace | The verb is not documented on this machine. Use `listbackups` and `latestbackup -t` |
| Dropbox as the off-machine copy; two Macs sync it | facts sheet "last off-machine copy (Dropbox)" | Syncthing, bisync, Backblaze: sync propagates deletes [C42, C43]; Dropbox version history 180 or 365 days on a team plan [C28] | strengthen | Dropbox is one copy with two mirrors, undoable only inside the history window. The snapshot tar counts as a backup only if no sync client can edit it in place |
| iCloud retirement with no replacement sync chosen | storage baseline §6 and §10 | Three shapes with named failure modes [C §4.5]; in all three the backup is a fourth thing outside the sync | adapt | Lay the three shapes before him with their failure modes (section 13). Do not pick "newer wins" for a tree both Macs edit [C41] |
| 965,000 files synced; iMac as full-estate node | storage baseline §2 | Dropbox 300,000 per computer, "includes online-only files" [C23, C24]; selective sync does not count [C26] | adapt | Selective sync per Mac, not online-only alone. Size Time Machine to the selected set [C14] |
| Icon-library exemption, approved, in progress | storage baseline §5 | BagIt manifest [D25]; OCFL [D26]; dark archive definition [D49]; NARA GRS 5.2 [D51] | strengthen | Write the five fields (reason, owner, manifest outside the tar, restore path with time, review date) before close-out |
| 53,160 screenshots older than six months, no rule | storage baseline §4 | NARA GRS 5.2 transitory "generally less than 180 days" [D51]; S3 lifecycle transition and expiration [D8] | adapt | One rule: past 180 days, batch to the warehouse with a manifest. Run by hand twice before any job runs it |
| 57% single-child folders; 25% of files under uninformative names | storage baseline §3 | Miller 1981; Larson and Czerwinski 1998 [D43, D45]; no source names the anti-pattern | adapt | The lab's number is its own evidence. Collapse single-child chains in working folders only; a cheap count sensor; leave the stock corpora out of the tree agents walk |
| Retrieval index: derived, rebuilt from the register, age on the facts sheet | baseline §2D | aider repo map [D36]; llms.txt [D38]; sitemaps cap [D39]; Spotlight and ripgrep as derived [D30, D32] | keep | The right pattern. Add an ignore file and a Spotlight privacy entry for stock folders; one entry file per top-level estate folder |
| Seven-field finding; three materiality levels; AI may raise, never lower | AD-11; sensor standard | SARIF level, kind, baselineState [A34, F62]; PagerDuty "when unsure, go higher" [A31]; CVSS plus CISA "is it happening now" [A32, A33] | strengthen | Add `baseline: new, unchanged, absent`. Add the second question. Add an owner field, always filled [A36] |
| Accepted-findings files with a reason | three files (baseline §1) | ISO 27005 residual-risk acceptance with monitoring [A24]; FedRAMP three deviation names [A25]; SARIF suppression with status [A34] | strengthen | Add who, reason type (false positive, accepted risk, will not fix, history), and expiry; the raising sensor re-reads the file so an expired acceptance returns |
| Closure by a receipt line; a loop closed by hand elsewhere stays open | baseline §2A | SOC 2 CC4.2 [A26]; NIST RC.RP-05 and 06 [A27]; CISA rescans [A35]; SonarQube "fixed" set by the tool [F64] | strengthen | No finding closed by a person. Closed when its sensor reports absent. If the sensor cannot re-check, the finding says so and stays open |
| "Show at open" findings with no owner (3 discovery, career-model 30 hits) | baseline §5 | IIA: silence is not acceptance; escalate [A36]; CISA deadlines by severity [A35] | strengthen | One deadline per level; past it with no action and no acceptance, re-raise as "being accepted by default" |
| "A missing line is the alarm" | Alfred's log; sensor standard | Healthchecks.io new, up, late, down, paused [F41]; Prometheus `absent()` [F42] | keep | Strongest external precedent of all ten sensor kinds. Add the late-versus-down split |
| Health as "did it run" | facts sheet; routines | Kubernetes liveness vs readiness [F39] | strengthen | Split alive from ready. The half-blind routine is alive-not-ready |
| Freshness: State stale rules by kind; index age; snapshot age | `state.py`; facts sheet | dbt `warn_after` and `error_after` [F33, F34]; TUF "MUST NOT trust an expired file" [F48] | adapt | Two thresholds per kind for registered sources and evidence items, mapped to show-at-open and interrupt; a reader must not lean on an item past expiry without saying so |
| Usage: `USAGE.jsonl` written, never read into a finding | baseline §2C, §5 | Trusted Advisor: a floor over a window for N days [F49] | adapt | One rule with a window and a floor, materiality record-only |
| Coverage: counts without denominators | facts sheet | OpenMetadata KPIs: percent with owner, by date [F36] | adapt | Three ratios with a target date |
| Drift: `verify.sh` for routines; README count vs script count; capability check | baseline §3 | Terraform plan [F44]; AWS Config [F43] | keep | Each is a Terraform plan in miniature. `verify.sh` needs an exit code and a way to run unattended (baseline §3) |
| Canonicality drift and supersession drift: sensed nowhere | baseline §4 | Content drift vs link rot [F53, F54]; Google canonical rules and redirect-hop limit [F58, F59]; ADMS `last` [F28]; Crossref resolution report [F57] | adapt | Two new sensor kinds, computable from the fields section 4 adds: one `canonical` per family with a hash-newest check; every `replaced-by` chain walked to its end with findings for over three hops, non-live end, loop, or dead id |
| Efficiency: no sensor reports its cost | baseline §3 | Google SRE monitoring chapter [F61] | adapt | Checks run and seconds taken, on the facts sheet; the page test on interrupts; a check with no finding in ninety days is a candidate for removal |
| Decision rows: number, date, decision, who, what follows | `ARCHITECTURE-DECISIONS.md` | Nygard and MADR [A19, A20]; RFC 2026 [A22]; decision journal [A38] | strengthen | Add "considered options" (one line) and "confirmation" (what script or file proves it happened). Two optional bet fields when a ruling is a bet, not a rule |
| "Three or more steps or a rule change" means plan first | `context/how-i-work.md` | ITIL standard, normal, emergency [A15]; Rust RFC threshold [A21] | adapt | Name the three types; write the list of standard changes an agent may do without asking |
| Two dated yeses for a new rule; corrections are evidence | `context/how-i-work.md`; memory | Two-person control vs four-eyes [A11]; NIST AC-5 separation of duties [A12] | keep | Proposer, validator, committer: agent proposes, script validates, Venkat commits. The deterministic validator is the honest second pair of eyes |
| Refusal layer: three minimums, root lock, unlazy stop hook | `CLAUDE.md`; `authority` entry | OPA's policy-as-data split [A14]; OWASP fail securely [E37]; Claude Code fail-closed matching [E18] | keep | Policy as data the hook reads; a case that must fail per hook. Any hook that errors denies |
| "Known broken" list in the front door | `CLAUDE.md` | ITIL known error [A28]; NIST after-action report [A27] | keep | It is a known-error list. Nothing names "problems" (one cause behind several alerts); one line per repeating cause |
| Session-sync fix closed by a test run reading the lab | `CLAUDE.md` 2026-09-10 | NIST RC.RP-05 integrity of restored assets verified [A27] | keep, and make it the rule | The model case for closure by re-check |
| Agent files: name, description, tools; some "All tools" | `.claude/agents/`; baseline §2C | Claude Code subagents [E5]; Saltzer and Schroeder least privilege [E8]; OWASP LLM06 [E9] | strengthen | Explicit allowlist per specialist; `maxTurns`; version and lifecycle; a "never" list mapped to a tool or hook |
| Agents not registered (AD-02) | `CAPABILITY-MAP.md` | Backstage catalog [F12]; Entra Agent ID sponsor [F25] | keep | The files are the registry. Borrow only `version` and a steward line |
| Alfred as manager; specialists return to Alfred | `AUTHORITY.md`; settled rule | OpenAI manager pattern [E4]; Anthropic orchestrator-workers [E2] | keep | Specialists never call specialists |
| Delegation carries objective, format, sources, boundaries in prose | this session's practice | Anthropic's four fields [E2]; A2A Task [E6]; OpenAI handoffs [E10] | adapt | A seven-line handoff note. Restrictions live on the tool and the file, never only in the note [E11] |
| Retrieval's evidence package with gaps; use ceilings per source | AD-24; `REGISTER.md` | Anthropic context engineering [E23]; TUF and RFC 9111 freshness [E25, E26] | keep | Add a "good until" date per item, defaulted by kind, compared by script |
| State: work and loop status words; claim and release; no "input-required" | AD-37; `state.py` | A2A task states [E6] | adapt | Six A2A words; "input-required" is the honest name for "stopped to ask Venkat" |
| No status block on specialist output | observed | `maxTurns` "marked as partial" [E5]; A2A terminal states [E6] | adapt | Status word, done, not done, evidence, next; the same block whether finished or ran out |
| Frozen tests changed only by his word; planted-fault proof; scripts not judges | AD-22, AD-23, AD-37; `prove-it-can-fail` | Anthropic evals [E42, E43]; mutation testing [E59]; Zheng and Panickssery judge biases [E55, E56] | keep | Add the commit hook against test-plus-subject edits; report pass^k [E50] |
| No specialist test sets; none of eight test kinds | observed | section 8 table | adapt | Insufficient and stale context first, then handoff, then planted injection, then authority and budget |
| "76% false success" in the front door | `CLAUDE.md` | Advani 2026 [E57]; Park and Choi 2026 [E58] | strengthen | Attach the scope: 75.8% of failures on one benchmark, 3% on another; scripted checks beat judges |
| Cloud routines: 28 recorded, 2 in the account, half-blind | `scheduled-routines` fault line | OpenLineage START with no terminal event [F31]; Kubernetes readiness [F39] | strengthen | Alive-not-ready is the honest state; a START with no COMPLETE after the expected time is a finding. The ruling on the missing routines is still his |
| Facts sheet as the one place numbers are gathered | `facts.py` | Google SRE golden signals; symptom-based alerting [F61] | keep | Add the two efficiency numbers and the owner column |

**Three patterns across the table.**

- **The lab's own ideas are the strongest ones in it.** "Scripts decide what is true," "a missing line is the alarm," "prove it can fail," "retire, never delete," and the registry standard each have a formal or established anchor and need no change. What they lack is reach: three registries enforce the standard, seventeen exist.
- **The gaps are fields, not systems.** Almost every strengthen and adapt row is two or three fields on a record the lab already has (`replaced-by`, `current`, `deprecated-on`, `expires`, `baseline`, `owner`, `steward`, `maxTurns`, `version`) plus a script that reads them. No row needs a product, a service, or a new store.
- **The three replace rows are all in the storage estate.** The canonicality check, the backup setup, and the `currentphase` line each rest on a false premise: that resolving equals canonical, that configured equals protected, that a verb exists because a script calls it.

## 12. Design principles for Step 2.5B

Each principle names its anchor and the lab evidence. All are **proposed**. They are grouped by the five standards 2.5B will write.

**Governance**

1. **One Accountable per decision, always written, even when it is always Venkat.** An empty owner is how findings die (RACI [A10], IIA [A36]). Lab evidence: three "show at open" findings with no owner today.
2. **Three change types, named.** Standard (an agent may do it, a script checks it, a receipt records it), normal (plan first, his go), emergency (do it now, write it up after, without exception). Keep a written list of standard changes (ITIL 4 [A15]). Lab evidence: the "three or more steps" rule already draws the line between standard and normal; the list does not exist.
3. **A ruling carries its confirmation.** Every decision row says what script or file will prove it was carried out (MADR [A20]). That is the bridge from a ruling to a sensor. Lab evidence: AD rows have "what follows" in prose and nothing a script reads.
4. **Exceptions expire.** An accepted finding carries who, a reason from a fixed short list, and a re-check date; the raising sensor re-reads the file (ISO 27005 [A24], FedRAMP [A25], SARIF [A34]). Lab evidence: three accepted files, none with a date.
5. **Closure is a sensor's word, never a person's.** A finding is closed when its own check reports it absent on a later run; if the check cannot re-run, the finding stays open and says why (SOC 2 [A26], NIST [A27], CISA [A35], SonarQube [F64]). Lab evidence: the 2026-09-10 session-sync fix was closed this way; the rule is not written.
6. **Two questions per finding.** How bad if true, and is it happening now (CVSS plus CISA [A32, A33]). Bad and happening interrupts; bad and not happening shows at open. When unsure, go higher [A31].
7. **Silence is escalated, not accepted.** Past its deadline with no action and no acceptance row, a finding is re-raised as "being accepted by default" (IIA [A36]).
8. **An incident closes on verified integrity and written criteria, with an after-action note** (NIST SP 800-61 [A27]). An hour of failed fixing is an incident, not a push-through (SRE [A29]).
9. **Records are fixed at creation by the party with direct knowledge; supersede, never edit** (ISO 15489 [A37], RFC Editor [B16], Nygard [A19]). The forward pointer lives in the index and the tombstone, never inside the old record.

**Lab organization and information architecture**

10. **A folder declares itself.** One fixed-name marker at each domain root and each replica root: id, role (canonical, replica, derived, historical, temporary), canonical location if not canonical, as-of date and validity window, `replaced-by` if superseded. A reader walks up to the nearest; the top says `root: true` (BagIt [B1], OCFL [B2], NDSA Level 1 [B4], Bazel [B30], EditorConfig [B28]).
11. **Identity is an id plus one resolver; a path in a consumer's file is a copy that goes stale** (DOI, Handle, ARK [B11 to B13]; the lab's own AD-17 rule "consumers ask by id"). Names carry no status words; apply to new names only [B44].
12. **Supersession is written in both directions and resolves in one hop.** `replaces` on the new record; `replaced-by` on the old record and the old location; one `current` on the family head; pointers point at the end, never at another pointer (RFC Editor [B16, B17], DataCite [B8], DCAT `hasCurrentVersion` [B10], RFC 6596 [B15]).
13. **Four relation words and no more**: replaces, replaced-by, identical-to, derived-from (DataCite [B8]). A new version sits beside the old one; a replacement retires it.
14. **Every old location gets a tombstone with a machine-readable state**: moved-to, or retired-on-purpose (separation sheet [B25], HTTP 301 and 410 [B14], S3 delete marker [B49]). A tombstone is the loudest thing in the folder, or the only thing.
15. **Derived artifacts are rebuilt, never edited, and say what they were built from and when** (Twelve-Factor [B33], medallion [B47]). A check refuses a derived file newer than its last build.
16. **A copy says it is a copy, and the source records the state of each copy** (S3 `REPLICA` and replication status [B48], Git LFS pointer [B35], git-annex location tracking [B37]). When copies disagree, one written survivorship rule names the winner (MDM [B46]); the lab's rule is that the canonical node wins.
17. **Every record has a disposition: retain, transfer, or destroy, with destroy marked never used** (NARA [B24], ARMA [B22]). Transfer means the warehouse.
18. **Drift is a diff against a declared expectation, in three lists**: declared but missing, present but undeclared, present but different in hash or canonical flag (Terraform [B52], BagIt complete-versus-valid [B1]). Metadata carries its own expiry, so a stale replica is stale regardless of content (TUF [B45]).
19. **Cost is counted in objects, not bytes, for enumeration, sync, and index; bytes still rule transfer and storage** (Dropbox, OneDrive, Google, S3, Git, HDFS [D1 to D6, D10, D22]). Keep any folder an agent must list under a few thousand entries; keep each machine's synced count under the vendor's line by selective sync, not online-only alone.
20. **An exemption from item-level search carries five things**: reason, owner, a manifest outside the archive, a restore path with expected time, a review date (BagIt [D25], OCFL [D26], dark archive [D49], NARA GRS 5.2 [D51]).
21. **Transitory material has a written lifecycle rule** (NARA GRS 5.2's 180 days [D51], S3 lifecycle [D8]), run by hand twice before any job runs it, with "destroy" written as "batch to the warehouse with a manifest."
22. **The estate is navigated through derived maps, never by walking**: an ignore file, an index excluded from stock corpora, one entry file per top-level folder in the llms.txt shape (ripgrep [D32], Spotlight privacy [D30], aider [D36], llms.txt [D38], sitemaps [D39]).

**Storage, sync, and backup** (part of Lab Organization in 2.5B, kept separate here because the goal names them)

23. **One canonical node per class of file; everything else is a mirror or a backup in one direction** (every one-way tool [C35, C39, C50]). A five-row table: class, canonical node, mirrors, backup, last verified.
24. **Sync is not backup; a live mirror is one copy however many machines hold it** (Syncthing, bisync, Backblaze [C42, C43]). The backup is the copy no sync client can write to (3-2-1-1-0 [C7]).
25. **Protection state is two fields**: last job state from the vendor's list, and the date of the last verified restore. Verified is never a job state (AWS, Azure, Veeam, Apple [C10 to C13]). A backup never restored is not yet a backup [C9]. Two numbers written once: recovery point, recovery time (NIST SP 800-34 [C1]).
26. **Three controls on every mutating operation, named separately**: baseline capture before (BagIt, Terraform [C48, C50]); revalidation at the moment of each write, with refusal as a normal outcome (RFC 9110 `If-Match`, Dropbox rev, S3 conditional writes [C54, C56, C57]); verification after, against the baseline, in both directions, kept as the receipt (`rclone check`, BagIt valid [C34, C48]). Plus a dry run first, a reverse per move, and one writer per tree while an executor runs.
27. **Completeness is per file in both directions, never per folder name** (BagIt complete [C48], AWS DMS [C49]). A claim that cannot be proven stays at the level it can be proven.
28. **Conflicts are kept, never auto-resolved by "newer wins," for any tree two machines edit** (Dropbox, Syncthing, Unison, bisync [C27, C40, C41, C37]).

**Specialist agents**

29. **Alfred coordinates only; specialists return only to Alfred** (settled; matches OpenAI's manager pattern [E4] and Anthropic's orchestrator [E2]). Single agent first; a second agent needs a reason the simpler shape could not meet [E1, E4].
30. **Identity is the file**: name, description, an explicit tools allowlist (never inherit-all), `maxTurns`, version, lifecycle status; read-only specialists get no write, edit, or shell tool (Claude Code [E5], Saltzer and Schroeder [E8], OWASP LLM06 [E9]).
31. **A "never" is enforced or it is a wish.** Each specialist ends with at most five never-lines, each mapped to a tool restriction or a hook [E10 to E12]. Restrictions live on the tool and the file, never only in a handoff note [E11].
32. **No specialist holds all three legs of the trifecta**: private data, untrusted content, external communication (Willison [E20], Hardy [E19]). A three-column table per specialist; three ticks is a bug.
33. **Authority is a front-matter fact, sorted by hand into reads and acts; a tool's self-description is untrusted** (MCP [E16]). Nothing irreversible without a human able to deny it (MCP, OWASP, EU Article 14 [E15, E16, E9]). "On the loop" is claimed only when a script or receipt actually watches [E14].
34. **A specialist receives the smallest high-signal slice, task first, evidence last, as pointers plus an evidence package, and returns a distilled summary with pointers** (Anthropic context engineering [E23], Lost in the Middle [E24]).
35. **Freshness is a date compared by code.** Every evidence item carries as-of and good-until, defaulted by source kind; a stale item is used only if the output says so (TUF, RFC 9111 [E25, E26]).
36. **Missing context narrows, asks, or stops; it never guesses.** Every specialist output ends with a status block: a word from complete, partial, blocked; what is done; what is not; where the evidence is; what next. The same block whether it finished or ran out (SQuAD 2.0 [E27], AbstentionBench [E28], `maxTurns` partial [E5]).
37. **Budgets are set and their exhaustion is named**: `maxTurns` on every specialist, the stop reason recorded, one retry for reads only, none for writes without idempotency (Anthropic, OpenAI, SRE, Stripe [E5, E30, E31, E35, E36]).
38. **A handoff carries seven things**: task, objective, output format, evidence pointers, constraints and never list, authority (read-only or may-act), what is already done (Anthropic, A2A, OpenAI [E2, E6, E10]). State uses six A2A task words, with input-required for "stopped to ask Venkat" [E6].
39. **Fail closed, fall back small, retire on purpose.** An errored hook denies; an unparseable specialist does not run; each specialist names its smaller job; a specialist failing the same check twice in a day is open and the brief says so; lifecycle words are experimental, active, deprecated, retired, and retired files go to the warehouse (OWASP fail securely [E37], circuit breaker [E33], Anthropic deprecations [E38]).

**Evaluation**

40. **Tests come from real jobs and real failures, 10 to 20 per specialist, code-graded where possible, frozen, changed only by his word** (Anthropic evals [E42, E43], Husain [E44]; the lab's AD-22 and AD-37).
41. **Eight kinds beyond known-answer, each one or two tasks per specialist**: insufficient context, stale context, faithfulness, planted injection, authority, budget exhaustion, handoff restriction, script-read outcome (section 8 table). The first three named are built first.
42. **A test proves it can fail before it counts** (mutation testing [E59], chaos [E60]; the lab's rule). A commit that changes a test and its subject together is refused.
43. **Reliability is pass^k, not one pass** (tau-bench [E50]). Three runs per frozen task.
44. **A judge, if used, is a different model than the actor, grades against a written rubric, never grades a state change a script could check, and is calibrated against 10 to 20 human-graded items** (Zheng [E55], Panickssery [E56], Advani [E57], Anthropic [E43], Husain [E44]).
45. **Self-reported success is not evidence; the 76% sentence carries its scope** (Advani [E57], Park and Choi [E58]).

**Registries and sensors**

46. **The registry standard as written, extended by script to every registry** (RFC 8126, RFC 2026, semver, ITIL [F1, F2, F11]). Two registration policies only: the operator adds freely, or the operator must rule first.
47. **Five status words stay; two dates and two pointers are added as fields**: `deprecated-on`, `sunset-on`, `replaced-by`, computed `current` (RFC 8594, RFC 9745, DCAT, ADMS [F4, F5, F27, F28]). No "review" state.
48. **Seven fields the catalog worlds agree on**: identity, steward, version, intended use, limits, evaluation (the lab's proof pointer), provenance (built from). The lab standard names the last two weakly (model cards, datasheets, Croissant, A2A, MCP [F18 to F24]).
49. **Ten sensor kinds, each with its smallest form** (section 9 table): integrity, health split into alive and ready, heartbeat with late and down, discovery as "not yet registered," freshness with two thresholds by kind, usage as a floor over a window, coverage as ratios with a date, drift as a diff, canonicality drift, supersession drift, efficiency as checks-run and seconds. A sensor reports, never fixes.
50. **Findings carry a baseline state** (new, unchanged, absent) computed against the last run by a stable key (SARIF [F62]). New is shown; unchanged is noise; absent means fixed or blind, and both get one line.
51. **Monitoring stays simple and pays for itself** (Google SRE [F61]). An interrupt must be urgent, actionable, and true; a check with no finding in ninety days is reviewed for removal.

## 13. Open decisions for Step 2.5B

His calls. None is made here. Each names what depends on it.

1. **The Time Machine fix.** A destination at least twice the included set (about 5 TB for today's 2.6 TiB volume), or exclusions that bring the included set under about 900 GB. Depends on decision 3. Until either, the facts sheet should say "not a backup yet."
2. **The off-machine backup that no sync client can touch.** The snapshot tar today lands in Dropbox, a synced folder. Where the one immutable copy lives (an unplugged disk, a store with no sync agent, a cloud bucket) is his. Depends on nothing; blocks driver 2's "working when."
3. **The sync shape for two Macs plus Dropbox.** Three shapes with named failure modes: cloud as hub (today), one Mac canonical with one-way mirrors, or two-way sync between the Macs with the cloud as a separate one-way copy. In all three the backup is a fourth thing. Blocks decisions 1 and 4 and the iCloud retirement's end state.
4. **Which classes of file are local on which Mac**, to bring each machine's synced count under 300,000 by selective sync. Depends on 3.
5. **The canonical node per class of file** (lab repos, client archive, media, stock assets, machine images), the five-row table. Depends on 3.
6. **A sixth status word or two fields.** Practice supports either; the two-field version (`deprecated-on`, `sunset-on` on a live record) keeps the list short and is what RFC 9745 does. His ruling, because AD-05 is his.
7. **The marker file's name and the tombstone's name.** Fixed names a script can find. Whether the existing `STATUS.md` becomes the marker or a new fixed name is chosen. One decision, then every script reads it.
8. **Whether the "no status words in names" rule applies backward.** Practice says apply to new names and add tombstones for the rest. Renaming `worthy-tool-v2`, `telegraph-plus`, or the Desktop copy would create moves. His call.
9. **The steward field.** Owner is always Venkat; steward is which routine, skill, or agent keeps a record true. Whether to add it to the registry standard.
10. **Standard changes.** The written list of changes an agent may make without asking (local, reversible, inside a domain). This widens agent authority and is his word by the minimums.
11. **Deadlines per materiality level** (proposed: interrupt same day; show at open a week, then it becomes an interrupt; record only monthly). His, because each becomes a line he reads.
12. **The 76% sentence.** Replace it in the front door with the scoped version. His, because the front door is his.
13. **Which specialist gets built first, and its trifecta row.** The evaluation kinds in section 8 need one real specialist to run against.
14. **Whether `docs/research/` is this brief's home**, and whether the six findings files behind it are kept (they are in the session scratchpad and will be lost with it unless placed).
15. **The icon-library exemption's five fields**, written before its close-out, and who reviews it on the review date.
16. **The routine count.** 28 recorded, 29 in the fault line, 2 in the account. Open since 2026-09-11; the alive-not-ready split makes the state honest but does not rule on the routines.

## 14. The AI-native test applied to the baseline

The definition (doctrine, section 0): the job is redesigned; AI is part of the core design; remove AI and the job no longer exists as designed; the main value can be a new way of working.

**Most of what this brief recommends is deliberately not AI-native, and that is correct.** Marker files, tombstones, manifests, hashes, expiry dates, allowlists, `maxTurns`, baseline states, and closure by re-scan are guardrails and sensors. Remove AI and they behave the same. The doctrine already says so: State and Authority are supporting layers "not tested against the definition on their own," and their deterministic parts are "intentional support for, and constraint on, the AI-native Products." The lab's core rule is the same idea in plain words: scripts decide what is true and what is forbidden.

**Where the reasoning sits, so the baseline does not slide into a checklist.** Five places, each already named in the lab's own definitions:

- **Materiality.** A sensor picks a level by rule; the AI may raise it with a reason, never lower it (AD-11). The two-question rule (how bad, is it happening) is computed; whether it matters to a driver is read.
- **What to investigate.** Discovery lists what is unregistered; the AI judges whether it looks useful and to which consumer (AD-08). A drift report lists three differences; the AI reads which one threatens a driver.
- **What a specialist should look at.** Retrieval and Context assemble the slice by meaning; the scripts only refuse what is out of scope, unresolvable, or expired (AD-24, Context v0.1).
- **What a finding means.** "Absent" is computed; whether it means fixed or blind is read.
- **What a move leaves behind.** The Portfolio decision rule reads a consequential move against direction; reuse and concentration are counted by script (portfolio architecture, section 5).

**Where a practice would fail the test and should be refused.** Any script that starts choosing the move, the slice, the strength of a claim, the moment to interrupt, or the reading of what drift means. Section 12 of the doctrine names this as the failure to watch for. Two candidates from this research to watch: a freshness rule that auto-drops stale evidence instead of marking it (the reader must still judge whether stale matters), and a usage sensor that auto-retires an unused skill instead of listing it.

**The Product Ecosystem and Portfolio architecture, checked.** Nothing here reopens the five Products, the three supports, the sixteen Portfolio objects, or the five loops. The recommendations land in the places those files already name: canonicality and supersession fields in the registries the Portfolio objects live in; sensors in `measurement`; specialist identity and handoff in Authority and Coordination; evaluation in the building-to-live gate (AD-15). The "one home per object" rule in the Portfolio architecture (section 2) is what the marker file and the `current` pointer make machine-checkable.

## 15. Verification against the goal's twelve points

1. **Governance, decision rights, change, exception, incident handling.** Section 3 (external, lab, verdict), section 10, principles 1 to 9.
2. **Machine-readable organization, artifact classes, canonicality, storage topology, supersession, archive and retention, sync, backup states.** Sections 4 and 5, principles 10 to 28. Artifact classes and states in principle 10 and 16; canonical location in 10 to 12; supersession chains in 12 to 14; archive and retention in 17 and 21; sync in 23, 24, 28; backup states in 25.
3. **Specialist-agent identity, boundaries, authority, context sufficiency, freshness, budgets, handoffs, degradation, lifecycle.** Section 7, principles 29 to 39. Alfred coordinates only is held as settled (principle 29).
4. **Evaluation of known-answer, stale and insufficient context, adversarial, authority, budget exhaustion, handoff, regression, real-world outcomes.** Section 8 table, principles 40 to 45.
5. **Registry identity and lifecycle plus the ten sensors** (integrity, health, discovery, freshness, usage, coverage, drift, canonicality drift, supersession drift, efficiency). Section 9 table (eleven rows including heartbeat), principles 46 to 51.
6. **Machine navigability, object-count and enumeration cost, governed exemptions.** Section 6, principles 19 to 22, with the count-versus-bytes verdict and its exception.
7. **Pre-change baseline capture, immediate pre-write revalidation, post-change verification** as three separate controls with separate anchors. Section 5 table, principle 26.
8. **Finding ownership, materiality, escalation, accepted exceptions, closure.** Section 10, principles 1, 4 to 7, 50.
9. **Explicit comparison of current lab practice with external practice.** Section 11, 56 rows, each with a lab file and an external anchor and one of five verdict words.
10. **Recommendations tied to identifiable sources.** Every principle in section 12 cites at least one source row; every row in section 11 cites one; section 16 reproduces all 342 source rows with labels.
11. **Enough for 2.5B without another broad research pass.** Section 12 gives 51 principles grouped by the five standards; section 13 gives the 16 decisions that gate them; the six findings files hold the per-practice "smallest honest version" and "over-engineering" lines for each.
12. **Nothing changed.** This file is the only thing written to the lab. No registry, schema, agent, sensor, hook, folder, sync setting, or estate object was touched. Proof: `git status` after writing shows one new file and the pre-existing modified log; the six findings files and drafts are in the session scratchpad.

**What this brief does not do.** It does not pick the sync shape, the backup destination, the marker filename, or the first specialist. It does not write any of the five standards. It does not re-run the estate measurements; the storage baseline's numbers are taken as given.

## 16. Sources

All 342 rows from the six passes, numbered by pass letter. Label is the source's own label. A row that rests on a secondary page or a snippet says so in its title.


### A. Governance (38 rows)

| # | Organisation | Title | Year | URL | Label |
|---|---|---|---|---|---|
| A1 | NIST | AI Risk Management Framework 1.0 (NIST AI 100-1) | 2023 | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf | FORMAL STANDARD |
| A2 | NIST | AI RMF Generative AI Profile (NIST AI 600-1) | 2024 | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf | FORMAL STANDARD |
| A3 | NIST | AI RMF Playbook, Govern | 2023 | https://airc.nist.gov/airmf-resources/playbook/govern/ | FORMAL STANDARD |
| A4 | ISO/IEC; Microsoft | ISO/IEC 42001:2023 AI management system (summary page used; iso.org 403) | 2023 | https://learn.microsoft.com/en-us/compliance/regulatory/offering-iso-42001 | FORMAL STANDARD |
| A5 | ISO/IEC | ISO/IEC 23894:2023 Guidance on AI risk management (preview) | 2023 | https://cdn.standards.iteh.ai/samples/77304/cb803ee4e9624430a5db177459158b24/ISO-IEC-23894-2023.pdf | FORMAL STANDARD |
| A6 | ISO/IEC; arc42 | ISO/IEC 38500:2024 Governance of IT (summary page used; iso.org 403) | 2024 | https://quality.arc42.org/standards/iso-38500 | FORMAL STANDARD |
| A7 | European Union | AI Act, Article 14 Human oversight | 2024 | https://artificialintelligenceact.eu/article/14/ | FORMAL STANDARD |
| A8 | European Union | AI Act, Article 12 Record-keeping | 2024 | https://artificialintelligenceact.eu/article/12/ | FORMAL STANDARD |
| A9 | European Union | AI Act, Article 26 Obligations of deployers | 2024 | https://artificialintelligenceact.eu/article/26/ | FORMAL STANDARD |
| A10 | Umbrex | RACI matrix | n.d. | https://umbrex.com/resources/frameworks/organization-frameworks/raci-matrix-responsible-accountable-consulted-informed/ | ESTABLISHED CONVENTION |
| A11 | NIST (CNSSI 4009) | Glossary: two-person control | 2022 | https://csrc.nist.gov/glossary/term/two_person_control | FORMAL STANDARD |
| A12 | NIST | SP 800-53 Rev 5, AC-5 Separation of duties (via csf.tools) | 2020 | https://csf.tools/reference/nist-sp-800-53/r5/ac/ac-5/ | FORMAL STANDARD |
| A13 | Tallyfy and others | Delegation of authority matrix | n.d. | https://tallyfy.com/delegation-of-authority-matrix-template/ | ESTABLISHED CONVENTION |
| A14 | Open Policy Agent (CNCF) | OPA documentation | 2026 | https://www.openpolicyagent.org/docs/latest/ | VENDOR PATTERN |
| A15 | itsm.tools (ITIL 4 summary) | Change enablement in ITIL 4 | n.d. | https://itsm.tools/change-enablement/ | ESTABLISHED CONVENTION |
| A16 | ISO/IEC | ISO/IEC 20000-1:2018 Service management (preview, contents only) | 2018 | https://cdn.standards.iteh.ai/samples/70636/17bebffa99f74756bcab329953450930/ISO-IEC-20000-1-2018.pdf | FORMAL STANDARD |
| A17 | Google | Site Reliability Engineering, ch. 8 Release Engineering | 2016 | https://sre.google/sre-book/release-engineering/ | VENDOR PATTERN |
| A18 | CNCF GitOps Working Group | OpenGitOps principles v1.0.0 | 2021 | https://opengitops.dev/ | ESTABLISHED CONVENTION |
| A19 | Michael Nygard (Cognitect) | Documenting Architecture Decisions | 2011 | https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions | ESTABLISHED CONVENTION |
| A20 | MADR project | Markdown Any Decision Records 4.0.0 | 2024 | https://adr.github.io/madr/ | ESTABLISHED CONVENTION |
| A21 | Rust project | Rust RFC process README | 2026 | https://github.com/rust-lang/rfcs/blob/master/README.md | ESTABLISHED CONVENTION |
| A22 | IETF | RFC 2026, The Internet Standards Process | 1996 | https://www.rfc-editor.org/rfc/rfc2026.html | FORMAL STANDARD |
| A23 | IETF | RFC 7282, On Consensus and Humming | 2014 | https://www.rfc-editor.org/rfc/rfc7282.html | ESTABLISHED CONVENTION |
| A24 | PECB (ISO/IEC 27005:2022 summary) | ISO/IEC 27005:2022 main changes | 2022 | https://pecb.com/en/article/iso-iec-270052022-main-changes-and-implications | FORMAL STANDARD |
| A25 | FedRAMP (US GSA) | Plan of Action and Milestones | n.d. | https://www.fedramp.gov/legacy/playbook/csp/authorization/poam/ | FORMAL STANDARD |
| A26 | AICPA (via Truvo) | SOC 2 Trust Services Criteria CC4.2 | 2017 | https://fex.truvocyber.com/browse/soc2/CC4.2 | FORMAL STANDARD |
| A27 | NIST | SP 800-61 Rev 3, Incident Response Recommendations | 2025 | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r3.pdf | FORMAL STANDARD |
| A28 | IT Process Wiki (ITIL summary, not fetched) | Problem Management | n.d. | https://wiki.en.it-processmaps.com/index.php/Problem_Management | ESTABLISHED CONVENTION |
| A29 | Google | Site Reliability Engineering, ch. 14 Managing Incidents | 2016 | https://sre.google/sre-book/managing-incidents/ | VENDOR PATTERN |
| A30 | Google | Site Reliability Engineering, ch. 15 Postmortem Culture | 2016 | https://sre.google/sre-book/postmortem-culture/ | VENDOR PATTERN |
| A31 | PagerDuty | Incident Response: Severity Levels | n.d. | https://response.pagerduty.com/before/severity_levels/ | VENDOR PATTERN |
| A32 | FIRST | CVSS v4.0 Specification | 2023 | https://www.first.org/cvss/v4.0/specification-document | FORMAL STANDARD |
| A33 | CISA | BOD 22-01 Known Exploited Vulnerabilities | 2021 | https://www.cisa.gov/news-events/directives/bod-22-01-reducing-significant-risk-known-exploited-vulnerabilities | FORMAL STANDARD |
| A34 | OASIS | SARIF 2.1.0 | 2020 | https://docs.oasis-open.org/sarif/sarif/v2.1.0/os/sarif-v2.1.0-os.html | FORMAL STANDARD |
| A35 | CISA | BOD 19-02 Vulnerability Remediation Requirements | 2019 | https://www.cisa.gov/news-events/directives/bod-19-02-vulnerability-remediation-requirements-internet-accessible-systems | FORMAL STANDARD |
| A36 | The IIA | Global Internal Audit Standards | 2024 | https://www.theiia.org/en/standards/2024-standards/global-internal-audit-standards/ | FORMAL STANDARD |
| A37 | ISO | ISO 15489-1:2016 Records management, concepts and principles (preview) | 2016 | https://cdn.standards.iteh.ai/samples/62542/fe383f4fe10448d5b22ce628b1542ed6/ISO-15489-1-2016.pdf | FORMAL STANDARD |
| A38 | Farnam Street | Decision Journal | n.d. | https://fs.blog/decision-journal/ | EMERGING PRACTICE |

### B. Information architecture (60 rows)

| # | Organisation | Title | Year | URL | Label |
|---|---|---|---|---|---|
| B1 | IETF | RFC 8493 The BagIt File Packaging Format | 2018 | https://www.rfc-editor.org/rfc/rfc8493 | FORMAL STANDARD |
| B2 | OCFL Editors | Oxford Common File Layout Specification 1.1 | 2024 | https://ocfl.io/1.1/spec/ | FORMAL STANDARD |
| B3 | Library of Congress | PREMIS Data Dictionary 3.0 (read via Wikipedia; loc.gov 403) | 2016 | https://www.loc.gov/standards/premis/ | FORMAL STANDARD |
| B4 | NDSA | Levels of Digital Preservation v2.1 | 2026 | https://ndsa.org/publications/levels-of-digital-preservation/ | ESTABLISHED CONVENTION |
| B5 | Trevor Owens (NDSA author) | NDSA Levels matrix transcription | 2013 | https://github.com/tjowens/NDSA-Levels-of-Digital-Preservation/blob/master/levels.md | ESTABLISHED CONVENTION |
| B6 | ISO / CCSDS | ISO 14721 OAIS Reference Model (read via Wikipedia) | 2025 | https://en.wikipedia.org/wiki/Open_Archival_Information_System | FORMAL STANDARD |
| B7 | DCMI | DCMI Metadata Terms | 2020 | https://www.dublincore.org/specifications/dublin-core/dcmi-terms/ | FORMAL STANDARD |
| B8 | DataCite | Metadata Schema 4.6, relatedIdentifier | 2024 | https://datacite-metadata-schema.readthedocs.io/en/4.6/properties/relatedidentifier/ | FORMAL STANDARD |
| B9 | schema.org | supersededBy | n.d. | https://schema.org/supersededBy | ESTABLISHED CONVENTION |
| B10 | W3C | Data Catalog Vocabulary (DCAT) Version 3 | 2024 | https://www.w3.org/TR/vocab-dcat-3/ | FORMAL STANDARD |
| B11 | DOI Foundation | What is a DOI (ISO 26324) | n.d. | https://www.doi.org/the-identifier/what-is-a-doi/ | FORMAL STANDARD |
| B12 | DONA Foundation | Handle System | n.d. | https://www.dona.net/handle-system | ESTABLISHED CONVENTION |
| B13 | ARK Alliance | About ARKs | n.d. | https://arks.org/about/ | ESTABLISHED CONVENTION |
| B14 | IETF | RFC 9110 HTTP Semantics (301, 410) | 2022 | https://www.rfc-editor.org/rfc/rfc9110 | FORMAL STANDARD |
| B15 | IETF | RFC 6596 The Canonical Link Relation | 2012 | https://www.rfc-editor.org/rfc/rfc6596 | FORMAL STANDARD |
| B16 | IETF / RFC Editor | RFC 7322 RFC Style Guide, Updates and Obsoletes | 2014 | https://www.rfc-editor.org/rfc/rfc7322 | ESTABLISHED CONVENTION |
| B17 | RFC Editor | RFC 2616 info page showing Obsoleted by | 2026 | https://www.rfc-editor.org/info/rfc2616 | ESTABLISHED CONVENTION |
| B18 | IETF | RFC 8594 The Sunset HTTP Header Field | 2019 | https://www.rfc-editor.org/rfc/rfc8594 | FORMAL STANDARD |
| B19 | IETF | RFC 9745 The Deprecation HTTP Response Header Field | 2025 | https://www.rfc-editor.org/rfc/rfc9745 | FORMAL STANDARD |
| B20 | Digital Curation Centre | ISO 15489 briefing paper (ISO page 403) | 2007 | https://dcc.ac.uk/guidance/briefing-papers/standards-watch-papers/iso-15489 | FORMAL STANDARD (standard); briefing is secondary |
| B21 | ISO | ISO 30301 (not read, UNVERIFIED) | 2019 | https://www.iso.org/standard/53732.html | FORMAL STANDARD |
| B22 | ARMA International | Generally Accepted Recordkeeping Principles (PDF fetched, text UNVERIFIED) | 2009 | https://www.armavi.org/docs/garp.pdf | ESTABLISHED CONVENTION |
| B23 | NARA | Bulletin 2008-07 endorsing DoD 5015.2-STD v3 | 2008 | https://www.archives.gov/records-mgmt/bulletins/2008/2008-07.html | FORMAL STANDARD |
| B24 | NARA / Cornell LII | 36 CFR 1220.18 Definitions (disposition, records schedule) | current | https://www.law.cornell.edu/cfr/text/36/1220.18 | FORMAL STANDARD |
| B25 | Society of American Archivists | Dictionary of Archives Terminology: separation sheet | n.d. | https://dictionary.archivists.org/entry/separation-sheet.html | ESTABLISHED CONVENTION |
| B26 | Linux Foundation | Filesystem Hierarchy Standard 3.0 | 2015 | https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html | FORMAL STANDARD |
| B27 | GitHub | About code owners | current | https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners | VENDOR PATTERN |
| B28 | EditorConfig | EditorConfig | current | https://editorconfig.org/ | ESTABLISHED CONVENTION |
| B29 | PyPA | pyproject.toml specification | 2026 | https://packaging.python.org/en/latest/specifications/pyproject-toml/ | FORMAL STANDARD |
| B30 | Bazel | Repositories, workspaces, packages, and targets | current | https://bazel.build/concepts/build-ref | VENDOR PATTERN |
| B31 | Google / CACM | Why Google Stores Billions of Lines of Code in a Single Repository | 2016 | https://research.google/pubs/why-google-stores-billions-of-lines-of-code-in-a-single-repository/ | VENDOR PATTERN |
| B32 | Nx | Monorepo Folder Structure (page 404 on fetch, UNVERIFIED) | current | https://nx.dev/docs/concepts/decisions/folder-structure | VENDOR PATTERN |
| B33 | Adam Wiggins | The Twelve-Factor App, V. Build, release, run | 2011 | https://12factor.net/build-release-run | ESTABLISHED CONVENTION |
| B34 | Pro Git | Git Tools: Submodules | 2nd ed. | https://git-scm.com/book/en/v2/Git-Tools-Submodules | ESTABLISHED CONVENTION |
| B35 | Git LFS | Git LFS specification (pointer format) | current | https://github.com/git-lfs/git-lfs/blob/main/docs/spec.md | ESTABLISHED CONVENTION |
| B36 | DVC (Iterative) | .dvc files | current | https://doc.dvc.org/user-guide/project-structure/dvc-files | VENDOR PATTERN |
| B37 | git-annex | How it works | current | https://git-annex.branchable.com/how_it_works/ | VENDOR PATTERN |
| B38 | Pro Git | Git Internals: Git Objects | 2nd ed. | https://git-scm.com/book/en/v2/Git-Internals-Git-Objects | ESTABLISHED CONVENTION |
| B39 | OCI | Image Format Specification: Descriptor (digest) | current | https://github.com/opencontainers/image-spec/blob/main/descriptor.md | FORMAL STANDARD |
| B40 | Tom Preston-Werner | Semantic Versioning 2.0.0 | 2013 | https://semver.org/ | ESTABLISHED CONVENTION |
| B41 | Mahmoud Hashemi | Calendar Versioning | current | https://calver.org/ | ESTABLISHED CONVENTION |
| B42 | IETF | RFC 3339 Date and Time on the Internet: Timestamps | 2002 | https://www.rfc-editor.org/rfc/rfc3339 | FORMAL STANDARD |
| B43 | ulid | ULID specification | current | https://github.com/ulid/spec | EMERGING PRACTICE |
| B44 | Tim Berners-Lee, W3C | Cool URIs don't change | 1998 | https://www.w3.org/Provider/Style/URI.html | ESTABLISHED CONVENTION |
| B45 | The Update Framework | TUF Specification v1.0.36 | 2026 | https://theupdateframework.github.io/specification/latest/ | FORMAL STANDARD |
| B46 | Profisee | MDM Survivorship: How to Choose the Right Record | 2025 | https://profisee.com/blog/mdm-survivorship/ | VENDOR PATTERN |
| B47 | Databricks | Medallion architecture | current | https://www.databricks.com/glossary/medallion-architecture | VENDOR PATTERN |
| B48 | AWS | S3 Replication; Getting replication status | current | https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-status.html | VENDOR PATTERN |
| B49 | AWS | S3 Working with delete markers | current | https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeleteMarker.html | VENDOR PATTERN |
| B50 | AWS | RDS read replicas | current | https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html | VENDOR PATTERN |
| B51 | Kubernetes | Objects in Kubernetes (spec and status) | current | https://kubernetes.io/docs/concepts/overview/working-with-objects/ | VENDOR PATTERN |
| B52 | HashiCorp | Manage resource drift | current | https://developer.hashicorp.com/terraform/tutorials/state/resource-drift | VENDOR PATTERN |
| B53 | Forte Labs | The PARA Method | 2023 | https://fortelabs.com/blog/para/ | ESTABLISHED CONVENTION |
| B54 | Johnny.Decimal | Introduction | current | https://johnnydecimal.com/10-19-concepts/11-core/11.01-introduction/ | EMERGING PRACTICE |
| B55 | zettelkasten.de | Introduction to the Zettelkasten Method | current | https://zettelkasten.de/introduction/ | ESTABLISHED CONVENTION |
| B56 | lycheeverse | lychee link checker | current | https://github.com/lycheeverse/lychee | ESTABLISHED CONVENTION |
| B57 | tcort | markdown-link-check | current | https://github.com/tcort/markdown-link-check | ESTABLISHED CONVENTION |
| B58 | sitemaps.org | Sitemaps XML format (lastmod) | current | https://www.sitemaps.org/protocol.html | FORMAL STANDARD |
| B59 | Digital Preservation Coalition | Handbook: Fixity and checksums | current | https://www.dpconline.org/handbook/technical-solutions-and-tools/fixity-and-checksums | ESTABLISHED CONVENTION |
| B60 | Pew Research Center | When Online Content Disappears | 2024 | https://www.pewresearch.org/data-labs/2024/05/17/when-online-content-disappears/ | EMERGING PRACTICE (study) |

### C. Storage, sync, backup, mutation (58 rows)

| # | Organisation | Title | Year | URL | Label |
|---|---|---|---|---|---|
| C1 | NIST | SP 800-34 Rev. 1, Contingency Planning Guide for Federal Information Systems (PDF read locally) | 2010 | https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-34r1.pdf | FORMAL STANDARD |
| C2 | NIST CSRC | Glossary: Recovery Point Objective; Recovery Time Objective | current | https://csrc.nist.gov/glossary/term/recovery_point_objective and https://csrc.nist.gov/glossary/term/recovery_time_objective | FORMAL STANDARD |
| C3 | ISO/IEC (via High Table, ISMS.online) | ISO/IEC 27001:2022 Annex A 8.13 Information backup; ISO/IEC 27002:2022 guidance | 2022 | https://hightable.io/iso-27001-annex-a-8-13-information-backup/ and https://www.isms.online/iso-27002/control-8-13-information-backup/ | FORMAL STANDARD (text UNVERIFIED against iso.org) |
| C4 | ISO | ISO 22301:2019 Security and resilience, Business continuity management systems, Requirements | 2019 | https://www.iso.org/standard/75106.html | FORMAL STANDARD (fetch blocked, UNVERIFIED) |
| C5 | Backup Wrap-up (W. Curtis Preston) | Peter Krogh, who coined "the 3-2-1 rule," on our podcast | 2021 | https://www.backupwrapup.com/peter-krogh-who-coined-the-3-2-1-rule-on-our-podcast/ | ESTABLISHED CONVENTION |
| C6 | Backblaze | The 3-2-1 Backup Rule and Beyond: 3-2-1 vs. 3-2-1-1-0 vs. 4-3-2 | 2024 | https://www.backblaze.com/blog/whats-the-diff-3-2-1-vs-3-2-1-1-0-vs-4-3-2/ | ESTABLISHED CONVENTION |
| C7 | Veeam | 3-2-1 Backup Rule Explained (Julia Furst Morgado) | 2024, upd. 2026 | https://www.veeam.com/blog/321-backup-rule.html | VENDOR PATTERN |
| C8 | AWS | AWS Backup Developer Guide: Restore testing | current | https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-testing.html | VENDOR PATTERN |
| C9 | kirbyidau.com | Quote: Schrödinger's Backup | 2022 | https://kirbyidau.com/2022/02/28/quote-schrodingers-backup-the-condition-of-any-backup-is-unknown-until-a-restore-is-attempted/ | ESTABLISHED CONVENTION (origin UNVERIFIED) |
| C10 | AWS | AWS Backup API: DescribeBackupJob (State values) | current | https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DescribeBackupJob.html | VENDOR PATTERN |
| C11 | Microsoft | Manage the backup jobs using REST API in Azure Backup; Get-AzRecoveryServicesBackupJob status values | 2026 | https://learn.microsoft.com/en-us/azure/backup/backup-azure-arm-userestapi-managejobs | VENDOR PATTERN |
| C12 | Veeam | Backup & Replication Event Reference: Backup Job Finished (JobResult 0 Success, 1 Warning, 2 Failed) | current | https://helpcenter.veeam.com/docs/vbr/events/event_190.html | VENDOR PATTERN |
| C13 | Apple | tmutil(8) man page (dated 10 June 2015) and `tmutil` usage listing, read on macOS 26.6.2 | 2015/2026 | local: `man tmutil`; mirror https://keith.github.io/xcode-man-pages/tmutil.8.html | VENDOR PATTERN |
| C14 | Apple | Back up your Mac with Time Machine | current | https://support.apple.com/en-us/104984 | VENDOR PATTERN |
| C15 | Apple | If Time Machine on your Mac recommends a larger backup disk | current | https://support.apple.com/guide/mac-help/mchl72b408e0/mac | VENDOR PATTERN |
| C16 | Apple | If you can't back up or restore your Mac using Time Machine | current | https://support.apple.com/en-us/102220 | VENDOR PATTERN |
| C17 | Apple | If a Time Machine backup is interrupted | current | https://support.apple.com/guide/mac-help/if-a-time-machine-backup-is-interrupted-mh15142/mac | VENDOR PATTERN |
| C18 | Eclectic Light Co. (Howard Oakley) | Time Machine to APFS: Backing up | 2021 | https://eclecticlight.co/2021/03/17/time-machine-to-apfs-backing-up/ | ESTABLISHED CONVENTION |
| C19 | Apple | About Time Machine local snapshots | current | https://support.apple.com/en-us/102154 | VENDOR PATTERN |
| C20 | Apple | Turn off Desktop & Documents Folders on your Mac | current | https://support.apple.com/en-us/126628 | VENDOR PATTERN |
| C21 | Apple | Add your Desktop and Documents files to iCloud Drive | current | https://support.apple.com/en-us/109344 | VENDOR PATTERN |
| C22 | Apple | Optimize storage space on your Mac | current | https://support.apple.com/guide/mac-help/sysp4ee93ca4/mac | VENDOR PATTERN |
| C23 | Dropbox | How many files can I store in my Dropbox account? | current | https://help.dropbox.com/storage-space/file-storage-limit | VENDOR PATTERN |
| C24 | Dropbox | Restrictions and limitations for teams | current | https://help.dropbox.com/plans/large-deployments | VENDOR PATTERN |
| C25 | Dropbox | Free up space with online-only files | current | https://help.dropbox.com/sync/make-files-online-only | VENDOR PATTERN |
| C26 | Dropbox | Selective sync overview | current | https://help.dropbox.com/sync/selective-sync-overview | VENDOR PATTERN |
| C27 | Dropbox | What's a conflicted copy? | current | https://help.dropbox.com/organize/conflicted-copy | VENDOR PATTERN |
| C28 | Dropbox | Dropbox version history overview | current | https://help.dropbox.com/delete-restore/version-history-overview | VENDOR PATTERN |
| C29 | Dropbox | How to use Dropbox Rewind | current | https://help.dropbox.com/delete-restore/rewind | VENDOR PATTERN |
| C30 | Dropbox | What happens when a user joins my Dropbox team account? | current | https://help.dropbox.com/account-access/user-joins-team | VENDOR PATTERN |
| C31 | Dropbox | Can I merge Dropbox accounts? | current | https://help.dropbox.com/account-settings/merge-two-accounts | VENDOR PATTERN |
| C32 | Dropbox | Developers reference: Content hash | current | https://www.dropbox.com/developers/reference/content-hash | VENDOR PATTERN |
| C33 | rclone | Dropbox backend | current | https://rclone.org/dropbox/ | VENDOR PATTERN |
| C34 | rclone | rclone check | current | https://rclone.org/commands/rclone_check/ | VENDOR PATTERN |
| C35 | rclone | rclone sync | current | https://rclone.org/commands/rclone_sync/ | VENDOR PATTERN |
| C36 | rclone | rclone move | current | https://rclone.org/commands/rclone_move/ | VENDOR PATTERN |
| C37 | rclone | Bisync | current | https://rclone.org/bisync/ | VENDOR PATTERN |
| C38 | rclone | Global flags (--dry-run, --checksum, --backup-dir, --max-delete, --immutable, --ignore-checksum, --check-first) | current | https://rclone.org/flags/ and https://rclone.org/docs/ | VENDOR PATTERN |
| C39 | Samba (rsync) | rsync(1) man page | current | https://download.samba.org/pub/rsync/rsync.1 | VENDOR PATTERN |
| C40 | Benjamin Pierce et al. | Unison File Synchronizer User Manual (GitHub source) | current | https://raw.githubusercontent.com/bcpierce00/unison/master/doc/unison-manual.tex | VENDOR PATTERN |
| C41 | Syncthing | Understanding Synchronization (conflicting changes) | current | https://docs.syncthing.net/users/syncing.html | VENDOR PATTERN |
| C42 | Syncthing | FAQ (is Syncthing a backup application) | current | https://docs.syncthing.net/users/faq.html | ESTABLISHED CONVENTION |
| C43 | Backblaze | Disaster Recovery 101: Backup vs. Replication (Kari Wilson) | 2025 | https://www.backblaze.com/blog/disaster-recovery-101-backup-vs-replication/ | ESTABLISHED CONVENTION |
| C44 | NDSA (Phillips, Bailey, Goethals, Owens) | The NDSA Levels of Digital Preservation: An Explanation and Uses (PDF read locally) | 2013 | https://www.digitalpreservation.gov/documents/NDSA_Levels_Archiving_2013.pdf | ESTABLISHED CONVENTION |
| C45 | NDSA | NDSA Announces the Levels of Digital Preservation 2.0 (matrix on OSF, not fetched) | 2019 | https://ndsa.org/2019/10/28/ndsa-announces-the-levels-of-digital-preservation-2.0.html | ESTABLISHED CONVENTION |
| C46 | NDSA | Checking Your Digital Content: What is Fixity, and When Should I be Checking It? (PDF read locally) | 2014 | https://www.digitalpreservation.gov/documents/NDSA-Fixity-Guidance-Report-final100214.pdf | ESTABLISHED CONVENTION |
| C47 | Digital Preservation Coalition | Digital Preservation Handbook: Fixity and checksums | current | https://www.dpconline.org/handbook/technical-solutions-and-tools/fixity-and-checksums | ESTABLISHED CONVENTION |
| C48 | IETF | RFC 8493, The BagIt File Packaging Format (V1.0) | 2018 | https://www.rfc-editor.org/rfc/rfc8493 | FORMAL STANDARD |
| C49 | AWS | AWS DMS data validation | current | https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Validating.html | VENDOR PATTERN |
| C50 | HashiCorp | Terraform CLI: state commands (backups cannot be disabled) | current | https://developer.hashicorp.com/terraform/cli/commands/state | VENDOR PATTERN |
| C51 | PostgreSQL Global Development Group | Upgrading a PostgreSQL Cluster | current | https://www.postgresql.org/docs/current/upgrading.html | VENDOR PATTERN |
| C52 | Red Hat (Ansible) | Validating tasks: check mode and diff mode | current | https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_checkmode.html | VENDOR PATTERN |
| C53 | HashiCorp | Terraform CLI: plan | current | https://developer.hashicorp.com/terraform/cli/commands/plan | VENDOR PATTERN |
| C54 | IETF | RFC 9110, HTTP Semantics: sections 9.2.2 (idempotent) and 13 (conditional requests) | 2022 | https://www.rfc-editor.org/rfc/rfc9110 | FORMAL STANDARD |
| C55 | Kubernetes | API Concepts: resource versions and optimistic concurrency | current | https://kubernetes.io/docs/reference/using-api/api-concepts/ | VENDOR PATTERN |
| C56 | Dropbox | Java SDK: WriteMode (add, overwrite, update(rev)) | current | https://dropbox.github.io/dropbox-sdk-java/api-docs/v3.0.x/com/dropbox/core/v2/files/WriteMode.html | VENDOR PATTERN |
| C57 | AWS | Amazon S3: How to prevent object overwrites with conditional writes | 2024 onward | https://docs.aws.amazon.com/AmazonS3/latest/userguide/conditional-writes.html | VENDOR PATTERN |
| C58 | Microsoft | Save disk space with OneDrive Files On-Demand for Mac | current | https://support.microsoft.com/en-us/office/save-disk-space-with-onedrive-files-on-demand-for-mac-529f6d53-e572-4922-a585-e7a318c135f0 | VENDOR PATTERN |

### D. Navigability and corpora (62 rows)

| # | Organisation | Title | Year | URL | Label |
|---|---|---|---|---|---|
| D1 | Microsoft Support | Restrictions and limitations in OneDrive and SharePoint | 2026 (current) | https://support.microsoft.com/en-us/office/restrictions-and-limitations-in-onedrive-and-sharepoint-64883a5d-228e-48f5-b3d2-eb39e07630fa | VENDOR PATTERN |
| D2 | Google Workspace | Shared drive limits in Google Drive | current | https://support.google.com/a/users/answer/7338880?hl=en | VENDOR PATTERN |
| D3 | Dropbox Help | Restrictions and limitations for team deployments of Dropbox | current | https://help.dropbox.com/plans/large-deployments | VENDOR PATTERN |
| D4 | Dropbox Help | How many files can I store in my Dropbox account? | current | https://help.dropbox.com/storage-space/file-storage-limit | VENDOR PATTERN |
| D5 | AWS | ListObjectsV2 (S3 API Reference) | current | https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectsV2.html | VENDOR PATTERN |
| D6 | AWS | Amazon S3 pricing | current | https://aws.amazon.com/s3/pricing/ | VENDOR PATTERN |
| D7 | AWS | Understanding archive retrieval options | current | https://docs.aws.amazon.com/AmazonS3/latest/userguide/restoring-objects-retrieval-options.html | VENDOR PATTERN |
| D8 | AWS | Managing the lifecycle of objects | current | https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html | VENDOR PATTERN |
| D9 | Microsoft Learn | Blob rehydration from the archive tier | 2026 | https://learn.microsoft.com/en-us/azure/storage/blobs/archive-rehydrate-overview | VENDOR PATTERN |
| D10 | GitHub Blog (Hostetler) | Improve Git monorepo performance with a file system monitor | 2022 | https://github.blog/engineering/infrastructure/improve-git-monorepo-performance-with-a-file-system-monitor/ | VENDOR PATTERN |
| D11 | GitHub Blog (Stolee) | Make your monorepo feel small with Git's sparse index | 2021 | https://github.blog/open-source/git/make-your-monorepo-feel-small-with-gits-sparse-index/ | VENDOR PATTERN |
| D12 | GitHub Blog (Stolee, Dye) | The Story of Scalar | 2022 | https://github.blog/open-source/git/the-story-of-scalar/ | VENDOR PATTERN |
| D13 | Git project | git-update-index (untracked cache, fsmonitor) | current | https://git-scm.com/docs/git-update-index | ESTABLISHED CONVENTION |
| D14 | Git project | git-sparse-checkout | current | https://git-scm.com/docs/git-sparse-checkout | ESTABLISHED CONVENTION |
| D15 | Git project | scalar | current | https://git-scm.com/docs/scalar | ESTABLISHED CONVENTION |
| D16 | Linux kernel | ext4: Directory Entries | current | https://docs.kernel.org/filesystems/ext4/directory.html | ESTABLISHED CONVENTION |
| D17 | man7.org | getdents(2) | current | https://man7.org/linux/man-pages/man2/getdents.2.html | ESTABLISHED CONVENTION |
| D18 | Olark engineering | You can list a directory containing 8 million files! But not with ls (fetch failed; excerpt only) | 2011 | https://www.olark.com/spw/2011/08/you-can-list-a-directory-with-8-million-files-but-not-with-ls/ | ESTABLISHED CONVENTION |
| D19 | Apple | TN1150: HFS Plus Volume Format | archive | https://developer.apple.com/library/archive/technotes/tn/tn1150.html | FORMAL STANDARD |
| D20 | Apple | APFS Guide FAQ (retired) | 2018 | https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/APFS_Guide/FAQ/FAQ.html | VENDOR PATTERN |
| D21 | Microsoft Learn | NTFS overview | 2025 | https://learn.microsoft.com/en-us/windows-server/storage/file-server/ntfs-overview | VENDOR PATTERN |
| D22 | Cloudera Blog | The Small Files Problem | 2009 | https://www.cloudera.com/blog/technical/the-small-files-problem.html | ESTABLISHED CONVENTION |
| D23 | PyTorch Blog | Efficient PyTorch I/O library for Large Datasets, Many Files, Many GPUs | 2020 | https://pytorch.org/blog/efficient-pytorch-io-library-for-large-datasets-many-files-many-gpus/ | ESTABLISHED CONVENTION |
| D24 | WebDataset | README | current | https://github.com/webdataset/webdataset | ESTABLISHED CONVENTION |
| D25 | IETF | RFC 8493: The BagIt File Packaging Format (V1.0) | 2018 | https://www.rfc-editor.org/rfc/rfc8493.html | FORMAL STANDARD |
| D26 | OCFL editors | Oxford Common File Layout Specification 1.1 | 2022 | https://ocfl.io/1.1/spec/ | FORMAL STANDARD |
| D27 | restic | Design reference | current | https://restic.readthedocs.io/en/stable/100_references.html | ESTABLISHED CONVENTION |
| D28 | HDF Group | Introduction to HDF5 | current | https://support.hdfgroup.org/documentation/hdf5/latest/_intro_h_d_f5.html | ESTABLISHED CONVENTION |
| D29 | Apache Parquet | File Format | current | https://parquet.apache.org/docs/file-format/ | ESTABLISHED CONVENTION |
| D30 | Apple Support | About Spotlight indexing and search results on Apple devices | 2026 | https://support.apple.com/en-us/102321 | VENDOR PATTERN |
| D31 | plocate | plocate, a much faster locate | current | https://plocate.sesse.net/ | ESTABLISHED CONVENTION |
| D32 | BurntSushi | ripgrep GUIDE | current | https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md | ESTABLISHED CONVENTION |
| D33 | Apache Lucene | Lucene 9.0 index format (package summary) | 2021 | https://lucene.apache.org/core/9_0_0/core/org/apache/lucene/codecs/lucene90/package-summary.html | ESTABLISHED CONVENTION |
| D34 | Sourcegraph | Zoekt design document | current | https://github.com/sourcegraph/zoekt/blob/main/doc/design.md | ESTABLISHED CONVENTION |
| D35 | GitHub Blog (Clem) | The technology behind GitHub's new code search | 2023 | https://github.blog/engineering/architecture-optimization/the-technology-behind-githubs-new-code-search/ | VENDOR PATTERN |
| D36 | aider | Building a better repository map with tree sitter | 2023 | https://aider.chat/2023/10/22/repomap.html | EMERGING PRACTICE |
| D37 | tree-sitter | Project page | current | https://tree-sitter.github.io/tree-sitter/ | ESTABLISHED CONVENTION |
| D38 | Howard / Answer.AI | The /llms.txt file | 2024 | https://llmstxt.org/ | EMERGING PRACTICE |
| D39 | sitemaps.org | Sitemaps XML format (protocol) | current | https://www.sitemaps.org/protocol.html | FORMAL STANDARD |
| D40 | W3C | Data Catalog Vocabulary (DCAT) Version 3 | 2024 | https://www.w3.org/TR/vocab-dcat-3/ | FORMAL STANDARD |
| D41 | Amundsen (Lyft) | README | current | https://github.com/amundsen-io/amundsen | ESTABLISHED CONVENTION |
| D42 | DataHub | README | current | https://github.com/datahub-project/datahub | VENDOR PATTERN |
| D43 | Miller, D. P. | The Depth/Breadth Tradeoff in Hierarchical Computer Menus (403 on fetch; confirmed via UMD HCIL TR 99-15) | 1981 | https://journals.sagepub.com/doi/10.1177/107118138102500179 | ESTABLISHED CONVENTION |
| D44 | UMD HCIL | Technical report 99-15 (summarises Miller 1981 and Larson and Czerwinski 1998) | 1999 | https://www.cs.umd.edu/hcil/trs/99-15/99-15.html | ESTABLISHED CONVENTION |
| D45 | Larson, Czerwinski (Microsoft Research) | Web Page Design: Implications of Memory, Structure and Scent for Information Retrieval | 1998 | https://www.microsoft.com/en-us/research/publication/web-page-design-implications-memory-structure-scent-information-retrieval/ | ESTABLISHED CONVENTION |
| D46 | Nielsen Norman Group (Whitenton) | Flat vs. Deep Website Hierarchies | 2013 | https://www.nngroup.com/articles/flat-vs-deep-hierarchy/ | ESTABLISHED CONVENTION |
| D47 | Nielsen Norman Group | Polyhierarchy in Information Architecture (video) | 2022 | https://www.nngroup.com/videos/polyhierarchy-information-architecture/ | ESTABLISHED CONVENTION |
| D48 | Rosenfeld, Morville (O'Reilly) | Information Architecture for the World Wide Web, 2nd ed., polyhierarchy section (403 on fetch; excerpt only) | 2002 | https://www.oreilly.com/library/view/information-architecture-for/0596000359/ch09s09.html | ESTABLISHED CONVENTION |
| D49 | Digital Preservation Coalition | Digital Preservation Handbook: Glossary | current | https://www.dpconline.org/handbook/glossary | ESTABLISHED CONVENTION |
| D50 | CLOCKSS | The Role of Dark Archives | current | https://clockss.org/the-role-of-dark-archives/ | VENDOR PATTERN |
| D51 | NARA | General Records Schedule 5.2: Transitory and Intermediary Records, Transmittal 34 | 2023 | https://www.archives.gov/files/records-mgmt/grs/grs05-2.pdf | FORMAL STANDARD |
| D52 | NARA | Scheduling Records | current | https://www.archives.gov/records-mgmt/scheduling/sch-records | FORMAL STANDARD |
| D53 | Dropbox Help | Free up space with online-only files | current | https://help.dropbox.com/sync/make-files-online-only | VENDOR PATTERN |
| D54 | Dropbox Help | How to open online-only files on macOS | current | https://help.dropbox.com/sync/online-only-mac | VENDOR PATTERN |
| D55 | Microsoft Support | Save disk space with OneDrive Files On-Demand for Windows | current | https://support.microsoft.com/en-us/onedrive/save-disk-space-with-onedrive-files-on-demand-for-windows | VENDOR PATTERN |
| D56 | Apple Support | Take a screenshot on Mac | current | https://support.apple.com/en-us/102646 | VENDOR PATTERN |
| D57 | Apple Support | Free up storage space on Mac | current | https://support.apple.com/en-us/102624 | VENDOR PATTERN |
| D58 | Apple Support | Manage storage on iPhone (TOC only on fetch) | current | https://support.apple.com/guide/iphone/manage-storage-on-iphone-iph47c931112/ios | VENDOR PATTERN |
| D59 | rclone | Documentation (--fast-list) | current | https://rclone.org/docs/ | ESTABLISHED CONVENTION |
| D60 | Backblaze | How to Use Rclone with Backblaze B2 Cloud Storage | current | https://www.backblaze.com/docs/cloud-storage-integrate-rclone-with-backblaze-b2 | VENDOR PATTERN |
| D61 | man7.org | rsync(1) (--inc-recursive) | current | https://www.man7.org/linux/man-pages/man1/rsync.1.html | ESTABLISHED CONVENTION |
| D62 | Dropbox Tech Blog (Jayakar) | Rewriting the heart of our sync engine | 2020 | https://dropbox.tech/infrastructure/rewriting-the-heart-of-our-sync-engine | VENDOR PATTERN |

### E. Agents and evaluation (60 rows)

| # | Organisation | Title | Year | URL | Label |
|---|---|---|---|---|---|
| E1 | Anthropic | Building effective agents | 2024 | https://www.anthropic.com/engineering/building-effective-agents | VENDOR PATTERN |
| E2 | Anthropic | How we built our multi-agent research system | 2025 | https://www.anthropic.com/engineering/multi-agent-research-system | VENDOR PATTERN |
| E3 | Cemri et al. (UC Berkeley) | Why Do Multi-Agent LLM Systems Fail? | 2025 | https://arxiv.org/abs/2503.13657 | EMERGING PRACTICE |
| E4 | OpenAI | A practical guide to building agents (PDF fetched; quotes via landing page snippet) | 2025 | https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf | VENDOR PATTERN |
| E5 | Anthropic | Claude Code: Create custom subagents | 2026 | https://code.claude.com/docs/en/sub-agents | VENDOR PATTERN |
| E6 | Google / Linux Foundation | Agent2Agent (A2A) Protocol Specification v1.0.0 | 2025 | https://a2a-protocol.org/latest/specification/ | FORMAL STANDARD |
| E7 | SPIFFE (CNCF) | SPIFFE Overview | n.d. | https://spiffe.io/docs/latest/spiffe-about/overview/ | FORMAL STANDARD |
| E8 | Saltzer and Schroeder | The Protection of Information in Computer Systems | 1975 | https://www.cs.virginia.edu/~evans/cs551/saltzer/ | ESTABLISHED CONVENTION |
| E9 | OWASP | LLM06:2025 Excessive Agency | 2025 | https://genai.owasp.org/llmrisk/llm062025-excessive-agency/ | ESTABLISHED CONVENTION |
| E10 | OpenAI | Agents SDK: Handoffs | 2025 | https://openai.github.io/openai-agents-python/handoffs/ | VENDOR PATTERN |
| E11 | OpenAI | Agents SDK: Guardrails | 2025 | https://openai.github.io/openai-agents-python/guardrails/ | VENDOR PATTERN |
| E12 | OWASP | Agentic AI Threats and Mitigations | 2025 | https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/ | ESTABLISHED CONVENTION |
| E13 | US Air Force | Unmanned Aircraft Systems Flight Plan 2009-2047 (page blocked; quote via search snippet, UNVERIFIED direct) | 2009 | https://www.globalsecurity.org/military/library/policy/usaf/usaf-uas-flight-plan_2009-2047.htm | ESTABLISHED CONVENTION |
| E14 | Carnegie Council (Leins, Kaspersen) | Seven Myths of Using the Term "Human on the Loop" | 2021 | https://www.carnegiecouncil.org/media/article/7-myths-of-using-the-term-human-on-the-loop | ESTABLISHED CONVENTION |
| E15 | European Union | AI Act, Article 14: Human oversight | 2024 | https://artificialintelligenceact.eu/article/14/ | FORMAL STANDARD |
| E16 | Model Context Protocol | Specification 2025-06-18: Tools (and Security and Trust & Safety) | 2025 | https://modelcontextprotocol.io/specification/2025-06-18/server/tools | FORMAL STANDARD |
| E17 | Anthropic | Claude Code: Configure permissions | 2026 | https://code.claude.com/docs/en/permissions | VENDOR PATTERN |
| E18 | Anthropic | Claude Code: Security | 2026 | https://code.claude.com/docs/en/security | VENDOR PATTERN |
| E19 | Norm Hardy | The Confused Deputy | 1988 | https://css.csail.mit.edu/6.858/2015/readings/confused-deputy.html | ESTABLISHED CONVENTION |
| E20 | Simon Willison | The lethal trifecta for AI agents | 2025 | https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/ | ESTABLISHED CONVENTION |
| E21 | OWASP | LLM01:2025 Prompt Injection | 2025 | https://genai.owasp.org/llmrisk/llm01-prompt-injection/ | ESTABLISHED CONVENTION |
| E22 | MITRE | ATLAS technique AML.T0051 LLM Prompt Injection (primary page 404 on 2026-09-14; verified via two secondary catalogues) | 2023 | https://atlas.mitre.org/techniques/AML.T0051 | ESTABLISHED CONVENTION |
| E23 | Anthropic | Effective context engineering for AI agents | 2025 | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents | VENDOR PATTERN |
| E24 | Liu et al. (Stanford) | Lost in the Middle: How Language Models Use Long Contexts | 2023 | https://arxiv.org/abs/2307.03172 | EMERGING PRACTICE |
| E25 | The Update Framework | TUF Specification v1.0.36 | 2024 | https://theupdateframework.github.io/specification/latest/ | FORMAL STANDARD |
| E26 | IETF | RFC 9111: HTTP Caching | 2022 | https://www.rfc-editor.org/rfc/rfc9111.html | FORMAL STANDARD |
| E27 | Rajpurkar, Jia, Liang (Stanford) | Know What You Don't Know: Unanswerable Questions for SQuAD (SQuAD 2.0) | 2018 | https://arxiv.org/abs/1806.03822 | ESTABLISHED CONVENTION |
| E28 | Kirichenko et al. (Meta FAIR) | AbstentionBench | 2025 | https://arxiv.org/abs/2506.09038 | EMERGING PRACTICE |
| E29 | Anthropic | Tool use with Claude (overview; missing-parameter behaviour) | 2026 | https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview | VENDOR PATTERN |
| E30 | OpenAI | Agents SDK: Running agents (max_turns) | 2025 | https://openai.github.io/openai-agents-python/running_agents/ | VENDOR PATTERN |
| E31 | Anthropic | Handling stop reasons | 2026 | https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons | VENDOR PATTERN |
| E32 | Michael Nygard (Pragmatic Bookshelf) | Release It! Second Edition | 2018 | https://pragprog.com/titles/mnee2/release-it-second-edition/ | ESTABLISHED CONVENTION |
| E33 | Microsoft | Azure Architecture Center: Circuit Breaker pattern | 2025 | https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker | ESTABLISHED CONVENTION |
| E34 | Microsoft | Azure Architecture Center: Bulkhead pattern | 2026 | https://learn.microsoft.com/en-us/azure/architecture/patterns/bulkhead | ESTABLISHED CONVENTION |
| E35 | Google | Site Reliability Engineering, ch. 22: Addressing Cascading Failures | 2017 | https://sre.google/sre-book/addressing-cascading-failures/ | ESTABLISHED CONVENTION |
| E36 | Stripe | API reference: Idempotent requests | 2026 | https://docs.stripe.com/api/idempotent_requests | ESTABLISHED CONVENTION |
| E37 | OWASP | Fail securely | n.d. | https://community.owasp.org/Fail_securely | ESTABLISHED CONVENTION |
| E38 | Anthropic | Model deprecations (active, legacy, deprecated, retired) | 2026 | https://platform.claude.com/docs/en/about-claude/model-deprecations | VENDOR PATTERN |
| E39 | Google | Maps Platform launch stages | n.d. | https://developers.google.com/maps/launch-stages | VENDOR PATTERN |
| E40 | Langfuse | Prompt management: get started | 2026 | https://langfuse.com/docs/prompt-management/get-started | VENDOR PATTERN |
| E41 | NIST | AI 600-1: Generative AI Profile (PDF fetched; text extracted lossily) | 2024 | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf | FORMAL STANDARD |
| E42 | Anthropic | Demystifying evals for AI agents | 2026 | https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents | VENDOR PATTERN |
| E43 | Anthropic | Create strong empirical evaluations (Develop tests) | 2026 | https://platform.claude.com/docs/en/test-and-evaluate/develop-tests | VENDOR PATTERN |
| E44 | Hamel Husain | Your AI Product Needs Evals | 2024 | https://hamel.dev/blog/posts/evals/ | ESTABLISHED CONVENTION |
| E45 | Ragas | Faithfulness metric | 2025 | https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/faithfulness/ | EMERGING PRACTICE |
| E46 | Saad-Falcon et al. (Stanford) | ARES: An Automated Evaluation Framework for RAG | 2023 | https://arxiv.org/abs/2311.09476 | EMERGING PRACTICE |
| E47 | Manakul et al. (Cambridge) | SelfCheckGPT | 2023 | https://arxiv.org/abs/2303.08896 | EMERGING PRACTICE |
| E48 | Microsoft | PyRIT: Python Risk Identification Tool | 2024 | https://github.com/microsoft/PyRIT | ESTABLISHED CONVENTION |
| E49 | Xia et al. (CSIRO Data61) | Evaluation-Driven Development and Operations of LLM Agents | 2024 | https://arxiv.org/abs/2411.13768 | EMERGING PRACTICE |
| E50 | Yao et al. (Sierra) | tau-bench | 2024 | https://arxiv.org/abs/2406.12045 | ESTABLISHED CONVENTION |
| E51 | Liu et al. (Tsinghua) | AgentBench | 2023 | https://arxiv.org/abs/2308.03688 | ESTABLISHED CONVENTION |
| E52 | Mialon et al. (Meta) | GAIA | 2023 | https://arxiv.org/abs/2311.12983 | ESTABLISHED CONVENTION |
| E53 | Jimenez et al. (Princeton) | SWE-bench | 2023 | https://arxiv.org/abs/2310.06770 | ESTABLISHED CONVENTION |
| E54 | Zhou et al. (CMU) | WebArena | 2023 | https://arxiv.org/abs/2307.13854 | ESTABLISHED CONVENTION |
| E55 | Zheng et al. (LMSYS) | Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena | 2023 | https://arxiv.org/abs/2306.05685 | ESTABLISHED CONVENTION |
| E56 | Panickssery et al. | LLM Evaluators Recognize and Favor Their Own Generations | 2024 | https://arxiv.org/abs/2404.13076 | EMERGING PRACTICE |
| E57 | Advani | From Confident Closing to Silent Failure: Characterizing False Success in LLM Agents | 2026 | https://arxiv.org/abs/2606.09863 | EMERGING PRACTICE |
| E58 | Park and Choi | When Do Agent Loops Mistake Stagnation for Progress? | 2026 | https://arxiv.org/abs/2607.25152 | EMERGING PRACTICE |
| E59 | PIT | Mutation testing (pitest.org) | n.d. | https://pitest.org/ | ESTABLISHED CONVENTION |
| E60 | Principles of Chaos Engineering | principlesofchaos.org | 2019 | https://principlesofchaos.org/ | ESTABLISHED CONVENTION |

### F. Registries and sensors (64 rows)

| # | Organisation | Title | Year | URL | Label |
|---|---|---|---|---|---|
| F1 | IETF | RFC 8126, Guidelines for Writing an IANA Considerations Section in RFCs | 2017 | https://www.rfc-editor.org/rfc/rfc8126.html | FORMAL STANDARD |
| F2 | IETF | RFC 2026, The Internet Standards Process, Revision 3 | 1996 | https://www.rfc-editor.org/rfc/rfc2026.html | FORMAL STANDARD |
| F3 | IETF | RFC 7322, RFC Style Guide (Updates / Obsoletes headers) | 2014 | https://www.rfc-editor.org/rfc/rfc7322.html | FORMAL STANDARD |
| F4 | IETF | RFC 8594, The Sunset HTTP Header Field | 2019 | https://www.rfc-editor.org/rfc/rfc8594.html | FORMAL STANDARD |
| F5 | IETF | RFC 9745, The Deprecation HTTP Response Header Field | 2025 | https://www.rfc-editor.org/rfc/rfc9745.html | FORMAL STANDARD |
| F6 | IANA | Link Relations registry (Specification Required; Notes column) | 2026 | https://www.iana.org/assignments/link-relations/link-relations.xhtml | FORMAL STANDARD |
| F7 | npm | npm-deprecate CLI docs | 2026 | https://docs.npmjs.com/cli/v10/commands/npm-deprecate | ESTABLISHED CONVENTION |
| F8 | Python | PEP 592, Adding Yank Support to the Simple API | 2019 | https://peps.python.org/pep-0592/ | ESTABLISHED CONVENTION |
| F9 | Rust | cargo yank | 2026 | https://doc.rust-lang.org/cargo/commands/cargo-yank.html | ESTABLISHED CONVENTION |
| F10 | Rust | Publishing on crates.io (a publish is permanent) | 2026 | https://doc.rust-lang.org/cargo/reference/publishing.html | ESTABLISHED CONVENTION |
| F11 | semver.org | Semantic Versioning 2.0.0 | 2013 | https://semver.org/ | ESTABLISHED CONVENTION |
| F12 | Backstage | Descriptor Format of Catalog Entities | 2026 | https://backstage.io/docs/features/software-catalog/descriptor-format | VENDOR PATTERN |
| F13 | GitHub | About code owners | 2026 | https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners | VENDOR PATTERN |
| F14 | OpenAPI Initiative | OpenAPI Specification 3.1.0 | 2021 | https://spec.openapis.org/oas/v3.1.0.html | FORMAL STANDARD |
| F15 | Axelos | ITIL 4 Glossaries of Terms (page found; text did not load, UNVERIFIED) | 2019 | https://www.axelos.com/resource-hub/glossary/ITIL-4-glossaries-of-terms | ESTABLISHED CONVENTION |
| F16 | MLflow | Model Registry (stages deprecated in 2.9.0) | 2024 | https://www.mlflow.org/docs/2.19.0/model-registry.html | VENDOR PATTERN |
| F17 | MLflow | Model Registry (current: versions, aliases, tags) | 2026 | https://mlflow.org/docs/latest/ml/model-registry/ | VENDOR PATTERN |
| F18 | Mitchell et al. | Model Cards for Model Reporting | 2019 | https://arxiv.org/abs/1810.03993 | ESTABLISHED CONVENTION |
| F19 | Hugging Face | Model Cards (Hub docs; base_model, new_version) | 2026 | https://huggingface.co/docs/hub/model-cards | ESTABLISHED CONVENTION |
| F20 | Gebru et al. | Datasheets for Datasets | 2021 | https://arxiv.org/abs/1803.09010 | ESTABLISHED CONVENTION |
| F21 | MLCommons | Croissant Format Specification 1.0 | 2024 | https://docs.mlcommons.org/croissant/docs/croissant-spec.html | EMERGING PRACTICE |
| F22 | A2A Project (Linux Foundation) | A2A Protocol Specification 1.0 (Agent Card) | 2026 | https://a2a-protocol.org/latest/specification/ | EMERGING PRACTICE |
| F23 | Model Context Protocol | MCP Registry (preview) | 2025 | https://github.com/modelcontextprotocol/registry | EMERGING PRACTICE |
| F24 | Model Context Protocol | server.json reference | 2025 | https://raw.githubusercontent.com/modelcontextprotocol/registry/main/docs/reference/server-json/generic-server-json.md | EMERGING PRACTICE |
| F25 | Microsoft | What are agent identities? (Entra Agent ID) | 2026 | https://learn.microsoft.com/en-us/entra/agent-id/what-are-agent-identities | EMERGING PRACTICE |
| F26 | Anthropic | Claude Managed Agents overview (beta) | 2026 | https://platform.claude.com/docs/en/managed-agents/overview | EMERGING PRACTICE |
| F27 | W3C | Data Catalog Vocabulary (DCAT), Version 3 | 2024 | https://www.w3.org/TR/vocab-dcat-3/ | FORMAL STANDARD |
| F28 | W3C | Asset Description Metadata Schema (ADMS) | 2013 | https://www.w3.org/TR/vocab-adms/ | FORMAL STANDARD |
| F29 | W3C | ODRL Information Model 2.2 | 2018 | https://www.w3.org/TR/odrl-model/ | FORMAL STANDARD |
| F30 | OpenLineage | Object Model | 2026 | https://openlineage.io/docs/spec/object-model | EMERGING PRACTICE |
| F31 | OpenLineage | Run Cycle | 2026 | https://openlineage.io/docs/spec/run-cycle | EMERGING PRACTICE |
| F32 | Bitol (LF AI & Data) | Open Data Contract Standard, Fundamentals | 2026 | https://bitol-io.github.io/open-data-contract-standard/latest/fundamentals/ | EMERGING PRACTICE |
| F33 | dbt Labs | Sources (freshness config) | 2026 | https://docs.getdbt.com/docs/build/sources | VENDOR PATTERN |
| F34 | dbt Labs | Source freshness | 2026 | https://docs.getdbt.com/docs/deploy/source-freshness | VENDOR PATTERN |
| F35 | DataHub | Dataset entity (status, ownership aspects) | 2026 | https://docs.datahub.com/docs/generated/metamodel/entities/dataset | VENDOR PATTERN |
| F36 | OpenMetadata | Key Performance Indicators (KPI) | 2026 | https://docs.open-metadata.org/latest/how-to-guides/data-insights/kpi | VENDOR PATTERN |
| F37 | NDSA | Levels of Digital Preservation (levels page; matrix row text UNVERIFIED) | 2019 | https://ndsa.org/publications/levels-of-digital-preservation/ | ESTABLISHED CONVENTION |
| F38 | W3C | Link Checker documentation | 2026 | https://validator.w3.org/checklink/docs/checklink.html | ESTABLISHED CONVENTION |
| F39 | Kubernetes | Liveness, Readiness, and Startup Probes | 2026 | https://kubernetes.io/docs/concepts/configuration/liveness-readiness-startup-probes/ | ESTABLISHED CONVENTION |
| F40 | IETF (individual draft) | Health Check Response Format for HTTP APIs, draft-06 (expired) | 2021 | https://datatracker.ietf.org/doc/html/draft-inadarei-api-health-check | EMERGING PRACTICE |
| F41 | Healthchecks.io | Documentation (states: new, up, late, down, paused) | 2026 | https://healthchecks.io/docs/ | ESTABLISHED CONVENTION |
| F42 | Prometheus | Query functions: absent(), absent_over_time() | 2026 | https://prometheus.io/docs/prometheus/latest/querying/functions/ | ESTABLISHED CONVENTION |
| F43 | AWS | What Is AWS Config? | 2026 | https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html | VENDOR PATTERN |
| F44 | HashiCorp | Manage Resource Drift (Terraform) | 2026 | https://developer.hashicorp.com/terraform/tutorials/state/resource-drift | VENDOR PATTERN |
| F45 | Apache Airflow | Tasks (SLAs), 2.10.5 | 2024 | https://airflow.apache.org/docs/apache-airflow/2.10.5/core-concepts/tasks.html | VENDOR PATTERN |
| F46 | Apache Airflow | Tasks, stable (SLA removed in 3.0, Deadline Alerts in 3.1) | 2026 | https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/tasks.html | VENDOR PATTERN |
| F47 | Great Expectations | Validate data freshness with GX | 2026 | https://docs.greatexpectations.io/docs/reference/learn/data_quality_use_cases/freshness/ | VENDOR PATTERN |
| F48 | The Update Framework | TUF Specification 1.0.36 (expires field) | 2026 | https://theupdateframework.github.io/specification/latest/ | FORMAL STANDARD |
| F49 | AWS | Trusted Advisor cost optimization checks (idle resources) | 2026 | https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html | VENDOR PATTERN |
| F50 | OpenTelemetry | GenAI semantic conventions repository (attribute names UNVERIFIED) | 2026 | https://github.com/open-telemetry/semantic-conventions-genai | EMERGING PRACTICE |
| F51 | Microsoft | Schema drift in mapping data flow | 2025 | https://learn.microsoft.com/en-us/azure/data-factory/concepts-data-flow-schema-drift | VENDOR PATTERN |
| F52 | Google Cloud | MLOps: Continuous delivery and automation pipelines in machine learning | 2026 | https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning | VENDOR PATTERN |
| F53 | Klein et al. (PLOS ONE) | Scholarly Context Not Found: One in Five Articles Suffers from Reference Rot | 2014 | https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0115253 | ESTABLISHED CONVENTION |
| F54 | Jones et al. (PLOS ONE) | Scholarly Context Adrift: Three out of Four URI References Lead to Changed Content | 2016 | https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0167475 | ESTABLISHED CONVENTION |
| F55 | Zittrain, Albert, Lessig (Harvard Law Review Forum) | Perma: Scoping and Addressing the Problem of Link and Reference Rot in Legal Citations (full text blocked today; figures from abstract) | 2014 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2329161 | ESTABLISHED CONVENTION |
| F56 | Internet Archive | Using the Wayback Machine (Save Page Now) | 2026 | https://help.archive.org/help/using-the-wayback-machine/ | ESTABLISHED CONVENTION |
| F57 | Crossref | Resolution report | 2026 | https://www.crossref.org/documentation/reports/resolution-report/ | ESTABLISHED CONVENTION |
| F58 | Google Search Central | Consolidate duplicate URLs (canonical) | 2026 | https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls | VENDOR PATTERN |
| F59 | Google Search Central | Site moves with URL changes (10 hops; keep chains under 5) | 2026 | https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes | VENDOR PATTERN |
| F60 | Profisee | MDM Survivorship: How to Choose the Right Record | 2025 | https://profisee.com/blog/mdm-survivorship/ | VENDOR PATTERN |
| F61 | Google | Site Reliability Engineering, ch. 6, Monitoring Distributed Systems | 2016 | https://sre.google/sre-book/monitoring-distributed-systems/ | ESTABLISHED CONVENTION |
| F62 | OASIS | SARIF Version 2.1.0 | 2020 | https://docs.oasis-open.org/sarif/sarif/v2.1.0/os/sarif-v2.1.0-os.html | FORMAL STANDARD |
| F63 | GitHub | Resolving code scanning alerts | 2026 | https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/resolving-code-scanning-alerts | VENDOR PATTERN |
| F64 | SonarSource | Editing issues (SonarQube Server) | 2026 | https://docs.sonarsource.com/sonarqube-server/user-guide/issues/managing | VENDOR PATTERN |
