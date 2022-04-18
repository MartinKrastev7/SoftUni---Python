import math

number_people = int(input())
entrance_tax = float(input())
price_chair = float(input())
price_umbrella = float(input())

total_entrance_tax = number_people * entrance_tax
number_chairs = number_people * 0.75
number_chairs = math.ceil(number_chairs)
total_price_chair = price_chair * number_chairs
number_umbrella = number_people / 2
number_umbrella = math.ceil(number_umbrella)
total_price_umbrella = price_umbrella * number_umbrella
total = total_entrance_tax + total_price_chair + total_price_umbrella
print(f"{total:.2f} lv.")
