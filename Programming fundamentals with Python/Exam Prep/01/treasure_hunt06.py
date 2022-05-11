initial_loot = input().split("|")
command = input()
sum_items = 0
is_empty = False

while command != "Yohoho!":
    command = command.split(" ")
    current_command = command[0]

    if current_command == "Loot":
        for i in range(len(command)):
            if i == 0:
                continue
            item = command[i]
            if item not in initial_loot:
                initial_loot.insert(0, item)


    elif current_command == "Drop":
        index = int(command[1])
        if 0 <= index < len(initial_loot):
            initial_loot.append(initial_loot[index])
            initial_loot.pop(index)

        else:
            command = input()
            continue

    elif current_command == "Steal":
        n = int(command[1])
        if n >= len(initial_loot):
            removed = initial_loot
            print(", ".join(removed))
            print("Failed treasure hunt.")
            is_empty = True
            break
        else:
            removed = initial_loot[-n:]
            del initial_loot[-n:]
            print(", ".join(removed))


    command = input()

if not is_empty:
    for i in range(len(initial_loot)):
        sum_items += len(initial_loot[i])

    average = f"{sum_items / len(initial_loot):.2f}"
    print(f"Average treasure gain: {average} pirate credits.")