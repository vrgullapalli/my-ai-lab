# Storage Estate Baseline — 2026-09-14

**Amended 2026-09-15.** Section 1 (size), section 4 (object count) and section 5 (exemption)
revised after the estate-wide hash sweep completed and Account B was swept. Superseded figures
are struck through in place rather than deleted; see §11 Amendment Record.

**Purpose.** Factual baseline of the storage estate, device topology, sync and protection state,
for use as a research input. This document records measurement, not proposals. It contains no
design, no recommended structure, and no migration plan.

**Companion baseline.** `CURRENT-REGISTRIES-CHECKS-SENSORS.md` covers registries, checks and
sensors inside the Lab. This document covers the estate the Lab sits in.

**Evidence location.** `~/DriveAtlas/` — per-territory manifests, duplicate ledger with content
hashes, per-file move logs with reversal commands, run log, run brief with dated rulings.
DriveAtlas is operational evidence and is deliberately not copied into the Lab.

**Claim labelling.** VERIFIED = measured or hash-proven by a stated method. CLAIMED = owner's
account, recorded as such. UNKNOWN = not established.

**Method for all VERIFIED file-level figures.** Full metadata sweep of Dropbox Account A via
`rclone lsf -R` (paths, sizes, modification times; zero content reads), 2026-09-13, 964,867 files.
Hash verification via Dropbox server-side `content_hash` (SHA-256 over 4 MB blocks, then SHA-256
of concatenated block hashes) read through the API — no bytes downloaded. 125,970 files hashed.

---

## 1. Estate size

| Point in time | Pool used | Status |
|---|---|---|
| 2026-09-13 06:00 | 10.253 TiB | VERIFIED (`rclone about`) |
| 2026-09-14 | **5.691 TiB** | VERIFIED |

Reduction 4.560 TiB (44%). Free space 4.747 → 9.309 TiB of a 16.49 TiB pooled quota.

Any figure of 7.33 TiB in earlier material is superseded; it was a lagging usage counter observed
mid-deletion. Dropbox's reported usage trails large deletions by hours.

**Composition of the reduction.** VERIFIED:
- 2.57 TiB — redundant copies, hash-confirmed, 132 clusters above 1 GB across 529 files
- ~2.9 TB — 2021 screen recordings, deleted by the owner after inspection
- 0 TiB — consolidation of a second Dropbox member account into the primary (both were members of
  one team sharing one quota pool; the transfer removed a second canonical namespace, not storage)

## 2. Device and store topology

| Node | Role | State |
|---|---|---|
| iMac (primary workstation) | intended full-estate node | 7.3 TiB volume, 2.6 TiB used, 4.7 TiB free · VERIFIED |
| MacBook | intended selective working node | **NOT OBSERVED — see note below** |
| Dropbox (Telisina team) | replication / transport | 5.691 TiB · VERIFIED |
| iCloud Drive | currently holds the canonical Lab | 12,787 files · VERIFIED |
| Seagate external, 1.8 TB | Time Machine destination | see §6 |

**Machine identity — correction of record, 2026-09-14.** The iMac's boot volume is named
`MacBookHD`, and `/Volumes/MacBookHD` is a symlink to `/` on the iMac itself. This was initially
mistaken for a mounted MacBook. **No second machine has been observed at any point in this work.**
Every figure previously described as an iMac-versus-MacBook comparison was the iMac compared to
itself and is withdrawn, specifically: the claim that the Lab model folder was byte-identical
across both machines, and the claim that the MacBook's copy of the superseded lab was twelve days
stale. Neither was measured. MacBook state is UNKNOWN.

The underlying lesson is the same one this estate keeps producing: a volume name is not evidence
of what a volume is. The name was accepted without checking the device.

**Two local Dropbox roots exist.** The active sync root is `~/Telisina Dropbox/Venkat Gullapalli/`.
A legacy `~/Dropbox/` folder also exists holding 12 GB across 5 folders. An earlier local-footprint
figure derived from the legacy folder was wrong and is withdrawn. Current local Dropbox footprint:
UNKNOWN — the active root is not readable under present access constraints.

**Two folders present to the user as "Documents".** `~/Documents/` on local disk, and
`~/Library/Mobile Documents/com~apple~CloudDocs/Documents/` in iCloud Drive. Finder displays both
as "Documents". The Lab resides in the second. Materialising iCloud content downloads it in place
and does not relocate it. This ambiguity has already produced one misidentification of the Lab's
location during this work.

