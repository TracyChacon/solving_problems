# Markdown Heading Converter

# Given a string representing a Markdown heading, return the equivalent HTML heading.

# A valid Markdown heading must:

#     Start with zero or more spaces, followed by
#     1 to 6 hash characters (#) in a row, then
#     At least one space. And finally,
#     The heading text.

# The number of hash symbols determines the heading level. For example, one hash symbol corresponds to an h1 tag, and six hash symbols correspond to an h6 tag.

# If the given string doesn't have the exact format above, return "Invalid format".

# For example, given "# My level 1 heading", return "<h1>My level 1 heading</h1>".

# Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.

import re

# def convert(heading: str) -> str:
#     heading_pattern = r'[#]+[\s]{1}'
#     match_heading = re.search(heading_pattern, heading)
#     heading_level = 0
#     output_str = 'Invalid format'
    
#     if match_heading:
#         start, end = match_heading.span()
#         heading_level = end - start - 1
#         print(f"heading:'{heading[start: end]}', {end} - {start} = {end - start}")

#         if heading_level <= 6:
#             output_str = f"<h{heading_level}>{heading[end: ]}</h{heading_level}>"
        
#     return output_str

def convert(heading: str) -> str:
    # Start <= ^ of string and zero or one or more <= * space characters <=[\s] 
    # ^[\s]*
    # Group 1 in parenthesis <= ()  1 to 6 {1,6} hashes #
    # ([#]{1,6})
    # One or more <= +  space characters <= [\s]
    # [\s]+
    # Group 2 in parenthesis <= ()  zero or one or more <= * of any characters <= .
    # (.*)
    pattern = r'^[\s]*([#]{1,6})[\s]+(.*)$'
    match = re.search(pattern, heading)
    heading_level = 0
    output_str = 'Invalid format'
    # Condition for if the pattern matched the heading
    if match:
        # Length of hashes  from group 1 represents the heading level
        hashes = match.group(1)
        heading_level = len(hashes)
        # Get text and strip left and right whitespace
        text = match.group(2).strip()
        # if heading text existsi and isn't an empty string
        if text:
            output_str = f"<h{heading_level}>{text}</h{heading_level}>"
        
    return output_str

if __name__ == '__main__':

    # Tests

    # Test 1 should return "<h1>My level 1 heading</h1>".
    print(convert("# My level 1 heading"))
    # Test 2 should return "Invalid format".
    # print(convert("My heading"))
    # Test 3 should return "<h5>My level 5 heading</h5>".
    print(convert("##### My level 5 heading"))
    # Test 4 should return "Invalid format".
    # print(convert("#My heading"))
    # Test 5 should return "<h3>My level 3 heading</h3>".
    print(convert("  ###  My level 3 heading"))
    # Test 6 should return "Invalid format".
    print(convert("####### My level 7 heading"))
    # Test 7 should return "<h2>My #2 heading</h2>".
    # print(convert("## My #2 heading"))