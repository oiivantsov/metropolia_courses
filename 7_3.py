"""
Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. Ohjelma kysyy käyttäjältä, haluaako tämä
syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa. Jos käyttäjä valitsee uuden lentoaseman
syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen. Jos käyttäjä valitsee haun, ohjelma kysyy
ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen. Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy.
Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa. (
ICAO-koodi on lentoaseman yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät
koodeja helposti selaimen avulla.)
"""


def peli():
    lentoasemat = {}

    onko_peli = True

    while onko_peli:
        valinta = int(input("Valitse toiminto:\n"
                            "1 - Syöttää uuden lentoaseman\n"
                            "2 - Hakea syötetyn lentoaseman tiedot\n"
                            "3 - Lopettaa\n"
                            "Anna numero: "))
        if valinta == 1:
            icao_koodi = input("Anna ICAO-koodi: ")
            if icao_koodi in lentoasemat.keys():
                print(f"Annettu ICAO-koodi '{icao_koodi}' on jo olemassa tietokannassa.")
                valinta_2 = int(
                    input(f"Haluatko muuttaa vastaavat lentoasematiedot (tätä nykyä '{lentoasemat[icao_koodi]}')?\n"
                          "1 - Kyllä\n"
                          "2 - Ei\n"
                          "Anna numero: "))
                if valinta_2 == 1:
                    asema_nimi = input("Anna uusi lentoaseman nimi: ")
                    lentoasemat[icao_koodi] = asema_nimi
            else:
                asema_nimi = input("Anna lentoaseman nimi: ")
                lentoasemat[icao_koodi] = asema_nimi
        elif valinta == 2:
            icao_koodi = input("Anna ICAO-koodi: ")
            if icao_koodi in lentoasemat.keys():
                print(f"Lentoaseman nimi on '{lentoasemat[icao_koodi]}'")
            else:
                print(f"Annettu ICAO-koodi '{icao_koodi}' ei ole olemassa tietokannassa.")
        elif valinta == 3:
            onko_peli = False

    # print(lentoasemat)


peli()
