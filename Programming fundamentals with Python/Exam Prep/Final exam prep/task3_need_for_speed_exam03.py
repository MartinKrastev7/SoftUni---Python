number_of_cars = int(input())
cars_dict = {}

for i in range(number_of_cars):
    cars_lines = input().split("|")
    car_name = cars_lines[0]
    mileage = int(cars_lines[1])
    fuel = int(cars_lines[2])

    current_cars = {}
    current_cars["mileage"] = mileage
    current_cars["fuel"] = fuel
    cars_dict[car_name] = current_cars

command = input()

while command != "Stop":
    command = command.split(" : ")
    current_command = command[0]

    if current_command == "Drive":
        car_name = command[1]
        distance = int(command[2])
        fuel = int(command[3])

        if cars_dict[car_name]["fuel"] >= fuel:
            cars_dict[car_name]["mileage"] += distance
            cars_dict[car_name]["fuel"] -= fuel
            print(f"{car_name} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        else:
            print("Not enough fuel to make that ride")

        if cars_dict[car_name]["mileage"] >= 100000:
            cars_dict.pop(car_name)
            print(f"Time to sell the {car_name}!")

    elif current_command == "Refuel":
        car_name = command[1]
        fuel = int(command[2])
        total = 0

        if cars_dict[car_name]["fuel"] + fuel > 75:
            total = 75 - cars_dict[car_name]["fuel"]
            cars_dict[car_name]["fuel"] = 75
        else:
            total = fuel
            cars_dict[car_name]["fuel"] += total
        print(f"{car_name} refueled with {total} liters")

    elif current_command == "Revert":
        car_name = command[1]
        kilometers = int(command[2])

        cars_dict[car_name]["mileage"] -= kilometers
        if cars_dict[car_name]["mileage"] > 10000:
            print(f"{car_name} mileage decreased by {kilometers} kilometers")
        elif cars_dict[car_name]["mileage"] <= 10000:
            cars_dict[car_name]["mileage"] = 10000

    command = input()

for key in cars_dict:
    print(f"{key} -> Mileage: {cars_dict[key]['mileage']} kms, Fuel in the tank: {cars_dict[key]['fuel']} lt.")