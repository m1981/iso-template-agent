"""Execute the planned release-cycle diagnostics on an isolated source copy.

No model repair, formal proof, real approval, or dependency installation.
"""
import argparse
from copy import deepcopy
import gzip
from hashlib import sha256
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
        parser.error("Choose a new output file; historical evidence is immutable.")
    with TemporaryDirectory(prefix="release-cycle-") as temp:
        root = Path(temp)
        for relative in ("src/isomodel", "model", "tests/fixtures"):
            shutil.copytree(args.source / relative, root / relative,
                            ignore=shutil.ignore_patterns("__pycache__"))
        hashes = {p.relative_to(root).as_posix(): sha256(p.read_bytes()).hexdigest()
                  for p in sorted(root.rglob("*")) if p.is_file()}
        sys.path.insert(0, str(root / "src"))
        from isomodel.execution import replay
        from isomodel.loader import load_model

        model = load_model(root / "model/process.yaml")
        fixtures = {name: json.loads((root / f"tests/fixtures/{name}/scenario.json").read_text())
                    for name in ("wit1", "wit3", "wit5")}
        base = fixtures["wit1"]
        wit3, wit5 = fixtures["wit3"], fixtures["wit5"]
        results = []

        def scenario(events, source=base):
            return dict(source, events=deepcopy(events))

        def run(name, data, outcome="completed", code=None, assertions=None, candidate=None):
            selected = candidate if candidate is not None else model
            before = deepcopy((selected, data))
            result = replay(selected, data)
            checks = {"outcome": result["outcome"] == outcome,
                      "inputs_unchanged": (selected, data) == before}
            if code:
                checks["reason"] = result["steps"][-1].get("code") == code
            if outcome != "completed":
                last = result["steps"][-1]
                checks["rejected_state_unchanged"] = last["before"] == last["after"]
            if assertions and checks["outcome"]:
                checks.update(assertions(result))
            results.append({"case": name, "expected_outcome": outcome,
                            "expected_code": code, "checks": checks,
                            "passed": all(checks.values()), "result": result,
                            "model_overrides": None if candidate is None else candidate})
            return result

        def current(state):
            return state["releases"][state["current_release"]]

        def two_releases(result):
            steps = result["steps"]
            if len(steps) != 40:
                return {"forty_steps": False}
            first = steps[28]["after"]["releases"][1]
            final = result["final_state"]
            opened = steps[33]["after"]
            return {
                "v1_immutable_every_step": all(s["after"]["releases"][1] == first for s in steps[29:]),
                "consent_not_change": steps[31]["after"]["next_release_required"] is False,
                "change_consumed_pending": steps[32]["after"]["next_release_required"] is True
                    and steps[32]["after"]["questions"]["q1"]["consumed"] is True,
                "new_release_fields": opened["current_release"] == 2 and not opened["next_release_required"]
                    and current(opened) == {"number": 2, "state": "in_preparation", "scope": first["scope"],
                                           "snapshot": None, "acceptance": None},
                "both_accepted": all(r["state"] == "accepted" for r in final["releases"].values()),
                "distinct_snapshots": first["snapshot"]["a2"]["version"] == 1
                    and final["releases"][2]["snapshot"]["a2"]["version"] == 2,
            }

        run("WIT5_full_history", wit5, assertions=two_releases)
        run("WIT3_replacement", wit3, assertions=lambda r: {
            "repaired_edges": r["final_state"]["items"]["a1"]["depends_on"] == ["r3"]
                and r["final_state"]["items"]["d1"]["depends_on"] == ["r3"],
            "both_ids_in_scope": {"r1", "r3"} <= set(current(r["final_state"])["scope"]),
            "accepted": current(r["final_state"])["state"] == "accepted",
        })

        w7_index = next(i for i, e in enumerate(wit3["events"]) if e["transition"] == "W07")
        legal = {
            "W01": (base["events"][:26], {"transition": "W01", "actor": "A"}, base),
            "W02": (base["events"][:27], {"transition": "W02", "actor": "R"}, base),
            "W03": (base["events"][:27], {"transition": "W03", "actor": "R", "findings": ["qf"]}, base),
            "W04": (base["events"][:28], base["events"][28], base),
            "W05": (base["events"][:28], {"transition": "W05", "actor": "U", "question": "qf"}, base),
            "W06": (wit5["events"][:33], wit5["events"][33], wit5),
            "W07": (wit3["events"][:w7_index], wit3["events"][w7_index], wit3),
        }

        def frame(ident):
            def check(result):
                last = result["steps"][-1]
                pre, post = last["before"], last["after"]
                expected = deepcopy(pre)
                rel = current(expected)
                if ident in {"W01", "W02"}:
                    rel["state"] = {"W01": "ready", "W02": "reviewed"}[ident]
                elif ident in {"W03", "W05"}:
                    rel["state"] = "in_preparation"
                    expected["questions"] = deepcopy(post["questions"])
                elif ident == "W04":
                    rel["state"] = "accepted"
                    fields = ("type", "depends_on", "state", "predecessor", "version", "rejections", "suspect")
                    rel["snapshot"] = {item: {key: deepcopy(pre["items"][item][key]) for key in fields}
                                       for item in rel["scope"]}
                    rel["acceptance"] = {"number": pre["current_release"],
                                         "quote": last["event"]["evidence"]["quote"]}
                elif ident == "W06":
                    number = pre["current_release"] + 1
                    expected["releases"][number] = dict(number=number, state="in_preparation",
                        scope=deepcopy(current(pre)["scope"]), snapshot=None, acceptance=None)
                    expected["current_release"] = number
                    expected["next_release_required"] = False
                else:
                    rel["scope"] = sorted(set(rel["scope"]) | {last["event"]["item"]})
                checks = {"frame": post == expected}
                if ident in {"W03", "W05"}:
                    q = post["questions"].get("qf", {})
                    checks["new_blocker"] = set(post["questions"]) == set(pre["questions"]) | {"qf"}
                    checks["question_semantics"] = all(q.get(k) == v for k, v in
                        {"state": "open", "kind": "general", "blocking": True, "age": 1}.items())
                return checks
            return check

        for ident, (prefix, event, source) in legal.items():
            run(ident + "_legal", scenario(prefix + [event], source), assertions=frame(ident))
            wrong = dict(event, actor="U" if event["actor"] != "U" else "A")
            run(ident + "_wrong_actor", scenario(prefix + [wrong], source), "rejected", "actor")

        ready = base["events"][:27]
        reviewed = base["events"][:28]
        blocker = {"transition": "P00", "actor": "R", "question": "qf", "attributes": {"blocking": True}}
        accept = base["events"][28]
        run("W01_false_tests", scenario(base["events"][:26] + [dict(legal["W01"][1], inputs={"tests_ok": False})]), "rejected", "guard")
        run("W01_blocker", scenario(base["events"][:26] + [blocker, legal["W01"][1]]), "rejected", "guard")
        run("W04_no_review", scenario(ready + [accept]), "rejected", "state")
        run("W04_no_quote", scenario(reviewed + [{"transition": "W04", "actor": "U"}]), "rejected", "evidence")
        blocked_acceptance = scenario(reviewed + [blocker, accept])
        run("W04_late_blocker", blocked_acceptance, "rejected", "guard")
        run("W06_no_change", scenario(base["events"] + [legal["W06"][1]]), "rejected", "guard")
        run("W06_cannot_skip", scenario(wit5["events"][:33] + [wit5["events"][34]], wit5), "rejected", "pending_release")
        limited = deepcopy(model)
        limited["test_instance"]["bounds"]["max_releases"] = 1
        run("W06_boundary", scenario(wit5["events"][:34], wit5), "error", "boundary", candidate=limited)
        run("W07_uncreated_successor", scenario([legal["W07"][1]], wit3), "rejected", "guard")
        run("W03_invalid_findings", scenario(ready + [{"transition": "W03", "actor": "R", "findings": ["qf", "qf"]}]), "error", "input")
        run("W03_empty_findings", scenario(ready + [{"transition": "W03", "actor": "R", "findings": []}]), assertions=lambda r: {
            "no_questions": r["final_state"]["questions"] == {},
            "preparation": current(r["final_state"])["state"] == "in_preparation"})

        resolution = [
            {"transition": "P01", "actor": "A", "question": "qf"},
            {"transition": "P02", "actor": "U", "question": "qf", "inputs": {"unambiguous_answer": True},
             "evidence": {"simulation": True, "decision": "SIM-DEC", "quote": "Demonstracyjna odpowiedź, nie rzeczywista zgoda."}},
            legal["W01"][1], legal["W02"][1], accept]
        for ident in ("W03", "W05"):
            prefix, event, source = legal[ident]
            run(ident + "_blocks_readiness", scenario(prefix + [event, legal["W01"][1]]), "rejected", "guard")
            run(ident + "_return_to_acceptance", scenario(prefix + [event] + resolution), assertions=lambda r: {
                "resolved": r["final_state"]["questions"]["qf"]["state"] == "resolved",
                "accepted": current(r["final_state"])["state"] == "accepted"})

        def modified(ident):
            candidate = deepcopy(model)
            return candidate, next(t for t in candidate["release_transitions"] if t["id"] == ident)

        candidate, transition = modified("W04")
        transition["from"] = ["ready", "reviewed"]
        run("M01_skip_review", scenario(ready + [accept]), candidate=candidate, assertions=lambda r: {
            "bad_acceptance_executed": current(r["final_state"])["state"] == "accepted"
                and r["steps"][-1]["before"]["releases"][1]["state"] == "ready"})
        candidate, transition = modified("W04")
        transition["guard"] = "true"
        run("M02_ignore_blocker", blocked_acceptance, candidate=candidate, assertions=lambda r: {
            "bad_acceptance_executed": current(r["final_state"])["state"] == "accepted"
                and r["final_state"]["questions"]["qf"]["state"] == "open"})
        candidate, transition = modified("W06")
        transition["effects"].insert(2, "release.state := in_preparation")
        run("M03_rewrite_old_state", scenario(wit5["events"][:34], wit5), candidate=candidate, assertions=lambda r: {
            "old_acceptance_changed": r["steps"][-1]["before"]["releases"][1] != r["final_state"]["releases"][1],
            "new_release_created": r["final_state"]["current_release"] == 2})

        candidate, transition = modified("W04")
        transition["effects"][0] = "release.snapshot := snapshot({})"
        run("M04_empty_snapshot", scenario(reviewed + [accept]), candidate=candidate, assertions=lambda r: {
            "snapshot_oracle_detects": not frame("W04")(r)["frame"],
            "empty_snapshot_executed": current(r["final_state"])["snapshot"] == {}})
        candidate, transition = modified("W04")
        transition["effects"].append("release.acceptance := {number: 99}")
        run("M05_wrong_acceptance", scenario(reviewed + [accept]), candidate=candidate, assertions=lambda r: {
            "acceptance_oracle_detects": not frame("W04")(r)["frame"],
            "wrong_number_executed": current(r["final_state"])["acceptance"]["number"] == 99})

        report = {"simulation": True, "source_files_sha256": hashes, "results": results,
                  "passed": all(r["passed"] for r in results)}
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_bytes(gzip.compress((json.dumps(report, ensure_ascii=False, indent=2) + "\n").encode(), mtime=0))
        for result in results:
            failed = [k for k, v in result["checks"].items() if not v]
            print(result["case"], "OK" if result["passed"] else "FAIL", ",".join(failed))
        print(f"{sum(r['passed'] for r in results)}/{len(results)} expectations matched")
        return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
