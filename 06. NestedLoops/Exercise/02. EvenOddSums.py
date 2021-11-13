first_num = int(input())
second_num = int(input())
for number in range(first_num, second_num + 1):
    even = 0
    odd = 0
    number = str(number)
    for idx, digit in enumerate(number, 1):
        if idx % 2 == 0:
            even += int(digit)
        else:
            odd += int(digit)
    if even == odd:
        print(number, end=' ')

