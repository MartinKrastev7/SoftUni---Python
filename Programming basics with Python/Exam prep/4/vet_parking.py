number_days = int(input())
parking_tax = 0
total_amount = 0
hours_number = int(input())
parking_day_tax = 0
for day in range(1, number_days + 1):
    parking_day_tax = 0
    for hour in range(1, hours_number + 1):
        if day % 2 == 0 and hour % 2 != 0:
            parking_tax = 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            parking_tax = 1.25
        else:
            parking_tax = 1
        total_amount += parking_tax
        parking_day_tax += parking_tax
    print(f"Day: {day} - {parking_day_tax:.2f} leva")
print(f"Total: {total_amount:.2f} leva")

