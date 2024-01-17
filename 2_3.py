"""
Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden. Ohjelma tulostaa suorakulmion piirin ja pinta-alan.
Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta.
"""

suorakulmion_kanta = float(input("Hei, mikä on suorakulmion kanta?: "))
korkeus = float(input("Mikä on suorakulmion korkeus?: "))

suorakulmion_piiri = suorakulmion_kanta * 2 + korkeus * 2
pinta_alan = suorakulmion_kanta * korkeus

print("Kiitos!\n"
      "Suorakulmion piiri on: %.2f\n"
      "Suorakulmion pinta-ala on: %.2f"
      % (suorakulmion_piiri, pinta_alan))
