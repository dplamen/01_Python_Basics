n = int(input())
current = 1
flag = False
for row in range(1, n + 1):
    for col in range(1, row + 1):
        if current <= n:
            print(str(current) + ' ', end='')
            current += 1
        else:
            flag = True
            break
    if flag:
        break
    print()
