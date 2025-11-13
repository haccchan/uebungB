start = True
geburtstage = {}
while start:
    e = input("\nAusgabe \n (n) neuen Eintrag anlegen \n (d) einen Eintrag löschen \n (s) nach einer Person suchen \n (l) alle Einträge auflisten \n (q) Kalenderprogramm beenden ")
    if e == "n":
        name = str(input("Geburtstag Name: "))
        jahr = int(input("Geburtstag Jahr: "))
        monat = int(input("Geburtstag Monat: "))
        tage = int(input("Geburtstag Tage: "))
        geburtstage[name] = (jahr, monat, tage)

    if e == "d":
        print(geburtstage)
        name = str(input("Welche Geburtstag möchten Sie löschen? (Name eingeben)"))
        geburtstage.pop(name)

    if e == "s":
        print(geburtstage)
        name = str(input("Wer suchen Sie?"))
        for i in range(len(geburtstage[name])):
            print(geburtstage[name][i], end=".")

    if e == "l":
        for i in geburtstage:
            print(i, end=":")
            for j in range(len(geburtstage[i])):
                print(geburtstage[i][j], end=".")

    if e == "q":
        start = False