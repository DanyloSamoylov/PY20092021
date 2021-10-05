
stock = {
    'banana': 6,
    'apple': 0,
    'orange': 32,
    'pear': 15
}
prices = {
    'banana': 4,
    'apple': 2,
    'orange': 1.5,
    'pear': 3
}
result_ = {}
for key in stock:
    if key in prices:
        result_[key] = stock[key] * prices[key]
print(result_)

total = 0
for key in result_:
    if key in result_:
        total += result_[key]
print(total)
