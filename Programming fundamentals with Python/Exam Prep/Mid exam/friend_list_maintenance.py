friends = input().split(", ")
command = input()
blacklisted_count = 0
lost_count = 0
while command != "Report":
    command = command.split(" ")
    current_command = command[0]

    if current_command == "Blacklist":
        name = command[1]
        if name in friends:
            blacklisted_count += 1
            index = friends.index(name)
            friends[index] = "Blacklisted"
            print(f"{name} was blacklisted.")
        else:
            print(f"{name} was not found.")

    elif current_command == "Error":
        index = int(command[1])
        if 0 <= index < len(friends):
            if friends[index] != "Blacklisted" and friends[index] != "Lost":
                print(f"{friends[index]} was lost due to an error.")
                friends[index] = "Lost"
                lost_count += 1

    elif current_command == "Change":
        index = int(command[1])
        new_name = command[2]
        if 0 <= index < len(friends):
            print(f"{friends[index]} changed his username to {new_name}.")

            friends[index] = new_name

    command = input()

print(f"Blacklisted names: {blacklisted_count}")
print(f"Lost names: {lost_count}")
print(" ".join(friends))