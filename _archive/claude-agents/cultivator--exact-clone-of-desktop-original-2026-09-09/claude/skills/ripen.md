---
name: ripen
description: "Check which seeds are closest to becoming writable content — show ripeness scores, missing criteria, and newly ready seeds"
---

# Ripen — Ripeness Check

## Steps

1. Read `garden-state.md` Ripeness Tracker section
2. Read seed files for any seeds at 2+ criteria
3. Display seeds closest to becoming writable content:
   - Seeds meeting the most ripeness criteria (sorted highest first)
   - For each: which criteria are met, which are missing
   - What specific action would advance each missing criterion
   - Seeds that just crossed into ready since last check
4. If any seeds crossed 3/5 threshold:
   - Move from `seeds/` to `ready/`
   - Inform the user with context on why it ripened
5. Add "by the way" addendum with background observations
6. Update `garden-state.md`
