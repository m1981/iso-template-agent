"""Test narzędzi śladu: pełny łańcuch wszystkich typów z id.toml, każdy błąd E1–E8, W1, W3 i rekord postępu.

Buduje kopię szablonu w katalogu tymczasowym z przykładowymi artefaktami (moduły
nawigacji i ryzyk wdrożone), sprawdza, że jest bez błędów, a potem psuje ją na
kolejne sposoby i sprawdza, że trace.py zgłasza właściwy kod. Testuje też hooki.
Użycie: python3 tools/test_tools.py   (kod wyjścia 1 = test nie przeszedł)
"""
import os
import shutil
import subprocess
import sys
import tempfile

KORZEN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PLIKI = {
    "scenarios.md": "### SC-01 Ania zapisuje sprawy w biegu\n- person: Ania\n- content: zapisuje, potem porządkuje\n- status: initiated\n",
    "scope.md": ("### IO-01 Przechwytywanie\n- kind: In\n- status: initiated\n\n"
                 "### IO-02 Powiadamianie osób spoza systemu\n- kind: Out\n- status: initiated\n"),
    "principles.md": "### DP-01 Prowadzenie do postępu\n- established_by: D-01\n- content: system podsuwa następny krok\n- status: initiated\n",
    "glossary.md": ("### G-AKT-01 Użytkownik (User)\n- definition: osoba z kontem\n- status: initiated\n\n"
                    "### G-ELM-01 Element (Item)\n- definition: zapisana treść\n- changed_by: D-01\n- status: initiated\n\n"
                    "### G-ELM-02 Inbox (Inbox)\n- definition: widok nowych Elementów\n- status: initiated\n\n"
                    "### G-AKT-02 Delegat (Delegate)\n- definition: osoba spoza systemu\n- status: initiated\n"),
    "use-cases.md": "### UC-01 Przechwycić Element\n- level: sea\n- scenarios: SC-01\n- scope: IO-01\n- status: initiated\n",
    "risks.md": "### RSK-01 Brak sieci przy zapisie\n- source: UC-01\n- status: initiated\n",
    "requirements.md": ("### CAP-01\n- pattern: event\n- text: When the User submits an Item, System shall store it in the Inbox.\n- source: UC-01\n- status: initiated\n\n"
                        "### CAP-02\n- pattern: unwanted\n- text: If the device is offline, then System shall store the Item locally.\n- source: RSK-01\n- status: initiated\n\n"
                        "### OUT-01\n- pattern: ubiquitous\n- text: System shall not notify a Delegate.\n- source: IO-02, DP-01\n- status: initiated\n"),
    "plan.md": ("### OBJ-01 Specyfikacja gotowa do implementacji\n- measure: wymagania zweryfikowane\n\n"
                "### MS-01 Zakres i przypadki użycia\n- objective: OBJ-01\n- due: 2026-11-01\n- tag: baseline-01-zakres\n\n"
                "### TSK-01 Napisać przypadki i wymagania\n- milestone: MS-01\n- produces: UC, CAP-01\n- status: in_progress\n\n"
                "### PRK-01 Za mało czasu\n- concerns: MS-01\n- status: open\n- mitigation: mniejszy zakres\n"),
    "verification.md": ("### VER-01 Przegląd UC-01\n- items: UC-01\n- date: 2026-10-14\n- result: pass\n\n"
                        "### VER-02 Przegląd CAP-02\n- items: CAP-02\n- date: 2026-10-14\n- result: fail\n"),
    "corrections.md": "### COR-01 Doprecyzować CAP-02\n- cause: VER-02\n- action: poprawić tekst\n- status: initiated\n",
    "validation.md": "### VAL-01 Walidacja SC-01\n- items: SC-01\n- date: 2026-10-14\n- result: pass\n",
    "acceptance.md": "### ACC-01 Odbiór MS-01\n- milestone: MS-01\n- date: 2026-10-14\n- result: accepted\n",
    "tests/capture.feature": ("Feature: Przechwytywanie\n\n  @AT-01\n  # verifies: CAP-01\n  # status: initiated\n  Scenario: Zapis\n    Given x\n"),
}

