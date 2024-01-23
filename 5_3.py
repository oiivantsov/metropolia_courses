"""
Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku. Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.

Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.
"""

luvut = []


def alkuluku(luku):
    for i in range(2, luku):
        if luku % i == 0:
            return f"Syötetty luku {luku} ei ole alkuluku"

    luvut.append(luku)
    return f"Syötetty luku {luku} on alkuluku"


print(alkuluku(int(input("Anna kokonaisluku: "))))

# for j in range(1, 101):
#     print(alkuluku(j))
#
# print(luvut)
