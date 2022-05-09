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

#vtoro reshenie
targets = list(map(int, input().split(" ")))

line = input()
while line != "End":
    command_list = line.split(" ")
    command = command_list[0]
    index = int(command_list[1])
    value = int(command_list[2])

    if command == "Shoot" and index >= 0 and index < len(targets):
        current_target = targets[index]
        current_target -= value
        if current_target <= 0:
            targets.pop(index)
        else:
            targets[index] = current_target

    elif command == "Add":
        if index >= 0 and index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif command == "Strike":
        if index - value >= 0 and index + value < len(targets):
            targets = targets[0:index - value] + targets[index + value + 1:]
        else:
            print("Strike missed!")

    line = input()

targets = list(map(str, targets))
output = "|".join(targets)
print(output)