# Plan: the restore-and-diff check for driver 2 (F-20260913-0540-1), 2026-09-14

**One line:** after each snapshot, unpack it in a scratch folder, count and checksum both trees, and print one `restore check:` line for the facts sheet; a planted bad file must turn that line into an ALERT.

**What it proves.** Driver 2 in `context/intent/STANDING.md` says "My work survives the loss of any one machine" and "Working when: a clean restore has been run and verified against the source." Its own next step: "the restore-and-diff becomes a scheduled sensor, so the invariant is measured, not remembered." The last restore was done by hand on 2026-09-10 (Alfred's log, 12:40: "restore diffed"). Nothing has checked since.

**Design point.** Compare the restore with the lab at the moment the snapshot was made, not days later. A test today against the 09-10 tar shows 4,909 files in the lab that the tar lacks. That is four days of work, not a bad backup. So the check runs right after `snapshot.sh`, on the tar it just wrote.

**Steps and exact commands.** Add a script `restore-check.sh` next to `snapshot.sh` in `~/Documents/_warehouse/_backups/`. It does this:
```
TAR=$(ls -t ~/Documents/_warehouse/_backups/snapshots/*.tar.gz | head -1)
R=$(mktemp -d /tmp/restore-check.XXXXXX)
tar -xzf "$TAR" -C "$R"
tree_sum() { cd "$1" && find . -type f -not -path './.venv/*' -not -path '*/node_modules/*' -not -name '.DS_Store' \
  -not -path '*/.next/*' -not -path '*/.playwright-mcp/*' -not -path '*/__pycache__/*' \
  -not -path './work-os/upskill-advisor/.env' -not -path './work-os/upskill-advisor/telegraph/.env' \
  -not -path './work-os/projects/worthy-tool-v2/.env.local' | LC_ALL=C sort | tr '\n' '\0' \
  | xargs -0 shasum -a 256 | shasum -a 256 | cut -c1-16; }
A=$(tree_sum "$R"); B=$(tree_sum ~/Documents/my-ai-lab)
NA=$(find "$R" -type f | wc -l | tr -d ' '); NB=$(find ~/Documents/my-ai-lab -type f | wc -l | tr -d ' ')
if [ "$A" = "$B" ]; then echo "restore check: $(basename $TAR) restored, $NA files, tree checksum matches the lab"
else echo "ALERT restore check: $(basename $TAR) restored but differs from the lab ($NA vs $NB files, checksums $A vs $B)"; fi
rm -rf "$R"
```
The exclude list is the same one `snapshot.sh` uses, so the two trees are compared on equal terms. The script writes its one line to `~/Documents/_warehouse/_backups/snapshots/restore-check.last`. `facts.py` reads that file and prints the line on the facts sheet, with the date; if the file is older than the newest tar, it prints `ALERT restore check: not run since the last snapshot`.

**Cost, measured today on the 09-10 tar.** Unpack: 2.8 seconds. Checksum the restore: 1.4 seconds. Checksum the lab: 2.4 seconds. About 7 seconds in all. Disk: 344 MB in `/tmp`, freed at the end. The disk has 1.6 TB free.

**How often and what starts it.** Once per snapshot. Recommended: `snapshot.sh` calls `restore-check.sh` as its last step, so no one has to remember. The open routine already runs `facts.py open` each first session, so the line shows up the next morning with no new job. Second option: a launchd job like `com.venkat.session-sync` that runs both scripts daily at 12:30. That adds a plist to keep alive and a second Full Disk Access grant to watch; only worth it if snapshots also move to a schedule.

**The planted-fault test (do this before trusting it).** Run the check once and confirm the good line. Then, inside a copy of the unpacked scratch restore, append one line to one file, for example `echo x >> $R/CLAUDE.md`, and run the compare step again. The line must change to the ALERT form. Done by hand today: the tree checksum went from `081e04a76096b29f` to `d74d8af930b19b03` with one file touched, and back again when the change was undone. Also test the second fault: delete `restore-check.last` and confirm `facts.py` prints the "not run" ALERT. Record both runs with `prove-it-can-fail`.

**What it must never do.** Never write into the lab. Never touch the warehouse tar except to read it. Never delete anything except its own scratch folder under `/tmp`. Never run `git`. Never print file contents, only counts and checksums, so no secret can leak onto the facts sheet.

**Known limits.** It proves the tar unpacks and matches the lab. It does not prove the Dropbox copy unpacks; add the same check on the Dropbox tar later if wanted. Files the snapshot skips on purpose (the three `.env` files) are not covered, by design.
