budget = float(input())
mute_number = int(input())
price_clothing_mute = float(input())

decor_price = budget * 10 / 100
if mute_number > 150:
    price_clothing_mute = mute_number * price_clothing_mute - ((price_clothing_mute * mute_number) * 10 / 100)
else:
    price_clothing_mute = mute_number * price_clothing_mute
total_amount_for_movie = decor_price + price_clothing_mute
difference = abs(total_amount_for_movie - budget)
if budget < total_amount_for_movie:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
elif budget >= total_amount_for_movie:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
