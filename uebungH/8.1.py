from turtle import *

def painter():
    # Startwerte
    start = (-100, -100)
    scale = 0.99 # =1 : endlossschleife, !=1: spiral
    #im Zentrum schrumpft die Länge sehr langsamer und langsamer

    # Turtle vorbereiten
    speed(0)
    goto(*start)
    dot()
    pendown()
    degrees()

    def run(length, angle):
        while length >= 1:
            forward(length)
            left(angle)
            dot()
            length *= scale

    def walk(length, angle):
        if length < 1:
            return
        forward(length)
        left(angle)
        #dot()
        walk(scale * length, angle)
        dot()#Punkte werden nur für sehr kleine length (<1) gesetzt


    walk(100, 38)


'''    def walk(length, angle):
        forward(length) # geht nach vorne
        left(angle) # dreht sich um angle
        #dot() #Punkt zeichnen
        walk(scale * length, angle) # rekursion
        dot() #walk und dot tauschen
        #nur ersten Punkt zeichnen #weil es eine Rekursion vorher gibt
        return'''



# Programm starten
painter()
done()


