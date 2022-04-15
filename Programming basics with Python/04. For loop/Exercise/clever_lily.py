ages = int(input())
laundry_price = float(input())
toy_price = int(input())
total_money = 0
total_toys = 0
birthday_money = 0

for current_age in range(1, ages + 1):
    if current_age % 2 != 0:
        total_toys += 1
    else:
        birthday_money += 10
        total_money += birthday_money - 1

total_money += total_toys * toy_price
diff = abs(total_money - laundry_price)
if total_money >= laundry_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")




