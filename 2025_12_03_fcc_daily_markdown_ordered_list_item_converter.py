# Markdown Ordered List Item Converter

# Given a string representing an ordered list item in Markdown, return the equivalent HTML string.

# A valid ordered list item in Markdown must:

#     Start with zero or more spaces, followed by
#     A number (1 or greater) and a period (.), followed by
#     At least one space, and then
#     The list item text.

# If the string doesn't have the exact format above, return "Invalid format". Otherwise, wrap the list item text in li tags and return the string.

# For example, given "1. My item", return "<li>My item</li>"

# Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.

import re

def convert_list_item(markdown: str) -> str:
    pattern = r'^\s*[1-9]\d*\.\s+(.+)\s*$'
    match = re.fullmatch(pattern, markdown)

    if match:
        text = match.group(1)
        return f"<li>{text}<li/>"
    else:
        return 'Invalid format'

if __name__ == '__main__':
    # Tests
    # Test 1 should return "<li>My item</li>".
    print(convert_list_item("1. My item"))
    # Test 2 should return "<li>Another item</li>".
    print(convert_list_item(" 1.  Another item"))
    # Test 3 should return "Invalid format".
    print(convert_list_item("1 . invalid item"))
    # Test 4 should return "<li>list item text</li>".
    print(convert_list_item("2. list item text"))
    # Test 5 should return "Invalid format".
    print(convert_list_item(". invalid again"))
    # Test 6 should return "Invalid format".
    print(convert_list_item("A. last invalid"))