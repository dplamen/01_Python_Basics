tabs = int(input())
salary = int(input())
sites = {'Facebook': 150, 'Instagram': 100, 'Reddit': 50}
for i in range(tabs):
    site = input()
    if site in sites:
        salary -= sites[site]
    if salary <= 0:
        break
if salary > 0:
    print(salary)
else:
    print('You have lost your salary.')