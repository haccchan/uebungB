def power(x,n):
    if n == 1:
        return x
    return power(x,n//2) * power(x,n-n//2)

def power2(x, n, speicher={}):
    if n in speicher:
        return speicher[n]
    if n == 1:
        return x
    speicher[n] = power(x, n//2) * power(x, n - n//2)
    return speicher[n]
