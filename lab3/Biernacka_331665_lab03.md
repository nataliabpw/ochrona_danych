# Zadanie 1
ECB
Blok 1: a5ba2b6280d433bccfe6a0461cb88c4e
Blok 2: a5ba2b6280d433bccfe6a0461cb88c4e
Blok 3: a5ba2b6280d433bccfe6a0461cb88c4e
Blok 4: a5ba2b6280d433bccfe6a0461cb88c4e

Wszystkie cztery bloki kryptogramu ECB są identyczne, tak jak bloki w oryginalnych danych, ponieważ w ECB szyfrujemy każdy blok osobno, bez użycia operacji XOR i IV, dlatego identyczne dwa bloki wejściowe, zaszyfrowane AES dają dwa identyczne bloki w kryptogramie.

CBC
Blok 1: 077bf79ee51a25becc77560926ea032d
Blok 2: d9b318512653d1ecd0b763a14a90f467
Blok 3: 42735eab18116367a46831d42759bf20
Blok 4: bf2c76fe6061a3165465a77a76735e4f

W trybie CBC żadne z wypisanych bloków nie są identyczne

Zgodność odszyfrowania:
ECB: True
CBC: True

Oba kryptogramy zostały poprawnie odszyfrowane do oryginalnych 64 bajtów. Podczas odszyfrowywania CBC użyto tego samego IV, który zastosowano przy szyfrowaniu.

Wniosek: 
Tryb ECB szyfruje każdy blok niezależnie, dlatego identyczne bloki wejściowe dały identyczne bloki kryptogramu. W trybie CBC każdy blok zależy od poprzedniego bloku kryptogramu, a pierwszy od IV, dlatego bloki wynikowe były różne.

# Zadanie 2
Test 1 - puste dane
Długość danych (w bajtach): 0
Długość kryptogramu (w bajtach): 16
Zgodność bajtów: True

Test 2 - 16 bajtów ASCII
Długość danych (w bajtach): 16
Długość kryptogramu (w bajtach): 32
Zgodność bajtów: True

Test 3 - wiadomosc.txt
Długość danych (w bajtach): 247
Długość kryptogramu (w bajtach): 256
Zgodność bajtów: True

Długość kryptogramów wynika z zastosowania dopełnienia PKCS#7, które uzupełnia dane do pełnej wielokrotności 16 bajtów, czyli rozmiaru bloku AES. W przypadku pustych danych dołączany jest cały blok o długości 16 bajtów, podobnie w przypadku danych o długości pełnego bloku - 16 bajtów, natomiast dla pliku wiadomosc.txt zawierającego 247 bajtów, dodawanych jest 9 bajtów - otrzymujemy 256 bajtów, czyli wielokrotność 16. 

We wszystkich trzech testach odszyfrowane dane są identyczne z oryginalnymi, co potwierdzają wyniki True.

Test 4 - ponowny szyfr, inna sól i iv
Długość pierwszego kryptogramu (w bajtach): 256
Długość drugiego kryptogramu (w bajtach): 256
Czy kryptogramy identyczne: False
Sole różne: True
IV różne: True

Oba kryptogramy mają tę samą długość, ale różnią się zawartością, ponieważ dane wejściowe są takie same, a zastosowanie PKCS#7 powoduje dodanie takiej samej liczby bajtów dopełnienia. Nie są identyczne, gdyż przy drugim szyfrowaniu użyto nowej soli i nowego wektora IV. Zmiana soli powoduje uzyskanie innego klucza na podstawie tego samego hasła, natomiast zmiana IV wpływa na wynik szyfrowania w trybie CBC. 

# Zadanie 3.
Najlepszych 5 kandydatów:
Znak: m, H = 4.4536
Znak: b, H = 7.9472
Znak: x, H = 7.9490
Znak: o, H = 7.9493
Znak: 2, H = 7.9502

Najlepszy znak: m - najniższa entropia
Pierwszy wiersz tekstu: Odszyfrowany tekst:
Record 000. The archive contains laboratory notes about symmetric encryption and careful handling of binary files.

Liczba możliwych kluczy wynosi 36, ponieważ klucz skłąda się z 16 powtórzeń wybranego znaku spośród 26 małych liter alfabetu i 10 cyfr

Ranking entropii może zawieźć dla danych skompresowanych, ponieważ
