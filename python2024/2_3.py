"""
Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden. Ohjelma tulostaa suorakulmion piirin ja pinta-alan.
Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta.
"""

kanta = float(input("Hei, mikä on suorakulmion kanta?: "))
korkeus = float(input("Mikä on suorakulmion korkeus?: "))

piiri = kanta * 2 + korkeus * 2
ala = kanta * korkeus

print(f"Kiitos!\n"
      f"Suorakulmion piiri on: {piiri:.2f}\n"
      f"Suorakulmion pinta-ala on: {ala:.2f}")
