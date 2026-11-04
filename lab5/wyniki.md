# Zadanie 1.

| adres                      | kod HTTP przed | kod HTTP po   |
|----------------------------|----------------|---------------|
| GET /materialy/            | 200 OK         | 403 Forbidden |
| GET /materialy/notatka.txt | 200 OK         | 200 OK        |
| GET /wewnetrzne/           | 200 OK         | 403 Forbidden |
| GET /wewnetrzne/plan.txt   | 200 OK         | 403 Forbidden |


## Logi przed zmianami
web-1  | 172.18.0.1 - - [04/Nov/2026:11:25:47 +0000] "GET /materialy/ HTTP/1.1" 200 305
web-1  | 172.18.0.1 - - [04/Nov/2026:11:27:43 +0000] "GET /materialy/notatka.txt HTTP/1.1" 200 69
web-1  | 172.18.0.1 - - [04/Nov/2026:11:28:18 +0000] "GET /wewnetrzne/ HTTP/1.1" 200 301
web-1  | 172.18.0.1 - - [04/Nov/2026:11:29:54 +0000] "GET /wewnetrzne/plan.txt HTTP/1.1" 200 58


http://127.0.0.1:8080/materialy/
HTTP/1.1 200 OK
Widoczna jest lista: 
- Parent directory
- notatka.txt

http://127.0.0.1:8080/wewnetrzne/
HTTP/1.1 200 OK
Widoczna jest lista:
- Parent directory
- plan.txt

## Logi po zmianach
web-1  | 172.18.0.1 - - [04/Nov/2026:11:41:56 +0000] "GET /wewnetrzne/plan.txt HTTP/1.1" 403 239
web-1  | [Wed Nov 04 11:42:01.373482 2026] [authz_core:error] [pid 16:tid 48] [client 172.18.0.1:52906] AH01630: client denied by server configuration: /usr/local/apache2/htdocs/wewnetrzne/

web-1  | 172.18.0.1 - - [04/Nov/2026:11:42:01 +0000] "GET /wewnetrzne/ HTTP/1.1" 403 239
web-1  | [Wed Nov 04 11:42:13.671332 2026] [autoindex:error] [pid 93:tid 99] [client 172.18.0.1:36646] AH01276: Cannot serve directory /usr/local/apache2/htdocs/materialy/: No matching DirectoryIndex (index.html) found, and server-generated directory index forbidden by Options directive

web-1  | 172.18.0.1 - - [04/Nov/2026:11:42:13 +0000] "GET /materialy/ HTTP/1.1" 403 239

web-1  | 172.18.0.1 - - [04/Nov/2026:11:42:20 +0000] "GET /materialy/notatka.txt HTTP/1.1" 200 69


## Wniosek:
Wyłączenie listowania katalogu uniemożliwia wyświetlenie jego zawartości, ale nie blokuje dostępu do plików po podaniu ich pełnego adresu URL (jak w przypadku notatka.txt)
Blokada dostępu poprzez "Require all denied" blokuje natomiast cały dostęp HTTP do katalogu i jego zawartości (jak w przypadku plan.txt)


# Zadanie 2.

| test             | kod HTTP         |
|------------------|------------------|
| Bez logowania    | 401 Unauthorized |
| Błędne hasło     | 401 Unauthorized |
| Poprawne hasło   | 200 OK           |
| Publiczna strona | 200 OK           |

## Bez logowania
curl.exe -i http://127.0.0.1:8080/panel/raport.txt
HTTP/1.1 401 Unauthorized
Date: Wed, 04 Nov 2026 11:52:00 GMT
Server: Apache
**WWW-Authenticate: Basic realm="Laboratorium 5"**

