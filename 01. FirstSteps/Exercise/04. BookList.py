from math import floor

pages = int(input())
pages_per_hour = int(input())
days = int(input())

hours_per_day = floor(pages / pages_per_hour / days)
print(hours_per_day)
