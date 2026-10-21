from collections import Counter
import math
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

with open("slaby_ecb.bin", "rb") as plik:
    kryptogram = plik.read()

probka = kryptogram[:4096]

def entropia(data):
    counts = Counter(data)
    length = len(data)

    if length == 0:
        return 0.0

    entropy = 0
    for count in counts.values():
        p = count / length
        entropy -= p * math.log2(p)

    return entropy

alfabet = "abcdefghijklmnopqrstuvwxyz0123456789"
wyniki = []

for znak in alfabet:
    klucz = znak.encode("ascii") * 16

    aes = AES.new(klucz, AES.MODE_ECB)
    odszyfrowana_probka = aes.decrypt(probka)

    H = entropia(odszyfrowana_probka)
    wyniki.append((H, znak))


wyniki.sort()

print("\nNajlepszych 5 kandydatów:")
for H, znak in wyniki[:5]:
    print(f"Znak: {znak}, H = {H:.4f}")

najlepsze_H, najlepszy_znak = wyniki[0]
klucz = najlepszy_znak.encode("ascii") * 16

print("\nNajlepszy znak:", najlepszy_znak)
print("Entropia:", f"{najlepsze_H}")

aes = AES.new(klucz, AES.MODE_ECB)
odszyfrowane_padded = aes.decrypt(kryptogram)

tekst_jawny = unpad(
    odszyfrowane_padded,
    AES.block_size
)

tekst = tekst_jawny.decode("utf-8")
wiersze = tekst.splitlines()

print("\nOdszyfrowany tekst:")
for wiersz in wiersze:
    print(wiersz)
