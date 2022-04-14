budget = int(input())
season = input()
number_fishers = int(input())
rent = 0

if season == "Spring":
    rent = 3000
    if number_fishers <= 6:
        rent = rent - (rent * 0.1)
    elif 7 <= number_fishers <= 11:
        rent = rent - (rent * 0.15)
    elif number_fishers > 12:
        rent = rent - (rent * 0.25)
    elif number_fishers % 2 == 0:
        rent = rent - (rent * 0.05)

elif season == "Summer" or season == "Autumn":
    rent = 4200
    if number_fishers <= 6:
        rent = rent - (rent * 0.1)
    elif 7 <= number_fishers <= 11:
        rent = rent - (rent * 0.15) # rent = rent * 0.85
    elif number_fishers > 12:
        rent = rent - (rent * 0.25)
    elif number_fishers % 2 == 0 and season != "Autumn":
        rent = rent - (rent * 0.05)

elif season == "Winter":
    rent = 2600
    if number_fishers <= 6:
        rent = rent - (rent * 0.1)
    elif 7 <= number_fishers <= 11:
        rent = rent - (rent * 0.15)
    elif number_fishers > 12:
        rent = rent - (rent * 0.25)
    elif number_fishers % 2 == 0:
        rent = rent - (rent * 0.05)

needed_money = abs(budget - rent)
if budget >= rent:
    print(f"Yes! You have {needed_money:.2f} leva left.")
elif budget < rent:
    print(f"Not enough money! You need {needed_money:.2f} leva.")

##########  vtoro reshenie upr
budget = int(input())
season = input()
number_fishers = int(input())
rent = 0

if season == "Spring":
    rent = 3000
elif season == "Summer" or season == "Autumn":
    rent = 4200
elif season == "Winter":
    rent = 2600
if number_fishers <= 6:
    rent *= 0.9
elif number_fishers <= 11:
    rent *= 0.85
else:
    rent *= 0.75
if season != "Autumn" and number_fishers % 2 == 0:
    rent *= 0.95

needed_money = abs(budget - rent)
if budget >= rent:
    print(f"Yes! You have {needed_money:.2f} leva left.")
elif budget < rent:
    print(f"Not enough money! You need {needed_money:.2f} leva.")