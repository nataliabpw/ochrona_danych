from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad, unpad


haslo = "MojeHasło123".encode("utf-8")

def generate_key(haslo, salt):
    return PBKDF2(haslo, salt, dkLen=32, count=200000, hmac_hash_module=SHA256)

def aes_cbc(dane, haslo):
    salt = get_random_bytes(16)
    iv = get_random_bytes(16)

    klucz = generate_key(haslo, salt)

    szyfr = AES.new(klucz, AES.MODE_CBC, iv=iv)
    kryptogram = szyfr.encrypt(pad(dane, AES.block_size))

    return kryptogram, salt, iv

def aes_cbc_odszyfr(kryptogram, haslo, salt, iv):
    klucz = generate_key(haslo, salt)

    aes = AES.new(klucz, AES.MODE_CBC, iv=iv)
    dane_padded = aes.decrypt(kryptogram)

    return unpad(dane_padded, AES.block_size)


def test(dane):
    kryptogram, salt, iv = aes_cbc(dane, haslo)
    odzyskane = aes_cbc_odszyfr(kryptogram, haslo, salt, iv)

    print("Długość danych (w bajtach):", len(dane))
    print("Długość kryptogramu (w bajtach):", len(kryptogram))
    print("Zgodność bajtów:", odzyskane == dane)

    return kryptogram, salt, iv

print("Test 1 - puste dane")
wynik1 = test(b"")

print("\nTest 2 - 16 bajtów ASCII")
wynik2 = test(b"0123456789ABCDEF")

print("\nTest 3 - wiadomosc.txt")
with open("wiadomosc.txt", "rb") as plik:
    wiadomosc = plik.read()

wynik3 = test(wiadomosc)


print("\nTest 4 - ponowny szyfr, inna sól i iv")
kryptogram1, sol1, iv1 = wynik3

kryptogram2, sol2, iv2 = aes_cbc(wiadomosc, haslo)

print("Długość pierwszego kryptogramu (w bajtach):", len(kryptogram1))
print("Długość drugiego kryptogramu (w bajtach):", len(kryptogram2))
print("Czy kryptogramy identyczne:", kryptogram1 == kryptogram2)
print("Sole różne:", sol1 != sol2)
print("IV różne:", iv1 != iv2)