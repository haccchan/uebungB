A = [4,3,2,1]  # Startturm (oben liegt die kleinste Zahl)
n = len(A)
B = []                     # Zwischenturm
C = []                     # Zielturm

def ausgabe():
    print(A)
    print(B)
    print(C)
    print("-----")

def bewegen(X, Y):
    """Führe die einzig gültige Bewegung zwischen zwei Türmen aus."""
    if not X:               # X leer → nimm von Y nach X
        X.append(Y.pop())
    elif not Y:             # Y leer → nimm von X nach Y
        Y.append(X.pop())
    elif X[-1] < Y[-1]:     # kleiner oben auf X → lege nach Y
        Y.append(X.pop())
    else:                   # sonst lege von Y nach X
        X.append(Y.pop())

ausgabe()

# Reihenfolge der Pegelpaare hängt von der Parität von n ab
ordnung = [(A, B), (A, C), (B, C)]

schritt = 2**n - 1

for i in range(schritt):
    X, Y = ordnung[i % 3]
    bewegen(X, Y)
    ausgabe()