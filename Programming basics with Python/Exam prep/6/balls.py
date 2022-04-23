import math

balls_number = int(input())
total_points = 0
points_red = 0
points_orange = 0
points_yellow = 0
points_white = 0
points_others = 0
count_black = 0

for text in range(balls_number):
    color = input()

    if color == "red":
        points_red += 1
        total_points += 5
    elif color == "orange":
        points_orange += 1
        total_points += 10
    elif color == "yellow":
        points_yellow += 1
        total_points += 15
    elif color == "white":
        points_white += 1
        total_points += 20
    elif color == "black":
        count_black += 1
        total_points = math.floor(total_points / 2)
    else:
        points_others += 1
        total_points = total_points
print(f"Total points: {total_points}")
print(f"Points from red balls: {points_red}")
print(f"Points from orange balls: {points_orange}")
print(f"Points from yellow balls: {points_yellow}")
print(f"Points from white balls: {points_white}")
print(f"Other colors picked: {points_others}")
print(f"Divides from black balls: {count_black}")








