joinery_number = int(input())
joinery_type = input()
type_delivery = input()
total_price = 0
price_90 = 110
price_100 = 140
price_130 = 190
price_200 = 250
condition = True

if joinery_number < 10:
    print("Invalid order")
else:
    if joinery_type == "90X130":
        if 30 < joinery_number <= 60:
            price_90 *= 0.95
            total_price = joinery_number * price_90
        elif joinery_number > 60:
            price_90 *= 0.92
            total_price = joinery_number * price_90
        else:
            condition = False
    elif joinery_type == "100X150":
        if 40 < joinery_number <= 80:
            price_100 *= 0.94
            total_price = joinery_number * price_100
        elif joinery_number > 80:
            price_100 *= 0.90
            total_price = joinery_number * price_100
        else:
            condition = False
    elif joinery_type == "130X180":
        if 20 < joinery_number <= 50:
            price_130 *= 0.93
            total_price = joinery_number * price_130
        elif joinery_number > 50:
            price_130 *= 0.88
            total_price = joinery_number * price_130
        else:
            condition = False
    elif joinery_type == "200X300":
        if 25 < joinery_number <= 50:
            price_200 *= 0.91
            total_price = joinery_number * price_200
        elif joinery_number > 50:
            price_200 *= 0.86
            total_price = joinery_number * price_200
        else:
            condition = False
#else:
 #   condition = False
    if type_delivery == "With delivery":
        total_price += 60
    else:
        total_price = total_price

    if joinery_number > 99:
        total_price *= 0.96

#if condition:
    print(f"{total_price:.2f} BGN")
#else:
 #   print("Invalid order")
