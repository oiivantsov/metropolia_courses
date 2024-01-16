"""
Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan.
"""

from math import pi

value_check = True
radius = float(0)

while value_check:
    try:
        radius = float(input("Hei, mikä on ympyrän säde?: "))
        value_correct = False
    except ValueError:
        print("Käytä vaan '.' kun sinulla ei ole kokonaisluku :)")


area = pi * radius ** 2

print("Kiitos!\nYmpyrän pinta-ala on: %.2f" % area)