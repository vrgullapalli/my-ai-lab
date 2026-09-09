# EXAMPLE-001 — Pedagogy as the Hidden AI Skill

**NOTE:** This is an example seed file showing the format. Real seeds live in `garden/seeds/`.

---

- ID: 001
- Status: growing
- Planted: 2026-04-01
- Last activity: 2026-04-03
- Signals: 3
- Connections: 002, 004
- Ripeness: 3/5 criteria met
  - ✅ Signal Diversity (3 sources: blog, conversation, observation)
  - ✅ Cluster Size (connected to 2+ seeds)
  - ✅ Tension Present (unresolved: is this trainable?)
  - ❌ Personal Stake (need more engagement)
  - ❌ Age Threshold (only 2 days old)

## Original signal

Blog post claiming "the most underrated AI skill isn't prompting, it's teaching." Author argued that as models get better, the bottleneck shifts from "getting the right output" to "teaching the model your specific context and standards."

## Germination

**What made you notice this?**
> I've been hitting walls with Claude where I know it CAN do what I want, but I can't articulate my standards well enough. Feels like teaching a junior employee who has the raw capability but not the taste.

**Do you agree or resist it?**
> Both. I think it's true for complex, taste-based work. But false for simple tasks where a good example beats a thousand words of explanation.

## Attached signals

### Signal 2 — 2026-04-02
Conversation with Cris about training junior devs. Same pattern: smart people fail not from lack of skill but from not knowing what "good" looks like in YOUR specific context. The teaching challenge is standard transfer, not information transfer.

### Signal 3 — 2026-04-03
Observation: The best AI power users I know all keep extensive "reference documents" — style guides, decision logs, rejected examples. They're literally building training materials for their AI assistant.

## Agent notes

**Convergence warning:** Signal 3 connects to seed 004 (Knowledge Management). Both about building personal systems that externalize taste/standards. Possible theme emerging around "externalized cognition."

**Tension:** Is this skill trainable? Or do you need to already be a good teacher/manager to become a good AI user?

## History

- 2026-04-01: Planted as seedling
- 2026-04-02: Added Signal 2 (conversation), moved to growing
- 2026-04-03: Added Signal 3 (observation), met cluster size criteria
- 2026-04-03: Connected to seed 002 (AI as junior dev), seed 004 (Knowledge Management)

---

## Format Reference

Every seed file follows this structure:

```markdown
# {ID} — {Slug/Title}

- ID: {number}
- Status: seedling | growing | ripening | wilting | orphan
- Planted: YYYY-MM-DD
- Last activity: YYYY-MM-DD
- Signals: {count}
- Connections: {list of connected seed IDs + names}
- Ripeness: {X/5 criteria met — list which}

## Original signal
{What the person observed or thought}

## Germination
{User's responses to germination questions}

## Attached signals
### Signal N — {date}
{Source + summary + how it connects}

## Agent notes
{Cross-references, editorial observations, convergence flags}

## History
- YYYY-MM-DD: {action taken}
```

## Status Meanings

- **Seedling**: Just planted. Raw idea, no connections yet.
- **Growing**: Connecting to other seeds or collecting signals.
- **Ripening**: Meets 3+ maturity criteria. Close to writable content.
- **Wilting**: No new signals or interactions in 14+ days.
- **Orphan**: No connections to any other seed after 10+ days.
- **Composted**: Retired from active garden. Stored in `compost/`.
