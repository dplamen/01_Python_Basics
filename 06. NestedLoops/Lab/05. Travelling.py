destination = input()
while destination != 'End':
    budget = float(input())
    while budget > 0:
        budget -= float(input())
    if budget <= 0:
        print(f'Going to {destination}!')
    destination = input()

