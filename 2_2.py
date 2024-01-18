"""
Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan.
"""

from math import pi

sade = float(input("Hei, mikä on ympyrän säde?: "))
ala = pi * sade * sade

print(f"Kiitos!\nYmpyrän pinta-ala on: {ala:.2f}")