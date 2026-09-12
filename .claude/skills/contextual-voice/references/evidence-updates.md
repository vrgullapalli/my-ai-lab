# Updating the Voice Model

Use this guide only when new writing evidence is being evaluated or the user asks the skill to learn.

## Evidence hierarchy

Give the most weight to:

1. An explicit instruction about what the user wants or rejects.
2. A direct correction with a reason.
3. A repeated choice among alternatives across multiple contexts.
4. Repeated patterns in final, user-approved writing.
5. Patterns in user-authored source material.
6. A single accepted draft or isolated example.

Do not infer a stable preference from assistant-generated prose merely because the user did not object.

## Stable rule or contextual dial?

Treat evidence as a candidate stable rule only when it repeats across at least two materially different formats or the user explicitly makes it global.

Treat evidence as contextual when it is tied to an audience, channel, purpose, or one specific piece. Add or refine a format dial rather than changing the core.

Treat one-off instructions as local unless the user says to remember them.

## Update conservatively

- Add the narrowest rule that explains the evidence.
- Preserve existing rules that are not contradicted.
- When new evidence conflicts with an older rule, prefer the more explicit, recent, and repeated evidence.
- If the conflict could reflect context rather than a changed preference, create a contextual exception.
- Do not erase a stable rule because of one unusual deliverable.
- Replace or consolidate rules when they express the same underlying preference. Do not accumulate a long list of near-duplicates.

## Record the reason

For every material update, capture:

- the observed correction or choice;
- whether it is stable, contextual, or local;
- which rule it changes;
- confidence: high, medium, or low;
- what future evidence would confirm or reverse it.

Do not expose this bookkeeping in normal writing output unless asked.

## Drift checks

Periodically look for:

- favored phrases becoming repetitive;
- short sentences turning into artificial fragments;
- skepticism becoming automatic contrarianism;
- warmth becoming hedging;
- compression removing needed reasoning;
- format rules leaking into unrelated formats;
- old preferences surviving after repeated explicit corrections.

The goal is recognizable continuity with contextual range, not frozen imitation.
