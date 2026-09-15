---
name: context-check
description: Reads the whole lab and reports what is duplicated, what is declared dead but still live, what nothing points at, what is uncommitted, and what points at paths that no longer exist. Changes nothing in the lab. Use before and after any restructuring, when Venkat says context check, check the lab, what is out of place, what is not linked, is anything missing, did that actually get done, or asks whether a plan was really carried out.
---

# Context check

> **Base directory:** the lab, `/Users/venkatgullapalli/Documents/my-ai-lab/`

## Why this exists

Between 2026-09-04 and 2026-09-07, five plans were written to reorganize the lab.
None were carried out. Each one *said* what should happen; none could say what
did happen.

A plan can claim it is done. This cannot. It only reads what is on disk.

## Operational DNA

The standard is section 16 of `docs/architecture/LAB-OPERATING-MODEL.md`. This skill's answers
(from the audit of 2026-09-15 and the repair the same day, AD-38):

| Property | State | In one clause |
|---|---|---|
| Job | OWN | say what is true about the lab's structure by script, so a plan cannot claim it is done |
| Scope | OWN | the whole lab minus history (`evidence/`) and archives; section D names every area it measures, counts the files loose at the root of `docs/` and `context/`, and says what it leaves out; reads one folder outside the lab, the warehouse snapshots, and says so |
| Process | OWN | runs on his word or when many files moved; seven sections; a person reads the output and reports the two or three findings that change what he does. Failure path: a wrong root exits 2 with `NOT A LAB ROOT`, and a helper that is missing or crashes is an `ALERT` in its own section with the error, and the run exits 1; never a blank section, never a clean line about the wrong folder |
| State | NONE BY DESIGN for the scripts, which write nothing; OWN for the two accepted files, the only state here |
| Context | INHERIT | disk and git are the whole context; it receives no opinion |
| Evidence | OWN | the output is the evidence; the facts sheet carries one line per helper every session (INHERIT, `facts.py`) |
| Trust | OWN | every section header says `[measured]` or `[word match]`; a word-match hit is read before it is acted on |
| Authority and control | OWN | running is always allowed; a finding closes only by a rerun (RESOLVED) or by an acceptance line (ACCEPTED, never counted as resolved); who may accept is in section 16, and the accepted files record who, item or bulk, when, under what word. who responds is named below: Alfred coordinates, the responsible specialist repairs, Venkat alone accepts |
| Experience | OWN | headline number first, then the findings that matter; never the whole output |
| Evaluation and learning | OWN | three planted-fault test files, one per script, in `tests/`, each with a wrong-root fault, and the check's with a helper crash, a missing helper, and a helper with findings as the control; the accepted files are the learning record, and a bulk sweep is reported as bulk |

## What to run

```bash
.claude/skills/context-check/context-check.sh
```

It changes nothing in the lab. It uses one scratch folder for section E and removes it on
exit. Safe to run at any time, including in the middle of other work. It takes about a
minute on the real lab.

**Exit codes.** 0: every section measured. 1: at least one `ALERT` line, a section that could
not measure because its helper is missing or crashed; the closing line counts them. 2: the
root is not a lab (no `CLAUDE.md` or no `.claude/`), and nothing was measured. A wrong root
or a helper crash was found on 2026-09-15 to read as a clean lab; both are planted in the
tests now, so they cannot come back quietly.

## What it reports

Every section header carries one of two labels. **`[measured]`** means a script checked the
thing itself: a checksum, a path, a front-matter line, a git status. Act on it. **`[word
match]`** means a script matched words or file names, not the thing. Read the hits before
acting on them.

A third marker, **`ALERT`**, means a section could not measure at all: its helper is missing
or crashed. It is not a finding about the lab; it is a broken sensor. Fix the sensor first.

| Section | Label | Question it answers |
|---|---|---|
| A | measured | Can this be undone? Uncommitted work per repo, age of the last snapshot, folders with no repo at all |
| B | measured | Is the same file sitting in two live places, ready to drift apart? |
| C | word match | Is anything declared superseded but still in the search path? Matches the words superseded, deprecated, retired, do not use, no longer near the top of a file, so it also lists files that merely mention them |
| D | measured | Can a machine follow the connections, per area? Covers the brand record, every `docs/` and `context/` area, and prints any `docs/` or `context/` folder it does not know. Excluded on purpose: `evidence/` (history), `.claude/` (skill-check covers it); not measured yet: `work-os/projects/`, `scheduled-tasks/`, `upskill-advisor/` |
| E | word match | What does nothing point at? A file counts as pointed-at if its bare name appears anywhere, so a same-named file elsewhere hides an orphan; the count is a floor |
| F | measured | What points at paths that no longer exist? Runs `dead-pointers.py` and prints its OPEN, ACCEPTED, and RESOLVED lines. Replaced the grep for four known folder names on 2026-09-15; that grep only found names someone already knew were dead |
| G | measured | Do the capability map, the definitions, and the lab agree? Runs `docs/architecture/check.py` and `context/sources/check.py`, which live with the things they watch |

