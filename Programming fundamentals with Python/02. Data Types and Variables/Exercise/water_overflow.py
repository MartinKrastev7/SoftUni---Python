n = int(input())
tank_capacity = 255
liters_in_tank = 0

for i in range(1, n + 1):
    liters_of_water = int(input())
    liters_in_tank += liters_of_water
    tank_capacity -= liters_of_water

    if tank_capacity < 0:
        liters_in_tank -= liters_of_water
        tank_capacity += liters_of_water
        print("Insufficient capacity!")

        continue

print(f"{liters_in_tank}")

# vtori if variant -
# liter_of_water = int(input)
# if liter_of_water + tank_capacity <= 255:
# tank_capacity += liter_of_water
#continue