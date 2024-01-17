"""
Kirjoita ohjelma, joka kysyy kolme kokonaislukua. Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.
"""


def summa(n1, n2, n3):
    return n1 + n2 + n3


def tulo(n1, n2, n3):
    return n1 * n2 * n3


def keskiarvo(n1, n2, n3):
    return (n1 + n2 + n3) / 3


luvut = []
i = 1


print("Hei!\n")

while len(luvut) < 3:
    try:
        luku = int(input(f"Mikä on sinun {i} kokonaisluku?: "))
        luvut.append(luku)
        i += 1
    except ValueError:
        print("Käytä vain kokonailukuja!")


print(f"Kiitos!\n"
      f"Summa on {summa(luvut[0], luvut[1], luvut[2])}\n"
      f"Tulo on {tulo(luvut[0], luvut[1], luvut[2])}\n"
      f"Keskiarvo on {keskiarvo(luvut[0], luvut[1], luvut[2])}")
