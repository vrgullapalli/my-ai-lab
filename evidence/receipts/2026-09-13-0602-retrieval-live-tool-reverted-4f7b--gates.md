# Gates: Retrieval v0.1

OWNS: context/sources/retrieve.py, context/sources/index/**, context/sources/tests/run_tests.py, .claude/skills/retrieval/**, docs/reports/2026-09-12--retrieval-v0-1*.md, context/sources/discovery-accepted.txt

Scope: the minimum Retrieval that passes the seven frozen tests in context/sources/tests/RETRIEVAL-TESTS.md, with the model limited to semantic candidate selection, ranking, and conflict flagging, evidence fetched deterministically after selection, and the size of the full-index semantic pass measured on every run. All checks run python3 from the lab root.

- [x] G1: the derived index covers every file of the eligible source set
  CHECK: python3 context/sources/retrieve.py index
  EXPECT: coverage complete
  EVIDENCE: automatic-evidence=v1; definition-sha256=ef618c8c63d76398ec9619a194226fec21cae5e2499b3dfb640d14ef56576560; exit=0; EXPECT=matched; output-sha256=688f43683f99ce305d18c4702993a9af7aa310956614512104fac52eb30b85e9; output-bytes=121; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=3702f30b69b7/61 entries

- [x] G2: a fetch of a path outside the register is refused
  CHECK: python3 context/sources/tests/run_tests.py --prove-boundary
  EXPECT: boundary refused
  EVIDENCE: automatic-evidence=v1; definition-sha256=2f5577703aac24a9b543b05f20d3696e630cd4bcee54057983c93aead94721a8; exit=0; EXPECT=matched; output-sha256=c08497302a7ea1450565ca27603b72ea162d966aba2a6ce139c4cb38d02d974d; output-bytes=112; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=3702f30b69b7/61 entries

- [ ] G3: the seven frozen tests pass on a blind semantic pass plus deterministic fetch
  CHECK: python3 context/sources/tests/run_tests.py --selections context/sources/index/selections.json
  EXPECT: RETRIEVAL TESTS: 7 of 7 passed
  EVIDENCE: pending

- [x] G4: the size and estimated cost of the full-index semantic pass is measured and printed
  CHECK: python3 context/sources/retrieve.py stats
  EXPECT: /index size: \d+ records, \d+ bytes, ~\d+ tokens/
  EVIDENCE: automatic-evidence=v1; definition-sha256=27948a22602a73ede47aa09484842d713e5d987bde1bee11597d020ca0945d1b; exit=0; EXPECT=matched; output-sha256=1107eb900897e4225b9caffef871b3991bdb3b9cbffe1248dc708c1e969fa56a; output-bytes=141; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=3702f30b69b7/61 entries

- [x] G5: the canonical career model is untouched by every run
  CHECK: python3 -c "import subprocess;o=subprocess.run(['git','status','--porcelain','work-os/brand-os/model'],capture_output=True,text=True).stdout;print('model untouched' if not o.strip() else 'model changed:\n'+o)"
  EXPECT: model untouched
  EVIDENCE: automatic-evidence=v1; definition-sha256=4873cb6c818157a164d3dfcd9795bcda4a9a064b100fcbd8cee8e688952cfb0e; exit=0; EXPECT=matched; output-sha256=c4a9b278e0e1fef4f1575b8b41944fd2b839e8f68b9c8129d8fe33001fbea182; output-bytes=16; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=3702f30b69b7/61 entries

- [x] G6: the source register still passes with the index in place
  CHECK: python3 context/sources/check.py --summary
  EXPECT: register findings: 0
  EVIDENCE: automatic-evidence=v1; definition-sha256=be58319026494beda667b7f787964631c694c30d4e32be2f3d3d8c19008f956a; exit=0; EXPECT=matched; output-sha256=bb63cedc996bbaa8753036d9d71b0e8cb6574322d7e6f68ab5f8b3e2ea5ef41c; output-bytes=194; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=3702f30b69b7/61 entries

- [x] G7: the architecture check still passes
  CHECK: python3 docs/architecture/check.py
  EXPECT: 0 finding(s)
  EVIDENCE: automatic-evidence=v1; definition-sha256=8ca3015ba36e06d3112040163934de3ca26cb5cc16b8164add55f051055bd13c; exit=0; EXPECT=matched; output-sha256=646324b20266d579f8f99d2a9c40ca65ffed6f8a48f08965d1bc1323313d0118; output-bytes=100; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=3702f30b69b7/61 entries

- [x] G8: every known-answer file is still inside the eligible set
  CHECK: python3 context/sources/tests/reachability.py
  EXPECT: OK reachability
  EVIDENCE: automatic-evidence=v1; definition-sha256=a0ec7b71d87686f328e2fe149cc10663920c30973cd20cf6969d01a3a042a1d5; exit=0; EXPECT=matched; output-sha256=7cd63fa8a5be4b73052da073507a348ac48fe772f6fa3249e6f436e0235bf35c; output-bytes=391; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=3702f30b69b7/61 entries

- [x] G9: the register's planted-fault tests still pass
  CHECK: python3 context/sources/tests/check_tests.py
  EXPECT: all passed
  EVIDENCE: automatic-evidence=v1; definition-sha256=3f773b4f33395efef1e5cb164274fce6913760a78211f375b351502ef81fff84; exit=0; EXPECT=matched; output-sha256=16eebeb6a0cf240faf3a2af195120286a43a2353d81a4e004e11b8baf0c58b68; output-bytes=1293; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=3702f30b69b7/61 entries

- [x] G10: a dated run report with the results and the size measurement exists in docs/reports
  CHECK: python3 -c "import glob;fs=glob.glob('docs/reports/2026-09-12--retrieval-v0-1*.md');t=open(fs[0]).read() if fs else '';print('report present with size line' if fs and 'index size' in t else 'no report or no size line')"
  EXPECT: report present with size line
  EVIDENCE: automatic-evidence=v1; definition-sha256=b82e3f86ee4c3f27572e2cad6694cb6bc7e10dfa49932902ceb6a0184ef25bf8; exit=0; EXPECT=matched; output-sha256=288e8175ff492bd5b318c0ab3a9dbc997725d5a2b91390f428582a1cf293ea5b; output-bytes=30; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=3702f30b69b7/61 entries

- [x] G11: the retrieval skill exists and declares its base directory
  CHECK: python3 -c "t=open('.claude/skills/retrieval/SKILL.md').read();print('base line present' if 'Base directory' in t else 'missing')"
  EXPECT: base line present
  EVIDENCE: automatic-evidence=v1; definition-sha256=a187885f4246450a65188d3d2723287738ac756ea6980382133bf0241a88bbb4; exit=0; EXPECT=matched; output-sha256=54113163794e0d204e2566e6506a098959fd2c47fa80db5bc572beeea601d2cf; output-bytes=18; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=3702f30b69b7/61 entries

- [x] G12: the semantic candidate-selection change is scored blind on all seven frozen tests, T2 first, and the result line is printed whatever it says
  CHECK: python3 -c "import subprocess;r=subprocess.run(['python3','context/sources/tests/run_tests.py','--selections','context/sources/index/selections.json'],capture_output=True,text=True);print([l for l in r.stdout.splitlines() if l.startswith('RETRIEVAL TESTS')][0])"
  EXPECT: /RETRIEVAL TESTS: [0-7] of 7 passed/
  EVIDENCE: automatic-evidence=v1; definition-sha256=9d9d0e0b23a3b098fec735bff2fd7285e2dba20a3eac9ef603d29d29def7dced; exit=0; EXPECT=matched; output-sha256=da3f87429a8a2168145b13586980f388ef95da617127f27802d24b8c96a89800; output-bytes=31; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=3702f30b69b7/61 entries

- [x] G13: a dated report records the method, the T2 result, the full result against the 5 of 7 baseline, cost, and any new failure
  CHECK: python3 -c "import glob;fs=sorted(glob.glob('docs/reports/2026-09-12--retrieval-v0-1-semantic*.md'));t=open(fs[-1]).read() if fs else '';print('semantic report present' if fs and 'baseline' in t and 'T2' in t and 'tokens' in t else 'missing')"
  EXPECT: semantic report present
  EVIDENCE: automatic-evidence=v1; definition-sha256=34841ebb2d71a832edbd086f4e40c092684615a6edc965bfdd1eaecd54580431; exit=0; EXPECT=matched; output-sha256=18de10e461bcb3c1b2d71a2f32d4f2ae3410a9b11508f04ede4edf09e6437482; output-bytes=24; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=3702f30b69b7/61 entries

- [x] G14: the staged-selection experiment's grouping is proven: every scoped record in exactly one group, must-consider held out, and a planted duplicate fails the check
  CHECK: python3 -c "import subprocess as s;a=s.run(['python3','context/sources/tests/staged_experiment.py','check','--out','context/sources/index/runs/staged-T2-A'],capture_output=True,text=True);b=s.run(['python3','context/sources/tests/staged_experiment.py','check','--out','context/sources/index/runs/staged-T2-A','--plant'],capture_output=True,text=True);print('grouping proven' if a.returncode==0 and b.returncode==1 else 'grouping not proven: '+a.stdout+b.stdout)"
  EXPECT: grouping proven
  EVIDENCE: automatic-evidence=v1; definition-sha256=ba388d995d090a483bd43a336e69641235a0b7b4041ffff173212bfdbe2bfea9; exit=0; EXPECT=matched; output-sha256=26cdb1dbadad8c06ce9e18f9aecbd7dbe17d3782dec8a784ca8577483a6221a9; output-bytes=16; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=3702f30b69b7/61 entries

- [ ] G15: the staged experiment is scored blind on T2 first and then all seven, and the result line is printed whatever it says
  CHECK: python3 -c "import subprocess;r=subprocess.run(['python3','context/sources/tests/run_tests.py','--selections','context/sources/index/runs/staged-selections.json'],capture_output=True,text=True);print([l for l in r.stdout.splitlines() if l.startswith('RETRIEVAL TESTS')][0])"
  EXPECT: /RETRIEVAL TESTS: [0-7] of 7 passed/
  EVIDENCE: pending

- [x] G16: a dated report records the staged run: accuracy against the baseline and the hundred-line runs, the seed's stage-1 fate, two-salt stability, cost in tokens, and latency
  CHECK: python3 -c "import glob;fs=sorted(glob.glob('docs/reports/2026-09-12--retrieval-v0-1-staged*.md'));t=open(fs[-1]).read() if fs else '';print('staged report present' if fs and all(w in t for w in ('baseline','salt','tokens','latency','stage 1')) else 'missing')"
  EXPECT: staged report present
  EVIDENCE: automatic-evidence=v1; definition-sha256=1b08e06c3929dd5996dff4bb8aafbdf0c1bc5b39211337f41e6c5f5c94363455; exit=0; EXPECT=matched; output-sha256=57b1b0222594d93f56809131b8e31368ba32c0afbb657ae73e16f2d1881c0bdc; output-bytes=22; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=3702f30b69b7/61 entries

- [x] G17: the jobs reconstruction is written as a dated report with the four asked-for parts: the job list with the eight fields, the top jobs, the three stress tests, and the single proving-ground pick with evidence
  CHECK: python3 -c "t=open('docs/reports/2026-09-13--alfred-real-jobs-reconstructed.md').read();need=('Trigger','Inputs needed','His judgment','Friction','Freq','stress','proving ground','Evidence');miss=[w for w in need if w.lower() not in t.lower()];print('jobs report complete' if not miss else 'missing: '+', '.join(miss))"
  EXPECT: jobs report complete
  EVIDENCE: automatic-evidence=v1; definition-sha256=a5adfbef9e77a71844d77ae2fb9e141289d0b630454f41c586a0ab0c6b478772; exit=0; EXPECT=matched; output-sha256=a0afad7ead8e2517dec7810f1ae3712a686ce9b302a424d024c1996975bed523; output-bytes=21; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=92b72f00e8ac/38 entries

Close-out at his word, 2026-09-13 05:29 (the /goal that answers the G3 and G15 handoffs: reuse the stage-one picks, remove the second-level cut, rank the 172-record unions once, then the seven if T2 permits):

- [x] G18: both one-level unions are rebuilt from the saved stage-one picks, 172 records each, the seed inside, no second level
  CHECK: python3 -c "import json;ms=[json.load(open(f'context/sources/index/runs/staged-T2-{s}-one-level/manifest.json')) for s in 'AB'];us=[open(f'context/sources/index/runs/staged-T2-{s}-one-level/union.txt').read() for s in 'AB'];print('unions rebuilt' if all(m.get('levels')==1 and m.get('union_size')==172 for m in ms) and all('A-LIVE-187' in u for u in us) else 'not rebuilt')"
  EXPECT: unions rebuilt
  EVIDENCE: automatic-evidence=v1; definition-sha256=da50adc37c58ed4d513b4c4c8a2673cc2002cae0f87b4c9f7605f6efee702c56; exit=0; EXPECT=matched; output-sha256=4ca973c6de193a599d9892ecf4d16086b0fa865bee86d802f424693d0c36e721; output-bytes=15; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=92b72f00e8ac/38 entries

- [x] G19: T2 is scored blind under salt A on the one-level union, and the result line is printed whatever it says
  CHECK: python3 -c "import subprocess;r=subprocess.run(['python3','context/sources/tests/run_tests.py','--selections','context/sources/index/runs/staged-T2-A-one-level-selections.json'],capture_output=True,text=True);print([l for l in r.stdout.splitlines() if l.startswith(('PASS T2','FAIL T2'))][0])"
  EXPECT: /^(PASS|FAIL) T2 /
  EVIDENCE: automatic-evidence=v1; definition-sha256=fadccd98fbc39dc5280d8e87e984497584c34a091587aadce2327bbd2aa38011; exit=0; EXPECT=matched; output-sha256=5db0d1002ec2babc8a32488e5051a4df13a8e80fbec397eebb63186274d13df9; output-bytes=236; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=92b72f00e8ac/38 entries

- [x] G20: T2 is scored blind under salt B on the one-level union, and the result line is printed whatever it says
  CHECK: python3 -c "import subprocess;r=subprocess.run(['python3','context/sources/tests/run_tests.py','--selections','context/sources/index/runs/staged-T2-B-one-level-selections.json'],capture_output=True,text=True);print([l for l in r.stdout.splitlines() if l.startswith(('PASS T2','FAIL T2'))][0])"
  EXPECT: /^(PASS|FAIL) T2 /
  EVIDENCE: automatic-evidence=v1; definition-sha256=0115332505dff123a008d28bee29c161f71f708d1ff37e0a33fdfd72eda5155a; exit=0; EXPECT=matched; output-sha256=cc1899a6bb7a1560aec9106b87dfe0871f86e74556fcf1545421d2e6674f5a60; output-bytes=233; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=92b72f00e8ac/38 entries

- [x] G21: the seven frozen tests are scored as one file, T2 from the staged one-level salt A run and the other six from the last full run (T2 did not permit the six staged runs), and the result line is printed whatever it says; replaces the handed-off G15
  CHECK: python3 -c "import subprocess;r=subprocess.run(['python3','context/sources/tests/run_tests.py','--selections','context/sources/index/runs/staged-selections.json'],capture_output=True,text=True);print([l for l in r.stdout.splitlines() if l.startswith('RETRIEVAL TESTS')][0])"
  EXPECT: /RETRIEVAL TESTS: [0-7] of 7 passed/
  EVIDENCE: automatic-evidence=v1; definition-sha256=8da9d6244d38ed985398ede062f50a6a58c92020b7ca1396de924f293599ec9e; exit=0; EXPECT=matched; output-sha256=da3f87429a8a2168145b13586980f388ef95da617127f27802d24b8c96a89800; output-bytes=31; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=92b72f00e8ac/38 entries

- [x] G22: a dated close-out report records T2 under both salts, the seven-test result, the K deviation, known limitations, and the package interface for downstream consumers
  CHECK: python3 -c "t=open('docs/reports/2026-09-13--retrieval-v0-1-close-out.md').read().lower();need=('salt a','salt b','of 7','limitation','interface','k=8','deviation','downstream');miss=[w for w in need if w not in t];print('close-out report complete' if not miss else 'missing: '+', '.join(miss))"
  EXPECT: close-out report complete
  EVIDENCE: automatic-evidence=v1; definition-sha256=695557636ee3fc21b4acb21c5792bfff4ba9ca8228f7567491f2c172944e144a; exit=0; EXPECT=matched; output-sha256=37d9758298a7695fa2672d1855e87f8db88e2b31c86a87ddf4afc2191c138e6f; output-bytes=26; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=92b72f00e8ac/38 entries

ABANDON: G3 five of seven frozen tests pass in the final blind run (run 4); T2 (meaning match to seed A-LIVE-187 and the article's research file) failed in all four blind runs and T4 failed on one file's rank in all four. Passing them needs either a different semantic method or a change to a frozen test, and both are Venkat's word, not a session's. Handoff: docs/reports/2026-09-12--retrieval-v0-1-first-runs.md, sections 4 and 5, with the two questions for him.
ABANDON: G15 needs Venkat: the seven-test staged run waits on his choice between lifting the union cap to 180 (one final rank) and widening the second level's K, because both salts showed stage 1 picking the seed and the second level dropping it, and the plan's own rule forbids a session changing a parameter after a T2 failure. Handoff: docs/reports/2026-09-12--retrieval-v0-1-staged-selection.md, section 4. T2 was scored under both salts (FAIL on the frozen condition; stage 1 hit twice); the seven run as soon as he chooses.
