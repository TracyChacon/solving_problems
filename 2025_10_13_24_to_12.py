# 24 to 12
# Given a string representing a time of the day in the 24-hour format of "HHMM", return the time in its equivalent 12-hour format of "H:MM AM" or "H:MM PM".

# The given input will always be a four-digit string in 24-hour time format, from "0000" to "2359".

def to_12(time: str) -> str:
    # Delimiters use the full HHMM integer value for clean range checks
    AM_END_DELIMITER = 1159 

    time_24_int = int(time)
    hour = time_24_int // 100 # Extract hours integer
    minute = time[2:]         # Keep minutes string

    # 1. Determine AM/PM
    if time_24_int <= AM_END_DELIMITER:
        meridiem = "AM"
        if hour == 0:
            # Handle Midnight (00xx -> 12)
            hour = 12
    else:
        meridiem = "PM"
        if hour > 12:
            # Handle 13xx onwards (13-12=1, 14-12=2, etc.)
            hour -= 12
        # Note: 12xx (Noon) already equals 12, so no change needed.

    # 2. Format the result
    return f"{hour}:{minute} {meridiem}"


if __name__ == "__main__":
    print(to_12("1124"))
    print(to_12("0900"))
    print(to_12("1455"))
    print(to_12("1146"))
    print(to_12("0030"))
    print(to_12("0009"))
    print(to_12("0000"))
    print(to_12("1500"))
    print(to_12("0300"))