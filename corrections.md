# Korekty

Rejestr korekt (ISO/IEC 29110-5-1-2 WP.04, correction register): działania naprawiające odchylenie od planu albo usterkę znalezioną w weryfikacji, walidacji lub akceptacji. Korekta wskazuje przyczynę w polu `cause:` (P-03); progress.md pokazuje korekty niezakończone. Stany wprost z normy: initiated, approved, completed.

Format:

```
### COR-nn Tytuł problemu
- cause: TSK-nn, MS-nn, PRK-nn, VER-nn, VAL-nn albo ACC-nn
- action: co robimy
- by: kto odpowiada
- opened: RRRR-MM-DD
- due: RRRR-MM-DD
- status: initiated | approved | completed
```

Brak korekt.
