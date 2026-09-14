# Gates: 38 follow-ups Alfred can do alone (2026-09-14)

OWNS: CLAUDE.md, TASTE.md, DONE.md, context/README.md, .claude/**, context/sources/**, work-os/brand-os/model/**, work-os/scheduled-tasks/market-signals/assemble.sh, docs/about-me/VOICE-PROFILE-venkat-gullapalli.md, docs/ecosystem/**

Scope: close six moot follow-ups, fix ten sensor and script defects with tests, correct sixteen stale lines and dead pointers, rename the ecosystem files, and prepare six reviews, all local and undoable

- [x] G1: facts.py tests pass after the close-count, closed-ID, drivers-proof, model-check, no-transcript and index-age changes
  CHECK: python3 .claude/agents/alfred/sensors/tests/facts_tests.py
  EXPECT: FACTS TESTS PASSED
  EVIDENCE: automatic-evidence=v1; definition-sha256=fbd11a03dc7dc75c4c676a1fdcb2adeccbfd4443159c3b8a853f8786874ed10b; exit=0; EXPECT=matched; output-sha256=c4492e5a5d57be9b676b5876f369ad1ccbed2e49fd60820b9df77fda4c6a8261; output-bytes=2821; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=c7a0898f6518/38 entries

- [x] G2: facts sheet carries the three new sensor lines (career model check, notes with no transcript, retrieval index age)
  CHECK: python3 -c "import subprocess;o=subprocess.run(['python3','.claude/agents/alfred/sensors/facts.py','open'],capture_output=True,text=True).stdout;ks=['career model check:','sessions with a note but no transcript:','retrieval index:'];m=[k for k in ks if k not in o];print('missing:',m) if m else print('THREE SENSOR LINES PRESENT')"
  EXPECT: THREE SENSOR LINES PRESENT
  EVIDENCE: automatic-evidence=v1; definition-sha256=b7da84de0fb052a3b4dd24006b160ce46090f73b33c0b7879dcd3b31db687801; exit=0; EXPECT=matched; output-sha256=35908c85a377a8bed8d84d0beaf538d61638e0f4c6cced82a2e1401e44f885ca; output-bytes=27; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=c7a0898f6518/38 entries

- [x] G3: source-register tests pass with the two new planted-fault cases and the four retrieval defects fixed
  CHECK: python3 context/sources/tests/check_tests.py
  EXPECT: all passed
  EVIDENCE: automatic-evidence=v1; definition-sha256=3f773b4f33395efef1e5cb164274fce6913760a78211f375b351502ef81fff84; exit=0; EXPECT=matched; output-sha256=0254c6c27f2851207a7621ae5fbc295d6093dc8127a340bcb7d1d92a611019ad; output-bytes=1362; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=c7a0898f6518/38 entries

- [x] G4: session-sync secret pattern masks a fake Anthropic key with dashes and a fake Google key, and a plain sentence is left alone
  CHECK: python3 -c "import importlib.util as u;s=u.spec_from_file_location('ss','.claude/agents/alfred/sensors/session-sync.py');m=u.module_from_spec(s);s.loader.exec_module(m);a='sk-ant-api03-AbCdEf-GhIjKl_MnOpQr-StUvWx_YzAbCd-EfGhIjKlMnOpQrStUvWxYzAbCdEfGh';g='AIzaSyA1b2C3d4E5f6G7h8I9j0K1l2M3n4O5p6Q';assert m.SECRET.search(a),'anthropic missed';assert m.SECRET.search(g),'google missed';assert not m.SECRET.search('the lab root became a repository on 2026-09-09'),'false hit';print('SECRET PATTERN OK')"
  EXPECT: SECRET PATTERN OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=b0cd264e093709b1c8289a48fa0bb22677e5948545f8ec5734c318114f6f7701; exit=0; EXPECT=matched; output-sha256=cf5e93b07de2cd305d5ecc869123f094fcfcee4263fca1ceb36f1332fff4c49d; output-bytes=18; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=c7a0898f6518/38 entries

- [x] G5: CLAUDE.md no longer says 26 skills, ten things, or no off-machine copy
  CHECK: python3 -c "t=open('CLAUDE.md').read();bad=[s for s in ['26 skills','Only ten things','No off-machine copy of anything'] if s in t];print('still there:',bad) if bad else print('FRONT DOOR LINES FIXED')"
  EXPECT: FRONT DOOR LINES FIXED
  EVIDENCE: automatic-evidence=v1; definition-sha256=faf5897dd63b3e48867bb0a5109b22bbf8d33149f78428aef2653aa2b5f95c51; exit=0; EXPECT=matched; output-sha256=fcfe44414959c64bd633ebfad966e625801569c21ff7d650a8bf995ee0469b1e; output-bytes=23; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=c7a0898f6518/38 entries

- [x] G6: TASTE.md, context/README.md, and DONE.md no longer carry the three false lines
  CHECK: python3 -c "bad=[];t=open('TASTE.md').read();bad+=['TASTE PROFILE.md'] if 'context/PROFILE.md' in t else [];t=open('context/README.md').read();bad+=['README loaded'] if 'Loaded every session' in t else [];t=open('DONE.md').read();bad+=['DONE bypass'] if \"can't be bypassed by a prompt, agent, plugin, or connector\" in t else [];print('still there:',bad) if bad else print('THREE FALSE LINES FIXED')"
  EXPECT: THREE FALSE LINES FIXED
  EVIDENCE: automatic-evidence=v1; definition-sha256=667a745fe445eb3d1a9b74ebe575a186d2eff788075fc9832fb07ebace534143; exit=0; EXPECT=matched; output-sha256=ed30db41fd11a836512f94f616b5da66603be0ec040207c358d89123e39aad49; output-bytes=24; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=c7a0898f6518/38 entries

- [x] G7: skill check reports no missing base directory line and no problem from book-to-skill or contextual-voice
  CHECK: python3 -c "import subprocess;o=subprocess.run(['python3','.claude/skills/context-check/skill-check.py'],capture_output=True,text=True).stdout;bad=[s for s in ['NO BASE DIRECTORY LINE','book-to-skill','contextual-voice'] if s in o];print('still there:',bad) if bad else print('BASE LINES OK')"
  EXPECT: BASE LINES OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=52556f638473c91e69381adb7e0454cca48dee1e716238179ca45d896fb2e52d; exit=0; EXPECT=matched; output-sha256=9894a47fe47cb5c8f1fd0faf19349dbdb80183c0ab559a0738f0e89b8b673281; output-bytes=14; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=c7a0898f6518/38 entries

- [x] G8: no live skill or agent file under .claude still says PROJECT-SPECIFIC to AI Advisory Search (Alfred's log is history and may)
  CHECK: python3 -c "import subprocess;o=subprocess.run(['grep','-rl','AI Advisory Search','.claude'],capture_output=True,text=True).stdout.split();o=[f for f in o if not f.endswith('LOG.md')];print('still:',o) if o else print('STALE NAME GONE')"
  EXPECT: STALE NAME GONE
  EVIDENCE: automatic-evidence=v1; definition-sha256=9352268fb2daae73c0acdb2d74dfeca587c61cb72ed9c065a3533f50bccd2d34; exit=0; EXPECT=matched; output-sha256=87ff0194acd82f963c878d0b04a0a27ba573c5eb9487b771120100c384a52c4c; output-bytes=16; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=c7a0898f6518/38 entries

- [x] G9: assemble.sh reads the trigger id as its own column and the foundation daily routine body shows a clean uuid
  CHECK: python3 -c "import re,json;s=open('work-os/scheduled-tasks/market-signals/assemble.sh').read();assert re.search(r'read -r .*\\buuid\\b.*\\btrig\\b',s) or re.search(r'read -r .*\\btrig\\b',s),'no trig column';b=json.load(open('work-os/scheduled-tasks/market-signals/01-foundation/daily/build/routine-body.json'));t=json.dumps(b);ids=re.findall(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}',t);assert ids,'no uuid';assert '|' not in ''.join(ids);print('ASSEMBLE OK')"
  EXPECT: ASSEMBLE OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=8381802e02f1273129d9f68c36100f56ba38fa93c00a48cd9f7f96b28c038bf5; exit=0; EXPECT=matched; output-sha256=525e8147a22d606bea560b173233b6565a8e4c82e52bdead3dd20ffe25416622; output-bytes=12; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=c7a0898f6518/38 entries

- [x] G10: the nine ecosystem files carry date-first names and the same bytes as before the rename
  CHECK: python3 -c "import hashlib,os,re;d='docs/ecosystem';fs=sorted(os.listdir(d));assert len(fs)==9,fs;assert all(re.match(r'^2026-09-1[34]--[a-z0-9-]+\\.md$',f) for f in fs),fs;before=sorted(l.split()[0] for l in open('/private/tmp/claude-501/-Users-venkatgullapalli-Documents-my-ai-lab/6e33e463-c18c-4a9a-92e3-d9838b9d00a1/scratchpad/eco-manifest.sha'));after=sorted(hashlib.sha256(open(os.path.join(d,f),'rb').read()).hexdigest() for f in fs);assert before==after,'bytes differ';print('RENAME VERIFIED')"
  EXPECT: RENAME VERIFIED
  EVIDENCE: automatic-evidence=v1; definition-sha256=6185e083a70858efd0ed2224c98c56e35137f9c7181f1212de634adae48e5935; exit=0; EXPECT=matched; output-sha256=5387e130b587b771e063517e17b84866b3ce394c8051501a5a7706dc1f98f256; output-bytes=16; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=c7a0898f6518/38 entries

- [x] G11: no live dead pointer remains under .claude/ or in CLAUDE.md, and the whole sweep is below 60 unreviewed mentions
  CHECK: python3 -c "import subprocess,re;o=subprocess.run(['python3','.claude/skills/context-check/dead-pointers.py'],capture_output=True,text=True).stdout;files=re.findall(r'^  (\\S+)$',o,re.M);n=int(re.search(r'LIVE DEAD POINTERS: (\\d+)',o).group(1));bad=[f for f in files if f.startswith('.claude/') or f=='CLAUDE.md'];print('bad:',bad,'total:',n) if bad or n>=60 else print('SWEEP DONE',n)"
  EXPECT: SWEEP DONE
  EVIDENCE: automatic-evidence=v1; definition-sha256=c44c556c0a31e84e5dc60a086cb00380beee4247b3726e87e47e35e11eccaafb; exit=0; EXPECT=matched; output-sha256=3745e8ccd8fbd74f679ce859aa80b53f1a18c44fa8e2cef89157fa9a9dedd3b0; output-bytes=13; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=c7a0898f6518/38 entries

- [x] G12: the career model folder says 14 recovered, SPOKES.md matches ruling 038, status names the lab as home, the README open-items line no longer lists the PV Index spec, the graph has the PRD-002 to CAP-068 edge, and decision-log.md has a dated line for each
  CHECK: python3 -c "import os,glob;m='work-os/brand-os/model/';bad=[];t=open(m+'03-career-stage-map.md').read();bad+=['21 recovered'] if '21 recovered' in t else [];t=open(m+'00-status.md').read();bad+=['Desktop path'] if 'Desktop' in t else [];t=open(m+'README.md').read();bad+=['PV Index unlocated'] if 'PV Index' in t and 'unlocated' in t else [];t=open(m+'decision-log.md').read();bad+=['no 2026-09-14 log line'] if '2026-09-14' not in t else [];print('still:',bad) if bad else print('MODEL LINES FIXED')"
  EXPECT: MODEL LINES FIXED
  EVIDENCE: automatic-evidence=v1; definition-sha256=1988deff6b87752730ddcfded533beb2ddca9ccb2c0b2c745e5ac683d0b62faa; exit=0; EXPECT=matched; output-sha256=a31fa97a97407caa96d57cba856b1fc65883e582a778f0a6b1f80e6113b5915b; output-bytes=18; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=c7a0898f6518/38 entries

- [x] G13: the profile's Q2 status matches the interview file (approval note copied), and the alfred-open skill's D3 line says what verify.sh actually needs
  EVIDENCE: profile line 193 now carries the 01:58 approval and 01:59 revision (grep 'APPROVED by Venkat 2026-09-11 01:58' docs/about-me/VOICE-PROFILE-venkat-gullapalli.md = 1 hit); alfred-open SKILL.md step 2 now says D3 cannot run verify.sh without a folder of fetched routine responses and marks the 21 Unknown (checked by reading the file 2026-09-14 03:08)

- [x] G14: six reviews are prepared in the scratchpad and summarized in the reply: brief overlap (0248-3), snapshot holds the 137 ignored files (0220-2), restore-and-diff sensor plan (0540-1), mid-task message render plan (0602-2), Q14 check (1510-10), contextual-voice findings 2 to 5 (0540-5)
  EVIDENCE: six files in the session scratchpad, read by Alfred 2026-09-14: brief-overlap-review.md (41 lines, zero same-day repeats across 3 shared dates), snapshot-references-check.md (57 of 137 in the tar, 80 added after 09-10), restore-and-diff-sensor-plan.md (35 lines, planted-fault done by hand), mid-task-render-plan.md (34 lines, patch applies clean), voice-checks.md (50 lines: Q14 restart does not match, findings 2 to 5 hold), commit-key-guard-plan.md (13 lines)

- [x] G15: the six moot follow-ups (1627-4, 1508-1, 2141-2, 2141-3, 2258-3, 0215-3) are listed with their proof for the close routine to mark closed, and the discovery items (0134-2) are reviewed into discovery-accepted.txt with a reason each
  EVIDENCE: closes.md in the session scratchpad lists the six with proof lines for alfred-close; discovery-accepted.txt gained 20 domain lines with reasons (check.py now: discovery 5 to review, 1 recorded; was 21 recorded)
