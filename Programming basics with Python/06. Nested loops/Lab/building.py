number_of_floors = int(input())
number_of_rooms = int(input())
room_numbers = ""
for f in range(number_of_floors, 0 , -1):
    for r in range(number_of_rooms):
        current_number_of_room = f * 10 + r
        if f == number_of_floors:
            print(f"L{current_number_of_room} ", end="")

        elif f % 2 != 0:
            room_numbers += f"A{current_number_of_room} "
        else:
            room_numbers += f"O{current_number_of_room} "
    print(room_numbers)
    room_numbers = ""


######### vtori variant
floors = int(input())
rooms = int(input())

for floor in range(floors, 0, -1):
    if floor == floors or floors == 1:
        prefix = "L"
    elif floor % 2 == 0:
        prefix = "O"
    else:
        prefix = "A"
    for room in range(rooms):
        print(f"{prefix}{floor}{room}", end=" ")
    print()
