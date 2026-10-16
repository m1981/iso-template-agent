# Plan projektu

Część zarządcza planu, wzorowana na ISO/IEC 29110-5-1-2 WP.10: co powstaje, po co i kiedy. Jak pracujemy (ślad, zmiany, rola agenta) opisuje AGENTS.md. Cele, kamienie milowe, zadania i ryzyka projektu mają ID, więc ślad i rekord postępu (progress.md, generowany) widzą plan tak samo jak specyfikację.

Plan zmienia się jak każdy artefakt: edycja, przegląd diffu, commit z ID. Zmiana celu albo terminu kamienia wymaga decyzji D-nn.

## Produkt i zakres
Uzupełnij: jaki system, dla kogo, po co (cel produktu i najważniejsze potrzeby Użytkownika). Zakres szczegółowo: scope.md (In/Out). Szablon zakłada etap specyfikacji, bez kodu i bez certyfikacji; plan kolejnego etapu pisze się, gdy do niego dojdziemy.

## Cykl wytwarzania
Uzupełnij, np.: przyrostowo, fala po fali według AGENTS.md („Kolejność wdrażania praktyk”); każdy kamień milowy kończy się baseline'em.

## Zespół i zasoby
Uzupełnij: kto (Użytkownik, agent), ile czasu tygodniowo, narzędzia (git, python3, agent LLM).

## Wersjonowanie i dostarczenie
- repozytorium: git, jedyne źródło prawdy (P-01); lokalizacja: uzupełnij
- wersje: commity z ID (P-07); baseline'y: tagi `baseline-nn-nazwa` przypisane do kamieni milowych (pole `tag:`)
- kopia zapasowa i odtwarzanie (WP.12): drugi remote, np. prywatne repozytorium na GitHubie (uzupełnij adres); push z tagami (`make hooks` ustawia push.followTags); odtworzenie = `git clone`
- dostarczenie: uzupełnij, co i w jakiej postaci otrzymuje odbiorca

## Cele
Mierzalne cele projektu. Kamień milowy wskazuje cel (`objective:`).

```
### OBJ-nn Tytuł celu
- measure: po czym poznamy, że cel jest osiągnięty
```

## Kamienie milowe
Kamień milowy kończy się baseline'em: gdy w repozytorium jest tag z pola `tag:`, progress.md pokazuje kamień jako osiągnięty z datą tagu. Akceptację odbiorcy zapisuje rekord ACC w acceptance.md.

```
### MS-nn Tytuł kamienia
- objective: OBJ-nn
- due: RRRR-MM-DD
- tag: baseline-nn-nazwa
- acceptance_criteria: co musi być spełnione
```

## Zadania
Zadanie wskazuje kamień (`milestone:`) i to, co wytwarza (`produces:`): kody typów (np. `UC, REQ`) albo konkretne ID. `produces:` jest jedynym polem wskazującym w dół, jawnym wyjątkiem od P-03. Weryfikacje, walidacje i przeglądy też są zadaniami.

```
### TSK-nn Tytuł zadania
- milestone: MS-nn
- produces: UC, REQ
- status: planned | in_progress | completed
- due: RRRR-MM-DD
- completed: RRRR-MM-DD
- deviation: opcjonalnie, dlaczego inaczej niż w planie
```

## Ryzyka projektu
Ryzyka dla terminu, zakresu albo zasobów projektu. Ryzyka produktu (co może pójść źle u Użytkownika) są w module ryzyk (RSK-nn).

```
### PRK-nn Tytuł ryzyka
- concerns: OBJ-nn, MS-nn albo TSK-nn (opcjonalnie)
- status: open | closed
- mitigation: jak ograniczamy
```
