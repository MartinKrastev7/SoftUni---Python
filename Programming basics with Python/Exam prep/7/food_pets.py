number_days = int(input())
total_food = float(input())
total_dog = 0
total_cat = 0
total_biscuit = 0
total_eaten = 0
percent_total_eaten = 0
percent_dog_eaten = 0
percent_cat_eaten = 0

for day in range(1, number_days + 1):
    eaten_dog = int(input())
    eaten_cat = int(input())
    total_dog += eaten_dog
    total_cat += eaten_cat
    if day % 3 == 0:
        total_biscuit += (eaten_cat + eaten_dog) * 0.1
total_eaten = total_dog + total_cat
percent_total_eaten = total_eaten * 100 / total_food
percent_dog_eaten = total_dog * 100 / total_eaten
percent_cat_eaten = total_cat * 100 / total_eaten

print(f"Total eaten biscuits: {int(round(total_biscuit,0))}gr.")
print(f"{percent_total_eaten:.2f}% of the food has been eaten.")
print(f"{percent_dog_eaten:.2f}% eaten from the dog.")
print(f"{percent_cat_eaten:.2f}% eaten from the cat.")
