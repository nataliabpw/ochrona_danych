with open("tekst_pl.txt", "rb") as f:
    cryptogram = f.read()

def encrypt(bytes, key):
    result = bytearray(len(bytes))
    for i, byte in enumerate(bytes):
        key_char = key[i % len(key)]
        code = (byte + ord(key_char)) % 256
        result[i] = code
    return result

def decrypt(bytes, key):
    result = bytearray(len(bytes))
    for i, byte in enumerate(bytes):
        key_char = key[i % len(key)]
        code = (byte - ord(key_char)) % 256
        result[i] = code
    return result

key = "ZAMEK"

encrypted = encrypt(cryptogram, key)

# with open("vigenere.bin", "wb") as f:
#     f.write(encrypted)

decrypted = decrypt(encrypted, key)

# for i in range(len(cryptogram)):
#     if (cryptogram[i]!=decrypted[i]):
#         print("Błąd!")

print(decrypted == cryptogram)

empty = b""
print("Empty:")
print(empty == decrypt(encrypt(empty, key), key))

print("0 i 255:")
bytes = bytes([0, 255])
print(bytes == decrypt(encrypt(bytes, key), key))


ciag = b"BRAMABRAMABRAMA"

encrypted_szyfr = encrypt(ciag, "SZYFR")
encrypted_kod = encrypt(ciag, "KOD")

def show_hex(data):
    for i in range(0, len(data), 5):
        print(data[i:i+5].hex())

print("Klucz SZYFR:")
show_hex(encrypted_szyfr)

print("Klucz KOD:")
show_hex(encrypted_kod)