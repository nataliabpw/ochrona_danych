def decrypt(cryptogram_b, key):
    result = ""
    for b in cryptogram_b:
        code = (b - key) % 256
        result += chr(code)
    return result

def readability(text):
    printable = sum(1 for c in text if (ord(c) in range(32,127) or ord(c) in [9, 10,13]))
    return printable / len(text)

with open("cezar.bin", "rb") as f:
    cryptogram = f.read()

# print(list(cryptogram))
# print(type(cryptogram))

text_ra = {}

for key in range(256):
    candidate = decrypt(cryptogram, key)
    text_ra[key]=readability(candidate)

posortowane = sorted(text_ra.items(), key=lambda item: (-item[1], item[0]))



for k, ra in posortowane[:5]:
    candidate = decrypt(cryptogram, k)
    print(f"Klucz: {k}, zgodność: {ra} {repr(candidate)[:30]}")


with open("cezar.txt", "w") as f:
    f.write(decrypt(cryptogram, 233))