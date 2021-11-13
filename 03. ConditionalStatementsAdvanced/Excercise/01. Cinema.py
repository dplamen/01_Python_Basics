view = input()
rows = int(input())
columns = int(input())

if view == 'Premiere':
    price = 12.00
elif view == 'Normal':
    price = 7.50
elif view == 'Discount':
    price = 5.00

print(f'{price*rows*columns:.2f} leva')