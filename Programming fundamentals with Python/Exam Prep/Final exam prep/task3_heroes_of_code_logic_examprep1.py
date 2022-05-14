number_heroes = int(input())
heroes_dict = {}

for i in range(number_heroes):
    command = input().split(" ")
    name = command[0]
    hp = int(command[1])
    mp = int(command[2])

    current_dict = {}
    current_dict["HP"] = hp
    current_dict["MP"] = mp
    heroes_dict[name] = current_dict

command = input()

while command != "End":
    command = command.split(" - ")
    current_command = command[0]

    if current_command == "CastSpell":
        name = command[1]
        mp = int(command[2])
        spell = command[3]

        if heroes_dict[name]["MP"] >= mp:
            heroes_dict[name]["MP"] -= mp
            print(f"{name} has successfully cast {spell} and now has {heroes_dict[name]['MP']} MP!")
        else:
            print(f"{name} does not have enough MP to cast {spell}!")

    elif current_command == "TakeDamage":
        name = command[1]
        damage = int(command[2])
        attacker = command[3]

        heroes_dict[name]["HP"] -= damage
        if heroes_dict[name]["HP"] > 0:
            print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes_dict[name]['HP']} HP left!")
        else:
            heroes_dict.pop(name)
            print(f"{name} has been killed by {attacker}!")

    elif current_command == "Recharge":
        name = command[1]
        amount = int(command[2])
        total = 0

        if heroes_dict[name]["MP"] + amount > 200:
            total = 200 - heroes_dict[name]["MP"]
            heroes_dict[name]["MP"] = 200
        else:
            total = amount
            heroes_dict[name]["MP"] += total
        print(f"{name} recharged for {total} MP!")

    elif current_command == "Heal":
        name = command[1]
        amount = int(command[2])
        total = 0

        if heroes_dict[name]["HP"] + amount > 100:
            total = 100 - heroes_dict[name]["HP"]
            heroes_dict[name]["HP"] = 100

        else:
            total = amount
            heroes_dict[name]["HP"] += total

        print(f"{name} healed for {total} HP!")

    command = input()

for key in heroes_dict:
    print(key)
    print(f"  HP: {heroes_dict[key]['HP']}")
    print(f"  MP: {heroes_dict[key]['MP']}")
