"""Test narzędzi procesu: pełny łańcuch wszystkich typów z id.toml, każdy błąd E1–E9, W1, W3, W4, W5 i rekord postępu.

Buduje w katalogu tymczasowym projekt z kopią pakietu procesu (process/) i przykładowymi artefaktami
(moduły nawigacji i ryzyk wdrożone), sprawdza, że jest bez błędów, a potem psuje go na kolejne sposoby
i sprawdza, że trace.py zgłasza właściwy kod. Testuje też hooki, init.py i kontrole make check.
Fixture powstaje tylko z pakietu i jego wzorców, nie z dokumentów projektu, w którym test uruchomiono.
Każdy podproces dostaje PROCESS_ROOT katalogu tymczasowego.
Użycie: python3 process/tools/test_tools.py   (kod wyjścia 1 = test nie przeszedł)
"""
import os
import shutil
import subprocess
import sys
import tempfile

PROC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # katalog pakietu procesu

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
    "tests/capture.feature": ("Feature: Przechwytywanie\n\n  @AT-01\n  # verifies: CAP-01\n  # runner: process/tools/test_tools.py::chain\n  # status: initiated\n  Scenario: Zapis\n    Given x\n"),
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
    ("E4", "tests/capture.feature", "# runner: process/tools/test_tools.py::chain", "# runner: tools/brak.py::chain"),
]

WARNINGS = [
    ("W3", "requirements.md", "- source: IO-02, DP-01\n- status: initiated", "- source: IO-02, DP-01\n- status: verified", "W3 OUT-01"),
    ("W3", "requirements.md", "- source: RSK-01\n- status: initiated", "- source: RSK-01\n- status: approved", "W3 CAP-02"),
    ("W1", "corrections.md", "- cause: VER-02", "- cause: TSK-01", "W1 VER-02"),
    ("W4", "risks.md", "- source: UC-01\n", "- source: UC-01\n- źródło: UC-01\n", "W4 RSK-01"),
    ("W4", "plan.md", "- mitigation: mniejszy zakres\n", "- mitigation: mniejszy zakres\n- działanie: x\n", "W4 PRK-01"),
]


# Pliki fixture w układzie projektu (szablon D-42): stara nazwa → ścieżka względem katalogu głównego.
PATHS = {"scenarios.md": "spec/scenarios.md", "scope.md": "spec/scope.md", "principles.md": "spec/principles.md",
         "glossary.md": "spec/glossary.md", "use-cases.md": "spec/use-cases.md", "risks.md": "spec/risks.md",
         "requirements.md": "spec/requirements.md", "plan.md": "project/plan.md", "decisions.md": "project/decisions.md",
         "verification.md": "records/verification.md", "corrections.md": "records/corrections.md",
         "validation.md": "records/validation.md", "acceptance.md": "records/acceptance.md",
         "tests/capture.feature": "spec/tests/capture.feature", "trace.md": "reports/trace.md",
         "progress.md": "reports/progress.md", "iso-map.html": "reports/iso-map.html"}
FIXTURES = {PATHS.get(k, k): v for k, v in FIXTURES.items()}
BREAKAGES = [(code, PATHS.get(f, f), a, b) for code, f, a, b in BREAKAGES]
WARNINGS = [(code, PATHS.get(f, f), a, b, e) for code, f, a, b, e in WARNINGS]

sys.path.insert(0, os.path.join(PROC, "tools"))
import model as M  # noqa: E402
import init as I  # noqa: E402

# Przykłady używają podmiotu wymagań ze wzorca ustawień, więc test działa także po ustawieniu własnego `system`.
SYSTEM = M.load_toml(os.path.join(PROC, "templates", "project", "settings.toml")).get("system", "System")


def for_system(text):
    return text.replace("System shall", f"{SYSTEM} shall")


FIXTURES = {name: for_system(text) for name, text in FIXTURES.items()}
BREAKAGES = [(code, name, for_system(a), for_system(b)) for code, name, a, b in BREAKAGES]


def env_for(tmpdir):
    return dict(os.environ, PROCESS_ROOT=tmpdir)


def run_py(tmpdir, *args, stdin_text=None):
    return subprocess.run([sys.executable, "-B", *args], cwd=tmpdir, capture_output=True, text=True,
                          input=stdin_text, env=env_for(tmpdir))


def copy_process(target):
    shutil.copytree(PROC, os.path.join(target, "process"), ignore=shutil.ignore_patterns("__pycache__"))


