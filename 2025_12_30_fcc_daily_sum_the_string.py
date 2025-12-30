# Sum the String

# Given a string containing digits and other characters, return the sum of all numbers in the string.

#     Treat consecutive digits as a single number. For example, "13" counts as 13, not 1 + 3.
#     Ignore any non-digit characters.

import re

def string_sum(s: str) -> int:
   numbers_list = re.split(r'\D+', s)

   numbers = [int(n) for n in numbers_list if n]

   return sum(numbers)

if __name__ == "__main__":
    # Tests

    # Test 1 should return 5.
    print(string_sum("3apples2bananas"))
    # Test 2 should return 17.
    print(string_sum("10cats5dogs2birds"))
    # Test 3 should return 125344.
    print(string_sum("125344"))
    # Test 4 should return 321.
    print(string_sum("a1b20c300"))
    # Test 5 should return 1653.
    print(string_sum("a12b34c56d78e90f123g456h789i0j1k2l3m4n5"))