from math import ceil, floor

days = int(input())
food_kg = int(input())
food_per_day_dog_kg = float(input())
food_per_day_cat_kg = float(input())
food_per_day_turtle_gr = float(input())

needed_food_dog = days * food_per_day_dog_kg
needed_food_cat = days * food_per_day_cat_kg
needed_food_turtle_kg = (days * food_per_day_turtle_gr) / 1000
total_food_needed_kg = needed_food_dog + needed_food_cat + needed_food_turtle_kg
food_left_kg = abs(food_kg - total_food_needed_kg)

if food_kg >= total_food_needed_kg:
    food_left_kg = floor(food_left_kg)
    print(f"{food_left_kg} kilos of food left.")
else:
    food_left_kg = ceil(food_left_kg)
    print(f"{food_left_kg} more kilos of food are needed.")
