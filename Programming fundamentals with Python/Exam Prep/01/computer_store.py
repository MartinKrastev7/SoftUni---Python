price_without_tax = input()
sum_amount = 0
taxes = 0
final_amount = 0
is_finished = False

while True:
    if price_without_tax == "special" or price_without_tax == "regular":
            is_finished = True
            break

    price_without_tax = float(price_without_tax)
    if price_without_tax < 0:
        print("Invalid price!")
        price_without_tax = input()
        continue

    sum_amount += price_without_tax
    price_without_tax = input()

taxes = 0.2 * sum_amount
final_amount = sum_amount + taxes


if is_finished:
    if price_without_tax == "special":
        final_amount *= 0.90
    if final_amount == 0:
        print("Invalid order!")
    else:
        print("Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {sum_amount:.2f}$")
        print(f"Taxes: {taxes:.2f}$")
        print("-----------")
        print(f"Total price: {final_amount:.2f}$")


#vtoro reshenie
line = input()
net_price = 0



while line != "special" and line != "regular":
    current_price = float(line)

    if current_price > 0:
        net_price += current_price
    else:
        print("Invalid price!")


    line = input()

if net_price <= 0:
    print("Invalid order!")
else:
    taxes = net_price * 0.2
    final_price = net_price + taxes
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {net_price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")

    if line == "special":
        final_price *= 0.90

    print(f"Total price: {final_price:.2f}$")