pirate_ship_status = list(map(int, input().split(">")))
warship_status = list(map(int, input().split(">")))
max_health_capacity = int(input())
is_sunken = False
sum_pirate = 0
sum_war = 0
command = input()

while command != "Retire":
    command = command.split(" ")
    current_command = command[0]

    if current_command == "Fire":
        index = int(command[1])
        damaged = int(command[2])
        if 0 <= index < len(warship_status):
            warship_status[index] -= damaged
            if warship_status[index] <= 0:
                print("You won! The enemy ship has sunken.")
                is_sunken = True
                break
        if is_sunken:
            break


    elif current_command == "Defend":
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])
        if 0 <= start_index < len(pirate_ship_status) and 0 <= end_index < len(pirate_ship_status):
          #  pirate_ship_status = [ship - damage for ship in pirate_ship_status[start_index:end_index]]
            for i in range(start_index, end_index + 1):
                pirate_ship_status[i] -= damage
                if pirate_ship_status[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    is_sunken = True
                    break
            if is_sunken:
                break
        if is_sunken:
            break


    elif current_command == "Repair":
        index = int(command[1])
        health = int(command[2])
        if 0 <= index < len(pirate_ship_status):
            if pirate_ship_status[index] + health > max_health_capacity:
                #pirate_ship_status[index] = max_health_capacity
                health = max_health_capacity - pirate_ship_status[index]
            #else:
            pirate_ship_status[index] += health

    elif current_command == "Status":
        repair_value = max_health_capacity * 0.2
        count = 0
        for i in pirate_ship_status:
            if i < repair_value:
                count += 1

        print(f"{count} sections need repair.")

    command = input()


if not is_sunken:
    sum_pirate = sum(pirate_ship_status)
    sum_war = sum(warship_status)

    print(f"Pirate ship status: {sum_pirate}")
    print(f"Warship status: {sum_war}")

#vtori nachin s funkcii
def fire(index, damage, war_ship, flag):
    index = int(index)
    damage = int(damage)
    if 0 <= index < len(war_ship):
        war_ship[index] -= damage
        if war_ship[index] <= 0:
            flag = False
            print("You won! The enemy ship has sunken.")
    return war_ship, flag


def defend(start_index, end_index, damage, pirate_ship, flag):
    start_index = int(start_index)
    end_index = int(end_index)
    damage = int(damage)
    if 0 <= start_index < end_index and start_index < end_index < len(pirate_ship):
        for i in range(start_index, end_index + 1):
            pirate_ship[i] -= damage
            if pirate_ship[i] <= 0:
                flag = False
                print("You lost! The pirate ship has sunken.")
                break
    return pirate_ship, flag


def repair(index, health, pirate_ship, max_health):
    index = int(index)
    health = int(health)
    if 0 <= index < len(pirate_ship):
        if pirate_ship[index] + health < max_health:
            pirate_ship[index] += health
        else:
            pirate_ship[index] = max_health
    return pirate_ship


def status(pirate_ship, maximum_health):
    repairs_lower_than = maximum_health * 0.2
    repair_count = len([_ for _ in pirate_ship if _ < repairs_lower_than])
    print(f"{repair_count} sections need repair.")


status_pirate_ship = [int(_) for _ in input().split(">")]
status_warship = [int(_) for _ in input().split(">")]
max_health = int(input())
command = input()
flag = True
while not command == "Retire" and flag is True:
    command = command.split(' ')
    if command[0] == "Fire":
        status_warship, flag = fire(command[1], command[2], status_warship, flag)
    elif command[0] == "Defend":
        status_pirate_ship, flag = defend(command[1], command[2], command[3], status_pirate_ship, flag)
    elif command[0] == "Repair":
        status_pirate_ship = repair(command[1], command[2], status_pirate_ship, max_health)
    elif command[0] == "Status":
        status = status(status_pirate_ship, max_health)
    command = input()
if flag:
    print(f"Pirate ship status: {sum(status_pirate_ship)}\nWarship status: {sum(status_warship)}")

