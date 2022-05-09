targets = list(map(int, input().split(" ")))
command = input()
count_shot = 0
indexes_shot = []

while command != "End":
    current_index = int(command)
    if current_index in range(len(targets)):
        targets = [x - targets[current_index] if x > targets[current_index] else x + targets[current_index]
                   for x in targets]

        count_shot += 1
        indexes_shot.append(current_index)

        targets[current_index] = -1

    command = input()

for x in indexes_shot:
    targets[x] = -1

list_targets = [str(x) for x in targets]

print(f"Shot targets: {count_shot} -> {' '.join(list_targets)}")

#vtori nachin
targets = list(map(int, input().split()))
shot_targets = 0

while True:
    command = input()
    if command == 'End':
        print(f"Shot targets: {shot_targets} -> {' '.join(map(str, targets))}")
        break

    index = int(command)
    if index in range(len(targets)):
        current_number = targets[index]
        for i in range(len(targets)):
            if targets[i] != -1:
                if targets[i] > current_number:
                    targets[i] -= current_number
                else:
                    targets[i] += current_number
        targets[index] = -1
        shot_targets += 1