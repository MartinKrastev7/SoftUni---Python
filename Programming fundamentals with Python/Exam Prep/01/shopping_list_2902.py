groceries = input().split("!")


while True:
    command = input()
    if command == "Go Shopping!":
        break
    current_command = command.split(" ")

    if current_command[0] == "Urgent":
        item = current_command[1]
        if item in groceries:
            continue
        else:
            groceries.insert(0, item)

    elif current_command[0] == "Unnecessary":
        item = current_command[1]
        if item in groceries:
            groceries.remove(item)
        else:
            continue

    elif current_command[0] == "Correct":
        old_item = current_command[1]
        new_item = current_command[2]
        groceries = [x if x != old_item else new_item for x in groceries]

    elif current_command[0] == "Rearrange":
        item = current_command[1]
        if item in groceries:
            groceries.remove(item)
            groceries.append(item)


print(", ".join(groceries))
