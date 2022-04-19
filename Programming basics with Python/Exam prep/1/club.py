income_target = float(input())
is_target = False
coctail_name = input()
price = 0
total_income = 0
while coctail_name != "Party!":
    number_coctails = int(input())
    price = int(len(coctail_name)) * number_coctails
    if price % 2 != 0:
        price *= 0.75

    total_income += price
    if total_income >= income_target:
        is_target = True
        break

    coctail_name = input()

diff = abs(income_target - total_income)
if is_target:
    print("Target acquired.")
else:
    print(f"We need {diff:.2f} leva more.")
print(f"Club income - {total_income:.2f} leva.")