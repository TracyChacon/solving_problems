# Most Frequent

# Given an array of elements, return the element that appears most frequently.

#     There will always be a single most frequent element.

# from typing import Any

# def most_frequent(list: list) -> Any:
#     frequency_counter = {}

#     for element in list:
#         if element not in frequency_counter:
#             frequency_counter[element] = 1
#         else:
#             frequency_counter[element] += 1

#     # print(f"frequency_counter: {frequency_counter}")
#     return max(frequency_counter, key=frequency_counter.get)

from typing import Any
from collections import Counter

def most_frequent(list: list) -> Any:
    frequency_counter = 

    for element in list:
        if element not in frequency_counter:
            frequency_counter[element] = 1
        else:
            frequency_counter[element] += 1

    # print(f"frequency_counter: {frequency_counter}")
    return max(frequency_counter, key=frequency_counter.get)

if __name__ == '__main__':
    # Tests

    # Test 1 should return "a".
    print(most_frequent(["a", "b", "a", "c"]))
    # Test 2 should return 2.
    print(most_frequent([2, 3, 5, 2, 6, 3, 2, 7, 2, 9]))
    # Test 3 should return False.
    print(most_frequent([True, False, "False", "True", False]))
    # Test 4 should return 40.
    print(most_frequent([40, 20, 70, 30, 10, 40, 10, 50, 40, 60]))