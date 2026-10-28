import hashlib

def sha256_file(nazwa_pliku):
    with open(nazwa_pliku, "rb") as plik:
        dane = plik.read()

    return hashlib.sha256(dane).hexdigest()


def sprawdz_sumy():
    with open("SHA256SUMS.txt", "r", encoding="utf-8") as plik:
        for wiersz in plik:
            wiersz = wiersz.rstrip("\r\n")

            if not wiersz:
                continue

            if len(wiersz) < 67 or wiersz[64:66] != "  ":
                print(f"{wiersz}: BŁĄD")
                continue

            oczekiwany_skrot = wiersz[:64]
            nazwa_pliku = wiersz[66:]

            try:
                aktualny_skrot = sha256_file(nazwa_pliku)
            except FileNotFoundError:
                print(f"{nazwa_pliku}: BRAK")
                continue

            if aktualny_skrot == oczekiwany_skrot.lower():
                print(f"{nazwa_pliku}: OK")
            else:
                print(f"{nazwa_pliku}: BŁĄD")


def porownaj_skroty():
    tekst1 = "Ala ma kota."
    tekst2 = "Ola ma kota."

    skrot1 = hashlib.sha256(tekst1.encode("ascii")).digest()
    skrot2 = hashlib.sha256(tekst2.encode("ascii")).digest()

    xor = int.from_bytes(skrot1, "big") ^ int.from_bytes(skrot2, "big")

    liczba_bitow = bin(xor).count("1")

    print("\nPorównanie skrótów:")
    print("SHA-256 Ala ma kota.:", skrot1.hex())
    print("SHA-256 Ola ma kota.:", skrot2.hex())
    print("XOR skrótów:", format(xor, "064x"))
    print("Liczba różniących się bitów:", liczba_bitow)


sprawdz_sumy()
porownaj_skroty()