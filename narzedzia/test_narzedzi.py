"""Test narzędzi śladu: pełny łańcuch wszystkich typów z id.toml oraz każdy błąd B1–B8.

Buduje kopię szablonu w katalogu tymczasowym z przykładowymi artefaktami (moduły
nawigacji i ryzyk wdrożone), sprawdza, że jest bez błędów, a potem psuje ją na
kolejne sposoby i sprawdza, że slad.py zgłasza właściwy kod. Testuje też hooki.
Użycie: python3 narzedzia/test_narzedzi.py   (kod wyjścia 1 = test nie przeszedł)
"""
import os
import shutil
import subprocess
import sys
import tempfile

KORZEN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PLIKI = {
    "scenki.md": "### SC-01 Ania zapisuje sprawy w biegu\n- osoba: Ania\n- treść: zapisuje, potem porządkuje\n",
    "zakres.md": "### IO-01 Przechwytywanie\n- rodzaj: In\n\n### IO-02 Powiadamianie osób spoza systemu\n- rodzaj: Out\n",
    "zasady.md": "### ZP-01 Prowadzenie do postępu\n- ustanawia: D-01\n- treść: system podsuwa następny krok\n",
    "slownik.md": ("### G-AKT-01 Użytkownik (User)\n- definicja: osoba z kontem\n\n"
                   "### G-ELM-01 Element (Item)\n- definicja: zapisana treść\n- zmienione przez: D-01\n\n"
                   "### G-ELM-02 Inbox (Inbox)\n- definicja: widok nowych Elementów\n\n"
                   "### G-AKT-02 Delegat (Delegate)\n- definicja: osoba spoza systemu\n"),
    "przypadki-uzycia.md": "### UC-01 Przechwycić Element\n- poziom: morze\n- scenki: SC-01\n- zakres: IO-01\n",
    "ryzyka.md": "### RYZ-01 Brak sieci przy zapisie\n- źródło: UC-01\n",
    "wymagania.md": ("### CAP-01\n- wzorzec: event\n- tekst: When the User submits an Item, System shall store it in the Inbox.\n- źródło: UC-01\n- status: draft\n\n"
                     "### CAP-02\n- wzorzec: unwanted\n- tekst: If the device is offline, then System shall store the Item locally.\n- źródło: RYZ-01\n- status: draft\n\n"
                     "### OUT-01\n- wzorzec: ubiquitous\n- tekst: System shall not notify a Delegate.\n- źródło: IO-02, ZP-01\n- status: draft\n"),
    "testy/przechwytywanie.feature": ("Feature: Przechwytywanie\n\n  @AT-01\n  # weryfikuje: CAP-01\n  Scenario: Zapis\n    Given x\n"),
}

PSUCIA = [
    ("B1", "przypadki-uzycia.md", "- scenki: SC-01\n- zakres: IO-01\n", ""),
    ("B2", "wymagania.md", "- źródło: UC-01\n", "- źródło: UC-09\n"),
    ("B3", "zakres.md", "### IO-02 Powiadamianie", "### IO-01 Powiadamianie"),
    ("B4", "wymagania.md", "- status: draft\n", "- status: gotowe\n"),
    ("B5", "wymagania.md", "System shall store it", "System shall store it and shall"),
    ("B6", "wymagania.md", "store it in the Inbox", "store it in the Archive"),
    ("B7", "wymagania.md", "- źródło: RYZ-01\n", "- źródło: SC-01\n"),
    ("B8", "wymagania.md", "- źródło: RYZ-01\n", "- źródło: UC-01\n"),
]


def uruchom(kat, *args, wejscie=None):
    return subprocess.run([sys.executable, "-B", *args], cwd=kat, capture_output=True, text=True, input=wejscie)


def przygotuj(kat):
    for f in ("narzedzia", ".githooks"):
        shutil.copytree(os.path.join(KORZEN, f), os.path.join(kat, f), ignore=shutil.ignore_patterns("__pycache__"))
    shutil.copy(os.path.join(KORZEN, "decyzje.md"), kat)
    shutil.copytree(os.path.join(KORZEN, "moduly", "nawigacja"), os.path.join(kat, "nawigacja"),
                    ignore=shutil.ignore_patterns("__pycache__"))
    os.makedirs(os.path.join(kat, "testy"), exist_ok=True)
    for p, tresc in PLIKI.items():
        with open(os.path.join(kat, p), "w", encoding="utf-8") as f:
            f.write(tresc)


def main():
    porazki = []
    with tempfile.TemporaryDirectory() as kat:
        przygotuj(kat)
        r = uruchom(kat, "narzedzia/slad.py")
        if r.returncode != 0:
            porazki.append("łańcuch wzorcowy ma błędy:\n" + r.stdout)
        slad = open(os.path.join(kat, "slad.md"), encoding="utf-8").read()
        for oczek in ("| UC-01 | UC | SC-01, IO-01 |", "| CAP-01 | WYM | UC-01 |", "| CAP-01 | WYM | AT-01 |",
                      "| UC-01 | UC | RYZ-01, CAP-01, E-01, E-02, E-03, E-04, E-05 |", "| D-01 | D | ZP-01, G-ELM-01 |"):
            if oczek not in slad:
                porazki.append(f"slad.md nie zawiera wiersza: {oczek}")
        for kod, plik, a, b in PSUCIA:
            sciezka = os.path.join(kat, plik)
            oryg = open(sciezka, encoding="utf-8").read()
            assert a in oryg, (kod, a)
            open(sciezka, "w", encoding="utf-8").write(oryg.replace(a, b, 1))
            r = uruchom(kat, "narzedzia/slad.py", "/dev/null")
            if r.returncode != 1 or f"\n{kod} " not in "\n" + r.stdout:
                porazki.append(f"{kod} nie został zgłoszony:\n{r.stdout}")
            open(sciezka, "w", encoding="utf-8").write(oryg)

        def git(*a):
            return subprocess.run(["git", *a], cwd=kat, capture_output=True, text=True)
        git("init", "-q", "-b", "main")
        git("config", "user.name", "test"), git("config", "user.email", "test@example.com")
        git("config", "core.hooksPath", ".githooks")
        uruchom(kat, "narzedzia/slad.py")
        git("add", "-A")
        if git("commit", "-q", "-m", "bez identyfikatora").returncode == 0:
            porazki.append("commit-msg przepuścił opis bez ID")
        if git("commit", "-q", "-m", "Pierwszy commit (D-01)").returncode != 0:
            porazki.append("commit z D-01 został odrzucony")
        with open(os.path.join(kat, "slad.md"), "a", encoding="utf-8") as f:
            f.write("x\n")
        git("add", "-A")
        if git("commit", "-q", "-m", "Zmiana (D-01)").returncode == 0:
            porazki.append("pre-commit przepuścił nieaktualny slad.md")

    for p in porazki:
        print("NIE:", p)
    print(f"test_narzedzi: {len(PSUCIA)} psuć, hooki commit-msg i pre-commit — {'OK' if not porazki else f'{len(porazki)} porażek'}")
    return 1 if porazki else 0


if __name__ == "__main__":
    sys.exit(main())
