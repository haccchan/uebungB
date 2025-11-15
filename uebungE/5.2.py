z = 2
minf=5
maxf=10

def f(x,min,max):
    if ((x < min)|(x > max)):
        return False
    else:
        return True

print(f(z,minf,maxf))