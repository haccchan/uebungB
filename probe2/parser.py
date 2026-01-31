#1.1

def countIn(text: str, zeichen: str) -> int:
    try:
        z: int = 0
        for i in range(len(text)):
            if text[i] == zeichen:
                z += 1
        return z
    except TypeError or (text == ""):
        return -1

#1.2
def convertInput(input_number: str) -> float:
    return float(input_number)

def convertInput2(input_number: str) -> float:
    try:
        result = convertInput(input_number)
        print(result)
        return result

    except ValueError:
        print("nicht gültig")
        a: bool = True
        while a:
            e = input("Eintrag: ")
            try:
                result = convertInput(e)
                print(result)
                return result
            except ValueError:
                print("nicht gültig")


#1.3
def teileString(text:str, zeichen: str) -> list:
    if len(zeichen) != 1:
        return []
    return text.split(zeichen)

#testcases
if __name__ == "__main__":
    print(countIn("Zur Kreuzigung? Gut. Durch die Tür hinaus, zur linken Reihe, jeder nur ein Kreuz.","K"))
    print(countIn("Was macht die Knackwurst so knackig? Das N.","k"))
    convertInput2("42")
    convertInput2("4+3")
    convertInput2("9.16")
    convertInput2("9,16")
    convertInput2("9")
    print(teileString("Wie heißt ein Bär, der fliegen kann? Hubschraubär","?"))
    print(teileString("Durch die Tür hinaus, zur linken Reihe, jeder nur ein Kreuz.","."))
