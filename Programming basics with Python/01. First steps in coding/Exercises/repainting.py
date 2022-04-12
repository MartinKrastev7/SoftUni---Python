necessary_quantity_nylon_square_metres = int(input())
necessary_quantity_painting_litres = int(input())
quantity_diluent_litres = int(input())
hours_for_work = int(input())

price_nylon = (necessary_quantity_nylon_square_metres + 2) * 1.50
price_painting = (necessary_quantity_painting_litres +(necessary_quantity_painting_litres * 10 / 100)) * 14.50
price_diluent = quantity_diluent_litres * 5.00
price_bags = 0.40
total_price_materials = price_nylon + price_painting + price_diluent + price_bags
total_price_workers = (total_price_materials * 30 / 100) * hours_for_work
total_price = total_price_workers + total_price_materials

print(total_price)