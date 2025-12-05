# Symmetric Difference

# Given two arrays, return a new array containing the symmetric difference of them.

#     The symmetric difference between two sets is the set of values that appear in either set, but not both.
#     Return the values in the order they first appear in the input arrays.


# Let A and B be sets. 
# The symmetric difference of A and B
# (denoted by A ^ B ) 
# is the set of all elements that are in A and B 
# but not in both. 
# That is, A ^ B = (A | B) - (A & B)
#
# Where the Union of A and B is denoted by A | B
# and the Intersection of A and B is denoted by A & B
#
# For an understanding of unions, intersections, and symmetric difference see: https://math.libretexts.org/Bookshelves/Combinatorics_and_Discrete_Mathematics/Applied_Discrete_Structures_(Doerr_and_Levasseur)/01%3A_Set_Theory/1.02%3A_Basic_Set_Operations

# def difference(list_1: list, list_2: list) -> list:
#     set_1 = set(list_1)
#     set_2 = set(list_2)

#     return list(set_1 ^ set_2)

def difference(list_1: list, list_2: list) -> list:
    set_1 = set(list_1)
    set_2 = set(list_2)
    
    # 1. Calculate the symmetric difference (efficiently!)
    # set_1 ^ set_2 is the symmetric difference operator.
    symmetric_difference_set = set_1 ^ set_2
    
    # Critical Caveat: Sets are UNORDERED (or insertion-ordered, but 
    # the order isn't guaranteed to match the original lists). 
    # We must iterate over the original lists to preserve the required order.
    
    symmetric_difference_ordered_list = []

    # 2. Iterate through list_1 to collect the first elements
    for element in list_1:
        if element in symmetric_difference_set:
            symmetric_difference_ordered_list.append(element)
            # Remove to avoid duplicates in step 3
            symmetric_difference_set.remove(element) 
    
    # 3. Iterate through list_2 to collect the remaining elements
    for element in list_2:
        if element in symmetric_difference_set:
            symmetric_difference_ordered_list.append(element)
            
    return symmetric_difference_ordered_list
if __name__ == '__main__':
    # Tests

    # Test 1 should return [1, 2, 4, 5].
    print(difference([1, 2, 3], [3, 4, 5]))
    # Test 2 should return ["a", "c"].
    print(difference(["a", "b"], ["c", "b"]))
    # Test 3 should return [1, "b"].
    print(difference([1, "a", 2], [2, "b", "a"]))
    # Test 4 should return [2, 4, 6, 8].
    print(difference([1, 3, 5, 7, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]))