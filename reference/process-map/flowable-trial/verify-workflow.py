#!/usr/bin/env python3
"""F4 RED replay or selected faults, exclusively on disposable copies."""
import argparse
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('f3_runner',ROOT/'verify-mutations.py')
copy_support=importlib.util.module_from_spec(spec)
spec.loader.exec_module(copy_support)
FACADE='src/main/java/org/example/processlab/workflow/ChangeProcess.java'
ENGINE='src/main/java/org/example/processlab/engine/EngineSession.java'
BPMN='src/main/resources/change.bpmn20.xml'
FAULTS=[
 ('role',FACADE,'require(command.role()==role,','require(true,'),
 ('version',FACADE,'require(before.version()==command.expectedVersion(),','require(true,'),
 ('command-id',FACADE,'require(before.receipts().stream().noneMatch(r->r.commandId().equals(command.id())),','require(true,'),
 ('process-id',FACADE,'.taskId(command.taskId()).processInstanceId(command.processId())','.taskId(command.taskId())'),
 ('task-id',FACADE,'.taskId(command.taskId()).processInstanceId(command.processId())','.processInstanceId(command.processId())'),
 ('authorization-step',BPMN,'sourceRef="start" targetRef="authorize"','sourceRef="start" targetRef="impact"'),
 ('permission-reset',FACADE,'proposal=propose.requirement(); authorized=false; action="PROPOSE";',
  'proposal=propose.requirement(); action="PROPOSE";'),
 ('correction-routing',BPMN,'sourceRef="after_qualify" targetRef="prepare"','sourceRef="after_qualify" targetRef="accept"'),
 ('partial-write',FACADE,'        engine.getTaskService().complete(command.taskId(),',
  '        engine.getRuntimeService().setVariable(command.processId(),STATE,StateCodec.encode(next));\n        engine.getTaskService().complete(command.taskId(),'),
 ('dmn-history',ENGINE,'dmnConfiguration.setHistoryEnabled(true);','dmnConfiguration.setHistoryEnabled(false);'),
 ('future-review',FACADE,'require(known.contains(review.subject()) && known.containsAll(review.basis()),','require(true,'),
 ('future-run',FACADE,'require(known.contains(run.testCase()) && known.contains(run.software()),','require(true,'),
]

def run_case(name,directory):
    log=ROOT/'evidence'/('f4-'+name+'.log')
    with log.open('w') as output:
        result=subprocess.run(['./verify','-o','-Dtest=ChangeProcessTest','clean','test'],cwd=directory,
                              stdout=output,stderr=subprocess.STDOUT,timeout=120)
    totals=dict(tests=0,failures=0,errors=0,skipped=0)
    failed=[]
    for report in (directory/'target/surefire-reports').glob('TEST-*.xml'):
        root=ET.parse(report).getroot()
        for key in totals: totals[key]+=int(root.attrib[key])
        failed.extend(case.attrib['name'] for case in root.findall('testcase') if case.find('failure') is not None)
    semantic=result.returncode!=0 and totals['tests']>0 and totals['failures']>0 and totals['errors']==0 and totals['skipped']==0
    return dict(case=name,exit_code=result.returncode,**totals,failed_tests=failed,semantic_failure=semantic,log=log.name)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--red',action='store_true')
    args=parser.parse_args()
    cases=[('red-replay',None,None,None)] if args.red else FAULTS
    results=[]
    for name,file,before,after in cases:
        with tempfile.TemporaryDirectory(prefix='flowable-f4-') as temporary:
            directory=Path(temporary); copy_support.copy_trial(directory)
            if args.red:
                # Historical F4 API predates persistence; exclude only F5 tests on this disposable copy.
                for test in ('PersistentTrialTest.java', 'RestartWorker.java', 'DemoCommand.java'):
                    (directory/'src/test/java/org/example/processlab'/test).unlink(missing_ok=True)
                for name_in_source,source in json.loads((ROOT/'evidence/f4-red-sources.json').read_text()).items():
                    path=Path(name_in_source)
                    if path.is_absolute() or '..' in path.parts or not name_in_source.startswith('src/main/'):
                        raise ValueError('Unsafe replay path')
                    (directory/path).write_text(source)
            else:
                path=directory/file; source=path.read_text()
                if source.count(before)!=1: raise ValueError('Expected one fault anchor: '+name)
                path.write_text(source.replace(before,after,1))
            result=run_case(name,directory); results.append(result); print(json.dumps(result),flush=True)
    (ROOT/'evidence'/('f4-red-replay.json' if args.red else 'f4-faults.json')).write_text(json.dumps(results,indent=2)+'\n')
    return 0 if all(r['semantic_failure'] for r in results) else 1


if __name__=='__main__': raise SystemExit(main())
