"""
Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.
"""

import random

arpapeli = True

while arpapeli:

    peli_paatos = input("Haluatko arpoa ('y' = Kyllä, 'n' = Ei)?: ").lower()

    if peli_paatos == "y":

        koodi_3 = f"Kolmenumeroisen koodi: " \
                  f"{random.randint(0, 9)} | {random.randint(0, 9)} | {random.randint(0, 9)}"
        koodi_4 = f"Nelinumeroisen koodi: " \
                  f"{random.randint(1, 6)} | {random.randint(1, 6)} | {random.randint(1, 6)} | {random.randint(1, 6)}"

        print(koodi_3)
        print(koodi_4)

    else:
        arpapeli = False
