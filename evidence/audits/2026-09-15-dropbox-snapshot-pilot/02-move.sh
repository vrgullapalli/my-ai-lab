#!/bin/bash
# Pilot move: file the 2026-09-08 snapshot into the canonical home, under the three controls.
# canonical home: my-ai-lab-backups/  (id my-ai-lab-snapshots, role derived)
# old location:   my-ai-lab/          (superseded, keeps a tombstone ROLE.md)
# Reverse (undo), if ever needed:
#   cp -p "my-ai-lab-backups/my-ai-lab--2026-09-08--0622".{tar.gz,sha256,manifest.txt} my-ai-lab/ ; rm my-ai-lab/ROLE.md
#   (Dropbox version history also holds the removed files for the plan's window.)
set -euo pipefail
cd "$HOME/Library/CloudStorage/Dropbox-Telisina/Venkat Gullapalli"
BASE="$1"   # baseline file with sha256 lines
OLD=my-ai-lab; NEW=my-ai-lab-backups; STEM=my-ai-lab--2026-09-08--0622
echo "[1] declare the canonical home"
cat > "$NEW/ROLE.md" <<'ROLE'
# my-ai-lab snapshots
- id: my-ai-lab-snapshots
- role: derived
- area: work
- scope: ai-lab
- derived-from: my-ai-lab
- built: 2026-09-10
- rebuild: ~/Documents/_warehouse/_backups/snapshot.sh <this folder>
- as-of: 2026-09-15
- steward: facts.py (the "last off-machine copy" line)
- declared-by: venkat
- replaces: my-ai-lab-snapshots
- note: dated, checksummed snapshots of the lab, built by snapshot.sh and copied here as the off-machine copy. The lab itself is canonical wherever it currently lives (the MacBook on 2026-09-15). This folder's path is its current location, not its identity. The old location ../my-ai-lab is superseded (AD-40 pilot, 2026-09-15).
ROLE
for f in tar.gz sha256 manifest.txt; do
  src="$OLD/$STEM.$f"; dst="$NEW/$STEM.$f"
  want=$(grep " $src\$" "$BASE" | awk '{print $1}')
  echo "[2] revalidate $src against baseline"
  have=$(shasum -a 256 "$src" | awk '{print $1}')
  [[ "$have" == "$want" ]] || { echo "MISMATCH before copy: $src"; exit 3; }
  [[ -e "$dst" ]] && { echo "REFUSE: $dst already exists"; exit 4; }
  echo "[3] copy -p"
  cp -p "$src" "$dst"
  echo "[4] verify the copy"
  got=$(shasum -a 256 "$dst" | awk '{print $1}')
  [[ "$got" == "$want" ]] || { echo "MISMATCH after copy: $dst"; exit 5; }
  touch -r "$src" "$dst"
  echo "[5] remove the source (copy verified)"
  rm "$src"
done
echo "[6] tombstone at the old location"
cat > "$OLD/ROLE.md" <<'ROLE'
# my-ai-lab snapshots (old location, superseded)
- id: my-ai-lab-snapshots
- role: historical
- area: work
- scope: ai-lab
- as-of: 2026-09-15
- replaced-by: my-ai-lab-snapshots
- replaced-on: 2026-09-15
- steward: facts.py (the "last off-machine copy" line)
- declared-by: venkat
- note: the 2026-09-08 snapshot that lived here was copied to ../my-ai-lab-backups, verified by sha256, then removed from here on 2026-09-15 (AD-40 pilot). Nothing new is written here. The record and the reverse command are in the lab at evidence/audits/2026-09-15-dropbox-snapshot-pilot/.
ROLE
echo "[7] manifest beside the canonical marker"
( cd "$NEW" && shasum -a 256 *.tar.gz *.sha256 *.manifest.txt > MANIFEST.txt )
echo "DONE"
