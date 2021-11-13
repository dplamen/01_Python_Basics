from math import pi
type_figure = input()
area = 0
if type_figure == 'square':
    a = float(input())
    area = a * a
elif type_figure == 'rectangle':
    a = float(input())
    b = float(input())
    area = a * b
elif type_figure == 'circle':
    r = float(input())
    area = pi * r * r
elif type_figure == 'triangle':
    a = float(input())
    ha = float(input())
    area = a * ha / 2

print(f'{area:.3f}')
