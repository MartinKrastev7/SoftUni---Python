capacity = float(input())
is_capacity_full = False
command = input()
total_loads = 0
third_load = 0
while command != "End":
    current_load = float(command)
    third_load += 1
    if total_loads == 3:
        current_load = current_load + (current_load * 0.10)
        third_load = 0

    if capacity <= current_load:
        is_capacity_full = True
        print("No more space!")
        break
    total_loads += 1
    capacity -= current_load
    command = input()
    if command == "End":
        print("Congratulations! All suitcases are loaded!")
print(f"Statistic: {total_loads} suitcases loaded.")

############ vtoro reshenie
load_capacity = float(input())
command = input()
suitcase_volume = 0
free_volume = load_capacity
counter = 0
enough_space = True
while command != 'End':
    suitcase_volume = float(command)
    counter += 1
    if counter % 3 == 0:
        suitcase_volume *= 1.1
    if free_volume < suitcase_volume:
        enough_space = False
        counter -= 1
        break
    free_volume -= suitcase_volume
    command = input()
if not enough_space:
    print(f'No more space!')
else:
    print(f'Congratulations! All suitcases are loaded!')
print(f'Statistic: {counter} suitcases loaded.')