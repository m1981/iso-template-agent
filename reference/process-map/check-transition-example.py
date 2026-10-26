"""Read-only diagnostic of an existing model, executed from a temporary copy.

Run using the existing iso-model-state Python environment; no installation.
Prints JSON to stdout. This is not an implementation of the proposed adapter.
"""

import argparse
from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import sys
import tempfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("model_repo", type=Path)
    args = parser.parse_args()
    source = args.model_repo.resolve()
    sys.dont_write_bytecode = True
    paths = sorted((source / "src/isomodel").rglob("*.py")) + [
        source / "model/process.yaml",
        source / "tests/fixtures/wit1/scenario.json",
    ]
    with tempfile.TemporaryDirectory(prefix="transition-review-") as folder:
        copy = Path(folder)
        fingerprints = {}
        for original in paths:
            relative = original.relative_to(source)
            target = copy / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(original, target)
            fingerprints[str(relative)] = hashlib.sha256(target.read_bytes()).hexdigest()
        sys.path.insert(0, str(copy / "src"))
        from isomodel import load_model
        from isomodel.execution import execute_step, initial_state, StepRejected

        model = load_model(copy / "model/process.yaml")
        scenario = json.loads((copy / "tests/fixtures/wit1/scenario.json").read_text())
        state = initial_state(model)
        prefix = []
        for event in scenario["events"]:
            if event["transition"] == "W02":
                break
            state = execute_step(model, state, event, scenario["inputs"])["after"]
            prefix.append(event["transition"])
        assert state["releases"][state["current_release"]]["state"] == "ready"
        cases = []

        def attempt(name, event, expected, inputs=None, setup=None):
            test_state = deepcopy(state)
            if setup:
                test_state = execute_step(model, test_state, setup, scenario["inputs"])["after"]
            before = deepcopy(test_state)
            test_inputs = scenario["inputs"] if inputs is None else inputs
            try:
                result = execute_step(model, test_state, event, test_inputs)
                release = result["after"]["releases"][test_state["current_release"]]
                observed = release["state"]
                extra = {"acceptance": release["acceptance"], "questions": result["after"]["questions"]}
            except StepRejected as error:
                observed = "rejected:" + error.code
                extra = {}
            assert test_state == before, name + ": input changed"
            assert observed == expected, (name, observed, expected)
            cases.append({"case": name, "event": event, "observed": observed,
                          "setup": setup, "inputs": test_inputs, "input_unchanged": True, **extra})

        attempt("W02 without report", {"transition": "W02", "actor": "R"}, "reviewed")
        attempt("W02 author role", {"transition": "W02", "actor": "A"}, "rejected:actor")
        attempt("W04 before W02", {"transition": "W04", "actor": "U"}, "rejected:state")
        attempt("W03 with finding", {"transition": "W03", "actor": "R", "findings": ["q1"]}, "in_preparation")
        attempt("W02 tests now false", {"transition": "W02", "actor": "R"}, "reviewed",
                scenario["inputs"] | {"tests_ok": False})
        for blocking in (True, False):
            attempt("W02 after new question blocking=" + str(blocking),
                    {"transition": "W02", "actor": "R"}, "reviewed",
                    setup={"transition": "P00", "actor": "A", "question": "q1",
                           "attributes": {"blocking": blocking}})
        print(json.dumps({"time_utc": datetime.now(timezone.utc).isoformat(),
                          "python": sys.version, "source_repo": str(source),
                          "source_sha256": fingerprints, "simulation": True,
                          "prefix": prefix, "cases": cases,
                          "limitation": "Diagnostic of copied model only; no adapter or actual release review."},
                         ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
