n = int(input())
l = int(input())

for i1 in range(1, n + 1):
    for i2 in range(1, l + 1):
        for i3 in range(97, 97 + l):
            for i4 in range(97, 97 + l):
                for i5 in range(1, n + 1):
                    if i5 > i1 and i5 > i2:
                        print(str(i1) + str(i2) + chr(i3) + chr(i4) + str(i5), end=' ')
