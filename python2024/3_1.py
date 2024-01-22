"""
Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä. Jos kuha on alamittainen,
ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle,
montako senttiä alimmasta sallitusta pyyntimitasta puuttuu. Kuha on alamittainen, jos sen pituus on alle 37 cm.
"""

h_pituus = 37

kuha = float(input("Mikä on kuhan pituuden senttimetreinä?: "))

if kuha < h_pituus:
    print(f"Pitäisi laskea kuha takaisin järveen!\nSen pituus on alle {h_pituus} cm, "
          f"eli sallitusta pyyntimitasta puuttuu {h_pituus - kuha:.1f} cm")
else:
    print("Onneksi olkoon! Otetaan tuo kuha mukaan!")