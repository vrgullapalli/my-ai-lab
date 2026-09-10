#!/bin/bash
# root-lock.sh — refuses to let anything new be created at the lab root.
# Reads the PreToolUse JSON on stdin. Prints a deny decision, or nothing.
#
# Why: on 2026-09-09 _archive/ and _backups/ reappeared at the root twice,
# because the rules said to put them there. The rules were fixed. This is the
# belt as well as the braces.

LAB="/Users/venkatgullapalli/Documents/my-ai-lab"
ALLOWED="CLAUDE.md ROOT.md TASTE.md RULINGS-IN-FORCE.md DONE.md .claude context evidence work-os docs"

payload=$(cat)

deny() {
  printf '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":%s}}\n' \
    "$(printf '%s' "$1" | python3 -c 'import json,sys; print(json.dumps(sys.stdin.read()))')"
  exit 0
}

is_allowed() {
  local name="$1"
  for a in $ALLOWED; do [ "$name" = "$a" ] && return 0; done
  return 1
}

# what is the first path segment under the lab root?
root_entry() {
  local p="$1"
  case "$p" in
    "$LAB"/*) printf '%s' "${p#$LAB/}" | cut -d/ -f1 ;;
    *) return 1 ;;
  esac
}

tool=$(printf '%s' "$payload" | python3 -c 'import json,sys; print(json.load(sys.stdin).get("tool_name",""))' 2>/dev/null)

case "$tool" in
  Write|Edit|NotebookEdit)
    fp=$(printf '%s' "$payload" | python3 -c 'import json,sys; print(json.load(sys.stdin).get("tool_input",{}).get("file_path",""))' 2>/dev/null)
    [ -z "$fp" ] && exit 0
    entry=$(root_entry "$fp") || exit 0
    [ -z "$entry" ] && exit 0
    is_allowed "$entry" && exit 0
    deny "The lab root is locked. \"$entry\" is not one of the ten things allowed there.

Allowed at the root: CLAUDE.md, ROOT.md, TASTE.md, RULINGS-IN-FORCE.md, DONE.md, .claude/, context/, evidence/, work-os/, docs/

Put it inside a domain instead, or in ~/Documents/_warehouse/ if it is finished with. If it genuinely belongs at the root, ask Venkat first and add it to ALLOWED in .claude/hooks/root-lock.sh."
    ;;
  Bash)
    cmd=$(printf '%s' "$payload" | python3 -c 'import json,sys; print(json.load(sys.stdin).get("tool_input",{}).get("command",""))' 2>/dev/null)
    [ -z "$cmd" ] && exit 0
    # only look at commands that create things, and only at explicit lab-root targets
    printf '%s' "$cmd" | grep -qE '(mkdir|touch|tee|cp|mv|ln|unzip|tar)' || exit 0
    while IFS= read -r hit; do
      entry=$(printf '%s' "$hit" | sed "s|^$LAB/||" | cut -d/ -f1)
      [ -z "$entry" ] && continue
      is_allowed "$entry" && continue
      deny "The lab root is locked, and this command targets \"$entry\" there.

Allowed at the root: CLAUDE.md, ROOT.md, TASTE.md, RULINGS-IN-FORCE.md, DONE.md, .claude/, context/, evidence/, work-os/, docs/

Put it inside a domain instead, or in ~/Documents/_warehouse/ if it is finished with."
    done < <(printf '%s' "$cmd" | grep -oE "$LAB/[^ \"';|)&]+" | sort -u)
    ;;
esac
exit 0
