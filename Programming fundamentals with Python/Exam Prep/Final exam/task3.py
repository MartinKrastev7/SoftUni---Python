facebook_dict = {}
command = input()

while command != "Log out":
    command = command.split(": ")
    current_command = command[0]

    if current_command == "New follower":
        user = command[1]

        if user not in facebook_dict:
            facebook_dict[user] = {"likes": 0, "comments": 0}

    elif current_command == "Like":
        user = command[1]
        count = int(command[2])

        if user not in facebook_dict:
            facebook_dict[user] = {"likes": count, "comments": 0}
        else:
            facebook_dict[user]["likes"] += count

    elif current_command == "Comment":
        user = command[1]

        if user not in facebook_dict:
            facebook_dict[user] = {"comments": 1, "likes": 0}
        else:
            facebook_dict[user]["comments"] += 1

    elif current_command == "Blocked":
        user = command[1]

        if user in facebook_dict:
            facebook_dict.pop(user)
        else:
            print(f"{user} doesn't exist.")

    command = input()

print(f"{len(facebook_dict)} followers")
for key in facebook_dict:
    print(f"{key}: {facebook_dict[key]['likes'] + facebook_dict[key]['comments']}")
