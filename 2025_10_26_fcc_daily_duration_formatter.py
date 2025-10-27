# Duration Formatter
# Given an integer number of seconds, return a string representing the same duration in the format "H:MM:SS", where "H" is the number of hours, "MM" is the number of minutes, and "SS" is the number of seconds. Return the time using the following rules:

# Seconds: Should always be two digits.
# Minutes: Should omit leading zeros when they aren't needed. Use "0" if the duration is less than one minute.
# Hours: Should be included only if they're greater than zero.

# def format(seconds: int) -> str:
#     SEC_PER_MIN = 60
#     MIN_PER_HR = 60

#     decimal_hrs = seconds / SEC_PER_MIN / MIN_PER_HR
#     truncated_hrs = int(decimal_hrs)

#     decimal_min = (decimal_hrs - truncated_hrs) * MIN_PER_HR
#     truncated_min = int(decimal_min)
    
#     rounded_sec = round((decimal_min - truncated_min) * SEC_PER_MIN)

#     if truncated_hrs < 1:
#         return f"{truncated_min}:{rounded_sec:02d}"

#     return f"{truncated_hrs}:{truncated_min:02d}:{rounded_sec:02d}"

def format(seconds: int) -> str:
    SEC_PER_MIN = 60
    SEC_PER_HR = 3600

    hrs = seconds // SEC_PER_HR
    sec = seconds % SEC_PER_HR % SEC_PER_MIN
    min = seconds % SEC_PER_HR // SEC_PER_MIN
    
    if hrs != 0:
        return f"{min}:{sec:02d}"

    return f"{hrs}:{min:02d}:{sec:02d}"

# Test 1 should return "8:20".
print(format(500))
# Test 2 should return "1:06:40".
print(format(4000))
# Test 3 should return "0:01".
print(format(1))
# Test 4 should return "1:32:35".
print(format(5555))
# Test 5 should return "27:46:39".
print(format(99999))
