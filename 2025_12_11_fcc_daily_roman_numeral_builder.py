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

######################################################################
# Positional Lookup Solution
######################################################################
# Implements rules for conversion for all numbers 1 up to 3999
def to_roman(num: int) -> str:
    if not 1 <= num <= 3999:
        raise ValueError("Input number must be between 1 and 3999")
    # Positional lookup table grouping by 1s, 10s, 100s, and 1000s and maps each digit's value directly to its corresponding Roman numeral.
    roman_numeral_by_base_10_position = {
    0: ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
    1: ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
    2: ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
    3: ['', 'M', 'MM', 'MMM'],}
  
    roman_numeral = []
    # The integer `num` is converted to a string `num_str`
    # in order to iterate over later in the for loop
    num_str = f"{num}"
    # The `power` variable tracks the current base 10 power (3 for thousands, 2 for hundreds, 1 for tens, and 0 for ones)
    power = len(num_str) - 1

    for i in range(power + 1): 
        # The `number` varible used to as index to fetch the Roman numeral 
        # representation for that place
        number = int(num_str[i])

        roman_numeral.append(roman_numeral_by_base_10_position[power][number])
        power -= 1

    return "".join(roman_numeral)

######################################################################
# Traditional Greedy Solution
######################################################################

# def to_roman(num: int) -> str:
#     # Key: Value, Value: Roman Symbol
#     roman_map = {
#         1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
#         100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
#         10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
#     }
    
#     result = []
    
#     # Iterate from largest value (1000) down to smallest (1)
#     for value, symbol in roman_map.items():
#         # Keep track of how many times this value can be subtracted
#         count = num // value 
        
#         # Append the symbol that many times
#         result.append(symbol * count)
        
#         # Subtract the total amount from the number
#         num -= value * count
        
#         # Optimization: If num is 0, we are done
#         if num == 0:
#             break
            
#     return "".join(result)

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