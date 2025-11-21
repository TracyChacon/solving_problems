# Longest Word

# Given a sentence string, return the longest word in the sentence.

#     Words are separated by a single space.
#     Only letters (a-z, case-insensitive) count toward the word's length.
#     If there are multiple words with the same length, return the first one that appears.
#     Return the word as it appears in the given string, with punctuation removed.

import re

def longest_word(sentence: str) -> str:
    # Strip Punctuation & Split: Use a list comprehension to iterate through 
    # words (from sentence.split()) and immediately strip non-letter chars 
    # with re.sub(r"[^a-zA-Z]", "", word). This prepares the data for comparison. (O(N))
    stripped_words = [re.sub(r"[^a-zA-Z]", "", word) for word in sentence.split()]
    # Find the Max: Use Python's built-in max() function with key=len. 
    # This elegantly compares the length of every stripped word (satisfying the 
    # "letters only" rule) and, crucially, returns the first word in the list 
    # that ties for the maximum length. (O(N))
    return max(stripped_words, key=len) 

if __name__ == '__main__':
    # Tests

    # Test 1 should return "quick".
    print(longest_word("The quick red fox"))
    # Test 2 should return "challenge".
    print(longest_word("Hello coding challenge."))
    # Test 3 should return "This".
    print(longest_word("Do Try This At Home."))
    # Test 4 should return "exlamation".
    print(longest_word("This sentence... has commas, ellipses, and an exlamation point!"))
    # Test 5 should return "tie".
    print(longest_word("A tie? No way!"))
    # Test 6 should return "Wouldnt".
    print(longest_word("Wouldn't you like to know."))