## Who responds to a finding

The sensor reports. It fixes nothing. The response owner is named here, not inherited
(wording his, 2026-09-15 02:31: "Small wording fix. No redesign."):

- **Alfred coordinates the response**: identify, route, track, integrate. He may perform only
  routine coordination or explicitly delegated local corrections.
- **The responsible specialist owns substantive repair.** A dead pointer in a skill goes to
  whoever owns that skill's domain; a helper crash goes to the sensor's owner.
- **Venkat alone** may accept an unresolved finding or approve a material change to a rule or
  to authority. Alfred writes the acceptance line on his word. An accepted finding is still
  there and is never counted as resolved; RESOLVED is proven only by a rerun.

The 995 bulk-accepted mentions stay visible as unconfirmed accepted legacy state. They are not
a reason to redesign this check (his word, same message).

## How to report it back to Venkat

**Do not paste the whole output.** It runs to a few hundred lines. Read it, then
give him the headline number and the two or three findings that would change what
he does next. He reads at a glance. Lead with the number, then what it means.

The orphan count in section E is usually the one that matters. It is the direct
measure of "I cannot find anything."

## Two more scripts beside it

```bash
python3 .claude/skills/context-check/dead-pointers.py           # every path a live file names that does not exist, lab-wide
python3 .claude/skills/context-check/dead-pointers.py --all     # also dated files, and each accepted mention with its record
python3 .claude/skills/context-check/role-map.py <root> [<root>...] [--verify-manifests]   # role marker files under a root (the fixed marker name is in the Organization Standard, AD-40): the derived map plus drift findings; tests in tests/role_map_tests.py
python3 .claude/skills/context-check/skill-check.py             # skills and agents only, strict: empty bodies, base
                                                                #   directories, every path, every skill named by name
python3 .claude/skills/context-check/skill-check.py --summary   # the one line Alfred's facts sheet carries
```

Both are read-only. `dead-pointers.py` counts a path as found if a file of that name exists
anywhere in the lab; that is right for a lab-wide sweep and wrong for a skill, which fails
silently when its pointer is off by a folder. `skill-check.py` resolves against the skill's
own folder, its declared base directory, and the lab root, nothing else, and it also flags a
skill that names a retired skill.

## Open, accepted, resolved

`dead-pointers.py` ends with three lines, and they are never folded into one number:

- **OPEN** — unreviewed mentions in live files of paths that do not exist. The count to act on.
- **ACCEPTED** — mentions still on disk that a person reviewed and left on purpose, with the
  reason in the accepted file. Counted apart, split into item by item, bulk, and no record.
  **Accepted is not resolved.**
- **RESOLVED** — not counted. A mention leaves the report only when its path exists again or
  the mention is gone. Run again to prove it.

**Who may accept** (section 16 of the operating model): Venkat, item by item or as a named
set. Alfred writes the line on his word. A bulk acceptance without his explicit word naming
the set is recorded and reported as bulk, unconfirmed. The record is a marker line above a
group in the accepted file, and everything below it carries that record until the next marker:

```
# accepted-by: <who> | item or bulk | <date> | <the word or record that authorized it>
```

`dead-pointers-accepted.txt` has two groups today: 5 lines reviewed one by one on 2026-09-12
during the writing-guide move (39 mentions), and the sweep of 2026-09-14 under follow-up
F-20260910-1627-1, closed by Alfred alone (106 lines, about 995 mentions). The sweep is
marked bulk and unconfirmed. His word can confirm it as a set or ask for item review; nothing
was reverted, because reverting would bury the real open ones under a thousand lines.
`skill-check-accepted.txt` keeps its older one-line-per-finding form; the same marker works
there when it is next touched.

## Tests

```bash
python3 .claude/skills/context-check/tests/skill_check_tests.py     # skill-check.py: the seven stale pointers of 2026-09-10, planted; a wrong root
python3 .claude/skills/context-check/tests/dead_pointers_tests.py   # dead-pointers.py: open, found, dated, item, bulk, no record, resolved by rerun, read-only; a wrong root
python3 .claude/skills/context-check/tests/context_check_tests.py   # context-check.sh: legend, B, C, D, E, F, G on a planted lab, a clean-lab control, read-only;
                                                                    #   a wrong root, a helper crash, a missing helper, and a helper with findings as the control
```

Each builds a throwaway lab and points the script at it through the environment
(`LAB_ROOT`, `LAB_SNAPSHOTS`, `LAB_DOCS`, `DEAD_POINTERS_ACCEPTED`), so the real lab is never
read or written. Each prints its PASSED line only when every case passes.

## What it will not tell you

- Whether a file is any *good*. It counts and compares; it does not judge.
- Whether a connection is *meaningful*. A link that exists is a link that exists.
- What to do about any of it. That is a conversation, not a script.
