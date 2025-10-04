# Space Week Day 1: Stellar Classification
# October 4th marks the beginning of World Space Week. The next seven days will bring you astronomy-themed coding challenges.

# For today's challenge, you are given the surface temperature of a star in Kelvin (K) and need to determine its stellar classification based on the following ranges:

# "O": 30,000 K or higher

# "B": 10,000 K - 29,999 K

# "A": 7,500 K - 9,999 K

# "F": 6,000 K - 7,499 K

# "G": 5,200 K - 5,999 K

# "K": 3,700 K - 5,199 K

# "M": 0 K - 3,699 K

# Return the classification of the given star.

def classification(temp: int) -> str:

    match temp:
        case kevin if kevin >= 30000:
            return "O" 
        case kevin if 10000 <= kevin <= 29999:
            return "B" 
        case kevin if 7500 <= kevin <= 9999:
            return "A" 
        case kevin if 6000 <= kevin <= 7499:
            return "F" 
        case kevin if 5200 <= kevin <= 5999:
            return "G" 
        case kevin if 3700 <= kevin <= 5199:
            return "K" 
        case kevin if 0 <= kevin <= 3699:
            return "M" 
        case _:
            return "Error: Something went wrong somewhere."

if __name__ == "__main__":
    print(classification(9999))





