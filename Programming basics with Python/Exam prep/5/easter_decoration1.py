clients_number = int(input())
count = 0
total_amount = 0
current_amount = 0

for buy in range(1, clients_number + 1):
    current_amount = 0
    count = 0
    while True:
        command = input()
        if command == "Finish":
            break

        count += 1
        if command == "basket":
            current_amount += 1.50
        elif command == "wreath":
            current_amount += 3.80
        elif command == "chocolate bunny":
            current_amount += 7

    if count % 2 == 0:
        current_amount *= 0.80
    total_amount += current_amount
    print(f"You purchased {count} items for {current_amount:.2f} leva.")

average = total_amount / clients_number

print(f"Average bill per client is: {average:.2f} leva.")


