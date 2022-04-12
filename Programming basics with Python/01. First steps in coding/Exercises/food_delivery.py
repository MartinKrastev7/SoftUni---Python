number_chicken_menu = int(input())
number_fish_menu = int(input())
number_vegan_menu = int(input())

price_chicken_menu = number_chicken_menu * 10.35
price_fish_menu = number_fish_menu * 12.40
price_vegan_menu = number_vegan_menu * 8.15
price_delivery = 2.50
total_price_menu = price_chicken_menu + price_fish_menu + price_vegan_menu
price_dessert = total_price_menu * 20 / 100
total_price_order = total_price_menu + price_dessert + price_delivery

print(float(total_price_order))
