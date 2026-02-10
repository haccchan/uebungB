from kollektion import *
from rekursion import *
from parser import *

def menu():
    e = input("Geben Sie Nummer ein. \n Kollektion : 1 \n Rekursion, Interation: 2 \n Parser : 3")
    if e == "1":
        print(l1())
        print(l2())
        print(d1())
    if e == "2":
        try:
            z = int(input("Geben Sie Zahl: "))
            r = recursive_solution(z)
            i = iterative_solution(z)

            print(r)
            print(i)

            if r != i:
                raise ValueError

        except ValueError:
            print("Invalid input")

        print(second_recursion(9))

        if e == "3":
            z = input("Geben Sie ein: ")
            z1 = parse_weight(z)
            print(z1)
            print(normalize(z1), "g")
            print(add("136g", "5.109kg"))


menu()