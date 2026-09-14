# Plan: a guard that refuses a commit holding a key (not built; needs Venkat's go)

Job: stop a real key from ever entering the lab's git history. The transcript mask only cleans renders; a key pasted into any other file today would commit fine. (Follow-up F-20260910-1630-3, second half.)

1. Where it lives: `.claude/hooks/pre-commit-key-guard.py`, next to `root-lock.py`, with a one-line `.git/hooks/pre-commit` that calls it. Tests go in `.claude/hooks/tests/`, like the root lock. It is installed by hand, once, in each lab repo (7 repos, so 7 installs); git never copies hooks on its own.
2. What it scans: only the staged text (`git diff --cached`), added lines only, every file type. It does not read the working tree or history, so it stays fast and never blocks on old dated records.
3. What pattern: the sensor's SECRET pattern, imported from `session-sync.py` so there is one home for the list. If the import ever fails the hook refuses the commit and says why, rather than passing blind.
4. What it refuses: any staged added line with a hit. It prints the file, the line number, and the kind of key, never the key itself. Exit 1, commit stopped. A `[secret-like text removed]` mask string is not a hit.
5. What it allows: an escape for a deliberate fake, `KEY_GUARD_ALLOW=1 git commit`, which also writes one line to the commit message trailer so the receipt sees it.
6. How it is tested: (a) stage a file with a fake Anthropic key, run the hook, require exit 1; (b) stage the test file itself (it holds fake keys) and require exit 1, so the test proves the guard bites; (c) stage plain prose with dates and paths, require exit 0; (d) prove-it-can-fail: point the hook at the old 00bd144 pattern and require the Google-key case to slip through.
7. Not covered, said plainly: keys already in history, keys in files that are never staged, and the six repos where the hook is not yet installed. The morning facts sheet could report "key guard installed: N of 7 repos" as a sensor line.

Decision for Venkat: yes or no to building this, and whether the escape in line 5 should exist at all.
