# Snapshot check for the references folder (F-20260912-0220-2), 2026-09-14

**Answer:** 57 of the 137 files are in the newest tar. 80 are not. 78 of the 80 were added on 2026-09-11, after the tar was made. The two client scoping decks are in the tar.

**The tar checked:** `my-ai-lab--2026-09-10--1241.tar.gz`, made 2026-09-10 12:41, 118,069,940 bytes, 7,186 members (5,950 files), in `~/Documents/_warehouse/_backups/snapshots/`. Its checksum matches its `.sha256` file.

**The folder now:** 137 files in `work-os/brand-os/engagement-os/references/`. Git holds none of them. Line 10 of `.gitignore` in `work-os/brand-os/` skips the whole folder.

**In the tar from that folder:** 98 files. 57 match the folder today. The other 41 are the old `writing-guide/` folder, which was replaced by `writing-guide--POINTER.md` on 2026-09-11.

**Missing from the tar (80 files):**
- 78 files under `mia-kiraki/`: `README.md`, `CONNECTIONS.md`, `ADAPT-AND-EXTEND.md`, and 75 articles in `mia-kiraki/articles/`, dated 2025-07-30 to 2026-09-09. All written to disk on 2026-09-11 between 00:59 and 01:25. That is after the tar.
- `writing-guide--POINTER.md`, written 2026-09-11 23:52. Also after the tar.
- `_archive/writing-guide--2026-09-03-initial-desktop-copy/.DS_Store` (a Finder file the snapshot skips on purpose) and one `__pycache__/*.pyc` file (also skipped on purpose). Neither needs a backup.

So every real file that existed on 2026-09-10 is in the tar. The 79 real files added since have no copy anywhere: not in git, not in the tar. The full list is in `refs-missing.txt` next to this file.

**Dropbox copy: not the same bytes, and not meant to be.** The facts sheet names the Dropbox file `my-ai-lab--2026-09-10--1239.tar.gz`. It is a separate snapshot made two minutes earlier, at 12:39.
- Warehouse tar: 118,069,940 bytes, checksum starts `406ee886`. 7,186 members.
- Dropbox tar: 118,069,406 bytes, checksum starts `c041b50f`. 7,185 members. Matches its own `.sha256`.
- The only member difference is one log file, `.remember/logs/autonomous/save-124121.log`, in the warehouse tar only. The references folder is the same 98 files in both.

**One thing seen along the way:** `work-os/projects/_archive/` holds 2,714 files today. The front door says no `_archive/` may live in the lab. Not part of this task; flagging it.
