# What's My Age Again?

# Given the date of someone's birthday in the format YYYY-MM-DD, return the person's age as of November 27th, 2025.

#     Assume all birthdays are valid dates before November 27th, 2025.
#     Return the age as an integer.
#     Be sure to account for whether the person has already had their birthday in 2025.

def calculate_age(birthday: str) -> int:
    
    return 1
# Tests
if __name__ == '__main__':
    # Test 1 should return 25.
    print(calculate_age("2000-11-20"))
    # Test 2 should return 24.
    print(calculate_age("2000-12-01"))
    # Test 3 should return 11.
    print(calculate_age("2014-10-25"))
    # Test 4 should return 31.
    print(calculate_age("1994-01-06"))
    # Test 5 should return 30.
    print(calculate_age("1994-12-14"))