# Lab 7 - Natalia Biernacka 331665

# Zadanie 1 - SQL Injection

## Podatność 
**`app.py`, funkcja `sekret` - klucz od użytkownika jest sklejany ze stringiem zapytania w wierszu 21:**
`"... WHERE klucz = '" + klucz + "'"`.

## Pięć wejść i liczba zwróconych wierszy:

| # | Wejście (klucz) | Wierszy |
|---|---|---|
| 1 | `1234` | 1 |
| 2 | `'` | 0 (OperationalError: unrecognized token: "'''") |
| 3 | `' OR '1'='1` | 4 (wszystkie) |
| 4 | `' UNION SELECT name, sql FROM sqlite_master --` | 2 (spis tabel - konta, sekrety) |
| 5 | `' UNION SELECT login, rola \|\| ':' \|\| email FROM konta --` | 2 (dane dla admin i anna) |

## Zapytanie po wstawieniu danych (wejście nr 3):
```
SELECT wlasciciel, sekret FROM sekrety WHERE klucz = '' OR '1'='1'
```

## Nazwy tabel i kolumn drugiej tabeli:
tabele `sekrety` i `konta`

druga tabela `konta(login, rola, email)`


## Jak wejście zmieniło strukturę zapytania:
Apostrof zamknął napis
 z kluczem wcześniej, niż zakładał programista, a reszta wejścia (`OR`, `UNION`) została wykonana jako składnia SQL, nie jako dane od użytkownika

---

# Zadanie 2 - Zapytanie z parametrami

## Poprawka (fragment kodu):
```python
zapytanie = "SELECT wlasciciel, sekret FROM sekrety WHERE klucz = ?"
wiersze, blad = [], None
try:
    with sqlite3.connect(BAZA, uri=True) as db:
        wiersze = db.execute(zapytanie, (klucz,)).fetchall()
except sqlite3.Error as exc:
        blad = f"{type(exc).__name__}: {exc}"
        app.logger.exception(blad)
        blad = "Nieprawidłowe dane"
```

## Sześć wejść — przed i po poprawce:

| Wejście (klucz) | Wierszy przed | Wierszy po |
|---|---|---|
| `1234` | 1 | 1 |
| `'` | 0 (błąd SQLite) | 0 - brak klucza któy jest apostrofem |
| `' OR '1'='1` | 4 | 0 |
| `' UNION SELECT name, sql FROM sqlite_master --` | 2 | 0 |
| `' UNION SELECT login, rola \|\| ':' \|\| email FROM konta --` | 2 | 0 |
| `d'Artagnan` | 0 (błąd przez apostrof) | 1 |

## Dlaczego wartość parametru nie zmienia struktury zapytania:
 treść zapytania jest kompilowana zanim baza pozna wartość; wartość jest przekazana osobno i tylko porównywana z zawartością kolumny, więc jej znaki (apostrof, `OR`, `--`) nie są interpretowane jako składnia.

## Czy parametr zastąpi nazwę tabeli:

nie - `?` działa tylko dla wartości - stały napis. Np. przy ORDER BY ? nie możemy podstawić kolumny wlasciciel, ponieważ zinterpretowane zostanie to jako dosłowna wartość "wlasciciel", a sortowanie po stałym napisie niczego nie zmienia

---

# Zadanie 3 - Code Injection w kalkulatorze

## Podatność:
`app.py`, funkcja `kalkulator` - `eval(wyrazenie)` wykonuje dowolne wyrażenie Pythona

## Trzy wyrażenia z kroku 2 (skrócone wyniki):

| Wyrażenie | Skrócony wynik |
|---|---|
| `__import__('os').listdir('/etc')` | lista plików `/etc` (m.in. `os-release`, `passwd`) |
| `open('/etc/os-release').read()` | NAME="Alpine Linux" ID=alpine VERSION_ID=3.24.4 ... |
| `__import__('os').getuid()` | 1000 |


## Testy po poprawce:

| Wejście | Kod HTTP | Wynik |
|---|---|---|
| `2+3` | 200 | 5.0 |
| `7 / 2` | 200 | 3.5 |
| `-1.5*4` | 200 | -6.0 |
| `1/0` | 400 | Dzielenie przez zero |
| `__import__('os').listdir('/etc')` | 400 | Nieprawidłowe dane |
| `open('/etc/os-release').read()` | 400 | Nieprawidłowe dane |
| `__import__('os').getuid()` | 400 | Nieprawidłowe dane |
| (puste `?wyrazenie=`) | 400 | Nieprawidłowe dane |

## Dlaczego lista dozwolonych operacji jest lepsza niż blokowanie słów:
Lista dozwolonych operacji przepuszcza tylko znany, poprawny format (liczba, operator, liczba), więc nie da się przemycić niczego nieprzewidzianego. Blokowanie słów takich jak `import` zawodzi, bo np. `open('/etc/os-release').read()` nie zawiera słowa `import`, a i tak czyta plik

---
