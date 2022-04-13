import math

number_magnolia = int(input())
number_hyacinth = int(input())
number_roses = int(input())
number_cactus = int(input())
present_price = float(input())

magnolia_price = 3.25 * number_magnolia
hyacinth_price = 4 * number_hyacinth
roses_price = 3.50 * number_roses
cactus_price = 8 * number_cactus
total_price = magnolia_price + hyacinth_price + roses_price + cactus_price
total_price = total_price - (total_price * 0.05)
diff = abs(present_price - total_price)

if total_price >= present_price:
    diff = math.floor(diff)
    print(f"She is left with {diff} leva.")
else:
    diff = math.ceil(diff)
    print(f"She will have to borrow {diff} leva.")
