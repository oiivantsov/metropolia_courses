"""
Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan.
"""

from math import pi

radius = float(input("Hei, mikä on ympyrän säde?: "))
area = pi * radius * radius

print("Kiitos!\nYmpyrän pinta-ala on: %.2f" % area)