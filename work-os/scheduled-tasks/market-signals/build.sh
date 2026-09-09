#!/bin/bash
# Assembles the market-signal prompts from _schema/ plus each pillar's deltas.txt.
# Usage: ./build.sh   (from the market-signals folder). No network. Writes only <pillar>/<cadence>/prompt.md.
set -euo pipefail
cd "$(dirname "$0")"
for pillar in [0-9]*/ ; do
  pillar=${pillar%/}
  for cadence in daily wednesday friday; do
    d="$pillar/$cadence"
    [ -f "$d/deltas.txt" ] || continue
    { printf '{{HEADER}}\n\n'; cat "_schema/$cadence.md"; } > "$d/.merged"
    cat _schema/defaults.txt "$d/deltas.txt" > "$d/.deltas"; awk -f _schema/fill.awk "$d/.deltas" "$d/.merged" > "$d/.filled"
    # squeeze runs of blank lines to one
    cat -s "$d/.filled" > "$d/prompt.md"
    rm -f "$d/.merged" "$d/.filled" "$d/.deltas"
    printf '%-44s %s words\n' "$d/prompt.md" "$(wc -w < "$d/prompt.md" | tr -d ' ')"
  done
done
