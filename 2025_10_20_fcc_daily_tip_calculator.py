# Tip Calculator
# Given the price of your meal and a custom tip percent, return an array with three tip values; 15%, 20%, and the custom amount.

# Prices will be given in the format: "$N.NN".
# Custom tip percents will be given in this format: "25%".
# Return amounts in the same "$N.NN" format, rounded to two decimal places.
# For example, given a "$10.00" meal price, and a "25%" custom tip value, return ["$1.50", "$2.00", "$2.50"].

def calculate_tips(meal_price: str, custom_tip: str) -> list[str]:

    PERCENT_15 = 0.15
    PERCENT_20 = 0.20
    percent_custom = float(custom_tip.replace('%', '')) / 100
    price = float(meal_price.replace("$", ''))

    return [
        f"${round(tip_amount, 2):.2f}" 
        for tip_amount in [price * PERCENT_15, price * PERCENT_20, price * percent_custom]
        ]
    

if __name__ == "__main__":
    # should return ["$1.50", "$2.00", "$2.50"].
    print(calculate_tips("$10.00", "25%") )
    # should return ["$13.45", "$17.93", "$23.31"].
    print(calculate_tips("$89.67", "26%")) 
    # should return ["$2.98", "$3.97", "$1.79"].
    print(calculate_tips("$19.85", "9%")) 