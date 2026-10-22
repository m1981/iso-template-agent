# Zakres

Granice systemu, ustalane przed przypadkami użycia (najtańsza decyzja w projekcie). Pozycja In wskazuje przypadki, które ją realizują (przypadek podaje ją w polu `scope:`). Pozycja Out może być źródłem wymagania-ograniczenia (np. „system nie powiadamia osób spoza systemu”).

Format:

```
### IO-nn Temat
- kind: In | Out
- rationale: dlaczego w zakresie albo poza nim
- release: 1.0 (dla Out: kiedy wraca, jeśli w ogóle)
- status: initiated
```

## Pozycje

Brak pozycji.

## Aktorzy i cele

Poziomy celu według Cockburna: cloud (cel nadrzędny), kite (zbiorczy), sea (cel użytkownika, jedna sesja), fish (podfunkcja). Każdy cel na poziomie morza i latawca ma przypadek użycia.

| Aktor | Cel | Poziom | Przypadek |
| --- | --- | --- | --- |
| (aktor główny) | (cel zwykłymi słowami) | sea | (UC-nn) |

Aktorzy wspierający (inne systemy) i aktorzy poza sceną (osoby, których interes się liczy, ale nie korzystają z systemu) też trafiają do słownika.
