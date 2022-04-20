budget = float(input())
litres_fuel_needed = float(input())
day = input()

fuel_price = litres_fuel_needed * 2.10
sum_fuel_guide = fuel_price + 100

if day == "Saturday":
    sum_fuel_guide *= 0.90
elif day == "Sunday":
    sum_fuel_guide *= 0.80

diff = abs(budget - sum_fuel_guide)

if budget >= sum_fuel_guide:
    print(f"Safari time! Money left: {diff:.2f} lv.")
else:
    print(f"Not enough money! Money needed: {diff:.2f} lv.")