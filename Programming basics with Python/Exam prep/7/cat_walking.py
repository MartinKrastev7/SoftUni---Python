minutes_per_day = int(input())
number_walks = int(input())
calories_per_day = int(input())

total_minutes = minutes_per_day * number_walks
total_calories = total_minutes * 5
percent_calories = calories_per_day / 2

if percent_calories <= total_calories:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {total_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {total_calories}.")