def recursive_solution(x: int) -> int:
    if x == 0 :
        return 0
    return x + recursive_solution(x-1)

def iterative_solution(x: int) -> int:
    res = 0
    for i in range(1,x+1):
        res = res + i
    return res

def second_recursion(x: float) -> float:
    if x <= 0:
        return 1
    return second_recursion(x-1) + 2*second_recursion(x-2)