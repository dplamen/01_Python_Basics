start = int(input())
end = int(input())
magic_number = int(input())
count = 0
found = False
for num1 in range(start, end + 1):
    for num2 in range(start, end + 1):
        count += 1
        if num1 + num2 == magic_number:
            found = True
            print(f'Combination N:{count} ({num1} + {num2} = {magic_number})')
            break
    if found:
        break
if not found:
    print(f"{count} combinations - neither equals {magic_number}")
