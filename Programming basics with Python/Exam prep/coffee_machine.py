drink = input()
sugar = input()
number_drinks = int(input())

price = 0

if drink == "Espresso":
    if sugar == "Without":
        price = number_drinks * 0.9
        price = price - (price * 0.35)
    elif sugar == "Normal":
        price = number_drinks * 1
    elif sugar == "Extra":
        price = number_drinks * 1.2
    if number_drinks >= 5:
        price *= 0.75
elif drink == "Cappuccino":
    if sugar == "Without":
        price = number_drinks * 1
        price = price - (price * 0.35)
    elif sugar == "Normal":
        price = number_drinks * 1.2
    elif sugar == "Extra":
        price = number_drinks * 1.6
elif drink == "Tea":
    if sugar == "Without":
        price = number_drinks * 0.5
        price = price - (price * 0.35)
    elif sugar == "Normal":
        price = number_drinks * 0.6
    elif sugar == "Extra":
        price = number_drinks * 0.7

if price > 15:
    price *= 0.80

print(f"You bought {number_drinks} cups of {drink} for {price:.2f} lv.")