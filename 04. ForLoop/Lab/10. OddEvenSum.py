n = int(input())
left_sum = 0
right_sum = 0
for i in range(n):
    if i % 2 == 0:
        left_sum += int(input())
    else:
        right_sum += int(input())

if left_sum == right_sum:
    print(f"Yes\nSum = {left_sum}")
else:
    print(f"No\nDiff = {abs(left_sum - right_sum)}")
