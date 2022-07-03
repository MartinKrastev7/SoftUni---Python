from collections import deque

materials = [int(x) for x in input().split(" ")]
magic_levels = deque([int(x) for x in input().split(" ")])

made_gifts = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0
}

while materials and magic_levels:
    current_material = materials.pop()
    current_magic = magic_levels.popleft()
    sum_of_them = current_material + current_magic

    if sum_of_them < 100:
        if sum_of_them % 2 == 0:
            sum_of_them = 0
            current_material *= 2
            current_magic *= 3
            sum_of_them = current_material + current_magic
        else:
            sum_of_them *= 2

    elif sum_of_them > 499:
        sum_of_them /= 2

    if 100 <= sum_of_them <= 199:
        made_gifts["Gemstone"] += 1
    elif 200 <= sum_of_them <= 299:
        made_gifts["Porcelain Sculpture"] += 1
    elif 300 <= sum_of_them <= 399:
        made_gifts["Gold"] += 1
    elif 400 <= sum_of_them <= 499:
        made_gifts["Diamond Jewellery"] += 1

if made_gifts["Gemstone"] >= 1 and made_gifts["Porcelain Sculpture"] >= 1 or \
    made_gifts["Gold"] >= 1 and made_gifts["Diamond Jewellery"] >= 1:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials])}")
if magic_levels:
    print(f"Magic left: {', '.join([str(x) for x in magic_levels])}")

for key, value in sorted(made_gifts.items()):
    if value >= 1:
        print(f"{key}: {value}")