"""
Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.
"""

import random

arpapeli = True

while arpapeli:

    kolmenumeroisen_koodi = "Kolmenumeroisen koodi: | "
    nelinumeroisen_koodi = "Nelinumeroisen koodi: | "

    peli_paatos = input("Haluatko arpoa ('y' = Kyllä, 'n' = Ei)?: ").lower()

    if peli_paatos == "y":
        for i in range(1, 5):

            if i < 4:
                kolmenumeroisen_koodi += f"{random.randint(0, 9)} | "
                nelinumeroisen_koodi += f"{random.randint(1, 6)} | "
            else:
                nelinumeroisen_koodi += f"{random.randint(1, 6)} | "

        print(kolmenumeroisen_koodi[:-1])
        print(nelinumeroisen_koodi[:-1])

    else:
        arpapeli = False
