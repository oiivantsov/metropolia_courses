"""
Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden. Ohjelma tulostaa suorakulmion piirin ja pinta-alan.
Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta.
"""

suorakulmion_kanta = float(input("Hei, mikä on suorakulmion kanta?: "))
korkeus = float(input("Mikä on suorakulmion korkeus?: "))

suorakulmion_piiri = suorakulmion_kanta * 2 + korkeus * 2
pinta_alan = suorakulmion_kanta * korkeus

print(f"Kiitos!\n"
      f"Suorakulmion piiri on: {suorakulmion_piiri:.2f}\n"
      f"Suorakulmion pinta-ala on: {pinta_alan:.2f}")
