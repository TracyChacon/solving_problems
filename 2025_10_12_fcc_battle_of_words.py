# Battle of Words
# Given two sentences representing your team and an opposing team, where each word from your team battles the corresponding word from the opposing team, determine which team wins using the following rules:

# The given sentences will always contain the same number of words.
# Words are separated by a single space and will only contain letters.
# The value of each word is the sum of its letters.
# Letters a to z correspond to the values 1 through 26. For example, a is 1, and z is 26.
# A capital letter doubles the value of the letter. For example, A is 2, and Z is 52.
# Words battle in order: the first word of your team battles the first word of the opposing team, and so on.
# A word wins if its value is greater than the opposing word's value.
# The team with more winning words is the winner.
# Return "We win" if your team is the winner, "We lose" if your team loses, and "Draw" if both teams have the same number of wins.

def points_for_letter(char: str) -> int:
    ord_value = ord(char)

    if ord('a') <= ord_value <= ord('z'):
        return ord_value - ord('a') + 1
    elif ord('A') <= ord_value <= ord('Z'):
        return (ord_value - ord('A') + 1) * 2
    else:
        return 0
    

def battle(our_team: str, opponent: str) -> str : 
    our_team_words = our_team.split()
    opponent_words = opponent.split()
    rounds = len(our_team_words)
    our_team_wins = 0
    opponent_wins = 0

    for round in range(rounds):
        our_team_points_current_round = 0
        opponent_points_current_round = 0

        for char in our_team_words[round]:
            our_team_points_current_round += points_for_letter(char)
        for char in opponent_words[round]:
            opponent_points_current_round += points_for_letter(char)
        
        if our_team_points_current_round > opponent_points_current_round:
            our_team_wins += 1
        elif opponent_points_current_round > our_team_points_current_round:
            opponent_wins += 1

    if our_team_wins > opponent_wins:
        return "We win"
    elif opponent_wins > our_team_wins:
        return "We lose"
    else:
        return "Draw"

            



if __name__ == "__main__":
    print(battle("hello world", "hello word"))