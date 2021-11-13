steps = 10000
going_home = False
while not going_home:
    line = input()
    if line == 'Going home':
        line = input()
        going_home = True
    steps -= int(line)
    if steps < 0:
        print("Goal reached! Good job!")
        print(f"{abs(steps)} steps over the goal!")
        break

if steps > 0:
    print(f"{steps} more steps to reach goal.")
