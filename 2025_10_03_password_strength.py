def isspecial(char: str) -> bool:
    SPECIAL_CHARS = '!@#$%^&*'
    return char in SPECIAL_CHARS

def check_strength(password: str) -> str:
    strength = 0

    rules = {
        'is_upper': False,
        'is_lower': False,
        'is_number': False,
        'is_special': False,
        'length_greater_than_8': False,
    }

    for char in password:
        if char.isupper():
            rules["is_upper"] = True
        if char.islower():
            rules["is_lower"] = True
        if char.isdigit():
            rules["is_number"] = True
        if isspecial(char):
            rules["is_special"] = True

    if len(password) >= 8:
        rules['length_greater_than_8'] = True
    # if one is true but not the other then make both false so not to count them
    if rules["is_lower"] ^ rules["is_upper"] :
        rules["is_lower"] = False
        rules["is_upper"] = False
    # Since these two rules count as one subtract one from strength int
    elif rules["is_lower"] and rules["is_upper"]:
        strength -= 1


    strength += sum(rules.values())

    match strength:
        case score if score >= 4:
            return "strong"
        case score if 2 <= score < 4:
            return "medium"
        case score if score <= 1:
            return "weak"
        case _:
            return "Error: Something went wrong"