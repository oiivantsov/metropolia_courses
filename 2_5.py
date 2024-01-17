"""
Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina.
Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.

Yksi leiviskä on 20 naulaa.
Yksi naula on 32 luotia.
Yksi luoti on 13,3 grammaa.

------

Anna leiviskät.
3

Anna naulat.
9

Anna luodit.
13.5

Massa nykymittojen mukaan:
29 kilogrammaa ja 545.95 grammaa.

"""

leiviskat = float(input("Anna leiviskät.\n"))
naulat = float(input("Anna naulat.\n"))
luodit = float(input("Anna luodit.\n"))

grammat = 13.3 * (luodit + naulat * 32 + leiviskat * 32 * 20)
kilogrammat = int(grammat / 1000)

print("Massa nykymittojen mukaan:\n"
      "%.0f kilogrammaa ja %.2f grammaa. "
      % (kilogrammat, grammat))

