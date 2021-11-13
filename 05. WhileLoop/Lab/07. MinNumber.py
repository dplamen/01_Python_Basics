import sys
min_num = sys.maxsize
line = input()
while line != 'Stop':
    number = int(line)
    if number < min_num:
        min_num = number
    line = input()
print(min_num)
