"""Hook commit-msg: opis commita musi wskazać co najmniej jedno istniejące ID (P-07).

Dzięki temu każda zmiana ma przyczynę w modelu śladu (decyzja, wymaganie, przypadek…).
Pomija commity scalające (Merge …) oraz fixup!/squash!.
Użycie: python3 tools/check_commit.py <plik_z_opisem_commita>
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import model as M  # noqa: E402


def main(plik):
    with open(plik, encoding="utf-8") as f:
        linie = [l for l in f.read().splitlines() if not l.startswith("#")]
    opis = "\n".join(linie).strip()
    if not opis or opis.startswith(("Merge ", "fixup!", "squash!")):
        return 0
    m = M.Model()
    ids = m.ids_w(opis)
    znane = [i for i in ids if i in m.po_id]
    if znane:
        return 0
    print("commit-msg: opis commita nie wskazuje żadnego istniejącego ID (P-07).")
    if ids:
        print(f"Znalezione, ale nieistniejące: {', '.join(sorted(set(ids)))}")
    print("Dodaj np. decyzję (D-nn) albo element, którego dotyczy zmiana.")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
