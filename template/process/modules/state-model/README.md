# Moduł: model stanów (w przygotowaniu)

Maszyna stanów najważniejszego obiektu dziedziny (np. elementu, zamówienia) w Mermaid `stateDiagram-v2`. To najczęściej pomijany model: z przejść wynikają wymagania EARS „event” (When …), z zachowania w stanie „state” (While …), a ze strażników „unwanted” (If …, then …).

Status: opis i konwencja są gotowe; skrypt sprawdzający jeszcze nie istnieje.

Konwencja:
- stany i przejścia w pliku `states.mmd`,
- każde przejście ma komentarz `%% transition <Z> -> <Do>: OBS-nn`, a każdy stan `%% state <Nazwa>: OBS-nn`.

Planowana kontrola: każdy stan i każde przejście wskazuje co najmniej jedno istniejące wymaganie; stany nieosiągalne i bez wyjścia są błędem (podobnie jak R1–R2 w module nawigacji).
