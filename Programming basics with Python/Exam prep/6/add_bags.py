price_luggage_over_20kg = float(input())
kg_luggage = float(input())
days_to_travel = int(input())
number_luggage = int(input())

if kg_luggage < 10:
    price_luggage_over_20kg *= 0.2
elif 10 <= kg_luggage <= 20:
    price_luggage_over_20kg *= 0.5

if days_to_travel > 30:
    price_luggage_over_20kg = (price_luggage_over_20kg * 0.1) + price_luggage_over_20kg
elif 7 <= days_to_travel <= 30:
    price_luggage_over_20kg = (price_luggage_over_20kg * 0.15) + price_luggage_over_20kg
else:
    price_luggage_over_20kg = (price_luggage_over_20kg * 0.40) + price_luggage_over_20kg

total_price = price_luggage_over_20kg * number_luggage

print(f"The total price of bags is: {total_price:.2f} lv.")

