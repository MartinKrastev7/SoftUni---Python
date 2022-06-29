from collections import deque

elf_energies = deque([int(x) for x in input().split(" ")])
boxes = [int(x) for x in input().split(" ")]

turns_count = 0
total_energy_spent = 0
toys_count = 0

while boxes and elf_energies:

    while elf_energies and elf_energies[0] < 5:
        elf_energies.popleft()
    if not elf_energies:
        break

    box = boxes.pop()
    elf_energy = elf_energies.popleft()
    turns_count += 1

    toys_to_be_created_count = 1
    energy_to_be_spent = box
    energy_increased_factor = 1

    if turns_count % 3 == 0:
        toys_to_be_created_count = 2
        energy_to_be_spent *= 2

    if turns_count % 5 == 0:
        toys_to_be_created_count = 0
        energy_increased_factor = 0

    if energy_to_be_spent <= elf_energy:
        toys_count += toys_to_be_created_count
        total_energy_spent += energy_to_be_spent
        elf_energies.append(elf_energy - energy_to_be_spent + energy_increased_factor)
    else:
        boxes.append(box)
        elf_energies.append(elf_energy * 2)


print(f"Toys: {toys_count}")
print(f"Energy: {total_energy_spent}")
if elf_energies:
    print(f"Elves left: {', '.join([str(x) for x in elf_energies])}")
if boxes:
    print(f"Boxes left: {', '.join([str(x) for x in boxes])}")

#vtori nachin
elfs_energy = deque(int(x) for x in input().split())
materials_box = [int(x) for x in input().split()]
crafted_gifts = 0
elf_turns = 0
used_energy = 0
while elfs_energy and materials_box:

    elf = elfs_energy.popleft()

    if elf <= 4:
        continue

    elf_turns += 1
    current_toys = 0

    materials = materials_box.pop()

    if elf < materials:
        materials_box.append(materials)
        elfs_energy.append(elf * 2)
        continue
    if elf_turns % 3 == 0 and elf < materials * 2:
        materials_box.append(materials)
        elfs_energy.append(elf * 2)
        continue

    if elf_turns % 3 == 0 and elf >= materials * 2:
        current_toys += 2
        if elf_turns % 5 == 0:
            elf -= 1
        elf -= materials * 2 - 1
        used_energy += materials * 2

    if elf_turns % 3 != 0:
        current_toys += 1
        if elf_turns % 5 == 0:
            elf -= 1
        elf -= materials - 1
        used_energy += materials

    if elf_turns % 5 != 0:
        crafted_gifts += current_toys

    elfs_energy.append(elf)

print(f'Toys: {crafted_gifts}')
print(f'Energy: {used_energy}')
if elfs_energy:
    print(f'Elves left: {", ".join(str(x) for x in elfs_energy)}')
if materials_box:
    print(f'Boxes left: {", ".join(str(x) for x in materials_box)}')