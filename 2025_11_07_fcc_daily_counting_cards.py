# Counting Cards

# A standard deck of playing cards has 13 unique cards in each suit.
#  Given an integer representing the number of cards to pick from the 
# deck, return the number of unique combinations of cards you can pick.

#     Order does not matter. Picking card A then card B is the same as 
#       picking card B then card A.

# For example, given 52, return 1. There's only one combination of 52 
# cards to pick from a 52 card deck. And given 2, return 1326, There's
#  1326 card combinations you can end up with when picking 2 cards from
#  the deck.


######################################################
#  Intuition for the problem
# - Standard deck of cards has 52 cards. There are 52 
#   cards to choose from. If a card is selected, one
#   card is selected and now there are 51 cards to 
#   choose from. There are now 51 cards to choose from,
#   if a second card is selected 50 cards are left and
#   and two cards have been selected.

######################################################

# print(f"5: {52/5 * 51/4 * 50/3 * 49/2 * 48/1}")
# print(f"2: {52/2 * 51/1}")


######################################################
# Naive implementation
# - Does not account for symmetry principle/optimization
# - Uses floating point arithmetic in loop. This can 
#   cause precision errors in programs for suffienctly 
#   large iterations
######################################################

# def combinations(cards: int) -> int:
#     if cards == 52:
#         return 1

#     cards_left_in_deck = 52
#     accumulator = 1

#     for cards_left_to_choose_from in range(cards, 0, -1):
#         accumulator *= cards_left_in_deck / cards_left_to_choose_from
#         cards_left_in_deck -= 1

#     return int(accumulator)




####################################################
# Symmetry Optimization
#  - Takes advantage of symmetry principle
#  - Does not use floating point arithmetic in loop. This can 
#    cause precision errors in programs for suffienctly 
#    large iterations
####################################################
import math


def combinations(cards: int) -> int:
    # A standard deck has 52 cards.
    DECK_SIZE = 52
  
    n = DECK_SIZE
    
    # 1. Symmetry Optimization: Calculate C(n, min(k, n-k))
    # This ensures the loop runs the fewest number of times.
    cards_optimized = min(cards, n - cards)
    
    # If k is 0 or 52, the combination is 1.
    if cards_optimized < 0:
        return 0
    if cards_optimized == 0:
        return 1

    numerator = 1
    denominator = 1
    
    # Iterate cards_optimized times, using pure integer multiplication.
    for i in range(cards_optimized):
        # Numerator: n * (n-1) * ...
        numerator *= (n - i)
        # Denominator: k * (k-1) * ...
        denominator *= (i + 1)
        
    # Since combinations always result in an integer, integer division (//) is safe.
    return numerator // denominator



###############################################
# pythonic

# - Uses built-in function
###############################################
# import math

# def combinations(cards: int) -> int:
#     DECK_SIZE = 52
#     if cards < 0 or cards > DECK_SIZE:
#         return 0
    
#     return math.comb(DECK_SIZE, cards)


# Tests
if __name__ == "__main__":
    # Test 1 should return 1.
    print(combinations(52))
    # Test 2 should return 52.
    print(combinations(1))
    # Test 3 should return 1326.
    print(combinations(2))
    # Test 4 should return 2598960.
    print(combinations(5))
    # Test 5 should return 15820024220.
    print(combinations(10))
    # Test 6 should return 1326.
    print(combinations(50))