number_rooms = int(input())
count_room = 0
chairs_left = 0
chairs_needed = 0
all_seats_taken = True
for room in range(number_rooms):
    chairs_visitors = input().split(" ")
    chairs = chairs_visitors[0]
    visitors = int(chairs_visitors[1])
    chairs_needed = 0
    count_room += 1
    if len(chairs) > visitors:
        chairs_left += len(chairs) - visitors
    elif len(chairs) < visitors:
        all_seats_taken = False
        chairs_needed = visitors - len(chairs)
        print(f"{chairs_needed} more chairs needed in room {count_room}")

if all_seats_taken:
    print(f"Game On, {chairs_left} free chairs left")

#vtori nachin
def office_management(number_of_rooms):
    left_chairs = 0
    conditon = True

    for room_number in range(1, number_of_rooms + 1):
        data = input().split(" ")
        available_chairs = data[0]
        visitors = int(data[1])

        diff = abs(len(available_chairs) - visitors)

        if len(available_chairs) < visitors:
            conditon = False
            print(f"{diff} more chairs needed in room {room_number}")

        elif len(available_chairs) > visitors:
            left_chairs += diff

    if conditon:
        print(f"Game On, {left_chairs} free chairs left")


info = int(input())
office_management(info)
