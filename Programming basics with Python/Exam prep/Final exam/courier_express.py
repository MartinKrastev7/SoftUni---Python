package_weight_kg = float(input())
type_delivery = input()
distance_km = int(input())

total_price = 0
percent_over = 0
percent_over_kg = 0
total_percent_over = 0
total_amount_after_over = 0


if type_delivery == "standard":
    if package_weight_kg < 1:
        total_price = distance_km * 0.03
    elif 1 <= package_weight_kg < 10:
        total_price = distance_km * 0.05
    elif 10 <= package_weight_kg < 40:
        total_price = distance_km * 0.10
    elif 40 <= package_weight_kg < 90:
        total_price = distance_km * 0.15
    elif 90 <= package_weight_kg < 150:
        total_price = distance_km * 0.20

elif type_delivery == "express":
    if package_weight_kg < 1:
        total_price = distance_km * 0.03
        percent_over = 0.8 * 0.03
        percent_over_kg = package_weight_kg * percent_over
        total_percent_over = distance_km * percent_over_kg
        total_amount_after_over = total_price + total_percent_over
        total_price = total_amount_after_over
    elif 1 <= package_weight_kg < 10:
        total_price = distance_km * 0.05
        percent_over = 0.4 * 0.05
        percent_over_kg = package_weight_kg * percent_over
        total_percent_over = distance_km * percent_over_kg
        total_amount_after_over = total_price + total_percent_over
        total_price = total_amount_after_over
    elif 10 <= package_weight_kg < 40:
        total_price = distance_km * 0.10
        percent_over = 0.05 * 0.10
        percent_over_kg = package_weight_kg * percent_over
        total_percent_over = distance_km * percent_over_kg
        total_amount_after_over = total_price + total_percent_over
        total_price = total_amount_after_over
    elif 40 <= package_weight_kg < 90:
        total_price = distance_km * 0.15
        percent_over = 0.02 * 0.15
        percent_over_kg = package_weight_kg * percent_over
        total_percent_over = distance_km * percent_over_kg
        total_amount_after_over = total_price + total_percent_over
        total_price = total_amount_after_over
    elif 90 <= package_weight_kg < 150:
        total_price = distance_km * 0.20
        percent_over = 0.01 * 0.20
        percent_over_kg = package_weight_kg * percent_over
        total_percent_over = distance_km * percent_over_kg
        total_amount_after_over = total_price + total_percent_over
        total_price = total_amount_after_over


print(f"The delivery of your shipment with weight of {package_weight_kg:.3f} kg. would cost {total_price:.2f} lv.")