from collections import deque

bomb_effects = deque([int(x) for x in input().split(",")])
bomb_casing = [int(x) for x in input().split(",")]

bombs_dict = {
    40: "Datura Bombs",
    60: "Cherry Bombs",
    120: "Smoke Decoy Bombs"
}

made_bombs = {
    "Datura Bombs": 0,
    "Cherry Bombs": 0,
    "Smoke Decoy Bombs": 0
}

is_bomb_pouch = False

while bomb_casing and bomb_effects:
    if made_bombs["Datura Bombs"] >= 3 and made_bombs["Cherry Bombs"] >= 3 and made_bombs["Smoke Decoy Bombs"] >= 3:
        is_bomb_pouch = True
        break
    current_bomb_effect = bomb_effects.popleft()
    current_bomb_casing = bomb_casing.pop()
    sum_of_them = current_bomb_effect + current_bomb_casing

    if sum_of_them in bombs_dict:
        current_bomb = bombs_dict[sum_of_them]
        made_bombs[current_bomb] += 1

    else:
        current_bomb_casing -= 5
        bomb_effects.appendleft(current_bomb_effect)
        bomb_casing.append(current_bomb_casing)

if is_bomb_pouch:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effects])}")
else:
    print("Bomb Effects: empty")

if bomb_casing:
    print(f"Bomb Casings: {', '.join([str(x) for x in bomb_casing])}")
else:
    print("Bomb Casings: empty")

for key, value in sorted(made_bombs.items(), key=lambda x: x[0]):
    print(f"{key}: {value}")
