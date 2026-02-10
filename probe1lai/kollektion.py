#l1

def l1() -> list[int]:
    return [(x**2) for x in range(-20,23) if x%2==0]
#l2

def l2() -> list[int]:
    return [(x+1)**3 for x in range(-10,12)]

#d1 gop l1 l2

def d1() -> dict[int, int]:
    return dict(zip(l1(), l2()))

