n = int(input())
presentation_name = input()
count_presentations = 0
sum_presentations = 0

while presentation_name != 'Finish':
    sum_grades = 0
    for i in range(n):
        sum_grades += float(input())
    print(f"{presentation_name} - {sum_grades/n:.2f}.")
    count_presentations += 1
    sum_presentations += sum_grades/n
    presentation_name = input()

print(f"Student's final assessment is {sum_presentations/count_presentations:.2f}.")
