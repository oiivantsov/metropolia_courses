"""
Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän. Muokatun funktion
avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa. Edellisestä tehtävästä poiketen nopan heittelyä
jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa.
"""

from random import randint


def heitto(n):
    return randint(1, n)


i = 0

while True:
    max_luku = int(input("Anna nopan maksimisilmäluku: "))
    if max_luku < 1:
        print("Anna kokonainen luku >= 1")
    else:
        break

while True:
    noppa_luku = heitto(max_luku)
    print(f"Saatu silmäluku on {noppa_luku}")
    i += 1
    if noppa_luku == max_luku:
        print(f"Nopan maksimisilmäluku tulee {i} heittojen jälkeen!")
        break
