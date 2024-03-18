"""
Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi. Tee pääohjelman
alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta. Jokaisen auton huippunopeus arvotaan
100 km/h ja 200 km/h väliltä. Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa.
Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:

Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä. Tämä tehdään
kutsumalla kiihdytä-metodia. Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla
kulje-metodia. Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä. Lopuksi tulostetaan
kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.
"""
from random import randint

# ----------------- OLIO ------------------------------

colors = ["\033[31m", "\033[32m", "\033[33m", "\033[34m", "\033[35m", "\033[93m", "\033[97m", "\033[95m", "\033[96m", "\033[90m"]
color_off = "\033[0m"
line = "-----------------------------------"


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, color, nopeus=0, matka=0, aika=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.color = color

        self.nopeus = nopeus
        self.matka = matka
        self.aika = aika

    def kiihdyta(self, nopeuden_muutos):
        self.nopeus += nopeuden_muutos
        if self.nopeus < 0:
            self.nopeus = 0
        elif self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        return

    def kulje(self, tunnit):
        self.matka += self.nopeus * tunnit
        self.aika += tunnit

    def __str__(self):
        return f"{line}\n" \
               f"Rekisteritunnus on: {self.color}{self.rekisteritunnus}{color_off}\n" \
               f"Huippunopeus on: {self.color}{self.huippunopeus}{color_off}\n" \
               f"Tämänhetkinen nopeus on: {self.color}{self.nopeus}{color_off}\n" \
               f"Kuljettu matka on: {self.color}{self.matka}{color_off}\n" \
               f"Matka-tunnit on: {self.color}{self.aika}{color_off}\n" \
               f"{line}"


# ----------------- KILPAILU-OHJELMA ------------------------------

max_nopeuden_muutos = 15
min_nopeuden_muutos = -10
max_nopeus = 200
min_nopeus = 100
etaisyys = 10_000
aika_vali = 1

autot = [Auto(rekisteritunnus=f"ABC-{i+1}", huippunopeus=randint(min_nopeus, max_nopeus), color=colors[i]) for i in range(10)]
i = 1
print(line)

while autot:
    for auto in autot:
        nopeuden_muutos = randint(min_nopeuden_muutos, max_nopeuden_muutos)
        auto.kiihdyta(nopeuden_muutos)
        auto.kulje(aika_vali)
        if auto.matka >= etaisyys:
            print(f"{i} sija:")
            print(auto)
            autot.remove(auto)
            i += 1

