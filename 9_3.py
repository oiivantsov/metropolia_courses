"""
Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän. Metodi kasvattaa
kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt. Esimerkki: auto-olion
tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan
lukemaan 2090 km.
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

    def kulje(self, tunnit):
        self.matka += self.nopeus * tunnit

    def __str__(self):
        return f"Rekisteritunnus on: {Color.off}{self.rekisteritunnus}{Color.off}\n" \
               f"Huippunopeus on: {Color.off}{self.huippunopeus}{Color.off}\n" \
               f"Tämänhetkinen nopeus on: {Color.off}{self.nopeus}{Color.off}\n" \
               f"Kuljettu matka on: {Color.cian}{self.matka}{Color.off}"


auto = Auto(rekisteritunnus="ABC-123", huippunopeus=142)

print(line)
auto.kiihdyta(60)
auto.kulje(1.5)
print(auto)

print(line)
auto.kulje(5)
print(auto)

print(line)

