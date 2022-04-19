hall_capacity = int(input())

total_money = 0
is_full = False
number_people = 0

command = input()
while command != "Movie time!":
    number = int(command)
    number_people += number
    if hall_capacity < number_people:
        is_full = True
        break

    total_money += number * 5
    if number % 3 == 0:
        total_money -= 5



    command = input()

diff = abs(hall_capacity - number_people)
if is_full:
    print(f"The cinema is full.")
else:
    print(f"There are {diff} seats left in the cinema.")

print(f"Cinema income - {total_money} lv.")