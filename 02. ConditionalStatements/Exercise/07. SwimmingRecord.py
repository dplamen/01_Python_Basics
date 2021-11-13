record = float(input())
distance = float(input())
time_one_meter = float(input())

time = distance * time_one_meter
delay = distance // 15 * 12.5
time += delay

if time < record:
    print(f"Yes, he succeeded! The new world record is {time:.2f} seconds.")
else:
    print(f"No, he failed! He was {time - record:.2f} seconds slower.")
