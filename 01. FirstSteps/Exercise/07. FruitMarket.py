price_strawberries = float(input())
quantity_bananas = float(input())
quantity_oranges = float(input())
quantity_raspberries = float(input())
quantity_strawberries = float(input())

price_raspberries = 0.5 * price_strawberries
price_oranges = 0.60 * price_raspberries
price_bananas = 0.20 * price_raspberries

cost = price_raspberries * quantity_raspberries + price_bananas * quantity_bananas \
       + price_strawberries * quantity_strawberries + price_oranges * quantity_oranges
print(cost)
