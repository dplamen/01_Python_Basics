n = int(input())
number = 1
for i in range(n):
    print(number)
    number = 2 * number + 1
    if number > n:
        break
