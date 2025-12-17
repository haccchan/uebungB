def iterative_T(n):
    T = 1
    for i in range(1, n + 1):
        T += i
    return T

def rekursive_T(n):
    if n == 0:
        return 1
    return rekursive_T(n - 1) + n

def test():
    with open("test_daten.txt") as f:
        for line in f:
            n = int(line.strip())
            print(n, iterative_T(n), rekursive_T(n))


def menu():
    print("1: iterative_T")
    print("2: rekursive_T")
    print("3: test")
    choice = input("Auswahl: ")

    if choice == "1":
        n = int(input("n eingeben: "))
        print(iterative_T(n))
    elif choice == "2":
        n = int(input("n eingeben: "))
        print(rekursive_T(n))
    elif choice == "3":
        test()
    else:
        print("Ungültige Auswahl")


menu()