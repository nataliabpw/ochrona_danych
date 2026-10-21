from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

iv = get_random_bytes(16)

dane = ("0123456789ABCDEF" * 4).encode("ascii")
key = bytes.fromhex("000102030405060708090a0b0c0d0e0f")

ecb = AES.new(key, AES.MODE_ECB)
wynik_ecb = ecb.encrypt(dane)

cbc = AES.new(key, AES.MODE_CBC, iv)
wynik_cbc = cbc.encrypt(dane)


print("ECB")
for i in range(4):
    blok = wynik_ecb[i * 16:(i + 1) * 16]
    print(f"Blok {i + 1}: {blok.hex()}")

print("\nCBC")
for i in range(4):
    blok = wynik_cbc[i * 16:(i + 1) * 16]
    print(f"Blok {i + 1}: {blok.hex()}")


odszyfrowane_ecb = AES.new(
    key, AES.MODE_ECB
).decrypt(wynik_ecb)

odszyfrowane_cbc = AES.new(
    key, AES.MODE_CBC, iv
).decrypt(wynik_cbc)

print("Zgodność odszyfrowania:")
print("ECB:", odszyfrowane_ecb == dane)
print("CBC:", odszyfrowane_cbc == dane)