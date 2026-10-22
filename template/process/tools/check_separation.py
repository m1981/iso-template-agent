"""Autor nie weryfikuje sam siebie w jednym commicie (szablon D-38; ISO/IEC 29110 SI.O7, uwaga 2).

Pre-commit porównuje to, co idzie do commita (indeks gita), z ostatnim commitem (HEAD):
  E9  commit dodaje rekord VER albo VAL z wynikiem „pass” i w tym samym commicie zmienia
      (albo tworzy) któryś z elementów wskazanych w jego polu items.
Zmiana samego pola status nie liczy się jako zmiana elementu (status zmienia się przy weryfikacji).
Tablica decyzyjna: E9 tylko gdy rekord jest nowy, wynik to pass i element zmienił się w tym commicie.
Pierwszy commit repozytorium (brak HEAD) jest importem i nie jest sprawdzany.

Reguły śladu są z bieżących narzędzi (process/tools/id.toml), ustawienia z każdej migawki.

Użycie: python3 process/tools/check_separation.py   (kod wyjścia 1 = E9)
"""
import io
import os
import shutil
import subprocess
import sys
import tarfile
import tempfile

TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, TOOLS_DIR)
import model as M  # noqa: E402

ROOT = M.ROOT

RECORD_TYPES = ("VER", "VAL")


def git(*args, **kw):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, **kw)


def snapshot_head(target):
    archive = git("archive", "--format=tar", "HEAD")
    with tarfile.open(fileobj=io.BytesIO(archive.stdout)) as t:
        try:
            t.extractall(target, filter="data")
        except TypeError:
            t.extractall(target)


def snapshot_index(target):
    git("checkout-index", "-a", "-f", f"--prefix={target}{os.sep}")


def violations(head, staged):
    found = []
    for e in staged.elements:
        if e.type not in RECORD_TYPES or e.id in head.by_id:
            continue  # tylko rekordy dodane w tym commicie
        if staged.value(e, "result") != "pass":
            continue
        for item in staged.ids_in(e.fields.get("items", "")):
            now = staged.by_id.get(item)
            before = head.by_id.get(item)
            if now is None:
                continue
            if before is None:
                found.append(f"E9 {e.id}: {item} powstaje w tym samym commicie, w którym ma wynik „pass”")
            elif M.fingerprint(before) != M.fingerprint(now):
                found.append(f"E9 {e.id}: {item} zmienia się w tym samym commicie, w którym ma wynik „pass”")
    return found


def main():
    if git("rev-parse", "--verify", "-q", "HEAD").returncode != 0:
        return 0
    tmp = tempfile.mkdtemp()
    try:
        head_dir, staged_dir = os.path.join(tmp, "head"), os.path.join(tmp, "staged")
        snapshot_head(head_dir)
        snapshot_index(staged_dir)
        # ten sam model śladu dla obu stron: reguły bieżących narzędzi
        found = violations(M.Model(head_dir), M.Model(staged_dir))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    for x in found:
        print(x)
    if found:
        print("\npre-commit: autor nie weryfikuje sam siebie (szablon D-38). Zacommituj zmianę elementu osobno, "
              "a rekord weryfikacji w kolejnym commicie, najlepiej z osobnej sesji weryfikatora (process/roles/verifier.md).")
    return 1 if found else 0


if __name__ == "__main__":
    sys.exit(main())
