
# Capitalize It

# Given a string title, return a new string formatted in title case using the following rules:

#     Capitalize the first letter of each word.
#     Make all other letters in each word lowercase.
#     Words are always separated by a single space.

def title_case(title):
    return " ".join([word.lower().capitalize() for word in title.split()])

if __name__ == '__main__':
    # Tests

    # Test 1 should return "Hello World".
    print(title_case("hello world"))
    # Test 2 should return "The Quick Brown Fox".
    print(title_case("the quick brown fox"))
    # Test 3 should return "Javascript And Python".
    print(title_case("JAVASCRIPT AND PYTHON"))
    # Test 4 should return "Avocado Toast For Breakfast".
    print(title_case("AvOcAdO tOAst fOr brEAkfAst"))