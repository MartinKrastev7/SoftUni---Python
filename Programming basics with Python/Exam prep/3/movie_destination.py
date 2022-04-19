budget = float(input())
destination = input()
season = input()
days = int(input())

price = 0

if destination == "Dubai":
    if season == "Winter":
        price = days * 45000
        price *= 0.70
    elif season == "Summer":
        price = days * 40000
        price *= 0.70
elif destination == "Sofia":
    if season == "Winter":
        price = days * 17000
        price = price + (price * 0.25)
    elif season == "Summer":
        price = days * 12500
        price = price + (price * 0.25)
elif destination == "London":
    if season == "Winter":
        price = days * 24000

    elif season == "Summer":
        price = days * 20250

diff = abs(budget - price)

if budget >= price:
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")
else:
    print(f"The director needs {diff:.2f} leva more!")