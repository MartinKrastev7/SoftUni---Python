budget = float(input())
price_1kg_flour = float(input())

price_1pack_eggs = price_1kg_flour * 0.75
price_1l_milk = price_1kg_flour + (price_1kg_flour * 0.25)
price_250ml_milk = price_1l_milk / 4
amount_for_one_bread = price_1kg_flour + price_1pack_eggs + price_250ml_milk

color_eggs_count = 0
bread_count = 0

while budget >= amount_for_one_bread:
    bread_count += 1
    color_eggs_count += 3

    if bread_count % 3 == 0:
        color_eggs_count -= (bread_count - 2)



    budget -= amount_for_one_bread

print(f"You made {bread_count} loaves of Easter bread! Now you have {color_eggs_count} eggs and {budget:.2f}BGN left.")