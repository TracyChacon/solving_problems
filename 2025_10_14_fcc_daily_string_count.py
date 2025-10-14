# String Count
# Given two strings, determine how many times the second string appears in the first.

# The pattern string can overlap in the first string. For example, "aaa" contains "aa" twice. The first two a's and the second two.


def compute_lps_array(pattern: str) -> list[int]:
    pattern_length = len(pattern)
    lps = [0] * pattern_length
    length = 0
    i = 1

    while i < pattern_length:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def count(text: str, pattern: str) -> int:
    print(f"text: {text}, pattern: {pattern}")
    text_length = len(text)
    pattern_length = len(pattern)

    if pattern_length == 0:
        return 0
    if text_length < pattern_length:
        return 0
    
    lps = compute_lps_array(pattern)

    text_itr = 0
    pattern_itr = 0
    count = 0

    while text_itr < text_length:
        if pattern[pattern_itr] == text[text_itr]:
            text_itr += 1
            pattern_itr += 1
        if pattern_itr == pattern_length:
            count += 1
            pattern_itr = lps[pattern_itr - 1]
        elif i < text_length and pattern[pattern_itr] != text[text_itr]:
            if pattern_itr != 0:
                pattern_itr = lps[pattern_itr - 1]
            else:
                i += 1
    return count




if __name__ == "__main__":
    print(kmp_search("abcdefg","def"))
    print(kmp_search("hello","world"))
    print(kmp_search("mississippi","iss"))
    print(kmp_search("she sells seashells by the seashore","sh"))
    print(kmp_search("101010101010101010101","101"))
    print(compute_lps_array("ababa"))
