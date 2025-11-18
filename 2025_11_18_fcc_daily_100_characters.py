# 100 Characters

# Welcome to the 100th Daily Coding Challenge!

# Given a string, repeat its characters until the result is exactly 100 characters long. If your repetitions go over 100 characters, trim the extra so it's exactly 100.

def one_hundred(chars: str) -> str:
    # Test for empty string to avoid division by zero error later
    if not chars:
        return ""
    # 1. Calculate the number of full repetitions needed
    # 2. Calculate the remainder (slice length)
    # 3. Concatenate the repeated string and the required slice
    # print(100 // len(chars) * len(chars) + 100 % len(chars))
    # print(100 // len(chars) * len(chars))
    # print(100 % len(chars))
    return (chars * (100 // len(chars)) + chars[:100 % len(chars)])
 

# Tests
if __name__ == '__main__':
    # test 1 should return "One hundred One hundred One hundred One hundred One hundred One hundred One hundred One hundred One ".
    print(one_hundred("One hundred "))
    # test 2 should return "freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeC".
    print(one_hundred("freeCodeCamp "))
    # test 3 should return "daily challenges daily challenges daily challenges daily challenges daily challenges daily challenge".
    print(one_hundred("daily challenges "))
    # test 4 should return "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!".
    print(one_hundred("!"))