#1.1

def countIn(text: str, zeichen: str) -> int:
    try:
        return text.count(zeichen)
    except TypeError or (text == ""):
        return -1

#1.2
def convertInput(input_number: str) -> float:
    while True:
        try:
            return float(input_number)
        except ValueError:
            print("nicht gültig")
            input_number = input("Eintrag: ")

#1.3
def teileString(text:str, zeichen: str) -> list:
    if len(zeichen) != 1:
        return []
    return text.split(zeichen)

#testcases
if __name__ == "__main__":
    print(countIn("Zur Kreuzigung? Gut. Durch die Tür hinaus, zur linken Reihe, jeder nur ein Kreuz.","K"))
    print(countIn("Was macht die Knackwurst so knackig? Das N.","k"))
    print(convertInput("42"))
    print(convertInput("4+3"))
    print(convertInput("9.16"))
    print(convertInput("9,16"))
    print(convertInput("9"))
    print(teileString("Wie heißt ein Bär, der fliegen kann? Hubschraubär","?"))
    print(teileString("Durch die Tür hinaus, zur linken Reihe, jeder nur ein Kreuz.",","))
