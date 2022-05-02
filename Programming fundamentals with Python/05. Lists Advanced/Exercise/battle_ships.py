rows_count = int(input())
coord_list = []

while rows_count > 0:
    coord_list.append(list(map(int, input().split())))
    rows_count -= 1

# the location description - row/column

attacks_list = input().split()
ships_destroyed = 0

for element in attacks_list:
    coord1, coord2 = element.split('-')
    coord1 = int(coord1)
    coord2 = int(coord2)
    if coord_list[coord1][coord2] > 0:
        coord_list[coord1][coord2] -= 1
        if coord_list[coord1][coord2] == 0:
            ships_destroyed += 1

print(ships_destroyed)