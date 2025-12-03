# Türme
A = [4, 3, 2, 1]   # Startturm
B = []             # Hilfsturm
C = []             # Zielturm

def show():
    print(A)
    print(B)
    print(C)
    print("-----")

# Anfang
show()

# 1. bewege 1 von A → B
B.append(A.pop()); show()
# 2. bewege 2 von A → C
C.append(A.pop()); show()
# 3. bewege 1 von B → C
C.append(B.pop()); show()
# 4. bewege 3 von A → B
B.append(A.pop()); show()
# 5. bewege 1 von C → A
A.append(C.pop()); show()
# 6. bewege 2 von C → B
B.append(C.pop()); show()
# 7. bewege 1 von A → B
B.append(A.pop()); show()
# 8. bewege 4 von A → C
C.append(A.pop()); show()
# 9. bewege 1 von B → C
C.append(B.pop()); show()
#10. bewege 2 von B → A
A.append(B.pop()); show()
#11. bewege 1 von C → A
A.append(C.pop()); show()
#12. bewege 3 von B → C
C.append(B.pop()); show()
#13. bewege 1 von A → B
B.append(A.pop()); show()
#14. bewege 2 von A → C
C.append(A.pop()); show()
#15. bewege 1 von B → C
C.append(B.pop()); show()