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

def count(text: str, parameter: str) -> int:
    print(f"text: {text}, parameter: {parameter}")
    text_length = len(text)
    parameter_length = len(parameter)

    if parameter_length == 0:
        return 0
    if text_length < parameter_length:
        return 0
    
    lps = compute_lps_array(parameter)

    text_itr = 0
    parameter_itr = 0
    count = 0

    while text_itr < text_length:
        if parameter[parameter_itr] == text[text_itr]:
            text_itr += 1
            parameter_itr += 1
        if parameter_itr == parameter_length:
            count += 1
            parameter_itr = lps[parameter_itr - 1]
        elif text_itr < text_length and parameter[parameter_itr] != text[text_itr]:
            if parameter_itr != 0:
                parameter_itr = lps[parameter_itr - 1]
            else:
                text_itr += 1
    return count




if __name__ == "__main__":
    print(count("abcdefg","def"))
    # print(count("hello","world"))
    # print(count("mississippi","iss"))
    # print(count("she sells seashells by the seashore","sh"))
    # print(count("101010101010101010101","101"))
    # print(compute_lps_array("ababa"))
