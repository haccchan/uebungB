string = "Aa 2"
def zahlen(s):
    low : int = 0
    high : int = 0
    for i in s:

        if i.islower():
            low += 1
        elif i.isupper():
            high += 1
    return low,high

print(zahlen(string))