## 3. Structural measurements (bear on machine navigability)

VERIFIED, estate-wide across 964,867 files:

| Measure | Value |
|---|---|
| Folders containing exactly one child | **12,103 of 21,206 — 57.1%** |
| Path segments carrying no information | **751,606 of 7,340,880 — 10.2%** |
| Files beneath an uninformative segment | **241,966 — 25% of estate, 1,683 GB** |
| Of those, files modified after 2023 | **24** |

Uninformative segments counted include `untitled folder*`, `new folder with items*`, `backup stuff`,
`desktop backup*`, `misc`, `temp`, and one segment named `old dropbox wewerwewer` containing
134,972 files.

**Observed cause.** Recursive backup nesting: each backup absorbed its predecessor whole. One
personal video exists in 7 locations; one template archive in 6; one dataset pair in 8.
Representative path:
`New Folder With Items/untitled folder 4/untitled folder 3/Old Bootable Desktop/New Folder With Items 3/New Folder With Items/50th Anniversary/`

**Composition of the 241,966-file region** (rule-based classification, CLAIMED accuracy):
work artifacts 698 GB · unclassified 469 GB · personal 272 GB · purchased design-asset libraries
242 GB across 121,464 files · code 2.4 GB.

## 4. Object count versus storage size

VERIFIED. Distribution by content class:

| Class | Files | Size |
|---|---|---|
| images + design | **670,685** | 0.56 TiB |
| everything else | 203,640 | 0.52 TiB |
| documents | 56,104 | 0.67 TiB |
| video | 23,310 | 4.18 TiB* |
| data + archives | 11,128 | 3.49 TiB |

*pre-deletion figure.

**`images + design` is 70% of the estate's file count in 10% of its bytes**, largely purchased
stock icon libraries. Enumeration cost, sync cost and index cost scale with object count, not size.

**Worked case.** One stock icon library was found duplicated:

| Path | Files | Size |
|---|---|---|
| `New Folder With Items/Old Dropbox wewerwewer/My Documents/MDK ICONS/` | 26,405 | 2.07 GB |
| `New Folder With Items/BACKUP STUFF/Old Dropbox wewerwewer/My Documents/MDK ICONS/` | 26,405 | 2.07 GB |

VERIFIED: zero differences across all 26,405 relative paths and byte sizes; 1,337 files
hash-sampled across four sub-bundles, every combined hash identical. Collapsing recovers 2.07 GB
and removes 26,405 objects from every sync operation and every directory enumeration.

**Screenshot age distribution.** VERIFIED: 53,160 files older than six months; 203 newer. 99.6%.

## 5. Governed exemption in progress

The duplicated icon library is being consolidated into a single archive file, placed in an archive
area, and set to online-only. This deliberately sacrifices item-level searchability and agent
navigability for a corpus judged replaceable (purchased stock art, re-downloadable).

Recorded as a **deliberate exemption with stated rationale**, not an oversight. Status: **COMPLETE, 2026-09-14.** `Archive/MDK-ICONS-2026-09-14.zip`, 1.61 GiB, 26,405 file
entries, content hash verified identical on both sides. Two source trees (26,405 files each)
quarantined; **52,810 objects removed from the working estate for ~2 GB of space.**

## 6. Protection state

**Sync.** Dropbox operates on both machines. iCloud currently synchronises the Lab between them.
The owner has decided to discontinue iCloud use. No replacement sync mechanism has been selected.
Status: UNRESOLVED.

**Backup.** VERIFIED, and stated using protection-state distinctions rather than a single flag:

| State | Value |
|---|---|
| Configured | YES — destination `Seagate-Backup`, 1.8 TB, registered with Time Machine |
| Running | NO — `tmutil currentphase` returns `BackupNotRunning` |
| Completed | **NO — `tmutil latestbackup` returns no backups for this machine** |
| Restore-verified | NO |
| Degraded / failed | Destination 95% full (93 GB free) holding one `.interrupted` and one `.inprogress` attempt, both dated 2026-09-10 |

**Root cause.** Source volume is 2.6 TiB; destination is 1.8 TB. The operation cannot complete and
will continue consuming the destination while failing.

A configured, actively-consuming destination with zero completed backups presents as healthy to
casual inspection. Owner has deferred remediation; recorded as an open reliability gap.

## 7. Canonicality state

The career/capability model has occupied three locations. VERIFIED:

