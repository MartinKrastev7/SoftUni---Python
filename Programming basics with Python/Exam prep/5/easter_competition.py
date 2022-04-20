import sys

number_kozunakis = int(input())
points_count = 0
baker_max = ""
max_points = -sys.maxsize

for bake in range(1, number_kozunakis + 1):
    best_player = False
    baker_name = input()
    points_count = 0

    while True:

        command = input()
        if command == "Stop":

            break
        command = int(command)
        points_count += command
        if points_count > max_points:
            max_points = points_count
            baker_max = baker_name
            best_player = True

    print(f"{baker_name} has {points_count} points.")
    if best_player:
        print(f"{baker_max} is the new number 1!")

print(f"{baker_max} won competition with {max_points} points!")

######## reshenie dve
easter_bread = int(input())

top_score = 0
best_chef = ''

for _ in range(easter_bread):
    new_best_baker = False
    score = 0
    name = input()

    while True:
        command = input()

        if command == 'Stop':
            break

        score += int(command)
        if score > top_score:
            top_score = score
            best_chef = name
            new_best_baker = True

    print(f'{name} has {score} points.')
    if new_best_baker:
        print(f'{best_chef} is the new number 1!')

print(f'{best_chef} won competition with {top_score} points!')