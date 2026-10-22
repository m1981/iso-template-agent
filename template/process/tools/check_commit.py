"""Hook commit-msg: opis commita musi wskazać co najmniej jedno istniejące ID (P-07).

Dzięki temu każda zmiana ma przyczynę w modelu śladu (decyzja, wymaganie, przypadek…).
Pomija commity scalające (Merge …) oraz fixup!/squash!. Diff wklejany przez `git commit -v`
(pod linią nożyczek) i linie komentarza nie liczą się do opisu.
Użycie: python3 process/tools/check_commit.py <plik_z_opisem_commita>
"""
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import model as M  # noqa: E402


SCISSORS = re.compile(r"^\S -{24} >8 -{24}$")


def comment_char():
    """Znak komentarza z core.commentChar (domyślnie „#”; przy „auto” git dobiera go sam)."""
    r = subprocess.run(["git", "config", "core.commentChar"], capture_output=True, text=True)
    value = r.stdout.strip()
    return value if len(value) == 1 else "#"


def description(text, char="#"):
    """Opis commita tak, jak zapisze go git: bez linii komentarza i bez wszystkiego od linii
    nożyczek („>8”), pod którą `git commit -v` wkleja diff."""
    lines = []
    for line in text.splitlines():
        if SCISSORS.match(line):
            break
        if not line.startswith(char):
            lines.append(line)
    return "\n".join(lines).strip()


def main(file):
    with open(file, encoding="utf-8") as f:
        desc = description(f.read(), comment_char())
    if not desc or desc.startswith(("Merge ", "fixup!", "squash!")):
        return 0
    m = M.Model()
    ids = m.ids_in(desc)
    known = [i for i in ids if i in m.by_id]
    if known:
        return 0
    print("commit-msg: opis commita nie wskazuje żadnego istniejącego ID (P-07).")
    if ids:
        print(f"Znalezione, ale nieistniejące: {', '.join(sorted(set(ids)))}")
    print("Dodaj np. decyzję (D-nn) albo element, którego dotyczy zmiana.")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
