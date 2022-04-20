import math

price_tennis_rocket = float(input())
number_tennis_rocket = int(input())
number_trainers = int(input())

price_trainers = 1/6 * price_tennis_rocket
total_rockets_price = number_tennis_rocket * price_tennis_rocket
total_trainers_price = number_trainers * price_trainers
price_another_equipment = (total_trainers_price + total_rockets_price) * 0.2
total_price = total_rockets_price + total_trainers_price + price_another_equipment
price_for_djokovic = total_price / 8
price_for_djokovic = math.floor(price_for_djokovic)
price_for_sponsors = total_price * 7/8
price_for_sponsors = math.ceil(price_for_sponsors)

print(f"Price to be paid by Djokovic {price_for_djokovic}")
print(f"Price to be paid by sponsors {price_for_sponsors}")

