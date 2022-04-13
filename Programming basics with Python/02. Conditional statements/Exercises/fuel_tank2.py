type_fuel = input()
fuel_quantity = float(input())
club_card = input()

gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93
total_price = 0

if club_card == "Yes":
    if type_fuel == "Gasoline":
        gasoline_price = gasoline_price - 0.18
        total_price = gasoline_price * fuel_quantity
    elif type_fuel == "Diesel":
        diesel_price = diesel_price - 0.12
        total_price = diesel_price * fuel_quantity
    elif type_fuel == "Gas":
        gas_price = gas_price - 0.08
        total_price = gas_price * fuel_quantity
else:
    if type_fuel == "Gasoline":
        total_price = gasoline_price * fuel_quantity
    elif type_fuel == "Diesel":
        total_price = diesel_price * fuel_quantity
    elif type_fuel == "Gas":
        total_price = gas_price * fuel_quantity

if 20 <= fuel_quantity <= 25:
    total_price *= 0.92
elif fuel_quantity > 25:
    total_price *= 0.90

print(f"{total_price:.2f} lv.")

