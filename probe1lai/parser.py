#4.1 : chuyển str "12 kg" thành tuple ( float 12.0, "kg")
def parse_weight(str_input: str) -> tuple[float, str]:
    try:
        value_str, unit = str_input.split()
        value = float(value_str)

        if unit not in ("mg", "g", "kg"):
            raise ValueError

        return value, unit

    except Exception as e:
        print(e)
        return 1.0, str_input

#4.2 đổi đơn vị : từ "12 kg","g" thành 12000 , "g"
def normalize(start_weight: tuple[float, str], target_unit: str) -> tuple[float, str]:
    factors = {"mg": 1, "g": 1000, "kg": 1000000}
    value, unit = start_weight
    new_value = value * factors[unit] / factors[target_unit]
    return new_value, target_unit

# 4.3 cộng hai cân nặng vào : ("12kg","13000g") thành 25, "kg"
def add(weight1: str, weight2: str) -> tuple[float, str]:
    w1 = parse_weight(weight1)
    w2 = parse_weight(weight2)
    normalize(w2, w1[1])
    return w1[0] + w2[0], w1[1]
