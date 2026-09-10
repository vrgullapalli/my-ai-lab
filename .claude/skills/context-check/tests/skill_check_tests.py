#!/usr/bin/env python3
"""Tests for skill-check.py, in the prove-it-can-fail form: a clean fixture must pass, and
every kind of break the check claims to catch must make it fail and name the break.

Run:  python3 .claude/skills/context-check/tests/skill_check_tests.py

Builds a throwaway lab in a temp folder, so it never reads or writes the real one. The
seven stale pointers found by hand in the 2026-09-10 skills audit are planted here in the
same shapes they had, so the check is proven against the failures that motivated it.
Prints SKILL CHECK TESTS PASSED only when every case passes.
"""
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(os.path.dirname(HERE), "skill-check.py")
failures = 0


def check(name, ok, detail=""):
    global failures
    failures += 0 if ok else 1
    print(f"  {'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail[:300]})" if detail and not ok else ""))


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def run(lab, accepted=None):
    env = dict(os.environ, LAB_ROOT=lab, CLAUDE_PLUGINS=os.path.join(lab, "no-plugins"),
               CLAUDE_USER_SKILLS=os.path.join(lab, "no-user-skills"),
               SKILL_CHECK_ACCEPTED=accepted or os.path.join(lab, "no-accepted.txt"))
    r = subprocess.run([sys.executable, SCRIPT], capture_output=True, text=True, env=env, timeout=60)
    return r.returncode, r.stdout


def make_lab():
    lab = tempfile.mkdtemp(prefix="skill-check-tests-")
    # a domain with real files, the way engagement-os has them
    for p in ("work-os/eng/targets/index/companies.json", "work-os/eng/assets/briefs/README.md",
              "work-os/eng/seedbank/session/A-001.md", "work-os/brand-os/visual/DESIGN-IDENTITY.md",
              "work-os/eng/docs/state.md"):
        write(os.path.join(lab, p), "x\n")
    # a clean skill: every pointer resolves, base directory exists, names a skill that exists
    write(os.path.join(lab, ".claude/skills/clean/SKILL.md"), """---
name: clean
description: A skill whose pointers all resolve, including `work-os/brand-os/visual/DESIGN-IDENTITY.md`.
---

# Clean

> **Base directory:** all relative paths in this skill resolve from `work-os/eng/`
> (lab root: `LABROOT/`).

Read `targets/index/companies.json` and `docs/state.md`. Seeds go in `session/` under the
seedbank. Run the `other` skill after. Write to `assets/briefs/<ASSET-ID>--brief.md`.
Two words with a slash, like dark/light or read/write, are not paths.
""".replace("LABROOT", lab))
    write(os.path.join(lab, ".claude/skills/other/SKILL.md"), """---
name: other
description: exists
---

# Other

> **Base directory:** the lab root.

It does one thing, in `work-os/eng/docs/state.md`.
""")
    write(os.path.join(lab, ".claude/agents/helper.md"), "# Helper\n\nReads `work-os/eng/docs/state.md`.\n")
    return lab


# 1. clean run: the check passes on a lab with nothing wrong
lab = make_lab()
rc, out = run(lab)
check("clean: exits 0 with zero problems", rc == 0 and "SKILL CHECK PROBLEMS: 0" in out, out)
check("clean: word pairs like dark/light are not read as paths", "dark/light" not in out and "read/write" not in out, out)
check("clean: a placeholder path `assets/briefs/<ASSET-ID>--brief.md` resolves on the part before the placeholder", "assets/briefs" not in out, out)
check("clean: `session/` inside a seedbank domain resolves one level below the base", "session/" not in out, out)