| Location | Period | Forward pointer |
|---|---|---|
| `career-advisor/career-evolution/` | to 2026-09-02 | YES — banner file → brand-identity |
| `my-ai-lab-v2/brand-identity/model/` | 2026-09-02 → 09-09 | **NONE — no file in it references `work-os`** |
| `my-ai-lab/work-os/brand-os/model/` | since 2026-09-09 | canonical; sole copy asserting this |

**The supersession chain terminates at a non-canonical node.** A consumer traversing it reaches the
middle location, finds a complete artifact set including a README and a status file, and stops.
This occurred during this work. `capabilities.json` is byte-identical across all three
(hash `a30be6a33b13…`), so no content claim is affected; an update directed at either superseded
path would write into a frozen snapshot.

**Existing checks do not detect this.** VERIFIED: `validate_and_render.py` reports
`OK: 81 records valid`. Of those 81 records, **0 reference `work-os`**; 31 reference the superseded
lab; 2 reference Dropbox. Every recorded path resolves, because superseded copies remain on disk.
The check has reported healthy for five days against a topology that changed on 2026-09-09.

This is a sensing gap by construction: the check answers *does this path resolve* and not *is this
path still canonical*. Distinct sensor classes are implied — canonicality drift and supersession
drift — neither of which is reducible to integrity checking.

**Textual reference surface.** VERIFIED: 438 files across the superseded lab contain a path string
naming a superseded location. Most are dated records for which the path was correct when written.

## 8. Evidence on mutating operations

Two distinct controls were exercised during this work, with different outcomes. Both are VERIFIED.

**Write-time revalidation — held.** During the duplicate collapse the owner was concurrently
deleting files, so the precomputed plan went stale within hours. The executing process re-verified
existence and content hash of *both* the retained copy and the redundant copy immediately before
each move, skipping on any mismatch. Result across 397 planned operations: 388 executed, **9 skipped,
0 failures**. In two of those skips the control prevented permanent loss of the last remaining copy
of a 21.7 GB archive and a 13.0 GB archive, whose retained counterparts the owner had deleted
minutes earlier. A more recent scan would have shortened the staleness window, not closed it.

**Baseline capture — omitted, and unrecoverable.** The second-account consolidation was executed
before its pre-transfer manifest was built. Verification was therefore possible only at
folder-name granularity: 32 folders recorded beforehand, 32 present afterwards, exact match in both
directions. **File-level completeness is unproven and now unprovable** — no baseline exists to
compare against, and the source account no longer exists.

These are two separate requirements, not one. Revalidating state immediately before a write does
not enable verification after it. A third control — post-change verification against a captured
baseline — was available in the first case and impossible in the second.

## 9. Reorganization status

**No reorganization has been performed.** All 29 original top-level folders in Dropbox Account A
remain at their original paths, including one containing 186,336 files. Six candidate target
folders were created and remain empty. No file has been filed into any of them.

Completed operations are limited to: metadata sweep, hash verification, duplicate quarantine
(reviewed and cleared by the owner), owner-initiated deletions, account consolidation, and the
in-progress icon consolidation. All are reduction or measurement. None commits to an organizational
vocabulary.

## 10. Open decisions

| # | Decision | Status |
|---|---|---|
| 1 | Organizational vocabulary for the estate | UNRESOLVED — gates any filing |
| 2 | Cross-machine sync mechanism after iCloud | UNRESOLVED |
| 3 | Backup and recovery capability | UNRESOLVED — deferred by owner, recorded as a reliability gap |
| 4 | Canonical storage topology per artifact class | UNRESOLVED |
| 5 | Disposition of the superseded lab alongside the current one | UNRESOLVED |

The owner has stated that the existing `work-os` structure is "not ideally organized" (CLAIMED),
which bears on whether its vocabulary should govern a future model.

---

## 11. Amendment Record — 2026-09-15

### A. Estate size — §1 superseded
The hash sweep completed and Account B was swept. Figures covering Account A alone are superseded.

| Metric | Was (Account A only) | Now (both accounts) |
|---|---|---|
| Files | 964,867 | **1,650,074** |
| Pool used | 5.691 TiB | 5.768 TiB |

Estate file count is **71% larger** than §1 records. The earlier figure predates the account
consolidation and covered one account.

### B. Duplication — VERIFIED at every size tier, whole estate
Method: `rclone lsf -R --format "hsp" --hash dropbox`, one recursive pass per folder returning
Dropbox server-side `content_hash`. Zero bytes downloaded. Account A: 36 of 37 folders, 938,039
files. Account B: 32 of 32 subfolders, 712,035 files. All hashes valid 64-character values.

