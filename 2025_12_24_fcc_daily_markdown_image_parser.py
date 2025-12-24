# Markdown Image Parser

# Given a string of an image in Markdown, return the equivalent HTML string.

# A Markdown image has the following format: "![alt text](image_url)". Where:

#     alt text is the description of the image (the alt attribute value).
#     image_url is the source URL of the image (the src attribute value).

# Return a string of the HTML img tag with the src set to the image URL and the alt set to the alt text.

# For example, given "![Cute cat](cat.png)" return '<img src="cat.png" alt="Cute cat">';

#     Make sure the tag, order of attributes, spacing, and quote usage is the same as above.

# Note: The console may not display HTML tags in strings when logging messages — check the browser console to see logs with tags included.

def parse_image(markdown: str) -> str:
    # Find the positions of the brackets for the alt text
    alt_start = markdown.find("![") + 2
    alt_end = markdown.find("]")

    # Find the positions of the parentheses for the image URL
    url_start = markdown.find("(", alt_end) + 1
    url_end = markdown.find(")", url_start)

    # Extract the substrings
    alt_text = markdown[alt_start:alt_end]
    image_url = markdown[url_start: url_end]

    # Return formated HTML string
    return f'<img src="{image_url}" alt="{alt_text}">'

if __name__ == '__main__':
    # Tests

    # Test 1 should return '<img src="cat.png" alt="Cute cat">'.
    print(parse_image("![Cute cat](cat.png)"))
    # Test 2 should return '<img src="https://freecodecamp.org/cdn/rocket-ship.jpg" alt="Rocket Ship">'.
    print(parse_image("![Rocket Ship](https://freecodecamp.org/cdn/rocket-ship.jpg)"))
    # Test 3 should return '<img src="https://freecodecamp.org/cats.jpeg" alt="Cute cats!">'.
    print(parse_image("![Cute cats!](https://freecodecamp.org/cats.jpeg)"))