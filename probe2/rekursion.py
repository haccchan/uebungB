def recursive_solution(x:int, schritt : int = 1) -> int:
    print("schritt is:", schritt)
    if x == 0:
        return 0
    return x**2 + recursive_solution(x-1, schritt + 1)

def iterative_solution(x:int) -> int:
    f : int = 0
    z : int = 0
    while (x>0):
        f = f + x**2
        x = x - 1
        z = z + 1

    return f

def second_recursion(n: float) -> float:
    if n == 1:
        return 1
    if n == 0:
        return 1
    return second_recursion(n-1) + 2*(second_recursion(n-2))

if __name__ == "__main__":
    for i in range(2,11):
        recursive_solution(i)
        print(iterative_solution(i))
        print(second_recursion(i))

