# For day six of Space Week, you will be given a date in the format "YYYY-MM-DD" and need to determine the phase of the moon for that day using the following rules:

# Use a simplified lunar cycle of 28 days, divided into four equal phases:

# "New": days 1 - 7
# "Waxing": days 8 - 14
# "Full": days 15 - 21
# "Waning": days 22 - 28
# After day 28, the cycle repeats with day 1, a new moon.

# Use "2000-01-06" as a reference new moon (day 1 of the cycle) to determine the phase of the given day.
# You will not be given any dates before the reference date.
# Return the correct phase as a string.
from datetime import datetime

def moon_phase(date_string: str) -> str:
    PERIOD = 28
    OFFSET = 1
    reference_new_moon_date = datetime.strptime("2000-01-06", "%Y-%m-%d")
    given_date = datetime.strptime(date_string, "%Y-%m-%d")

    day_of_lunar_cycle = (given_date - reference_new_moon_date).days % PERIOD + OFFSET
    
    match day_of_lunar_cycle:
        case day if 1 <= day <= 7:
            return "New"
        case day if 8 <= day <= 14:
            return "Waxing"
        case day if 15 <= day <= 21:
            return "Full"
        case day if 22 <= day <= 28:
            return "Waning"
        case _:
            return "Error: Something went wrong."

    
    

if __name__ == "__main__":
    print(moon_phase("2000-01-12"))