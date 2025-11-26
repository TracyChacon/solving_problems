# BuzzFizz

# Given an array, determine if it is a correct FizzBuzz sequence from 1 to the last item in the array. A sequence is correct if:

#     Numbers that are multiples of 3 are replaced with "Fizz"
#     Numbers that are multiples of 5 are replaced with "Buzz"
#     Numbers that are multiples of both 3 and 5 are replaced with "FizzBuzz"
#     All other numbers remain as integers in ascending order, starting from 1.
#     The array must start at 1 and have no missing or extra elements.

def is_fizz_buzz(sequence: list[str]) -> bool:
    for i in range(1, len(sequence) + 1):
        value_in_sequence = sequence[i - 1]
        multiple_15 = i % 15 == 0
        multiple_3 = i % 3 == 0
        multiple_5 = i % 5 == 0
        fizzbuzzy = multiple_15 or multiple_3 or multiple_5 
        is_fizz = value_in_sequence == 'Fizz'
        is_buzz = value_in_sequence == 'Buzz'
        is_fizz_buzz = value_in_sequence == 'FizzBuzz'

        if multiple_15 and not is_fizz_buzz:
            return False
        elif not multiple_15 and multiple_3 and not is_fizz:
            return False
        elif not multiple_15 and not multiple_3 and multiple_5 and not is_buzz:
            return False
        elif not fizzbuzzy and not isinstance(value_in_sequence, int):
            return False
    return True

# Tests

# Test 1 should return True.
print(is_fizz_buzz([1, 2, "Fizz", 4]))
# Test 2 should return False.
print(is_fizz_buzz([1, 2, 3, 4]))
# Test 3 should return False.
print(is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", 7]))
# Test 4 should return False.
print(is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, "FizzBuzz"]))
# Test 5 should return False.
print(is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, "Fizz"]))
# Test 6 should return False.
print(is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, "Buzz"]))
# Test 7 should return True.
print(is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz", "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz", 28, 29, "FizzBuzz", 31, 32, "Fizz", 34, "Buzz", "Fizz", 37, 38, "Fizz", "Buzz", 41, "Fizz", 43, 44, "FizzBuzz", 46, 47, "Fizz", 49, "Buzz"]))