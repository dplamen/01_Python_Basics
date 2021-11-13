name = input()
sum_grade = 0.00
year = 1
fail_count = 0
while year <= 12:
    grade = float(input())
    if grade < 4.00:
        fail_count += 1
    else:
        sum_grade += grade
        year += 1
    if fail_count == 2:
        print(f"{name} has been excluded at {year} grade")
        break
if year == 13:
    print(f"{name} graduated. Average grade: {sum_grade / (year - 1):.2f}")
