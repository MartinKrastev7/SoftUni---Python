def get_next_pos(row, col, command):
    if command == "up":
        return row - 1, col
    elif command == "down":
        return row + 1, col
    elif command == "left":
        return row, col - 1
    elif command == "right":
        return row, col + 1


def is_outside(row, col, rows, cols):
    return row < 0 or col < 0 or row == rows or col == cols


size = int(input())
matrix = []

player_row = 0
player_col = 0
burrow = []

for row in range(size):
    elements = list(input())
    for col in range(size):
        if elements[col] == "S":
            player_row = row
            player_col = col
        elif elements[col] == "B":
            burrow.append([row, col])

    matrix.append(elements)


food = 0
dead = False
is_enough_food = False

while food <= 10:
    command = input()
    next_row, next_col = get_next_pos(player_row, player_col, command)
    matrix[player_row][player_col] = "."
    player_row, player_col = next_row, next_col

    if is_outside(next_row, next_col, size, size):
        dead = True
        break
    elif matrix[next_row][next_col] == "B":
        matrix[next_row][next_col] = "."
        player_row, player_col = burrow[1][0], burrow[1][1]

    elif matrix[next_row][next_col] == "*":
        food += 1
        if food >= 10:
            matrix[next_row][next_col] = "S"
            is_enough_food = True
            break

    matrix[player_row][player_col] = "."


if dead:
    print("Game over!")
if is_enough_food:
    print("You won! You fed the snake.")

print(f"Food eaten: {food}")

for row in matrix:
    print("".join(row))