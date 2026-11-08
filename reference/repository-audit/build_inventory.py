"""Snapshot audit, not a process gate. Run from anywhere; only reads Git objects.

python3 reference/repository-audit/build_inventory.py --output /tmp/inventory.tsv
Classifications describe ca8f336. Do not reuse them for a new revision without review.
"""
import argparse
import csv
import json
import subprocess
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = 'ca8f336'


def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args], text=True)


def classify(p):
    """Goal, role, authority, currency, maintenance; family classification, not proof."""
    if p.startswith('template/'):
        goal = 'G1-pakiet-procesu'
        if '/templates/' in p or p.endswith('.jinja'):
            return goal, 'wzorzec', 'wzorzec-nie-fakt-projektu', 'w-dystrybucji', 'utrzymac; zmiany podlegaja testom dystrybucji'
        if p.endswith(('.py', '.toml', '.mk', '.html')) or '/hooks/' in p:
            return goal, 'implementacja-konfiguracja', 'mechanizm-nie-tekst-ISO', 'w-dystrybucji', 'utrzymac; testowac zgodnie z obszarem'
        return goal, 'instrukcja-pakietu', 'regula-lokalna-w-zakresie', 'w-dystrybucji; wyjatki lokalne w decyzjach', 'utrzymac; nie oznacza egzekwowania kazdego zdania'
    if p.startswith('reference/golden/'):
        return 'G2-rozwoj-szablonu', 'fixture', 'oczekiwanie-testu', 'uzywane-przez-golden_master', 'utrzymac; nie archiwizowac tylko z powodu wieku'
    if p.startswith('reference/tdd/') or p == 'reference/layout-map.md':
        return 'G2-rozwoj-szablonu', 'dowod-lub-plan-migracji', 'zapis-historyczny', 'historyczne-dla-okreslonej-zmiany', 'zachowac; zaleznosci test_move przed przeniesieniem'
    if p.startswith('archive/'):
        return 'G8-archiwum', 'archiwum', 'zapis-historyczny', 'historyczne', 'poza codzienna lektura; sprawdzic test_move przed usunieciem'
    if p.startswith('reference/vcs-lite-interview/'):
        return 'G7-wywiad-vcs-lite', 'analiza-lub-material-wywiadu', 'informacyjne', 'historyczne; nie dowodzi przyczyn sukcesu', 'zachowac; czytac najpierw README i findings'
    if p.startswith('reference/process-simulator/'):
        goal='G4-lekcja-L1'
    elif p.startswith('reference/process-map/flowable-trial/'):
        goal='G6-eksperyment-Flowable'
    elif p.startswith('reference/process-modeling/'):
        goal='G5-modelowanie-i-koordynacja'
    elif p.startswith('reference/process-map/'):
        goal='G5-modelowanie-i-koordynacja'
    elif p.startswith(('reference/planning-examples/', 'reference/repository-evolution/')):
        return 'G3-edukacja-i-propozycje', 'przyklad-dydaktyczny', 'informacyjne-nie-decyzja', 'fikcyjny-przyklad', 'zachowac do nauki; poza mapa codziennej pracy'
    elif p.startswith('reference/'):
        return 'G3-edukacja-i-propozycje', 'analiza-propozycja-lub-transkrypt', 'informacyjne', 'datowane; nie aktywuje praktyki', 'lektura na zadanie; ponownie ocenic przed wdrozeniem'
    else:
        goal='G2-rozwoj-szablonu'
    if '/evidence/' in p:
        return goal, 'dowod-w-zakresie-proby', 'zapis-wykonania-nie-odbior', 'historyczne-dla-opisanej-wersji', 'zachowac z raportem; nie nadpisywac nowym wynikiem'
    if p.startswith('reports/'):
        return goal, 'raport-generowany', 'widok-pochodny', 'sprawdzic-date-i-podstawe; nie stan calego-repo', 'generowac narzedziem; nie poprawiac recznie'
    if p.startswith('records/'):
        return goal, 'rejestr-lub-jego-format', 'rekord-nie-domyslne-zatwierdzenie', 'sprawdzac konkretne wpisy', 'utrzymac; pusty format nie dowodzi wykonania'
    if p.startswith('spec/'):
        return goal, 'specyfikacja-lub-kryteria', 'lokalna-specyfikacja-w-zakresie', 'podstawa-szablonu; statusy oceniac osobno', 'utrzymac razem z decyzjami i testami'
    if '/tests/' in p or p.startswith('tests/') or '/src/test/' in p:
        return goal, 'test', 'wykonywalne-oczekiwanie', 'wersja-na-bazowym-commicie; bez nowej regresji', 'utrzymac z implementacja'
    if p.endswith(('.py', '.java', '.xml', '.dmn', '.bpmn', '.bpmn20.xml', '.toml', '.js', '.css', '.properties')) or Path(p).name in ('Makefile', 'verify', 'resume-demo', 'show-card', 'mvnw', 'mvnw.cmd', 'setup-jdk') or Path(p).name.startswith(('verify-', 'replay-')):
        return goal, 'implementacja-lub-konfiguracja', 'realizacja-nie-tekst-ISO', 'wersja-na-bazowym-commicie; bez nowej regresji', 'utrzymac w granicach danego eksperymentu'
    if p.endswith(('.svg', '.png', '.html')):
        return goal, 'widok-lub-render', 'informacyjne-pochodne', 'sprawdzic zgodnosc ze zrodlem', 'poza lektura tekstowa; nie usuwac bez sprawdzenia linkow'
    if p.endswith(('.dot', '.mmd')):
        return goal, 'zrodlo-diagramu', 'informacyjne', 'zakres i data diagramu', 'utrzymac razem z renderem'
    if p.endswith('.md'):
        return goal, 'dokumentacja', 'informacyjne', 'mieszane; ocena tresci przy uzyciu', 'czytac wedlug mapy celu'
    return goal, 'konfiguracja-lub-zasob', 'pomocnicze', 'wersja-na-bazowym-commicie', 'zachowac; potrzeba zalezy od wykonawcy'


