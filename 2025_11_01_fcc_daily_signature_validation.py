# Signature Validation
# Given a message string, a secret key string, and a signature number, determine if the signature is valid using this encoding method:

# Letters in the message and secret key have these values:
# a to z have values 1 to 26 respectively.
# A to Z have values 27 to 52 respectively.
# All other characters have no value.
# Compute the signature by taking the sum of the message plus the sum of the secret key.
# For example, given the message "foo" and the secret key "bar", the signature would be 57:

# f (6) + o (15) + o (15) = 36
# b (2) + a (1) + r (18) = 21
# 36 + 21 = 57
# Check if the computed signature matches the provided signature.

def offset(number: int) -> int:
    LOWER_CASE_OFFSET = 96
    UPPER_CASE_OFFSET = 38
    if number >= ord('a'):
        return number - LOWER_CASE_OFFSET
    
    return number - UPPER_CASE_OFFSET
    

def verify(message: str, key: str, signature: int) -> bool:
    message_sum = sum(offset(ord(char)) for char in message if char.isalpha())
    key_sum = sum(offset(ord(char)) for char in key if char.isalpha())

    return signature == message_sum + key_sum

if __name__ == '__main__':
    # Test 1 should return True.
    print(verify("foo", "bar", 57))
    # Test 2 should return False.
    print(verify("foo", "bar", 54))
    # Test 3 should return True.
    print(verify("freeCodeCamp", "Rocks", 238))
    # Test 4 should return False.
    print(verify("Is this valid?", "No", 210))
    # Test 5 should return True.
    print(verify("Is this valid?", "Yes", 233))
    # Test 6 should return True.
    print(verify("Check out the freeCodeCamp podcast,", "in the mobile app", 514))