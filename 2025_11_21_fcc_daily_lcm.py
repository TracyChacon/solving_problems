# LCM

# Given two integers, return the least common multiple (LCM) of the two numbers.

# The LCM of two numbers is the smallest positive integer that is a multiple of both numbers. For example, given 4 and 6, return 12 because:

#     Multiples of 4 are 4, 8, 12 and so on.
#     Multplies of 6 are 6, 12, 18 and so on.
#     12 is the smallest number that is a multiple of both.


####################################################################
# Initial Code                                                     #
####################################################################
# def gcd(a:int, b:int) -> int:
#     if a == 0 and b == 0:
#         return 0

#     larger_number = 0
#     smaller_number = 0
#     remainder = 0

#     if a > b:
#         larger_number = a
#         smaller_number = b
#     elif a < b:
#         larger_number = b
#         smaller_number = a

#     while True:
#         remainder = larger_number % smaller_number
#         if remainder == 0:
#             return smaller_number
#         larger_number = smaller_number
#         smaller_number = remainder

# def lcm(a:int, b:int) -> int:
#     return int(a * b / gcd(a, b))


####################################################################
# Improved Code                                                    #
####################################################################

def gcd(a:int, b:int) -> int | str:
    # Use absolute values for correct GCD calculation
    a, b = abs(a), abs(b)
    # Handle cases where one or both numbers are zero
    # GCD(x, 0) = |x|. If both are 0, it returns 0 (per programming convention)
    if a == 0:
        return b
    if b == 0:
        return a
    # The algorithm works correctly whether a>b or b>a, so an explicit setup block is often unnecessary if you use Python's way of swapping variables.
    # Where a is the old divisor, and b is the new remainder
    while b:
        a, b = b, a % b

    return a 

def lcm(a:int, b:int) -> int:
    # Handle cases where one or both numbers are zero
    if a == 0 or b == 0:
        return 0
    # Apply the LCM formula
    # Use integer division (//) and absolute value for the guaranteed positive result
    return abs(a * b) // gcd(a, b)

if __name__ == '__main__':
    # Tests

    # Test 1 should return 12.
    print(lcm(4, 6))
    # Test 2 should return 18.
    print(lcm(9, 6))
    # Test 3 should return 100.
    print(lcm(10, 100))
    # Test 4 should return 221.
    print(lcm(13, 17))
    # Test 5 should return 630.
    print(lcm(45, 70))
    # Test 6 should return 750.
    print(lcm(125, 30))