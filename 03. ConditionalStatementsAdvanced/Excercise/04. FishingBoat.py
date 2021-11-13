budget = int(input())
season = input()
fishermen = int(input())

cost = 0
if season == 'Spring':
    cost += 3000
elif season == 'Summer' or season == 'Autumn':
    cost += 4200
elif season == 'Winter':
    cost += 2600

if 0 < fishermen <= 6:
    cost *= 0.90
elif fishermen <= 11:
    cost *= 0.85
else:
    cost *= 0.75

if fishermen % 2 == 0 and season != 'Autumn':
    cost *= 0.95

if budget >= cost:
    print(f'Yes! You have {budget - cost:.2f} leva left.')
else:
    print(f'Not enough money! You need {cost - budget:.2f} leva.')
