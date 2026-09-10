---
name: public-asset-development
version: 1.0.0
description: >
  Use when an approved public asset has to be built or finished: an experience spec
  is marked approved-for-build, a QA verdict came back REVISE, or Venkat says build
  it, finish the instrument, make the page, implement the spec. The build stage of
  the publishing chain, between experience design and public asset QA. Triggers on:
  build the asset, build it, finish the instrument, implement the spec, development
  stage, public-asset-development.
---

# Public asset development

> **Base directory:** all relative paths in this skill resolve from `work-os/brand-os/engagement-os/`
> (lab root: `/Users/venkatgullapalli/Documents/my-ai-lab/`). Written 2026-09-10 at Venkat's word
> ("write a thin build skill"), because the chain named this stage for two weeks and nothing held it.

PROJECT-SPECIFIC to the publishing system. Never publishes, deploys, sends, or shares
anything. Builds what the spec says and hands the result to QA with a written record.

**Position.** After the experience spec is approved for build, after claim verification,
before `public-asset-qa`. Development implements the spec. It never invents the experience,
the judgment, or the words.

## Required inputs. Stop if any is missing

Read these before touching a file. Each one is a predicate a script or a glance can settle.

| Input | Where | Must say |
|---|---|---|
| Public asset brief | `assets/briefs/<ID>--brief--<date>.md` | frontmatter `ruling: APPROVED` |
| Experience spec | `assets/experience/<ID>--spec--<date>.md`, the newest | frontmatter `status: approved-for-build` |
| AI-native design record | the opportunity folder, AI-native assets only | verdict earned, with inputs, behavior, refusals, acceptance tests |
| Registry entry | `assets/registry.yaml` | the asset id exists |
| Claim ledger | `assets/verification/<ID>--claims--<date>.md` | exists, if the asset carries any number or external fact |

**If the records disagree, stop and name it.** The registry saying "build not authorized"
while the spec says "approved-for-build" is a contradiction for Venkat to settle, not a
choice for the builder to make. Say which two lines disagree, quote them, and wait.

A message that says "build it" does not settle the contradiction. It was written without
the two lines in front of him. The build starts only after one of two things: he changes
the losing line himself, or he answers the one question "the registry says X and the spec
says Y, which wins?" in so many words. "He said build it, so that settles the registry" is
the rationalization this paragraph exists to stop. It cost nothing to ask; it costs a day
to build against a record that still says no.

## What a build is

1. **Sources first.** Authored content lives in source files (a case model, a template, a
   readings file, a stylesheet). Built output is generated from them by a build tool kept
   beside them. Never hand-edit a generated file; fix the source and rebuild.
2. **The spec's words are the words.** Readings, labels, refusal lines, and result
   sentences come from the spec or its authored set, verbatim. Runtime string assembly
   that produces sentences nobody read aloud is a build failure, not a style note.
3. **Visual work goes through the identity.** Run `design-brief` before the first visual
   decision, then the `frontend-design` plugin skill for the build itself. `design-review`
   runs after, and its findings go in the build record.
4. **The spec's acceptance tests become runnable checks.** Every test the spec lists under
   its acceptance section is a script under `tests/` beside the other asset tests, and
   `prove-it-can-fail` applies: each check is shown to fail when its invariant is broken
   before it counts as passing.
5. **Two deterministic gates run at the end,** and their output is quoted, not summarized:

   ```bash
   python3 tools/check_public_safety.py assets/releases/<ID>/
   python3 tools/validate_public_value.py release assets/releases/<ID>/
   ```

## Output contract

Everything lands under `assets/releases/<ID>/` (PRIVATE until Venkat publishes):

- sources, the build tool, and the built output, in folders named for what they are
  (an instrument folder, a page folder). The AS-006 package, now in the warehouse under
  `engagement-os-archived-2026-09-10/`, is the worked example of that layout
- `release.yaml`, updated only in the fields the build changes: `version`, and a
  `built:` line with the date and the spec it implements. `approval:` fields are never
  touched here.
- **`BUILD--<date>.md`, the build record.** Machine frontmatter: `asset`, `spec` (path),
  `spec_status`, `date`, `built_by` (model id), `acceptance_tests` (passed / proven / total),
  `safety_check` (clean | violations | could-not-run), `release_validator` (valid | errors),
  `unverified` (list). Body, in this order: what was built, one line per file · the
  acceptance tests, each with pass and proven · the safety and validator output, quoted ·
  what QA should look at first · what this build could not do and why · the registry line
  Venkat would approve if QA passes, written out, not applied.

**Hand off:** `public-asset-qa`, pointed at the spec and the build record. The build stage
grades nothing. PASS is QA's word, then Venkat's.

## When the instruction says more than "build"

| Venkat says | This stage does |
|---|---|
| "put it on the site" / "deploy it" / "publish" | build and record; then say, in one line, that publication is Gate 2 and needs his word on the release package, the site's hold, and a domain. Copy nothing into the site repo. |
| "share it with X tonight" / "send it" | not this stage. Sending is his; the text for it is `asset-expression` after Gate 2. |
| "just fix the QA notes" | this stage, in REVISE mode: change sources only, rebuild, rerun every check, write a new build record naming the QA file it answers. |
| "show me" | a private Artifact page for his eyes, from the built output, no share link, and it is said to be a preview in the first line. |

## Never

Publish, deploy, push, or commit · copy anything into the site repository · send or share
with anyone but Venkat · change `ruling`, `status`, `approval`, or `decided_by` fields in
the brief, the spec, the registry, or `release.yaml` · edit the brief or the spec · draft
outreach or expressions · call the result PASS · declare a check "proven" that
`prove-it-can-fail` has not run.
