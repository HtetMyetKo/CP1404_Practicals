items = int(input("Number of items: "))
overall_prices = []

for i in range(0, items):
    price = float(input("Price of item: "))
    overall_prices.append(price)
total = sum(overall_prices)

if total > 100:
    discount = total - (total * 0.1)
    print("Total price for {} items is ${:.2f}".format(items, discount))

else:
    print("Total price for {} items is ${:.2f}" .format(items, total))
