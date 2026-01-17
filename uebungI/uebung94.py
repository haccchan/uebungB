from uebung7 import *
class Person:

    def __init__(self, vorname: str, nachname: str,
                 jahr: int, monat: int, tag: int,
                 telefon: str, email: str):

        # einfache Validierung
        if not vorname or not nachname:
            raise ValueError("Vorname oder Nachname fehlt")

        self.vorname = vorname
        self.nachname = nachname
        self.telefon = telefon
        self.email = email

        self.__jahr = jahr
        self.__monat = monat
        self.__tag = tag

    def get_geburtsdatum(self):
        return self.__jahr, self.__monat, self.__tag

    def get_monat(self):
        return self.__monat

    def get_tag(self):
        return self.__tag

# ===================== PROGRAMMSTART =====================

def main():
    laden()

    start = True
    while start:
        e = input(print_menu())
        if e == "n":
            n()
        elif e == "d":
            d()
        elif e == "l":
            l()
        elif e == "s":
            s()
        elif e == "b":
            b()
        elif e == "q":
            start = False