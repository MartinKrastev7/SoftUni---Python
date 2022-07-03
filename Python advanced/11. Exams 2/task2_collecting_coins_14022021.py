from math import floor


def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


size = int(input())
matrix = []
player_row = 0
player_col = 0

for row in range(size):
    elements = input().split(" ")
    for col in range(size):
        if elements[col] == "P":
            player_row = row
            player_col = col
    matrix.append(elements)

coordinates = []
matrix[player_row][player_col] = 0
current_row, current_col = player_row, player_col
coins = 0

moves = {
    "left": (0, -1),  # left
    "up": (-1, 0),  # up
    "right": (0, 1),  # right
    "down": (1, 0)  # down
}

is_win = False
coordinates.append([current_row, current_col])

while True:
    command = input()
    if command not in moves:
        continue

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
        if matrix[current_row][current_col] != "X":
            coins += int(matrix[current_row][current_col])
            coordinates.append([current_row, current_col])
            matrix[current_row][current_col] = 0

        elif matrix[current_row][current_col] == "X":
            coins = floor(coins / 2)
            coordinates.append([current_row, current_col])
            break

    else:
        if command == "up":
            current_row += size
        elif command == "down":
            current_row -= size
        elif command == "left":
            current_col += size
        elif command == "right":
            current_col -= size
        if matrix[current_row][current_col] != "X":
            coins += int(matrix[current_row][current_col])
            coordinates.append([current_row, current_col])
            matrix[current_row][current_col] = 0

        elif matrix[current_row][current_col] == "X":
            coins = floor(coins / 2)
            coordinates.append([current_row, current_col])
            break

    if coins >= 100:
        is_win = True
        break


if is_win:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {coins} coins.")

print("Your path:")
print(*coordinates, sep='\n')