def prepare(tmpdir):
    """Projekt testowy: kopia pakietu, ustawienia i rejestr ze wzorców (D-01), mapa nawigacji ze wzorca, fixture."""
    copy_process(tmpdir)
    templates = os.path.join(tmpdir, "process", "templates")
    for d in ("project", "spec/tests", "spec/navigation", "records", "reports"):
        os.makedirs(os.path.join(tmpdir, d), exist_ok=True)
    shutil.copy(os.path.join(templates, "project", "settings.toml"), os.path.join(tmpdir, "project", "settings.toml"))
    with open(os.path.join(tmpdir, "project", "decisions.md"), "w", encoding="utf-8") as f:
        f.write(I.register_text("", "2026-10-14"))
    for name in ("screens.mmd", "navigation-map.html"):
        shutil.copy(os.path.join(templates, "spec", "navigation", name), os.path.join(tmpdir, "spec", "navigation", name))
    for p, content in FIXTURES.items():
        with open(os.path.join(tmpdir, p), "w", encoding="utf-8") as f:
            f.write(content)


class Failures(list):
    """Lista porażek przypisanych do nazwanych przypadków; raport testów czyta wiersze CASE (D-60)."""

    def __init__(self):
        super().__init__()
        self.current, self.cases = None, {}

    def case(self, name):
        self.current = name
        self.cases.setdefault(name, True)

    def append(self, msg):
        super().append(f"[{self.current}] {msg}")
        self.cases[self.current] = False


