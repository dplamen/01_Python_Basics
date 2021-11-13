searched_book = input()
line = input()
count = 0
is_found = False
while line != 'No More Books':
    if line == searched_book:
        is_found = True
        print(f"You checked {count} books and found it.")
        break
    count += 1
    line = input()

if not is_found:
    print(f'The book you search is not here!')
    print(f'You checked {count} books.')