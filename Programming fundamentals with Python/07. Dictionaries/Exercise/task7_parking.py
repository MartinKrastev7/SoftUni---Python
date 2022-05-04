number_of_commands = int(input())
registered_dict = {}

for i in range(1, number_of_commands + 1):
    command = input().split(" ")

    if command[0] == "register":
        username = command[1]
        license_plate_num = command[2]
       # registered_dict[username] = license_plate_num

        if username in registered_dict.keys():
            print(f"ERROR: already registered with plate number {license_plate_num}")
        else:
            print(f"{username} registered {license_plate_num} successfully")

        registered_dict[username] = license_plate_num

    elif command[0] == "unregister":
        username = command[1]

        if username not in registered_dict:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            registered_dict.pop(username)

for key, value in registered_dict.items():
    print(f"{key} => {value}")