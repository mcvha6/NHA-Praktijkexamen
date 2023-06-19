def pensioen(status,leeftijd): # berekent je pensioen
    # Check leeftijd
    if leeftijd < 65:
        uitvoer = f"U mag nog {65-leeftijd} jaar werken tot uw pensioen"
        return uitvoer
    else:
        if leeftijd > 69:   # als je  ouder bent dan 70 krig je meer pensien en daarvoor moet je verder in de list.
            lf=3        
        else:
            lf=0
    # check de werkstatuut
    if status == "z":
        uitvoer = f"U krijgt voor € {uitkering[0+lf]} per week aan pensioen"
    else:
        if status == "m":
            uitvoer = f"U krijgt voor € {uitkering[1+lf]} per week aan pensioen"
        else:
            uitvoer = f"U krijgt voor € {uitkering[2+lf]} per week aan pensioen"
    return uitvoer

uitkering=[300,350,370,315,370,395]   # de uitkeringsbedragen in de volgorde zelfstandig, medewerker, ambtenaar, en daarachter als ze 70+ zijn

leeftijd=int(input("Wat is u Leeftijd? "))
print("Wat is u staat van dienst?")
werkstatuut=(input("Voer in: (m)edewerker, (z)elfstandige of (a)mbtenaar: "))
print()
print()
print(pensioen(werkstatuut,leeftijd))

