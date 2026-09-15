#!/bin/bash
# context-check.sh — tells the truth about the lab's context architecture.
#
# READ-ONLY. This script changes nothing in the lab. It uses one scratch folder
# for section E and removes it on exit. Run it any time, before or after any change.
#
# Usage:  .claude/skills/context-check/context-check.sh            full report to screen
#         .claude/skills/context-check/context-check.sh > out.txt  save it yourself
#         or just:  /context-check
#
# Exit code: 0 when every section measured; 1 when a section could not measure (a helper
# missing or crashed, listed as ALERT lines); 2 when the root is not a lab at all.
#
# LAB_ROOT and LAB_SNAPSHOTS in the environment point it at a planted lab; the tests use them.
#
# Why it exists: five reorganization plans were written between 2026-09-04 and
# 2026-09-07 and none were executed. A plan can claim it is done. This cannot.
#
# 2026-09-15 (AD-38): every section header says [measured] or [word match]; section D
# covers docs/ and context/ and names what it leaves out; section F runs dead-pointers.py
# instead of a grep for four folder names someone already knew were dead. Same day, second
# pass: a wrong or empty root fails visibly instead of reporting a clean lab, and a helper
# that is missing or crashes is an ALERT in its section, never a blank.

set -uo pipefail

LAB="${LAB_ROOT:-/Users/venkatgullapalli/Documents/my-ai-lab}"
SNAPSHOTS="${LAB_SNAPSHOTS:-/Users/venkatgullapalli/Documents/_warehouse/_backups/snapshots}"
cd "$LAB" 2>/dev/null || { echo "NOT A LAB ROOT: $LAB does not exist; nothing was measured"; exit 2; }

# A lab root holds the front door, CLAUDE.md, and the .claude/ folder. Anything else is the
# wrong folder, and a clean report about the wrong folder would be a lie.
if [ ! -f CLAUDE.md ] || [ ! -d .claude ]; then
  echo "NOT A LAB ROOT: $LAB has no CLAUDE.md or no .claude/ folder; nothing was measured"
  exit 2
fi

SCRATCH=$(mktemp -d "${TMPDIR:-/tmp}/context-check.XXXXXX")
trap 'rm -rf "$SCRATCH"' EXIT

SKIP='/\.git/|/_backups/|/node_modules/|/\.tmp/|/\.playwright-mcp/'
SKIP_ARCH="${SKIP}|/_archive/"

live_files() { find . -type f -name "*.md" 2>/dev/null | grep -vE "$SKIP_ARCH"; }
all_files()  { find . -type f -name "*.md" 2>/dev/null | grep -vE "$SKIP"; }

rule() { printf '\n%s\n%s\n' "$1" "$(printf '=%.0s' $(seq 1 ${#1}))"; }

ALERTS=0
alert() { echo "  ALERT: $1"; ALERTS=$((ALERTS+1)); }

# run_helper <label> <script> [args...]
# Runs a helper script and prints its output (only the lines matching FILTER, when FILTER is
# set). A helper that is missing, prints nothing, or dies with a traceback is an ALERT: that
# section measured nothing, and the run exits 1 at the end. A helper that exits nonzero with
# findings of its own is not an ALERT; its findings are printed and it is named.
run_helper() {
  local label="$1" script="$2"; shift 2
  if [ ! -f "$script" ]; then
    alert "$label not present at $script; this section measured nothing"
    return
  fi
  local out="$SCRATCH/helper.out" rc
  python3 "$script" "$@" > "$out" 2>&1; rc=$?
  if [ "$rc" -ne 0 ] && { [ ! -s "$out" ] || grep -q "Traceback" "$out"; }; then
    alert "$label crashed (exit $rc); this section measured nothing. Its last lines:"
    tail -8 "$out" | sed 's/^/      /'
    return
  fi
  if [ -n "${FILTER:-}" ]; then grep -E "$FILTER" "$out" | sed 's/^/  /'; else sed 's/^/  /' "$out"; fi
  [ "$rc" -ne 0 ] && echo "  ($label exited $rc: it found problems; they are listed above)"
  return 0
}

echo "CONTEXT CHECK — $(date '+%Y-%m-%d %H:%M')"
echo "Lab: $LAB"
echo "Read-only. Nothing was changed."
echo
echo "How to read a section header:"
echo "  [measured]    a script checked the thing itself: a checksum, a path, a front-matter line, a git status. Act on it."
echo "  [word match]  a script matched words or file names, not the thing. Read the hits before acting on them."
echo "  ALERT         a section could not measure: a helper is missing or crashed. The run exits 1. Fix the sensor first."
echo
echo "Who responds: Alfred coordinates the response (identify, route, track, integrate) and may do only routine"
echo "  coordination or explicitly delegated local corrections. The responsible specialist owns substantive repair."
echo "  Venkat alone accepts an unresolved finding or approves a material change to a rule or authority;"
echo "  accepted is never counted as resolved."

