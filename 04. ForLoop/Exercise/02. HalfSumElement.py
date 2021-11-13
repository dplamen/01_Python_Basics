import sys
n = int(input())
max_num = -sys.maxsize
sum = 0
for i in range(n):
    number = int(input())
    if number > max_num:
        max_num = number
    sum += number

difference = sum - 2 * max_num
if difference == 0:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    print("No")
    print(f'Diff = {abs(difference)}')


