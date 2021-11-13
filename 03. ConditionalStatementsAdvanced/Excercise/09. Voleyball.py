import math
year = input()
p = int(input())
h = int(input())

weekends = 48
plays = (weekends - h) * 3 / 4 + h + p * 2 / 3

if year == 'leap':
    plays *= 1.15

print(math.floor(plays))


