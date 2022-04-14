budget = float(input())
category = input()
people_in_group = int(input())
transport = 0
ticket_price = 0

if 1 <= people_in_group <= 4:
    transport = budget * 0.75
elif people_in_group < 10:
    transport = budget * 0.60
elif people_in_group < 25:
    transport = budget * 0.50
elif people_in_group < 50:
    transport = budget * 0.40
else:
    transport = budget * 0.25

if category == "VIP":
    ticket_price = 499.99 * people_in_group
elif category == "Normal":
    ticket_price = 249.99 * people_in_group

diff = budget - transport
money_left = abs(ticket_price - diff)

if diff >= ticket_price:
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    print(f"Not enough money! You need {money_left:.2f} leva.")