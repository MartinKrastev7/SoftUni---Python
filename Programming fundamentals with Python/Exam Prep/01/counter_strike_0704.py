initial_energy = int(input())
command_distance = input()
is_out_energy = False
won_count = 0

while command_distance != "End of battle":
    distance = int(command_distance)
    if initial_energy < distance:
        print(f"Not enough energy! Game ends with {won_count} won battles and {initial_energy} energy")
        is_out_energy = True
        break
    initial_energy -= distance
    won_count += 1

    if won_count % 3 == 0:
        initial_energy += won_count

    command_distance = input()

if not is_out_energy:
    print(f"Won battles: {won_count}. Energy left: {initial_energy}")