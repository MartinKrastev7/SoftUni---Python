initial_eggs = int(input())
eggs_sold = 0
total_sold = 0
command = input()
is_over = False

while command != "Close":
    action = int(input())
    if command == "Buy" and action > initial_eggs:
        is_over = True
        break
    if command == "Buy":
        initial_eggs -= action
        total_sold += action
    elif command == "Fill":
        initial_eggs += action

    command = input()

if is_over:
    print("Not enough eggs in store!")
    print(f"You can buy only {initial_eggs}.")
else:
    print("Store is closed!")
    print(f"{total_sold} eggs sold.")