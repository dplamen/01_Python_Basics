deposit_amt = float(input())
term = int(input())
interest_rate = float(input())

amt_maturity = deposit_amt * (1 +  interest_rate * term / 1200)
print(f'{amt_maturity:.2f}')
