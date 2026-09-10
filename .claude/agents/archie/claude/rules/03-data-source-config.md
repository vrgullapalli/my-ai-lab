STATUS: CONFIGURED (2026-09-09, by the lab rule that data lives in the domain that owns it)

```yaml
data_source: local
fetch_strategy: file_read
lab_root: /Users/venkatgullapalli/Documents/my-ai-lab
config: work-os/brand-os/engagement-os/agents/archie/config/data-sources.yaml
outputs: work-os/brand-os/engagement-os/agents/archie/outputs/
backlog: work-os/brand-os/engagement-os/agents/archie/backlog/
kills:   work-os/brand-os/engagement-os/agents/archie/archive/kills/
inbox:   work-os/brand-os/engagement-os/agents/archie/inbox/
```

## How the config is read (Venkat's three tiers, kept from ARCHIE v2)

The yaml file lists every source in three tiers. The order is the point.

- **Tier 1, always:** the seedbank, topic cards, chronicles, work corpus, voice notes, the Telegraph project, the backlog. Read during research (pipeline steps 1–3).
- **Tier 2, after the sweep:** positioning, the six Capability Pillars, Trust Is the Product, the audience, the Moonshot guidance. Read at pipeline step 4 only. Never before.
- **Tier 3, drafting only:** the writing guide and voice examples. ARCHIE never reads these. They belong to the writing system after handoff.

Precedence: brand-os wins over any other context whenever they disagree. The writing canon (`voice/VENKAT-WRITING-CANON.md`, read through the generated guide folder) is the voice authority.

Market lenses (job postings, friction) read the weekly instrument first (`market_instrument` in the yaml); live sweeps fill topic-specific gaps only.

Do not change these paths here. Change `lab_root` in the yaml if the lab moves.