# 2. the seven stale pointers from the 2026-09-10 audit, in the shapes they had
lab = make_lab()
write(os.path.join(lab, ".claude/skills/stale/SKILL.md"), """---
name: stale
description: Reads context/DESIGN-IDENTITY.md, asks only what that file doesn't answer, and writes into work/plans/{slug}/.
---

# Stale

> **Base directory:** all relative paths in this skill resolve from `work-os/eng/`

1. Check the exclude set in `index/companies.json` (the file is really under targets/).
2. Screenshots HTML via the `webapp-testing` skill.
3. Write `assets/distribution/<ASSET-ID>--distribution--<date>.md`.
4. It hands `public-asset-development` an implementable spec.
5. Run `python3 telegraph/evals/prove_checks.py` (that repo is gone).
6. Then /instrument-ship takes over.
""")
rc, out = run(lab)
check("stale: exits 1", rc == 1, out)
for tok in ("context/DESIGN-IDENTITY.md", "work/plans/", "index/companies.json", "assets/distribution/",
            "telegraph/evals/prove_checks.py"):
    check(f"stale: catches dead path {tok}", f"DEAD PATH: {tok}" in out, out)
for name in ("webapp-testing", "public-asset-development", "instrument-ship"):
    check(f"stale: catches missing skill {name}", f"MISSING SKILL: {name}" in out, out)
check("stale: a bare frontmatter description is read, not only backticks", "DEAD PATH: context/DESIGN-IDENTITY.md" in out, out)

# 3. an empty body, the shape of the six hollow skills
lab = make_lab()
write(os.path.join(lab, ".claude/skills/hollow/SKILL.md"), "---\nname: hollow\ndescription: looks fine\nlicense: x\n---\n\n# Hollow\n")
rc, out = run(lab)
check("hollow: an empty body is flagged", rc == 1 and "EMPTY BODY" in out, out)

# 4. base directory problems
lab = make_lab()
write(os.path.join(lab, ".claude/skills/nobase/SKILL.md"), "---\nname: nobase\n---\n\n# No base\n\nReads `work-os/eng/docs/state.md` and does things.\n")
write(os.path.join(lab, ".claude/skills/badbase/SKILL.md"), "---\nname: badbase\n---\n\n# Bad base\n\n> **Base directory:** `work-os/gone/`\n\nReads `docs/state.md`.\n")
rc, out = run(lab)
check("nobase: a skill with no base directory line is flagged", "NO BASE DIRECTORY LINE" in out and "nobase" in out, out)
check("badbase: a base directory that does not exist is flagged", "BASE DIRECTORY MISSING: work-os/gone" in out, out)

# 5. a bare file name anywhere in the lab does NOT count: only near the skill, its base, or the root
lab = make_lab()
write(os.path.join(lab, "work-os/far/away/deep/inside/here/companies.json"), "x")
write(os.path.join(lab, ".claude/skills/bare/SKILL.md"), "---\nname: bare\n---\n\n# Bare\n\n> **Base directory:** the lab root.\n\nOpen `nowhere.json` and `deep/inside/here/companies.json`.\n")
rc, out = run(lab)
check("bare: a file name that exists only far away is still a dead path", "DEAD PATH: nowhere.json" in out, out)
check("bare: a folder path is not found by matching its file name elsewhere", "DEAD PATH: deep/inside/here/companies.json" in out, out)

# 6. accepted exceptions are counted, not listed; a new finding still shows
lab = make_lab()
write(os.path.join(lab, ".claude/skills/stale/SKILL.md"), "---\nname: stale\n---\n\n# Stale\n\n> **Base directory:** the lab root.\n\nSee `old/place.md` and `other/gone.md`.\n")
acc = os.path.join(lab, "accepted.txt")
write(acc, ".claude/skills/stale/SKILL.md :: old/place.md | history, reviewed\n")
rc, out = run(lab, accepted=acc)
check("accepted: the reviewed token is not listed", "old/place.md" not in out, out)
check("accepted: the unreviewed token still is", "DEAD PATH: other/gone.md" in out and "1 accepted" in out, out)

# 7. the mutation is undone: the clean lab still passes (the check is not simply always failing)
lab = make_lab()
rc, out = run(lab)
check("clean again: passes after the broken cases", rc == 0, out)

print()
if failures:
    print(f"SKILL CHECK TESTS FAILED: {failures}")
    sys.exit(1)
print("SKILL CHECK TESTS PASSED")
