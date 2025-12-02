# Camel to Snake

# Given a string in camel case, return the snake case version of the string using the following rules:

#     The input string will contain only letters (A-Z and a-z) and will always start with a lowercase letter.
#     Every uppercase letter in the camel case string starts a new word.
#     Convert all letters to lowercase.
#     Separate words with an underscore (_).


# Iterates through the string and ahandles uppercase letters by prepending an
# underscore and converting the letter to lowercase.
def to_snake(camel: str) -> str:
    snake = []

    for i in range(len(camel)):
        if not camel[i].isupper():
            snake.append(camel[i])
        else:
            snake.append(f"_{camel[i].lower()}")

    return "".join(snake) 

# If a character 'c' is uppercase, prepend an underscore and convert to lower.
# Otherwise, just keep the character.
# The 'if camel[0].isupper()' is a theoretical guard, but the prompt says 
# the input always starts with a lowercase letter, so it's not strictly needed
# for the specific prompt, but good practice for robustness.
def to_snake_i1(camel: str) -> str:
   snake_chars = [
       f"_{char.lower()}" if char.isupper() else char for char in camel
   ] 

   return "".join(snake_chars)

# Find all uppercase letters (A-Z) and replace them 
# with an underscore followed by the lowercase version of that letter.
# The first argument is the pattern: '([A-Z])' captures the uppercase letter.
# The second argument is the replacement string: r'_\1' uses the captured group.
# The final .lower() ensures everything is lowercased, though the replacement
# function already handles the character being replaced.
import re

def to_snake_i2(camel: str) -> str:
    return re.sub(r'([A-Z])', r'_\1', camel).lower()


if __name__ == '__main__':
    # Tests

    # Test 1 should return "hello_world".
    print(to_snake("helloWorld"))
    # Test 2 should return "my_variable_name".
    print(to_snake("myVariableName"))
    # Test 3 should return "freecodecamp_daily_challenges".
    print(to_snake("freecodecampDailyChallenges"))