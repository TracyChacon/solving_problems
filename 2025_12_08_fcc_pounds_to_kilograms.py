# Pounds to Kilograms

# Given a weight in pounds as a number, return the string "(lbs) pounds equals (kgs) kilograms.".

#     Replace "(lbs)" with the input number.
#     Replace "(kgs)" with the input converted to kilograms, rounded to two decimals and always include two decimal places in the value.
#     1 pound equals 0.453592 kilograms.
#     If the input is 1, use "pound" instead of "pounds".
#     If the converted value is 1, use "kilogram" instead of "kilograms".

from decimal import Decimal

def convert_to_kgs(lbs: int|float) -> str:
    LBS_TO_KG_FACTOR = Decimal('0.453592')
    kgs = Decimal(lbs) * LBS_TO_KG_FACTOR

    lbs_unit_plural = 'pound' if lbs == 1 else 'pounds'
    kgs_unit_plural = 'kilogram' if f"{kgs:.2f}" == '1.00' else 'kilograms'
    
    return f"{lbs} {lbs_unit_plural} equals {kgs:.2f} {kgs_unit_plural}."

if __name__ == '__main__':
    # Tests

    # Test 1 should return "1 pound equals 0.45 kilograms.".
    print(convert_to_kgs(1))
    # Test 2 should return "0 pounds equals 0.00 kilograms.".
    print(convert_to_kgs(0))
    # Test 3 should return "100 pounds equals 45.36 kilograms.".
    print(convert_to_kgs(100))
    # Test 4 should return "2.5 pounds equals 1.13 kilograms.".
    print(convert_to_kgs(2.5))
    # Test 5 should return "2.20462 pounds equals 1.00 kilogram.".
    print(convert_to_kgs(2.20462))