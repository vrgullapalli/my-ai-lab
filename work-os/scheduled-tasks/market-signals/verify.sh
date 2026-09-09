#!/bin/bash
# Compares every live market-signal routine's prompt against its build/full-prompt.md.
# Usage: ./verify.sh <dir-of-RemoteTrigger-json-responses>
# Each input file: an HTTP status line, then JSON with .trigger.name and
# .trigger.derived_state.prompt (a create/update/get response). Prints OK or DIFF per routine.
set -uo pipefail
cd "$(dirname "$0")"
TR="${1:?usage: ./verify.sh <dir-of-json-responses>}"
TMP=$(mktemp); trap 'rm -f "$TMP"' EXIT
map() { case "$1" in
 "Signals: All Market, Daily") echo 00-all-market-signals/daily;;
 "Signals: All Market, Midweek") echo 00-all-market-signals/wednesday;;
 "Signals: All Market, Weekly") echo 00-all-market-signals/friday;;
 "Signals: Foundation, Daily") echo 01-foundation/daily;;
 "Signals: Foundation, Midweek") echo 01-foundation/wednesday;;
 "Signals: Foundation, Weekly") echo 01-foundation/friday;;
 "Signals: Meaning and Context, Daily") echo 02-meaning-and-context/daily;;
 "Signals: Meaning and Context, Midweek") echo 02-meaning-and-context/wednesday;;
 "Signals: Meaning and Context, Weekly") echo 02-meaning-and-context/friday;;
 "Signals: Use Case, Daily") echo 03-use-case/daily;;
 "Signals: Use Case, Midweek") echo 03-use-case/wednesday;;
 "Signals: Use Case, Weekly") echo 03-use-case/friday;;
 "Signals: Operating Model, Daily") echo 04-operating-model/daily;;
 "Signals: Operating Model, Midweek") echo 04-operating-model/wednesday;;
 "Signals: Operating Model, Weekly") echo 04-operating-model/friday;;
 "Signals: Trust and Control, Daily") echo 05-trust-and-control/daily;;
 "Signals: Trust and Control, Midweek") echo 05-trust-and-control/wednesday;;
 "Signals: Trust and Control, Weekly") echo 05-trust-and-control/friday;;
 "Signals: Repeatability and Scale, Daily") echo 06-repeatability-and-scale/daily;;
 "Signals: Repeatability and Scale, Midweek") echo 06-repeatability-and-scale/wednesday;;
 "Signals: Repeatability and Scale, Weekly") echo 06-repeatability-and-scale/friday;;
esac; }
# newest response per routine name wins
for f in $(ls -t "$TR"/*.txt 2>/dev/null); do
  n=$(tail -n +2 "$f" 2>/dev/null | jq -r '.trigger.name // empty' 2>/dev/null)
  case "$n" in "Signals: "*) ;; *) continue;; esac
  grep -qxF "$n" "$TMP" && continue
  echo "$n" >> "$TMP"
  d=$(map "$n"); [ -z "$d" ] && { echo "NO MAP  $n"; continue; }
  tail -n +2 "$f" | jq -j '.trigger.derived_state.prompt' > "$d/build/.live"
  if [ "$(md5 -q "$d/build/.live")" = "$(md5 -q "$d/build/full-prompt.md")" ]
    then echo "OK      $n"
    else echo "DIFF    $n  ($d)"; diff "$d/build/.live" "$d/build/full-prompt.md" | head -10
  fi
  rm -f "$d/build/.live"
done | sort
