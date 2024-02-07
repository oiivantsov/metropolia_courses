"""
Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit. Ohjelma ilmoittaa lentokenttien välisen
etäisyyden kilometreinä. Laskenta perustuu tietokannasta haettuihin koordinaatteihin. Laske etäisyys geopy-kirjaston
avulla: https://geopy.readthedocs.io/en/stable/. Asenna kirjasto valitsemalla View / Tool Windows / Python Packages.
Kirjoita hakukenttään geopy ja vie asennus loppuun.
"""

import os
import mysql.connector
from geopy.distance import distance

sql_login = os.environ['SQL_LOG']
sql_password = os.environ['SQL_PASS']


def lan_long_search(icao):
    sql = f""" 
    SELECT airport.latitude_deg, airport.longitude_deg, airport.name, country.name
    FROM airport
    LEFT JOIN country 
    ON airport.iso_country = country.iso_country
    WHERE ident = "{icao}";
    """

    # print(sql)

    mycursor = mydb.cursor()
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    if mycursor.rowcount > 0:
        data = {
            "latitude": myresult[0][0],
            "longitude": myresult[0][1],
            "airport_name": myresult[0][2],
            "airport_country": myresult[0][3],
        }
        return data
    else:
        print("This code is missing from database!")
        return False


mydb = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user=sql_login,
    password=sql_password,
    autocommit=True
)

countries = []

for i in range(1, 3):
    if False not in countries:
        icao_code = input(f"What is {i} ICAO-code: ")
        countries.append(lan_long_search(icao_code))

if False not in countries:
    x_deg = countries[0]["latitude"], countries[0]["longitude"]
    y_deg = countries[1]["latitude"], countries[1]["longitude"]

    x_name = countries[0]["airport_name"]
    y_name = countries[1]["airport_name"]

    x_country = countries[0]["airport_country"]
    y_country = countries[1]["airport_country"]

    dist = distance(x_deg, y_deg).km

    print(f"The distance between {x_name} located in {x_country} and "
          f"{y_name} located in {y_country} is {dist:.2f} km")
