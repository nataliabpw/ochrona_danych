# Zadanie 1.

dokumenty/budzet.csv: BŁĄD
dokumenty/dane.bin: OK
dokumenty/harmonogram.txt: BRAK
dokumenty/kontakt.txt: OK
dokumenty/regulamin.txt: OK

Porównanie skrótów:
SHA-256 Ala ma kota.: 9b9ae722342758f4bb6a5dd94470ddfab3c95cda15186231f53bb4666e657605
SHA-256 Ola ma kota.: f7f49ccc3e7308f936f9cb71a792c3526663e9ddee89dc3e38fb83db4f308535
XOR skrótów: 6c6e7bee0a54500d8d9396a8e3e21ea8d5aab507fb91be0fcdc037bd2155f330
Liczba różniących się bitów: 131

Suma kontrolna zapisana obok pliku nie chronni przed celową podmianą, ponieważ atakujący może podmienić zarówno plik jak i zapisaną sumę kontrolną - nie mamy pewności czy pochodzi ona z zaufanego źródła.
W zamian lepiej użyć HMAC z tajnym kluczem lub podpisu cyfrowego.

# Zadanie 2.
Testy:
anna, poprawne hasło: True
anna, błędne hasło: False
piotr, poprawne hasło: True
kasia, błędne hasło: False

Nowe konta:
Sole identyczne: False
Skróty identyczne: False
Weryfikacja test1: True
Weryfikacja test2: True

Sól sprawia, że identyczne hasła mogą mieć różne skróty, co utrudnia wykorzystanie gotowych tablic skrótów
Iteracje zaś zwiększają koszt obliczania każdego sktótu co spowalnia ataki takie jak brute force


# Zadanie 3.
Znaleziona para:
Wariant oryginału: 7282
Wariant zmienionego: 1761
Wspólny h24: aac6b9

Wynik kroku 3:
h24 niezmienionego oryginału: 9a8fd6
Liczba pasujących wariantów: 0

Znalezienie dowolnej pary jest znacznie łątwiejsze niż dopasowanie do ustalonego skrótu z powodu paradoksu urodzinowego - znalezienie dowolnej kolizji wymaga średnio 2**(n/2) prób 
Zaś dopasowanie do ustalonego skrótu średnio 2**n prób
gdzie w tym zadaniu n=24 (skrót składa się z 3 bajtów)