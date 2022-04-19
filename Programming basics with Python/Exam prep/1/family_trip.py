budget = float(input())
number_nights = int(input())
price_per_night = float(input())
percent_additional_costs = int(input())
costs = 0
if number_nights > 7:
    price_per_night -= price_per_night * 0.05

costs = number_nights * price_per_night
costs += budget * (percent_additional_costs / 100)
diff = abs(budget - costs)

if budget >= costs:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    print(f"{diff:.2f} leva needed.")

