#number_of_pens = int(input())
#number_of_markers = int(input())
#liters_of_detergent = int(input())
#percent_discount = int(input())

#price_per_pen = 5.80
#price_per_markers = 7.20
#price_per_liter_detergent = 1.20
#needed_sum = number_of_pens * price_per_pen + number_of_markers * price_per_markers + \
 #            liters_of_detergent * price_per_liter_detergent
#percent_discount = percent_discount / 100 # percent_discount / = 100
#needed_sum = needed_sum - (needed_sum * percent_discount)

#print(needed_sum)

########### kod sus 100 tochki
pens = int(input())
markers = int(input())
liters = int(input())
percent = int(input())

price_pens = pens * 5.80
price_markers = markers * 7.20
price_prep = liters * 1.20
total_price = price_prep + price_markers + price_pens
final_price = total_price - total_price * (percent / 100)
print(final_price)