## Logi
web-1  | 172.18.0.1 - - [04/Nov/2026:11:52:00 +0000] "GET /panel/raport.txt HTTP/1.1" 401 421
web-1  | [Wed Nov 04 11:54:25.092918 2026] [auth_basic:error] [pid 10:tid 21] [client 172.18.0.1:50684] AH01617: user student: authentication failure for "/panel/raport.txt": Password Mismatch
web-1  | 172.18.0.1 - student [04/Nov/2026:11:54:25 +0000] "GET /panel/raport.txt HTTP/1.1" 401 421
web-1  | 172.18.0.1 - student [04/Nov/2026:11:55:16 +0000] "GET /panel/raport.txt HTTP/1.1" 200 58
web-1  | 172.18.0.1 - - [04/Nov/2026:11:56:48 +0000] "GET / HTTP/1.1" 200 351

## Wnioski:
HTTP Basic koduje dane logowania za pomocą Base64, ale nie szyfruje ich. Dlatego przy zwykłym HTTP dane mogą zostać przechwycone podczas transmisji


# Zadanie 3.

## Wynik skryptu
curl.exe -i http://127.0.0.1:8080/cgi-bin/uprawnienia.cgi
HTTP/1.1 200 OK
Date: Wed, 04 Nov 2026 12:11:10 GMT
Server: Apache
Transfer-Encoding: chunked
Content-Type: text/plain; charset=utf-8

Efektywny UID: 2
Efektywny GID: 2

ODCZYT PLIKOW:

Plik: /lab-data/ogolny.txt
Wynik: odczyt udany
Treść:
LAB05: dokument dostepny dla grupy procesu WWW.


Plik: /lab-data/poufny.txt
Wynik: odmowa dostępu do pliku


## Prawa plików
docker compose exec web ls -ln /lab-data/
total 8
-rw-r-----    1 0        2               48 Nov  3 18:55 ogolny.txt
-rw-------    1 0        2               61 Nov  3 18:55 poufny.txt

ogolny.txt - właściciel ma odczyt i zapis, grupa ma odczyt, pozostali nie posiadają dostępu
poufny - właściciel ma odczyt i zapis

Proces CGI działa z efektywnym UID = 2 oraz GID = 2. Oba pliki należą do właściciela o UID = 0 i grupy o GID = 2. Plik ogolny.txt posiada uprawnienia 640, dzięki czemu proces CGI może go odczytać na podstawie uprawnień grupy. Plik poufny.txt posiada uprawnienia 600, dlatego proces CGI nie ma prawa odczytu, ponieważ nie jest jego właścicielem.

Proces CGI działa jako użytkownik daemon. Jest członkiem grupy daemon, dlatego może odczytać plik ogolny.txt, który ma uprawnienia 640.

Natomiast plik poufny.txt ma uprawnienia 600, więc grupa nie ma prawa odczytu. Użytkownik daemon nie jest jego właścicielem, dlatego odczyt zostaje odrzucony.

| test                         | kod HTTP |
|------------------------------|----------|
| CGI przed Basic              | 200      |
| CGI po Basic, bez logowania  | 401      |
| CGI po Basic, poprawne hasło | 200      |

## Po zabezpieczeniu
bez logowania:
curl.exe -i http://127.0.0.1:8080/cgi-bin/uprawnienia.cgi
HTTP/1.1 401 Unauthorized
Date: Wed, 04 Nov 2026 12:21:11 GMT
Server: Apache
WWW-Authenticate: Basic realm="Laboratorium 5"

z prawidłowym hasłem:
curl.exe -i -u student http://127.0.0.1:8080/cgi-bin/uprawnienia.cgi
Enter host password for user 'student':
HTTP/1.1 200 OK
Date: Wed, 04 Nov 2026 12:22:41 GMT
Server: Apache
Transfer-Encoding: chunked
Content-Type: text/plain; charset=utf-8

Efektywny UID: 2
Efektywny GID: 2

ODCZYT PLIKOW:

Plik: /lab-data/ogolny.txt
Wynik: odczyt udany
Treść:
LAB05: dokument dostepny dla grupy procesu WWW.


Plik: /lab-data/poufny.txt
Wynik: odmowa dostępu do pliku


## Wnioski:
Zalogowanie użytkownika do serwera WWW nie nadaje programowi CGI uprawnień administratora systemu, ponieważ proces CGI działa z własnym efektywnym UID i GID, niezależnym od użytkownika HTTP