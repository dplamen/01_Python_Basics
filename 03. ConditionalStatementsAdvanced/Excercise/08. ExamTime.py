exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_time = exam_hour * 60 + exam_minute
arrival_time = arrival_hour * 60 + arrival_minute

difference = exam_time - arrival_time

if difference < 0:
    print('Late')
    if difference > -60:
        print(f"{-difference} minutes after the start")
    else:
        difference = f'{-difference // 60}:{-difference % 60:02}'
        print(f"{difference} hours after the start")
elif 0 <= difference <= 30:
    print('On time')
    if difference > 0:
        print(f"{difference} minutes before the start")
else:
    print('Early')
    if difference < 60:
        print(f"{difference} minutes before the start")
    else:
        difference = f'{difference // 60}:{difference % 60:02}'
        print(f"{difference} hours before the start")


