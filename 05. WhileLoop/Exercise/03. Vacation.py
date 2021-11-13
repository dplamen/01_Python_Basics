target = float(input())
cash = float(input())
days = 0
days_spend = 0
while True:
    activity = input()
    amount = float(input())
    days += 1
    if activity == 'save':
        cash += amount
        days_spend = 0
    elif activity == 'spend':
        days_spend += 1
        if days_spend == 5:
            print("You can't save the money.")
            print(days)
            break
        if amount > cash:
            cash = 0
        else:
            cash -= amount

    if cash >= target:
        print(f"You saved the money for {days} days.")
        break


