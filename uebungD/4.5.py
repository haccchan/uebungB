import random

# Spielerlisten
tor = ["Neuer", "ter Stegen", "Trapp"]

abwehr = ["Boateng", "Ginter", "Hector", "Hummels",
          "Ruediger", "Schulz", "Sueele"]

mittelfeld = ["Brandt", "Can", "Draxler", "Goretzka", "Guendogan",
              "Kroos", "Mueller", "Rudy"]

angriff = ["Gnabry", "Reus", "Sane", "Werner"]

import random

# Torwart (1 Spieler)
torwart = random.choice(tor)

# 4 Abwehrspieler zufällig auswählen
abwehr_auswahl = random.sample(abwehr, 4)

# 4 Mittelfeldspieler zufällig auswählen
mittelfeld_auswahl = random.sample(mittelfeld, 4)

# 2 Angreifer zufällig auswählen
angriff_auswahl = random.sample(angriff, 2)

# Ausgabe
print("Tor:", torwart)
print("Abwehr:", ", ".join(abwehr_auswahl))
print("Mittelfeld:", ", ".join(mittelfeld_auswahl))
print("Angriff:", ", ".join(angriff_auswahl))