# ---------------------------------------------------------------- A. recovery
rule "A. [measured] Can this be undone?"
echo "git:     $(git --version 2>&1 | head -1)"
echo "python3: $(python3 --version 2>&1 | head -1)"
echo
snap=$(ls -1t "$SNAPSHOTS"/*.tar.gz 2>/dev/null | head -1)
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
rule "B. [measured] The same file in more than one live place"
echo "(identical content by checksum — a change to one silently leaves the other stale)"
echo
live_files | while IFS= read -r f; do
  printf '%s  %s\n' "$(shasum -a 256 "$f" 2>/dev/null | cut -c1-16)" "$f"
done | sort | awk '
  { if ($1 == prev) { if (!shown) { print ""; print "  " prevpath } ; print "  " $2; shown=1 }
    else { shown=0 } ; prev=$1; prevpath=$2 }
' | head -60

# --------------------------------------------------- C. superseded but living
rule "C. [word match] Declared dead, still on the retrieval surface"
echo "(matches the words superseded, deprecated, retired, do not use, no longer near the top of a file;"
echo " a file that merely mentions those words is listed too — read each hit)"
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
rule "D. [measured] Can anything follow the connections?"
echo "(front matter = machine can read it; link = machine can follow it)"
echo "(areas: the brand record, the docs about the lab, and the context about Venkat, plus the"
echo " files that sit loose at the root of docs/ and context/)"
echo "(excluded on purpose: evidence/ is history and nothing is meant to link into it;"
echo " .claude/ is checked by skill-check.py; work-os/projects/, scheduled-tasks/, upskill-advisor/"
echo " carry their own READMEs and are not measured here yet)"
echo
printf '%-44s %6s %10s %10s\n' "AREA" "FILES" "FRONTMTR" "FOLLOWABLE"

# measure_area <label> <find arguments...>: one row per area, skipped when it has no files
measure_area() {
  local label="$1"; shift
  local t=0 y=0 l=0 f
  while IFS= read -r f; do
    t=$((t+1))
    [ "$(head -1 "$f" 2>/dev/null)" = "---" ] && y=$((y+1))
    grep -qE '\]\([^)]*\.md|\[\[[^]]+\]\]' "$f" 2>/dev/null && l=$((l+1))
  done < <(find "$@" -type f -name "*.md" 2>/dev/null | grep -vE "$SKIP_ARCH")
  [ "$t" -eq 0 ] && return 0
  printf '%-44s %6s %10s %10s\n' "$label" "$t" "$y" "$l"
}

AREAS="work-os/brand-os/voice work-os/brand-os/venkat-writing-guide
       work-os/brand-os/model work-os/brand-os/audience
       work-os/brand-os/positioning work-os/brand-os/messaging
       work-os/brand-os/terminology work-os/brand-os/context
       work-os/brand-os/engagement-os/seedbank
       work-os/brand-os/engagement-os/targets
       work-os/brand-os/engagement-os/assets
       work-os/brand-os/engagement-os/editorial
       docs/about-me docs/architecture docs/documentation docs/ecosystem
       docs/plans docs/reports docs/research
       context/intent context/sources context/state"
for area in $AREAS; do
  [ -d "$area" ] || continue
  measure_area "$area" "$area"
done
for d in docs context; do
  [ -d "$d" ] || continue
  measure_area "$d/ (files at its root)" "$d" -maxdepth 1
done
echo
echo "docs/ and context/ folders on disk not in the list above (add them, or say why not):"
missing=0
for d in docs context; do
  [ -d "$d" ] || continue
  for sub in "$d"/*/; do
    sub="${sub%/}"
    case " $(echo $AREAS) " in
      *" $sub "*) ;;
      *) echo "  $sub"; missing=$((missing+1));;
    esac
  done
done
[ "$missing" -eq 0 ] && echo "  none"

# ----------------------------------------------------------------- E. orphans
rule "E. [word match] Files nothing points at"
echo "(no other live file mentions the file's bare name — invisible unless you remember it;"
echo " a same-named file elsewhere hides an orphan, so the count is a floor, not a fact)"
echo
live_files | sed 's|.*/||' | sort -u > "$SCRATCH/names" 2>/dev/null
grep -rhoE '[A-Za-z0-9][A-Za-z0-9._-]*\.md' --include="*.md" --include="*.sh" --include="*.json" . 2>/dev/null \
  | grep -vE "$SKIP" | sort -u > "$SCRATCH/refs" 2>/dev/null
orph=0
while IFS= read -r f; do
  b="${f##*/}"
  case "$b" in README.md|CLAUDE.md|MEMORY.md|INDEX.md|AGENTS.md|STATUS.md|PLAN.md|DECISIONS.md) continue;; esac
  grep -qxF "$b" "$SCRATCH/refs" || { orph=$((orph+1)); [ "$orph" -le 25 ] && echo "  ${f#./}"; }
done < <(live_files)
echo
echo "  TOTAL ORPHANS: $orph  (of $(live_files | wc -l | tr -d ' ') live markdown files)"

# ------------------------------------------------------------ F. dead pointers
rule "F. [measured] Paths named in live files that no longer exist"
echo "(dead-pointers.py, beside this script. It replaced the grep for four known folder names on"
echo " 2026-09-15: that grep only found names someone already knew were dead. Known blind spot:"
echo " a bare file name counts as found if any file of that name exists anywhere in the lab.)"
echo
FILTER='^(OPEN|ACCEPTED|RESOLVED|LIVE DEAD POINTERS)' run_helper "dead-pointers.py" .claude/skills/context-check/dead-pointers.py

# ------------------------------------------------- G. architecture record
rule "G. [measured] Do the capability map, the definitions, and the lab agree?"
echo "(docs/architecture/check.py: the registry standard as a test. ids, statuses, paths, definitions, competing records)"
echo
run_helper "docs/architecture/check.py" docs/architecture/check.py
echo
echo "(context/sources/check.py: retrieval's source register. ids, words, locations, health, coverage, source discovery)"
echo
run_helper "context/sources/check.py" context/sources/check.py

if [ "$ALERTS" -gt 0 ]; then
  rule "Done with $ALERTS ALERT(s): the sections marked ALERT measured nothing. Nothing was changed."
  exit 1
fi
rule "Done — nothing was changed."
