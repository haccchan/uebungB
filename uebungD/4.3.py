wort = input("Geben Sie das Wort ein: ")
print("Das Wortratespiel Galgenmännchen beginnt!")

l = ['_'] * len(wort)
boolean = True
v = 0

while boolean:
    print("".join(l))
    buchstabe = input("Geben Sie den Buchstaben ein: ")

    f = 0
    for i in range(len(wort)):
        if buchstabe == wort[i]:
            l[i] = wort[i]
        else:
            f += 1

    if f == len(wort):
        v += 1
        print("Falsch! Fehlversuch:", v)

    if "".join(l) == wort:
        boolean = False
        print("Gewonnen! Das Wort war:", wort)
        print("Fehlversuche:", v)

    if(v>5):
        boolean = False
        print("Verloren! Schwach! Antwort:", wort)