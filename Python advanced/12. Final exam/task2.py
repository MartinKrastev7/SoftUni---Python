players_names = input().split(", ")
player_one = players_names[0]
player_two = players_names[1]
size = 6
matrix = []

for _ in range(size):
    matrix.append([x for x in input().split(" ")])

winner = ""
count_throw = 0
is_out = False
is_trap = False
is_hit_player_one = False
is_hit_player_two = False

while True:
    player_coordinates = input().split(", ")
    (player_shot_row, player_shot_col) = player_coordinates
    player_shot_row = int(player_shot_row.replace('(', ''))
    player_shot_col = int(player_shot_col.replace(')', ''))

 #   if is_hit:
  #      count_throw += 1
   #     is_hit = False

    player_name = ""
    other_player_name = ""
    if count_throw % 2 == 0:
        if is_hit_player_one:
            is_hit_player_one = False
            count_throw += 1
            continue
        player_name = player_one
        other_player_name = player_two
    else:
        if is_hit_player_two:
            is_hit_player_two = False
            count_throw += 1
            continue
        player_name = player_two
        other_player_name = player_one

    #if is_hit:
    #    count_throw += 1
   #     is_hit = False

    if matrix[player_shot_row][player_shot_col] == "E":
        is_out = True
        print(f"{player_name} found the Exit and wins the game!")
        break
    elif matrix[player_shot_row][player_shot_col] == "T":
        is_trap = True
        print(f"{player_name} is out of the game! The winner is {other_player_name}.")
        break
    elif matrix[player_shot_row][player_shot_col] == "W":
        print(f"{player_name} hits a wall and needs to rest.")
        if count_throw % 2 == 0:
            is_hit_player_one = True
        else:
            is_hit_player_two = True

    count_throw += 1
    #if is_hit:
     #   count_throw += 1
      #  is_hit = False
