"""
Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin. Ohjelma hakee ja tulostaa koodia vastaavan
lentokentän nimen ja sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta. ICAO-koodi on tallennettuna
airport-taulun ident-sarakkeeseen.
"""

import os
import mysql.connector

sql_login = os.environ['SQL_LOG']
sql_password = os.environ['SQL_PASS']


def hae_icao(icao):
    sql = f""" 
    SELECT airport.ident, airport.name, airport.municipality, country.name 
    FROM airport
    LEFT JOIN country 
    ON airport.iso_country = country.iso_country
    WHERE airport.ident = "{icao}";
    """

    # print(sql)

    mycursor = mydb.cursor()
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    if mycursor.rowcount > 0:
        print(f"Päivää!\n"
              f"Haettu ICAO-koodi on {myresult[0][0]}.\n"
              f"Lentokentän nimi on {myresult[0][1]}.\n"
              f"Sijaintikuna on {myresult[0][2]}.\n"
              f"Maa on {myresult[0][3]}.")
    else:
        print("Haettu ICAO-koodi ei ole olemassa.")


mydb = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user=sql_login,
    password=sql_password,
    autocommit=True
)

icao_koodi = input("Hae ICAO-koodi: ")
hae_icao(icao_koodi)
