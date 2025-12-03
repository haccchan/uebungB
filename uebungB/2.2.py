zahl1 = int(input("Zahl1: "))
zahl2 = int(input("Zahl2: "))

if zahl1>zahl2:
    anfang = zahl2
    ende = zahl1
if zahl2>zahl1:
    anfang = zahl1
    ende = zahl2
else:
    summe = zahl1

#Lösungsweg 1, mathematischer Weg mit absolut
summe1 = ((zahl1+zahl2)*((abs(zahl1-zahl2))+1)/2)
print("Summe:", summe1)

#Lösungsweg 2, mathematischer Weg ohne absolut
summe2 = (anfang + ende) * (ende - anfang+1) / 2
print("Summe:", summe2)

#Lösungsweg 3, mit Scleife
summe : int = 0
for i in range(anfang, ende+1, 1):
        summe = summe + i
print("Summe:", summe)

#Lösungsweg 4, mit Rekursion
def sum(z1, z2):
    if z1 == z2:
        return z1
    elif z1 > z2:
        return z1 + sum(z1-1, z2)
    elif z1 < z2:
        return z1 + sum(z1+1, z2)

print("Summe:", sum(zahl1,zahl2))