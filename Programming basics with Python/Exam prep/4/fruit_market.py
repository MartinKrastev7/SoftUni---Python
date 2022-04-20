price_strawberry = float(input())
bananas_quantity = float(input())
oranges_quantity = float(input())
raspberry_quantity = float(input())
strawberry_quantity = float(input())

price_raspberry = price_strawberry / 2
price_oranges = price_raspberry - (price_raspberry * 0.4)
price_bananas = price_raspberry - (price_raspberry * 0.8)

total_sum_strawberry = price_strawberry * strawberry_quantity
total_sum_raspberry = price_raspberry * raspberry_quantity
total_sum_oranges = price_oranges * oranges_quantity
total_sum_bananas = price_bananas * bananas_quantity

total_all = total_sum_strawberry + total_sum_raspberry + total_sum_oranges + total_sum_bananas

print(f"{total_all:.2f}")