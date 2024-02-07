"""
Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja tulostaa kyseisessä maassa olevien
lentokenttien lukumäärät tyypeittäin. Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä, että pieniä
lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.
"""

import os
import mysql.connector

sql_login = os.environ['SQL_LOG']
sql_password = os.environ['SQL_PASS']


def hae_iso_maa(iso_maa):
    sql = f""" 
    SELECT airport.`type`, COUNT(*) AS "num_of_airports"
    FROM airport
    WHERE airport.iso_country = "{iso_maa}"
    GROUP BY airport.`type`
    ORDER BY num_of_airports DESC;
    """

    # print(sql)

    mycursor = mydb.cursor()
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    if mycursor.rowcount > 0:
        for i in myresult:
            print(i)
    else:
        print("Haettu ISO-koodi ei ole olemassa.")


mydb = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user=sql_login,
    password=sql_password,
    autocommit=True
)

iso_koodi = input("Hae ISO-maakoodi: ")
hae_iso_maa(iso_koodi)
