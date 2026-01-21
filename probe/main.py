from kollektion import *
from rekursion import *
from parser import *
def show_menue() :
    e = input("Bitte geben Sie ein\n(1)Kollektion\n(2)Rekursion\n(3)Parser\n(4)Programm beenden")
    if e == "1" :
        print(d1())

    elif e == "2" :
        e2 = int(input("Geben Sie x ein"))
        if e2 == 9:
            print(second_recursion(e2))
        if (recursive_solution(e2)) == (iterative_solution(e2)):
            print(recursive_solution(e2))
        else:
            print("Fehlermeldung")
    elif e == "3" :
        print(parse_weight("23.5 kg"))
        print(normalize(parse_weight("23.5 kg"),"g"))
        add("136 g","5.109 kg")
