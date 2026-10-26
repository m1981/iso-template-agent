"""Render the three explanatory diagrams; no process checks or project mutations."""
from pathlib import Path
import subprocess


def main():
    folder = Path(__file__).resolve().parent
    for name in ("flow", "context", "controls"):
        for extension in ("svg", "png"):
            subprocess.run(
                ["dot", f"-T{extension}", str(folder / f"{name}.dot"),
                 "-o", str(folder / f"{name}.{extension}")], check=True
            )
        print(f"Rendered {name}.svg and {name}.png")


if __name__ == "__main__":
    main()
