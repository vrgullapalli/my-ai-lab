# Judge: run a piece through Purple Cow

Give this skill an article, a draft, a transcript, a post, a pitch, a product page, or an idea in a sentence. It reads the piece against the book and returns one verdict, the questions it failed, and the one change that would move it.

## Inputs it takes

- A file path in the lab (a draft, a gate file, a transcript under `evidence/sessions/`, a research note).
- Pasted text.
- A one-line idea ("a diagnostic that scores a pharma team's data trust").

Read the whole piece before judging. Judge the subject of the piece (the asset, the offer, the position) first, the wording second. Godin: "It's not about the way you say it, it's what you say."

## The seven questions (ask them in this order)

1. **Very good, or remarkable?** Would a reader repeat one line of this to a peer without being asked? If the honest answer is "they would nod," it is very good, which the book calls invisible. Name the one line a reader might repeat, or say there is none.
2. **Which limit does it push?** Cheapest, fastest, slowest, most exclusive, most honest, most narrow, most hated, the opposite of the leader. A piece that sits in the middle on every axis is a brown cow. Name the axis and the extreme, or "none."
3. **Who are the sneezers, and what is their script?** Which specific group would carry this to others, and what one-breath line would they use? If the script needs "also, and, plus," it is not a script.
4. **Would some people dislike it?** Remarkable means some readers object. If everyone in the audience would agree, the piece has been sanded by a committee, even a committee of one. Name who would push back and on what.
5. **Is the Cow in the asset or only in the wording?** Godin's test from the Dutch Boy can: where does the product end and the hype begin? If the only remarkable part is a turn of phrase, say so. The fix is upstream.
6. **Is it a niche with otaku, or everyone?** Who is the smallest group this overwhelms? "Senior commercial leaders" is everyone. "Directors who just inherited a CRM migration" is a niche.
7. **Does it ask "why not?"** Does the piece do something "just not done" in its field (publish the price, tell the truth about the downside, refuse the standard format)? Or does it follow the leader?

## The output shape

Keep it under 200 words. Plain words. Quote the piece, do not paraphrase it.

```
**Verdict:** brown cow | very good | remarkable for <the niche>

**Failed:** the question numbers it failed, each with one quoted line as evidence
**Passed:** the question numbers it passed, each with one quoted line

**The one change:** the single move that would turn it, stated as a product or position change first, a wording change only if the asset already passes.

**The sneezer's script:** one line a reader could repeat. Or "none yet."

**Chapter to read:** the one chapter file that covers the failure.
```

## Rules

- Judge the asset, not the author. Criticism of the piece is not criticism of him.
- Never soften a brown-cow verdict. "Very good" is a fail in this book.
- No rewriting inside the judge. If he wants a rewrite, that is the voice skill's job, and it runs its own pass.
- Quote the book only where it decides the question; the chapter link carries the rest.
- Zero passes is a valid result. So is "remarkable, ship it."
