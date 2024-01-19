"""
Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l). Ohjelma ilmoittaa,
onko hemoglobiiniarvo alhainen, normaali vai korkea.

Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.
"""

s, h = input("Syötä biologisen sukupuoli ('n' tai 'm') ja hemoglobiiniarvo (kokonaisluku) käyttäen 'space': ").split()
h = int(h)

if s == "n":
    if h < 117:
        print("hemoglobiiniarvo on liian matala.")
    elif h > 175:
        print("hemoglobiiniarvo on liian korkea.")
    else:
        print("hemoglobiiniarvo on liian normaali.")
elif s == "m":
    if h < 134:
        print("hemoglobiiniarvo on liian matala.")
    elif h > 195:
        print("hemoglobiiniarvo on liian korkea.")
    else:
        print("hemoglobiiniarvo on liian normaali.")
else:
    print("Virheellinen sukupuoli.")
