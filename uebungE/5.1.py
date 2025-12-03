l1 = [8,2,3,0,7]
def f(list):
    s: int = 0
    for i in list:
        s = s + i

    return s

print(f(l1))