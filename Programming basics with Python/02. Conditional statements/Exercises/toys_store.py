trip_price = float(input())
puzzles_number = int(input())
talking_dolls_number = int(input())
teddy_bears_number = int(input())
minions_number = int(input())
trucks_number = int(input())

puzzle_price = 2.60
talking_doll_price = 3
teddy_bear_price = 4.10
minion_price = 8.20
truck_price = 2
amount = puzzles_number * puzzle_price + talking_dolls_number * talking_doll_price \
               + teddy_bears_number * teddy_bear_price + minions_number * minion_price + \
               trucks_number * truck_price
number_of_toys = puzzles_number + talking_dolls_number + teddy_bears_number + minions_number + trucks_number

if number_of_toys >= 50:
    discount = amount * 25 / 100
    amount = amount - discount

rent = amount * 10 / 100
profit = amount - rent

if profit >= trip_price:
    print(f"Yes! {profit - trip_price:.2f} lv left.")
else:
    print(f"Not enough money! {trip_price - profit:.2f} lv needed.")
