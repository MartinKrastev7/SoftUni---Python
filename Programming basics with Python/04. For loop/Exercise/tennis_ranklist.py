import math

number_tournaments = int(input())
initial_points = int(input())
total_points = 0
points1 = 0
points2 = 0
points3 = 0
average_points = 0
percent_wins = 0
wins = 0
W = 2000
F = 1200
SF = 720

for text in range(number_tournaments):
    tournaments_stage = input()

    if tournaments_stage == "W":
        points1 += W
        wins += 1
    elif tournaments_stage == "F":
        points2 += F
    elif tournaments_stage == "SF":
        points3 += SF

total_points = points1 + points2 + points3 + initial_points
average_points = (points1 + points2 + points3) / number_tournaments
average_points = math.floor(average_points)
percent_wins = (wins / number_tournaments) * 100
print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f"{percent_wins:.2f}%")