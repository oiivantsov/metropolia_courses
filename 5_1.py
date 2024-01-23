"""
Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän. Ohjelma heittää kerran kaikkia arpakuutioita
ja tulostaa silmälukujen summan. Käytä for-toistorakennetta.
"""

from random import randint

noppa_luku = int(input("Arpakuutioiden lukumäärä: "))
luvut = [randint(1, 6) for i in range(noppa_luku)]

# for luku in luvut:
#     print(luku)

print(f"Silmälukujen summa on {sum(luvut)}.")
