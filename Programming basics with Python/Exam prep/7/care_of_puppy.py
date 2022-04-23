food_bought_kg = int(input())
food_bought_gr = food_bought_kg * 1000
total_eaten = 0
is_food_enough = True
command = input()

while command != "Adopted":
    food_eaten = int(command)
    total_eaten += food_eaten
    if food_bought_gr < total_eaten:
        is_food_enough = False
    command = input()
diff = abs(food_bought_gr - total_eaten)
if is_food_enough:
    print(f"Food is enough! Leftovers: {diff} grams.")
else:
    print(f"Food is not enough. You need {diff} grams more.")
