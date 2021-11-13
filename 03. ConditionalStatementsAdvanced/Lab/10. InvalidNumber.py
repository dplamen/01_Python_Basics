def is_valid(number):
    if 100 <= number <= 200 or number == 0:
        return True
    return False


n = int(input())
if not is_valid(n):
    print('invalid')
