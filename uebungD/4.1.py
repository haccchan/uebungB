print("Geben Sie eine ganzzahlige positive Zahl ein:")
x = int(input())

# Liste der Primzahlen
primzahl = [2]

# Primzahlen finden
for i in range(3, x+1):
    ist_prim = True
    for j in range(2, i):
        if i % j == 0:
            ist_prim = False
            break
    if ist_prim:
        primzahl.append(i)

# Primfaktoren sammeln
faktoren = []
zahl = x

k = 0

while k < len(primzahl):
    if zahl % primzahl[k] == 0:
        faktoren.append(primzahl[k])
        zahl = zahl / primzahl[k]
    else:
        k = k + 1

for i in range(len(faktoren)):
    if i == len(faktoren) - 1:
        print(faktoren[i])         # letzter Wert -> kein Stern
    else:
        print(faktoren[i], "*", end=" ")
