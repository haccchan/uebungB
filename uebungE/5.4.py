satz : str = "Vitaler Nebel mit Sinn ist im Leben relativ"

def istPalindrom(s):
    s = s.lower().replace(" ", "")
    for i in range(len(s)-1):
        if s[i] != s[-i-1]:
            return False

    return True

print(istPalindrom(satz))