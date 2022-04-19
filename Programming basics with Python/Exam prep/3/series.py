budget = float(input())
number_series = int(input())
diff = 0
amount = budget
for serial in range(1,number_series + 1):
    serial_name = input()
    serial_price = float(input())

    if serial_name == "Thrones":
        serial_price *= 0.50
    elif serial_name == "Lucifer":
        serial_price *= 0.60
    elif serial_name == "Protector":
        serial_price *= 0.70
    elif serial_name == "TotalDrama":
        serial_price *= 0.80
    elif serial_name == "Area":
        serial_price *= 0.90

    amount -= serial_price
    diff += serial_price

if budget >= diff:
    print(f"You bought all the series and left with {amount:.2f} lv.")
else:
    print(f"You need {abs(amount):.2f} lv. more to buy the series!")