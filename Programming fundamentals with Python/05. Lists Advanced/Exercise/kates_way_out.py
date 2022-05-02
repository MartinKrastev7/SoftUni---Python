def find_position(maze):
    position = []
    for row in range(len(maze)):
        for el in maze[row]:
            if el == 'k':
                position.append(row)
                position.append(maze[row].find('k'))
                return position


def next_free_spot(maze):
    free_spots = []

    for row in range(len(maze)):
        for el in range(len(maze[row])):
            tmp = []
            if maze[row][el] == ' ':
                tmp.append(row)
                tmp.append(el)
                free_spots.insert(0, tmp)

    return free_spots


def find_path(position, next_free, maze):
    is_blocked = True
    step = 0
    moves = 0

    while step < len(next_free):
        x1 = next_free[step][0]
        x2 = next_free[step][1]
        temp = []
        temp.append(x1)
        temp.append(x2)
        # moving left
        if temp[0] == position[0] and position[1] - temp[1] == 1:
            position = temp
            moves += 1
            next_free.pop(step)
            step = 0
        # moving right
        elif temp[0] == position[0] and temp[1] - position[1] == 1:
            position = temp
            moves += 1
            next_free.pop(step)
            step = 0
        # moving down
        elif temp[0] - position[0] == 1 and position[1] == temp[1]:
            position = temp
            moves += 1
            next_free.pop(step)
            step = 0
        # moving up
        elif position[0] - temp[0] == 1 and position[1] == temp[1]:
            position = temp
            moves += 1
            next_free.pop(step)
            step = 0


        else:

            step += 1

    if position[0] == 0 or position[0] == (len(maze) - 1) or position[1] == 0 or position[1] == len(maze[0]):
        return f'Kate got out in {moves + 1} moves'
    return f'Kate cannot get out'


m_rows = int(input())
maze = []
moves = 0
free_space = True
for row in range(m_rows):
    maze.append(input())
position = find_position(maze)
next_free = next_free_spot(maze)
movement = find_path(position, next_free, maze)
print(movement)

#vtori nachin
def all_false(x):
    for check in x:
        if check:
            return False
    return True


def char_replace(string, x, y):
    temp = list(string[x])
    temp[y] = "#"
    temp = "".join(temp)
    maze[x] = temp


def kate(x):
    for row in x:
        if "k" in row:
            return x.index(row), row.index("k")


def way_out_path(x):
    way_out_map = []
    for a, row in enumerate(x):
        for b, column in enumerate(row):
            if column == " ":
                way_out_map.append([a, b])
    return way_out_map


def way_out(x, y, way_out_map):
    move = 0
    while True:
        found_a_way = [[x, y + 1] in way_out_map, [x, y - 1] in way_out_map, [x + 1, y] in way_out_map,
                       [x - 1, y] in way_out_map]
        found_a_way_value = [[x, y + 1], [x, y - 1], [x + 1, y], [x - 1, y]]

        if x == maze_rows - 1 or y == len(maze[0]) - 1 or y == 0:
            return f"Kate got out in {move + 1} moves"

        if not all_false(found_a_way):
            x, y = found_a_way_value[found_a_way.index(True)]
            char_replace(maze, x, y)
            way_out_map.remove(found_a_way_value[found_a_way.index(True)])
            move += 1

        else:
            return "Kate cannot get out"


maze_rows = int(input())
maze = [input() for x in range(maze_rows)]
kate_row, kate_column = kate(maze)
map_to_freedom = way_out_path(maze)
print(way_out(kate_row, kate_column, map_to_freedom))