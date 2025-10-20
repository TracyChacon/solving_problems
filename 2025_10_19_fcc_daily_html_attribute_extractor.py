# HTML Attribute Extractor
# Given a string of a valid HTML element, return the attributes of the element using the following criteria:

# You will only be given one element.
# Attributes will be in the format: attribute="value".
# Return an array of strings with each attribute property and value, separated by a comma, in this format: ["attribute1, value1", "attribute2, value2"].
# Return attributes in the order they are given.
# If no attributes are found, return an empty array.

def extract_attributes(element: str) -> list[str]:
    print(element)
    start_of_attributes = element.find(' ', element.find('<'))
    
    print(start_of_attributes)
    return ["str"]

if __name__ in "__main__":
    # should return ["class, red"].
    print(extract_attributes('< span class="red"></>'))
    # # should return ["charset, UTF-8"].
    # print(extract_attributes('<meta charset="UTF-8" />'))
    # # should return []
    # print(extract_attributes("<p>Lorem ipsum dolor sit amet</p>"))
    # # should return ["name, email", "type, email", "required, true"]
    # print(extract_attributes('<input name="email" type="email" required="true" />'))
    # # should return ["id, submit", "class, btn btn-primary"]
    # print(extract_attributes('<button id="submit" class="btn btn-primary">Submit</button>'))