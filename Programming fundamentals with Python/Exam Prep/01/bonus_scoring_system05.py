import math
#import sys

number_students = int(input())
number_lectures = int(input())
additional_bonus = int(input())
#max_bonus = -sys.maxsize
max_bonus = 0
high_attendances = 0
total_bonus = 0


for i in range(number_students):
    count_attendances = int(input())
    total_bonus = count_attendances / number_lectures * (5 + additional_bonus)

    if total_bonus >= max_bonus:
        max_bonus = total_bonus
        high_attendances = count_attendances


max_bonus = math.ceil(max_bonus)
print(f"Max Bonus: {max_bonus}.")
print(f"The student has attended {high_attendances} lectures.")