PSUCIA = [
    ("E1", "use-cases.md", "- scenarios: SC-01\n- scope: IO-01\n", ""),
    ("E1", "scenarios.md", "- status: initiated\n", ""),
    ("E2", "requirements.md", "- source: UC-01\n", "- source: UC-09\n"),
    ("E3", "scope.md", "### IO-02 Powiadamianie", "### IO-01 Powiadamianie"),
    ("E4", "requirements.md", "- status: initiated\n", "- status: draft\n"),
    ("E5", "requirements.md", "System shall store it", "System shall store it and shall"),
    ("E6", "requirements.md", "store it in the Inbox", "store it in the Archive"),
    ("E7", "requirements.md", "- source: RSK-01\n", "- source: SC-01\n"),
    ("E8", "requirements.md", "- source: RSK-01\n", "- source: UC-01\n"),
    ("E1", "plan.md", "- due: 2026-11-01\n", ""),
    ("E4", "plan.md", "- produces: UC, CAP-01", "- produces: UC, przypadki"),
    ("E4", "verification.md", "- result: pass\n", "- result: ok\n"),
    ("E4", "use-cases.md", "- status: initiated\n", "- status: brief\n"),
    ("E7", "corrections.md", "- cause: VER-02", "- cause: UC-01"),
]

OSTRZEZENIA = [
    ("W3", "requirements.md", "- source: IO-02, DP-01\n- status: initiated", "- source: IO-02, DP-01\n- status: verified", "W3 OUT-01"),
    ("W3", "requirements.md", "- source: RSK-01\n- status: initiated", "- source: RSK-01\n- status: approved", "W3 CAP-02"),
    ("W1", "corrections.md", "- cause: VER-02", "- cause: TSK-01", "W1 VER-02"),
]


def uruchom(kat, *args, wejscie=None):
    return subprocess.run([sys.executable, "-B", *args], cwd=kat, capture_output=True, text=True, input=wejscie)


def przygotuj(kat):
    for f in ("tools", ".githooks"):
        shutil.copytree(os.path.join(KORZEN, f), os.path.join(kat, f), ignore=shutil.ignore_patterns("__pycache__"))
    shutil.copy(os.path.join(KORZEN, "decisions.md"), kat)
    shutil.copytree(os.path.join(KORZEN, "modules", "navigation"), os.path.join(kat, "navigation"),
                    ignore=shutil.ignore_patterns("__pycache__"))
    os.makedirs(os.path.join(kat, "tests"), exist_ok=True)
    for p, tresc in PLIKI.items():
        with open(os.path.join(kat, p), "w", encoding="utf-8") as f:
            f.write(tresc)


