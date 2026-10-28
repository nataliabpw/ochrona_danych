import hashlib

LICZBA_WIERSZY = 13
LICZBA_WARIANTOW = 8192

def wczytaj_plik(nazwa):
    with open(nazwa, "rb") as plik:
        dane = plik.read()

    wiersze = dane.split(b"\n")[:-1]
    return dane, wiersze


def h24(dane):
    return hashlib.sha256(dane).digest()[:3]


def utworz_wariant(wiersze, v):
    wynik = []

    for i, wiersz in enumerate(wiersze):
        if (v >> i) & 1:
            wynik.append(wiersz + b" \n")
        else:
            wynik.append(wiersz + b"\n")

    return b"".join(wynik)


def main():
    oryginal, wiersze_oryginalu = wczytaj_plik("oryginal.txt")
    zmieniony, wiersze_zmienionego = wczytaj_plik("zmieniony.txt")

    skroty_oryginalu = {}

    for v in range(LICZBA_WARIANTOW):
        wariant = utworz_wariant(wiersze_oryginalu, v)
        skrot = h24(wariant)

        skroty_oryginalu.setdefault(skrot, v)

    znaleziona_para = False

    for v_zmieniony in range(LICZBA_WARIANTOW):
        wariant = utworz_wariant(wiersze_zmienionego, v_zmieniony)
        skrot = h24(wariant)

        if skrot in skroty_oryginalu:
            v_oryginal = skroty_oryginalu[skrot]

            print("Znaleziona para z h24:")
            print("Wariant oryginału:", v_oryginal)
            print("Wariant zmienionego:", v_zmieniony)
            print("Wspólny h24:", skrot.hex())

            znaleziona_para = True
            break

    if not znaleziona_para:
        print("Nie znaleziono pary wariantów z tym samym h24.")      
    
    docelowy_skrot = h24(oryginal)
    licznik = 0

    for v in range(LICZBA_WARIANTOW):
        wariant = utworz_wariant(wiersze_zmienionego, v)

        if h24(wariant) == docelowy_skrot:
            licznik +=1

    print("\n--- 3. ---")
    print("h24 niezmienionego oryginału:", docelowy_skrot.hex())
    print("Liczba pasujących wariantów:", licznik)


if __name__ == "__main__":
    main()

print(2**12)