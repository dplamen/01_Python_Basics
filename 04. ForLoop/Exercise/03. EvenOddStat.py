import sys
n = int(input())
OddSum = 0
EvenSum = 0
OddMin = sys.maxsize
OddMax = -sys.maxsize
EvenMin = sys.maxsize
EvenMax = -sys.maxsize

for i in range(1, n + 1):
    number = float(input())
    if i % 2 == 0:
        EvenSum += number
        if number > EvenMax:
            EvenMax = number
        if number < EvenMin:
            EvenMin = number
    else:
        OddSum += number
        if number > OddMax:
            OddMax = number
        if number < OddMin:
            OddMin = number

print(f'OddSum={OddSum:.2f},')
print(f'OddMin={OddMin:.2f},') if n > 0 else print(f'OddMin=No,')
print(f'OddMax={OddMax:.2f},') if n > 0 else print(f'OddMax=No,')
print(f'EvenSum={EvenSum:.2f},')
print(f'EvenMin={EvenMin:.2f},') if n > 1 else print(f'EvenMin=No,')
print(f'EvenMax={EvenMax:.2f}') if n > 1 else print(f'EvenMax=No')