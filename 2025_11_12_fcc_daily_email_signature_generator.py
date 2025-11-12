# Email Signature Generator

# Given strings for a person's name, title, and company, return an email signature as a single string using the following rules:

#     The name should appear first, preceded by a prefix that depends on the first letter of the name. For names starting with (case-insensitive):
#         A-I: Use >> as the prefix.
#         J-R: Use -- as the prefix.
#         S-Z: Use :: as the prefix.
#     A comma and space (, ) should follow the name.
#     The title and company should follow the comma and space, separated by " at " (with spaces around it).

# For example, given "Quinn Waverly", "Founder and CEO", and "TechCo" return "--Quinn Waverly, Founder and CEO at TechCo".

def generate_signature(name: str, title: str, company: str) -> str:
    first_letter_capitalize_ordinal = ord(name[0].upper())
    signature_prefix = ''

    # print(f"ord('A'): {ord('A')}")
    # print(f"ord('I'): {ord('I')}\n")
    # print(f"ord('J'): {ord('J')}")
    # print(f"ord('R'): {ord('R')}\n")
    # print(f"ord('S'): {ord('S')}")
    # print(f"ord('Z'): {ord('Z')}\n")

    print(f"first_letter_capitalize_ordinal: {first_letter_capitalize_ordinal}")

    match first_letter_capitalize_ordinal:
        case char_code if 65 <= char_code <= 73:
            signature_prefix = '>>'
        case char_code if 74 <= char_code <= 82:
            signature_prefix = '--'
        case char_code if 83 <= char_code <= 90:
            signature_prefix = '::'
        case _:
            print(f"char_code: {char_code}")
            signature_prefix = ':p'
    
    return f"{signature_prefix}{name}, {title} at {company}"
# Tests

# Test 1 should return "--Quinn Waverly, Founder and CEO at TechCo".
print(generate_signature("Quinn Waverly", "Founder and CEO", "TechCo"))
# Test 2 should return ">>Alice Reed, Engineer at TechCo".
print(generate_signature("Alice Reed", "Engineer", "TechCo"))
# Test 3 should return "::Tina Vaughn, Developer at example.com".
print(generate_signature("Tina Vaughn", "Developer", "example.com"))
# Test 4 should return ">>B. B., Product Tester at AcmeCorp".
print(generate_signature("B. B.", "Product Tester", "AcmeCorp"))
# Test 5 should return "::windstorm, Cloud Architect at Atmospheronics".
print(generate_signature("windstorm", "Cloud Architect", "Atmospheronics"))
