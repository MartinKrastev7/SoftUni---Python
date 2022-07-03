from collections import deque

elves_energies = deque([int(x) for x in input().split(" ")])
materials = [int(x) for x in input().split(" ")]

total_used_energy = 0
total_made_toys = 0
count = 0

while elves_energies and materials:
    while elves_energies and elves_energies[0] < 5:
        elves_energies.popleft()
    if not elves_energies:
        break

    current_energy = elves_energies.popleft()
    current_material = materials.pop()
    count += 1

    toys_to_be_created_count = 1
    energy_to_be_spent = current_material
    energy_increased_factor = 1 # cookie ate

    if count % 3 == 0:
        toys_to_be_created_count = 2
        energy_to_be_spent *= 2

    if count % 5 == 0:
        toys_to_be_created_count = 0
        energy_increased_factor = 0

    if current_energy >= energy_to_be_spent:
        total_made_toys += toys_to_be_created_count
        total_used_energy += energy_to_be_spent
        elves_energies.append(current_energy - energy_to_be_spent + energy_increased_factor)

    else:
        elves_energies.append(current_energy * 2)
        materials.append(current_material)

print(f"Toys: {total_made_toys}")
print(f"Energy: {total_used_energy}")
if elves_energies:
    print(f"Elves left: {', '.join([str(x) for x in elves_energies])}")
if materials:
    print(f"Boxes left: {', '.join([str(x) for x in materials])}")


#vtori nachin
elf_energy_deque = deque([int(el) for el in input().split()])
boxes_stack = [int(el) for el in input().split()]

toys = 0
energy = 0

counter_elves = 0

while elf_energy_deque and boxes_stack:

    while elf_energy_deque and elf_energy_deque[0] < 5:
        elf_energy_deque.popleft()

    if not elf_energy_deque:
        break

    current_elf = elf_energy_deque.popleft()
    current_box = boxes_stack.pop()

    counter_elves += 1

    if counter_elves % 3 == 0 and counter_elves % 5 == 0:

        if current_elf < current_box * 2:
            current_elf = current_elf * 2
            elf_energy_deque.append(current_elf)
            boxes_stack.append(current_box)

        elif current_elf >= current_box * 2:
            double_box = current_box * 2
            energy += double_box
            current_elf -= double_box
            elf_energy_deque.append(current_elf)

    elif counter_elves % 5 == 0:

        if current_elf < current_box:
            current_elf = current_elf * 2
            elf_energy_deque.append(current_elf)
            boxes_stack.append(current_box)

        elif current_elf >= current_box:
            energy += current_box
            current_elf -= current_box
            elf_energy_deque.append(current_elf)

    elif counter_elves % 3 == 0:

        if current_elf < current_box * 2:
            current_elf = current_elf * 2
            elf_energy_deque.append(current_elf)
            boxes_stack.append(current_box)

        elif current_elf >= current_box * 2:
            toys += 2
            double_box = current_box * 2
            energy += double_box
            current_elf -= double_box
            current_elf += 1
            elf_energy_deque.append(current_elf)

    else:

        if current_elf < current_box:
            current_elf = current_elf * 2
            elf_energy_deque.append(current_elf)
            boxes_stack.append(current_box)

        elif current_elf >= current_box:
            toys += 1
            energy += current_box
            current_elf -= current_box
            current_elf += 1
            elf_energy_deque.append(current_elf)

print(f"Toys: {toys}")
print(f"Energy: {energy}")

if elf_energy_deque:
    print(f"Elves left: {', '.join([str(el) for el in elf_energy_deque])}")

if boxes_stack:
    print(f"Boxes left: {', '.join([str(el) for el in boxes_stack])}")