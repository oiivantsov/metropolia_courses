"""
Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C) ja tulostaa sen sanallisen kuvauksen
alla olevan luettelon mukaisesti. Tehtävässä on käytettävä if/elif/else-toistorakennetta.

LUX on parvekkeellinen hytti yläkannella.
A on ikkunallinen hytti autokannen yläpuolella.
B on ikkunaton hytti autokannen yläpuolella.
C on ikkunaton hytti autokannen alapuolella.
Jos käyttäjä syöttää kelvottoman hyttiluokan, ohjelma tulostaa Virheellinen hyttiluokka.
"""

h = input("Syötä laivan hyttiluokka (LUX, A, B, C): ").upper()

if h == "LUX":
    print(f"{h} on parvekkeellinen hytti yläkannella.")
elif h == "A":
    print(f"{h} on ikkunallinen hytti autokannen yläpuolella.")
elif h == "B":
    print(f"{h} on ikkunaton hytti autokannen yläpuolella.")
elif h == "C":
    print(f"{h} on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")