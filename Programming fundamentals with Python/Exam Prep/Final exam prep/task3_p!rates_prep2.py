command = input()
cities_dict = {}

while command != "Sail":
    command = command.split("||")
    city = command[0]
    population = int(command[1])
    gold = int(command[2])

    if city not in cities_dict:
        current_city_dict = {}
        current_city_dict["people"] = population
        current_city_dict["gold"] = gold
        cities_dict[city] = current_city_dict
    else:
        cities_dict[city]["people"] += population
        cities_dict[city]["gold"] += gold

    command = input()

command_events = input()

while command_events != "End":
    command_events = command_events.split("=>")
    current_command = command_events[0]

    if current_command == "Plunder":
        town = command_events[1]
        people = int(command_events[2])
        gold = int(command_events[3])

        cities_dict[town]["people"] -= people
        cities_dict[town]["gold"] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

        if cities_dict[town]["people"] == 0 or cities_dict[town]["gold"] == 0:
            cities_dict.pop(town)
            print(f"{town} has been wiped off the map!")

    elif current_command == "Prosper":
        town = command_events[1]
        gold = int(command_events[2])

        if gold < 0:
            print(f"Gold added cannot be a negative number!")
            command_events = input()
            continue
        else:
            cities_dict[town]["gold"] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities_dict[town]['gold']} gold.")

    command_events = input()

if len(cities_dict.keys()) > 0:
    print(f"Ahoy, Captain! There are {len(cities_dict.keys())} wealthy settlements to go to:")
    for city in cities_dict:
        print(f"{city} -> Population: {cities_dict[city]['people']} citizens, Gold: {cities_dict[city]['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")

#vtori nachin
def extract_func(command, data_dict):
    command = command.split("||")
    town = command[0]
    population = int(command[1])
    gold = int(command[2])

    if town not in data_dict:
        data_dict[town] = [population, gold]
    else:
        data_dict[town][0] += population
        data_dict[town][1] += gold

    return data_dict


def sail_func(command, data_dict):
    command = command.split("=>")
    current_command = command[0]

    if current_command == "Plunder":
        town = command[1]
        people = int(command[2])
        gold = int(command[3])

        data_dict[town][0] -= people
        data_dict[town][1] -= gold

        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

        if data_dict[town][0] <= 0 or data_dict[town][1] <= 0:
            del data_dict[town]
            print(f"{town} has been wiped off")

    elif current_command == "Prosper":
        town = command[1]
        gold = int(command[2])

        if gold > 0:
            data_dict[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {data_dict[town][1]} gold.")
        else:
            print("Gold added cannot be a negative number!")

    return data_dict


def pirates():
    data_dict = {}

    while True:
        command = input()
        condition = False

        if command == "End":
            break

        elif command != "Sail" and not condition:
            data_dict = extract_func(command, data_dict)

        elif command == "Sail":
            condition = True
            continue

        elif condition:
            data_dict = sail_func(command, data_dict)

        print(f"Ahoy capitane {len(data_dict)}")

        for data in data_dict:
            town = data
            current_population = data_dict[data][0]
            gold = data_dict[data][1]

            print(f"{town} -> Population: {current_population}, Gold: {gold}")

pirates()