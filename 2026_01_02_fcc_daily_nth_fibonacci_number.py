# Nth Fibonacci Number

# Given an integer n, return the nth number in the fibonacci sequence.

# The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. The first 10 numbers in the sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

def nth_fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    # Initialize the first two numbers
    a, b = 0, 1
    
    # Calculate up to n
    for _ in range(2, n + 1):
        # Update a and b: next number is the sum of previous two
        a, b = b, a + b
        
    return a

if __name__ == '__main__':
    # Tests

    # Test 1 should return 2.
    print(nth_fibonacci(4))
    # Test 2 should return 34.
    print(nth_fibonacci(10))
    # Test 3 should return 377.
    print(nth_fibonacci(15))
    # Test 4 should return 63245986.
    print(nth_fibonacci(40))
    # Test 5 should return 1304969544928657.
    print(nth_fibonacci(75))