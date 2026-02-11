#f1

def recursive_solution(x: int, z: int = 0) -> int:
    if x == 0:
        print("Schritt r:", z)
        return 0
    else:
        return x + recursive_solution(x - 1, z + 1)


#f2
def iterative_solution(x: int) -> int:
    s = 0
    z = 0
#cách 1
    for i in range(1,x+1):
        s = s + i
        z += 1
#cách 2
    while x >= 0:
        s = s + x
        x = x - 1
        z +=1
#
    print("schritt i:",z)
    return s
#s
def second_recursion(x: float) -> float:
    if x <= 0:
        return 1
    return second_recursion(x-1) + 2* second_recursion(x-2)