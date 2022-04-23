percent_fats = int(input())
percent_proteins = int(input())
percent_carbohydrates = int(input())
total_calories = int(input())
percent_water_content = int(input())

total_fats_gr = ((percent_fats / 100) * total_calories) / 9
total_protein_gr = ((percent_proteins / 100) * total_calories) / 4
total_carbohydrates_gr = ((percent_carbohydrates / 100) * total_calories) / 4
food_weight = total_fats_gr + total_protein_gr + total_carbohydrates_gr
calories_gr_food = total_calories / food_weight
percent_water = 100 - percent_water_content
calories_gr = (percent_water / 100) * calories_gr_food

print(f"{calories_gr:.4f}")