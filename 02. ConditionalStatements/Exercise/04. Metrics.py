num = float(input())
from_metric = input()
to_metric = input()

if from_metric == 'm':
    if to_metric == 'm':
        conv = 1
    elif to_metric == 'cm':
        conv = 100
    elif to_metric == 'mm':
        conv = 1000
elif from_metric == 'cm':
    if to_metric == 'm':
        conv = 0.01
    elif to_metric == 'cm':
        conv = 1
    elif to_metric == 'mm':
        conv = 10
elif from_metric == 'mm':
    if to_metric == 'm':
        conv = 0.001
    elif to_metric == 'cm':
        conv = 0.1
    elif to_metric == 'mm':
        conv = 1
print(f'{conv*num:.3f}')



