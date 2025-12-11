# Markdown Bold Parser

# Given a string that may include some bold text in Markdown, return the equivalent HTML string.

#     Bold text in Markdown is any text that starts and ends with two asterisks (**) or two underscores (__).
#     There cannot be any spaces between the text and the asterisks or underscores, but there can be spaces in the text itself.
#     Convert all bold occurrences to HTML b tags and return the string.

# For example, given "**This is bold**", return "<b>This is bold</b>".

# Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.

######################################################################
# Initial Code
######################################################################

# import re

# def parse_bold(markdown: str) -> str:
#     pattern_asterisk = r'(([*]{2})([^\s](.+?)[^\s])([*]{2}))'
#     pattern_underline = r'(([_]{2})([^\s](.+?)[^\s])([_]{2}))'

#     html = re.sub(pattern_asterisk, r'<b>\3</b>', markdown)
#     html = re.sub(pattern_underline, r'<b>\3</b>', html)

#     return html

######################################################################
# optimized Code
######################################################################
import re

def parse_bold(markdown: str) -> str:
    # Capturing two asterisks or two underscores: (\*{2}|_{2})
    # Negative Lookahead (no space after delimiter): (?!\s)
    # Non-greedy content capture: (.+?)
    # Negative Lookbehind (no space before delimiter): (?<!\s)
    # Back-reference to the starting delimiter: \1
    pattern = r'(\*{2}|_{2})(?!\s)(.+?)(?<!\s)\1'
    
    # Replace the whole match with <b> and the content (\2)
    return re.sub(pattern, r'<b>\2</b>', markdown)
# Tests
if __name__ == '__main__':
    # Test 1 should return "<b>This is bold</b>".
    print(parse_bold("**This is bold**"))
    # Test 2 should return "<b>This is also bold</b>".
    print(parse_bold("__This is also bold__"))
    # Test 3 should return "**This is not bold **".
    print(parse_bold("**This is not bold **"))
    # Test 4 should return "__ This is also not bold__".
    print(parse_bold("__ This is also not bold__"))
    # Test 5 should return "The <b>quick</b> brown fox <b>jumps</b> over the <b>lazy</b> dog.".
    print(parse_bold("The **quick** brown fox __jumps__ over the **lazy** dog."))