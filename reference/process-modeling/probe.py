"""Read-only source audit and isolated replay for the criteria mapping.

This is a narrow diagnostic, not the model's regression suite or an acceptance.
Run with the existing iso-model-state Python environment; installs nothing.
"""

import argparse
from copy import deepcopy
from hashlib import sha256
import gzip
import json
from pathlib import Path
import shutil
import sys
from tempfile import TemporaryDirectory


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        parser.error("Output already exists; choose a new result file.")
    source = args.source.resolve()
    hashes = {}
    for relative in ("model/process.yaml", "PLAN.md", "docs/WLASCIWOSCI.md",
                     "docs/STAN.md", "docs/KARTA-CELU-I-ZAKRESU.md"):
        hashes[relative] = sha256((source / relative).read_bytes()).hexdigest()
    with TemporaryDirectory(prefix="process-mapping-") as temp:
        root = Path(temp)
        for relative in ("src/isomodel", "model", "tests/fixtures"):
            shutil.copytree(source / relative, root / relative,
                            ignore=shutil.ignore_patterns("__pycache__"))
        for path in sorted(root.rglob("*")):
            if path.is_file():
                hashes[path.relative_to(root).as_posix()] = sha256(path.read_bytes()).hexdigest()
        sys.path.insert(0, str(root / "src"))
        from isomodel.execution import replay
        from isomodel.loader import load_model

        model = load_model(root / "model/process.yaml")
        scenarios = {
            name: json.loads((root / f"tests/fixtures/{name}/scenario.json").read_text())
            for name in ("wit1", "wit2", "wit3", "wit4", "wit5")
        }
        expected_steps = {"wit1": 29, "wit2": 33, "wit3": 54, "wit4": 13, "wit5": 40}
        results = []

        def record(name, scenario, expected_outcome, expected_count=None, code=None):
            result = replay(model, scenario)
            last = result["steps"][-1]
            matches = result["outcome"] == expected_outcome
            if expected_count is not None:
                matches = matches and len(result["steps"]) == expected_count
            if code is not None:
                matches = matches and last.get("code") == code
            results.append({"case": name, "expected_outcome": expected_outcome,
                            "matches_expectation": matches, "result": result})

        for name, scenario in scenarios.items():
            record(name, scenario, "completed", expected_steps[name])

        wrong_actor = deepcopy(scenarios["wit1"])
        wrong_actor["events"][-1]["actor"] = "A"
        record("acceptance_by_author", wrong_actor, "rejected", code="actor")

        blocker = deepcopy(scenarios["wit1"])
        blocker["events"].insert(-1, {"transition": "P00", "actor": "R",
                                      "question": "late",
                                      "attributes": {"blocking": True}})
        record("late_blocking_question", blocker, "rejected", code="guard")

        changed_test_input = deepcopy(scenarios["wit1"])
        changed_test_input["events"][-1].setdefault("inputs", {})["tests_ok"] = False
        # W04 does not consume tests_ok. This records an abstraction boundary,
        # not a claim that acceptance of a real failed test is acceptable.
        record("tests_false_only_at_W04", changed_test_input, "completed", 29)

        report = {"simulation": True, "scope": "5 witnesses and 3 diagnostic probes",
                  "source_files_sha256": hashes, "results": results,
                  "all_expectations_matched": all(r["matches_expectation"] for r in results)}
        args.output.parent.mkdir(parents=True, exist_ok=True)
        payload = (json.dumps(report, ensure_ascii=False, indent=2) + "\n").encode()
        if args.output.suffix == ".gz":
            payload = gzip.compress(payload, mtime=0)
        args.output.write_bytes(payload)
        for row in results:
            print(row["case"], row["result"]["outcome"], len(row["result"]["steps"]),
                  "matches=" + str(row["matches_expectation"]))
        return 0 if report["all_expectations_matched"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
