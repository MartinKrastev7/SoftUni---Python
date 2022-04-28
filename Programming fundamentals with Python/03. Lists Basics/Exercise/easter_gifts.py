gifts = input().split(" ")
commands = input()

while commands != "No Money":
    current_command = commands.split(" ")
    command = current_command[0]
    new_gift = current_command[1]

    if command == "OutOfStock":
        if new_gift in gifts:
            gifts = [x if x != new_gift else "None" for x in gifts]
    elif command == "Required":
        index = int(current_command[2])
        if 0 <= index < len(gifts):
            gifts[index] = new_gift
    elif command == "JustInCase":
        gifts.pop()
        gifts.append(new_gift)
    commands = input()

for i in gifts:
    if "None" in gifts:
        gifts.remove("None")
print(" ".join(gifts))
