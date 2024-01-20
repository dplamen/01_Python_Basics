student_name = input()

grade = 1
sum_grade_marks = 0.00
fail = 0

while grade < 13:
    grade_mark = float(input())
    if grade_mark >= 4:
        grade += 1
        sum_grade_marks += grade_mark
    else:
        fail += 1
        if fail == 2:
            print(f'{student_name} has been excluded at {grade} grade')
            break
else:
    print(f'{student_name} graduated. Average grade: {sum_grade_marks / 12:.2f}')
