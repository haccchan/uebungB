string : str = "Hallo Welt"

def zahlen(s):
    s = s.replace(" ", "")
    low : int = 0
    high : int = 0
    for i in s:
        if i.islower():
            low += 1
        else:
            high += 1
    return low,high

print(zahlen(string))