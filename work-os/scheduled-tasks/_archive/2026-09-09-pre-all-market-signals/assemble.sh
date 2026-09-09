#!/bin/bash
# Builds each task's full cloud prompt and its routine body into <task>/build/.
# Usage: ./assemble.sh   (from this folder). Needs jq. Writes only inside <task>/build/.
# The body works for RemoteTrigger 'update' (and, minus clear_mcp_connections, for 'create').
set -euo pipefail
cd "$(dirname "$0")"
ENV_ID="env_011CUK7ovEXytcue7Dpm4mu5"   # the "Default" cloud environment

expand() {  # fill {{MARKET_LENS}} and {{SIGNAL_STRUCTURE}} from _shared/
  awk -v lens="_shared/market-lens.md" -v sig="_shared/signal-structure.md" '
    /\{\{MARKET_LENS\}\}/      { while ((getline l < lens) > 0) print l; close(lens); next }
    /\{\{SIGNAL_STRUCTURE\}\}/ { while ((getline l < sig)  > 0) print l; close(sig);  next }
    { print }' "$1"
}

# name | task folder | artifact title prefix | lookback | favicon | cron (UTC) | model | event uuid
build() {
  local name="$1" dir="$2" prefix="$3" lookback="$4" favicon="$5" cron="$6" model="$7" uuid="$8"
  mkdir -p "$dir/build"
  local out="$dir/build/full-prompt.md"
  {
    cat _shared/about-venkat.md; echo
    expand "$dir/prompt.md"; echo
    cat _shared/writing-rules.md; echo
    cat _shared/network-limits.md; echo
    if [ -n "$prefix" ]; then
      sed -e "s/{{PREFIX}}/$prefix/g" -e "s/{{LOOKBACK}}/$lookback/g" -e "s/{{FAVICON}}/$favicon/g" _shared/delivery.md
    fi
  } > "$out"
  jq -n --arg name "$name" --arg cron "$cron" --arg uuid "$uuid" --arg model "$model" \
        --arg env "$ENV_ID" --rawfile prompt "$out" '
    { name: $name, cron_expression: $cron, enabled: true, clear_mcp_connections: true,
      job_config: { ccr: {
        environment_id: $env,
        session_context: {
          model: $model, sources: [],
          allowed_tools: ["WebSearch","WebFetch","Read","Write","Bash","Glob","Grep","Artifact","PushNotification"] },
        events: [ { data: { uuid: $uuid, session_id: "", type: "user", parent_tool_use_id: null,
                            message: { content: $prompt, role: "user" } } } ] } } }' \
    > "$dir/build/routine-body.json"
  echo "$out: $(wc -w < "$out") words"
}

build "Daily Briefing"            daily-briefing            "Daily Briefing"          "the three most recent"                                                            "📰" "0 11 * * *"   claude-sonnet-5 dbb5208c-670e-4956-9019-03bca0de619f
build "Market Signal Brief"       market-signal-brief       "Market Signal Brief"     "the three most recent, plus the most recent one titled 'Weekly Signal Synthesis'"  "📡" "0 12 * * 1-5" claude-opus-5   f4de0841-20f0-4837-9aff-844ef2985b5c
build "Weekly Signal Synthesis"   weekly-signal-synthesis   "Weekly Signal Synthesis" "the most recent one, plus every 'Market Signal Brief' and 'Daily Briefing' dated this week" "🧭" "0 20 * * 5"   claude-opus-5   0e84d96b-9a20-4a3c-9238-27ff0b461825
build "Pharma Intelligence Watch" pharma-intelligence-watch ""                        ""                                                                                 ""   "0 12 * * 3"   claude-opus-5   0acb2d64-a2a7-4bf8-b67a-b20e387a2abd
build "Matching Roles Scan"       matching-roles-scan       "Matching Roles Scan"     "the most recent one"                                                              "🎯" "0 13 * * 1"   claude-sonnet-5 c2fb5ca9-8326-4d55-afa0-18c1500da6ce
build "Weekend Read"              weekend-read              "Weekend Read"            "the six most recent"                                                              "📖" "0 12 * * 6"   claude-opus-5   d46051e4-4e45-4d89-a0e1-a23b3627e222
