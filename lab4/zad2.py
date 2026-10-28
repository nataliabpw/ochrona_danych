import hashlib
import hmac
import secrets

def wczytaj_baze():
    baza = {}

    with open("hasla.txt", "r", encoding="utf-8") as plik:
        for linia in plik:
            linia = linia.rstrip("\r\n")

            if not linia:
                continue

            login, iteracje, sol_hex, skrot_hex = linia.split(":")

            baza[login] = {
                "iteracje": int(iteracje),
                "sol": bytes.fromhex(sol_hex),
                "skrot": bytes.fromhex(skrot_hex)
            }

    return baza


baza = wczytaj_baze()


def weryfikuj(login, haslo):
    if login not in baza:
        return False

    rekord = baza[login]

    obliczony_skrot = hashlib.pbkdf2_hmac(
        "sha256",
        haslo.encode("utf-8"),
        rekord["sol"],
        rekord["iteracje"],
        dklen=32
    )

    return hmac.compare_digest(obliczony_skrot, rekord["skrot"])


def dodaj(login, haslo):
    if login in baza:
        raise ValueError("Taki login już istnieje")

    iteracje = 600000
    sol = secrets.token_bytes(16)

    skrot = hashlib.pbkdf2_hmac(
        "sha256",
        haslo.encode("utf-8"),
        sol,
        iteracje,
        dklen=32
    )

    baza[login] = {
        "iteracje": iteracje,
        "sol": sol,
        "skrot": skrot
    }

    return f"{login}:{iteracje}:{sol.hex()}:{skrot.hex()}"


print("Testy:")
print("anna, poprawne hasło:", weryfikuj("anna", "Kasztan-2026"))
print("anna, błędne hasło:", weryfikuj("anna", "kasztan-2026"))
print("piotr, poprawne hasło:", weryfikuj("piotr", "Żółw na łące"))
print("kasia, błędne hasło:", weryfikuj("kasia", "Kasztan-2026"))


print("\nNowe konta:")

wspolne_haslo = "Haslo123!"
dodaj("test1", wspolne_haslo)
dodaj("test2", wspolne_haslo)

print(
    "Sole identyczne:",
    baza["test1"]["sol"] == baza["test2"]["sol"]
)

print(
    "Skróty identyczne:",
    baza["test1"]["skrot"] == baza["test2"]["skrot"]
)

print("Weryfikacja test1:", weryfikuj("test1", wspolne_haslo))
print("Weryfikacja test2:", weryfikuj("test2", wspolne_haslo))