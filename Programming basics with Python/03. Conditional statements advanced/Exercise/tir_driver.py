season = input()
km_monthly = float(input())
price_per_km = 0
total_money = 0
salary = 0

if km_monthly <= 5000:
    if season == "Spring" or season == "Autumn":
        price_per_km = 0.75 * km_monthly
    elif season == "Summer":
        price_per_km = 0.90 * km_monthly
    elif season == "Winter":
        price_per_km = 1.05 * km_monthly
elif 5000 < km_monthly <= 10000:
    if season == "Spring" or season == "Autumn":
        price_per_km = 0.95 * km_monthly
    elif season == "Summer":
        price_per_km = 1.10 * km_monthly
    elif season == "Winter":
        price_per_km = 1.25 * km_monthly
elif 10000 < km_monthly <= 20000:
    price_per_km = 1.45 * km_monthly

total_money = price_per_km * 4
salary = total_money - (total_money * 0.1)

print(f"{salary:.2f}")