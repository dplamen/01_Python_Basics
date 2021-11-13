n = int(input())
hist = [0, 0, 0]
for i in range(n):
    number = int(input())
    if number % 2 == 0:
        hist[0] += 1
    if number % 3 ==0:
        hist[1] += 1
    if number % 4 ==0:
        hist[2] += 1

for p in hist:
    print(f'{p/n*100:.2f}%')
