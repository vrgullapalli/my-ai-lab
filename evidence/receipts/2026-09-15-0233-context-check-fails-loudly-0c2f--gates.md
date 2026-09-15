# Gates: context-check repaired against Operational DNA v2 (audit of 2026-09-15)

OWNS: .claude/skills/context-check/**, .unlazy/context-check-repair/**

Scope: context-check.sh, dead-pointers.py, and skill-check.py fail visibly on a wrong or empty root and on a helper crash; the superseded four-name detector is gone; measured and word-match labels stay in the output; accepted is reported apart from open and never as resolved; docs/ and context/ are covered or excluded on purpose; the response owner is named; every planted failure has a test.

- [x] G1: an empty root makes context-check.sh fail visibly, not report a clean lab
  CHECK: python3 -c "import os,subprocess,tempfile;d=tempfile.mkdtemp();r=subprocess.run(['/bin/bash','.claude/skills/context-check/context-check.sh'],env=dict(os.environ,LAB_ROOT=d,LAB_SNAPSHOTS=d+'/none'),capture_output=True,text=True);o=r.stdout+r.stderr;print('exit',r.returncode);print('EMPTY ROOT FAILS VISIBLY' if r.returncode!=0 and 'NOT A LAB ROOT' in o and 'TOTAL ORPHANS: 0' not in o else 'EMPTY ROOT LOOKS CLEAN')"
  EXPECT: EMPTY ROOT FAILS VISIBLY
  EVIDENCE: automatic-evidence=v1; definition-sha256=027d163eb6be944b48adf5d9de94f1accf1da141d278f65f6814fb28103711df; exit=0; EXPECT=matched; output-sha256=6f9ad34a0603fcebc11415757fa0c37dd6980c06b363f0ad755fa2bf75e423f0; output-bytes=32; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=46559098bd72/39 entries

- [x] G2: an empty root makes dead-pointers.py and skill-check.py fail visibly, and the facts-sheet line starts with ALERT
  CHECK: python3 -c "import os,subprocess,tempfile,sys;d=tempfile.mkdtemp();e=dict(os.environ,LAB_ROOT=d,LAB_DOCS=d+'/nd',DEAD_POINTERS_ACCEPTED=d+'/na',CLAUDE_PLUGINS=d+'/np',CLAUDE_USER_SKILLS=d+'/ns',SKILL_CHECK_ACCEPTED=d+'/na');a=subprocess.run([sys.executable,'.claude/skills/context-check/dead-pointers.py'],env=e,capture_output=True,text=True);b=subprocess.run([sys.executable,'.claude/skills/context-check/skill-check.py','--summary'],env=e,capture_output=True,text=True);oa=a.stdout+a.stderr;ob=b.stdout+b.stderr;print(a.returncode,oa.strip()[:120]);print(b.returncode,ob.strip()[:120]);print('BOTH FAIL VISIBLY' if a.returncode!=0 and 'NOT A LAB ROOT' in oa and 'LIVE DEAD POINTERS: 0' not in oa and b.returncode!=0 and b.stdout.startswith('ALERT') and '0 problems' not in ob else 'ONE LOOKS CLEAN')"
  EXPECT: BOTH FAIL VISIBLY
  EVIDENCE: automatic-evidence=v1; definition-sha256=df48bf76255525a50d10cc2cf188435ab265eac640e12217983596ab7f769fe2; exit=0; EXPECT=matched; output-sha256=a313a37fc9ffc700934b73487c65f7b8b85f05642060d73a480e9ef9965153eb; output-bytes=264; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=46559098bd72/39 entries

- [x] G3: a crashing helper shows as an ALERT in its section with the error, the run exits nonzero, and the closing line counts it
  CHECK: python3 .claude/skills/context-check/tests/context_check_tests.py
  EXPECT: CONTEXT CHECK TESTS PASSED
  EVIDENCE: automatic-evidence=v1; definition-sha256=b3a330bc58bc904f3da56860866c9aa464b1eea1ee1723a74885f161f42afaa4; exit=0; EXPECT=matched; output-sha256=0665cabbc75497250fd1be785539b7e02221765f692ccfbd24bf3f3c7205aeb7; output-bytes=2080; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=46559098bd72/39 entries

- [x] G4: the superseded four-name detector no longer exists in the script or its output
  CHECK: python3 -c "t=open('.claude/skills/context-check/context-check.sh').read();bad=[w for w in ('files mention it','\"my-ai-lab-v2/\" \"My_AI_Lab/\"') if w in t];print('bad:',bad);print('OLD DETECTOR GONE' if not bad and 'dead-pointers.py' in t else 'OLD DETECTOR PRESENT')"
  EXPECT: OLD DETECTOR GONE
  EVIDENCE: automatic-evidence=v1; definition-sha256=4eae8604a127b06d6ebcbe0d489b61f515fa8d22fdaecb095d9abeacaa2b9314; exit=0; EXPECT=matched; output-sha256=2d67beb813d6b30818e2aedd772247fcd32bbd70a3d84e4f41be4d9d13922bc4; output-bytes=26; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=46559098bd72/39 entries

- [x] G5: on the real lab every section header carries [measured] or [word match], and C and E are the only word-match sections
  CHECK: python3 -c "import subprocess,re;o=subprocess.run(['/bin/bash','.claude/skills/context-check/context-check.sh'],capture_output=True,text=True).stdout;h=re.findall(r'^([A-G])\. \[(measured|word match)\]',o,re.M);print(h);print('LABELS DISTINCT' if len(h)==7 and {l for l,k in h if k=='word match'}=={'C','E'} else 'LABELS MISSING')"
  EXPECT: LABELS DISTINCT
  EVIDENCE: automatic-evidence=v1; definition-sha256=89bec6084f360a5b291f6b4504067acb47fb957b32f6e46b2b19565b6b62628a; exit=0; EXPECT=matched; output-sha256=f7c050ae02e23d7fcfb73972a62adac9471f33cfc1c3de37a9d0a7904af8b83b; output-bytes=154; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=46559098bd72/39 entries

- [x] G6: on the real lab, accepted is reported apart from open, marked not resolved, split item, bulk, no record; the bulk sweep shows as bulk and unconfirmed
  CHECK: python3 -c "import subprocess,re;o=subprocess.run(['python3','.claude/skills/context-check/dead-pointers.py'],capture_output=True,text=True).stdout;a=re.search(r'^ACCEPTED: (\d+).*not resolved.*item by item: (\d+).*bulk by Alfred, unconfirmed: (\d+).*no acceptance record: (\d+)',o,re.M);r=re.search(r'^RESOLVED: not counted',o,re.M);print(a.group(0) if a else 'no ACCEPTED line');print('ACCEPTED APART FROM RESOLVED' if a and r and int(a.group(3))>900 and int(a.group(1))==sum(int(a.group(i)) for i in (2,3,4)) else 'ACCEPTED FOLDED')"
  EXPECT: ACCEPTED APART FROM RESOLVED
  EVIDENCE: automatic-evidence=v1; definition-sha256=97877d3d8bd4b11a110435a11351640bb56046aae7807d720dd34c2fc4b82583; exit=0; EXPECT=matched; output-sha256=d4a08095e511187f76d62e8f442c5b58c84ed810fc8936e991fd8c5012b0cadb; output-bytes=192; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=46559098bd72/39 entries

- [x] G7: dead-pointers tests pass, including the accepted-never-resolved and empty-root cases
  CHECK: python3 .claude/skills/context-check/tests/dead_pointers_tests.py
  EXPECT: DEAD POINTERS TESTS PASSED
  EVIDENCE: automatic-evidence=v1; definition-sha256=e7075e233a6bd81aeb530ac780563692ab45ddeaf933896eab7fff53b5c54337; exit=0; EXPECT=matched; output-sha256=c55a9f6cae6c566f3c5d364807c069efd5b26def5ca463ed22cb36b581eb806d; output-bytes=1081; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=46559098bd72/39 entries

- [x] G8: skill-check tests pass, including the empty-root case
  CHECK: python3 .claude/skills/context-check/tests/skill_check_tests.py
  EXPECT: SKILL CHECK TESTS PASSED
  EVIDENCE: automatic-evidence=v1; definition-sha256=2c4d84e0ecb3b08e90d876200005d348f56af5f7bf32d9a5712a6b29551dfcfb; exit=0; EXPECT=matched; output-sha256=b66f436cb46bb0afaaecf6c8f3f012ddbd355c44490c3cb0d34664cf5f36d516; output-bytes=1521; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=46559098bd72/39 entries

- [x] G9: every docs/ and context/ folder on disk is measured in section D or named as excluded, and files loose at their roots are counted
  CHECK: python3 -c "import subprocess,re;o=subprocess.run(['/bin/bash','.claude/skills/context-check/context-check.sh'],capture_output=True,text=True).stdout;d=re.search(r'^D\. .*?(?=^E\. )',o,re.M|re.S).group(0);import os;subs=[f'{p}/{s}' for p in ('docs','context') for s in sorted(os.listdir(p)) if os.path.isdir(f'{p}/{s}')];miss=[s for s in subs if not re.search(r'^'+re.escape(s)+r'\s+\d',d,re.M)];print('unmeasured:',miss);print('D COVERS DOCS AND CONTEXT' if not miss and 'none' in d.split('add them')[1] and re.search(r'^context/ \(files at its root\)\s+2',d,re.M) else 'D HAS A HOLE')"
  EXPECT: D COVERS DOCS AND CONTEXT
  EVIDENCE: automatic-evidence=v1; definition-sha256=f898237977802e5cbe54a71532f1e21cab1eac5f8281f0cacc93a914ef38b415; exit=0; EXPECT=matched; output-sha256=2fd143baf0f7162ba1b9b3a13919b6314de55c5e4ca170fe43e91f7b1f70dfc0; output-bytes=41; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=46559098bd72/39 entries

- [x] G10: the skill file names the response owner for a finding and the two new planted failures
  CHECK: python3 -c "t=open('.claude/skills/context-check/SKILL.md').read();need=('Who responds','wrong root','helper crash','never counted as resolved');miss=[n for n in need if n not in t];print('missing:',miss);print('OWNER AND PROOF NAMED' if not miss else 'SKILL FILE SILENT')"
  EXPECT: OWNER AND PROOF NAMED
  EVIDENCE: automatic-evidence=v1; definition-sha256=1ed160c83b7bc58daf9fc9852a3333942e464ae3aa477488842876bc2e7cd5bc; exit=0; EXPECT=matched; output-sha256=e6c16cafe71eca1e9caa85669340c4580dc9d9be19df14431de9cd49feb82ceb; output-bytes=34; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=46559098bd72/39 entries

- [x] G11: the facts-sheet line still works on the real lab: skill-check --summary prints its one line with no ALERT
  CHECK: python3 .claude/skills/context-check/skill-check.py --summary
  EXPECT: /^skill check: \d+ skills and \d+ agent files checked; 0 files with 0 problems/
  EVIDENCE: automatic-evidence=v1; definition-sha256=deabefce356d7d0e0957ab6b8d4fd3983e43ff0952cc2a90b2165382d570a020; exit=0; EXPECT=matched; output-sha256=6fcb1c9c955de0086906e9e195cb8cc6547659ae41df10c9a0973c5ae3e7c38b; output-bytes=88; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=46559098bd72/39 entries

- [x] G12: this session changed only the files it owns; a row written by another live session is named with that session, not counted
  CHECK: python3 .unlazy/context-check-repair/owned-check.py
  EXPECT: ONLY OWNED FILES CHANGED
  EVIDENCE: automatic-evidence=v1; definition-sha256=995c1d6ab716d8d0226dfe0d1a6af3ad703c80b2ad15e94a03fbccd6af3cea98; exit=0; EXPECT=matched; output-sha256=3d3002d65920e95e117f6369eeb5881835310d26aad2862db6d5a060456fd70b; output-bytes=940; shell=/bin/sh; cwd=/Users/venkatgullapalli/Documents/my-ai-lab; path=46559098bd72/39 entries
