# Vowel Balance
# Given a string, determine whether the number of vowels in the first half of the string is equal to the number of vowels in the second half.

# The string can contain any characters.
# The letters a, e, i, o, and u, in either uppercase or lowercase, are considered vowels.
# If there's an odd number of characters in the string, ignore the center character.

def is_balanced(s: str) -> bool:
    print(s)
    print(len(s) // 2)
    vowels = 'aeiou'
    left_vowel_count = 0
    right_vowel_count = 0



    # print (f"{len(s) % 2 == 0} == {s[len(s) // 2]}")
    if len(s) % 2 == 0 and s[len(s) // 2].lower() in vowels:
        right_vowel_count += 1

    for index in range(len(s)):
        # print(f"{index}: {s[index]}")

        if s[index].lower() in vowels:
            if index < len(s) // 2:
                left_vowel_count += 1
            elif index > len(s) // 2:  
                right_vowel_count += 1
    
    # print (f"{left_vowel_count} == {right_vowel_count}")
    return left_vowel_count == right_vowel_count


print(is_balanced('racecar'))
# print(is_balanced('Lorem Ipsum'))
# print(is_balanced('Kitty Ipsum'))
print(is_balanced('string'))