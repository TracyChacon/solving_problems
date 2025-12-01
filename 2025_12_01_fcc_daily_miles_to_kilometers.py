# Miles to Kilometers

# Given a distance in miles as a number, return the equivalent distance in kilometers.

#     The input will always be a non-negative number.
#     1 mile equals 1.60934 kilometers.
#     Round the result to two decimal places.

def convert_to_km(miles: int | float) -> str:
    KILOMETERS_PER_MILE = 1.60934
    
    # 1. Apply the mathematical precision requirement (round to 2 decimals)
    kilometers = round(miles * KILOMETERS_PER_MILE, 2)
    
    # 2. Check if the rounded result is an exact integer (e.g., 1.0, 32.0)
    if kilometers.is_integer():
        # Return the clean integer as a string (e.g., "1" or "32")
        return str(int(kilometers))
    
    # 3. Otherwise, return the float's string representation, which naturally
    # drops trailing zeros (e.g., 33.80 becomes "33.8").
    return str(kilometers)

if __name__ == '__main__':
    # Tests

    # Test 1 should return 1.61.
    print(convert_to_km(1))
    # Test 2 should return 33.8.
    print(convert_to_km(21))
    # Test 3 should return 5.63.
    print(convert_to_km(3.5))
    # Test 4 should return 0.
    print(convert_to_km(0))
    # Test 5 should return 1.
    print(convert_to_km(0.621371))