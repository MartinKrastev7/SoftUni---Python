budget = float(input())
number_statistics = int(input())
price_clothing = float(input())
price_clothes = 0
decor = budget * 0.10
if number_statistics > 150:
    price_clothes = number_statistics * price_clothing
    price_clothes *= 0.90
else:
    price_clothes = number_statistics * price_clothing
total = decor + price_clothes
diff = abs(budget - total)
if budget >= total:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")