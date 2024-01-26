"""
Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6. Kirjoita
pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen. Pääohjelma tulostaa kunkin heiton jälkeen saadun
silmäluvun.
"""

from random import randint

def heitto():
    return randint(1, 6)

i = 0

while True:
    noppa_luku = heitto()
    print(f"Saatu silmäluku on {noppa_luku}")
    i += 1
    if noppa_luku == 6:
        print(f"Kuutonen tulee {i} heittojen jälkeen!")
        break


