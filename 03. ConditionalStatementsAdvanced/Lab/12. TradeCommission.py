town = input()
s = float(input())

error = False

if town == 'Sofia':
    if s < 0:
        error = True
    elif s <= 500:
        c = 0.05
    elif s <= 1000:
        c = 0.07
    elif s <= 10000:
        c = 0.08
    else:
        c = 0.12
elif town == 'Varna':
    if s < 0:
        error = True
    elif s <= 500:
        c = 0.045
    elif s <= 1000:
        c = 0.075
    elif s <= 10000:
        c = 0.10
    else:
        c = 0.13
elif town == 'Plovdiv':
    if s < 0:
        error = True
    elif s <= 500:
        c = 0.055
    elif s <= 1000:
        c = 0.08
    elif s <= 10000:
        c = 0.12
    else:
        c = 0.145
else:
    error = True

if error:
    print('error')
else:
    print(f'{s*c:.2f}')

