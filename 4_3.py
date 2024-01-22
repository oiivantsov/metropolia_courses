"""Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon
lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman."""

max_luku = -10 ** 12
min_luku = 10 ** 12


while True:
    entry = input("Anna luku: ")
    if entry == "":
        break
    else:
        entry = float(entry)
    if max_luku < entry:
        max_luku = entry
    if min_luku > entry:
        min_luku = entry

print(f"Max annettu: {max_luku:.2f}")
print(f"Min annettu: {min_luku:.2f}")

