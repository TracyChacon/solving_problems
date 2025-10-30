# Nth Prime
# A prime number is a positive integer greater than 1 that is divisible only by 1 and itself. The first five prime numbers are 2, 3, 5, 7, and 11.

# Given a positive integer n, return the nth prime number. For example, given 5 return the 5th prime number: 11.



# def is_prime(num: int) -> bool:
#     """
#     Checks if a given number is prime using the 6k ± 1 optimization.
#     Time Complexity: O(sqrt(num))
#     """
#     if num <= 1:
#         return False
#     if num <= 3:
#         return True
#     # Rule 1: If num is divisible by 2 or 3, it's not prime
#     if num % 2 == 0 or num % 3 == 0:
#         return False
    
#     # Rule 2: Check for factors up to sqrt(num)
#     # Start checking from 5, increment by 6 (5, 11, 17, 23, ...)
#     # This checks numbers of the form 6k ± 1
#     i = 5
#     while i * i <= num:
#         if num % i == 0 or num % (i + 2) == 0:
#             return False
#         i += 6
#     return True

# def nth_prime(n: int) -> int:
#     """
#     Returns the nth prime number using optimized trial division (6k ± 1).
#     """

#     if n <= 0:
#         raise ValueError("n must be a positive integer.")
    
#     # Handle the first few primes explicitly
#     if n == 1: return 2
#     if n == 2: return 3
#     if n == 3: return 5
    
#     # Initialization for the main search loop (starting the 6k ± 1 sequence)
#     count = 3    # We've already accounted for the first three primes (2, 3, 5)
#     num = 7      # Start checking with the next prime candidate, which is 6*1 + 1
    
#     # Loop until the nth prime is found
#     while count < n:
#         # Check num (6k + 1)
#         if is_prime(num):
#             count += 1
#             if count == n:
#                 return num
        
#         # Check num + 4 (6k + 5, which is the next prime candidate in the sequence)
#         # We only check this if the nth prime hasn't been found yet.
#         if is_prime(num + 4):
#             count += 1
#             if count == n:
#                 return num + 4
        
#         # Move to the next 6k+1 candidate (e.g., from 7 to 13)
#         num += 6
            
#     # This line should technically be unreachable given the logic above
#     # but provides a safe fallback return if the loop condition were somehow violated.
#     return num





import math

def prime_limit(n: int) -> int:
    if n < 6:
        return 13
    
    limit = int(n * (math.log(n) + math.log(math.log(n))))
    
    return limit + 100

def sieve_of_eratosthenes(limit: int) -> list[int]:
    if limit < 2:
        return []
    
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for multiple in range(i**2, limit + 1, i):
                is_prime[multiple] = False
    
    primes = [num for num, is_p in enumerate(is_prime) if is_p]

    return primes

def nth_prime(n: int) -> int:
    if not isinstance(n, int) or n <=0:
        raise ValueError('n must be positive integer.')
    
    limit = prime_limit(n)
    primes = sieve_of_eratosthenes(limit)

    if n > len(primes):
        raise RuntimeError("Sieve limit was to low. Increase the limit estimate.")
    
    return primes[n - 1]



if __name__ == "__main__":
    # Test 1 should return 11.
    print(f"5th prime: {nth_prime(5)}")
    # Test 2 should return 29.
    print(f"10th prime: {nth_prime(10)}")
    # Test 3 should return 53.
    print(f"16th prime: {nth_prime(16)}")
    # Test 4 should return 523.
    print(f"99th prime: {nth_prime(99)}")
    # Test 5 should return 7919.
    print(f"1000th prime: {nth_prime(1000)}")
    # Test 6 should return 104729 (the 10,000th prime).
    print(f"10000th prime: {nth_prime(10000)}")