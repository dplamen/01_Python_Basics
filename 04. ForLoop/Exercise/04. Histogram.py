n = int(input())
hist = [0, 0, 0, 0, 0]
for i in range(n):
    number = int(input())
    if number < 200:
        hist[0] += 1
    elif number < 400:
        hist[1] += 1
    elif number < 600:
        hist[2] += 1
    elif number < 800:
        hist[3] += 1
    else:
        hist[4] += 1

for p in hist:
    print(f'{p/n*100:.2f}%')
