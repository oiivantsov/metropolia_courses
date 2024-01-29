"""
Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma tulostaa sitä vastaavan
vuodenajan (kevät, kesä, syksy, talvi). Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina
monikkotietorakenteeseen. Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on
ensimmäinen talvikuukausi.
"""

vuodenajat = ("talvi", "talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy")
jarjestysnumero = int(input("Anna kuukauden järjestysnumero (1-12): "))
vuodenaika = vuodenajat[jarjestysnumero - 1]
print (f"{jarjestysnumero}. kuukauden vuodenaika on {vuodenaika}.")

