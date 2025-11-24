# Message Validator

# Given a message string and a validation string, determine if the message is valid.

#     A message is valid if each word in the message starts with the corresponding letter in the validation string, in order.
#     Letters are case-insensitive.
#     Words in the message are separated by single spaces.


def is_valid_message(message: str, validation: str) -> bool:
    # Clear and descriptive variable name
    message_split = message.split()
    # Check number of words in message is equal to the length of the validation string
    if len(message_split) != len(validation):
        return False
    # Iterate over each word in message_split list a
    for i in range(len(message_split)):
        # Return False to end function if there is a mismatch
        if message_split[i][0].lower() != validation[i].lower():
            return False
    # If no edge cases return False then function will return True
    return True

# Can use python's built-in function zip() combined with generator expression for 
# A more pythonic approach
def is_valid_message_pythonic(message: str, validation: str) -> bool:
    message_split = message.split()
    # Check number of words in message is equal to the length of the validation string
    if len(message_split) != len(validation):
        return False
    # all() checks if all comparisons inside the generator expression are True.
    return all(
        # zip() pairs each word with its corresponding validation character
        word[0].lower() == char.lower() for word, char in zip(message_split, validation)
    )

# Tests
if __name__ == '__main__':

    # Test 1 should return True.
    print(is_valid_message("hello world", "hw"))
    # Test 2 should return True.
    print(is_valid_message("ALL CAPITAL LETTERS", "acl"))
    # Test 3 should return False.
    print(is_valid_message("Coding challenge are boring.", "cca"))
    # Test 4 should return True.
    print(is_valid_message("The quick brown fox jumps over the lazy dog.", "TQBFJOTLD"))
    # Test 5 should return False.
    print(is_valid_message("The quick brown fox jumps over the lazy dog.", "TQBFJOTLDT"))