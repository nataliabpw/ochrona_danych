from hashlib import sha256
teksty = ["Ala ma kota.", "Ala ma kota!"]

for t in teksty:
    skrot = sha256(t.encode("utf-8")).hexdigest()
    print(t)
    print(skrot)
