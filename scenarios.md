# Scenki użytkownika

Opowieści o tym, jak konkretna osoba używa systemu w swoim życiu lub pracy. Scenka jest korzeniem śladu: z niej wynikają cele (przypadki użycia) i służy jako test akceptacyjny listy aktor–cel. Każde zdanie scenki powinno wskazywać jakiś cel albo interes, a każdy cel powinien mieć oparcie w jakiejś scence. Gdy odwzorowanie nie działa w którąś stronę, jest luka albo nadmiar.

Przypadek użycia wskazuje scenkę w polu `scenarios:`; trace.py ostrzega o scence, z której nie wynika żaden przypadek (W1).

Format:

```
### SC-nn Kto, w jakiej sytuacji
- person: kim jest, co robi, czego potrzebuje
- interests: czego oczekuje od systemu (np. „nic mi nie umyka”)
- content: kilka akapitów narracji w pierwszej osobie albo w trzeciej
- status: initiated
```

Brak scenek.
