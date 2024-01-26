"""
Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa listassa olevien lukujen summan.
Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.
"""


def listan_summa(luvut):
    lukujen_sum = 0
    for i in luvut:
        lukujen_sum += i
    return lukujen_sum


luku_list = []

while True:
    a_luku = input("Anna kokonainen luku, tai vain paina 'Enter' jos olet valmis: ")
    if a_luku == "":
        break
    try:
        luku_list.append(int(a_luku))
    except ValueError:
        print("Anna vain kokonainen luku, tai vain tyhjä arvo!")


print(f"Annettujen lukujen summa = {listan_summa(luku_list)}")
