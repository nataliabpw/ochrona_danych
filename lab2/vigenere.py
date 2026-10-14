with open("tekst_pl.txt", "rb") as f:
    cryptogram = f.read()

def encrypt(bytes, key):
    result = bytearray(len(cryptogram))
    for i, byte in enumerate(bytes):
        key_char = key[i % len(key)]
        code = (byte + ord(key_char)) % 256
        result[i] = code
    return result

def decrypt(bytes, key):
    result = bytearray(len(cryptogram))
    for i, byte in enumerate(bytes):
        key_char = key[i % len(key)]
        code = (byte - ord(key_char)) % 256
        result[i] = code
    return result

# key = "ZAMEK"

# encrypted = encrypt(cryptogram, key)
# decrypted = decrypt(encrypted, key)

# for i in range(len(cryptogram)):
#     if (cryptogram[i]!=decrypted[i]):
#         print("Błąd!")

# with open("vigenere.bin", "wb") as f:
#     f.write(encrypted)

ciag = "BRAMABRAMABRAMA"

bytes = bytearray(len(ciag))

for i in range(len(ciag)):
    bytes[i] = ord(ciag[i])

def show_hex(bytes):
    print(bytes.hex())

print("Key: SZYFR:")
print(encrypt(bytes, "SZYFR"))
# show_hex(encrypt(bytes, "SZYFR"))

print("Key: KOD:")
print(encrypt(bytes, "KOD"))
# show_hex(encrypt(bytes, "KOD"))