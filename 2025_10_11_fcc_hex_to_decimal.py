# Hex to Decimal
# Given a string representing a hexadecimal number (base 16), return its decimal (base 10) value as an integer.

# Hexadecimal is a number system that uses 16 digits:

# 0-9 represent values 0 through 9.
# A-F represent values 10 through 15.
# Here's a partial conversion table:

# Hexadecimal	Decimal
# 0	0
# 1	1
# ...	...
# 9	9
# A	10
# ...	...
# F	15
# 10	16
# ...	...
# 9F	159
# A0	160
# ...	...
# FF	255
# 100	256
# The string will only contain characters 0–9 and A–F.

def hex_char_to_dec_int(string: str) -> int:
    hexadecimal = "0123456789ABCDEF"
    
    return hexadecimal.index(string)

def hex_to_decimal(hex: str) -> int:
    BASE = 16
    position = len(hex) - 1
    accumulator = 0
   
    for weight in range(len(hex)):
        decimal_int = hex_char_to_dec_int(hex[position])
        accumulator += decimal_int * BASE**weight
        position -= 1
    return accumulator


if __name__ == "__main__":
    # should return 10
    print(hex_to_decimal("A"))
    # should return 21
    print(hex_to_decimal("15"))
    # should return 46
    print(hex_to_decimal("2E"))
    # should return 255
    print(hex_to_decimal("FF"))
    # should return 2623
    print(hex_to_decimal("A3F"))