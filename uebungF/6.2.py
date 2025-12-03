class Person:

    def __init__(self, vorname : str, nachname : str, jahr: int, monat : int, tage : int, telefon : str, email : str):
        self.vorname = vorname
        self.nachname = nachname
        self.telefon = telefon
        self.email = email

        self.__jahr = jahr
        self.__monat = monat
        self.__tage = tage

    def get_geburtsdatum(self):
        return self.__jahr, self.__monat, self.__tage

geburtstage = {
    "1" : Person("Trang", "Pham", 2005, 11, 7, "2944", "ptirhjt"),
   "2" : Person("Max", "Mustermann", 1990, 1, 3, "1234", "max@test.de")
}

# geburtstage["1"].vorname = "Le Pham"

def print_menu():
    return "\n (n) neuen Eintrag anlegen \n (d) einen Eintrag löschen \n (s) nach einer Person suchen \n (l) alle Einträge auflisten \n (q) Kalenderprogramm beenden "

def n():
    vorname = str(input("Geburtstag Vorname: "))
    nachname = str(input("Geburtstag Nachname: "))
    jahr = int(input("Geburtstag Jahr: "))
    monat = int(input("Geburtstag Monat: "))
    tage = int(input("Geburtstag Tage: "))
    telefon = str(input("Geburtstag Telefon: "))
    email = str(input("Geburtstag Email: "))

    person = Person(vorname, nachname, jahr, monat, tage, telefon, email)
    key = vorname + " " + nachname
    geburtstage[key] = person

def d():
    for key, person in geburtstage.items():
        print( key , ". " ,person.vorname ," ", person.nachname)
    name = str(input("Welcher Kontakt möchten Sie löschen? (Ordnung eingeben)"))
    geburtstage.pop(name)

def l():
    for key, person in geburtstage.items():
        print(person.vorname + " " + person.nachname +
              ", Geburtstag: " + str(person.get_geburtsdatum()) +
              ", Telefon: " + person.telefon +
              ", Email: " + person.email)


def s():
    for key in geburtstage.keys():
        print(key)
    name = str(input("Wer suchen Sie?"))
    print(geburtstage[name].get_geburtsdatum())
    print(geburtstage[name].vorname + " " + geburtstage[name].nachname + ": "
                ", Geburtstag: " + str(geburtstage[name].get_geburtsdatum()) +
          ", Telefon: " + geburtstage[name].telefon +
          ", Email: " + geburtstage[name].email)


start = True
while(start):
    e = input(print_menu())
    if e == "n":
        n()
    if e == "d":
        d()
    if e == "l":
        l()
    if e == "s":
        s()
    if e == "q":
        start = False
