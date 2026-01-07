# vOwElcAsE

# Given a string, return a new string where all vowels are converted to uppercase and all other alphabetical characters are converted to lowercase.

#     Vowels are "a", "e", "i", "o", and "u" in any case.
#     Non-alphabetical characters should remain unchanged.

def vowel_case(s: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u']
    chars = list(s.lower())
    vowel_upper = []

    for char in chars:
        if char not in vowels:
            vowel_upper.append(char)
        else:
            vowel_upper.append(char.upper()) 
    
    return "".join(vowel_upper)

# def vowel_case_1(s: str) -> str:
#     vowels = {'a', 'e', 'i', 'o', 'u'}

#     return "".join(char.upper() if char in vowels else char for char in s.lower())

if __name__ == '__main__':
    # Tests

    # Test 1 should return "vOwElcAsE".
    print(vowel_case("vowelcase"))
    # Test 2 should return "cOdIng Is fUn".
    print(vowel_case("coding is fun"))
    # Test 3 should return "hEllO, wOrld!".
    print(vowel_case("HELLO, world!"))
    # Test 4 should return "gIt chErry-pIck".
    print(vowel_case("git cherry-pick"))
    # Test 5 should return "hEAd~1".
    print(vowel_case("HEAD~1"))