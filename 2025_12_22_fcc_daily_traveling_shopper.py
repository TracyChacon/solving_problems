# Traveling Shopper

# Given an amount of money you have, and an array of items you want to buy, determine how many of them you can afford.

#     The given amount will be in the format ["Amount", "Currency Code"]. For example: ["150.00", "USD"] or ["6000", "JPY"].
#     Each array item you want to purchase will be in the same format.

# Use the following exchange rates to convert values:
# Currency 	1 Unit Equals
# USD 	1.00 USD
# EUR 	1.10 USD
# GBP 	1.25 USD
# JPY 	0.0070 USD
# CAD 	0.75 USD

#     If you can afford all the items in the list, return "Buy them all!".
#     Otherwise, return "Buy the first X items.", where X is the number of items you can afford when purchased in the order given.

def buy_items(funds: list[str], items: list[list[str]]) -> str:
    exchange_rates = {
        "USD": 1.00,
        "EUR": 1.10,
        "GBP": 1.25,
        "JPY": 0.0070,
        "CAD": 0.75
    }

    def to_usd(amount: list[str]) -> int|float:
        value = float(amount[0])
        currency = amount[1]
        return value * exchange_rates[currency]
    
    budget_usd = to_usd(funds)
    items_bought = 0

    for item in items:
        item_cost_usd = to_usd(item)

        if budget_usd >= item_cost_usd:
            budget_usd -= item_cost_usd
            items_bought += 1
        else:
            break

    if items_bought == len(items):
        return "Buy them all!"
    else:
        return f"Buy the first {items_bought} items."

# Tests

# Test 1 should return "Buy the first 2 items.".
print(buy_items(["150.00", "USD"], [["50.00", "USD"], ["75.00", "USD"], ["30.00", "USD"]]))
# Test 2 should return "Buy them all!".
print(buy_items(["200.00", "EUR"], [["50.00", "USD"], ["50.00", "USD"]]))
# Test 3 should return "Buy the first 3 items.".
print(buy_items(["100.00", "CAD"], [["20.00", "USD"], ["15.00", "EUR"], ["10.00", "GBP"], ["6000", "JPY"], ["5.00", "CAD"], ["10.00", "USD"]]))
# Test 4 should return "Buy them all!".
print(buy_items(["5000", "JPY"], [["3.00", "USD"], ["1000", "JPY"], ["5.00", "CAD"], ["2.00", "EUR"], ["4.00", "USD"], ["2000", "JPY"]]))
# Test 5 should return "Buy the first 5 items.".
print(buy_items(["200.00", "USD"], [["50.00", "USD"], ["40.00", "EUR"], ["30.00", "GBP"], ["5000", "JPY"], ["25.00", "CAD"], ["20.00", "USD"]]))