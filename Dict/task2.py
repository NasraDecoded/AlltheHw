# Input data
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
#creating a function that takes two dicts
def total_value (stock,prices):
    total = 0

    for item in stock:
        no_of_stock = stock[item]
        price = prices[item]
        total += no_of_stock * price
    return total

print(total_value(stock,prices))