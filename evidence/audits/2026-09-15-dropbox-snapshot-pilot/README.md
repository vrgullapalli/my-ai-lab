# Dropbox snapshot-folder pilot, 2026-09-15

The first pilot of the Organization Standard (`docs/architecture/ORGANIZATION-STANDARD.md`, approved AD-40 at 02:51), run at Venkat's /goal of 02:51 from the MacBook Pro. New files only; nothing here is edited after the day.

| File | What it holds |
|---|---|
| `00-preflight.txt` | machine, the absence of an iMac mount (deviation, stated), Dropbox client, writability, six files |
| `01-baseline-before.txt` | sha256 of all six files before any change, control one |
| `02-move.sh`, `02-move.log` | the exact commands run, with the reverse command; revalidate at each write (control two), copy, verify, remove |
| `03-verify-after.txt` | reconciliation against the baseline in both directions (control three): 6 planned, 6 found, 0 missing, 0 unplanned, 0 differing, 0 left behind |
| `04-rescan-role-map.txt` | the re-scan: 2 markers, 1 id, 0 findings, manifests verified |

**Result.** One canonical home for the lab's snapshot files: Dropbox `my-ai-lab-backups/` (id `my-ai-lab-snapshots`, role derived, built by `snapshot.sh`). The old location `my-ai-lab/` holds only its tombstone `ROLE.md` with `replaced-by`. The canonical lab on the MacBook was not touched. `facts.py` was not changed; its "last off-machine copy" line still resolves (2026-09-10 snapshot, 4 days old) because the canonical stayed at the path it already read. That line is still a path copy, which the standard names as a stale-path risk; replacing it with a lookup by id is a follow-up, not part of this pilot.

**Proof the check can fail.** `.claude/skills/context-check/tests/role_map_tests.py`, ten cases on a planted estate: clean, duplicate canonical (interrupt), resolved by rerun, chain longer than one hop, one-way supersession, write after supersession, unconfirmed canonical, manifest drift, read-only, wrong root. All passed 2026-09-15 02:57.
