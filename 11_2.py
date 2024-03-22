"""
Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto. Sähköautolla on
ominaisuutena akkukapasiteetti kilowattitunteina. Polttomoottoriauton ominaisuutena on bensatankin koko litroina.
Kirjoita aliluokille alustajat. Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden
ja akkukapasiteetin. Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman
kapasiteettinsa. Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja yhden
polttomoottoriauton (ACD-123, 165 km/h, 32.3 l). Aseta kummallekin autolle haluamasi nopeus, käske autoja ajamaan
kolmen tunnin verran ja tulosta autojen matkamittarilukemat.
"""

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
               f"Matka-tunnit on: {self.color}{self.aika}{color_off}"


class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, color, akkukapasiteetti, nopeus=0, matka=0, aika=0):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekisteritunnus, huippunopeus, color, nopeus, matka, aika)

    def __str__(self):
        return super().__str__() + "\n"\
            f"Akkukapasiteetti on {self.color}{self.akkukapasiteetti} kWh{color_off}\n" \
            f"{line}"

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, color, bensatankki, nopeus=0, matka=0, aika=0):
        self.bensatankki = bensatankki
        super().__init__(rekisteritunnus, huippunopeus, color, nopeus, matka, aika)

    def __str__(self):
        return super().__str__() + "\n"\
            f"Bensatankki koko litroina on {self.color}{self.bensatankki} l{color_off}\n" \
            f"{line}"


sähköauto = Sähköauto(rekisteritunnus="ABC-15", huippunopeus=180, nopeus=120, color=colors[0], akkukapasiteetti=52.5)
polttomoottoriauto = Polttomoottoriauto(rekisteritunnus="ACD-123", huippunopeus=165, nopeus=110, color=colors[1], bensatankki=32.3)

sähköauto.kulje(tunnit=3)
polttomoottoriauto.kulje(tunnit=3)

print(line)
print(sähköauto)
print(polttomoottoriauto)


