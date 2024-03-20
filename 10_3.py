"""
Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys, joka käskee kaikki
hissit pohjakerrokseen. Jatka pääohjelmaa siten, että talossasi tulee palohälytys.
"""


line = "-------------------------------------------"


class Hissi:
    def __init__(self, alin_kerros, ylin_kerros, hissin_numero):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nyky_kerros = alin_kerros
        self.hissin_numero = hissin_numero

    def kerros_ylos(self):
        self.nyky_kerros += 1
        if self.nyky_kerros > self.ylin_kerros:
            self.nyky_kerros = self.ylin_kerros
            print(f"Hissi #{self.hissin_numero} ei siirry ylös, nyt on ylin kerros")
        print(f"Hissi #{self.hissin_numero} on nyt {self.nyky_kerros} kerroksessa.")

    def kerros_alas(self):
        self.nyky_kerros -= 1
        if self.nyky_kerros < self.alin_kerros:
            self.nyky_kerros = self.alin_kerros
            print(f"Hissi #{self.hissin_numero} ei siirry alas, nyt on alin kerros")
        print(f"Hissi #{self.hissin_numero} on nyt {self.nyky_kerros} kerroksessa")

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
                print(f"Hissi #{self.hissin_numero} on nyt valitussa kerroksessa")


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lukumaara):
        self.alin_kerros = alin_kerros
        self.hissit = [Hissi(alin_kerros, ylin_kerros, hissin_numero=i+1) for i in range(hissien_lukumaara)]

    def aja_hissia(self, hissin_numero, kerros):
        valittu_hissi = self.hissit[hissin_numero - 1]
        valittu_hissi.siirry_kerrokseen(kerros)

    def palohalytys(self):
        for i in range(len(self.hissit)):
            self.aja_hissia(i + 1, self.alin_kerros)


talo = Talo(alin_kerros=0, ylin_kerros=8, hissien_lukumaara=2)

talo.aja_hissia(hissin_numero=1, kerros=5)
talo.aja_hissia(hissin_numero=2, kerros=8)
talo.palohalytys()