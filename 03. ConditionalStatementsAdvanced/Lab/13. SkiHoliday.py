one_room = 18
apartment = 25
president_apartment = 35

days = int(input())
room_type = input()
grade = input()

discount = 0
if room_type == 'room for one person':
    discount = 0
    price = (days - 1) * (1 - discount) * one_room
elif room_type == 'apartment':
    if days < 10:
        discount = 0.30
    elif days <= 15:
        discount = 0.35
    else:
        discount = 0.50
    price = (days - 1) * (1 - discount) * apartment
elif room_type == 'president apartment':
    if days < 10:
        discount = 0.10
    elif days <= 15:
        discount = 0.15
    else:
        discount = 0.20
    price = (days - 1) * (1 - discount) * president_apartment

if grade == 'positive':
    price *= 1.25
elif grade == 'negative':
    price *= 0.90

print(f'{price:.2f}')
