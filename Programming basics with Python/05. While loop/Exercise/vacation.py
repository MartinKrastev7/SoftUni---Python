money_vacation = float(input())
available_money = float(input())
days_counter = 0
spending_counter = 0


while available_money < money_vacation and spending_counter < 5:

    kind_action = input()
    amount = float(input())
    days_counter += 1

    if kind_action == "save":
        available_money += amount
        spending_counter = 0
    elif kind_action == "spend":
        available_money -= amount
        spending_counter += 1
        if available_money < 0:
            available_money = 0

if spending_counter == 5:
    print("You can't save the money.")
    print(days_counter)

if available_money >= money_vacation:
    print(f"You saved the money for {days_counter} days.")
