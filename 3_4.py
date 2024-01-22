"""
Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi.
Vuosi on karkausvuosi, jos se on jaollinen neljällä. Sadalla jaolliset vuodet ovat karkausvuosia
vain jos ne ovat jaollisia myös neljälläsadalla.
"""


def on_karkausvuosi(vuosi):
    if vuosi % 4 == 0:
        if vuosi % 100 == 0:
            if vuosi % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


if on_karkausvuosi(int(input("Syötä vuosi: "))):
    print("On karkausvuosi!")
else:
    print("Ei ole karkausvuosi!")
