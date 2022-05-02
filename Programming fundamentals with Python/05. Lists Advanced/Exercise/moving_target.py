targets = [int(x) for x in input().split(" ")]
command = input()

while command != "End":
    commands_target = command.split(" ")
    action = commands_target[0]
    targets_len = [str(i) for i in targets]
    if len(commands_target) > 1:
        index_place = int(commands_target[1])
        move = int(commands_target[2])
    if action == "Shoot":
      #  targets_len = [str(i) for i in targets]
        if index_place in range(len(targets_len)):
            targets[index_place] -= move
            if targets[index_place] <= 0:
                targets.pop(index_place)

    elif action == "Add":
        if index_place in range(len(targets_len)):
           # targets[index_place] = targets[move]
            targets.insert(index_place, move)
        else:
            print("Invalid placement!")

    elif action == "Strike":
     #   if index_place - move <= len(targets_len) and index_place + move <= len(targets_len):
           # targets.pop(index_place - move,index_place + move,index_place)
           first_index = index_place - move
           second_index = index_place + move
           if first_index in range(len(targets_len)) and second_index in range(len(targets_len)):
               del targets[first_index:second_index + 1]
           else:
               print("Strike missed!")
          #  targets.pop(index_place + move)
          #  targets.pop(index_place)
    command = input()

targets = [str(x) for x in targets]
print("|".join(targets))