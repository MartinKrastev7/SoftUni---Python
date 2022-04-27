import sys

number_snowballs = int(input())
best_ball = -sys.maxsize
best_weight = 0
best_time = 0
best_quality = 0


for ball in range(1, number_snowballs + 1):
    weight_snowball = int(input())
    time_needed = int(input())
    quality = int(input())

    value_calc = (weight_snowball / time_needed) ** quality

    if value_calc > best_ball:
        best_ball = value_calc
        best_weight = weight_snowball
        best_time = time_needed
        best_quality = quality
#ili taka bez 3 best - best_quality = {weight_snowball} : {time_needed} = {best ball} ({quality})
print(f"{best_weight} : {best_time} = {best_ball:.0f} ({best_quality})")



