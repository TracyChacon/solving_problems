# Roman Numeral Builder

# Given an integer, return its equivalent value in Roman numerals.

# Roman numerals use these symbols:
# Symbol 	Value
# I 	1
# V 	5
# X 	10
# L 	50
# C 	100
# D 	500
# M 	1000

# Roman numerals are written from largest to smallest, left to right using the following rules:

#     Addition is used when a symbol is followed by one of equal or smaller value. For example, 18 is written as XVIII (10 + 5 + 1 + 1 + 1 = 18).
#     Subtraction is used when a smaller symbol appears before a larger one, to represent 4 or 9 in any place value. For example, 19 is written as XIX (10 + (10 - 1)).
#     No symbol may be repeated more than three times in a row. Subtraction is used when you would otherwise need to write a symbol more than three times in a row. So the largest number you can write is 3999.

# Here's one more example: given 1464, return "MCDLXIV" (1000 + (500 - 100) + 50 + 10 + (5 - 1)).

def to_roman(num: int) -> str:
    roman_numeral_by_base_10_position = {
    0: ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
    1: ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
    2: ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
    3: ['', 'M', 'MM', 'MMM'],}
  
    roman_numeral = []
    num_str = f"{num}"
    position = len(num_str) - 1

    
    for i in range(position + 1): 
        roman_numeral.append(roman_numeral_by_base_10_position[position][int(num_str[i])])
        position -= 1

    return "".join(roman_numeral)

if __name__ == '__main__':
    # Tests

    # Test 1 should return "XVIII".
    print(to_roman(18))
    # Test 2 should return "XIX".
    print(to_roman(19))
    # Test 3 should return "MCDLXIV".
    print(to_roman(1464))
    # Test 4 should return "MMXXV".
    print(to_roman(2025))
    # Test 5 should return "MMMCMXCIX".
    print(to_roman(3999))