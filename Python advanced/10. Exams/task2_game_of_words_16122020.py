def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


initial_string = input()
size = int(input())
matrix = []
player_row = 0
player_col = 0

for row in range(size):
    elements = list(input())
    for col in range(size):
        if elements[col] == "P":
            player_row = row
            player_col = col

    matrix.append(elements)

matrix[player_row][player_col] = "-"

moves = {
    "left": (0, -1),  # left
    "up": (-1, 0),  # up
    "right": (0, 1),  # right
    "down": (1, 0)  # down
}

number = int(input())
current_row, current_col = player_row, player_col

for i in range(number):
    command = input()
    last_row, last_col = current_row, current_col

    if command == "up":
        current_row += moves[command][0]
        current_col += moves[command][1]
    elif command == "down":
        current_row += moves[command][0]
        current_col += moves[command][1]
    elif command == "left":
        current_row += moves[command][0]
        current_col += moves[command][1]
    elif command == "right":
        current_row += moves[command][0]
        current_col += moves[command][1]

    if is_inside(current_row, current_col, size):
        if matrix[current_row][current_col] != "-" and matrix[current_row][current_col] != "P":
            initial_string += matrix[current_row][current_col]
            matrix[current_row][current_col] = "-"
    else:
        current_row, current_col = last_row, last_col
        if len(initial_string) > 0:
            initial_string = initial_string[:-1]

matrix[current_row][current_col] = "P"

print(initial_string)
for row in matrix:
    print(''.join(row))
