"""
Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan vastaavan litramäärän. Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
Yksi gallona on 3,785 litraa.
"""

def galonna_to_litro(galonna):
    return galonna * 3.785


while True:
    a_gallona = float(input("Anna bensiinin määrä Yhdysvaltain nestegallonoina: "))
    if a_gallona < 0:
        print("Annettu luku on negatiivinen!")
        break
    print(f"{a_gallona} gallonaa = {galonna_to_litro(a_gallona)} litraa")
