# Installed 2026-09-09

Source: https://github.com/virgiliojr94/book-to-skill (the official repository)
Commit at install: see git-sha below. Cloned, reviewed, then copied — not run.

## What was checked before installing

- **No network calls** in the package code. The only URLs are in comments and docs.
- **No access** to wallets, keychain, browser storage, ssh keys or cookies.
- `subprocess` is used three times, all document converters:
  `ebook-convert` (Calibre), `pdftotext` and `pdfinfo` (poppler).

## One thing to know

On first use the skill runs `pip install` for nine document-parsing packages:
pdf-inspector, docling, pypdf, pdfminer.six, ebooklib, beautifulsoup4,
python-docx, striprtf, trafilatura. It installs them without asking.

## Warning carried over from the source

The repository ships a `SECURITY-NOTICE.md` about a malicious copy at
`Leutenegger/book-to-skill`, which steals cryptocurrency wallet data. That is a
different repository. This install is from the official one. Do not install the other.

Only these were copied: SKILL.md, book_to_skill/, scripts/, LICENSE.md,
README.md, SECURITY-NOTICE.md. Tests, docs, evals, CI and translations were not.
git-sha: a6cad12dee07a7700068e2aa51cba871ef3b5349
