def is_prime(number):
    prime = True
    if number < 2:
        prime = False
    for i in range(2, number):
        if number % i == 0:
            prime = False
    return prime


sum_prime = 0
sum_non_prime = 0
command = input()
while command != 'stop':
    n = int(command)
    if n < 0:
        print('Number is negative.')
    elif is_prime(n):
        sum_prime += n
    else:
        sum_non_prime += n
    command = input()

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")




