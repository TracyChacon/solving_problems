# Snowflake Generator

# Given a multi-line string that uses newline characters (\n) to represent a line break, return a new string where each line is mirrored horizontally and attached to the end of the original line.

#     Mirror a line by reversing all of its characters, including spaces.

# For example, given "* \n *\n* ", which logs to the console as:

# * 
#  *
# * 

# Return "*  *\n ** \n*  *", which logs to the console as:

# *  *
#  ** 
# *  *

# Take careful note of the whitespaces in the given and returned strings. Be sure not to trim any of them.

def generate_snowflake(crystals: str) -> str:
    # Split the string by `\n` into a list of lines
    lines = crystals.split('\n')
    mirrored_lines = []

    for line in lines:
        # Mirror each string element in lines list
        mirrored_line = line + line[::-1]
        mirrored_lines.append(mirrored_line)
    
    # `return` a `join` of the `mirrored_lines` list by '\n'
    return "\n".join(mirrored_lines)

if __name__ == '__main__':
    # Tests

    # Test 1 should return "*  *\n ** \n*  *".
    print(generate_snowflake("* \n *\n* "))
    # Test 2 should return "X=~~=X".
    print(generate_snowflake("X=~"))
    # Test 3 should return " X    X \n  v  v  \nX--==--X\n  ^  ^  \n X    X ".
    print(generate_snowflake(" X  \n  v \nX--=\n  ^ \n X  "))
    # Test 4 should return "*   **   *\n * *  * * \n* * ** * *\n * *  * * \n*   **   *".
    print(generate_snowflake("*   *\n * * \n* * *\n * * \n*   *"))
    # Test 5 should return "*  --  *\n * -- * \n*  --  *".
    print(generate_snowflake("*  -\n * -\n*  -"))