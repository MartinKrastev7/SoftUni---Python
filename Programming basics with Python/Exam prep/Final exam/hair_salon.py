is_target = False
total_amount = 0
target = int(input())
command = input()
while command != "closed":
    type_hair = input()
    if command == "haircut":
        if type_hair == "mens":
            total_amount += 15
        elif type_hair == "ladies":
            total_amount += 20
        elif type_hair == "kids":
            total_amount += 10
    elif command == "color":
        if type_hair == "touch up":
            total_amount += 20
        elif type_hair == "full color":
            total_amount += 30

    if total_amount >= target:
        is_target = True
        break

    command = input()

diff = abs(target - total_amount)

if is_target:
    print(f"You have reached your target for the day!")
    print(f"Earned money: {total_amount}lv.")
else:
    print(f"Target not reached! You need {diff}lv. more.")
    print(f"Earned money: {total_amount}lv.")