#!/usr/bin/env python3
"""Run bounded TLC checks. No downloads, product execution, or implicit approval."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import time

ROOT = Path(__file__).resolve().parent
JAR_SHA256 = '936a262061c914694dfd669a543be24573c45d5aa0ff20a8b96b23d01e050e88'
INVARIANTS = ['V1_TypedAndBound', 'V2_HistoryPreserved', 'V3_SingleCompletion',
              'V4_ReplayStable', 'V5_GuardedWrite', 'V6_NoFalseCredit',
              'V7_NoFalseInvalidation', 'V8_NoHiddenFinding']


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def classify(returncode, output, expected):
    """An expected semantic counterexample is different from arbitrary failure."""
    violation = re.search(r'Invariant (\w+) is violated', output)
    if expected:
        ok = returncode == 12 and violation is not None and violation[1] == expected
        ok = ok and 'The behavior up to this point is:' in output
        return 'expected_counterexample' if ok else 'unexpected_result'
    ok = returncode == 0 and 'Model checking completed. No error has been found.' in output
    return 'bounded_pass' if ok and not violation else 'unexpected_result'


def configuration(case):
    checks = case.get('checks', INVARIANTS)
    if case['kind'] == 'witness':
        checks = checks + ['NotGoal']
    return '\n'.join([
        'CONSTANTS', ' Empty = Empty', f' Scenario = "{case["scenario"]}"',
        f' Mutation = "{case.get("mutation", "none")}"',
        f' MaxDepth = {case["depth"]}', 'INIT Init', 'NEXT Next',
        'CONSTRAINT WithinHorizon', 'CHECK_DEADLOCK FALSE',
        *('INVARIANT ' + check for check in checks), ''])


def run_case(case, args, out):
    cfg = configuration(case)
    expected = 'NotGoal' if case['kind'] == 'witness' else case.get('expected')
    with tempfile.TemporaryDirectory(prefix='p3-tlc-') as temporary:
        scratch = Path(temporary)
        shutil.copy2(ROOT / 'P3.tla', scratch / 'P3.tla')
        (scratch / 'P3.cfg').write_text(cfg)
        cmd = [str(args.java), '-Xmx512m', '-XX:+UseParallelGC', '-cp', str(args.jar),
               'tlc2.TLC', '-workers', '1', '-seed', '1', '-fp', '0',
               '-config', 'P3.cfg', 'P3.tla']
        started = time.monotonic()
        try:
            process = subprocess.run(cmd, cwd=scratch, capture_output=True, text=True, timeout=60)
            output = process.stdout + process.stderr
            status = classify(process.returncode, output, expected)
            returncode = process.returncode
        except subprocess.TimeoutExpired as error:
            output = (error.stdout or b'').decode(errors='replace') if isinstance(error.stdout, bytes) else (error.stdout or '')
            output += '\nRUNNER: TIMEOUT 60 s; inconclusive.\n'
            status, returncode = 'timeout', None
        seconds = round(time.monotonic() - started, 3)
    with (out / 'runs.jsonl').open('a') as stream:
        stream.write(json.dumps({'case': case['name'], 'config': cfg, 'output': output}, ensure_ascii=False) + '\n')
    stats = re.findall(r'([\d,]+) states generated, ([\d,]+) distinct states found, ([\d,]+) states left on queue', output)
    return dict(case, status=status, expected_invariant=expected, returncode=returncode,
                seconds=seconds, states=stats[-1] if stats else None,
                command=cmd, log='runs.jsonl', record=case['name'])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--java', type=Path, default=ROOT.parent / 'flowable-trial/.tooling/jdk-17.0.21+9/Contents/Home/bin/java')
    parser.add_argument('--jar', type=Path, default=ROOT.parents[2].parent / 'iso-model-state/artifacts/tools/tla/1.7.4/tla2tools.jar')
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--only', help='comma-separated case names')
    args = parser.parse_args()
    args.java, args.jar = args.java.resolve(), args.jar.resolve()
    if not args.java.is_file() or not os.access(args.java, os.X_OK):
        parser.error('Provide an existing Java runtime using --java; no automatic installation.')
    if not args.jar.is_file() or sha256(args.jar) != JAR_SHA256:
        parser.error('Provide TLC 1.7.4 matching the pinned SHA-256 using --jar.')
    cases = json.loads((ROOT / 'cases.json').read_text())
    if args.only:
        names = set(args.only.split(','))
        if not names <= {c['name'] for c in cases}:
            parser.error('Unknown case name')
        cases = [c for c in cases if c['name'] in names]
    out = args.output.resolve()
    out.mkdir(parents=True, exist_ok=False)
    for name in ['P3.tla', 'check.py', 'cases.json']:
        shutil.copy2(ROOT / name, out / name)
    report = {'scope': 'bounded P3 abstraction; no liveness, identity or database proof',
              'sources': {name: sha256(ROOT / name) for name in ['P3.tla', 'check.py', 'cases.json']},
              'toolchain': {'jar_sha256': sha256(args.jar),
                            'java': subprocess.run([str(args.java), '-version'], capture_output=True, text=True, check=True).stderr.strip()},
              'results': []}
    for case in cases:
        result = run_case(case, args, out)
        report['results'].append(result)
        (out / 'summary.json').write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n')
        print(f'{case["name"]}: {result["status"]} ({result["seconds"]} s)', flush=True)
    return 0 if all(r['status'] in {'bounded_pass', 'expected_counterexample'} for r in report['results']) else 1


if __name__ == '__main__':
    raise SystemExit(main())
