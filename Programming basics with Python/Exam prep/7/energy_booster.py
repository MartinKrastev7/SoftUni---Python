fruit_type = input()
size_set = input()
number_ordered_sets = int(input())
price_watermelon = 0
price_mango = 0
price_pineapple = 0
price_raspberry = 0
total_price = 0

if size_set == "small":
    if fruit_type == "Watermelon":
        price_watermelon = 2 * 56
        total_price = number_ordered_sets * price_watermelon
    elif fruit_type == "Mango":
        price_mango = 2 * 36.66
        total_price = number_ordered_sets * price_mango
    elif fruit_type == "Pineapple":
        price_pineapple = 2 * 42.10
        total_price = number_ordered_sets * price_pineapple
    elif fruit_type == "Raspberry":
        price_raspberry = 2 * 20
        total_price = number_ordered_sets * price_raspberry
elif size_set == "big":
    if fruit_type == "Watermelon":
        price_watermelon = 5 * 28.70
        total_price = number_ordered_sets * price_watermelon
    elif fruit_type == "Mango":
        price_mango = 5 * 19.60
        total_price = number_ordered_sets * price_mango
    elif fruit_type == "Pineapple":
        price_pineapple = 5 * 24.80
        total_price = number_ordered_sets * price_pineapple
    elif fruit_type == "Raspberry":
        price_raspberry = 5 * 15.20
        total_price = number_ordered_sets * price_raspberry

if 400 <= total_price <= 1000:
    total_price *= 0.85
elif total_price > 1000:
    total_price *= 0.50
print(f"{total_price:.2f} lv.")
