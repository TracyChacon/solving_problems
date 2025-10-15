# HTML Tag Stripper
# Given a string of HTML code, remove the tags and return the plain text content.

# The input string will contain only valid HTML.
# HTML tags may be nested.
# Remove the tags and any attributes.
# For example, '<a href="#">Click here</a>' should return "Click here".

def strip_tags(html: str) -> str:
    return html

if __name__ == "__main__":
    print(strip_tags(""))