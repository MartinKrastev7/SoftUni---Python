fruit = input()
day_of_week = input()
quantity = float(input())
price = 0
condition = True

if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" or day_of_week == "Thursday" \
        or day_of_week == "Friday":
    if fruit == "banana":
        price = 2.50 * quantity
    elif fruit == "apple":
        price = 1.20 * quantity
    elif fruit == "orange":
        price = 0.85 * quantity
    elif fruit == "grapefruit":
        price = 1.45 * quantity
    elif fruit == "kiwi":
        price = 2.70 * quantity
    elif fruit == "pineapple":
        price = 5.50 * quantity
    elif fruit == "grapes":
        price = 3.85 * quantity
    else:
        condition = False
elif day_of_week == "Saturday" or day_of_week == "Sunday":
    if fruit == "banana":
        price = 2.70 * quantity
    elif fruit == "apple":
        price = 1.25 * quantity
    elif fruit == "orange":
        price = 0.90 * quantity
    elif fruit == "grapefruit":
        price = 1.60 * quantity
    elif fruit == "kiwi":
        price = 3.00 * quantity
    elif fruit == "pineapple":
        price = 5.60 * quantity
    elif fruit == "grapes":
        price = 4.20 * quantity
    else:
        condition = False
else:
    condition = False

if condition:
    print(f"{price:.2f}")
else:
    print("error")
