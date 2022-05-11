items = input().split(", ")
command = input()

while command != "Craft!":
    command = command.split(" - ")
    current_command = command[0]

    if current_command == "Collect":
        current_item = command[1]
        if current_item in items:
            command = input()
            continue
        else:
            items.append(current_item)

    elif current_command == "Drop":
        current_item = command[1]
        if current_item in items:
            items.remove(current_item)

    elif current_command == "Combine Items":
        item = command[1]
        old_item = item.split(":")[0]
        new_item = item.split(":")[1]
        if old_item in items:
            index = items.index(old_item)
            items.insert(index + 1, new_item)

    elif current_command == "Renew":
        current_item = command[1]
        if current_item in items:
            items.remove(current_item)
            items.append(current_item)

    command = input()

print(", ".join(items))
