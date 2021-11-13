budget = float(input())
cast = int(input())
price_cl = float(input())

cost_decor = 0.10 * budget
if cast > 150:
    price_cl *= 0.90
cost_cast = cast * price_cl
total_cost = cost_cast + cost_decor
if total_cost > budget:
    print("Not enough money!")
    print(f"Wingard needs {total_cost - budget:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {budget - total_cost:.2f} leva left.")
