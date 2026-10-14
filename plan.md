# Plan projektu

Część zarządcza planu (D-08), wzorowana na ISO/IEC 29110-5-1-2 WP.10: co powstaje, po co i kiedy. Jak pracujemy (ślad, zmiany, rola agenta) opisuje AGENTS.md. Cele, kamienie milowe, zadania i ryzyka projektu mają ID (D-09), więc ślad i rekord postępu (postep.md, generowany) widzą plan tak samo jak specyfikację.

Plan zmienia się jak każdy artefakt: edycja, przegląd diffu, commit z ID. Zmiana celu albo terminu kamienia wymaga decyzji D-nn.

## Produkt i zakres
Uzupełnij: jaki system, dla kogo, po co (cel produktu i najważniejsze potrzeby Użytkownika). Zakres szczegółowo: zakres.md (In/Out). Szablon zakłada etap specyfikacji, bez kodu i bez certyfikacji; plan kolejnego etapu pisze się, gdy do niego dojdziemy.

## Cykl wytwarzania
Uzupełnij, np.: przyrostowo, fala po fali według AGENTS.md („Kolejność wdrażania praktyk”); każdy kamień milowy kończy się baseline'em.

## Zespół i zasoby
Uzupełnij: kto (Użytkownik, agent), ile czasu tygodniowo, narzędzia (git, python3, agent LLM).

## Wersjonowanie i dostarczenie
- repozytorium: git, jedyne źródło prawdy (P-01); lokalizacja: uzupełnij
- wersje: commity z ID (P-07); baseline'y: tagi `baseline-nn-nazwa` przypisane do kamieni milowych (pole `tag:`)
- kopia zapasowa i odtwarzanie (WP.12): uzupełnij
- dostarczenie: uzupełnij, co i w jakiej postaci otrzymuje odbiorca

## Cele
Mierzalne cele projektu. Kamień milowy wskazuje cel (`cel:`).

```
### CEL-nn Tytuł celu
- miara: po czym poznamy, że cel jest osiągnięty
```

## Kamienie milowe
Kamień milowy kończy się baseline'em: gdy w repozytorium jest tag z pola `tag:`, postep.md pokazuje kamień jako osiągnięty z datą tagu. Akceptację odbiorcy zapisuje rekord AKC w rekordy.md.

```
### KM-nn Tytuł kamienia
- cel: CEL-nn
- termin: RRRR-MM-DD
- tag: baseline-nn-nazwa
- kryteria akceptacji: co musi być spełnione
```

## Zadania
Zadanie wskazuje kamień (`kamień:`) i to, co wytwarza (`produkuje:`): kody typów (np. `UC, WYM`) albo konkretne ID. `produkuje:` jest jedynym polem wskazującym w dół, jawnym wyjątkiem od P-03 (D-09). Weryfikacje, walidacje i przeglądy też są zadaniami.

```
### ZAD-nn Tytuł zadania
- kamień: KM-nn
- produkuje: UC, WYM
- status: planowane | w toku | zakończone
- termin: RRRR-MM-DD
- zakończono: RRRR-MM-DD
- odchylenie: opcjonalnie, dlaczego inaczej niż w planie
```

## Ryzyka projektu
Ryzyka dla terminu, zakresu albo zasobów projektu. Ryzyka produktu (co może pójść źle u Użytkownika) są w module ryzyk (RYZ-nn).

```
### RP-nn Tytuł ryzyka
- dotyczy: CEL-nn, KM-nn albo ZAD-nn (opcjonalnie)
- status: otwarte | zamknięte
- działanie: jak ograniczamy
```
