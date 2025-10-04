def to_decimal(binary: str) -> int:
    accumulator = 0
    # rightmost item position index of the binary string
    position = len(binary) - 1
    # where n represents the nth binary number position
    # which happens to match indexed based lists when iterating
    for n in range(len(binary)):
        # if the number in the binary string is a `1` then add 2**n
        if int(binary[position]):
            accumulator += 2**n
        position -= 1
    return accumulator



# print(to_decimal("101"))
print(to_decimal("1010"))
print(to_decimal("10010"))
print(to_decimal("1010101"))