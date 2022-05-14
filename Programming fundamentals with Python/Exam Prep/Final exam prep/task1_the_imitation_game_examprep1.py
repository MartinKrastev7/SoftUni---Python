message = input()
command = input()

while command != "Decode":
    command = command.split("|")
    current_command = command[0]

    if current_command == "Move":
        number = int(command[1])

        message = message[number:] + message[:number]

    elif current_command == "Insert":
        index = int(command[1])
        value = command[2]

        message = message[:index] + value + message[index:]

    elif current_command == "ChangeAll":
        substring = command[1]
        replacement = command[2]

        message = message.replace(substring, replacement)

    command = input()

print(f"The decrypted message is: {message}")