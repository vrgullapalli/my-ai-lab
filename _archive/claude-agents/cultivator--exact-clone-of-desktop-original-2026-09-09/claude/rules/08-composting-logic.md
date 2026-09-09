# Composting Logic

## Wilting

14 days with no new signals AND no user interaction -> status changes to "wilting." Mention in the "by the way" addendum.

## Orphan

No connections to any seed or theme after 10 days -> flagged as orphan.

## Composting

- Files move to `compost/`, never deleted
- Cross-reference new seeds against compost and offer revival when connections appear
- User always decides — the agent surfaces candidates, never auto-composts

## Convergence Detection

Flag convergence when 2+ seeds share at least 2 of:
- Same cluster membership
- Overlapping signal sources
- Similar framing in original observations

Threshold is deliberately low. False positives are useful — if the user says "no, these are different, here's why," that clarification deepens both seeds.
