"""
Kirjoita ohjelma, joka kysyy nimesi ja sen jälkeen tervehtii sinua omalla nimelläsi. Esimerkkejä:

Jos syötät nimeksesi Viivi, ohjelma tervehtii sinua sanoin Terve, Viivi!
Jos syötät nimeksesi Ahmed, ohjelma tervehtii sinua sanoin Terve, Ahmed!

"""

name = input("Mikä on nimesi?: ").capitalize()
print(f"Terve, {name}!")

