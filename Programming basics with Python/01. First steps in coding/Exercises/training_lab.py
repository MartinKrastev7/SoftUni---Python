w = float(input())
h = float(input())

w_in_cm = w * 100
h_in_cm = h * 100
corridor_space = h_in_cm - 100
number_in_h = corridor_space // 70
number_in_w = w_in_cm // 120

number_total = (number_in_w * number_in_h) - 3
print(number_total)

