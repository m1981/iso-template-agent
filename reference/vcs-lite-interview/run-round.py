"""Run one read-only retrospective round against the specified Claude session."""
import argparse
import json
from pathlib import Path
import subprocess
import sys

BASE = Path(__file__).resolve().parent
SESSION = "e5a1e620-442a-4613-9606-6bffe6dfbe04"
PROJECT = Path("/Users/michal/PycharmProjects/byte-brewery/packages/vcs_lite")
CLAUDE = "/Users/michal/.local/bin/claude"


def public_events(value):
    """Keep response text and protocol metadata, omit internal reasoning blocks."""
    if isinstance(value, list):
        return [public_events(item) for item in value
                if not isinstance(item, dict) or item.get("type") not in {"thinking", "redacted_thinking"}]
    if isinstance(value, dict):
        return {key: public_events(item) for key, item in value.items()
                if key not in {"thinking", "reasoning_content"}}
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("round", type=int, choices=range(1, 6))
    number = parser.parse_args().round
    parts = [BASE.joinpath("contract.txt").read_text()]
    for prior in range(1, number):
        parts += ["POPRZEDNIE PYTANIE:", BASE.joinpath(f"round-{prior:02d}-prompt.txt").read_text(),
                  "POPRZEDNIA ODPOWIEDŹ:", BASE.joinpath(f"round-{prior:02d}-response.md").read_text()]
    parts += ["BIEŻĄCA RUNDA:", BASE.joinpath(f"round-{number:02d}-prompt.txt").read_text()]
    prompt = "\n\n".join(parts)
    BASE.joinpath(f"round-{number:02d}-input.txt").write_text(prompt)
    command = [CLAUDE, "--safe-mode", "--tools", "", "--strict-mcp-config",
               "--disable-slash-commands", "--permission-mode", "dontAsk",
               "--no-session-persistence", "--resume", SESSION, "--fork-session",
               "--output-format", "json", "--print"]
    with BASE.joinpath(f"round-{number:02d}-stderr.txt").open("w") as error:
        result = subprocess.run(command, input=prompt, text=True, cwd=PROJECT,
                                stdout=subprocess.PIPE, stderr=error)
    data = public_events(json.loads(result.stdout))
    BASE.joinpath(f"round-{number:02d}-raw.json").write_text(json.dumps(data, ensure_ascii=False, indent=2))
    print(f"round={number}, exit={result.returncode}", flush=True)
    if result.returncode:
        print(BASE.joinpath(f"round-{number:02d}-stderr.txt").read_text()[-2500:])
        sys.exit(result.returncode)
    if isinstance(data, list):
        data = next(item for item in reversed(data) if item.get("type") == "result")
    if data.get("is_error") or not isinstance(data.get("result"), str):
        print("No successful interview response; inspect raw result.")
        sys.exit(1)
    BASE.joinpath(f"round-{number:02d}-response.md").write_text(data["result"] + "\n")
    print(json.dumps({k: data.get(k) for k in ("session_id", "duration_ms", "num_turns", "is_error")}), flush=True)


if __name__ == "__main__":
    main()
