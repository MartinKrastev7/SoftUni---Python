football_team = input()
number_played = int(input())
w_count = 0
d_count = 0
l_count = 0
w_points = 0
d_points = 0
l_points = 0
w_percent = 0
total_points = 0

for play in range(1, number_played + 1):
    result = input()
    if result == "W":
        w_count += 1
        w_points = 3 * w_count

    elif result == "D":
        d_count += 1
        d_points = 1 * d_count
    elif result == "L":
        l_count += 1
        l_points = 0
    w_percent = w_count * 100 / number_played
    total_points = w_points + d_points + l_points

if number_played == 0:
    print(f"{football_team} hasn't played any games during this season.")
else:
    print(f"{football_team} has won {total_points} points during this season.")
    print("Total stats:")
    print(f"## W: {w_count}")
    print(f"## D: {d_count}")
    print(f"## L: {l_count}")
    print(f"Win rate: {w_percent:.2f}%")

