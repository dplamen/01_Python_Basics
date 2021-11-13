N1 = int(input())
N2 = int(input())
operation = input()

if operation in ('+', '-', '*'):
    result = eval(str(N1) + operation + str(N2))
    if result % 2 == 0:
        even_odd = 'even'
    else:
        even_odd = 'odd'
    print(f"{N1} {operation} {N2} = {result} - {even_odd}")
elif operation == '/':
    if N2 != 0:
        result = N1 / N2
        print(f"{N1} / {N2} = {result:.2f}")
    else:
        print(f"Cannot divide {N1} by zero")
elif operation == '%':
    if N2 != 0:
        result = N1 % N2
        print(f"{N1} % {N2} = {result}")
    else:
        print(f"Cannot divide {N1} by zero")
