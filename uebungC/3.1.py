l1 = []
for i in range(1, 101):
    l1.append(i)

print("Liste l1:", l1)

index = int(input("Bitte geben Sie einen Index zwischen 0 und 99 ein: "))

wert = l1[index]
l1.pop(index)
l1.append(wert)

l2 = l1.copy()
l2.reverse()

print("Neue Liste l1:", l1)
print("Invertierte Liste l2:", l2)