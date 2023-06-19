""""
def berekening(leeftijd):
    if leeftijd<65:
        uitvoer="U moet nog",65-leeftijd,"jaar tot uw pensioen"
    else:
        if leeftijd>=70:
            uitvoer=2
        else:
            uitvoer=1
    return uitvoer
"""

def basis(status):        # kijkt wat je basisuitekring is
    if status == "z":
        uitvoer=uitkering[0]
    else:
        if status == "m":
            uitvoer=uitkering[1]
        else:
            uitvoer=uitkering[2]
    return uitvoer
    
uitkering=[300,350,370]

leeftijd=int(input("Wat is u Leeftijd? "))
print("Wat is u staat van dienst?")
werkstatuut=(input("Voer in: (m)edewerker, (z)zelfstandige of (a)mbtenaar: "))
print()
print("U krijgt voor",basis(werkstatuut)," euro aan pensioen")

