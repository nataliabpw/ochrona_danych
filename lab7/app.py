"""Sejf sekretow i kalkulator - celowo podatna aplikacja do laboratorium 7.

Uruchamiaj wylacznie lokalnie, w kontenerze z pakietu. Dane sa fikcyjne.
"""
import sqlite3

from flask import Flask, render_template, request

app = Flask(__name__)
BAZA = "file:/dane/sekrety.db?mode=ro"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/sekret")
def sekret():
    klucz = request.args.get("klucz", "")
    zapytanie = "SELECT wlasciciel, sekret FROM sekrety WHERE klucz = ?"
    wiersze, blad = [], None
    try:
        with sqlite3.connect(BAZA, uri=True) as db:
            wiersze = db.execute(zapytanie, (klucz,)).fetchall()
    except sqlite3.Error as exc:
        blad = f"{type(exc).__name__}: {exc}"
        app.logger.exception(blad)
        blad = "Nieprawidłowe dane"
    return render_template("sekret.html", klucz=klucz, zapytanie=zapytanie, wiersze=wiersze, blad=blad)


import re, operator

OPS = {"+": operator.add, "-": operator.sub,
       "*": operator.mul, "/": operator.truediv}
WZORZEC = re.compile(r"\s*(-?\d+(?:\.\d+)?)\s*([+\-*/])\s*(-?\d+(?:\.\d+)?)\s*")

@app.route("/kalkulator")
def kalkulator():
    wyrazenie = request.args.get("wyrazenie")
    if wyrazenie is None:
        return render_template("kalkulator.html", wyrazenie="", wynik=None)
    m = WZORZEC.fullmatch(wyrazenie) if len(wyrazenie) <= 100 else None
    if not m:
        return ("Nieprawidłowe dane", 400)
    a, op, b = float(m[1]), m[2], float(m[3])
    if op == "/" and b == 0:
        return ("Dzielenie przez zero", 400)
    return render_template("kalkulator.html", wyrazenie=wyrazenie, wynik=OPS[op](a, b))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
