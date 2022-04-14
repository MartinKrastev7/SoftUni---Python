month = input()
number_of_nights = int(input())
studio = 0
apartment = 0

if month == "May" or month == "October":
    studio = 50
    apartment = 65
elif month == "June" or month == "September":
    studio = 75.20
    apartment = 68.70
elif month == "July" or month == "August":
    studio = 76
    apartment = 77

price_for_studio = studio * number_of_nights
price_for_apartment = apartment * number_of_nights

if 7 < number_of_nights < 14 and (month == "May" or month == "October"):
    price_for_studio *= 0.95
elif number_of_nights > 14 and month == "May" or month == "October":
    price_for_studio *= 0.70
elif number_of_nights > 14 and month == "June" or month == "September":
    price_for_studio *= 0.80
if number_of_nights > 14:
    price_for_apartment *= 0.90

print(f"Apartment: {price_for_apartment:.2f} lv.")
print(f"Studio: {price_for_studio:.2f} lv.")

