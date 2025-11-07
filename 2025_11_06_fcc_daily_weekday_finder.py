# Weekday Finder

# Given a string date in the format YYYY-MM-DD, return the day of the week.

# Valid return days are:

#     "Sunday"
#     "Monday"
#     "Tuesday"
#     "Wednesday"
#     "Thursday"
#     "Friday"
#     "Saturday"

# Be sure to ignore time zones.

from datetime import datetime

def get_weekday(date_string: str) -> str:
    date = datetime.strptime(date_string, '%Y-%m-%d')
    weekday_full_name = date.strftime('%A')

    return weekday_full_name

# Tests

if __name__ == "__main__":
    # Test 1 should return Thursday.
    print(get_weekday("2025-11-06"))
    # Test 2 should return Friday.
    print(get_weekday("1999-12-31"))
    # Test 3 should return Saturday.
    print(get_weekday("1111-11-11"))
    # Test 4 should return Wednesday.
    print(get_weekday("2112-12-21"))
    # Test 5 should return Monday.
    print(get_weekday("2345-10-01"))