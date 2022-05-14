new_stops = input()
command = input()


while command != "Travel":
    command = command.split(":")
    current_command = command[0]
    if current_command == "Add Stop":
        index = int(command[1])
        string_new = command[2]

        if 0 <= index <= len(new_stops):
            new_stops = new_stops[:index] + string_new + new_stops[index:]
        print(new_stops)

    elif current_command == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index < len(new_stops) and 0 <= end_index < len(new_stops):
            new_stops = new_stops[0:start_index] + new_stops[end_index + 1:]
        print(new_stops)

    elif current_command == "Switch":
        old_string = command[1]
        new_string = command[2]

        if old_string in new_stops:
            new_stops = new_stops.replace(old_string, new_string)
        print(new_stops)

    command = input()

print(f"Ready for world tour! Planned stops: {new_stops}")

#vtori nachin
def world_tour(destinations):


    while True:
        command = input().split(":")

        if command[0] == "Travel":
            print(f"Ready for world tour! Planned stops: {destinations}")
            break

        elif command[0] == "Add Stop":
            index = int(command[1])
            string = command[2]

            if 0 <= index <= len(destinations):
                destinations = destinations[:index] + string + destinations[index:]

        elif command[0] == "Remove Stop":
            start_index = int(command[1])
            end_index = int(command[2])

            if 0 <= start_index <= end_index < len(destinations):
                destinations = destinations[:start_index] + destinations[end_index + 1:]


        elif command[0] == "Switch":
            old_string = command[1]
            new_string = command[2]

            if old_string in destinations:
                destinations = destinations.replace(old_string,new_string)


        print(destinations)


data = input()
world_tour(data)