"""
Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan lentokentän nimen ja kaupungin
JSON-muodossa. Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta. Esimerkiksi EFHK-koodia vastaava
GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/kenttä/EFHK. Vastauksen on oltava muodossa: {"ICAO":"EFHK",
"Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.
"""

from flask import Flask, Response
import json

import os
import mysql.connector

sql_login = os.environ['SQL_LOG']
sql_password = os.environ['SQL_PASS']

app = Flask(__name__)


@app.route('/kenttä/<icao>')
def hae_icao(icao):
    try:
        mydb = mysql.connector.connect(
            host='localhost',
            port=3306,
            database='flight_game',
            user=sql_login,
            password=sql_password,
            autocommit=True
        )
    except mysql.connector.Error as error:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "SQL-palvelimeen ei saa yhteyttä."
        }

    else:
        sql = f""" 
        SELECT airport.ident, airport.name, airport.municipality
        FROM airport
        LEFT JOIN country 
        ON airport.iso_country = country.iso_country
        WHERE airport.ident = "{icao}";
        """

        with mydb.cursor() as mycursor:
            mycursor.execute(sql)
            myresult = mycursor.fetchall()

            if mycursor.rowcount > 0:
                tilakoodi = 200
                vastaus = {
                    "status": tilakoodi,
                    "ICAO": icao,
                    "Name": myresult[0][1],
                    "Municipality": myresult[0][2]
                }
            else:
                tilakoodi = 400
                vastaus = {
                    "status": tilakoodi,
                    "teksti": "Haettu ICAO-koodi ei ole olemassa."
                }

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")


@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status": "404",
        "teksti": "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
