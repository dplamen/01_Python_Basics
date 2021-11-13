fruit = input()
day = input()
q = float(input())

menu = 'banana / apple / orange / grapefruit / kiwi / pineapple / grapes'.split(' / ')
prices_day = [2.50, 1.20, 0.85, 1.45, 2.70, 5.50, 3.85]
prices_weekend = [2.70, 1.25, 0.90, 1.60, 3.00, 5.60, 4.20]
error = False

if fruit in menu:
    if day in ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'):
        menu = dict(zip(menu, prices_day))
    elif day in ('Saturday', 'Sunday'):
        menu = dict(zip(menu, prices_weekend))
    else:
        error = True
else:
    error = True
if error:
    print('error')
else:
    print(f'{menu[fruit] * q:.2f}')

