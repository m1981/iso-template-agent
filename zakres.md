# Zakres

Granice systemu, ustalane przed przypadkami użycia (najtańsza decyzja w projekcie). Pozycja In wskazuje przypadki, które ją realizują (przypadek podaje ją w polu `zakres:`). Pozycja Out może być źródłem wymagania-ograniczenia (np. „system nie powiadamia osób spoza systemu”).

Format:

```
### IO-nn Temat
- rodzaj: In | Out
- uzasadnienie: dlaczego w zakresie albo poza nim
- wersja: 1.0 (dla Out: kiedy wraca, jeśli w ogóle)
```

## Pozycje

Brak pozycji.

## Aktorzy i cele

Poziomy celu według Cockburna: chmura (cel nadrzędny), latawiec (zbiorczy), morze (cel użytkownika, jedna sesja), ryba (podfunkcja). Każdy cel na poziomie morza i latawca ma przypadek użycia.

| Aktor | Cel | Poziom | Przypadek |
| --- | --- | --- | --- |
| (aktor główny) | (cel zwykłymi słowami) | morze | (UC-nn) |

Aktorzy wspierający (inne systemy) i aktorzy poza sceną (osoby, których interes się liczy, ale nie korzystają z systemu) też trafiają do słownika.
