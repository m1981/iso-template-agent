"""Test narzędzi śladu: pełny łańcuch wszystkich typów z id.toml, każdy błąd B1–B8, O3 i rekord postępu.

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
    "wymagania.md": ("### CAP-01\n- wzorzec: event\n- tekst: When the User submits an Item, System shall store it in the Inbox.\n- źródło: UC-01\n- status: rozpoczęty\n\n"
                     "### CAP-02\n- wzorzec: unwanted\n- tekst: If the device is offline, then System shall store the Item locally.\n- źródło: RYZ-01\n- status: rozpoczęty\n\n"
                     "### OUT-01\n- wzorzec: ubiquitous\n- tekst: System shall not notify a Delegate.\n- źródło: IO-02, ZP-01\n- status: rozpoczęty\n"),
    "plan.md": ("### CEL-01 Specyfikacja gotowa do implementacji\n- miara: wymagania zweryfikowane\n\n"
                "### KM-01 Zakres i przypadki użycia\n- cel: CEL-01\n- termin: 2026-11-01\n- tag: baseline-01-zakres\n\n"
                "### ZAD-01 Napisać przypadki i wymagania\n- kamień: KM-01\n- produkuje: UC, CAP-01\n- status: w toku\n\n"
                "### RP-01 Za mało czasu\n- dotyczy: KM-01\n- status: otwarte\n- działanie: mniejszy zakres\n"),
    "rekordy.md": ("### WER-01 Przegląd UC-01\n- obiekt: UC-01\n- data: 2026-10-14\n- wynik: zgodny\n\n"
                   "### WER-02 Przegląd CAP-02\n- obiekt: CAP-02\n- data: 2026-10-14\n- wynik: niezgodny\n\n"
                   "### KOR-01 Doprecyzować CAP-02\n- przyczyna: WER-02\n- działanie: poprawić tekst\n- status: rozpoczęta\n\n"
                   "### AKC-01 Odbiór KM-01\n- kamień: KM-01\n- data: 2026-10-14\n- wynik: przyjęty\n"),
    "testy/przechwytywanie.feature": ("Feature: Przechwytywanie\n\n  @AT-01\n  # weryfikuje: CAP-01\n  Scenario: Zapis\n    Given x\n"),
}

PSUCIA = [
    ("B1", "przypadki-uzycia.md", "- scenki: SC-01\n- zakres: IO-01\n", ""),
    ("B2", "wymagania.md", "- źródło: UC-01\n", "- źródło: UC-09\n"),
    ("B3", "zakres.md", "### IO-02 Powiadamianie", "### IO-01 Powiadamianie"),
    ("B4", "wymagania.md", "- status: rozpoczęty\n", "- status: gotowe\n"),
    ("B5", "wymagania.md", "System shall store it", "System shall store it and shall"),
    ("B6", "wymagania.md", "store it in the Inbox", "store it in the Archive"),
    ("B7", "wymagania.md", "- źródło: RYZ-01\n", "- źródło: SC-01\n"),
    ("B8", "wymagania.md", "- źródło: RYZ-01\n", "- źródło: UC-01\n"),
    ("B1", "plan.md", "- termin: 2026-11-01\n", ""),
    ("B4", "plan.md", "- produkuje: UC, CAP-01", "- produkuje: UC, przypadki"),
    ("B4", "rekordy.md", "- wynik: zgodny\n", "- wynik: ok\n"),
    ("B4", "przypadki-uzycia.md", "- poziom: morze\n", "- poziom: morze\n- status: draft\n"),
    ("B7", "rekordy.md", "- przyczyna: WER-02", "- przyczyna: UC-01"),
]

OSTRZEZENIA = [
    ("O3", "wymagania.md", "- źródło: IO-02, ZP-01\n- status: rozpoczęty", "- źródło: IO-02, ZP-01\n- status: zweryfikowany", "O3 OUT-01"),
    ("O3", "wymagania.md", "- źródło: RYZ-01\n- status: rozpoczęty", "- źródło: RYZ-01\n- status: zatwierdzony", "O3 CAP-02"),
    ("O1", "rekordy.md", "- przyczyna: WER-02", "- przyczyna: ZAD-01", "O1 WER-02"),
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
                      "| UC-01 | UC | RYZ-01, CAP-01, E-01, E-02, E-03, E-04, E-05, WER-01 |", "| D-01 | D | ZP-01, G-ELM-01 |",
                      "| ZAD-01 | UC, CAP-01 | UC-01, CAP-01 |", "| WP.23 | WER Weryfikacja | 2 |", "| WP.21 | slad.md | — |"):
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
        for kod, plik, a, b, oczek in OSTRZEZENIA:
            sciezka = os.path.join(kat, plik)
            oryg = open(sciezka, encoding="utf-8").read()
            assert a in oryg, (kod, a)
            open(sciezka, "w", encoding="utf-8").write(oryg.replace(a, b, 1))
            r = uruchom(kat, "narzedzia/slad.py", "/dev/null")
            if r.returncode != 0 or f"\n{oczek}" not in "\n" + r.stdout:
                porazki.append(f"{kod} nie zostało zgłoszone jako ostrzeżenie:\n{r.stdout}")
            open(sciezka, "w", encoding="utf-8").write(oryg)
        sciezka = os.path.join(kat, "przypadki-uzycia.md")
        oryg = open(sciezka, encoding="utf-8").read()
        open(sciezka, "w", encoding="utf-8").write(oryg.replace("- poziom: morze\n", "- poziom: morze\n- status: zweryfikowany\n"))
        r = uruchom(kat, "narzedzia/slad.py", "/dev/null")
        if "O3" in r.stdout:
            porazki.append("O3 zgłoszone mimo rekordu WER-01 z wynikiem zgodny:\n" + r.stdout)
        open(sciezka, "w", encoding="utf-8").write(oryg)
        r = uruchom(kat, "narzedzia/slad.py", "/dev/null")
        if "O3" in r.stdout or "O1 WER" in r.stdout:
            porazki.append("łańcuch wzorcowy ma nieoczekiwane ostrzeżenia:\n" + r.stdout)

        r = uruchom(kat, "narzedzia/postep.py")
        postep = open(os.path.join(kat, "postep.md"), encoding="utf-8").read()
        for oczek in ("| KM-01 Zakres i przypadki użycia | CEL-01 | 2026-11-01 | baseline-01-zakres | nie | AKC-01 przyjęty |",
                      "| ZAD-01 Napisać przypadki i wymagania | KM-01 | w toku | — | — | UC, CAP-01 | rozpoczęty 2 |",
                      "| KOR-01 Doprecyzować CAP-02 | rozpoczęta | WER-02 | poprawić tekst |",
                      "| WYM Wymaganie EARS | WP.13 | 3 | 0 | 0 |"):
            if oczek not in postep:
                porazki.append(f"postep.md nie zawiera wiersza: {oczek}")

        def git(*a):
            return subprocess.run(["git", *a], cwd=kat, capture_output=True, text=True)
        git("init", "-q", "-b", "main")
        git("config", "user.name", "test"), git("config", "user.email", "test@example.com")
        git("config", "core.hooksPath", ".githooks")
        uruchom(kat, "narzedzia/slad.py")
        uruchom(kat, "narzedzia/postep.py")
        git("add", "-A")
        if git("commit", "-q", "-m", "bez identyfikatora").returncode == 0:
            porazki.append("commit-msg przepuścił opis bez ID")
        r = git("commit", "-q", "-m", "Pierwszy commit (D-01)")
        if r.returncode != 0:
            porazki.append("commit z D-01 został odrzucony:\n" + r.stdout + r.stderr)
        git("tag", "-a", "baseline-01-zakres", "-m", "Baseline")
        with open(os.path.join(kat, "rekordy.md"), "a", encoding="utf-8") as f:
            f.write("\n### WER-03 Przegląd CAP-01\n- obiekt: CAP-01\n- data: 2026-10-14\n- wynik: zgodny\n")
        uruchom(kat, "narzedzia/slad.py")
        git("add", "-A")
        if git("commit", "-q", "-m", "Po baseline bez postep.md (D-01)").returncode == 0:
            porazki.append("pre-commit przepuścił nieaktualny postep.md po tagu")
        uruchom(kat, "narzedzia/postep.py")
        if "| baseline-01-zakres | tak, " not in open(os.path.join(kat, "postep.md"), encoding="utf-8").read():
            porazki.append("postep.md nie pokazuje osiągniętego kamienia KM-01 po tagu")
        git("add", "-A")
        r = git("commit", "-q", "-m", "Po baseline (D-01)")
        if r.returncode != 0:
            porazki.append("commit z aktualnym postep.md został odrzucony:\n" + r.stdout + r.stderr)
        with open(os.path.join(kat, "slad.md"), "a", encoding="utf-8") as f:
            f.write("x\n")
        git("add", "-A")
        if git("commit", "-q", "-m", "Zmiana (D-01)").returncode == 0:
            porazki.append("pre-commit przepuścił nieaktualny slad.md")

    for p in porazki:
        print("NIE:", p)
    print(f"test_narzedzi: {len(PSUCIA)} psuć, {len(OSTRZEZENIA)} ostrzeżeń, postęp, hooki commit-msg i pre-commit — {'OK' if not porazki else f'{len(porazki)} porażek'}")
    return 1 if porazki else 0


if __name__ == "__main__":
    sys.exit(main())
