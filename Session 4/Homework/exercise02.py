prices = {
    'banana': 4,
    'apple': 2,
    'orange': 1.5,
    'pear': 3
}

stock = {
    'banana': 6,
    'apple': 0,
    'orange': 32,
    'pear': 15
}

print("Hello!\nHere are the items I have:")

for key in prices:
    print('{0}: {1}\nprice: {2}\n'.format(key, stock[key], prices[key]))

total = 0
for key, value in prices.items():
    total = total + prices[key] * stock[key]

print("Total price if I sell all of my food:", total)
