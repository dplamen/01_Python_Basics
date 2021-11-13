fail_count = int(input())
count_pass = 0
count_fail = 0
score = 0

task_name = input()
while task_name != 'Enough':
    task_eval = float(input())
    if task_eval <= 4:
        count_fail += 1
    else:
        count_pass += 1

    if count_fail == fail_count:
        print(f"You need a break, {count_fail} poor grades.")
        break
    score += task_eval
    last_task = task_name
    task_name = input()
total_count = count_pass + count_fail
if task_name == 'Enough':
    print(f"Average score: {score/total_count:.2f}")
    print(f"Number of problems: {total_count}")
    print(f"Last problem: {last_task}")

