from collections import deque

firework_effects = deque([int(x) for x in input().split(", ")])
explosive_power = [int(x) for x in input().split(", ")]
made_fireworks = {
    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0
}
is_made = False
while firework_effects and explosive_power:
    current_effect = firework_effects.popleft()
    current_power = explosive_power.pop()
    sum_of_them = current_effect + current_power

    if current_effect <= 0:
        explosive_power.append(current_power)
        continue
    elif current_power <= 0:
        firework_effects.appendleft(current_effect)
        continue

    if sum_of_them % 3 == 0 and sum_of_them % 5 != 0:
        made_fireworks["Palm Fireworks"] += 1
    elif sum_of_them % 5 == 0 and sum_of_them % 3 != 0:
        made_fireworks["Willow Fireworks"] += 1
    elif sum_of_them % 3 == 0 and sum_of_them % 5 == 0:
        made_fireworks["Crossette Fireworks"] += 1
    else:
        current_effect -= 1
        firework_effects.append(current_effect)
        explosive_power.append(current_power)

    if made_fireworks["Palm Fireworks"] >= 3 and made_fireworks["Willow Fireworks"] >= 3 \
            and made_fireworks["Crossette Fireworks"] >= 3:
        is_made = True
        break

if is_made:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join([str(x) for x in firework_effects])}")
if explosive_power:
    print(f"Explosive Power left: {', '.join([str(x)for x in explosive_power])}")

for key, value in made_fireworks.items():
    print(f"{key}: {value}")