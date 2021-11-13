width = int(input())
length = int(input())
size = width * length
box = input()
while not box == 'STOP':
    box = int(box)
    if size >= box:
        size -= box
    else:
        print(f"No more cake left! You need {box - size} pieces more.")
        break
    box = input()

if box == 'STOP':
    print(f"{size} pieces are left.")
