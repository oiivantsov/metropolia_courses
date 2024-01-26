"""
Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina.
Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri. Pääohjelma kysyy käyttäjältä kahden pizzan
halkaisijat ja hinnat sekä ilmoittaa, kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi
yksikköhinta). Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.
"""

from math import pi

PIZZAN_MAARA = 2


def per_lasku(halk, hinta):
    pizzan_ala = pi * (halk ** 2) / 4
    # print(pizzan_ala)
    hinta_per_sent = hinta / pizzan_ala
    return hinta_per_sent


def paras_hinta(pizzat):
    ind = 0
    paras_hinta = 10 * 10 ^ 6
    paras_pizza_index = 0

    for pizza in pizzat:
        if pizza["hinta_per_cm"] < paras_hinta:
            paras_hinta = pizza["hinta_per_cm"]
            paras_pizza_index += ind
        ind += 1

    return f"Paras-hinta pizza on " \
           f"{pizzat[paras_pizza_index]['halkaisija']} cm halkaisijan kanssa ja " \
           f"{pizzat[paras_pizza_index]['hinta']} eur hinnan kanssa,\n" \
           f"koska sillä on alhaisempi yksikköhinta, joka = " \
           f"{pizzat[paras_pizza_index]['hinta_per_cm']:.2f} eur/cm^2"


def run():
    i = 1

    pizzat = []

    while i <= PIZZAN_MAARA:
        pizzan_halk = float(input(f"Anna {i} pizzan halkaisija senttimetreinä: "))
        pizzan_hinta = float(input(f"Anna {i} pizzan hinta euroina: "))
        pizzat.append(
            {
                "halkaisija": pizzan_halk,
                "hinta": pizzan_hinta,
                "hinta_per_cm": per_lasku(halk=pizzan_halk, hinta=pizzan_hinta)
            }
        )
        i += 1

    print(paras_hinta(pizzat))


run()
