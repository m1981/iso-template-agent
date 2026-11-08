#!/usr/bin/env python3
"""Replay existing suites on Git snapshots; no installation or source-repo writes.

Usage: /usr/bin/python3 reproduce.py [output-directory]
Requires existing trial .tooling and sibling iso-model-state/.venv.
Writes logs to output-directory, build/test scratch to a new temporary directory.
"""
from concurrent.futures import ThreadPoolExecutor
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET

TRIAL = Path(__file__).resolve().parents[2]
REPO = TRIAL.parents[2]
PYTHON_REPO = REPO.parent / 'iso-model-state'
JAVA_REV = '6845f799a57cdb2269879995c0b7bb92be9434fa'
PYTHON_REV = 'f74f55f2ea68d30fca22b4ddf7c9d05eb9ad82cb'
OUTPUT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parent
OUTPUT.mkdir(parents=True, exist_ok=True)
SCRATCH = Path(tempfile.mkdtemp(prefix='iso-a17-'))


def snapshot(source, revision, destination):
    destination.mkdir()
    data = subprocess.check_output(['git', '-C', str(source), 'archive', revision])
    subprocess.run(['tar', '-xf', '-', '-C', str(destination)], input=data, check=True)


snapshot(REPO, JAVA_REV, SCRATCH / 'java')
snapshot(PYTHON_REPO, PYTHON_REV, SCRATCH / 'python')
java = SCRATCH / 'java' / TRIAL.relative_to(REPO)
tooling = java / '.tooling'
tooling.mkdir()
for name in ('maven-user', 'repository'):
    shutil.copytree(TRIAL / '.tooling' / name, tooling / name)
# The JDK is only executed/read; Maven caches and all builds are private copies.
(tooling / 'jdk-17.0.21+9').symlink_to(TRIAL / '.tooling/jdk-17.0.21+9', target_is_directory=True)


def run(name, command, cwd, env):
    with (OUTPUT / (name + '.log')).open('w') as log:
        log.write('Command: ' + ' '.join(command) + '\n')
        log.flush()
        result = subprocess.run(command, cwd=cwd, env=env, stdout=log,
                                stderr=subprocess.STDOUT, timeout=300)
    # Normalize only trailing whitespace for Git; retain every output line.
    path = OUTPUT / (name + '.log')
    path.write_text('\n'.join(line.rstrip(' \t') for line in path.read_text().splitlines()) + '\n')
    print(name + ': exit=' + str(result.returncode), flush=True)
    return result.returncode


env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
py = str(PYTHON_REPO / '.venv/bin/python')
with ThreadPoolExecutor(max_workers=2) as pool:
    jobs = {
        'flowable': pool.submit(run, 'flowable', ['./verify', '-o', 'verify'], java, env),
        'python': pool.submit(run, 'python', [py, '-m', 'pytest', '-q',
            'tests/test_py01_rules.py', 'tests/test_py01_store.py',
            'tests/test_py01_cli.py', 'tests/test_py01_sensitivity.py',
            '--junitxml=' + str(OUTPUT / 'python-junit.xml')], SCRATCH / 'python', env),
    }
    exits = {name: job.result() for name, job in jobs.items()}

suites = []
for path in sorted((java / 'target/surefire-reports').glob('TEST-*.xml')):
    root = ET.parse(path).getroot()
    suites.append({key: root.get(key) for key in ('name', 'tests', 'failures', 'errors', 'skipped')})
    shutil.copyfile(path.with_name(path.name[5:-4] + '.txt'), OUTPUT / (path.stem[5:] + '.txt'))
summary = dict(java_revision=JAVA_REV, python_revision=PYTHON_REV, exit_codes=exits,
               flowable_suites=suites,
               python_suites=[dict(node.attrib) for node in ET.parse(OUTPUT / 'python-junit.xml').getroot()],
               python_version=subprocess.check_output([py, '--version'], text=True).strip(),
               scratch=str(SCRATCH),
               limits='Existing suites only; no TLC, new scenario, product change, benchmark or user acceptance.')
(OUTPUT / 'summary.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(summary, ensure_ascii=False, indent=2))
sys.exit(0 if all(code == 0 for code in exits.values()) else 1)
