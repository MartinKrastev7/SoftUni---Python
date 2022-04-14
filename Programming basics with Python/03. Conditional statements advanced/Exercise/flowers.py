chrysan_number = int(input())
rose_number = int(input())
tulip_number = int(input())
season = input()
holiday = input()
total_amount = 0
chrysan_price = 0
rose_price = 0
tulip_price = 0
if season == "Spring" or season == "Summer":
    chrysan_price = 2 * chrysan_number
    rose_price = 4.10 * rose_number
    tulip_price = 2.50 * tulip_number
elif season == "Autumn" or season == "Winter":
    chrysan_price = 3.75 * chrysan_number
    rose_price = 4.50 * rose_number
    tulip_price = 4.15 * tulip_number
total_amount = chrysan_price + rose_price + tulip_price
flowers_number = tulip_number + rose_number + chrysan_number
if holiday == "Y":
    total_amount = total_amount + (total_amount * 0.15)

if tulip_number > 7 and season == "Spring":
    total_amount = total_amount - (total_amount * 0.05)
elif rose_number >= 10 and season == "Winter":
    total_amount = total_amount - (total_amount * 0.10)

if flowers_number > 20:
    total_amount = total_amount - (total_amount * 0.20)
total_amount += 2

print(f"{total_amount:.2f}")


