"""Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan. Jos jompikumpi tai molemmat ovat väärin,
tunnus ja salasana kysytään uudelleen. Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on
syötetty viisi kertaa. Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty. (Oikea
käyttäjätunnus on python ja salasana rules)."""

MAX_YRITYS = 5
TUNNUS = "python"
SALASANA = "rules"

print("Anna käyttäjätunnus ja salasana, muuta muista, että sinulla vain 5 yritystä!")
k_tunnus = input("Käyttäjätunnuksesi: ")
k_salasana = input("Salasanasi: ")

entry = True
i = 1

while k_tunnus != TUNNUS or k_salasana != SALASANA:
    print("Jompikumpi tai molemmat ovat väärin.")
    print(f"Sinulla on vain {MAX_YRITYS - i} jäljellä!")
    i += 1
    if i > 5:
        print("Liian paljon yritystä!")
        print("Pääsy evätty!")
        entry = False
        break
    k_tunnus = input("Käyttäjätunnuksesi: ")
    k_salasana = input("Salasanasi: ")

if entry:
    print("Tervetuloa!")
