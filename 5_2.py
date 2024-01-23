"""
Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon
lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.
"""

luvut = []

i = 0
while True:
    entry = input("Anna luku: ")
    if entry == "":
        break
    else:
        entry = float(entry)
        luvut.append(entry)
        if i < 5:
            i += 1


luvut.sort(reverse=True)

msg = f"{i} suurinta suuruusjärjestyksessä suurimmasta alkaen: "
for i in luvut[:5]:
    msg += f"{i} | "
msg = msg[:-2]

print(msg)