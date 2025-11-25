


#     Daily Coding Challenge
#     November 25, 2025

# FizzBuzz

# Given an integer (n), return an array of integers from 1 to n (inclusive), replacing numbers that are multiple of:

#     3 with "Fizz".
#     5 with "Buzz".
#     3 and 5 with "FizzBuzz".

def fizz_buzz(n):
    fizz_buzz_list = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            fizz_buzz_list.append('FizzBuzz')
        elif i % 3 == 0:
            fizz_buzz_list.append('Fizz')
        elif i % 5 == 0:
            fizz_buzz_list.append('Buzz')
        else:
            fizz_buzz_list.append(i)
    return fizz_buzz_list

def fizz_buzz_pythonic(n):
    return ['FizzBuzz' if i % 15 == 0 else
            'Fizz' if i % 3 == 0 else
            'Buzz' if i % 5 == 0 else
            i
            for i in range(1, n + 1)
    ]


# Tests

# Test 1 should return [1, 2].
print(fizz_buzz(2))
# Test 2 should return [1, 2, "Fizz", 4].
print(fizz_buzz(4))
# Test 3 should return [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8].
print(fizz_buzz(8))
# Test 4 should return [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz"].
print(fizz_buzz(20))
# Test 5 should return [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz", "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz", 28, 29, "FizzBuzz", 31, 32, "Fizz", 34, "Buzz", "Fizz", 37, 38, "Fizz", "Buzz", 41, "Fizz", 43, 44, "FizzBuzz", 46, 47, "Fizz", 49, "Buzz"].
print(fizz_buzz(50))