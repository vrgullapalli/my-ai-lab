#!/bin/bash
# context-check.sh — tells the truth about the lab's context architecture.
#
# READ-ONLY. This script writes nothing, moves nothing, deletes nothing.
# It only looks and reports. Run it any time, before or after any change.
#
# Usage:  .claude/skills/context-check/context-check.sh            full report to screen
#         .claude/skills/context-check/context-check.sh > out.txt  save it yourself
#         or just:  /context-check
#
# Why it exists: five reorganization plans were written between 2026-09-04 and
# 2026-09-07 and none were executed. A plan can claim it is done. This cannot.

set -uo pipefail

LAB="/Users/venkatgullapalli/Documents/my-ai-lab"
cd "$LAB" || { echo "lab not found: $LAB"; exit 1; }

SKIP='/\.git/|/_backups/|/node_modules/|/\.tmp/|/\.playwright-mcp/'
SKIP_ARCH="${SKIP}|/_archive/"

live_files() { find . -type f -name "*.md" 2>/dev/null | grep -vE "$SKIP_ARCH"; }
all_files()  { find . -type f -name "*.md" 2>/dev/null | grep -vE "$SKIP"; }

rule() { printf '\n%s\n%s\n' "$1" "$(printf '=%.0s' $(seq 1 ${#1}))"; }

echo "CONTEXT CHECK — $(date '+%Y-%m-%d %H:%M')"
echo "Lab: $LAB"
echo "Read-only. Nothing was changed."

