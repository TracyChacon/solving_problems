# Integer Sequence
# Given a positive integer, return a string with all of the integers from 1 up to, and including, the given number, in numerical order.

# For example, given 5, return "12345".

# def sequence(n: int) -> str:
#     return "".join([str(num) for num in range(1, n + 1)])
def sequence(n: int) -> str:
    return "".join(str(num) for num in range(1, n + 1))
   


# Test 1 should return "12345".
print(sequence(5))
# Test 2 should return "12345678910".
print(sequence(10))
# Test 3 should return "1".
print(sequence(1))
# Test 4 should return "123456789101112131415161718192021222324252627".
print(sequence(27))