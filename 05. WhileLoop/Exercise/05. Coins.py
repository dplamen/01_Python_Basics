amount = float(input())
coins = [2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
count = 0
for coin in coins:
    if amount // coin > 0:
        count += amount//coin
        amount = round(amount % coin, 2)
    if amount == 0:
        break
print(int(count))
