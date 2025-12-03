print("Ausgabe")
print("Tilgungsplan")
n = int(input("Geben Sie bitte die gewünschte Annuität ein:"))

s : float = 10000
r : float = 0.07
j : int = 1

while(s>0):
    z = round(r*s)
    t = round(n - r*s)
    s = round(s - t)
    print("Jahr: ",j, " | Zinsen: ", z,"€ | Tilgung: ", t, "€ | Restschuld: ", s , "€")
    j = j +1
    if(s<n):
        print("Jahr: ", j, " | Zinsen: ", z, "€ | Tilgung: ", t, "€ | Restschuld: 0€")
        z = round(r * s)
        t = round(n - r * s)
        s = round(s - t)
        print("Zurückgeben:", s*(-1) ,"€")
        break