def main():
    failures = Failures()
    failures.case("toml-fallback")
    # parser zastępczy (Python < 3.11, np. 3.10 na Macu) musi dawać to samo co tomllib
    for fpath in (os.path.join(PROC, "tools", "id.toml"), os.path.join(PROC, "tools", "iso29110.toml"),
                  os.path.join(PROC, "templates", "project", "settings.toml")):
        if M.load_toml(fpath, fallback=True) != M.load_toml(fpath):
            failures.append(f"parser zastępczy czyta {os.path.relpath(fpath, PROC)} inaczej niż tomllib")
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
        failures.case("chain")
        r = run_py(tmpdir, "process/tools/trace.py")
        if r.returncode != 0:
            failures.append("łańcuch wzorcowy ma błędy:\n" + r.stdout)
        trace_md = open(os.path.join(tmpdir, "reports/trace.md"), encoding="utf-8").read()
        for expected in ("| UC-01 | UC | SC-01, IO-01 |", "| CAP-01 | REQ | UC-01 |", "| CAP-01 | REQ | AT-01 |",
                      "| UC-01 | UC | RSK-01, CAP-01, E-01, E-02, E-03, E-04, E-05, VER-01 |", "| D-01 | D | DP-01, G-ELM-01 |",
                      "| TSK-01 | UC, CAP-01 | UC-01, CAP-01 |", "| WP.23 | VER Weryfikacja | 2 |", "| WP.21 | reports/trace.md | — |",
                      "| SC-01 | SC | UC-01, VAL-01 |"):
            if expected not in trace_md:
                failures.append(f"trace.md nie zawiera wiersza: {expected}")
        for i, (code, file, a, b) in enumerate(BREAKAGES, 1):
            failures.case(f"breakage-{i:02d}")
            fpath = os.path.join(tmpdir, file)
            original = open(fpath, encoding="utf-8").read()
            assert a in original, (code, a)
            open(fpath, "w", encoding="utf-8").write(original.replace(a, b, 1))
            r = run_py(tmpdir, "process/tools/trace.py", "/dev/null")
            if r.returncode != 1 or f"\n{code} " not in "\n" + r.stdout:
                failures.append(f"{code} ({file}) nie został zgłoszony:\n{r.stdout}")
            open(fpath, "w", encoding="utf-8").write(original)
        for i, (code, file, a, b, expected) in enumerate(WARNINGS, 1):
            failures.case(f"warning-{i:02d}")
            fpath = os.path.join(tmpdir, file)
            original = open(fpath, encoding="utf-8").read()
            assert a in original, (code, a)
            open(fpath, "w", encoding="utf-8").write(original.replace(a, b, 1))
            r = run_py(tmpdir, "process/tools/trace.py", "/dev/null")
            if r.returncode != 0 or f"\n{expected}" not in "\n" + r.stdout:
                failures.append(f"{code} nie zostało zgłoszone jako ostrzeżenie:\n{r.stdout}")
            open(fpath, "w", encoding="utf-8").write(original)
        failures.case("w3-with-record")
        fpath = os.path.join(tmpdir, "spec/use-cases.md")
        original = open(fpath, encoding="utf-8").read()
        open(fpath, "w", encoding="utf-8").write(original.replace("- status: initiated\n", "- status: verified\n"))
        r = run_py(tmpdir, "process/tools/trace.py", "/dev/null")
        if "W3" in r.stdout:
            failures.append("W3 zgłoszone mimo rekordu VER-01 z wynikiem pass:\n" + r.stdout)
        open(fpath, "w", encoding="utf-8").write(original)
        failures.case("chain-no-warnings")
        r = run_py(tmpdir, "process/tools/trace.py", "/dev/null")
        if "W3" in r.stdout or "W1 VER" in r.stdout or "W4" in r.stdout:
            failures.append("łańcuch wzorcowy ma nieoczekiwane ostrzeżenia:\n" + r.stdout)

        def with_change(name, a, b, check):
            """Zmienia plik, uruchamia trace.py, przywraca plik; check(stdout, kod) zwraca opis porażki albo None."""
            fpath = os.path.join(tmpdir, name)
            original = open(fpath, encoding="utf-8").read()
            assert a in original, (name, a)
            open(fpath, "w", encoding="utf-8").write(original.replace(a, b, 1))
            r = run_py(tmpdir, "process/tools/trace.py", "/dev/null")
            open(fpath, "w", encoding="utf-8").write(original)
            problem = check(r.stdout, r.returncode)
            if problem:
                failures.append(problem + ":\n" + r.stdout)

        # D-33: sekcja charakterystyk jakości pokazuje liczbę wymagań i charakterystyki bez wymagań
        failures.case("quality-section")
        fpath = os.path.join(tmpdir, "spec/requirements.md")
        original = open(fpath, encoding="utf-8").read()
        assert "- source: RSK-01\n" in original
        open(fpath, "w", encoding="utf-8").write(original.replace("- source: RSK-01\n", "- source: RSK-01\n- quality: reliability\n", 1))
        quality_md = os.path.join(tmpdir, "quality.md")
        run_py(tmpdir, "process/tools/trace.py", quality_md)
        open(fpath, "w", encoding="utf-8").write(original)
        quality_text = open(quality_md, encoding="utf-8").read()
        for expected in ("| reliability | 1 | CAP-02 |", "| security | 0 | — |"):
            if expected not in quality_text:
                failures.append(f"sekcja charakterystyk jakości nie zawiera wiersza: {expected}")
        os.remove(quality_md)

        failures.case("id-in-text")
        # #3: tekst w kształcie ID nie jest odnośnikiem; nieznane ID z istniejącego obszaru jest
        with_change("spec/scope.md", "- kind: In\n", "- kind: In\n\nAlgorytm SHA-256, kodowanie UTF-16, wersja UC-990 i kod xUC-99.\n",
                    lambda out, rc: "tekst SHA-256/UTF-16/UC-990/xUC-99 dał błąd" if rc != 0 else None)
        with_change("spec/scope.md", "- kind: In\n", "- kind: In\n\nPatrz CAP-09.\n",
                    lambda out, rc: "nieznane CAP-09 w tekście nie dało E2" if "E2 spec/scope.md" not in out else None)
        failures.case("heading-colon")
        # #15: dwukropek po ID w nagłówku ma własny komunikat; punkt rozszerzenia nie jest polem
        with_change("spec/use-cases.md", "### UC-01 Przechwycić", "### UC-01: Przechwycić",
                    lambda out, rc: "nagłówek „UC-01:” bez komunikatu o dwukropku" if "dwukropek" not in out else None)
        failures.case("extension-point")
        with_change("spec/use-cases.md", "- status: initiated\n", "- status: initiated\n- 3a. Brak sieci: zapis lokalny\n",
                    lambda out, rc: "punkt rozszerzenia „3a.” potraktowany jak pole" if "W4" in out else None)
        failures.case("feature-untagged")
        # #4: scenariusz bez tagu nie dopisuje pól do poprzedniego testu AT
        with_change("spec/tests/capture.feature", "    Given x\n",
                    "    Given x\n\n  Scenario: Inny bez tagu\n  # verifies: OUT-01\n  # todo: dopisać\n    Given y\n",
                    lambda out, rc: "scenariusz bez tagu zmienił pola AT-01" if ("W4 AT-01" in out or rc != 0) else None)
        failures.case("nav-orphan")
        # #5: ekran bez krawędzi jest widoczny dla reguł mapy
        screens = os.path.join(tmpdir, "spec", "navigation", "screens.mmd")
        original = open(screens, encoding="utf-8").read()
        open(screens, "a", encoding="utf-8").write('  E06["E-06 Sierota"]\n  class E06 modal\n')
        r = run_py(tmpdir, "process/modules/navigation/check.py", "spec/navigation/screens.mmd")
        if r.returncode == 0 or "E-06 Sierota" not in r.stdout:
            failures.append("ekran bez krawędzi nie został zgłoszony przez reguły mapy:\n" + r.stdout)
        open(screens, "w", encoding="utf-8").write(original)

        failures.case("progress")
        r = run_py(tmpdir, "process/tools/progress.py")
        progress_md = open(os.path.join(tmpdir, "reports/progress.md"), encoding="utf-8").read()
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
        git("config", "core.hooksPath", "process/hooks")
        run_py(tmpdir, "process/tools/trace.py")
        run_py(tmpdir, "process/tools/progress.py")
        run_py(tmpdir, "process/tools/iso_map.py")
        failures.case("iso-map")
        iso_map = open(os.path.join(tmpdir, "reports/iso-map.html"), encoding="utf-8").read()
        for expected in ('<td>WP.10</td><td>Project plan</td>', 'TSK -.-&gt;|"produces (w dół)"|', "class WP01,"):
            if expected not in iso_map:
                failures.append(f"iso-map.html nie zawiera: {expected}")
        failures.case("commit-msg")
        git("add", "-A")
        if git("commit", "-q", "-m", "bez identyfikatora").returncode == 0:
            failures.append("commit-msg przepuścił opis bez ID")
        # #2: diff pod linią nożyczek (git commit -v) nie liczy się do opisu; core.commentChar jest uwzględniany
        msg = os.path.join(tmpdir, "msg.txt")
        open(msg, "w", encoding="utf-8").write("poprawka bez identyfikatora\n# ------------------------ >8 ------------------------\n+ D-01\n")
        if run_py(tmpdir, "process/tools/check_commit.py", msg).returncode == 0:
            failures.append("commit-msg przepuścił opis bez ID, licząc ID z diffu pod nożyczkami")
        git("config", "core.commentChar", ";")
        open(msg, "w", encoding="utf-8").write("; komentarz bez znaczenia\nZmiana (D-01)\n")
        if run_py(tmpdir, "process/tools/check_commit.py", msg).returncode != 0:
            failures.append("commit-msg nie uwzględnił core.commentChar")
        git("config", "--unset", "core.commentChar")
        os.remove(msg)
        failures.case("first-commit")
        r = git("commit", "-q", "-m", "Pierwszy commit (D-01)")
        if r.returncode != 0:
            failures.append("commit z D-01 został odrzucony:\n" + r.stdout + r.stderr)
        failures.case("w5")
        # D-32: zmiana rodzica po weryfikacji daje W5, sama zmiana stanu nie
        scen = os.path.join(tmpdir, "spec/scenarios.md")
        original = open(scen, encoding="utf-8").read()
        open(scen, "w", encoding="utf-8").write(original.replace("- status: initiated\n", "- status: verified\n"))
        if "W5" in run_py(tmpdir, "process/tools/trace.py", "/dev/null").stdout:
            failures.append("W5 po samej zmianie stanu rodzica")
        open(scen, "w", encoding="utf-8").write(original.replace("zapisuje, potem porządkuje", "zapisuje i od razu porządkuje"))
        r = run_py(tmpdir, "process/tools/trace.py", "/dev/null")
        if "W5 UC-01: rodzic SC-01 zmienił się po weryfikacji VER-01" not in r.stdout:
            failures.append("zmiana rodzica po weryfikacji nie dała W5:\n" + r.stdout)
        open(scen, "w", encoding="utf-8").write(original)
        failures.case("restore-check")
        # D-35: odtworzenie z kopii (lokalny bare jako origin)
        backup = os.path.join(tmpdir, "..", os.path.basename(tmpdir) + "-kopia.git")
        subprocess.run(["git", "init", "-q", "--bare", backup], capture_output=True)  # domyślna gałąź celowo inna niż main
        git("remote", "add", "origin", backup)
        git("push", "-q", "origin", "main")
        r = run_py(tmpdir, "process/tools/restore_check.py")
        if r.returncode != 0:
            failures.append("restore_check nie przeszedł na świeżej kopii:\n" + r.stdout)
        git("tag", "-a", "lokalny-tag", "-m", "x")
        r = run_py(tmpdir, "process/tools/restore_check.py", "--record")
        if r.returncode != 1 or "brak w kopii: lokalny-tag" not in r.stdout:
            failures.append("restore_check nie wykrył tagu spoza kopii:\n" + r.stdout)
        git("tag", "-d", "lokalny-tag")
        verification = open(os.path.join(tmpdir, "records/verification.md"), encoding="utf-8").read()
        if "- subject: repository" not in verification or "- failed: REPO.2" not in verification:
            failures.append("restore_check --record nie dopisał rekordu VER")
        r = run_py(tmpdir, "process/tools/trace.py")
        if r.returncode != 0:
            failures.append("rekord VER z subject: repository dał błędy śladu:\n" + r.stdout)
        run_py(tmpdir, "process/tools/progress.py")
        git("add", "-A")
        if git("commit", "-q", "-m", "Sprawdzenie kopii (D-01)").returncode != 0:
            failures.append("commit z rekordem odtworzenia został odrzucony")
        shutil.rmtree(backup, ignore_errors=True)
        failures.case("precommit-progress")
        git("tag", "-a", "baseline-01-zakres", "-m", "Baseline")
        with open(os.path.join(tmpdir, "records/verification.md"), "a", encoding="utf-8") as f:
            f.write("\n### VER-04 Przegląd CAP-01\n- items: CAP-01\n- date: 2026-10-14\n- result: pass\n")
        run_py(tmpdir, "process/tools/trace.py")
        git("add", "-A")
        if git("commit", "-q", "-m", "Po baseline bez progress.md (D-01)").returncode == 0:
            failures.append("pre-commit przepuścił nieaktualny progress.md po tagu")
        run_py(tmpdir, "process/tools/progress.py")
        if "| baseline-01-zakres | tak, " not in open(os.path.join(tmpdir, "reports/progress.md"), encoding="utf-8").read():
            failures.append("progress.md nie pokazuje osiągniętego kamienia MS-01 po tagu")
        git("add", "-A")
        r = git("commit", "-q", "-m", "Po baseline (D-01)")
        if r.returncode != 0:
            failures.append("commit z aktualnym progress.md został odrzucony:\n" + r.stdout + r.stderr)
        failures.case("precommit-iso-map")
        with open(os.path.join(tmpdir, "reports/iso-map.html"), "a", encoding="utf-8") as f:
            f.write("x\n")
        git("add", "-A")
        if git("commit", "-q", "-m", "Zmiana strony (D-01)").returncode == 0:
            failures.append("pre-commit przepuścił nieaktualny iso-map.html")
        git("checkout", "HEAD", "--", "reports/iso-map.html")
        # D-69: pre-commit sprawdza zawartość indeksu, nie katalog roboczy
        failures.case("precommit-index")
        req = os.path.join(tmpdir, "spec/requirements.md")
        good = open(req, encoding="utf-8").read()
        bad = good.replace("store it in the Inbox", "store it in the Archive", 1)
        assert bad != good
        open(req, "w", encoding="utf-8").write(bad)
        git("add", "spec/requirements.md")
        open(req, "w", encoding="utf-8").write(good)  # błąd tylko w indeksie
        r = git("commit", "-q", "-m", "Błąd tylko w indeksie (D-01)")
        if r.returncode == 0 or "E6" not in r.stdout + r.stderr:
            failures.append("pre-commit przepuścił błąd obecny tylko w indeksie:\n" + r.stdout + r.stderr)
            if r.returncode == 0:
                git("reset", "-q", "--hard", "HEAD~1")
        git("reset", "-q")
        git("checkout", "HEAD", "--", "spec/requirements.md")
        open(req, "w", encoding="utf-8").write(bad)  # błąd tylko w katalogu roboczym
        with open(os.path.join(tmpdir, "notatka.txt"), "w", encoding="utf-8") as f:
            f.write("notatka\n")
        git("add", "notatka.txt")
        r = git("commit", "-q", "-m", "Notatka przy błędzie poza indeksem (D-01)")
        if r.returncode != 0:
            failures.append("pre-commit odrzucił commit przez błąd spoza indeksu:\n" + r.stdout + r.stderr)
        git("checkout", "HEAD", "--", "spec/requirements.md")
        if git("status", "--porcelain").stdout.strip():
            failures.append("po przypadku precommit-index drzewo nie jest czyste:\n" + git("status", "--porcelain").stdout)

        failures.case("precommit-trace")
        with open(os.path.join(tmpdir, "reports/trace.md"), "a", encoding="utf-8") as f:
            f.write("x\n")
        git("add", "-A")
        if git("commit", "-q", "-m", "Zmiana (D-01)").returncode == 0:
            failures.append("pre-commit przepuścił nieaktualny trace.md")

        failures.case("init")
        # D-58: init.py w założonym projekcie odmawia; przy zmianach w śledzonych plikach też
        git("checkout", "HEAD", "--", "reports/trace.md")
        r = run_py(tmpdir, "process/tools/init.py")
        if r.returncode == 0 or "już założono" not in r.stdout:
            failures.append("init.py zadziałał w założonym projekcie:\n" + r.stdout)
        with open(os.path.join(tmpdir, "spec", "scope.md"), "a", encoding="utf-8") as f:
            f.write("\nzmiana\n")
        r = run_py(tmpdir, "process/tools/init.py", "--module", "risks")
        if r.returncode == 0 or "niezacommitowane" not in r.stdout:
            failures.append("init.py zadziałał mimo niezacommitowanych zmian:\n" + r.stdout)
        git("checkout", "HEAD", "--", "spec/scope.md")

    # D-60: raport testów: pass tylko gdy przeszły wszystkie przypadki; brak przypadku i kod 2 to nie sukces
    failures.case("test-report")
    with tempfile.TemporaryDirectory() as tmpdir:
        prepare(tmpdir)
        os.makedirs(os.path.join(tmpdir, "tools"))
        with open(os.path.join(tmpdir, "tools", "fake_runner.py"), "w", encoding="utf-8") as f:
            f.write('print("CASE a: pass")\nprint("CASE b: fail")\n')
        with open(os.path.join(tmpdir, "tools", "not_run.py"), "w", encoding="utf-8") as f:
            f.write('import sys\nprint("NIE URUCHOMIONO")\nsys.exit(2)\n')
        capture = os.path.join(tmpdir, "spec", "tests", "capture.feature")  # bez rekurencji: AT-01 nie uruchamia test_tools.py
        text = open(capture, encoding="utf-8").read()
        assert "process/tools/test_tools.py::chain" in text
        open(capture, "w", encoding="utf-8").write(text.replace("process/tools/test_tools.py::chain", "tools/fake_runner.py::a"))
        with open(os.path.join(tmpdir, "spec", "tests", "report.feature"), "w", encoding="utf-8") as f:
            f.write(for_system("Feature: Raport\n\n"
                    "  @AT-02\n  # verifies: CAP-01\n  # runner: tools/fake_runner.py::a\n  # status: initiated\n  Scenario: a\n    Given x\n\n"
                    "  @AT-03\n  # verifies: CAP-02\n  # runner: tools/fake_runner.py::a, tools/fake_runner.py::b\n  # status: initiated\n  Scenario: b\n    Given x\n\n"
                    "  @AT-04\n  # verifies: OUT-01\n  # runner: tools/fake_runner.py::c\n  # status: initiated\n  Scenario: c\n    Given x\n\n"
                    "  @AT-05\n  # verifies: OUT-01\n  # runner: tools/not_run.py::d\n  # status: initiated\n  Scenario: d\n    Given x\n\n"
                    "  @AT-06\n  # verifies: OUT-01\n  # status: initiated\n  Scenario: ręczny\n    Given x\n"))
        r = run_py(tmpdir, "process/tools/test_report.py", "report.md")
        report = open(os.path.join(tmpdir, "report.md"), encoding="utf-8").read() if os.path.exists(os.path.join(tmpdir, "report.md")) else ""
        for expected in ("| AT-02 | CAP-01 | pass |", "| AT-03 | CAP-02 | fail | tools/fake_runner.py::b: fail |",
                         "| AT-04 | OUT-01 | fail | tools/fake_runner.py::c: brak przypadku |",
                         "| AT-05 | OUT-01 | fail | tools/not_run.py::d: nie uruchomiono |", "| AT-06 | OUT-01 | ręczny |"):
            if expected not in report:
                failures.append(f"raport testów nie zawiera: {expected}\n{report}")
        if r.returncode != 1:
            failures.append(f"raport testów z porażkami zakończył się kodem {r.returncode}")

    # D-61: odwołania do ścieżek; brak pliku, sama nazwa pliku, wzorzec, wyjątek z powodem i zbędny wyjątek
    failures.case("refs")
    with tempfile.TemporaryDirectory() as tmpdir:
        copy_process(tmpdir)  # narzędzie z pakietu; pakiet nie jest śledzony w tym repozytorium testowym
        files = {"lib/trace.py": "# x\n", "docs/a.md": "Zobacz lib/trace.py, trace.py, spec/*.md i UC-nn.md.\n",
                 "docs/b.md": "Patrz brak/plik.md.\n", "docs/c.md": "Powstanie: later.md\n",
                 "project/check_refs.allow": "later.md # powstaje później\nstary.md # już nikt nie wspomina\n"}
        for name, text in files.items():
            os.makedirs(os.path.dirname(os.path.join(tmpdir, name)), exist_ok=True)
            open(os.path.join(tmpdir, name), "w", encoding="utf-8").write(text)
        subprocess.run(["git", "init", "-q"], cwd=tmpdir, capture_output=True)
        subprocess.run(["git", "add", *files], cwd=tmpdir, capture_output=True)
        r = run_py(tmpdir, "process/tools/check_refs.py")
        errs = [x for x in r.stdout.splitlines() if ": " in x and not x.startswith("check_refs:")]
        expected = ["docs/b.md:1: brak ścieżki „brak/plik.md”", "project/check_refs.allow:2: zbędny wyjątek „stary.md” (ścieżka istnieje albo nikt o niej nie wspomina)"]
        if r.returncode != 1 or errs != expected:
            failures.append(f"check_refs: oczekiwane {expected}, jest:\n{r.stdout}")

    # D-62: przeciek domeny: konkretne ID i pojęcia ze słownika projektu w plikach procesu
    failures.case("leak-id")
    with tempfile.TemporaryDirectory() as tmpdir:
        prepare(tmpdir)
        r = run_py(tmpdir, "process/tools/check_leak.py")
        if r.returncode != 0:
            failures.append("check_leak bez słownika zgłasza przeciek w samym pakiecie procesu:\n" + r.stdout)
        extra = os.path.join(tmpdir, "process", "extra")
        os.makedirs(extra)
        open(os.path.join(extra, "ok.md"), "w", encoding="utf-8").write("Wzór: UC-nn, CAP-nn, D-17, kodowanie UTF-16.\n")
        r = run_py(tmpdir, "process/tools/check_leak.py", "--glossary", "spec/glossary.md", "process/extra")
        if r.returncode != 0:
            failures.append("check_leak: zastępcze ID, D-nn i UTF-16 zgłoszone jako przeciek:\n" + r.stdout)
        for name, text, expected in (("leak-id", "Przykład: UC-01.\n", "konkretne ID UC-01 (UC)"),
                                     ("leak-id", "Przykład: CAP-03.\n", "konkretne ID CAP-03 (REQ)"),
                                     ("leak-term", "Każdy Item ma termin.\n", "pojęcie projektu „Item”"),
                                     ("leak-term", "Każdy element ma termin.\n", "pojęcie projektu „Element”")):
            failures.case(name)
            open(os.path.join(extra, "leak.md"), "w", encoding="utf-8").write(text)
            r = run_py(tmpdir, "process/tools/check_leak.py", "--glossary", "spec/glossary.md", "process/extra")
            if r.returncode != 1 or expected not in r.stdout:
                failures.append(f"check_leak nie zgłosił: {expected}\n{r.stdout}")

    # D-38: E9 według tablicy decyzyjnej (MC/DC): rekord nowy × wynik pass × element zmieniony w tym commicie
    with tempfile.TemporaryDirectory() as tmpdir:
        prepare(tmpdir)

        def git3(*a):
            return subprocess.run(["git", *a], cwd=tmpdir, capture_output=True, text=True)
        git3("init", "-q", "-b", "main")
        git3("config", "user.name", "test"), git3("config", "user.email", "test@example.com")
        git3("config", "core.hooksPath", "process/hooks")
        for script in ("trace.py", "progress.py", "iso_map.py"):
            run_py(tmpdir, "process/tools/" + script)
        failures.case("e9-import")
        git3("add", "-A")
        if git3("commit", "-q", "-m", "Import (D-01)").returncode != 0:
            failures.append("E9: pierwszy commit (import) został odrzucony")

        def attempt(changes):
            """changes: [(plik, a, b)]; „+” w a = dopisz b na końcu. Zwraca (czy commit przeszedł, wyjście)."""
            for name, a, b in changes:
                fpath = os.path.join(tmpdir, PATHS.get(name, name))
                text = open(fpath, encoding="utf-8").read()
                text = text + b if a == "+" else text.replace(a, b, 1)
                open(fpath, "w", encoding="utf-8").write(text)
            for script in ("trace.py", "progress.py", "iso_map.py"):
                run_py(tmpdir, "process/tools/" + script)
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
            failures.case("e9-" + name.split()[0])
            ok, out = attempt([(f, a, for_system(b)) for f, a, b in changes])
            if ok != expect_ok or (not expect_ok and "E9 VER-10" not in out):
                failures.append(f"E9, przypadek {name}: commit {'przeszedł' if ok else 'odrzucony'}, oczekiwano {'przejścia' if expect_ok else 'E9'}:\n{out}")

    # D-58, D-29: start projektu z samego pakietu (jak po copier copy): init.py, moduł ryzyk, pierwszy commit przez hooki
    failures.case("project-start")
    with tempfile.TemporaryDirectory() as tmpdir:
        copy = os.path.join(tmpdir, "projekt")
        os.makedirs(copy)
        copy_process(copy)
        with open(os.path.join(copy, "README.md"), "w", encoding="utf-8") as f:
            f.write("README użytkownika\n")
        r = run_py(copy, "process/tools/init.py")
        if r.returncode == 0:
            failures.append("init.py zadziałał poza repozytorium gita")

        def git2(*a):
            return subprocess.run(["git", *a], cwd=copy, capture_output=True, text=True, env=env_for(copy))
        git2("init", "-q", "-b", "main")
        git2("config", "user.name", "test"), git2("config", "user.email", "test@example.com")
        r = run_py(copy, "process/tools/init.py")
        if r.returncode != 0:
            failures.append("init.py w nowym repozytorium nie zadziałał:\n" + r.stdout + r.stderr)
        if open(os.path.join(copy, "README.md"), encoding="utf-8").read() != "README użytkownika\n" or "pominięto README.md" not in r.stdout:
            failures.append("init.py nadpisał istniejący README.md")
        for name in ("project/agreement.md", "project/plan.md", "project/settings.toml", "spec/requirements.md",
                     "records/verification.md", "AGENTS.md", "Makefile", "reports/trace.md"):
            if not os.path.exists(os.path.join(copy, name)):
                failures.append(f"init.py nie założył {name}")
        register = open(os.path.join(copy, "project", "decisions.md"), encoding="utf-8").read()
        if "### D-01 Start projektu z szablonu" not in register or "### D-02" in register or "{date}" in register:
            failures.append("rejestr nowego projektu nie ma samej decyzji D-01 z datą")
        if "VER-01" in open(os.path.join(copy, "records", "verification.md"), encoding="utf-8").read():
            failures.append("wzorzec rekordów weryfikacji zawiera rekord warstwy procesu")
        if run_py(copy, "process/tools/init.py").returncode == 0:
            failures.append("init.py zadziałał drugi raz")
        r = run_py(copy, "process/tools/init.py", "--module", "risks")
        if r.returncode != 0 or not os.path.exists(os.path.join(copy, "spec", "risks.md")):
            failures.append("init.py --module risks nie wdrożył modułu:\n" + r.stdout)
        r = subprocess.run(["make", "hooks"], cwd=copy, capture_output=True, text=True, env=env_for(copy))
        if r.returncode != 0 or git2("config", "--get", "core.hooksPath").stdout.strip() != "process/hooks":
            failures.append("make hooks w nowym projekcie nie ustawił process/hooks:\n" + r.stdout + r.stderr)
        r = subprocess.run(["make", "check"], cwd=copy, capture_output=True, text=True, env=env_for(copy))
        if r.returncode != 0:
            failures.append("make check w nowym projekcie nie przechodzi:\n" + r.stdout[-1500:] + r.stderr[-500:])
        git2("add", "-A")
        r = git2("commit", "-q", "-m", "Start projektu (D-01)")
        if r.returncode != 0:
            failures.append("pierwszy commit nowego projektu został odrzucony:\n" + r.stdout + r.stderr)
        if git2("tag").stdout.strip():
            failures.append("nowy projekt ma tagi szablonu")

    # D-71, D-73: kryteria odbioru zadania nie dają W4, a rekord postępu pokazuje je w osobnej sekcji
    failures.case("acceptance-criteria")
    with tempfile.TemporaryDirectory() as tmpdir:
        prepare(tmpdir)
        r = run_py(tmpdir, "process/tools/progress.py")
        if "## Kryteria odbioru" in open(os.path.join(tmpdir, "reports", "progress.md"), encoding="utf-8").read():
            failures.append("sekcja kryteriów odbioru bez kryteriów")
        plan = os.path.join(tmpdir, "project", "plan.md")
        text = open(plan, encoding="utf-8").read()
        assert "- status: in_progress\n" in text
        open(plan, "w", encoding="utf-8").write(text.replace("- status: in_progress\n", "- status: in_progress\n- acceptance_criteria: wymagania bez błędów śladu\n", 1))
        r = run_py(tmpdir, "process/tools/trace.py", os.devnull)
        if "W4 TSK-01" in r.stdout:
            failures.append("pole acceptance_criteria zadania dało W4:\n" + r.stdout)
        run_py(tmpdir, "process/tools/progress.py")
        progress = open(os.path.join(tmpdir, "reports", "progress.md"), encoding="utf-8").read()
        if "## Kryteria odbioru" not in progress or "| TSK-01 Napisać przypadki i wymagania | wymagania bez błędów śladu |" not in progress:
            failures.append("rekord postępu nie pokazuje kryteriów odbioru zadania:\n" + progress[-600:])

    for p in failures:
        print("NIE:", p)
    for name, ok in failures.cases.items():
        print(f"CASE {name}: {'pass' if ok else 'fail'}")
    print(f"test_tools: {len(BREAKAGES)} psuć, {len(WARNINGS)} ostrzeżeń, E9 (7 przypadków), postęp, init, start projektu, hooki commit-msg i pre-commit — {'OK' if not failures else f'{len(failures)} porażek'}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
