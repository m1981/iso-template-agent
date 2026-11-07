#!/usr/bin/env python3
"""F5 compiling RED replay / focused persistence faults on disposable copies only."""
import argparse
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('copy_support',ROOT/'verify-mutations.py')
support=importlib.util.module_from_spec(spec); spec.loader.exec_module(support)
ENGINE='src/main/java/org/example/processlab/engine/EngineSession.java'
TRIAL='src/main/java/org/example/processlab/workflow/ChangeTrial.java'
FAULTS=[
    ('memory-instead-of-file',ENGINE,'"jdbc:h2:file:"+path+(create ? "" : ";IFEXISTS=TRUE")',
     '"jdbc:h2:mem:persistence_fault;DB_CLOSE_DELAY=0"','F5_01_to_03_and_05_resumeInNewJvmsAndPreserveAcceptedHistory'),
    ('schema-upgrade-on-reopen',ENGINE,'createSchema ? ProcessEngineConfiguration.DB_SCHEMA_UPDATE_TRUE : ProcessEngineConfiguration.DB_SCHEMA_UPDATE_FALSE',
     'ProcessEngineConfiguration.DB_SCHEMA_UPDATE_TRUE','F5_04_emptyModelStoreIsNotInitializedOnReopen'),
    ('ignore-model-content',TRIAL,'!Arrays.equals(stored.readAllBytes(),current.readAllBytes())',
     'false','F5_04_changedXmlIsRefusedForBothEngines'),
    ('choose-first-definition',TRIAL,'processDefinitions.size()!=1 || decisionDefinitions.size()!=1\n                    || repository.createDeploymentQuery().count()!=1 || decisions.createDeploymentQuery().count()!=1',
     'processDefinitions.isEmpty() || decisionDefinitions.isEmpty()','F5_04_duplicateDefinitionsAreRefusedForBothEngines'),
]

def main():
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument('--red',action='store_true'); args=parser.parse_args()
    cases=[('red-replay',None,None,None,None)] if args.red else FAULTS
    results=[]
    for name,file,before,after,test in cases:
        with tempfile.TemporaryDirectory(prefix='flowable-f5-') as temp:
            directory=Path(temp); support.copy_trial(directory)
            if args.red:
                sources=json.loads((ROOT/'evidence/f5-red-sources.json').read_text())
                # Added boundary tests call openFile, absent from initial RED. Compatible stub only.
                sources[ENGINE]=sources[ENGINE].replace('    public ProcessEngine processes()',
                    '    public static EngineSession openFile(java.nio.file.Path p, boolean c, java.util.Map<String,Object> b) { return openInMemory("red_file_stub",b); }\n    public ProcessEngine processes()')
                for source,content in sources.items():
                    if source not in (ENGINE,TRIAL): raise ValueError('Unexpected source path')
                    (directory/source).write_text(content)
            else:
                path=directory/file; source=path.read_text()
                if source.count(before)!=1: raise ValueError('Expected one fault anchor: '+name)
                path.write_text(source.replace(before,after,1))
            log=ROOT/'evidence'/('f5-'+name+'.log')
            with log.open('w') as output:
                result=subprocess.run(['./verify','-o','-Dtest=PersistentTrialTest'+('#'+test if test else ''),'clean','test'],
                    cwd=directory,stdout=output,stderr=subprocess.STDOUT,timeout=180)
            totals=dict(tests=0,failures=0,errors=0,skipped=0); failed=[]
            for report in (directory/'target/surefire-reports').glob('TEST-*.xml'):
                root=ET.parse(report).getroot()
                for key in totals: totals[key]+=int(root.attrib[key])
                failed.extend(c.attrib['name'] for c in root.findall('testcase') if c.find('failure') is not None)
            semantic=result.returncode!=0 and totals['failures']>0 and totals['errors']==0 and totals['skipped']==0
            record=dict(case=name,exit_code=result.returncode,**totals,failed_tests=failed,semantic_failure=semantic,log=log.name)
            results.append(record); print(json.dumps(record),flush=True)
    (ROOT/'evidence'/('f5-red-replay.json' if args.red else 'f5-faults.json')).write_text(json.dumps(results,indent=2)+'\n')
    return 0 if all(r['semantic_failure'] for r in results) else 1

if __name__=='__main__': raise SystemExit(main())
