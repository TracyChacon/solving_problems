# Takeoff Fuel

# Given the numbers of gallons of fuel currently in your airplane, and the required number of liters of fuel to reach your destination, determine how many additional gallons of fuel you should add.

#     1 gallon equals 3.78541 liters.
#     If the airplane already has enough fuel, return 0.
#     You can only add whole gallons.
#     Do not include decimals in the return number.

import math

def fuel_to_add(current_gallons: int, required_liters: int) -> int:
    LITER_TO_GALLON_FACTOR = 3.78541 

    # Convert required_liters to gallons
    required_gallons = required_liters / LITER_TO_GALLON_FACTOR

    # Calculate the difference of current_gallons and required_gallons
    needed_gallon_amt = required_gallons - current_gallons

    # If the airplane
    if needed_gallon_amt <= 0:
        return 0
    
    return math.ceil(needed_gallon_amt)

if __name__ == "__main__":
    # Tests

    # Test 1 should return 1.
    print(fuel_to_add(0, 1))
    # Test 2 should return 6.
    print(fuel_to_add(5, 40))
    # Test 3 should return 0.
    print(fuel_to_add(10, 30))
    # Test 4 should return 4520.
    print(fuel_to_add(896, 20500))
    # Test 5 should return 12209.
    print(fuel_to_add(1000, 50000))