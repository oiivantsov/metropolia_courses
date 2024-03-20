"""
Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron. Hissillä on metodit
siirry_kerrokseen, kerros_ylös ja kerros_alas. Uusi hissi on aina alimmassa kerroksessa. Jos tee luodulle hissille h
esimerkiksi metodikutsun h.siirry_kerrokseen(5), metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta
kertaa, että hissi päätyy viidenteen kerrokseen. Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai
alaspäin ja ilmoittavat, missä kerroksessa hissi sen jälkeen on. Testaa luokkaa siten, että teet pääohjelmassa hissin
ja käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.
"""

line = "-------------------------------------------"


class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nyky_kerros = alin_kerros

    def kerros_ylos(self):
        self.nyky_kerros += 1
        if self.nyky_kerros > self.ylin_kerros:
            self.nyky_kerros = self.ylin_kerros
            print("Hissi ei siirry ylös, nyt on ylin kerros")
        print(f"Hissi on nyt {self.nyky_kerros} kerroksessa.")

    def kerros_alas(self):
        self.nyky_kerros -= 1
        if self.nyky_kerros < self.alin_kerros:
            self.nyky_kerros = self.alin_kerros
            print("Hissi ei siirry alas, nyt on alin kerros")
        print(f"Hissi on nyt {self.nyky_kerros} kerroksessa.")

    def siirry_kerrokseen(self, kerros: int):
        print(line)
        if kerros > self.ylin_kerros or kerros < self.alin_kerros:
            print("Ei ole sellaista kerrosta")
        else:
            if self.nyky_kerros < kerros:
                for i in range(kerros - self.nyky_kerros):
                    self.kerros_ylos()
            elif self.nyky_kerros > kerros:
                for i in range(self.nyky_kerros - kerros):
                    self.kerros_alas()
            else:
                print("Olet nyt valitussa kerroksessa")


h = Hissi(0, 8)

h.siirry_kerrokseen(3)
h.siirry_kerrokseen(-1)
h.siirry_kerrokseen(0)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(10)
