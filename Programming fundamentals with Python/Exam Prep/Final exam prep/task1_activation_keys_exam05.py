raw_key = input()
command = input()

while command != "Generate":
    command = command.split(">>>")
    current_command = command[0]

    if current_command == "Contains":
        substring = command[1]
        if substring in raw_key:
            print(f"{raw_key} contains {substring}")
        else:
            print("Substring not found!")

    elif current_command == "Flip":
        action = command[1]
        start_index = int(command[2])
        end_index = int(command[3])

        if action == "Upper":
            new_key = (raw_key[start_index:end_index]).upper()
            old_key = raw_key[start_index:end_index]
            raw_key = raw_key.replace(old_key, new_key)
        elif action == "Lower":
            new_key = (raw_key[start_index:end_index]).lower()
            old_key = raw_key[start_index:end_index]
            raw_key = raw_key.replace(old_key, new_key)

        print(raw_key)

    elif current_command == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])

        characters = raw_key[start_index:end_index]
        raw_key = raw_key.replace(characters, "")
        print(raw_key)

    command = input()

print(f"Your activation key is: {raw_key}")
