z : int = 2
def primpruf(x):
    if(x>0&x<3):
        return True
    elif(x<=0):
        return False
    else:
        ist_prim = True
        for i in range(3, x + 1):
            for j in range(2, i):
                if i % j == 0:
                    ist_prim = False
                    break
        return ist_prim


print(primpruf(z))