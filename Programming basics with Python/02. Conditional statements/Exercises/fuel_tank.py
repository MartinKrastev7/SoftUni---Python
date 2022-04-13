type_fuel = input()
fuel_in_tank = int(input())

if type_fuel != "Diesel" and type_fuel != "Gasoline" and type_fuel != "Gas":
    print("Invalid fuel!")

elif fuel_in_tank >= 25:
    print(f"You have enough {type_fuel.lower()}.")
elif fuel_in_tank < 25:
        print(f"Fill your tank with {type_fuel.lower()}!")


