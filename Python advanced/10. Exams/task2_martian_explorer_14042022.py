def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


size = 6
matrix = []
player_row = 0
player_col = 0

for row in range(size):
    elements = input().split(" ")
    for col in range(size):
        if elements[col] == "E":
            player_row = row
            player_col = elements.index("E")
    matrix.append(elements)

found_elements = {
    "Water deposit": 0,
    "Metal deposit": 0,
    "Concrete deposit": 0
}

moves = {
    "left": (0, -1),  # left
    "up": (-1, 0),  # up
    "right": (0, 1),  # right
    "down": (1, 0)  # down
}

commands = input().split(", ")
current_row, current_col = player_row, player_col
is_broken = False

for i in range(len(commands)):
    current_command = commands[i]

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

    if is_inside(current_row, current_col, size):
        if matrix[current_row][current_col] == "W":
            found_elements["Water deposit"] += 1
            print(f"Water deposit found at ({current_row}, {current_col})")
        elif matrix[current_row][current_col] == "M":
            found_elements["Metal deposit"] += 1
            print(f"Metal deposit found at ({current_row}, {current_col})")
        elif matrix[current_row][current_col] == "C":
            found_elements["Concrete deposit"] += 1
            print(f"Concrete deposit found at ({current_row}, {current_col})")
        elif matrix[current_row][current_col] == "R":
            is_broken = True
            print(f"Rover got broken at ({current_row}, {current_col})")
            break
    else:
        if current_command == "up":
            current_row += size
        elif current_command == "down":
            current_row -= size
        elif current_command == "left":
            current_col += size
        elif current_command == "right":
            current_col -= size

        if matrix[current_row][current_col] == "W":
            found_elements["Water deposit"] += 1
            print(f"Water deposit found at ({current_row}, {current_col})")
        elif matrix[current_row][current_col] == "M":
            found_elements["Metal deposit"] += 1
            print(f"Metal deposit found at ({current_row}, {current_col})")
        elif matrix[current_row][current_col] == "C":
            found_elements["Concrete deposit"] += 1
            print(f"Concrete deposit found at ({current_row}, {current_col})")
        elif matrix[current_row][current_col] == "R":
            is_broken = True
            print(f"Rover got broken at ({current_row}, {current_col})")
            break

    if is_broken:
        break

if found_elements["Water deposit"] >= 1 and found_elements["Metal deposit"] >= 1 \
    and found_elements["Concrete deposit"] >= 1:
    print(f"Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
