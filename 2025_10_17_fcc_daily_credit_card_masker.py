# Credit Card Masker
# Given a string of credit card numbers, return a masked version of it using the following constraints:

# The string will contain four sets of four digits (0-9), with all sets being separated by a single space, or a single hyphen (-).
# Replace all numbers, except the last four, with an asterisk (*).
# Leave the remaining characters unchanged.
# For example, given "4012-8888-8888-1881" return "****-****-****-1881".
import re

CARD_PATTERN = re.compile(r'(\d{4}[\-\s]){3}\d{4}')

def mask(card: str) -> str | None:
    if not CARD_PATTERN.fullmatch(card):
        return None
    
    delimeter = card[4]
    last_four = card[15: 19]
    masked = f"****{delimeter}****{delimeter}****{delimeter}"

    return masked + last_four


    

if __name__ == "__main__":
    print(mask("4012-8888-8888-1881"))
    print(mask("5105 1051 0510 5100"))
    print(mask("6011 1111 1111 1117"))
    print(mask("2223-0000-4845-0010"))