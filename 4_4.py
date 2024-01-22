"""Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10. Kone arvuuttelee lukua pelaajalta siihen asti,
kunnes tämä arvaa oikein. Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus
tai Oikein. Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä."""

from random import randint

arpo_luku = randint(1, 10)
print(arpo_luku)
entry = int(input("Anna luku 1-10: "))

while arpo_luku != entry:
    if arpo_luku > entry:
        print("Liian pieni arvaus")
        entry = int(input("Anna luku 1-10: "))
    elif arpo_luku < entry:
        print("Liian suuri arvaus")
        entry = int(input("Anna luku 1-10: "))

print("Oikein!")