# Explicit exceptions: directory does not establish authority.
OVERRIDES = {
 'template/process/modules/state-model/README.md': ('konwencja-modulu', 'instrukcja-opcjonalna', 'brak-skryptu-sprawdzajacego-Q09', 'nie przedstawia mechanicznego egzekwowania'),
 'reference/vcs-lite-interview/run-round.py': ('narzedzie-wywiadu', 'implementacja-badania', 'historyczna-proba; uruchomienie CLI nie zlecone', 'zachowac do odtworzenia metody; nie uruchamiac automatycznie'),
 'AGENTS.md': ('instrukcja', 'regula-lokalna', 'aktywny-punkt-wejscia', 'utrzymac'),
 'CLAUDE.md': ('instrukcja', 'regula-lokalna', 'aktywny-punkt-wejscia', 'utrzymac'),
 'README.md': ('nawigacja', 'informacyjne', 'niepelna-mapa-po-rozszerzeniu-repo', 'uzupelnic odnosniki, nie powielac planu'),
 'project/plan.md': ('plan-szablonu', 'plan-w-zakresie-D48', 'mieszane; stary make process-kit', 'naprawic nawigacje; nie mylic z A-planem laboratorium'),
 'project/decisions.md': ('rejestr-decyzji', 'decyzje-U-w-zakresie', 'aktywne-i-historyczne; czytac statusy', 'utrzymac; nie traktowac propozycji jako zgody'),
 'reports/test-report.md': ('raport-testow', 'zapis-historycznego-wykonania', '2026-10-22-b866213-dirty', 'zachowac; nie przedstawia obecnej regresji'),
 'reference/process-simulator/collaboration.md': ('kontrakt-wspolpracy', 'regula-lokalna-D78', 'aktywny-w-zakresie; parametry I1 historyczne', 'uwidocznic wyjatek w nawigacji'),
 'reference/process-simulator/progress.md': ('dziennik-laboratorium', 'zapis-historyczny-z-odeslaniem', 'mieszane; biezacy plan w coverage-map', 'czytac do odtworzenia zdarzen, nie jako drugi plan'),
 'reference/process-modeling/brief.md': ('punkt-wznowienia-i-brief', 'biezacy-punkt-wejscia-D87', 'punkt-wznowienia aktywny; reszta datowana', 'czytac poczatek; dawne propozycje nie sa zleceniem'),
 'reference/process-modeling/coverage-map.md': ('plan-rejestr-i-analizy', '8.7-plan-8.8-rejestr; reszta-w-swoim-zakresie', 'mieszane; stary naglowek F5-niezlecone', 'uzywac 8.7-8.8; oznaczyc dawny skrot'),
 'reference/process-modeling/work-card.md': ('karta-pracy', 'zakres-D83; nie nowe upowaznienie', 'historyczna-podstawa; pozniejsze D94-99 rozszerzaja prace', 'czytac z decyzjami, nie jako aktualny zakaz eksperymentu'),
 'reference/process-modeling/acceptance.md': ('propozycja-kryteriow', 'propozycja-z-mapowaniem-8.5', 'nie samodzielna bramka calego modelu', 'czytac z coverage-map 8.5'),
 'reference/process-map/README.md': ('indeks-map', 'informacyjne', 'nie obejmuje wszystkich pozniejszych dostaw', 'uzupelnic nawigacje'),
 'reference/process-map/flowable-trial/README.md': ('instrukcja-eksperymentu', 'techniczne-w-zakresie-F1-F5', 'mieszane; poczatek F4, dalsze F5 i karta', 'wyrownac opis aktualnego zakresu'),
 'reference/process-map/flowable-trial/architecture.md': ('architektura-eksperymentu', 'informacyjne', 'F4-z-aktualizacja-F5; nie pelna mapa nowego formattera', 'odswiezyc przy kolejnej zmianie architektury'),
 'reference/process-map/operator-preview/textstats-card-data-map.md': ('mapa-pol-karty', 'kontrakt-lokalny-karty-w-zakresie-zlecenia', 'aktualne-dla-archiwalnych-eksportow-F5', 'utrzymac z formatterem; nie utozsamiac z API'),
 'reference/vcs-lite-interview/remaining-rounds.md': ('dawny-plan-wywiadu', 'historyczne', 'zrealizowane; nie kolejka', 'zachowac historyczny status'),
 'CHANGELOG.md': ('historia-wydan', 'rejestr-wydan', 'Niewydane; brak tagu v1', 'nie utozsamiac baseline z wydaniem'),
}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args=parser.parse_args()
    # Reverse chronological application with rename detection; lineages are heuristic.
    history={}
    commits=git('rev-list', '--reverse', BASE).splitlines()
    for commit in commits:
        date=git('show', '-s', '--format=%cs', commit).strip()
        changes=git('diff-tree', '--root', '--no-commit-id', '--name-status', '-r', '-M', commit)
        for line in changes.splitlines():
            fields=line.split('\t'); status=fields[0]; path=fields[-1]
            if status.startswith('R'):
                item=history.pop(fields[1])
                item['path_since']=commit[:7]
                history[path]=item
            elif status == 'D':
                history.pop(path, None)
                continue
            elif path not in history:
                history[path]={'first_commit':commit[:7], 'first_date':date,
                               'origin_path':path, 'path_since':commit[:7]}
            history[path].update(last_commit=commit[:7], last_date=date)
    paths=git('ls-tree', '-r', '--name-only', BASE).splitlines()
    assert set(paths)==set(history), 'History and tree mismatch'
    rows=[]
    for p in paths:
        goal,role,authority,currency,keep=classify(p)
        basis='klasyfikacja-funkcji-katalogu-i-typu; bez pelnego audytu tresci'
        if p in OVERRIDES:
            role,authority,currency,keep=OVERRIDES[p]
            basis='odczyt tresci/punktu wejscia i odniesien; nie pelny audyt semantyczny'
        rows.append(dict(path=p, goal=goal, role=role, authority=authority,
                         currency=currency, maintenance=keep, basis=basis, **history[p]))
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('w',newline='',encoding='utf-8') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t',lineterminator='\n')
        writer.writeheader(); writer.writerows(rows)
    duplicates=defaultdict(list)
    for entry in git('ls-tree','-r',BASE).splitlines():
        meta,path=entry.split('\t',1)
        duplicates[meta.split()[2]].append(path)
    groups=[v for v in duplicates.values() if len(v)>1]
    milestones=[]
    for rev in ['716abb6','11ddded','12acb1d','e63c8da','5471272','0a988e4','8849a3b','8fa127b','16f5ff8',BASE]:
        items=git('ls-tree','-r','--name-only',rev).splitlines()
        milestones.append(dict(commit=rev,date=git('show','-s','--format=%cs',rev).strip(),files=len(items),md=sum(p.endswith('.md') for p in items)))
    print(json.dumps(dict(base=git('rev-parse',BASE).strip(),commits=len(commits),files=len(rows),
        markdown=sum(p.endswith('.md') for p in paths),goals=dict(Counter(r['goal'] for r in rows)),
        duplicates=groups,milestones=milestones),ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()
