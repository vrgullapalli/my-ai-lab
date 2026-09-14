# context/

The files that tell any session who Venkat is, how he sounds, and how he wants
work done. Only `how-i-work.md` loads every session, through the import line in the lab's
CLAUDE.md. The rest is read when a session opens it.

| File | Holds |
|---|---|
| `who-i-am.md` | Who he is — role, background, what he is building |
| `how-i-talk.md` | How he sounds, and how he wants to be written to |
| `how-i-work.md` | How work should be done with him |
| `CLAUDE.md` | Session instructions |
| `intent/STANDING.md` | The current drivers of the lab. Exists. They change; the machinery that reads them does not (Venkat, 2026-09-11) |
| `sources/REGISTER.md` | Retrieval's list of what it may depend on: 23 sources (20 inside the lab, 3 outside), each with owner, standing, authority tier, how dates are read, and use limits (what it may inform, what it must never establish alone). Exists since 2026-09-12 (build step 2). `sources/check.py` beside it proves the register, watches source health, counts coverage, runs source discovery, and resolves an id to its current location; `sources/tests/` proves the check can fail |

`how-i-work.md` exists since 2026-09-11, from Venkat's own text, and loads every session through an import line in the lab's CLAUDE.md (live 23:37). `who-i-am.md`, `how-i-talk.md`, and `CLAUDE.md` here do not exist yet. `intent/STANDING.md` does exist.

## Removal recorded — 2026-09-09

Four empty directories were created here on 2026-09-09 with the names above,
instead of files. A folder called `who-i-am.md` cannot hold the contents of
`who-i-am.md`, so nothing could be written into them.

All four were empty. They were removed so the real files can be created in
their place. Nothing was archived because there was nothing in them.

`who-i-am.md` had been created at the lab root rather than here. All four
belong in this folder.

## Moved — 2026-09-10

`how-i-work--observed.md` (evidence about how he works, from agents) was created here at 12:54 and moved to `docs/about-me/` at 12:56 at Venkat's word: "move that to /docs as a subfolder. its a draft until i review and approve." Nothing goes from it into `how-i-work.md` without his review.
