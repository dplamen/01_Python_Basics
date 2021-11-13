cake = 45
waffle = 5.80
pancake = 3.20

days = int(input())
chefs = int(input())
cakes = int(input())
waffles = int(input())
pancakes = int(input())

profit = days * (cake * cakes + waffle * waffles + pancake * pancakes) * 7
print(profit)