def is_inside(row, col, row_size, col_size):
    return 0 <= row < row_size and 0 <= col < col_size


rows_columns = input().split(", ")
row = int(rows_columns[0])
col = int(rows_columns[1])

matrix = []
christmas_decoration_count = 0
gifts_count = 0
cookies_count = 0
player_row = 0
player_col = 0

for r in range(row):
    elements = input().split(" ")
    for c in range(col):
        if elements[c] == "Y":
            player_row = r
            player_col = elements.index("Y")
    if "D" in elements:
        christmas_decoration_count += elements.count("D")
    if "G" in elements:
        gifts_count += elements.count("G")
    if "C" in elements:
        cookies_count += elements.count("C")
    matrix.append(elements)

collected_items_dict = {
    "Christmas decorations": 0,
    "Gifts": 0,
    "Cookies": 0
}

moves = {
    "left": (0, -1),  # left
    "up": (-1, 0),  # up
    "right": (0, 1),  # right
    "down": (1, 0)  # down
}

is_collected = False
current_row, current_col = player_row, player_col
command = input()

while command != "End":
    command = command.split("-")
    current_command = command[0]
    steps = int(command[1])

    for move in range(steps):
        last_row, last_col = current_row, current_col
        if current_command == "up":
            current_row += moves[current_command][0]
            current_col += moves[current_command][1]
        elif current_command == "down":
            current_row += moves[current_command][0]
            current_col += moves[current_command][1]
        elif current_command == "left":
            current_row += moves[current_command][0]
            current_col += moves[current_command][1]
        elif current_command == "right":
            current_row += moves[current_command][0]
            current_col += moves[current_command][1]

        if is_inside(current_row, current_col, row, col):
            if matrix[current_row][current_col] == "D":
                christmas_decoration_count -= 1
                collected_items_dict["Christmas decorations"] += 1
            elif matrix[current_row][current_col] == "G":
                gifts_count -= 1
                collected_items_dict["Gifts"] += 1
            elif matrix[current_row][current_col] == "C":
                cookies_count -= 1
                collected_items_dict["Cookies"] += 1

        else:
            if current_command == "up":
                current_row += row
            elif current_command == "down":
                current_row -= row
            elif current_command == "left":
                current_col += col
            elif current_command == "right":
                current_col -= col

            if matrix[current_row][current_col] == "D":
                christmas_decoration_count -= 1
                collected_items_dict["Christmas decorations"] += 1
            elif matrix[current_row][current_col] == "G":
                gifts_count -= 1
                collected_items_dict["Gifts"] += 1
            elif matrix[current_row][current_col] == "C":
                cookies_count -= 1
                collected_items_dict["Cookies"] += 1

        matrix[last_row][last_col] = "x"
        matrix[current_row][current_col] = "Y"

        if christmas_decoration_count == 0 and gifts_count == 0 and cookies_count == 0:
            is_collected = True
            break
    if is_collected:
        break
    command = input()

if is_collected:
    print("Merry Christmas!")
print("You've collected:")
for key, value in collected_items_dict.items():
    print(f"- {value} {key}")

for row in matrix:
    print(*row, sep=" ")