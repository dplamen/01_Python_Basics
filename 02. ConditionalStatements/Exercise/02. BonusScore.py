n = int(input())
if n <= 100:
    bonus = 5
elif n <= 1000:
    bonus = 0.20 * n
else:
    bonus = 0.10 * n

if n % 2 == 0:
    bonus += 1

if n % 10 == 5:
    bonus += 2

print(bonus)
print(bonus + n)
