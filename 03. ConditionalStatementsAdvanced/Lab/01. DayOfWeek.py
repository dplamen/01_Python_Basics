days = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
day = int(input())
if day in days:
    print(days[day])
else:
    print("Error")