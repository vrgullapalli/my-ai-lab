#!/bin/bash
# Assembles the 21 market-signal cloud prompts and their routine bodies into <pillar>/<cadence>/build/.
# Usage: ./assemble.sh   (from the market-signals folder). Needs jq. No network.
set -euo pipefail
cd "$(dirname "$0")"
S=../_shared
ENV_ID="env_011CUK7ovEXytcue7Dpm4mu5"

# pillar | cadence | routine name | title prefix | daily prefix | midweek prefix | favicon | cron UTC | model | uuid
while IFS='|' read -r dir cad name prefix dprefix mprefix fav cron model uuid; do
  [ -n "${dir:-}" ] || continue
  d="$dir/$cad"; mkdir -p "$d/build"
  case "$cad" in
    daily)     look="Pick the artifacts whose title begins with '$prefix' and read the three most recent." ;;
    wednesday) look="Pick every artifact whose title begins with '$dprefix' and carries a date from this week, Monday through today. Also pick the most recent artifact whose title begins with '$prefix'." ;;
    friday)    look="Pick every artifact whose title begins with '$dprefix' and carries a date from this week, Monday through today. Also pick the most recent artifact whose title begins with '$mprefix' and the most recent whose title begins with '$prefix'." ;;
  esac
  if [ "$dir" = "00-all-market-signals" ]; then
    push="Send exactly one mobile push notification with the PushNotification tool: the title line, then the two or three most important lines of the brief, then the artifact URL. Add one line saying the six pillar briefs for today publish after this one and appear in the same gallery. Never send a push about tool failures or partial progress, and never send more than one."
  else
    push="Do not send a push notification. This brief is one of seven in a batch, and the All Market Signals brief carries the single notification for the batch. Publishing the page is the delivery."
  fi
  out="$d/build/full-prompt.md"
  {
    cat $S/about-venkat.md; echo
    cat $S/market-lens-core.md; echo
    cat "$d/prompt.md"; echo
    cat $S/writing-rules.md; echo
    cat $S/network-limits.md; echo
    sed -e "s|{{PREFIX}}|$prefix|g" -e "s|{{FAVICON}}|$fav|g" $S/delivery-corpus.md \
      | awk -v l="$look" -v p="$push" '{gsub(/\{\{LOOKBACK\}\}/,l); gsub(/\{\{PUSH_RULE\}\}/,p); print}'
  } > "$out"
  jq -n --arg name "$name" --arg cron "$cron" --arg uuid "$uuid" --arg model "$model" \
        --arg env "$ENV_ID" --rawfile prompt "$out" '
    { name: $name, cron_expression: $cron, enabled: true, clear_mcp_connections: true,
      job_config: { ccr: { environment_id: $env,
        session_context: { model: $model, sources: [],
          allowed_tools: ["WebSearch","WebFetch","Read","Write","Bash","Glob","Grep","Artifact","PushNotification"] },
        events: [ { data: { uuid: $uuid, session_id: "", type: "user", parent_tool_use_id: null,
                            message: { content: $prompt, role: "user" } } } ] } } }' \
    > "$d/build/routine-body.json"
  printf '%-46s %5s words  %s  %s\n' "$name" "$(wc -w < "$out" | tr -d ' ')" "$cron" "$model"
done < routines.tsv
