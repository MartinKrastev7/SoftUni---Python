days = int(input())
room_type = input()
rating = input()
accommodation_price = 0
room_for_one_person = 18
apartment = 25
president_apartment = 35
nights = days - 1

if room_type == "apartment":
    if nights < 10:
        accommodation_price = nights * apartment
        accommodation_price *= 0.70
    elif 10 < nights < 15:
        accommodation_price = nights * apartment
        accommodation_price *= 0.65
    elif nights > 15:
        accommodation_price = nights * apartment
        accommodation_price *= 0.50
elif room_type == "president apartment":
    if nights < 10:
        accommodation_price = nights * president_apartment
        accommodation_price *= 0.90
    elif 10 < nights < 15:
        accommodation_price = nights * president_apartment
        accommodation_price *= 0.85
    elif nights > 15:
        accommodation_price = nights * president_apartment
        accommodation_price *= 0.80
else:
    accommodation_price = nights * room_for_one_person

if rating == "positive":
    accommodation_price = accommodation_price + (accommodation_price * 0.25)
elif rating == "negative":
    accommodation_price = accommodation_price - (accommodation_price * 0.10)



print(f"{accommodation_price:.2f}")

