message = input()
command = input()

while command != "Finish":
    command = command.split(" ")
    current_command = command[0]

    if current_command == "Replace":
        current_char = command[1]
        new_char = command[2]

        message = message.replace(current_char, new_char)
        print(message)

    elif current_command == "Cut":
        start_index = int(command[1])
        end_index = int(command[2])

        if 0 <= start_index <= end_index < len(message):
            message = message[:start_index] + message[end_index + 1:]
            print(message)
        else:
            print("Invalid indices!")

    elif current_command == "Make":
        case = command[1]

        if case == "Upper":
            message = message.upper()
            print(message)
        elif case == "Lower":
            message = message.lower()
            print(message)

    elif current_command == "Check":
        string_check = command[1]

        if string_check in message:
            print(f"Message contains {string_check}")
        else:
            print(f"Message doesn't contain {string_check}")

    elif current_command == "Sum":
        start_index = int(command[1])
        end_index = int(command[2])

        if 0 <= start_index <= end_index < len(message):
            substring = message[start_index:end_index + 1]
            total = 0
            for i in substring:
                total += int(ord(i))
            print(total)
        else:
            print("Invalid indices!")

    command = input()