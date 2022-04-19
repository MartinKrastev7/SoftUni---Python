actor_name = input()
points_academy = float(input())
number_raters = int(input())
total_points = 0
is_reached = False

for rate in range(1, number_raters + 1):
    rater_name = input()
    points_from_rater = float(input())
    total_points = (len(rater_name) * points_from_rater) / 2
    points_academy += total_points
    if points_academy > 1250.5:
        is_reached = True
        break

diff = abs(1250.5 - points_academy)
if is_reached:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {points_academy:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")