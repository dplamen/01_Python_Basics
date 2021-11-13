puzzle = 2.60
barbie = 3.00
teddy = 4.10
minion = 8.20
truck = 2.00

trip_price = float(input())
puzzle_q = int(input())
barbie_q = int(input())
teddy_q = int(input())
minion_q = int(input())
truck_q = int(input())

revenue = puzzle * puzzle_q + barbie * barbie_q + teddy * teddy_q + minion * minion_q + truck * truck_q
items = puzzle_q + barbie_q + teddy_q + minion_q + truck_q
if items >= 50:
    revenue *= 0.75
cost = 0.10 * revenue

if revenue - cost >= trip_price:
    print(f"Yes! {revenue - cost - trip_price:.2f} lv left.")
else:
    print(f'Not enough money! {trip_price - revenue + cost:.2f} lv needed.')
