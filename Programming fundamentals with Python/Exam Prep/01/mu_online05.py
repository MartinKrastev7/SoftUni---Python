initial_health = 100
initial_bitcoin = 0
rooms = input().split("|")
room_number = 0
is_dead = False
for room in rooms:
    current_room = room.split(" ")
    command = current_room[0]
    room_number += 1
    if command == "potion":
        number = int(current_room[1])
        if initial_health + number > 100:
            number = 100 - initial_health
            initial_health = 100
        else:
            initial_health += number
        print(f"You healed for {number} hp.")
        print(f"Current health: {initial_health} hp.")

    elif command == "chest":
        number = int(current_room[1])
        initial_bitcoin += number
        print(f"You found {number} bitcoins.")

    else:
        attack = int(current_room[1])
        initial_health -= attack
        if initial_health <= 0:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room_number}")
            is_dead = True
            break
        else:
            print(f"You slayed {command}.")


if not is_dead:
    print("You've made it!")
    print(f"Bitcoins: {initial_bitcoin}")
    print(f"Health: {initial_health}")
