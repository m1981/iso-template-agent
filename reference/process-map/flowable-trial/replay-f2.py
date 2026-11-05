#!/usr/bin/env python3
"""Reconstruct complete F2 sources from the preserved patch, without touching F4."""
import importlib.util
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('support',ROOT/'verify-mutations.py')
support=importlib.util.module_from_spec(spec)
spec.loader.exec_module(support)
patch=(ROOT/'evidence/f2-implementation.patch').read_text()
files=[]
for chunk in re.split(r'(?m)^--- ',patch)[1:]:
    lines=chunk.splitlines()
    target=lines[1].removeprefix('+++ b/')
    if not target.startswith('src/main/java/') or '..' in Path(target).parts:
        raise ValueError('Unexpected patch path')
    hunk=re.fullmatch(r'@@ -(\d+),(\d+) \+(\d+),(\d+) @@',lines[2])
    if hunk is None or int(hunk[1]) not in (0,1) or int(hunk[3])!=1:
        raise ValueError('Expected a complete-file patch')
    red=[line[1:] for line in lines[3:] if line.startswith((' ','-'))]
    green=[line[1:] for line in lines[3:] if line.startswith((' ','+'))]
    if len(red)!=int(hunk[2]) or len(green)!=int(hunk[4]):
        raise ValueError('Patch does not contain complete sources')
    files.append((target,red,green))
results=[]
for index,name in ((1,'red'),(2,'green')):
    with tempfile.TemporaryDirectory(prefix='flowable-f2-') as temporary:
        directory=Path(temporary)
        support.copy_trial(directory)
        shutil.rmtree(directory/'src')  # Only the newly created disposable copy.
        for item in files:
            if item[index]:
                target=directory/item[0]; target.parent.mkdir(parents=True,exist_ok=True)
                target.write_text('\n'.join(item[index])+'\n')
        tests=directory/'src/test/java/org/example/processlab'; tests.mkdir(parents=True)
        for test in ('DomainModelTest.java','EngineSessionTest.java'):
            shutil.copy2(ROOT/'src/test/java/org/example/processlab'/test,tests/test)
        shutil.copytree(ROOT/'src/test/resources',directory/'src/test/resources')
        log=ROOT/'evidence'/('f2-compat-'+name+'.log')
        with log.open('w') as output:
            process=subprocess.run(['./verify','-o','clean','verify'],cwd=directory,stdout=output,stderr=subprocess.STDOUT,timeout=120)
        counts=dict(tests=0,failures=0,errors=0,skipped=0)
        for report in (directory/'target/surefire-reports').glob('TEST-*.xml'):
            attrs=ET.parse(report).getroot().attrib
            for key in counts: counts[key]+=int(attrs[key])
        result=dict(stage=name,exit_code=process.returncode,**counts,log=log.name)
        results.append(result); print(json.dumps(result),flush=True)
(ROOT/'evidence/f2-compat-replay.json').write_text(json.dumps(results,indent=2)+'\n')
expected=[(5,4,0,0),(5,0,0,0)]
valid=all(tuple(r[k] for k in ('tests','failures','errors','skipped'))==e for r,e in zip(results,expected))
raise SystemExit(0 if valid and results[0]['exit_code']!=0 and results[1]['exit_code']==0 else 1)
