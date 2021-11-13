floors = int(input())
rooms = int(input())
for floor in range(floors, 0, -1):
    for room in range(rooms):
        if floor == floors:
            abr = 'L'
        elif floor % 2 == 0:
            abr = 'O'
        else:
            abr = 'A'
        if room < rooms:
            print(f'{abr}{floor}{room}', end=' ')
        else:
            print(f'{abr}{floor}{room}')
    print()
