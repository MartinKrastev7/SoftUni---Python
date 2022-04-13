from math import ceil, floor

x_metres_field = int(input())
y_grape_from_metre = float(input())
z_litres_wine = int(input())
workers_number = int(input())

total_grape = x_metres_field * y_grape_from_metre
wine = (total_grape * 0.4) / 2.5
wine_needed = z_litres_wine - wine
wine_left = wine - z_litres_wine

if wine < z_litres_wine:
    wine_needed = floor(wine_needed)
    print(f"It will be a tough winter! More {wine_needed} liters wine needed.")
elif wine >= z_litres_wine:
    wine_needed = floor(wine_needed)
    workers_part = wine_left / workers_number
    workers_part = ceil(workers_part)
    wine_left = ceil(wine_left)
    print(f"Good harvest this year! Total wine: {wine:.0f} liters.")
    print(f"{wine_left:.0f} liters left -> {workers_part} liters per person.")

