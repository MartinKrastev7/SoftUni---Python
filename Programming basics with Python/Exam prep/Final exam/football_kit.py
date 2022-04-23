tshirt_price = float(input())
amount_to_win_ball = float(input())

short_price = tshirt_price * 0.75
socks_price = short_price * 0.20
trainers_price = (tshirt_price + short_price) * 2
total_price = tshirt_price + short_price + socks_price + trainers_price
price_after_discount = total_price - (total_price * 0.15)
diff = amount_to_win_ball - price_after_discount

if price_after_discount >= amount_to_win_ball:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {price_after_discount:.2f} lv.")
else:
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {diff:.2f} lv. more.")

