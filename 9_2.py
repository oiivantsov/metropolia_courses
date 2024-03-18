"""
Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden muutoksen (km/h). Jos
nopeuden muutos on negatiivinen, auto hidastaa. Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa. Auton
nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi. Jatka pääohjelmaa siten, että auton
nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h. Tulosta tämän jälkeen auton nopeus. Tee
sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus. Kuljettua matkaa ei tarvitse vielä
päivittää.
"""


class Color:
    cian = "\033[96m"
    off = "\033[0m"


line = "-----------------------------------"


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka

    def kiihdyta(self, nopeuden_muutos):
        self.nopeus += nopeuden_muutos
        if self.nopeus < 0:
            self.nopeus = 0
        elif self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        return

    def __str__(self):
        return f"Rekisteritunnus on: {Color.off}{self.rekisteritunnus}{Color.off}\n" \
               f"Huippunopeus on: {Color.off}{self.huippunopeus}{Color.off}\n" \
               f"Tämänhetkinen nopeus on: {Color.cian}{self.nopeus}{Color.off}\n" \
               f"Kuljettu matka on: {Color.off}{self.matka}{Color.off}"


auto = Auto(rekisteritunnus="ABC-123", huippunopeus=142)

print(line)
print(auto)

print(line)
auto.kiihdyta(30)
print(auto)

print(line)
auto.kiihdyta(70)
print(auto)

print(line)
auto.kiihdyta(50)
print(auto)

print(line)
auto.kiihdyta(-200)
print(auto)

print(line)