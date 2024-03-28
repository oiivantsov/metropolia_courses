"""
Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api. Kirjoita ohjelma, joka kysyy
käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina. Perehdy
rajapinnan dokumentaatioon riittävästi. Palveluun rekisteröityminen on tarpeen, jotta saat rajapintapyynnöissä
tarvittavan API-avaimen (API key). Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.
"""

import requests
import os

url = "https://api.openweathermap.org/data/2.5/forecast"
appid = os.environ['SECRET_KEY']

"""
Helsinki
Tampere
Luhanka
Jyväskylä
"""
paikkakunta = ""

while paikkakunta == "":
    paikkakunta = input("Anna paikkakunta: ").lower()

print("")

parameters = {
    "appid": appid,
    "q": f"{paikkakunta},fi",
    "units": "metric"
}

try:
    response = requests.get(url=url, params=parameters)

    saatila = response.json()["list"][0]["weather"][0]["description"]
    lampotila = response.json()["list"][0]["main"]["temp"]

    print(f"Säätila: \"{saatila}\"")
    print(f"Lämpötila: {lampotila} Celsius-astetta")

except requests.RequestException as e:
    print("Hakua ei voitu suorittaa.")
