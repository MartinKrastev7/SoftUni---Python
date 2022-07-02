def valid_moves(row, col, size):
    if 0 <= row < size and 0 <= col < size:
        return True
    return False


size = 8
matrix = []

for row in range(size):
    matrix.append(input().split(" "))

queen_moves = [
    (0, -1),  # left
    (-1, -1),  # up left diagonal
    (-1, 0),  # up
    (-1, 1),  # up right diagonal
    (0, 1),  # right
    (1, 1),  # down right diagonal
    (1, 0),  # down
    (1, -1)  # down left diagonal
]

queens_position = []

for row in range(size):
    for col in range(size):
        king_found = False

        if matrix[row][col] == "Q":
            for move in queen_moves:
                current_row, current_col = row, col
                current_row += move[0]
                current_col += move[1]

                while valid_moves(current_row, current_col, size):
                    if matrix[current_row][current_col] == "K":
                        queens_position.append([row, col])
                        king_found = True
                        break
                    elif matrix[current_row][current_col] == "Q":
                        break

                    current_row += move[0]
                    current_col += move[1]

                if king_found:
                    break

if not queens_position:
    print("The king is safe!")
else:
    for line in queens_position:
        print(line)