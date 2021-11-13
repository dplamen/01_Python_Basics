flours = {"Roses": [5, 80, 0.10], "Dahlias": [3.80, 90, 0.15],
          "Tulips": [2.80, 80, 0.15], "Narcissus": [3, 120, -0.15],
          "Gladiolus": [2.50, 80, -0.20]}
flour = input()
quantity = int(input())
budget = int(input())

cost = 0
if quantity * flours[flour][2] > flours[flour][1] * flours[flour][2]:
    cost += flours[flour][0] * quantity * (1 - flours[flour][2])
else:
    cost += flours[flour][0] * quantity

if cost <= budget:
    print(f"Hey, you have a great garden with {quantity} {flour} and {budget-cost:.2f} leva left.")
else:
    print(f"Not enough money, you need {cost - budget:.2f} leva more.")