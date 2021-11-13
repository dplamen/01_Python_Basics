age_lili = int(input())
price_machine = float(input())
price_toy = float(input())
 
earning = 0
for i in range(1, age_lili + 1):
    if i % 2 != 0:
        earning += price_toy
    else:
        earning += i / 2 * 10
        earning -= 1

if earning >= price_machine:
    print(f'Yes! {earning - price_machine:.2f}')
else:
    print(f'No! {price_machine - earning:.2f}')

