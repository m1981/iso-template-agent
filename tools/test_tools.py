"""Test narzędzi śladu: pełny łańcuch wszystkich typów z id.toml, każdy błąd E1–E9, W1, W3, W4, W5 i rekord postępu.

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

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FIXTURES = {
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

BREAKAGES = [
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
    ("E7", "use-cases.md", "- scenarios: SC-01\n", "- scenarios: IO-01\n"),
    ("E7", "use-cases.md", "- scope: IO-01\n", "- scope: IO-02\n"),
    ("E4", "verification.md", "- result: pass\n", "- checklist: XYZ\n- result: pass\n"),
    ("E4", "verification.md", "- result: pass\n", "- checklist: UC\n- result: pass\n- failed: UC.3\n"),
    ("E4", "verification.md", "- result: fail\n", "- checklist: REQ\n- result: fail\n- failed: REQ.99\n"),
    ("E4", "requirements.md", "- source: UC-01\n", "- source: UC-01\n- quality: speed\n"),
    ("E1", "verification.md", "- items: UC-01\n", "- subject: inne\n"),
]

WARNINGS = [
    ("W3", "requirements.md", "- source: IO-02, DP-01\n- status: initiated", "- source: IO-02, DP-01\n- status: verified", "W3 OUT-01"),
    ("W3", "requirements.md", "- source: RSK-01\n- status: initiated", "- source: RSK-01\n- status: approved", "W3 CAP-02"),
    ("W1", "corrections.md", "- cause: VER-02", "- cause: TSK-01", "W1 VER-02"),
    ("W4", "risks.md", "- source: UC-01\n", "- source: UC-01\n- źródło: UC-01\n", "W4 RSK-01"),
    ("W4", "plan.md", "- mitigation: mniejszy zakres\n", "- mitigation: mniejszy zakres\n- działanie: x\n", "W4 PRK-01"),
]


# Przykłady używają podmiotu wymagań z tools/id.toml, więc test działa także po ustawieniu własnego `system`.
sys.path.insert(0, os.path.join(ROOT, "tools"))
import model as M  # noqa: E402

SYSTEM = M.load_toml(os.path.join(ROOT, "tools", "id.toml")).get("project", {}).get("system", "System")


def for_system(text):
    return text.replace("System shall", f"{SYSTEM} shall")


FIXTURES = {name: for_system(text) for name, text in FIXTURES.items()}
BREAKAGES = [(code, name, for_system(a), for_system(b)) for code, name, a, b in BREAKAGES]


def run_py(tmpdir, *args, stdin_text=None):
    return subprocess.run([sys.executable, "-B", *args], cwd=tmpdir, capture_output=True, text=True, input=stdin_text)


def prepare(tmpdir):
    for f in ("tools", ".githooks"):
        shutil.copytree(os.path.join(ROOT, f), os.path.join(tmpdir, f), ignore=shutil.ignore_patterns("__pycache__"))
    shutil.copy(os.path.join(ROOT, "decisions.md"), tmpdir)
    shutil.copy(os.path.join(ROOT, "checklist.md"), tmpdir)
    shutil.copytree(os.path.join(ROOT, "modules", "navigation"), os.path.join(tmpdir, "navigation"),
                    ignore=shutil.ignore_patterns("__pycache__"))
    os.makedirs(os.path.join(tmpdir, "tests"), exist_ok=True)
    for p, content in FIXTURES.items():
        with open(os.path.join(tmpdir, p), "w", encoding="utf-8") as f:
            f.write(content)


def main():
    failures = []
    # parser zastępczy (Python < 3.11, np. 3.10 na Macu) musi dawać to samo co tomllib
    for name in ("id.toml", "iso29110.toml"):
        fpath = os.path.join(ROOT, "tools", name)
        if M.load_toml(fpath, fallback=True) != M.load_toml(fpath):
            failures.append(f"parser zastępczy czyta tools/{name} inaczej niż tomllib")
    with tempfile.TemporaryDirectory() as tmpdir:
        bad_toml = os.path.join(tmpdir, "bad_toml.toml")
        open(bad_toml, "w", encoding="utf-8").write('a = "x"\n\nb = nie-napis\n')
        hard_toml = os.path.join(tmpdir, "hard_toml.toml")
        open(hard_toml, "w", encoding="utf-8").write('a = "C:\\\\" # komentarz\nb = [\n  "x [y]",\n  "z # nie komentarz",\n]\n')
        expected_toml = {"a": "C:\\", "b": ["x [y]", "z # nie komentarz"]}
        if M.load_toml(hard_toml, fallback=True) != expected_toml:
            failures.append(f"parser zastępczy źle czyta napisy z \\\\, # i ]: {M.load_toml(hard_toml, fallback=True)}")
        try:
            M.load_toml(bad_toml, fallback=True)
            failures.append("parser zastępczy przyjął niepoprawną wartość")
        except ValueError as e:
            if f"{bad_toml}:3:" not in str(e):
                failures.append(f"komunikat parsera zastępczego nie podaje numeru linii: {e}")
    with tempfile.TemporaryDirectory() as tmpdir:
        prepare(tmpdir)
        r = run_py(tmpdir, "tools/trace.py")
        if r.returncode != 0:
            failures.append("łańcuch wzorcowy ma błędy:\n" + r.stdout)
        trace_md = open(os.path.join(tmpdir, "trace.md"), encoding="utf-8").read()
        for expected in ("| UC-01 | UC | SC-01, IO-01 |", "| CAP-01 | REQ | UC-01 |", "| CAP-01 | REQ | AT-01 |",
                      "| UC-01 | UC | RSK-01, CAP-01, E-01, E-02, E-03, E-04, E-05, VER-01 |", "| D-01 | D | DP-01, G-ELM-01 |",
                      "| TSK-01 | UC, CAP-01 | UC-01, CAP-01 |", "| WP.23 | VER Weryfikacja | 2 |", "| WP.21 | trace.md | — |",
                      "| SC-01 | SC | UC-01, VAL-01 |"):
            if expected not in trace_md:
                failures.append(f"trace.md nie zawiera wiersza: {expected}")
        for code, file, a, b in BREAKAGES:
            fpath = os.path.join(tmpdir, file)
            original = open(fpath, encoding="utf-8").read()
            assert a in original, (code, a)
            open(fpath, "w", encoding="utf-8").write(original.replace(a, b, 1))
            r = run_py(tmpdir, "tools/trace.py", "/dev/null")
            if r.returncode != 1 or f"\n{code} " not in "\n" + r.stdout:
                failures.append(f"{code} ({file}) nie został zgłoszony:\n{r.stdout}")
            open(fpath, "w", encoding="utf-8").write(original)
        for code, file, a, b, expected in WARNINGS:
            fpath = os.path.join(tmpdir, file)
            original = open(fpath, encoding="utf-8").read()
            assert a in original, (code, a)
            open(fpath, "w", encoding="utf-8").write(original.replace(a, b, 1))
            r = run_py(tmpdir, "tools/trace.py", "/dev/null")
            if r.returncode != 0 or f"\n{expected}" not in "\n" + r.stdout:
                failures.append(f"{code} nie zostało zgłoszone jako ostrzeżenie:\n{r.stdout}")
            open(fpath, "w", encoding="utf-8").write(original)
        fpath = os.path.join(tmpdir, "use-cases.md")
        original = open(fpath, encoding="utf-8").read()
        open(fpath, "w", encoding="utf-8").write(original.replace("- status: initiated\n", "- status: verified\n"))
        r = run_py(tmpdir, "tools/trace.py", "/dev/null")
        if "W3" in r.stdout:
            failures.append("W3 zgłoszone mimo rekordu VER-01 z wynikiem pass:\n" + r.stdout)
        open(fpath, "w", encoding="utf-8").write(original)
        r = run_py(tmpdir, "tools/trace.py", "/dev/null")
        if "W3" in r.stdout or "W1 VER" in r.stdout or "W4" in r.stdout:
            failures.append("łańcuch wzorcowy ma nieoczekiwane ostrzeżenia:\n" + r.stdout)

        def with_change(name, a, b, check):
            """Zmienia plik, uruchamia trace.py, przywraca plik; check(stdout, kod) zwraca opis porażki albo None."""
            fpath = os.path.join(tmpdir, name)
            original = open(fpath, encoding="utf-8").read()
            assert a in original, (name, a)
            open(fpath, "w", encoding="utf-8").write(original.replace(a, b, 1))
            r = run_py(tmpdir, "tools/trace.py", "/dev/null")
            open(fpath, "w", encoding="utf-8").write(original)
            problem = check(r.stdout, r.returncode)
            if problem:
                failures.append(problem + ":\n" + r.stdout)

        # #3: tekst w kształcie ID nie jest odnośnikiem; nieznane ID z istniejącego obszaru jest
        with_change("scope.md", "- kind: In\n", "- kind: In\n\nAlgorytm SHA-256, kodowanie UTF-16, wersja UC-990 i kod xUC-99.\n",
                    lambda out, rc: "tekst SHA-256/UTF-16/UC-990/xUC-99 dał błąd" if rc != 0 else None)
        with_change("scope.md", "- kind: In\n", "- kind: In\n\nPatrz CAP-09.\n",
                    lambda out, rc: "nieznane CAP-09 w tekście nie dało E2" if "E2 scope.md" not in out else None)
        # #15: dwukropek po ID w nagłówku ma własny komunikat; punkt rozszerzenia nie jest polem
        with_change("use-cases.md", "### UC-01 Przechwycić", "### UC-01: Przechwycić",
                    lambda out, rc: "nagłówek „UC-01:” bez komunikatu o dwukropku" if "dwukropek" not in out else None)
        with_change("use-cases.md", "- status: initiated\n", "- status: initiated\n- 3a. Brak sieci: zapis lokalny\n",
                    lambda out, rc: "punkt rozszerzenia „3a.” potraktowany jak pole" if "W4" in out else None)
        # #4: scenariusz bez tagu nie dopisuje pól do poprzedniego testu AT
        with_change("tests/capture.feature", "    Given x\n",
                    "    Given x\n\n  Scenario: Inny bez tagu\n  # verifies: OUT-01\n  # todo: dopisać\n    Given y\n",
                    lambda out, rc: "scenariusz bez tagu zmienił pola AT-01" if ("W4 AT-01" in out or rc != 0) else None)
        # #5: ekran bez krawędzi jest widoczny dla reguł mapy
        screens = os.path.join(tmpdir, "navigation", "screens.mmd")
        original = open(screens, encoding="utf-8").read()
        open(screens, "a", encoding="utf-8").write('  E06["E-06 Sierota"]\n  class E06 modal\n')
        r = subprocess.run([sys.executable, "-B", "check.py", "screens.mmd"], cwd=os.path.join(tmpdir, "navigation"),
                           capture_output=True, text=True)
        if r.returncode == 0 or "E-06 Sierota" not in r.stdout:
            failures.append("ekran bez krawędzi nie został zgłoszony przez reguły mapy:\n" + r.stdout)
        open(screens, "w", encoding="utf-8").write(original)

        r = run_py(tmpdir, "tools/progress.py")
        progress_md = open(os.path.join(tmpdir, "progress.md"), encoding="utf-8").read()
        for expected in ("| MS-01 Zakres i przypadki użycia | OBJ-01 | 2026-11-01 | baseline-01-zakres | nie | ACC-01 accepted |",
                      "| TSK-01 Napisać przypadki i wymagania | MS-01 | in_progress | — | — | UC, CAP-01 | initiated 2 |",
                      "| COR-01 Doprecyzować CAP-02 | initiated | VER-02 | poprawić tekst |",
                      "| REQ Wymaganie EARS | WP.13 | 3 | 0 | 0 |"):
            if expected not in progress_md:
                failures.append(f"progress.md nie zawiera wiersza: {expected}")

        def git(*a):
            return subprocess.run(["git", *a], cwd=tmpdir, capture_output=True, text=True)
        git("init", "-q", "-b", "main")
        git("config", "user.name", "test"), git("config", "user.email", "test@example.com")
        git("config", "core.hooksPath", ".githooks")
        run_py(tmpdir, "tools/trace.py")
        run_py(tmpdir, "tools/progress.py")
        run_py(tmpdir, "tools/iso_map.py")
        iso_map = open(os.path.join(tmpdir, "iso-map.html"), encoding="utf-8").read()
        for expected in ('<td>WP.10</td><td>Project plan</td>', 'TSK -.-&gt;|"produces (w dół)"|', "class WP01,"):
            if expected not in iso_map:
                failures.append(f"iso-map.html nie zawiera: {expected}")
        git("add", "-A")
        if git("commit", "-q", "-m", "bez identyfikatora").returncode == 0:
            failures.append("commit-msg przepuścił opis bez ID")
        # #2: diff pod linią nożyczek (git commit -v) nie liczy się do opisu; core.commentChar jest uwzględniany
        msg = os.path.join(tmpdir, "msg.txt")
        open(msg, "w", encoding="utf-8").write("poprawka bez identyfikatora\n# ------------------------ >8 ------------------------\n+ D-01\n")
        if run_py(tmpdir, "tools/check_commit.py", msg).returncode == 0:
            failures.append("commit-msg przepuścił opis bez ID, licząc ID z diffu pod nożyczkami")
        git("config", "core.commentChar", ";")
        open(msg, "w", encoding="utf-8").write("; komentarz bez znaczenia\nZmiana (D-01)\n")
        if run_py(tmpdir, "tools/check_commit.py", msg).returncode != 0:
            failures.append("commit-msg nie uwzględnił core.commentChar")
        git("config", "--unset", "core.commentChar")
        os.remove(msg)
        r = git("commit", "-q", "-m", "Pierwszy commit (D-01)")
        if r.returncode != 0:
            failures.append("commit z D-01 został odrzucony:\n" + r.stdout + r.stderr)
        # D-32: zmiana rodzica po weryfikacji daje W5, sama zmiana stanu nie
        scen = os.path.join(tmpdir, "scenarios.md")
        original = open(scen, encoding="utf-8").read()
        open(scen, "w", encoding="utf-8").write(original.replace("- status: initiated\n", "- status: verified\n"))
        if "W5" in run_py(tmpdir, "tools/trace.py", "/dev/null").stdout:
            failures.append("W5 po samej zmianie stanu rodzica")
        open(scen, "w", encoding="utf-8").write(original.replace("zapisuje, potem porządkuje", "zapisuje i od razu porządkuje"))
        r = run_py(tmpdir, "tools/trace.py", "/dev/null")
        if "W5 UC-01: rodzic SC-01 zmienił się po weryfikacji VER-01" not in r.stdout:
            failures.append("zmiana rodzica po weryfikacji nie dała W5:\n" + r.stdout)
        open(scen, "w", encoding="utf-8").write(original)
        # D-35: odtworzenie z kopii (lokalny bare jako origin)
        backup = os.path.join(tmpdir, "..", os.path.basename(tmpdir) + "-kopia.git")
        subprocess.run(["git", "init", "-q", "--bare", backup], capture_output=True)  # domyślna gałąź celowo inna niż main
        git("remote", "add", "origin", backup)
        git("push", "-q", "origin", "main")
        r = run_py(tmpdir, "tools/restore_check.py")
        if r.returncode != 0:
            failures.append("restore_check nie przeszedł na świeżej kopii:\n" + r.stdout)
        git("tag", "-a", "lokalny-tag", "-m", "x")
        r = run_py(tmpdir, "tools/restore_check.py", "--record")
        if r.returncode != 1 or "brak w kopii: lokalny-tag" not in r.stdout:
            failures.append("restore_check nie wykrył tagu spoza kopii:\n" + r.stdout)
        git("tag", "-d", "lokalny-tag")
        verification = open(os.path.join(tmpdir, "verification.md"), encoding="utf-8").read()
        if "- subject: repository" not in verification or "- failed: REPO.2" not in verification:
            failures.append("restore_check --record nie dopisał rekordu VER")
        r = run_py(tmpdir, "tools/trace.py")
        if r.returncode != 0:
            failures.append("rekord VER z subject: repository dał błędy śladu:\n" + r.stdout)
        run_py(tmpdir, "tools/progress.py")
        git("add", "-A")
        if git("commit", "-q", "-m", "Sprawdzenie kopii (D-01)").returncode != 0:
            failures.append("commit z rekordem odtworzenia został odrzucony")
        shutil.rmtree(backup, ignore_errors=True)
        git("tag", "-a", "baseline-01-zakres", "-m", "Baseline")
        with open(os.path.join(tmpdir, "verification.md"), "a", encoding="utf-8") as f:
            f.write("\n### VER-04 Przegląd CAP-01\n- items: CAP-01\n- date: 2026-10-14\n- result: pass\n")
        run_py(tmpdir, "tools/trace.py")
        git("add", "-A")
        if git("commit", "-q", "-m", "Po baseline bez progress.md (D-01)").returncode == 0:
            failures.append("pre-commit przepuścił nieaktualny progress.md po tagu")
        run_py(tmpdir, "tools/progress.py")
        if "| baseline-01-zakres | tak, " not in open(os.path.join(tmpdir, "progress.md"), encoding="utf-8").read():
            failures.append("progress.md nie pokazuje osiągniętego kamienia MS-01 po tagu")
        git("add", "-A")
        r = git("commit", "-q", "-m", "Po baseline (D-01)")
        if r.returncode != 0:
            failures.append("commit z aktualnym progress.md został odrzucony:\n" + r.stdout + r.stderr)
        with open(os.path.join(tmpdir, "iso-map.html"), "a", encoding="utf-8") as f:
            f.write("x\n")
        git("add", "-A")
        if git("commit", "-q", "-m", "Zmiana strony (D-01)").returncode == 0:
            failures.append("pre-commit przepuścił nieaktualny iso-map.html")
        git("checkout", "HEAD", "--", "iso-map.html")
        with open(os.path.join(tmpdir, "trace.md"), "a", encoding="utf-8") as f:
            f.write("x\n")
        git("add", "-A")
        if git("commit", "-q", "-m", "Zmiana (D-01)").returncode == 0:
            failures.append("pre-commit przepuścił nieaktualny trace.md")

        # D-22: start nowego projektu z kopii szablonu
        r = run_py(tmpdir, "tools/new_project.py")
        if r.returncode == 0:
            failures.append("new_project.py zadziałał mimo niezacommitowanych zmian")
        git("checkout", "HEAD", "--", "trace.md")
        r = run_py(tmpdir, "tools/new_project.py")
        archive = os.path.join(tmpdir, "archive", "template")
        if r.returncode != 0:
            failures.append("new_project.py odmówił na czystym repozytorium:\n" + r.stdout + r.stderr)
        for name in ("decisions.md", "trace.md", "progress.md"):
            if not os.path.exists(os.path.join(archive, name)):
                failures.append(f"new_project.py nie przeniósł {name} do archive/template/")
        new_register = open(os.path.join(tmpdir, "decisions.md"), encoding="utf-8").read()
        if "### D-01 Start projektu z szablonu" not in new_register or "### D-02" in new_register:
            failures.append("nowy decisions.md nie zawiera samej decyzji D-01")
        git("add", "-A")
        r = git("commit", "-q", "-m", "Start projektu (D-01)")
        if r.returncode != 0:
            failures.append("pierwszy commit nowego projektu został odrzucony:\n" + r.stdout + r.stderr)
        if run_py(tmpdir, "tools/new_project.py").returncode == 0:
            failures.append("new_project.py zadziałał drugi raz")

    # D-38: E9 według tablicy decyzyjnej (MC/DC): rekord nowy × wynik pass × element zmieniony w tym commicie
    with tempfile.TemporaryDirectory() as tmpdir:
        prepare(tmpdir)

        def git3(*a):
            return subprocess.run(["git", *a], cwd=tmpdir, capture_output=True, text=True)
        git3("init", "-q", "-b", "main")
        git3("config", "user.name", "test"), git3("config", "user.email", "test@example.com")
        git3("config", "core.hooksPath", ".githooks")
        for script in ("trace.py", "progress.py", "iso_map.py"):
            run_py(tmpdir, "tools/" + script)
        git3("add", "-A")
        if git3("commit", "-q", "-m", "Import (D-01)").returncode != 0:
            failures.append("E9: pierwszy commit (import) został odrzucony")

        def attempt(changes):
            """changes: [(plik, a, b)]; „+” w a = dopisz b na końcu. Zwraca (czy commit przeszedł, wyjście)."""
            for name, a, b in changes:
                fpath = os.path.join(tmpdir, name)
                text = open(fpath, encoding="utf-8").read()
                text = text + b if a == "+" else text.replace(a, b, 1)
                open(fpath, "w", encoding="utf-8").write(text)
            for script in ("trace.py", "progress.py", "iso_map.py"):
                run_py(tmpdir, "tools/" + script)
            git3("add", "-A")
            r = git3("commit", "-q", "-m", "Próba (D-01)")
            git3("reset", "-q", "--hard", "HEAD~1" if r.returncode == 0 else "HEAD")
            return r.returncode == 0, r.stdout + r.stderr

        change_cap = ("requirements.md", "store it in the Inbox.", "store it in the Inbox at once.")
        new_ver = lambda result, items="CAP-01": ("verification.md", "+", f"\n### VER-10 Przegląd\n- items: {items}\n- date: 2026-10-17\n- result: {result}\n")
        cases = [
            ("1 nowy rekord, pass, element zmieniony", [change_cap, new_ver("pass")], False),
            ("2 nowy rekord, pass, element bez zmian", [new_ver("pass")], True),
            ("3 nowy rekord, fail, element zmieniony", [change_cap, new_ver("fail")], True),
            ("4 stary rekord VER-01, element zmieniony", [("use-cases.md", "Przechwycić Element", "Przechwycić Element szybko")], True),
            ("5 nowy element weryfikowany w tym samym commicie",
             [("requirements.md", "+", "\n### CAP-03\n- pattern: event\n- text: When the User submits an Item, System shall show it.\n- source: UC-01\n- status: initiated\n"),
              new_ver("pass", "CAP-03")], False),
            ("6 sama zmiana stanu przy weryfikacji", [("requirements.md", "- source: UC-01\n- status: initiated", "- source: UC-01\n- status: verified"), new_ver("pass")], True),
            ("7 rekord kopii zapasowej (subject: repository)",
             [change_cap, ("verification.md", "+", "\n### VER-10 Kopia\n- subject: repository\n- date: 2026-10-17\n- result: pass\n")], True),
        ]
        for name, changes, expect_ok in cases:
            ok, out = attempt([(f, a, for_system(b)) for f, a, b in changes])
            if ok != expect_ok or (not expect_ok and "E9 VER-10" not in out):
                failures.append(f"E9, przypadek {name}: commit {'przeszedł' if ok else 'odrzucony'}, oczekiwano {'przejścia' if expect_ok else 'E9'}:\n{out}")

    # D-22, D-29 na prawdziwych plikach: kopia szablonu bez historii, start projektu, pierwszy commit.
    # Tylko w samym szablonie (w projekcie archive/template/ już jest). Moduł nawigacji ma przykładową
    # mapę z UC-01 do zastąpienia, więc sprawdza go pierwsza część testu.
    in_template = not os.path.exists(os.path.join(ROOT, "archive", "template"))
    if in_template:
        with tempfile.TemporaryDirectory() as tmpdir:
            copy = os.path.join(tmpdir, "projekt")
            shutil.copytree(ROOT, copy, ignore=shutil.ignore_patterns(".git", "__pycache__", "archive"))
            if not os.path.exists(os.path.join(copy, "risks.md")):
                shutil.copy(os.path.join(copy, "modules", "risks", "risks.md"), copy)
            r = run_py(copy, "tools/new_project.py")
            if r.returncode == 0:
                failures.append("new_project.py zadziałał poza repozytorium gita")

            def git2(*a):
                return subprocess.run(["git", *a], cwd=copy, capture_output=True, text=True)
            git2("init", "-q", "-b", "main")
            git2("config", "user.name", "test"), git2("config", "user.email", "test@example.com")
            git2("config", "core.hooksPath", ".githooks")
            for script in ("trace.py", "progress.py", "iso_map.py"):  # moduł ryzyk zmienia pliki generowane
                run_py(copy, "tools/" + script)
            git2("add", "-A")
            r = git2("commit", "-q", "-m", "Kopia szablonu (D-01)")
            if r.returncode != 0:
                failures.append("commit kopii szablonu został odrzucony:\n" + r.stdout + r.stderr)
            r = run_py(copy, "tools/new_project.py")
            if r.returncode != 0:
                failures.append("new_project.py na kopii szablonu nie zadziałał:\n" + r.stdout + r.stderr)
            r = run_py(copy, "tools/trace.py")
            if r.returncode != 0:
                failures.append("po new_project.py ślad kopii szablonu ma błędy:\n" + r.stdout)
            git2("add", "-A")
            r = git2("commit", "-q", "-m", "Start projektu (D-01)")
            if r.returncode != 0:
                failures.append("pierwszy commit projektu z kopii szablonu został odrzucony:\n" + r.stdout + r.stderr)
            if git2("tag").stdout.strip():
                failures.append("kopia szablonu bez historii ma tagi szablonu")

    for p in failures:
        print("NIE:", p)
    print(f"test_tools: {len(BREAKAGES)} psuć, {len(WARNINGS)} ostrzeżeń, E9 (7 przypadków), postęp, new-project, hooki commit-msg i pre-commit — {'OK' if not failures else f'{len(failures)} porażek'}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
