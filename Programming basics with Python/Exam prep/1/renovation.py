import math

height_wall = int(input())
width_wall = int(input())
percent_not_painted = int(input())
area_painting = height_wall * width_wall * 4
total_area = area_painting - ((area_painting * percent_not_painted) / 100)
total_area = math.ceil(total_area)
command = input()
is_painted = False

while command != "Tired!":
    litres_painting = int(command)
    total_area -= litres_painting

    if total_area <= 0:
        is_painted = True
        break


    command = input()

if is_painted:
    if total_area < 0:
        paint_left = abs(total_area)
        print(f"All walls are painted and you have {paint_left} l paint left!")
    elif total_area == 0:
        print(f"All walls are painted! Great job, Pesho!")

else:
    print(f"{total_area} quadratic m left.")