def l1() -> list[int]:
    res = []
    for i in range(-20,23,2):
        res.append(i**2)
    return res

def l2() -> list[int]:
    res = []
    for i in range(-11,12,2):
        res.append((i+1)**3)
    return res

def d1() -> dict[int, int]:
    a = l1()
    b = l2()
    res = {}
    for i in range(0,len(a)):
        res[i] = a[i-10]
    for j in range(len(a),len(b)+len(a)):
        res[j] = b[j-20]
    return res

