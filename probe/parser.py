def parse_weight(str_input: str) -> tuple[float, str]:
    t = str_input.strip()
    try:
        if t[1] not in ("mg", "g","k"):
            raise ValueError("Ungultige Einheit")

    except (IndexError, ValueError):
        print("Ungultige Zahl")
        return 0, "kg"

    return float(t[0]), t[1]

def normalize(start_weight: tuple[float, str], target_unit: str) -> tuple[float, str]:
    if start_weight[1] == target_unit:
        return start_weight

    if start_weight[1] == "mg":
        w1 = 1
    elif start_weight[1] == "g":
        w1 = 1000
    elif start_weight[1] == "kg":
        w1 = 1000000
    else:
        print("Ungultige Einheit")
        return 0, "kg"

    if target_unit == "mg":
        w2 = 1
    elif target_unit == "g":
        w2 = 1000
    elif target_unit == "kg":
        w2 = 1000000
    else:
        print("Ungultige Einheit")
        return 0, "kg"

    return start_weight[0]*w1/w2, target_unit

def add(weight1: str, weight2: str)-> tuple[float, str]:
    weight1 = parse_weight(weight1)
    weight2 = normalize(parse_weight(weight2), weight1[1])
    return weight1[0] + weight2[0], weight1[1]