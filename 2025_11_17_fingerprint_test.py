# Fingerprint Test

# Given two strings representing fingerprints, determine if they are a match using the following rules:

#     Each fingerprint will consist only of lowercase letters (a-z).
#     Two fingerprints are considered a match if:
#         They are the same length.
#         The number of differing characters does not exceed 10% of the fingerprint length.

# def is_match(fingerprint_a: str, fingerprint_b: str) -> bool:
#     if len(fingerprint_a) != len(fingerprint_b):
#         return False
#     # Keep track of differing letters  
#     count = 0
#     # Loop and compare characters of the same position in each string
#     for idx in range(len(fingerprint_a)):
#         if fingerprint_a[idx] != fingerprint_b[idx]:
#             count += 1
#     # Check for 10% or less differing characters 
#     if count / len(fingerprint_a) * 100 <= 10:
#         return True

#     return False

def is_match(fingerprint_a: str, fingerprint_b: str) -> bool:
    if len(fingerprint_a) != len(fingerprint_b):
        return False
    len_a = len(fingerprint_a)
    # Keep track of differing letters  
    count = 0
    # Loop and compare characters of the same position in
    # each string
    # The zip() function takes multiple iterables (like 
    # strings, lists, or tuples) and returns an iterator of
    # tuples. Each tuple contains the element from the first
    # iterable, followed by the element from the second, and
    # so on, all taken from the same index.
    for char_a, char_b in zip(fingerprint_a, fingerprint_b):
        if char_a != char_b:
            count += 1
    # Check for 10% or less differing characters
    # Simplified conditional logic calculation using integer
    # arithmatic instead of floating-point arithmatic 
    # => count / len_a <= 10 / 100 
    # => count / len_a * 100 <= 10 / 100 * 100
    # => count / len_a * 100 <= 10
    # => count / len_a * len_a * 100 <= 10 * len_a
    # => count * 100 <= 10 * len_a
    # => count * 100 / 10 <= 10 / 10 * len_a
    # => count * 10 <= 1 * len_a
    # => count * 10 <= len_a
    if count * 10 <= len_a:
        return True

    return False

# Tests

# Test 1 should return True.
# print(is_match("helloworld", "helloworld"))
# Test 2 should return False.
# print(is_match("helloworld", "helloworlds"))
# Test 3 should return True.
# print(is_match("helloworld", "jelloworld"))
# print(is_match("helloworlx", "jelloworlz"))
# Test 4 should return True.
# print(is_match("thequickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthelazydog"))
# Test 5 should return True.
# print(is_match("theslickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthehazydog"))
# Test 7 should return False.
print(is_match("thequickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthehazycat"))