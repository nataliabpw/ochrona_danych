def rc4(bytes, key):
    key_codes = [ord(c) for c in key]
    key_length = len(key_codes)

    # KSA
    S = list(range(256))

    j = 0
    for i in range(256):
        j = (j + S[i] + key_codes[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]

    # PRGA
    i = 0
    j = 0

    result = bytearray()
    
    for byte in bytes:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]

        # XOR
        K = S[(S[i] + S[j]) % 256]
        result.append(byte ^ K)
    
    return result


# key = "abc"
# data = bytes([3, 165, 18, 0, 255])

# encrypted = rc4(data, key)
# decrypted = rc4(encrypted, key)

# print(decrypted == data)


import math
from collections import Counter

def entropy(data):
    counts = Counter(data)
    length = len(data)
    entropy = 0

    for count in counts.values():
        p = count / length
        entropy -= p * math.log2(p)
    
    return entropy

with open("rc4.bin", "rb") as f:
    cryptogram = f.read()

from itertools import product
from time import perf_counter

key_entropy = {}

start = perf_counter()

for letters in product("abcdefghijklmnopqrstuvwxyz", repeat=3):
    key = "".join(letters)

    candidate = rc4(cryptogram[:512], key)
    e = entropy(candidate)

    key_entropy[key] = e

end = perf_counter()
print(f"Czas przeszukiwania: {end-start} s")

posortowane = sorted( key_entropy.items(), key=lambda item: (item[1], item[0]))

for key, e in posortowane[:5]:
    print(f"Klucz: {key}, entropia: {e:.6f}")

key = posortowane[0][0]
print("Wybrany klucz:", key)
print("Liczba prób:", len(key_entropy))

decrypted = rc4(cryptogram, key)

with open("rc4.txt", "wb") as f:
    f.write(decrypted)

encrypted_again = rc4(decrypted, key)
print("Zgodność z kryptogramem:", encrypted_again == cryptogram)

print(f"Entropia kryptogramu: {entropy(cryptogram):.6f}")
print(f"Entropia odszyfrowania: {entropy(decrypted):.6f}")