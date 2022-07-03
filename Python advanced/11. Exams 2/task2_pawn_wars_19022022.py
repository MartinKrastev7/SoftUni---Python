size = 8
matrix = []
player_one_row = 0
player_one_col = 0
player_two_row = 0
player_two_col = 0

for row in range(size):
    elements = input().split(" ")
    for col in range(size):
        if "w" in elements:
            player_one_row = row
            player_one_col = elements.index("w")
        if "b" in elements:
            player_two_row = row
            player_two_col = elements.index("b")
    matrix.append(elements)

rows_ranks = [8, 7, 6, 5, 4, 3, 2, 1]
cols_ranks = ["a", "b", "c", "d", "e", "f", "g", "h"]

count_turn = 0
winner = ""
winner_row_rank = ""
winner_col_rank = ""
is_caught = False
is_queen = False

while True:
    if 0 <= player_one_row - 1 < size and 0<= player_one_col + 1 < size and matrix[player_one_row - 1][player_one_col + 1] == "b":
        print(f'Game over! White win, capture on {cols_ranks[player_one_col + 1]}{rows_ranks[player_one_row - 1]}.')
        break
    if 0 <= player_one_row - 1 < size and 0 <= player_one_col - 1 < size and matrix[player_one_row - 1][player_one_col - 1] == "b":
        print(f'Game over! White win, capture on {cols_ranks[player_one_col - 1]}{rows_ranks[player_one_row- 1]}.')
        break

    matrix[player_one_row][player_one_col] = "-"
    player_one_row -= 1
    matrix[player_one_row][player_one_col] = "w"

    if player_one_row == 0:
        print(f'Game over! White pawn is promoted to a queen at {cols_ranks[player_one_col]}{rows_ranks[player_one_row]}.')
        break

    if 0 <= player_two_row + 1 < size and 0 <= player_two_col + 1 < size and matrix[player_two_row + 1][player_two_col + 1] == "w":
        print(f'Game over! Black win, capture on {cols_ranks[player_two_col + 1]}{rows_ranks[player_two_row + 1]}.')
        break
    if 0 <= player_two_row + 1 < size and 0 <= player_two_col - 1 < size and matrix[player_two_row + 1][player_two_col - 1] == "w":
        print(f'Game over! Black win, capture on {cols_ranks[player_two_col - 1]}{rows_ranks[player_two_row + 1]}.')
        break

    matrix[player_two_row][player_two_col] = "-"
    player_two_row += 1
    matrix[player_two_row][player_two_col] = "b"

    if player_two_row == 7:
        print(f'Game over! Black pawn is promoted to a queen at {cols_ranks[player_two_col]}{rows_ranks[player_two_row]}.')
        break
