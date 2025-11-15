start = True
geburtstage = {}

def print_menu():
    return "\nAusgabe \n (n) neuen Eintrag anlegen \n (d) einen Eintrag löschen \n (s) nach einer Person suchen \n (l) alle Einträge auflisten \n (q) Kalenderprogramm beenden "

def n(geburtstage):
    name = str(input("Geburtstag Name: "))
    jahr = int(input("Geburtstag Jahr: "))
    monat = int(input("Geburtstag Monat: "))
    tage = int(input("Geburtstag Tage: "))
    geburtstage[name] = (jahr, monat, tage)

def d(geburtstage):
    print(geburtstage)
    name = str(input("Welche Geburtstag möchten Sie löschen? (Name eingeben)"))
    geburtstage.pop(name)

def l(geburtstage):
    for i in geburtstage:
        print(i, end=":")
        for j in range(len(geburtstage[i])):
            print(geburtstage[i][j], end=".")

def s(geburtstage):
    for key in geburtstage.keys():
        print(key)
    name = str(input("Wer suchen Sie?"))
    for i in range(len(geburtstage[name])):
        print(geburtstage[name][i], end=".")

while(start):
    e = input(print_menu())
    if e == "n":
        n(geburtstage)
    if e == "d":
        d(geburtstage)
    if e == "l":
        l(geburtstage)
    if e == "s":
        s(geburtstage)
    if e == "q":
        start = False


