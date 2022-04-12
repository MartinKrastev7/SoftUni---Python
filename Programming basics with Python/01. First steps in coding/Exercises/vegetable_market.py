vegetable_price = float(input())
fruit_price = float(input())
vegetable_kg = int(input())
fruit_kg = int(input())

vegetable_value = vegetable_price * vegetable_kg
fruit_value = fruit_price * fruit_kg
value_eur = (vegetable_value + fruit_value) / 1.94

print(f"{value_eur:.2f}")
