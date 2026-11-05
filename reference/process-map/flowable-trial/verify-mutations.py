#!/usr/bin/env python3
"""Re-run semantic faults on disposable copies; never mutate working sources.

Uses only Python's standard library. Requires the local JDK/Maven cache prepared
for ./verify. No network, packages, production workflow, or acceptance decisions.
"""
import argparse
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent
RULES = 'src/main/java/org/example/processlab/rules/Rules.java'
SNAPSHOT = 'src/main/java/org/example/processlab/rules/ProjectSnapshot.java'
DMN = 'src/main/resources/qualification.dmn'
QUALIFIER = 'src/main/java/org/example/processlab/engine/DmnQualifier.java'
MUTATIONS = [
    ('R6-allow-unknown-parent-fallback', QUALIFIER,
     'if (definitions.size() != 1) throw new IllegalStateException("Expected one definition in the requested deployment");',
     'if (definitions.isEmpty()) return repository.createDecisionQuery().decisionKey("qualification").latestVersion().singleResult();\n        if (definitions.size() != 1) throw new IllegalStateException("Expected one definition in the requested deployment");'),
    ('R1-duplicate-revision', SNAPSHOT,
     'if (!refs.add(artifact.ref()))', 'if (false)'),
    ('R2-append-discarded', SNAPSHOT,
     'return new ProjectSnapshot(artifacts, current, dependencies, next, runs);', 'return this;'),
    ('R3-no-transitive-traversal', RULES,
     'queue.add(dependent);', '// traversal deliberately disabled'),
    ('R4-ignore-review-basis', RULES,
     'review.subject().equals(subject) && new HashSet<>(review.basis()).equals(basis)',
     'review.subject().equals(subject)'),
    ('R4-ignore-stale-edge', RULES,
     'if (stale) return REVIEW_REQUIRED;', '// stale edge deliberately ignored'),
    ('R5-ignore-software-revision', RULES,
     'run.testCase().equals(test) && run.software().equals(software)', 'run.testCase().equals(test)'),
    ('R5-ignore-execution-error', RULES,
     'if (outcomes.contains(TestRunRecord.Outcome.ERROR)) return UNKNOWN;', '// ERROR deliberately ignored'),
    ('R6-empty-scope-ready', RULES,
     '!known.isEmpty() && !known.contains(UNKNOWN)', '!known.contains(UNKNOWN)'),
    ('R6-dmn-missing-basis-ready', DMN,
     "'MISSING_BASIS'", "'TO_OPERATOR'"),
    ('R6-dmn-conflict-ready', DMN,
     '<outputEntry id="r1o"><text>\'REVIEW_REQUIRED\'</text>',
     '<outputEntry id="r1o"><text>\'TO_OPERATOR\'</text>'),
    ('R6-dmn-failure-ready', DMN,
     "'CORRECTION'", "'TO_OPERATOR'"),
    ('R6-dmn-pending-ready', DMN,
     '<outputEntry id="r3o"><text>\'REVIEW_REQUIRED\'</text>',
     '<outputEntry id="r3o"><text>\'TO_OPERATOR\'</text>'),
    ('R6-dmn-ready-blocked', DMN,
     "'TO_OPERATOR'", "'CORRECTION'"),
]


def copy_trial(destination):
    for name in ('src', '.mvn'):
        shutil.copytree(ROOT / name, destination / name)
    for name in ('pom.xml', 'verify', 'mvnw'):
        shutil.copy2(ROOT / name, destination / name)
    (destination / '.tooling').symlink_to(ROOT / '.tooling', target_is_directory=True)


def execute(case, destination):
    log = ROOT / 'evidence' / ('f3-' + case + '.log')
    with log.open('w') as output:
        process = subprocess.run(['./verify', '-o', '-Dtest=DomainModelTest,EngineSessionTest,RulesTest,DmnQualifierTest', 'clean', 'test'], cwd=destination,
                                 stdout=output, stderr=subprocess.STDOUT, timeout=120)
    totals = dict(tests=0, failures=0, errors=0, skipped=0)
    reports = sorted((destination / 'target/surefire-reports').glob('TEST-*.xml'))
    for report in reports:
        tree = ET.parse(report).getroot()
        for key in totals:
            totals[key] += int(tree.attrib[key])
    killed = process.returncode != 0 and totals['failures'] > 0 and totals['errors'] == 0
    return dict(case=case, exit_code=process.returncode, **totals,
                semantic_failure=killed, log=log.name)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--red', action='store_true', help='Replay saved compiling stubs against current tests')
    args = parser.parse_args()
    results = []
    variants = [('red-replay', None, None, None)] if args.red else MUTATIONS
    for case, source, before, after in variants:
        with tempfile.TemporaryDirectory(prefix='flowable-f3-') as temp:
            target = Path(temp)
            copy_trial(target)
            if args.red:
                originals = json.loads((ROOT / 'evidence/f3-red-sources.json').read_text())
                for name, text in originals.items():
                    path = Path(name)
                    if path.is_absolute() or '..' in path.parts or not name.startswith('src/main/java/'):
                        raise ValueError('Unsafe replay path: ' + name)
                    (target / path).write_text(text)
            else:
                path = target / source
                text = path.read_text()
                if text.count(before) != 1:
                    raise ValueError('Mutation anchor must occur exactly once: ' + case)
                path.write_text(text.replace(before, after, 1))
            result = execute(case, target)
            results.append(result)
            print(json.dumps(result), flush=True)
    summary = ROOT / 'evidence' / ('f3-red-replay.json' if args.red else 'f3-mutations.json')
    summary.write_text(json.dumps(results, indent=2) + '\n')
    return 0 if all(r['semantic_failure'] for r in results) else 1


if __name__ == '__main__':
    raise SystemExit(main())
