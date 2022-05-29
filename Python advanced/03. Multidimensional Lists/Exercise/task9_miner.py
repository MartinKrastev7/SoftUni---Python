def in_maze(r, c, n):
    return 0 <= r < n and 0 <= c < n


def replace_positions(st_position, next_position):
    maze[next_position[0]][next_position[1]] = "s"
    maze[st_position[0]][st_position[1]] = "*"


n = int(input())
commands = [word for word in input().split()]

move = {"up": (-1, 0), "right": (0, 1), "down": (1, 0), "left": (0, -1)}

maze = []
all_coals = 0
coals_count = 0
pole = None

for r in range(n):
    row = input().split()
    maze.append(row)
    all_coals += row.count("c")
    if "s" in row:
        start_position = (r, row.index("s"))

position = start_position

for direction in commands:
    position = (start_position[0] + move[direction][0], start_position[1] + move[direction][1])
    if not in_maze(*position, n):
        position = start_position
        continue

    pole = maze[position[0]][position[1]]
    if pole == "e":
        break
    elif pole == "c":
        coals_count += 1
        replace_positions(start_position, position)
        start_position = position

    elif pole == "*":
        replace_positions(start_position, position)
        start_position = position


if pole == "e":
    print(f"Game over! {position}")
elif all_coals == coals_count:
    print(f"You collected all coal! {position}")
else:
    print(f"{all_coals - coals_count} pieces of coal left. {position}")
