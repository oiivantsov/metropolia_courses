"""Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän.
Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm"""


def tuuma_to_cm(tumma):
    return tumma * 2.54


while True:
    entry_tumma = float(input("Syötä tuuma: "))
    if entry_tumma < 0:
        print("Negatiivinen tuumamäärän")
        break
    else:
        print(tuuma_to_cm(entry_tumma))
