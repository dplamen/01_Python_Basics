total = 0.00
deposit = 0.00
command = input()
while command != "NoMoreMoney":
    deposit = float(command)
    if deposit < 0.00:
        print('Invalid operation!')
        break
    total += deposit
    print(f'Increase: {deposit:.2f}')
    command = input()

print(f'Total: {total:.2f}')
