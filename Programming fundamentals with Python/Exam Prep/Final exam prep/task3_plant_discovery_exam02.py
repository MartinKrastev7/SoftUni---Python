number_plants = int(input())
plants_dict = {}
rate_dict = {}


for i in range(number_plants):
    plants = input().split("<->")
    current_plant = plants[0]
    rarity = int(plants[1])
    rarity_dict = {}
    rarity_dict["Rarity"] = rarity

    if current_plant not in plants_dict:
        plants_dict[current_plant] = rarity_dict

    else:
        plants_dict[current_plant]["Rarity"] = rarity


command = input()

while command != "Exhibition":
    command = command.split(":")
    current_command = command[0]
    command = command[1].split("-")
    command = [x.strip(" ") for x in command]

    if current_command == "Rate":
        plant = command[0]
        rating = int(command[1])

        if plant in plants_dict:
            if plant not in rate_dict:
                rate_dict[plant] = []
                rate_dict[plant].append(rating)
            else:
                rate_dict[plant].append(rating)
        else:
            print("error")
    elif current_command == "Update":
        plant = command[0]
        new_rarity = int(command[1])

        if plant in plants_dict:
            plants_dict[plant]["Rarity"] = new_rarity
        else:
            print("error")

    elif current_command == "Reset":
        plant = command[0]

        if plant in rate_dict:
            rate_dict[plant].pop()
        else:
            print("error")

    command = input()

print("Plants for the exhibition:")
for key in plants_dict:
    average = 0
    if len(rate_dict[key]) > 0:
        average = sum(rate_dict[key]) / len(rate_dict[key])
    print(f"- {key}; Rarity: {plants_dict[key]['Rarity']}; Rating: {average:.2f}")

#vtori nachin
n = int(input())
plants = {}

for num in range(n):
    data = input().split('<->')
    plant_name = data[0]
    plant_rarity = int(data[1])
    plants[plant_name] = {"rarity": plant_rarity, "rating": []}

command = input()

while not command == 'Exhibition':
    data_1 = command.split(': ')
    data_2 = data_1[1].split(' - ')
    action = data_1[0]
    plant_name = data_2[0]
    if plant_name not in plants:
        print("error")
    elif action == "Rate":
        rating = int(data_2[1])
        plants[plant_name]["rating"].append(rating)
    elif action == "Update":
        new_rarity = int(data_2[1])
        plants[plant_name]["rarity"] = new_rarity
    elif action == "Reset":
        plants[plant_name]["rating"].clear()

    command = input()

print("Plants for the exhibition:")

for plant in plants:
    average_rating = 0
    if plants[plant]["rating"]:
        average_rating = sum(plants[plant]["rating"]) / len(plants[plant]["rating"])
    print(f"- {plant}; Rarity: {plants[plant]['rarity']}; Rating: {average_rating:.2f}")