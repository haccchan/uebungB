print("Ausgabe")
print("Tilgungsplan")
n = int(input("Geben Sie bitte die gewünschte Annuität ein:"))

s = 10000
r = 0.07
j = 1
while(s>0):
    z = round(r*s)
    t = round(n - r*s)
    s = round(s - t)
    print("Jahr: ",j, " | Zinsen: ", z,"€ | Tilgung: ", t, "€ | Restschuld: ", s )
    j = j +1