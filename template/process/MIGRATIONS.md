# Migracje dokumentów projektu

Copier aktualizuje narzędzia, normy i wzorce. Dostosowanie istniejących dokumentów projektu wymaga jawnie opisanej migracji i osobnego kroku; aktualizacja pakietu nie oznacza zakończenia migracji (szablon D-51).

Format wpisu:

```
## M-nn Tytuł (od wersji vX.Y.Z)
- reguła: co się zmieniło w procesie
- dotyczy: dokumenty nowe / w toku / zakończone
- jak znaleźć: kody błędów i ostrzeżeń trace.py albo polecenie
- kroki: co zrobić w dokumentach
- koniec: warunek zakończenia; projekt zapisuje decyzję i ustawia migrated_to w project/settings.toml
```

Brak migracji. Projekty założone przed pierwszym wydaniem (płaski układ szablonu) nie są aktualizowane przez copier; ich przejście opisze osobny wpis przy pierwszym takim projekcie.