def main():
    porazki = []
    with tempfile.TemporaryDirectory() as kat:
        przygotuj(kat)
        r = uruchom(kat, "tools/trace.py")
        if r.returncode != 0:
            porazki.append("łańcuch wzorcowy ma błędy:\n" + r.stdout)
        slad = open(os.path.join(kat, "trace.md"), encoding="utf-8").read()
        for oczek in ("| UC-01 | UC | SC-01, IO-01 |", "| CAP-01 | REQ | UC-01 |", "| CAP-01 | REQ | AT-01 |",
                      "| UC-01 | UC | RSK-01, CAP-01, E-01, E-02, E-03, E-04, E-05, VER-01 |", "| D-01 | D | DP-01, G-ELM-01 |",
                      "| TSK-01 | UC, CAP-01 | UC-01, CAP-01 |", "| WP.23 | VER Weryfikacja | 2 |", "| WP.21 | trace.md | — |",
                      "| SC-01 | SC | UC-01, VAL-01 |"):
            if oczek not in slad:
                porazki.append(f"trace.md nie zawiera wiersza: {oczek}")
        for kod, plik, a, b in PSUCIA:
            sciezka = os.path.join(kat, plik)
            oryg = open(sciezka, encoding="utf-8").read()
            assert a in oryg, (kod, a)
            open(sciezka, "w", encoding="utf-8").write(oryg.replace(a, b, 1))
            r = uruchom(kat, "tools/trace.py", "/dev/null")
            if r.returncode != 1 or f"\n{kod} " not in "\n" + r.stdout:
                porazki.append(f"{kod} ({plik}) nie został zgłoszony:\n{r.stdout}")
            open(sciezka, "w", encoding="utf-8").write(oryg)
        for kod, plik, a, b, oczek in OSTRZEZENIA:
            sciezka = os.path.join(kat, plik)
            oryg = open(sciezka, encoding="utf-8").read()
            assert a in oryg, (kod, a)
            open(sciezka, "w", encoding="utf-8").write(oryg.replace(a, b, 1))
            r = uruchom(kat, "tools/trace.py", "/dev/null")
            if r.returncode != 0 or f"\n{oczek}" not in "\n" + r.stdout:
                porazki.append(f"{kod} nie zostało zgłoszone jako ostrzeżenie:\n{r.stdout}")
            open(sciezka, "w", encoding="utf-8").write(oryg)
        sciezka = os.path.join(kat, "use-cases.md")
        oryg = open(sciezka, encoding="utf-8").read()
        open(sciezka, "w", encoding="utf-8").write(oryg.replace("- status: initiated\n", "- status: verified\n"))
        r = uruchom(kat, "tools/trace.py", "/dev/null")
        if "W3" in r.stdout:
            porazki.append("W3 zgłoszone mimo rekordu VER-01 z wynikiem pass:\n" + r.stdout)
        open(sciezka, "w", encoding="utf-8").write(oryg)
        r = uruchom(kat, "tools/trace.py", "/dev/null")
        if "W3" in r.stdout or "W1 VER" in r.stdout:
            porazki.append("łańcuch wzorcowy ma nieoczekiwane ostrzeżenia:\n" + r.stdout)

        r = uruchom(kat, "tools/progress.py")
        postep = open(os.path.join(kat, "progress.md"), encoding="utf-8").read()
        for oczek in ("| MS-01 Zakres i przypadki użycia | OBJ-01 | 2026-11-01 | baseline-01-zakres | nie | ACC-01 accepted |",
                      "| TSK-01 Napisać przypadki i wymagania | MS-01 | in_progress | — | — | UC, CAP-01 | initiated 2 |",
                      "| COR-01 Doprecyzować CAP-02 | initiated | VER-02 | poprawić tekst |",
                      "| REQ Wymaganie EARS | WP.13 | 3 | 0 | 0 |"):
            if oczek not in postep:
                porazki.append(f"progress.md nie zawiera wiersza: {oczek}")

        def git(*a):
            return subprocess.run(["git", *a], cwd=kat, capture_output=True, text=True)
        git("init", "-q", "-b", "main")
        git("config", "user.name", "test"), git("config", "user.email", "test@example.com")
        git("config", "core.hooksPath", ".githooks")
        uruchom(kat, "tools/trace.py")
        uruchom(kat, "tools/progress.py")
        git("add", "-A")
        if git("commit", "-q", "-m", "bez identyfikatora").returncode == 0:
            porazki.append("commit-msg przepuścił opis bez ID")
        r = git("commit", "-q", "-m", "Pierwszy commit (D-01)")
        if r.returncode != 0:
            porazki.append("commit z D-01 został odrzucony:\n" + r.stdout + r.stderr)
        git("tag", "-a", "baseline-01-zakres", "-m", "Baseline")
        with open(os.path.join(kat, "verification.md"), "a", encoding="utf-8") as f:
            f.write("\n### VER-03 Przegląd CAP-01\n- items: CAP-01\n- date: 2026-10-14\n- result: pass\n")
        uruchom(kat, "tools/trace.py")
        git("add", "-A")
        if git("commit", "-q", "-m", "Po baseline bez progress.md (D-01)").returncode == 0:
            porazki.append("pre-commit przepuścił nieaktualny progress.md po tagu")
        uruchom(kat, "tools/progress.py")
        if "| baseline-01-zakres | tak, " not in open(os.path.join(kat, "progress.md"), encoding="utf-8").read():
            porazki.append("progress.md nie pokazuje osiągniętego kamienia MS-01 po tagu")
        git("add", "-A")
        r = git("commit", "-q", "-m", "Po baseline (D-01)")
        if r.returncode != 0:
            porazki.append("commit z aktualnym progress.md został odrzucony:\n" + r.stdout + r.stderr)
        with open(os.path.join(kat, "trace.md"), "a", encoding="utf-8") as f:
            f.write("x\n")
        git("add", "-A")
        if git("commit", "-q", "-m", "Zmiana (D-01)").returncode == 0:
            porazki.append("pre-commit przepuścił nieaktualny trace.md")

    for p in porazki:
        print("NIE:", p)
    print(f"test_tools: {len(PSUCIA)} psuć, {len(OSTRZEZENIA)} ostrzeżeń, postęp, hooki commit-msg i pre-commit — {'OK' if not porazki else f'{len(porazki)} porażek'}")
    return 1 if porazki else 0


if __name__ == "__main__":
    sys.exit(main())
