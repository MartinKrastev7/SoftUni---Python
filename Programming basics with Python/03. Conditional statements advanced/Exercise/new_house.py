#type_flower = input()
#number_flowers = int(input())
#budget = int(input())
#roses_price = 5 * number_flowers
#dahlias_price = 3.80 * number_flowers
#tulips_price = 2.80 * number_flowers
#narcissus_price = 3 * number_flowers
#gladiolus_price = 2.50 * number_flowers
#needed_money = 0

#if type_flower == "Roses":
 #   if number_flowers > 80:
  #      roses_price = roses_price - (roses_price * 0.1)
   #     needed_money = abs(budget - roses_price)
    #elif number_flowers < 80:
     #   roses_price = roses_price
      #  needed_money = abs(budget - roses_price)
#elif type_flower == "Dahlias":
 #   if number_flowers > 90:
  #      dahlias_price = dahlias_price - (dahlias_price * 0.15)
   #     needed_money = abs(budget - dahlias_price)
   # elif number_flowers < 90:
   #     dahlias_price = dahlias_price
    #    needed_money = abs(budget - dahlias_price)
#elif type_flower == "Tulips":
 #   if number_flowers > 80:
  #      tulips_price = tulips_price - (tulips_price * 0.15)
   #     needed_money = abs(budget - tulips_price)
   # elif number_flowers < 80:
    #    tulips_price = tulips_price
     #   needed_money = abs(budget - tulips_price)
#elif type_flower == "Narcissus":
 #   if number_flowers < 120:
  #      narcissus_price = narcissus_price + (narcissus_price * 0.15)
   #     needed_money = abs(budget - narcissus_price)
   # elif number_flowers > 120:
    #    narcissus_price = narcissus_price
     #   needed_money = abs(budget - narcissus_price)
#elif type_flower == "Gladiolus":
 #   if number_flowers < 80:
  #      gladiolus_price = gladiolus_price + (gladiolus_price * 0.2)
   #     needed_money = abs(budget - gladiolus_price)
   # elif number_flowers > 80:
    #    gladiolus_price = gladiolus_price
     #   needed_money = abs(budget - gladiolus_price)

#print(narcissus_price)
#print(needed_money)

#if budget >= roses_price or budget >= dahlias_price or budget >= tulips_price or budget >= narcissus_price\
 #   or budget >= gladiolus_price:
 #   print(f"Hey, you have a great garden with {number_flowers} {type_flower} and {needed_money} leva left.")
#elif budget < roses_price or budget < dahlias_price or budget < tulips_price or budget < narcissus_price \
 #   or budget < gladiolus_price:
  #  print(f"Not enough money, you need {needed_money} leva more.")


################### vtoro reshenie upr

type_flower = input()
number_flowers = int(input())
budget = int(input())
needed_money = 0
price = 0

if type_flower == "Roses":
        price = 5 * number_flowers
        needed_money = abs(budget - price)
elif type_flower == "Dahlias":
        price = 3.8 * number_flowers
        needed_money = abs(budget - price)
elif type_flower == "Tulips":
        price = 2.8 * number_flowers
        needed_money = abs(budget - price)
elif type_flower == "Narcissus":
        price = 3 * number_flowers
        needed_money = abs(budget - price)
elif type_flower == "Gladiolus":
        price = 2.5 * number_flowers
        needed_money =abs(budget -price)


if type_flower == "Roses" and number_flowers > 80:
        price *= 0.9
        needed_money = abs(budget - price)
elif type_flower == "Dahlias" and number_flowers > 90:
        price *= 0.85
        needed_money = abs(budget - price)
elif type_flower == "Tulips" and number_flowers > 80:
        price *= 0.85
        needed_money = abs(budget - price)
elif type_flower == "Narcissus" and number_flowers < 120:
        price = price + (price * 0.15)
        needed_money = abs(budget - price)
elif type_flower == "Gladiolus" and number_flowers < 80:
        price = price + (price * 0.2)
        needed_money = abs(budget - price)

if budget >= price:
        print(f"Hey, you have a great garden with {number_flowers} {type_flower} and {needed_money:.2f} leva left.")
else:
        print(f"Not enough money, you need {needed_money:.2f} leva more.")