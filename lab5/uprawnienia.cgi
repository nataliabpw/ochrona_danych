#!/usr/bin/python3

import os

print("Content-Type: text/plain; charset=utf-8")
print()

print(f"Efektywny UID: {os.geteuid()}")
print(f"Efektywny GID: {os.getegid()}")

print("\nODCZYT PLIKOW:")

pliki = [
    "/lab-data/ogolny.txt",
    "/lab-data/poufny.txt"
]

for sciezka in pliki:
    print(f"\nPlik: {sciezka}")

    try:
        with open(sciezka, "r", encoding="utf-8") as plik:
            zawartosc = plik.read()
            print("Wynik: odczyt udany")
            print("Treść:")
            print(zawartosc)

    except PermissionError:
        print("Wynik: odmowa dostępu do pliku")

    except OSError as blad:
        print(f"Wynik: błąd odczytu: {blad}")