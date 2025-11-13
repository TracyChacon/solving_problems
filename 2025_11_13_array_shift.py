# Array Shift

# Given an array and an integer representing how many positions to shift the array, return the shifted array.

#     A positive integer shifts the array to the left.
#     A negative integer shifts the array to the right.
#     The shift wraps around the array.

# For example, given [1, 2, 3] and 1, shift the array 1 to the left, returning [2, 3, 1].
# Tests
"""

        8 / 10 = 0 R 8
        8 % 10 = 8
        1 / 3 = 0 R 1
        1 % 3 = 1
        ZERO BASED
        shift 1
          [ 1 2 3 ]
            0 1 2
          [ 2 3 1]
            0 1 2
            1 2 0
   
        shift 2
          [ 1 2 3 ]
            0 1 2
          [ 3 1 2 ]
            0 1 2
            2 0 1

        shift 3
          [ 1 2 3 ]
            0 1 2
          [ 1 2 3 ]
            0 1 2

        ONE BASED    
        shift 1
          [ 1 2 3 ]
            1 2 3
          [ 2 3 1]
            1 2 3
            2 3 1
   
        shift 2
          [ 1 2 3 ]
            1 2 3
          [ 3 1 2 ]
            1 2 3
            3 1 2

        shift 3
          [ 1 2 3 ]
            1 2 3
          [ 1 2 3 ]
            1 2 3
            
"""

def shift_array(arr: list, n: int) -> list[int]:
    shifted_list = arr[:]      

    for i in range(len(arr)):
        # print(f"{i} {(i + 1 * n) % len(arr)}")
        shift = (i + 1 * n * -1) % len(arr)
        shifted_list[shift] = arr[i]
    return shifted_list

# # Test 1 should return [2, 3, 1].
print(shift_array([1, 2, 3], 1))
# Test 2 should return [3, 1, 2].
# print(shift_array([1, 2, 3], -1))
# # Test 3 should return ["charlie", "alpha", "bravo"].
# print(shift_array(["alpha", "bravo", "charlie"], 5))
# # Test 4 should return ["bravo", "charlie", "alpha"].
# print(shift_array(["alpha", "bravo", "charlie"], -11))
# # Test 5 should return [5, 6, 7, 8, 9, 0, 1, 2, 3, 4].
# print(shift_array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 15))