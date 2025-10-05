def to_binary(decimal: int) -> str:
    binary_string = ""
    while(decimal >= 1):
        remainder = decimal % 2
        binary_string = str(remainder) + binary_string
        decimal //= 2

    return binary_string

if __name__ == "__main__":
    # print(to_binary(12))
    print(to_binary(5))