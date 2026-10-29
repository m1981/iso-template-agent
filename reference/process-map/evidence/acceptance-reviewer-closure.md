**R1 i R2 są zamknięte w rewizji 2 na poziomie specyfikacji.**

- **R1:** §6 wymaga wskazania aktualnego aktywnego zgłoszenia jako poprzednika; końcowy lub inny ID daje `CONFLICT`. Sprawdzenie i zapis obejmują atomowo cały przyrost. INV7 oraz S21–S22 obejmują wcześniejszy kontrprzykład i konkurencyjne zgłoszenia.
- **R2:** §7 rozdziela różne żądania od identycznych ponowień. Wspólny klucz i treść oznaczają jedno logiczne wykonanie oraz jeden wynik końcowy; `IN_PROGRESS` jest przejściowy i nie utrwala drugiej odmowy. S23 obejmuje równoczesne ponowienie oraz utratę odpowiedzi.
- **Odrzucenie przy niedostępnym źródle:** §6 i S14 jednoznacznie pozwalają odczytać zachowane zgłoszenie z tokenem i wykonać `reject` przy `unknown`, bez spełnienia G. Osobno wskazano awarię magazynu procesu, która uniemożliwia wiarygodny zapis.

Nie znalazłem pozostałej sprzeczności w tych poprawkach. Czytałem wyłącznie kontrakt, bez raportu rozliczenia autora; nie zmieniałem plików. To kontrola zamknięcia wskazanych uwag, nie pełny odbiór kontraktu ani potwierdzenie działania implementacji.
