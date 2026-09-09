# Extraction schema (Stage 3 output) — one JSON object per line
{"transcript_id": "2025-03-14_agency-call", "timestamp": "00:41:12",
 "speaker": "VENKAT", "quote": "<verbatim, unedited>",
 "bucket": "voice|line|lens|judgment|question|objection|call|definition|refusal|register",
 "tags": ["blunt","client"]}
Rules the schema enforces: no field for summaries, paraphrase, or
interpretation. Anything the miner wants to say ABOUT a quote goes in
tags (short) or nowhere. Redacted-counterparty context, if needed, is a
separate line with speaker "OTHER" and a one-line neutral description,
never a quote.
