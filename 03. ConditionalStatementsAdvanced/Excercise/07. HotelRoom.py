month = input()
nights = int(input())

flat = 0
studio = 0

if month in ('May', 'October'):
    if 0 < nights <= 7:
        studio = 50
        flat = 65
    elif nights <= 14:
        studio = 50 * 0.95
        flat = 65
    else:
        studio = 50 * 0.70
        flat = 65 * 0.90

elif month in ('June', 'September'):
    if 0 < nights <= 14:
        studio = 75.20
        flat = 68.70
    else:
        studio = 75.20 * 0.80
        flat = 68.70 * 0.90

elif month in ('July', 'August'):
    if 0 < nights <= 14:
        studio = 76
        flat = 77
    else:
        studio = 76
        flat = 77 * 0.90

print(f"Apartment: {flat * nights:.2f} lv.")
print(f"Studio: {studio * nights:.2f} lv.")



