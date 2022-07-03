def check_if_shot_is_valid(field, player_row, player_col):
    if (player_row < 0 or player_col < 0) or (player_row >= len(field) or player_col >= len(field)):
        return None
    return field[player_row][player_col]


size = 6
matrix = []

for _ in range(size):
    matrix.append([x for x in input().split(" ")])

scored_points = 0
throw_count = 0
while True:
    throw_count += 1
    player_coordinates = input().split(", ")
    (player_shot_row, player_shot_col) = player_coordinates
    player_shot_row = int(player_shot_row.replace('(', ''))
    player_shot_col = int(player_shot_col.replace(')', ''))
    target_hit = check_if_shot_is_valid(matrix, player_shot_row, player_shot_col)

    if target_hit is not None:
        if matrix[player_shot_row][player_shot_col] == "B":

            for row in range(size):
                if matrix[row][player_shot_col] != "B":
                    scored_points += int(matrix[row][player_shot_col])

            matrix[player_shot_row][player_shot_col] = "-"

    if throw_count == 3:
        break

if scored_points < 100:
    diff = 100 - scored_points
    print(f"Sorry! You need {diff} points more to win a prize.")
elif 100 <= scored_points <= 199:
    print(f"Good job! You scored {scored_points} points, and you've won Football.")
elif 200 <= scored_points <= 299:
    print(f"Good job! You scored {scored_points} points, and you've won Teddy Bear.")
elif 300 <= scored_points:
    print(f"Good job! You scored {scored_points} points, and you've won Lego Construction Set.")