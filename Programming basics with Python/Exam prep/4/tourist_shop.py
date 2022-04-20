is_more_expensive = False
budget = float(input())
total_amount_bought_products = 0
product_count = 0
bill = 0
product_name = input()
while product_name != "Stop":
    product_price = float(input())
    product_count += 1
    if product_count % 3 == 0:
        product_price *= 0.5
    #budget -= product_price
    #total_amount_bought_products += product_price
    if budget < product_price:
        bill = product_price - budget
        is_more_expensive = True
        break
    budget -= product_price
    total_amount_bought_products += product_price

    product_name = input()

if is_more_expensive:
    print(f"You don't have enough money!")
    print(f"You need {bill:.2f} leva!")
else:
    print(f"You bought {product_count} products for {total_amount_bought_products:.2f} leva.")


######## vtori nachin
while True:
    product_name = input()
    product_count += 1
    if product_name == "Stop":
        break

    product_price = float(input())
    if product_count % 3 == 0:
        product_price *= 0.5
    if product_price > budget:
        is_more_expensive = True
        break

    total_amount_bought_products += product_price
    budget -= product_price

