"""
Tehtävä on jatkoa aiemmalle autokilpailutehtävälle. Kirjoita Kilpailu-luokka, jolla on ominaisuuksina kilpailun
nimi, pituus kilometreinä ja osallistuvien autojen lista. Luokassa on alustaja, joka saa parametreinaan nimen,
kilometrimäärän ja autolistan ja asettaa ne ominaisuuksille arvoiksi. Luokassa on seuraavat metodit:

tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät toimenpiteet eli arpoo
kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia. tulosta_tilanne, joka tulostaa kaikkien
autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna. kilpailu_ohi, joka palauttaa True, jos jokin autoista
on maalissa eli se on ajanut vähintään kilpailun kokonaiskilometrimäärän. Muussa tapauksessa palautetaan False.
Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli". Luotavalle kilpailulle annetaan
kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä. Pääohjelma simuloi kilpailun etenemistä kutsumalla
toistorakenteessa tunti_kuluu-metodia, jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu
ohi. Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin välein sekä kertaalleen sen
jälkeen, kun kilpailu on päättynyt.
"""
from random import randint

# ----------------- CONFIG ------------------------------
autojen_maara = 10
max_nopeuden_muutos = 15
min_nopeuden_muutos = -10
max_nopeus = 200
min_nopeus = 100
pituus = 8_000
aika_vali = 1

# ----------------- STYLE & COLORS ------------------------------
colors = ["\033[31m", "\033[32m", "\033[33m", "\033[34m", "\033[1m\033[90m", "\033[93m", "\033[97m", "\033[95m",
          "\033[96m", "\033[35m"] * 10
color_bold = '\033[1m'
color_cian = '\033[96m'
color_off = "\033[0m"
line = "-----------------------------------"
dots = "............"


# ----------------- OLIOT ------------------------------
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
        return f"Rekisteritunnus on: {self.color}{self.rekisteritunnus}{color_off}\n" \
               f"Huippunopeus on: {self.color}{self.huippunopeus}{color_off}\n" \
               f"Tämänhetkinen nopeus on: {self.color}{self.nopeus}{color_off}\n" \
               f"Kuljettu matka on: {self.color}{self.matka}{color_off}\n" \
               f"Matka-tunnit on: {self.color}{self.aika}{color_off}\n" \
               f"{line}"


class Kilpailu:
    tunnit = 0

    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot
        self.malli_autot = []

    def tunti_kuluu(self):
        for auto in self.autot:
            if auto not in self.malli_autot:
                nopeuden_muutos = randint(min_nopeuden_muutos, max_nopeuden_muutos)
                auto.kiihdyta(nopeuden_muutos)
                auto.kulje(aika_vali)

                if auto.matka >= self.pituus:
                    self.malli_autot.append(auto)

        Kilpailu.tunnit += aika_vali

    def tulosta_tilanne(self, malli=False):
        if not malli:
            print(f"{color_bold}{color_cian}Tunti: {Kilpailu.tunnit}{color_off}")
            print(dots)
            for auto in self.autot:
                print(auto)
        else:
            print(f'{color_bold}{color_cian}"{self.nimi}" TULOKSET!{color_off}')
            print(dots)
            for i in range(len(self.malli_autot)):
                print(f"{color_bold}{i + 1} sija:{color_off}")
                print(self.malli_autot[i])

    def kilpailu_ohi(self):
        return len(self.autot) == len(self.malli_autot)


# ----------------- PAAOHJELMA ------------------------------
def main():
    autot = [Auto(rekisteritunnus=f"ABC-{i + 1}", huippunopeus=randint(min_nopeus, max_nopeus), color=colors[i])
             for i in range(autojen_maara)]

    kilpailu = Kilpailu(nimi="Suuri romuralli", pituus=pituus, autot=autot)

    print(dots)
    while not kilpailu.kilpailu_ohi():
        kilpailu.tunti_kuluu()
        if kilpailu.tunnit % 10 == 0:
            kilpailu.tulosta_tilanne()

    kilpailu.tulosta_tilanne(malli=True)
    return


main()
