import sys
max_num = -sys.maxsize
line = input()
while line != 'Stop':
    number = int(line)
    if number > max_num:
        max_num = number
    line = input()
print(max_num)
