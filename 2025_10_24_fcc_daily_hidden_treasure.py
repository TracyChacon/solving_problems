# Hidden Treasure
# Given a 2D array representing a map of the ocean floor that includes a hidden treasure, and an array with the coordinates ([row, column]) for the next dive of your treasure search, return "Empty", "Found", or "Recovered" using the following rules:

# The given 2D array will contain exactly one unrecovered treasure, which will occupy multiple cells.

# Each cell in the 2D array will contain one of the following values:

# "-": No treasure.
# "O": A part of the treasure that has not been found.
# "X": A part of the treasure that has already been found.

# If the dive location has no treasure, return "Empty".

# If the dive location finds treasure, but at least one other part of the treasure remains unfound, return "Found".

# If the dive location finds the last unfound part of the treasure, return "Recovered".

# For example, given:

# [
#   [ "-", "X"],
#   [ "-", "X"],
#   [ "-", "O"]
# ]
# And [2, 1] for the coordinates of the dive location, return "Recovered" because the dive found the last unfound part of the treasure.


#  Misses edge case in Test 7 below but still passed the challenge
# def dive(map: list[list], coordinates: list) -> str:
#     last_dive_area = len(map) - 1
#     coord1, coord2 = coordinates
    
#     if map[coord1][coord2] == "O" and coord1 == last_dive_area:
#         return "Recovered"
#     elif map[coord1][coord2] == "-":
#         return "Empty" 
#     else:
#         return "Found"


def dive(map: list[list], coordinates: list) -> str:
    row, column = coordinates
    dive_result = map[row][column]

    if dive_result == "-":
        return "Empty"
    elif dive_result == "X":
        return "Found"
    else:
        map[row][column] = "X"
        remaining_unfound_parts = 0
        
        for map_row in map:
            remaining_unfound_parts += map_row.count("O")
            
            if remaining_unfound_parts > 0:
                return "Found" 
    
        return 'Recovered'
    


    
if __name__ == "__main__":
    # Test 1: should return "Recovered".
    map1 = [[ "-", "X"], [ "-", "X"], [ "-", "O"]]
    print(dive(map1, [2, 1]) )
    # Test 2: should return "Empty".
    map2 = [[ "-", "X"], [ "-", "X"], [ "-", "O"]]
    print(dive(map2, [2, 0]) )
    # Test 3: should return "Found".
    map3 = [[ "-", "X"], [ "-", "O"], [ "-", "O"]]
    print(dive(map3, [1, 1]) )
    # Test 4: should return "Found".
    map4 = [[ "-", "-", "-"], [ "X", "O", "X"], [ "-", "-", "-"]]
    print(dive(map4, [1, 2]) )
    # Test 5: should return "Recovered".
    map5 = [[ "-", "-", "-"], [ "-", "-", "-"], [ "O", "X", "X"]]
    print(dive(map5, [2, 0]) )
    # Test 6: should return "Empty".
    map6 = [[ "-", "-", "-"], [ "-", "-", "-"], [ "O", "X", "X"]]
    print(dive(map6, [1, 2]) )
    # Test 7: should return "Recovered" (Last O found)
    map7 = [[ "-", "-", "-"], [ "X", "O", "X"], [ "-", "-", "-"]]
    print(dive(map7, [1, 1])) 




