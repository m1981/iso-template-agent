"""Reproduce early RED seam and a controlled mutation on disposable copies.

Run from any directory. No source edits and no fixed temporary paths.
All outputs and assertions are saved under evidence/.
"""
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent.parent
EVIDENCE = ROOT / "evidence"


def run(case, change, selection, expected):
    with tempfile.TemporaryDirectory(prefix="process-simulator-tdd-") as folder:
        copy = Path(folder)
        for name in ("app", "lessons", "tests"):
            shutil.copytree(ROOT / name, copy / name, ignore=shutil.ignore_patterns("__pycache__"))
        engine = copy / "app" / "engine.py"
        engine.write_text(change(engine.read_text(encoding="utf-8")), encoding="utf-8")
        env = os.environ | {"PYTHONPATH": str(copy / "tests") + os.pathsep + str(copy)}
        command = [sys.executable, "-B", "-m", "unittest", "-v", *selection]
        result = subprocess.run(command, cwd=copy, env=env, capture_output=True, text=True)
        output = result.stdout + result.stderr
        # Evidence remains portable; the disposable copy's random name is not needed.
        output = output.replace(str(copy), "<disposable-copy>")
        log = f"Case: {case}\nCommand: python3 -B -m unittest -v {' '.join(selection)}\nExit: {result.returncode}\n\n{output}"
        (EVIDENCE / f"{case}.log").write_text(log, encoding="utf-8")
        if result.returncode != expected:
            raise SystemExit(f"Unexpected result for {case}: {result.returncode}\n{output}")
        if expected and "Refused not raised" not in output and "NotImplementedError" not in output:
            raise SystemExit(f"Failure was not the intended oracle: {case}\n{output}")
        print(f"{case}: expected exit {expected}; evidence/{case}.log")


def remove_review_guard(source):
    old = '"Zespół w fabule", ("V1",),'
    if source.count(old) != 1:
        raise SystemExit("Mutation target changed; review the experiment before applying it.")
    return source.replace(old, '"Zespół w fabule", (),')


run("reproduced-core-red", lambda _: '''class Refused(ValueError):
    pass

def initial_state():
    return ()

def transition(state, action, note=""):
    raise NotImplementedError("First RED: transitions do not exist yet")
''', ["test_engine.FirstSlice"], 1)
run("mutation-review-red", remove_review_guard,
    ["test_engine.FirstSlice.test_cannot_test_without_review"], 1)
run("mutation-review-green", lambda source: source,
    ["test_engine.FirstSlice.test_cannot_test_without_review"], 0)
