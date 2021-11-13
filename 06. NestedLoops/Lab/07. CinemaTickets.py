tickets = {'student': 0, 'standard': 0, 'kid': 0, 'total': 0}
movie = input()
while movie != 'Finish':
    total_movie = 0
    free_places = int(input())
    for i in range(free_places):
        ticket = input()
        if ticket in tickets:
            total_movie += 1
            tickets[ticket] += 1
            tickets['total'] += 1
        if ticket == 'End':
            break
    print(f"{movie} - {total_movie/free_places * 100:.2f}% full.")
    movie = input()
print(f"Total tickets: {tickets['total']}")
print(f"{tickets['student']/tickets['total']*100:.2f}% student tickets.")
print(f"{tickets['standard']/tickets['total']*100:.2f}% standard tickets.")
print(f"{tickets['kid']/tickets['total']*100:.2f}% kids tickets.")
