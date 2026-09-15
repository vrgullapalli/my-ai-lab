# Gates: seed-capture repaired against Operational DNA v2

OWNS: .claude/skills/seed-capture/**, .claude/skills/alfred-close/SKILL.md, GATES.md

Scope: seed-capture owns idea capture only, names the AI role and the actor doing the judgment (Alfred, as the explicit exception), keeps its one write destination and deterministic tests, and gains a five-case judgment evaluation that a fresh session answers blind and a script scores.

- [x] G1: the operative text names one write destination and none of the removed ones
  CHECK: python3 -c "t=open('.claude/skills/seed-capture/SKILL.md').read();op=t[:t.index('## What left this skill')];bad=[w for w in ('concepts.md','PROFILE.md','wording-lenses','README count','README.md','missed.md','D-137') if w in op];print('forbidden in the operative text:',bad);print('WRITE SET CLEAN' if not bad and 'seedbank/session/' in op and 'Writes only to' in op else 'WRITE SET DIRTY')"
  EXPECT: WRITE SET CLEAN
  EVIDENCE: automatic-evidence=v1; definition-sha256=33a0c9bc47bac46a695415cd9a753f5081166868b7820a157573cde6866989fc; exit=0; EXPECT=matched; output-sha256=d1cb9dc6f50da33eed00a9cf9fb455172bd1c640b89d2b49fe8597447e411c10; output-bytes=52; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=e809136c1bd3/38 entries

- [x] G2: the skill names what changes because AI exists, and states one job with two gates
  CHECK: python3 -c "t=open('.claude/skills/seed-capture/SKILL.md').read();ok=all(s in t.lower() for s in ('because ai exists','one job with two gates','remove the ai'));print('AI ROLE NAMED' if ok else 'AI ROLE MISSING')"
  EXPECT: AI ROLE NAMED
  EVIDENCE: automatic-evidence=v1; definition-sha256=d0b6455e4ddc2982939b87b638adbad1b904dfc1c378d16d528ad48f36ff7c50; exit=0; EXPECT=matched; output-sha256=66f4e5e63a43a0d58b48824bef4fa32df49f82e4492e9156aac522390408e7b1; output-bytes=14; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=e809136c1bd3/38 entries

- [x] G3: the skill declares seed judgment as specialist work and Alfred's part as the explicit exception
  CHECK: python3 -c "t=open('.claude/skills/seed-capture/SKILL.md').read();ok='## Who does the judgment' in t and 'substantive' in t and 'explicit exception' in t and 'cultivator' in t;print('ACTOR DECLARED' if ok else 'ACTOR MISSING')"
  EXPECT: ACTOR DECLARED
  EVIDENCE: automatic-evidence=v1; definition-sha256=d3734cc8e373d7ecd9dd397945baa74dc83a83452bd99eda354a4f36159fe4bd; exit=0; EXPECT=matched; output-sha256=d3e23ca88de7a87a9087ec14e5119c6ffc12553df5795e33b51d2920a9e34956; output-bytes=15; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=e809136c1bd3/38 entries

- [x] G4: the close routine names the same exception in its seed step
  CHECK: python3 -c "t=open('.claude/skills/alfred-close/SKILL.md').read();s=t[t.index('3. **Seeds'):t.index('4. **Duty seven')];print('CLOSE NAMES EXCEPTION' if 'explicit exception' in s and 'specialist' in s else 'CLOSE SILENT')"
  EXPECT: CLOSE NAMES EXCEPTION
  EVIDENCE: automatic-evidence=v1; definition-sha256=d04697c29dc94abde39bdbef09762930ead95cc7cd08150921d278434f54174d; exit=0; EXPECT=matched; output-sha256=d79ec94c57c1fca7b1f226ef3e090796b8908638ebbf155ceeb1ccb23b2ad514; output-bytes=22; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=e809136c1bd3/38 entries

- [x] G5: the deterministic tests pass: known seed, broken seed, repeat, no seed, scan tools write nothing, write boundary
  CHECK: python3 .claude/skills/seed-capture/tests/seed_check_tests.py
  EXPECT: SEED CHECK TESTS PASSED
  EVIDENCE: automatic-evidence=v1; definition-sha256=c937a5168986498556ba3c9c2ade38259cc5f2825425bfacd83e745c518eda2e; exit=0; EXPECT=matched; output-sha256=7f98aa750b2499ebab911d8c5f685b5dd6c3c1c3d2e34f54f007a490096f97df; output-bytes=916; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=e809136c1bd3/38 entries

- [x] G6: the judgment set holds five cases of the five required kinds, and the cases file carries no answers
  CHECK: python3 .claude/skills/seed-capture/tests/judgment/score.py --check-set
  EXPECT: JUDGMENT SET OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=15cbf286c7b1f7eec9685f9547135d748248a81ae9e279abbd8b9d636bc49bfb; exit=0; EXPECT=matched; output-sha256=15792b47b462b469d792a3a9e6f230193a7ed830a05f2cb8071429a53ca5c53f; output-bytes=40; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=e809136c1bd3/38 entries

- [x] G7: a fresh session, given the cases without answers, told strong candidates from plausible non-seeds
  CHECK: python3 .claude/skills/seed-capture/tests/judgment/score.py /private/tmp/claude-501/-Users-venkatgullapalli-Documents-my-ai-lab/e6e5d2bc-4b33-43b1-ad40-8bbd95c2b491/scratchpad/judgment-verdicts.json
  EXPECT: JUDGMENT EVAL PASSED
  EVIDENCE: automatic-evidence=v1; definition-sha256=3b5dbfd6047a1f6e2bef781cde82947e5a46bd66b985db7aef375f9ae9248ecb; exit=0; EXPECT=matched; output-sha256=770656df83a63c3205f59f24ebdbb205ac1e1a91fafcf5577aae3dcf1c314216; output-bytes=893; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=e809136c1bd3/38 entries

- [x] G8: the strict skill check reports zero problems
  CHECK: python3 .claude/skills/context-check/skill-check.py --summary
  EXPECT: /0 files with 0 problems/
  EVIDENCE: automatic-evidence=v1; definition-sha256=e6ec05204516c0822f332001f991089153bf44217a1331c0c4e2fa2045cccbb6; exit=0; EXPECT=matched; output-sha256=6fcb1c9c955de0086906e9e195cb8cc6547659ae41df10c9a0973c5ae3e7c38b; output-bytes=88; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=e809136c1bd3/38 entries

- [x] G9: the architecture check still passes
  CHECK: python3 docs/architecture/check.py
  EXPECT: OK architecture check
  EVIDENCE: automatic-evidence=v1; definition-sha256=8a300f676a5db54d09e1254dbd946b8855dd6279bbec232048212c258ac17433; exit=0; EXPECT=matched; output-sha256=646324b20266d579f8f99d2a9c40ca65ffed6f8a48f08965d1bc1323313d0118; output-bytes=100; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=e809136c1bd3/38 entries

- [x] G10: only the owned files changed, plus what the lab's own hooks write on their own, plus what the morning goal left uncommitted
  CHECK: python3 -c "import subprocess;ok=('.claude/skills/seed-capture/','.claude/skills/alfred-close/SKILL.md','GATES.md','evidence/','.claude/agents/alfred/LOG.md','.claude/agents/alfred/state/','docs/research/2026-09-14--step-2-5a-research-brief.md','docs/architecture/','.claude/skills/context-check/');rows=[l[3:] for l in subprocess.run(['git','status','--porcelain'],capture_output=True,text=True).stdout.splitlines()];bad=[r for r in rows if not r.startswith(ok)];print('unexpected:',bad);print('ONLY OWNED FILES CHANGED' if not bad else 'UNRELATED CHANGE')"
  EXPECT: ONLY OWNED FILES CHANGED
  EVIDENCE: automatic-evidence=v1; definition-sha256=1dffeb07021d878b78be5ed36de188546ee1136f03dd3236e30800285be2554b; exit=0; EXPECT=matched; output-sha256=4eacc3661c2c3d66346883c0e0fe59b7930ef318d2cf252aef952be37fd38587; output-bytes=40; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=e809136c1bd3/38 entries
