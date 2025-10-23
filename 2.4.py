s = input("Geben Sie eine beliebig lange Reihe von Ziffern (0-9) ein, diese sollen jeweils durch ein Leerzeichen getrennt sein.")
summe : int = 0
for i in range (0,len(s),1):
    if s[i] != " ":
        summe += int(s[i])

print(summe)