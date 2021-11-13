n = int(input())
count = 0
for i1 in range(n + 1):
    for i2 in range(n + 1):
        for i3 in range(n + 1):
            if i1 + i2 + i3 == n:
                count += 1
print(count)
