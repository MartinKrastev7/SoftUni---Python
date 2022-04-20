contract_time = input()
contract_type = input()
mobile_internet = input()
months = int(input())

tax = 0

if contract_time == "one":
    if contract_type == "Small":
        tax = 9.98
    elif contract_type == "Middle":
        tax = 18.99
    elif contract_type == "Large":
        tax = 25.98
    elif contract_type == "ExtraLarge":
        tax = 35.99
elif contract_time == "two":
    if contract_type == "Small":
        tax = 8.58
     #   tax = tax - (tax * 0.0375)
    elif contract_type == "Middle":
        tax = 17.09
     #   tax = tax - (tax * 0.0375)
    elif contract_type == "Large":
        tax = 23.59
      #  tax = tax - (tax * 0.0375)
    elif contract_type == "ExtraLarge":
        tax = 31.79
     #   tax = tax - (tax * 0.0375)

if mobile_internet == "yes":
    if tax <= 10.00:
        tax += 5.50
    elif tax <= 30.00:
        tax += 4.35
    else:
        tax += 3.85

if contract_time == "two":
    tax = tax - (tax * 0.0375)

total_tax = months * tax
print(f"{total_tax:.2f} lv.")