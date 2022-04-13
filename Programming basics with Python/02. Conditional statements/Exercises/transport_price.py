n_km = int(input())
travel_time = input()
price_of_cheapest_transport = 0
day_tax = 0
night_tax = 0

if n_km < 20:
    entrance_tax = 0.70
    if travel_time == "day":
        day_tax = 0.79
        price_of_cheapest_transport = (day_tax * n_km) + entrance_tax
    elif travel_time == "night":
        night_tax = 0.90
        price_of_cheapest_transport = (night_tax * n_km) + entrance_tax
elif 20 <= n_km < 100:
    day_tax = 0.09
    price_of_cheapest_transport = day_tax * n_km
elif 100 <= n_km:
    day_tax = 0.06
    price_of_cheapest_transport = day_tax * n_km

print(f"{price_of_cheapest_transport:.2f}")