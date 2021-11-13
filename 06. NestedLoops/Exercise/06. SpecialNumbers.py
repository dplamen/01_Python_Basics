N = int(input())
for i1 in range(1, 10):
    for i2 in range(1, 10):
        for i3 in range(1, 10):
            for i4 in range(1, 10):
                if N % i1 == 0 and N % i2 == 0 \
                        and N % i3 == 0 and N % i4 == 0:
                    print(f'{i1}{i2}{i3}{i4}', end=' ')
