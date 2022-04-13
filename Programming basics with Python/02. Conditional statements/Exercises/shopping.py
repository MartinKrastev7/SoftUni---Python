budget = float(input())
video_card_number = int(input())
cpu_number = int(input())
ram_number = int(input())

video_card_price = video_card_number * 250
cpu_price = (video_card_price * 0.35) * cpu_number
ram_price = (video_card_price * 0.10) * ram_number
total_price = video_card_price + cpu_price + ram_price

if video_card_number > cpu_number:
    total_price = total_price - (total_price * 0.15)

needed_amount = abs(budget - total_price)

if budget >= total_price:
    print(f"You have {needed_amount:.2f} leva left!")
elif budget < total_price:
    print(f"Not enough money! You need {needed_amount:.2f} leva more!")
