"""
Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus, tämänhetkinen nopeus ja kuljettu
matka. Kirjoita luokkaan alustaja, joka asettaa ominaisuuksista kaksi ensin mainittua parametreina saatuihin
arvoihin. Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi. Kirjoita pääohjelma,
jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h). Tulosta pääohjelmassa sen jälkeen luodun
auton kaikki ominaisuudet.
"""


class Color:
    cian = "\033[96m"
    off = "\033[0m"


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka

    def __str__(self):
        return f"Rekisteritunnus on: {Color.cian}{self.rekisteritunnus}{Color.off}\n" \
               f"Huippunopeus on: {Color.cian}{self.huippunopeus}{Color.off}\n" \
               f"Tämänhetkinen nopeus on: {Color.cian}{self.nopeus}{Color.off}\n" \
               f"Kuljettu matka on: {Color.cian}{self.matka}{Color.off}"


auto = Auto(rekisteritunnus="ABC-123", huippunopeus=142)
print(auto)