geburtstage = {
    "A": (2000, 5, 21),
    "B": (1999, 12, 4),
    "C": (2001, 3, 15)
}

print("Geburtstag von A:", geburtstage["A"])

geburtstage["D"] = (1998, 7, 9)

# "E" bekommt den Geburtstag von "D" und "D" wird entfernt mit pop()
geburtstage["E"] = geburtstage.pop("D")

# Wert von "C" ändern
geburtstage["C"] = (2001, 3, 16)

# "B" entfernen
geburtstage.pop("B")

print("Aktuelle Geburtstagsliste:")
print(geburtstage)

#Keys (Namen) können nicht direkt umbenannt werden, man muss löschen & neu hinzufügen.
#Werte (Geburtstage) können leicht geändert werden