# ---------------------------------------------------------------- A. recovery
rule "A. Can this be undone?"
echo "git:     $(git --version 2>&1 | head -1)"
echo "python3: $(python3 --version 2>&1 | head -1)"
echo
snap=$(ls -1t /Users/venkatgullapalli/Documents/_warehouse/_backups/snapshots/*.tar.gz 2>/dev/null | head -1)
if [ -n "$snap" ]; then
  echo "Last full snapshot: $(basename "$snap")  ($(( ( $(date +%s) - $(stat -f %m "$snap") ) / 86400 )) days old)"
else
  echo "Last full snapshot: NONE FOUND  <-- nothing outside git is protected"
fi
echo
printf '%-46s %8s  %s\n' "REPO" "UNCOMMIT" "LAST COMMIT"
while IFS= read -r g; do
  r="${g%/.git}"
  n=$(git -C "$r" status --porcelain 2>/dev/null | wc -l | tr -d ' ')
  d=$(git -C "$r" log -1 --format=%cd --date=short 2>/dev/null)
  flag=""; [ "$n" -gt 0 ] && flag=" <-- unprotected"
  printf '%-46s %8s  %s%s\n' "${r#./}" "$n" "${d:-never}" "$flag"
done < <(find . -maxdepth 5 -name ".git" -type d 2>/dev/null | grep -vE '/_backups/|/\.tmp/' | sort)
echo
echo "Folders with no repo and no protection but git:"
for d in evidence context work-os/scheduled-tasks work-os/upskill-advisor; do
  [ -d "$d" ] && [ ! -d "$d/.git" ] && echo "  $d  ($(find "$d" -type f 2>/dev/null | wc -l | tr -d ' ') files)"
done

# -------------------------------------------------------------- B. duplicates
rule "B. The same file in more than one live place"
echo "(identical content — a change to one silently leaves the other stale)"
echo
live_files | while IFS= read -r f; do
  printf '%s  %s\n' "$(shasum -a 256 "$f" 2>/dev/null | cut -c1-16)" "$f"
done | sort | awk '
  { if ($1 == prev) { if (!shown) { print ""; print "  " prevpath } ; print "  " $2; shown=1 }
    else { shown=0 } ; prev=$1; prevpath=$2 }
' | head -60

# --------------------------------------------------- C. superseded but living
rule "C. Declared dead, still on the retrieval surface"
echo "(seed A-LIVE-101: declaring a new canonical source is only half the migration)"
echo
found=0
while IFS= read -r f; do
  case "$f" in */_archive/*) continue;; esac
  if head -40 "$f" 2>/dev/null | grep -qiE '^\s*(>|#|\*\*)?\s*(superseded|deprecated|retired|do not use|no longer)'; then
    dir=$(dirname "$f")
    sib=$(find "$dir" -maxdepth 1 -name "*.md" 2>/dev/null | wc -l | tr -d ' ')
    printf '  %s\n      still live, %s files in that folder\n' "${f#./}" "$sib"
    found=$((found+1))
  fi
done < <(live_files)
[ "$found" -eq 0 ] && echo "  none found"

# ------------------------------------------------------------- D. linkability
rule "D. Can anything follow the connections?"
echo "(front matter = machine can read it; link = machine can follow it)"
echo
printf '%-44s %6s %10s %10s\n' "AREA" "FILES" "FRONTMTR" "FOLLOWABLE"
for area in work-os/brand-os/voice work-os/brand-os/venkat-writing-guide \
            work-os/brand-os/model work-os/brand-os/audience \
            work-os/brand-os/positioning work-os/brand-os/messaging \
            work-os/brand-os/terminology work-os/brand-os/context \
            work-os/brand-os/engagement-os/seedbank \
            work-os/brand-os/engagement-os/targets \
            work-os/brand-os/engagement-os/assets \
            work-os/brand-os/engagement-os/editorial \
            chief-of-staff _audit; do
  [ -d "$area" ] || continue
  t=0; y=0; l=0
  while IFS= read -r f; do
    t=$((t+1))
    [ "$(head -1 "$f" 2>/dev/null)" = "---" ] && y=$((y+1))
    grep -qE '\]\([^)]*\.md|\[\[[^]]+\]\]' "$f" 2>/dev/null && l=$((l+1))
  done < <(find "$area" -type f -name "*.md" 2>/dev/null | grep -vE "$SKIP_ARCH")
  [ "$t" -eq 0 ] && continue
  printf '%-44s %6s %10s %10s\n' "$area" "$t" "$y" "$l"
done

# ----------------------------------------------------------------- E. orphans
rule "E. Files nothing points at"
echo "(no other live file mentions them by name — invisible unless you remember them)"
echo
live_files | sed 's|.*/||' | sort -u > /tmp/.cc_names 2>/dev/null
grep -rhoE '[A-Za-z0-9][A-Za-z0-9._-]*\.md' --include="*.md" --include="*.sh" --include="*.json" . 2>/dev/null \
  | grep -vE "$SKIP" | sort -u > /tmp/.cc_refs 2>/dev/null
orph=0
while IFS= read -r f; do
  b="${f##*/}"
  case "$b" in README.md|CLAUDE.md|MEMORY.md|INDEX.md|AGENTS.md|STATUS.md|PLAN.md|DECISIONS.md) continue;; esac
  grep -qxF "$b" /tmp/.cc_refs || { orph=$((orph+1)); [ "$orph" -le 25 ] && echo "  ${f#./}"; }
done < <(live_files)
echo
echo "  TOTAL ORPHANS: $orph  (of $(live_files | wc -l | tr -d ' ') live markdown files)"

# ------------------------------------------------------------ F. dead pointers
rule "F. Pointers to folders that no longer exist"
for p in "my-ai-lab-v2/" "My_AI_Lab/" "brand-identity/" "decision-products/"; do
  n=$(grep -rlF "$p" --include="*.md" . 2>/dev/null | grep -vE "$SKIP" | wc -l | tr -d ' ')
  printf '  %-24s %5s files mention it\n' "$p" "$n"
done
echo
echo "  (in dated records these are correct history — leave them. In live pointers they are bugs.)"

# ------------------------------------------------- G. architecture record
rule "G. Do the capability map, the definitions, and the lab agree?"
echo "(docs/architecture/check.py: the registry standard as a test. ids, statuses, paths, definitions, competing records)"
echo
python3 docs/architecture/check.py 2>&1 | sed 's/^/  /'

rule "Done — nothing was changed."
