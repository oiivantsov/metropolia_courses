"""
Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa toisen listan, joka on muuten
samanlainen kuin parametrina saatu lista paitsi että siitä on karsittu pois kaikki parittomat luvut. Kirjoita
testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että
karsitun listan.
"""


def parittomat_pois(luvut):
    parittomat_luvut = []
    for i in luvut:
        if i % 2 == 0: # kyllä, 0 on myös parillinen
            parittomat_luvut.append(i)
    return parittomat_luvut


luku_list = []

while True:
    a_luku = input("Anna kokonainen luku, tai vain paina 'Enter' jos olet valmis: ")
    if a_luku == "":
        break
    try:
        luku_list.append(int(a_luku))
    except ValueError:
        print("Anna vain kokonainen luku, tai vain tyhjä arvo!")

print(f"Alkuperäinen lista: {luku_list}")
print(f"'Parillinen' lista: {parittomat_pois(luku_list)}")
