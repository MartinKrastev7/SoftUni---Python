budget = float(input())
season = input()
destination = ""
price = 0
type_of_holiday = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        price = budget * 0.3
        type_of_holiday = "Camp"
    elif season == "winter":
        price = budget * 0.7
        type_of_holiday = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        price = budget * 0.4
        type_of_holiday = "Camp"
    elif season == "winter":
        price = budget * 0.8
        type_of_holiday = "Hotel"
elif budget > 1000:
    destination = "Europe"
    price = budget * 0.9
    type_of_holiday = "Hotel"
print(f"Somewhere in {destination}")
print(f"{type_of_holiday} - {price:.2f}")
