annual_tax = int(input())
sneakers_price = annual_tax - (annual_tax * 40 / 100)
dress_price = sneakers_price - (sneakers_price * 20 / 100)
ball_price = dress_price / 4
accessories_price = ball_price / 5
total_sum = annual_tax + sneakers_price + dress_price + ball_price + accessories_price

print(total_sum)