| Metric | Value |
|---|---|
| Duplicate clusters | **254,905** |
| **Redundant files (extra copies)** | **723,197 — 43.8% of the estate** |
| **Recoverable** | **1.53 TiB** |

By tier, Account A:

| Band | Clusters | Recoverable |
|---|---|---|
| over 1 GB | **0** | 0 |
| 1 MB – 1 GB | 38,532 | 1.12 TiB |
| 100 KB – 1 MB | 46,380 | 30.3 GB |
| under 100 KB | 101,461 | 3.4 GB |

**The zero in the top band independently validates the 2026-09-13 purge** — 132 clusters and
2.57 TiB were removed above 1 GB and none remain. The control confirms itself.

This strengthens §4: object count, not storage size, is the binding constraint. **723,197
redundant objects** is the material figure; 1.53 TiB is secondary.

### C. Cross-account overlap — a recorded prediction, disproved
Predicted 2026-09-14: the two accounts would overlap heavily, both holding Medikly-era material
across the same years. Tested by set intersection of content hashes:

| Measure | Value |
|---|---|
| Distinct content in A | 428,462 |
| Distinct content in B | 519,650 |
| Present in BOTH | **21,235 — 4.1% of B's distinct content** |
| Cross-account duplicated bytes | **0.08 TiB** |

**Disproved.** Shared era, shared company and shared naming conventions predicted nothing about
shared content. Provenance similarity is not content similarity. The consolidation was correct for
namespace reasons; it yielded no duplicate dividend.

B's redundancy is internal: 712,035 files, 519,650 distinct — **192,385 redundant files within B**,
largely independent of A.

### D. Machine identity and the Lab location — resolved since §2
- The Lab was moved out of iCloud to `~/Documents/my-ai-lab` on the iMac and **verified clean**:
  13,065 files, 0 iCloud stubs, and across two git repositories only 1 modified file and 2 deleted
  `.DS_Store`. A hollowed-out file would have appeared as a modification; none did. A checkpoint
  commit (`e47865e "Checkpoint before the lab leaves iCloud sync, at Venkat's word"`) made that
  verification possible — baseline capture working as intended.
- The iCloud original has been deleted by the owner. The replica question in §2 is closed.
- **MacBook state remains UNKNOWN.** No second machine has been observed.

### E. Lab structure — first measurement
5,897 files in 198 folders (excluding `.git`, `.venv`, `node_modules`).

| Finding | Value |
|---|---|
| `work-os` declared areas holding **zero** files | `references`, `_archive`, `skills` |
| A fourth area holding 3 files | `assets` |
| Largest area is misfiled | `upskill-advisor` is 2,132 files, **98.6% a nested `telegraph` project** belonging in `projects/` |
| Folders with exactly one child | 84 of 198 — **42.4%** (estate: 57.1%) |
| Internal duplication | 148 clusters, **2.7 MB** — negligible |
| Age | all content 2026-08 / 2026-09; root repo 36 commits, all since 2026-09-09 |

**The Lab is a design problem, not a hygiene problem.** Nothing is dead, duplicated or old;
declared structure and occupied structure simply diverge. This contrasts with the Dropbox estate,
where reduction did most of the work. It argues the Lab reorganization should follow the standard
rather than precede it — there is no reduction dividend to collect there first.

### F. Prior art located — capability-based organization was specified and never adopted
`chief-of-staff/operating-model/` holds `chief-of-staff-foundry-operating-model` v0.1.0-rc.1
(2026-08-22): `active_version: null`, `lifecycle_state: candidate`, `activation.approved: false`.
Scope: *"Content Foundry, Decision Foundry, Client Foundry, and later foundries."* RFC 2119
keywords, per-rule `[rule-id]` tags for conformance testing, versioned registry with checksums.

No rejection exists in DECISIONS.md. **It stalled at the adoption gate.** Remnants persist:
`work-os/projects/decision-foundry/` (109 files), named in the Lab's `CLAUDE.md` as a peer of two
ordinary projects — the organizing concept demoted to a sibling of what it was meant to organize.

Direct evidence that an Organization Standard requires a defined **adoption, activation and
supersession procedure**, not only a structure.

### G. Unchanged
Sections 6 (protection state), 7 (canonicality), 9 (no reorganization performed) and 10 (open
decisions) stand as written. Backup remains configured, never completed, and deferred by the owner.
The supersession chain for the career model remains broken at hop 2. **Zero files have been filed.**
